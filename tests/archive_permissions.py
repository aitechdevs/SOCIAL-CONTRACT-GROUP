"""Release archives must be usable by cPanel's static-file server."""
from pathlib import Path
import zipfile,stat
count=0
for path in Path('releases').glob('*.zip'):
 with zipfile.ZipFile(path) as archive:
  assert archive.testzip() is None,path
  names=set(archive.namelist())
  for entry in archive.infolist():
   mode=entry.external_attr>>16
   assert stat.S_IMODE(mode)==(0o755 if entry.is_dir() else 0o644),(path,entry.filename,oct(mode))
   assert not entry.filename.endswith('local.php'),path
   if not entry.is_dir():
    parent=Path(entry.filename).parent.as_posix()
    if parent!='.':assert parent+'/' in names,(path,entry.filename,'missing directory entry')
  count+=1
print('PASS:',count,'ZIPs: integrity, private config exclusion, 644 files and explicit 755 directories')
