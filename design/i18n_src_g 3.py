# -*- coding: utf-8 -*-
# Nguồn bản dịch: mẫu 6 "yuki" (Giáng sinh Nhật Bản, lật trang + tuyết) và tiêu đề có tên người nhận cho mẫu Noel.
# Dòng chào trên bìa lấy lại từ Noel ("fin": Giáng sinh an lành, {to}!).
from i18n_src_a import NOEL,NK,LANGS
_TT={
'vi':'{to} có một tấm thiệp Noel','en':'{to}, you have a Christmas card','fr':'{to}, vous avez une carte de Noël','de':'{to}, du hast eine Weihnachtskarte',
'it':'{to}, hai un biglietto di Natale','pl':'{to}, masz kartkę świąteczną','fi':'{to}, sinulle on joulukortti','es':'{to}, tienes una tarjeta de Navidad',
'pt':'{to}, você tem um cartão de Natal','sk':'{to}, máš vianočnú pohľadnicu','ko':'{to}님, 크리스마스 카드가 도착했어요','ja':'{to}さん、クリスマスカードが届いています',
'zh':'{to}，你收到一张圣诞贺卡','zh-TW':'{to}，你收到一張聖誕賀卡','th':'{to} คุณมีการ์ดคริสต์มาส','ms':'{to}, anda ada kad Krismas'}
NK.append('titleTo')
for _L in LANGS: NOEL[_L].append(_TT[_L])
YK=['title','titleTo','fin','hint']
_Y={
'vi':('Một tấm thiệp Giáng sinh','{to} có một tấm thiệp Giáng sinh'),
'en':('A Christmas card','{to}, you have a Christmas card'),
'fr':('Une carte de Noël','{to}, vous avez une carte de Noël'),
'de':('Eine Weihnachtskarte','{to}, du hast eine Weihnachtskarte'),
'it':('Un biglietto di Natale','{to}, hai un biglietto di Natale'),
'pl':('Kartka świąteczna','{to}, masz kartkę świąteczną'),
'fi':('Joulukortti','{to}, sinulle on joulukortti'),
'es':('Una tarjeta de Navidad','{to}, tienes una tarjeta de Navidad'),
'pt':('Um cartão de Natal','{to}, você tem um cartão de Natal'),
'sk':('Vianočná pohľadnica','{to}, máš vianočnú pohľadnicu'),
'ko':('크리스마스 카드','{to}님, 크리스마스 카드가 도착했어요'),
'ja':('クリスマスカード','{to}さん、クリスマスカードが届いています'),
'zh':('一张圣诞贺卡','{to}，你收到一张圣诞贺卡'),
'zh-TW':('一張聖誕賀卡','{to}，你收到一張聖誕賀卡'),
'th':('การ์ดคริสต์มาส','{to} คุณมีการ์ดคริสต์มาส'),
'ms':('Kad Krismas','{to}, anda ada kad Krismas')}
_H={'vi':'Hãy mở thiệp ra, {to} ơi','en':'Please open the card, {to}','fr':'Ouvre la carte, {to}','de':'Öffne die Karte, {to}','it':'Apri il biglietto, {to}','pl':'Otwórz kartkę, {to}','fi':'Avaa kortti, {to}','es':'Abre la tarjeta, {to}','pt':'Abra o cartão, {to}','sk':'Otvor pohľadnicu, {to}','ko':'{to}님, 카드를 열어 보세요','ja':'{to}さん、カードを開いてね','zh':'{to}，请打开贺卡吧','zh-TW':'{to}，請打開賀卡吧','th':'{to} เปิดการ์ดสิ','ms':'{to}, sila buka kad ini'}
YUKI={L:[_Y[L][0],_Y[L][1],NOEL[L][NK.index('fin')],_H[L]] for L in LANGS}
TPL_YUKI={
'vi':('Giáng sinh Nhật Bản','Lật trang thiệp, tuyết rơi trên khung cảnh Nhật Bản yên bình cùng lời chúc.'),
'en':('Japanese Snow Christmas','Turn the page to a quiet snowy Japanese scene with your wishes.'),
'fr':('Noël neigeux au Japon','Tournez la page : une paisible scène japonaise sous la neige et vos vœux.'),
'de':('Weihnachten im Schnee, Japan','Blättere um: eine ruhige verschneite Szene in Japan mit deinen Wünschen.'),
'it':('Natale nevoso in Giappone','Gira la pagina: una quieta scena giapponese sotto la neve con i tuoi auguri.'),
'pl':('Śnieżne święta w Japonii','Odwróć kartkę: spokojna, zaśnieżona japońska scena i twoje życzenia.'),
'fi':('Lumisen Japanin joulu','Käännä sivua: hiljainen lumimaisema Japanissa ja toivotuksesi.'),
'es':('Navidad nevada en Japón','Pasa la página: una tranquila escena japonesa bajo la nieve con tus deseos.'),
'pt':('Natal com neve no Japão','Vire a página: uma cena japonesa tranquila sob a neve com seus votos.'),
'sk':('Snežné Vianoce v Japonsku','Otoč stranu: pokojná zasnežená japonská scéna a tvoje priania.'),
'ko':('일본풍 눈 내리는 크리스마스','페이지를 넘기면 고요한 눈 내리는 일본 풍경과 함께 인사가 나타나요.'),
'ja':('雪の和風クリスマス','ページをめくると、静かな雪の日本の景色とメッセージが現れます。'),
'zh':('日式雪景圣诞','翻开一页，静谧的日式雪景与你的祝福一同出现。'),
'zh-TW':('日式雪景聖誕','翻開一頁，靜謐的日式雪景與你的祝福一同出現。'),
'th':('คริสต์มาสหิมะแบบญี่ปุ่น','เปิดหน้าการ์ดพบฉากหิมะญี่ปุ่นแสนสงบพร้อมคำอวยพร'),
'ms':('Krismas Salji Jepun','Selak halaman untuk melihat pemandangan salji Jepun yang tenang dengan ucapan anda.')}
