# -*- coding: utf-8 -*-
# Nguồn bản dịch: mẫu 9 "korea" (Giáng sinh Hàn Quốc: bìa, lật trang, chạm lần lượt bé trai, bé gái, chú chó, tuyết rơi + lời chúc).
# title/titleTo/fin/hint lấy lại từ mẫu yuki.
import i18n_src_g as G
from i18n_src_a import LANGS
_TAP={'vi':'Chạm vào chỗ đang sáng để gọi các bạn nhỏ ra sân tuyết nhé!','en':'Tap the glowing spot to call the little friends into the snow!',
'fr':'Touche l’endroit qui brille pour appeler les petits amis dans la neige !','de':'Tippe auf die leuchtende Stelle, um die kleinen Freunde in den Schnee zu rufen!',
'it':'Tocca il punto luminoso per chiamare i piccoli amici sulla neve!','pl':'Dotknij świecącego miejsca, aby zawołać małych przyjaciół na śnieg!',
'fi':'Kosketa hohtavaa kohtaa kutsuaksesi pienet ystävät lumelle!','es':'¡Toca el punto brillante para llamar a los pequeños amigos a la nieve!',
'pt':'Toque no ponto brilhante para chamar os amiguinhos para a neve!','sk':'Dotkni sa svietiaceho miesta a zavolaj malých kamarátov na sneh!',
'ko':'반짝이는 곳을 눌러 눈 쌓인 마당으로 친구들을 불러 보세요!','ja':'光っているところをタッチして、雪の庭に小さな友だちを呼んでね！',
'zh':'点一点发光的地方，把小伙伴们叫到雪地里来吧！','zh-TW':'點一點發光的地方，把小夥伴們叫到雪地裡來吧！',
'th':'แตะตรงจุดที่เรืองแสงเพื่อเรียกเพื่อนตัวน้อยออกมาที่ลานหิมะ!','ms':'Ketik tempat yang bercahaya untuk memanggil kawan-kawan kecil ke salji!'}
KK=['title','titleTo','fin','hint','tap']
KOREA={L:G.YUKI[L]+[_TAP[L]] for L in LANGS}
TPL_KOREA={
'vi':('Giáng sinh Hàn Quốc','Gọi bé trai, bé gái và chú cún ra sân tuyết Hàn Quốc, tuyết rơi cùng lời chúc.'),
'en':('Korean Snow Christmas','Call the boy, the girl and the puppy into a snowy Korean courtyard to unlock your wishes.'),
'fr':('Noël neigeux en Corée','Appelez le garçon, la fille et le chiot dans une cour coréenne sous la neige.'),
'de':('Weihnachten in Korea','Rufe Junge, Mädchen und Welpen in einen verschneiten koreanischen Hof.'),
'it':('Natale nevoso in Corea','Chiama il bambino, la bambina e il cagnolino in un cortile coreano innevato.'),
'pl':('Śnieżne święta w Korei','Zawołaj chłopca, dziewczynkę i szczeniaka na zaśnieżone koreańskie podwórko.'),
'fi':('Korealainen lumijoulu','Kutsu poika, tyttö ja pentu lumiselle korealaiselle pihalle.'),
'es':('Navidad nevada en Corea','Llama al niño, a la niña y al cachorro a un patio coreano bajo la nieve.'),
'pt':('Natal nevado na Coreia','Chame o menino, a menina e o cachorrinho para um pátio coreano coberto de neve.'),
'sk':('Snežné Vianoce v Kórei','Zavolaj chlapca, dievčatko a šteniatko na zasnežený kórejský dvor.'),
'ko':('한국 눈 내리는 크리스마스','소년, 소녀, 강아지를 눈 덮인 한옥 마당으로 불러 보세요.'),
'ja':('韓国の雪のクリスマス','男の子、女の子、子犬を雪の韓国の庭に呼んでみましょう。'),
'zh':('韩国雪夜圣诞','把男孩、女孩和小狗叫到韩国的雪地庭院里，迎来祝福。'),
'zh-TW':('韓國雪夜聖誕','把男孩、女孩和小狗叫到韓國的雪地庭院裡，迎來祝福。'),
'th':('คริสต์มาสหิมะเกาหลี','เรียกเด็กชาย เด็กหญิง และลูกสุนัขมาที่ลานหิมะแบบเกาหลี'),
'ms':('Krismas Salji Korea','Panggil budak lelaki, budak perempuan dan anak anjing ke halaman Korea yang bersalji.')}
