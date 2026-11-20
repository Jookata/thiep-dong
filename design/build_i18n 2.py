# -*- coding: utf-8 -*-
# Sinh docs/i18n.js, docs/<mẫu>/texts.js (noel, santa, catch, flappy, birthday) từ i18n_src_a/b/d/e/f.py; giao diện app từ i18n_src_c.py
import json,os,sys
sys.path.insert(0,os.path.dirname(__file__))
from i18n_src_a import *
from i18n_src_b import *
from i18n_src_c import *
from i18n_src_d import *
from i18n_src_e import *
from i18n_src_f import *
from i18n_src_g import *
from i18n_src_h import *
from i18n_src_i import NEWYEAR,YK2,TPL_NEWYEAR
from i18n_src_j import KOREA,KK,TPL_KOREA
from i18n_src_tpl import TPL
TPL['yuki']=TPL_YUKI
TPL['nen']=TPL_NEN
TPL['newyear']=TPL_NEWYEAR
TPL['korea']=TPL_KOREA
# chèn tên/mô tả mẫu thiệp (mẫu 3 trở đi) vào chuỗi giao diện app, ngay sau các tpl_* có sẵn
for _id,_tx in TPL.items():
    _j=max(i for i,k in enumerate(AK) if k.startswith('tpl_'))+1
    AK.insert(_j,'tpl_%s_title'%_id);AK.insert(_j+1,'tpl_%s_desc'%_id)
    for L in LANGS:
        APP[L].insert(_j,_tx[L][0]);APP[L].insert(_j+1,_tx[L][1])
D=os.path.join(os.path.dirname(__file__),'..','docs')
for L in LANGS:
    assert len(COMMON[L])==len(CK),(L,'common')
    assert len(NOEL[L])==len(NK),(L,'noel',len(NOEL[L]))
    assert len(SANTA[L])==len(SK),(L,'santa',len(SANTA[L]))
    assert len(CATCH[L])==len(DK),(L,'catch',len(CATCH[L]))
    assert len(FLAPPY[L])==len(FK),(L,'flappy',len(FLAPPY[L]))
    assert len(BDAY[L])==len(BK),(L,'birthday',len(BDAY[L]))
    assert len(YUKI[L])==len(YK),(L,'yuki',len(YUKI[L]))
    assert len(NEN[L])==len(EK),(L,'nen',len(NEN[L]))
    assert len(NEWYEAR[L])==len(YK2),(L,'newyear',len(NEWYEAR[L]))
    assert len(KOREA[L])==len(KK),(L,'korea',len(KOREA[L]))
def dump(o):return json.dumps(o,ensure_ascii=False,separators=(',',':'))
common={L:dict(zip(CK,COMMON[L])) for L in LANGS}
shared="""/* WinkCard: dùng chung cho mọi mẫu thiệp. FILE SINH TỰ ĐỘNG từ design/build_i18n.py, đừng sửa tay. */
var WC={
LANGS:%s,
NATIVE:%s,
COMMON:%s,
KEY:'w1nk-c4rd-2026',
/* mã ngôn ngữ trong link -> mã chuẩn (zh = giản thể, zh-TW = phồn thể) */
norm:function(s){s=String(s||'').toLowerCase().replace('_','-');
  if(s.indexOf('zh')===0)return /tw|hant|hk|mo/.test(s)?'zh-TW':'zh';
  s=s.slice(0,2);return this.LANGS.indexOf(s)>=0?s:''},
/* lời chúc riêng: base64url(XOR(UTF-8, KEY)) */
dec:function(m){try{m=String(m).replace(/-/g,'+').replace(/_/g,'/');while(m.length%%4)m+='=';
  var b=atob(m),a=new Uint8Array(b.length),k=this.KEY;
  for(var i=0;i<b.length;i++)a[i]=b.charCodeAt(i)^k.charCodeAt(i%%k.length);
  return new TextDecoder('utf-8').decode(a)}catch(e){return ''}},
enc:function(s){var u=new TextEncoder().encode(s),k=this.KEY,o='';
  for(var i=0;i<u.length;i++)o+=String.fromCharCode(u[i]^k.charCodeAt(i%%k.length));
  return btoa(o).replace(/\\+/g,'-').replace(/\\//g,'_').replace(/=+$/,'')},
/* ghép bảng chữ: chung + riêng từng mẫu */
build:function(TX){var T={};for(var i=0;i<this.LANGS.size;i++){}
  for(var j=0;j<this.LANGS.length;j++){var L=this.LANGS[j];T[L]=Object.assign({},this.COMMON[L],TX[L]||{})}
  return T}
};
"""%(dump(LANGS),dump(NATIVE),dump(common))
shared=shared.replace("for(var i=0;i<this.LANGS.size;i++){}\n","")
open(os.path.join(D,'i18n.js'),'w',encoding='utf-8').write(shared)
for name,keys,data in (('noel',NK,NOEL),('santa',SK,SANTA),('catch',DK,CATCH),('flappy',FK,FLAPPY),('birthday',BK,BDAY),('yuki',YK,YUKI),('nen',EK,NEN),('newyear',YK2,NEWYEAR),('korea',KK,KOREA)):
    tx={L:dict(zip(keys,data[L])) for L in LANGS}
    open(os.path.join(D,name,'texts.js'),'w',encoding='utf-8').write('/* FILE SINH TỰ ĐỘNG từ design/build_i18n.py */\nvar TX='+dump(tx)+';\n')
print('ok')

# ---- Android: strings.xml cho từng ngôn ngữ + Lang.java ----
A=os.path.join(os.path.dirname(__file__),'..','android','app','src','main')
def esc(t):
    t=t.replace('&','&amp;').replace('<','&lt;').replace("'","\\'").replace('"','\\"')
    if t.startswith('@') or t.startswith('?'): t='\\'+t
    return t
import shutil
for d in os.listdir(os.path.join(A,'res')):
    if d.startswith('values-en'): shutil.rmtree(os.path.join(A,'res',d))
for L in LANGS:
    assert len(APP[L])==len(AK),(L,'app')
    d=os.path.join(A,'res',FOLDER[L]);os.makedirs(d,exist_ok=True)
    lines=['<?xml version="1.0" encoding="utf-8"?>','<resources>','    <string name="app_name">WinkCard</string>' if L=='en' else '    <!-- app_name lấy từ values/strings.xml -->']
    for k,v in zip(AK,APP[L]): lines.append('    <string name="%s">%s</string>'%(k,esc(v)))
    lines.append('</resources>')
    # giữ lại các chuỗi cố định của values/ (create_title... đã nằm trong AK); thêm các chuỗi khác
    open(os.path.join(d,'strings.xml'),'w',encoding='utf-8').write('\n'.join(lines)+'\n')
j=['package com.jookata.thiepdong;','','/** FILE SINH TỰ ĐỘNG từ design/build_i18n.py. Danh sách ngôn ngữ của thiệp. */','final class Lang {','    final String code;','    final String name;','    final String intro;','','    Lang(String code, String name, String intro) {','        this.code = code;','        this.name = name;','        this.intro = intro;','    }','','    static final Lang[] ALL = {']
for L in LANGS:
    j.append('            new Lang("%s", "%s", "%s"),'%(L,NATIVE[L],INTRO[L].replace('"','\\"')))
j+=['    };','','    /** Chọn ngôn ngữ thiệp mặc định theo ngôn ngữ của máy. */','    static int defaultIndex(java.util.Locale loc) {','        String l = loc.getLanguage();','        String c = l;','        if ("zh".equals(l)) {','            String r = loc.getCountry();','            c = ("TW".equals(r) || "HK".equals(r) || "MO".equals(r) || "Hant".equals(loc.getScript())) ? "zh-TW" : "zh";','        }','        for (int i = 0; i < ALL.length; i++) if (ALL[i].code.equals(c)) return i;','        return 1; // English','    }','','}','']
open(os.path.join(A,'java','com','jookata','thiepdong','Lang.java'),'w',encoding='utf-8').write('\n'.join(j))
print('android ok')

# ---- Android: Templates.ALL + ảnh bìa, sinh từ design/cards.py ----
from cards import CARDS
_here=os.path.dirname(__file__)
_ids=[i for i,_ in CARDS]
for _id,_c in CARDS:
    assert os.path.isfile(os.path.join(_here,'covers',_id+'.webp')),('thiếu ảnh bìa design/covers/%s.webp'%_id)
    assert _id in ('noel','santa') or _id in TPL,('thiếu tên/mô tả (TPL) cho '+_id)
    shutil.copyfile(os.path.join(_here,'covers',_id+'.webp'),os.path.join(A,'res','drawable-nodpi','cover_%s.webp'%_id))
for f in os.listdir(os.path.join(A,'res','drawable-nodpi')):
    if f.startswith('cover_') and f[6:-5] not in _ids: os.remove(os.path.join(A,'res','drawable-nodpi',f))
_tp=os.path.join(A,'java','com','jookata','thiepdong','Templates.java')
_s=open(_tp,encoding='utf-8').read()
_a=_s.index('// BEGIN-GEN');_a=_s.index('\n',_a)+1;_z=_s.index('            // END-GEN')
_rows=',\n'.join('            new Template("%s", "%s", "%s", R.string.tpl_%s_title, R.string.tpl_%s_desc, R.drawable.cover_%s)'%(i,i,c,i,i,i) for i,c in CARDS)+'\n'
open(_tp,'w',encoding='utf-8').write(_s[:_a]+_rows+_s[_z:])
print('templates ok:',', '.join(_ids))
