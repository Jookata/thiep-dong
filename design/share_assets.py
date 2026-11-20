# -*- coding: utf-8 -*-
"""Gom hình trùng nhau giữa các mẫu thiệp vào docs/shared/.
Chạy:  python3 design/share_assets.py          (chỉ báo cáo, không đổi gì)
       python3 design/share_assets.py --apply  (chuyển file + sửa đường dẫn trong index.html)
Quy tắc: hai file được coi là một khi NỘI DUNG giống hệt (băm md5), dù khác tên. Hình riêng của từng mẫu (nền, ảnh bìa) giữ nguyên.
Nhớ sao lưu thư mục docs/ trước khi --apply. Mẫu nào ghép tên hình bằng code ('assets/'+tên+số) thì giữ nguyên bản chép riêng.
"""
import os,sys,hashlib,re,shutil
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','docs')
apply='--apply' in sys.argv
SH=os.path.join(D,'shared');os.makedirs(SH,exist_ok=True)
groups={}
for t in sorted(os.listdir(D)):
    a=os.path.join(D,t,'assets')
    if t=='shared' or not os.path.isdir(a):continue
    for f in sorted(os.listdir(a)):
        h=hashlib.md5(open(os.path.join(a,f),'rb').read()).hexdigest()
        groups.setdefault(h,[]).append((t,f))
# file đã có sẵn trong shared cũng tính vào nhóm
for f in os.listdir(SH):
    h=hashlib.md5(open(os.path.join(SH,f),'rb').read()).hexdigest()
    groups.setdefault(h,[]).insert(0,('shared',f))
used={}
total=0
for h,items in groups.items():
    ns=[i for i in items if i[0]!='shared']
    if not ns or (len(items)<2):continue
    name=next((f for t,f in items if t=='shared'),items[0][1])
    if name in used and used[name]!=h:name=name.rsplit('.',1)[0]+'_'+h[:6]+'.'+name.rsplit('.',1)[1]
    used[name]=h
    print('%-26s <- %s'%(name,', '.join('%s/%s'%i for i in items)))
    if not apply:continue
    dst=os.path.join(SH,name)
    if not os.path.exists(dst):shutil.copy(os.path.join(D,items[0][0],'assets',items[0][1]) if items[0][0]!='shared' else os.path.join(SH,items[0][1]),dst)
    for t,f in ns:
        p=os.path.join(D,t,'index.html');s=open(p,encoding='utf-8').read()
        if re.search(r"'assets/'\s*\+",s) and re.search(r'\d\.\w+$',f):print('  (bỏ qua %s/%s: mẫu ghép tên hình bằng code)'%(t,f));continue
        s2=re.sub(r"(?<![\w/.])assets/"+re.escape(f)+r"(?![\w.])",'../shared/'+name,s)
        if s2!=s:open(p,'w',encoding='utf-8').write(s2)
        os.remove(os.path.join(D,t,'assets',f))
    total+=1
print('\n%d nhóm hình trùng.'%sum(1 for h,i in groups.items() if len(i)>1 and any(x[0]!='shared' for x in i)),'Đã áp dụng.' if apply else 'Chưa đổi gì (thêm --apply để áp dụng).')
