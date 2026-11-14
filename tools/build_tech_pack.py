"""Build the additive tech pack and complete player ZIP from reviewed repository sources."""
from pathlib import Path
import argparse,hashlib,json,zipfile,shutil

def write_zip(target,files):
 target.parent.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for name,p in sorted(files):
   info=zipfile.ZipInfo(name,(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16;z.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
 with zipfile.ZipFile(target) as z:
  bad=z.testzip()
  if bad:raise RuntimeError('Corrupt ZIP entry '+bad)
 return hashlib.sha256(target.read_bytes()).hexdigest()

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--release-dir',type=Path);a=ap.parse_args();repo=a.repo.resolve();src=repo/'translation-src/tech';release=a.release_dir or repo/'release';release.mkdir(parents=True,exist_ok=True)
 files=[(p.relative_to(src).as_posix(),p) for p in src.rglob('*') if p.is_file()]
 assert files and (src/'pack.mcmeta').exists()
 pack='ZZZ_Prominence_II_Thai_Tech.zip';rp=repo/'resourcepacks'/pack;sha=write_zip(rp,files)
 paxi=repo/'config/paxi/resourcepacks'/pack;paxi.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(rp,paxi)
 overlay=[('resourcepacks/'+pack,rp),('config/paxi/resourcepacks/'+pack,paxi)]
 for rel in ['config/fancymenu/assets/tips.txt','config/fancymenu/customization/Esc Menu.txt','config/fancymenu/customization/LoadingScreen.txt','วิธีลงส่วนเสริมม็อดเทค.txt']:
  overlay.append((rel,repo/rel))
 addon=release/'Prominence_II_Thai_Tech_Addon.zip';addsha=write_zip(addon,overlay)
 full=[]
 for dirname in ['config','mods','resourcepacks']:
  full.extend((p.relative_to(repo).as_posix(),p) for p in (repo/dirname).rglob('*') if p.is_file())
 for rel in ['README.md','วิธีลงภาษาไทย.txt','วิธีติดตั้งสำหรับเช่าโฮสต์_Server.txt','วิธีลงส่วนเสริมม็อดเทค.txt']:
  p=repo/rel
  if p.exists():full.append((rel,p))
 friend=repo/'Prominence_II_Thai_Pack_For_Friends.zip';fullsha=write_zip(friend,full);shutil.copy2(friend,release/friend.name)
 result={'resourcepack_sha256':sha,'addon_sha256':addsha,'full_sha256':fullsha,'resourcepack_files':len(files),'full_files':len(full),'zip_crc_checked':True}
 (repo/'translation-review/tech/package-hashes.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
