# -*- coding: utf-8 -*-
# Nguồn bản dịch: mẫu 8 "newyear" (Chúc mừng năm mới: bìa, lật trang, chạm đồng hồ, pháo hoa). hint lấy từ mẫu yuki.
import i18n_src_g as G
from i18n_src_a import LANGS
_N={
'vi':('Một tấm thiệp chúc mừng năm mới','{to} có một tấm thiệp chúc mừng năm mới'),'en':('A New Year card','{to}, you have a New Year card'),
'fr':('Une carte de nouvel an','{to}, vous avez une carte de nouvel an'),'de':('Eine Neujahrskarte','{to}, du hast eine Neujahrskarte'),
'it':('Un biglietto di Capodanno','{to}, hai un biglietto di Capodanno'),'pl':('Kartka noworoczna','{to}, masz kartkę noworoczną'),
'fi':('Uudenvuoden kortti','{to}, sinulle on uudenvuoden kortti'),'es':('Una tarjeta de Año Nuevo','{to}, tienes una tarjeta de Año Nuevo'),
'pt':('Um cartão de Ano Novo','{to}, você tem um cartão de Ano Novo'),'sk':('Novoročná pohľadnica','{to}, máš novoročnú pohľadnicu'),
'ko':('새해 카드','{to}님, 새해 카드가 도착했어요'),'ja':('新年のカード','{to}さん、新年のカードが届いています'),
'zh':('一张新年贺卡','{to}，你收到一张新年贺卡'),'zh-TW':('一張新年賀卡','{to}，你收到一張新年賀卡'),
'th':('การ์ดปีใหม่','{to} คุณมีการ์ดปีใหม่'),'ms':('Kad Tahun Baru','{to}, anda ada kad Tahun Baru')}
_HB={'vi':'Chúc mừng năm mới,','en':'Happy New Year,','fr':'Bonne année,','de':'Frohes neues Jahr,','it':'Buon anno,','pl':'Szczęśliwego Nowego Roku,','fi':'Hyvää uutta vuotta,','es':'Feliz Año Nuevo,','pt':'Feliz Ano Novo,','sk':'Šťastný nový rok,','ko':'새해 복 많이 받으세요,','ja':'ハッピーニューイヤー、','zh':'新年快乐，','zh-TW':'新年快樂，','th':'สวัสดีปีใหม่ ','ms':'Selamat Tahun Baru,'}
_TAP={'vi':'Đồng hồ sắp điểm 12 giờ… hãy chạm vào đồng hồ nhé!','en':'Midnight is near… touch the clock!','fr':'Minuit approche… touche l’horloge !','de':'Mitternacht naht … tippe auf die Uhr!','it':'Mezzanotte si avvicina… tocca l’orologio!','pl':'Zbliża się północ… dotknij zegara!','fi':'Keskiyö lähestyy… kosketa kelloa!','es':'Se acerca la medianoche… ¡toca el reloj!','pt':'A meia-noite se aproxima… toque no relógio!','sk':'Blíži sa polnoc… dotkni sa hodín!','ko':'자정이 다가와요… 시계를 터치해 보세요!','ja':'真夜中が近づいています… 時計にさわってね！','zh':'午夜将至……点一下时钟吧！','zh-TW':'午夜將至……點一下時鐘吧！','th':'ใกล้เที่ยงคืนแล้ว… แตะที่นาฬิกาสิ!','ms':'Tengah malam hampir tiba… sentuh jam itu!'}
YK2=['title','titleTo','hint','hb','tap']
NEWYEAR={L:[_N[L][0],_N[L][1],G._H[L],_HB[L],_TAP[L]] for L in LANGS}
TPL_NEWYEAR={
'vi':('Chào năm mới','Chạm vào đồng hồ điểm 12 giờ, pháo hoa bắn lên và lời chúc năm mới hiện ra.'),
'en':('New Year Midnight','Touch the clock at midnight: fireworks burst and your New Year wishes appear.'),
'fr':('Minuit du Nouvel An','Touchez l’horloge à minuit : feux d’artifice et vœux de nouvel an.'),
'de':('Neujahrs-Mitternacht','Tippe um Mitternacht auf die Uhr: Feuerwerk und Neujahrswünsche erscheinen.'),
'it':('Mezzanotte di Capodanno','Tocca l’orologio a mezzanotte: fuochi d’artificio e auguri di buon anno.'),
'pl':('Sylwestrowa północ','Dotknij zegara o północy: pojawią się fajerwerki i życzenia noworoczne.'),
'fi':('Uudenvuoden keskiyö','Kosketa kelloa keskiyöllä: ilotulitus ja uudenvuoden toivotukset ilmestyvät.'),
'es':('Medianoche de Año Nuevo','Toca el reloj a medianoche: fuegos artificiales y tus deseos de Año Nuevo.'),
'pt':('Meia-noite de Ano Novo','Toque no relógio à meia-noite: fogos de artifício e votos de Ano Novo.'),
'sk':('Silvestrovská polnoc','Dotkni sa hodín o polnoci: objavia sa ohňostroj a novoročné priania.'),
'ko':('새해 자정','자정의 시계를 터치하면 불꽃놀이와 새해 인사가 나타나요.'),
'ja':('新年のカウントダウン','真夜中の時計にさわると、花火とお祝いのメッセージが現れます。'),
'zh':('新年零点','点一下零点的时钟，烟花绽放，新年祝福随之出现。'),
'zh-TW':('新年零點','點一下零點的時鐘，煙火綻放，新年祝福隨之出現。'),
'th':('เที่ยงคืนปีใหม่','แตะนาฬิกาตอนเที่ยงคืน พลุจะขึ้นพร้อมคำอวยพรปีใหม่'),
'ms':('Tengah Malam Tahun Baru','Sentuh jam pada tengah malam: bunga api meletup dan ucapan Tahun Baru muncul.')}
