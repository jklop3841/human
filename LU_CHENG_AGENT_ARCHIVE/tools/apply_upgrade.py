"""Apply this exact upgrade around the SHA-pinned v0.4 ZIP into an empty output directory."""
import argparse
import shutil
import zipfile
from pathlib import Path, PurePosixPath
from archive import validate
from migrate import ROOT, digest, json_text, read_json

def apply(source_zip, output):
    source_zip=Path(source_zip).resolve();output=Path(output).resolve()
    lock=read_json(ROOT/'migration/FREEZE.json')
    if digest(source_zip.read_bytes())!=lock['source_zip_sha256']:
        raise ValueError('Input ZIP differs from the pinned completed v0.4 handoff')
    if output==ROOT or output.is_relative_to(ROOT) or ROOT.is_relative_to(output):
        raise ValueError('Output must be separate from the patch directory')
    if output.exists() and any(output.iterdir()): raise ValueError('Output must be empty; no overwrite')
    data={}
    with zipfile.ZipFile(source_zip) as z:
        for info in z.infolist():
            if info.is_dir():continue
            p=PurePosixPath(info.filename)
            if p.is_absolute() or '..' in p.parts or p.parts[0]!='Agent_Atlas_v0.4': raise ValueError('Unexpected ZIP path')
            rel=PurePosixPath(*p.parts[1:]).as_posix()
            if rel in data: raise ValueError('Duplicate ZIP path')
            data[rel]=z.read(info)
    if set(data)!=set(lock['files']): raise ValueError('Frozen file set mismatch')
    if any(digest(data[p])!=h for p,h in lock['files'].items()): raise ValueError('Frozen content mismatch')
    shutil.copytree(ROOT,output,dirs_exist_ok=True,ignore=shutil.ignore_patterns('baseline_v0.4','__pycache__','*.pyc','work_runs'))
    for rel,content in data.items():
        p=output/lock['baseline_path']/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(content)
    report=validate(output)
    if report['errors']: raise ValueError('Applied archive failed validation: '+str(report['errors']))
    return {'status':'APPLIED_AND_VALIDATED','output':str(output),'frozen_files':len(data),'original_files_modified':0}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--atlas-zip',required=True);p.add_argument('--out',required=True);args=p.parse_args()
    try:print(json_text(apply(args.atlas_zip,args.out)))
    except ValueError as exc:p.exit(1,str(exc)+'\n')
