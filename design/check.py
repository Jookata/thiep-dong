# -*- coding: utf-8 -*-
# Kiểm tra trước khi đưa lên GitHub: python3 design/check.py  (thoát mã 1 nếu có lỗi)
import os,re,subprocess,sys,json
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from cards import CARDS
D=os.path.join(R,'docs');err=[]
def bad(m):err.append(m);print('LỖI:',m)
for cid,cat in CARDS:
    d=os.path.join(D,cid)
    for f in ('index.html','texts.js','preview.jpg'):
        if not os.path.isfile(os.path.join(d,f)):bad('%s: thiếu %s'%(cid,f))
    if not os.path.isfile(os.path.join(R,'design','covers',cid+'.webp')):bad('%s: thiếu design/covers/%s.webp'%(cid,cid))
    p=os.path.join(d,'index.html')
    if not os.path.isfile(p):continue
    h=open(p,encoding='utf-8').read()
    # file nội bộ được nhắc tới phải tồn tại
    for m in set(re.findall(r"""(?:src=|href=|url\(|href:)['"]?((?:\.\./shared/|assets/)[A-Za-z0-9_./-]+\.[a-z0-9]{3,4})""",h)):
        if not os.path.isfile(os.path.normpath(os.path.join(d,m))):bad('%s: thiếu file %s'%(cid,m))
    for m in set(re.findall(r"""['"](assets/[A-Za-z0-9_./-]+\.(?:webp|png|jpg))['"]""",h)):
        if not os.path.isfile(os.path.join(d,m)):bad('%s: thiếu file %s'%(cid,m))
    # cú pháp JS
    sc=re.findall(r'<script>([\s\S]*?)</script>',h)
    if sc and __import__('shutil').which('node'):
        open('/tmp/_chk.js','w',encoding='utf-8').write(sc[-1])
        r=subprocess.run(['node','--check','/tmp/_chk.js'],capture_output=True,text=True)
        if r.returncode:bad('%s: JS lỗi cú pháp: %s'%(cid,r.stderr.strip()[:200]))
    # bản dịch đủ ngôn ngữ
    tp=os.path.join(d,'texts.js')
    if os.path.isfile(tp):
        t=json.loads(open(tp,encoding='utf-8').read().split('var TX=',1)[1].rstrip().rstrip(';'))
        if len(t)!=16:bad('%s: texts.js không đủ 16 ngôn ngữ'%cid)
        ks=[set(v) for v in t.values()]
        if any(k!=ks[0] for k in ks):bad('%s: các ngôn ngữ lệch khóa'%cid)
    if '<title>' not in h or 'og:image' not in h:bad('%s: thiếu <title> hoặc og:image'%cid)
print('Đã kiểm tra %d thiệp: %s'%(len(CARDS),'CÓ LỖI' if err else 'ổn'))
sys.exit(1 if err else 0)
