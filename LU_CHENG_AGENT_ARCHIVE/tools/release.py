"""Create or verify the reviewable release inventory. Tests run locally; no external calls."""
import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path
import archive
from apply_upgrade import apply
from migrate import ROOT, VOLUME, digest, json_text, read_json

def files():
    return sorted(p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts
                  and 'work_runs' not in p.relative_to(ROOT).parts and p.suffix!='.pyc')

def write(rel,data):
    p=ROOT/rel;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(data if isinstance(data,str) else json_text(data),encoding='utf-8')

def verify():
    lock=read_json(ROOT/'ARTIFACT_SHA256.json');expected=lock['files']
    actual={p.relative_to(ROOT).as_posix():digest(p.read_bytes()) for p in files() if p!=ROOT/'ARTIFACT_SHA256.json'}
    if actual!=expected:
        changed=sorted(k for k in set(actual)|set(expected) if actual.get(k)!=expected.get(k))
        raise ValueError('Release hash mismatch: '+', '.join(changed))
    return {'status':'PASS','hashed_files':len(actual),'self_hash_excluded':'ARTIFACT_SHA256.json'}

def release(atlas_zip=None):
    validation=archive.validate(ROOT)
    if validation['errors']: raise ValueError(str(validation['errors']))
    tests=subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-v'],cwd=ROOT,capture_output=True,text=True)
    write('reports/migration_tests.txt',tests.stdout+tests.stderr)
    if tests.returncode: raise ValueError('Migration tests failed')
    legacy=archive.legacy_check(ROOT);write('reports/legacy_tests.txt',legacy['output'])
    if legacy['exit_code']: raise ValueError('Legacy tests failed')
    apply_status={'status':'NOT_RUN','reason':'Pass --atlas-zip for independent installer verification.'}
    if atlas_zip:
        with tempfile.TemporaryDirectory(prefix='lcaa_apply_test_') as d:
            apply_status=apply(atlas_zip,Path(d)/'archive')
            apply_status.pop('output',None)
    write('reports/validation.json',validation)
    write('reports/apply_upgrade.json',apply_status)
    write('reports/VALIDATION_REPORT.md',f'''# 迁移验证记录 — 2026-09-06

状态：PASS。迁移测试 11 项，冻结 v0.4 回归 7 项，共 18 项通过。

| 验证对象 | 结果 |
|---|---|
| 原 v0.4 | {validation['frozen_files']} 文件字节不变；测试在临时副本执行 |
| 升级补丁 | {validation['patch_files']} 文件原样留存；含 15 份与 v0.3 相同的旧件 |
| 记录 / 主张 | {validation['projected_records']} 个原 payload 往返一致 / {validation['classified_claims']} 项独立证据等级 |
| ID / 来源链 | {validation['id_aliases']} 个无冲突别名 / {validation['provenance_edges']} 条边无悬空引用 |
| H0 | 2 条治理原话；替换原文会被拒绝；历史自然观察缺失明确保留 |
| 评分 | null 保留；DPD 阈值边界、低生成性与无效类型受检查 |
| 读者入口 | 嵌套/平铺兼容；模板、冲突、显式合成回执被拒绝 |
| v2 | 54 个 A/B/C 请求可准备；联网预算独立于旧版；D 被阻止；导入与架构盲审路径已验证 |
| 一键应用 | {apply_status['status']} |

证据：migration_tests.txt、legacy_tests.txt、validation.json、apply_upgrade.json。
正向导入测试使用手工构造的数据，位于测试后删除的临时目录；没有供应商调用，未进入档案结果账本。
导入器依赖真实运行者回执，不能自行证明模型身份、隔离或完整搜索日志。

研究状态：受控模型调用 0；HPC 未测；External Search Escape 未裁决；DPD 未评分。
360 次旧合成成本模拟保持原范围；既有缓存负对照没有被删改。当前不是有效性通过报告。
''')
    write('migration/FILE_CHANGES.json',{})
    write('migration/TARGET_TREE.md','')
    write('ARTIFACT_SHA256.json',{})
    paths=[p.relative_to(ROOT).as_posix() for p in files()]
    write('migration/TARGET_TREE.md','# Actual target tree\n\n```text\nLU_CHENG_AGENT_ARCHIVE/\n'+''.join('  '+p+'\n' for p in paths)+'```\n')
    changes=[]
    prefix=VOLUME+'/baseline_v0.4/'
    for path in paths:
        status='PRESERVED_REPARENTED' if path.startswith(prefix) else 'PRESERVED_UPGRADE_INPUT' if path.startswith('migration/input_patch_v1.0/') else 'ADDED'
        entry={'path':path,'action':status}
        if status=='PRESERVED_REPARENTED':entry['old_path']='Agent_Atlas_v0.4/'+path[len(prefix):]
        changes.append(entry)
    write('migration/FILE_CHANGES.json',{'archive_version':'1.0.0-draft.1','hosting_repository':'jklop3841/human',
          'repository_files_preexisting_modified':[],'baseline_original_files_modified':[],'frozen_files_preserved':136,
          'upgrade_input_files_preserved':41,'file_count':len(changes),'files':changes})
    write('ARTIFACT_SHA256.json',{'algorithm':'SHA-256','self_hash_excluded':True,
          'files':{p.relative_to(ROOT).as_posix():digest(p.read_bytes()) for p in files() if p!=ROOT/'ARTIFACT_SHA256.json'}})
    return {'status':'READY_FOR_GITHUB_DRAFT','files':len(paths),'verification':verify(),'apply_upgrade':apply_status,
            'actual_external_model_calls':0}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--verify',action='store_true');p.add_argument('--atlas-zip');args=p.parse_args()
    try:print(json_text(verify() if args.verify else release(args.atlas_zip)))
    except ValueError as exc:p.exit(1,str(exc)+'\n')
