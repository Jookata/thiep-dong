# -*- coding: utf-8 -*-
# Nguồn bản dịch: mẫu 7 "nen" (Nến sinh nhật: bìa, lật trang, thổi nến, lời chúc). hb/blow lấy lại từ mẫu Sinh nhật 5, hint từ mẫu yuki.
import i18n_src_g as G
from i18n_src_f import BDAY,BK
from i18n_src_a import LANGS
_N={
'vi':('Một tấm thiệp sinh nhật','{to} có một tấm thiệp sinh nhật'),'en':('A birthday card','{to}, you have a birthday card'),
'fr':('Une carte d’anniversaire','{to}, vous avez une carte d’anniversaire'),'de':('Eine Geburtstagskarte','{to}, du hast eine Geburtstagskarte'),
'it':('Un biglietto di compleanno','{to}, hai un biglietto di compleanno'),'pl':('Kartka urodzinowa','{to}, masz kartkę urodzinową'),
'fi':('Syntymäpäiväkortti','{to}, sinulle on syntymäpäiväkortti'),'es':('Una tarjeta de cumpleaños','{to}, tienes una tarjeta de cumpleaños'),
'pt':('Um cartão de aniversário','{to}, você tem um cartão de aniversário'),'sk':('Narodeninová pohľadnica','{to}, máš narodeninovú pohľadnicu'),
'ko':('생일 카드','{to}님, 생일 카드가 도착했어요'),'ja':('バースデーカード','{to}さん、バースデーカードが届いています'),
'zh':('一张生日贺卡','{to}，你收到一张生日贺卡'),'zh-TW':('一張生日賀卡','{to}，你收到一張生日賀卡'),
'th':('การ์ดวันเกิด','{to} คุณมีการ์ดวันเกิด'),'ms':('Kad hari lahir','{to}, anda ada kad hari lahir')}
EK=['title','titleTo','hint','hb','blow']
NEN={L:[_N[L][0],_N[L][1],G._H[L],BDAY[L][BK.index('hb')],BDAY[L][BK.index('blow')]] for L in LANGS}
TPL_NEN={
'vi':('Nến sinh nhật','Thổi tắt ngọn nến đang cháy để nhận lời chúc sinh nhật cùng bài hát.'),
'en':('Birthday Candle','Blow out the burning candle to reveal your birthday wishes and song.'),
'fr':('Bougie d’anniversaire','Soufflez la bougie allumée pour découvrir vos vœux et la chanson d’anniversaire.'),
'de':('Geburtstagskerze','Puste die brennende Kerze aus und lies deine Wünsche mit dem Geburtstagslied.'),
'it':('Candelina di compleanno','Spegni la candelina accesa per scoprire gli auguri e la canzone di compleanno.'),
'pl':('Urodzinowa świeczka','Zdmuchnij palącą się świeczkę, aby zobaczyć życzenia i usłyszeć piosenkę.'),
'fi':('Syntymäpäiväkynttilä','Puhalla palava kynttilä sammuksiin, niin näet toivotukset ja kuulet laulun.'),
'es':('Vela de cumpleaños','Sopla la vela encendida para descubrir tus deseos y la canción de cumpleaños.'),
'pt':('Vela de aniversário','Sopre a vela acesa para ver os votos e ouvir a canção de aniversário.'),
'sk':('Narodeninová sviečka','Sfúkni horiacu sviečku a uvidíš priania a počuješ narodeninovú pieseň.'),
'ko':('생일 촛불','타오르는 촛불을 불어 끄면 생일 축하 메시지와 노래가 나타나요.'),
'ja':('バースデーキャンドル','燃えるキャンドルを吹き消すと、お祝いのメッセージと歌が現れます。'),
'zh':('生日蜡烛','吹灭燃烧的蜡烛，生日祝福与生日歌便会出现。'),
'zh-TW':('生日蠟燭','吹熄燃燒的蠟燭，生日祝福與生日歌便會出現。'),
'th':('เทียนวันเกิด','เป่าเทียนที่กำลังลุกไหม้ให้ดับ เพื่อพบคำอวยพรและเพลงวันเกิด'),
'ms':('Lilin Hari Lahir','Tiup lilin yang menyala untuk melihat ucapan dan lagu hari lahir.')}
