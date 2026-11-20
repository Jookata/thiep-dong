# -*- coding: utf-8 -*-
# DANH SÁCH THIỆP: nguồn duy nhất. Thêm thiệp mới = thêm 1 dòng ở đây + thư mục docs/<id>/ + ảnh bìa design/covers/<id>.webp
# + bản dịch tên/mô tả trong i18n_src_tpl (TPL). Sau đó chạy: python3 design/build_i18n.py
# Android (Templates.java + ảnh bìa) và các file ngôn ngữ đều được sinh tự động từ đây.
# (id, nhóm)  – nhóm: xmas | birthday | newyear (thêm nhóm mới trong Templates.java + cat_* ở i18n_src_c.py)
CARDS=[
 ('noel','xmas'),
 ('santa','xmas'),
 ('catch','xmas'),
 ('flappy','xmas'),
 ('yuki','xmas'),
 ('korea','xmas'),
 ('birthday','birthday'),
 ('nen','birthday'),
 ('newyear','newyear'),
]
