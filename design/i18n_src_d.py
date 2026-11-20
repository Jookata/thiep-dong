# -*- coding: utf-8 -*-
# Nguồn bản dịch (phần 4): mẫu "Hứng quà rơi" (docs/catch). {n} = số hộp quà cần hứng, {to} = tên người nhận.
# Câu 'fin' dùng lại đúng câu chúc cuối của mẫu Santa để các mẫu Giáng sinh đồng bộ.
from i18n_src_b import SANTA, SK
DK=['title','fin','c1','c2','c3']
_T={
'vi':['Hứng quà ông già Noel!','Ông già Noel bay ngang thả quà! Kéo ngón tay sang trái, phải để chiếc tất hứng đủ {n} hộp quà nhé!','Đủ {n} hộp rồi! Chạm vào hộp quà lớn để mở lời chúc!'],
'en':["Catch Santa's gifts!",'Santa is flying by, dropping gifts! Drag left and right to catch all {n} in the stocking!','All {n} caught! Tap the big gift to open your greeting!'],
'fr':['Attrape les cadeaux du Père Noël !','Le Père Noël passe en lâchant des cadeaux ! Glisse à gauche et à droite pour attraper les {n} cadeaux dans la chaussette !','Les {n} cadeaux sont attrapés ! Touche le grand cadeau pour découvrir ton message !'],
'de':['Fang die Geschenke vom Weihnachtsmann!','Der Weihnachtsmann fliegt vorbei und wirft Geschenke ab! Wische nach links und rechts, um alle {n} im Strumpf zu fangen!','Alle {n} gefangen! Tippe auf das große Geschenk, um deinen Gruß zu öffnen!'],
'it':['Prendi i regali di Babbo Natale!','Babbo Natale passa di qui e lascia cadere regali! Scorri a sinistra e a destra per prenderli tutti e {n} nella calza!','Presi tutti e {n}! Tocca il grande regalo per aprire gli auguri!'],
'pl':['Złap prezenty Świętego Mikołaja!','Święty Mikołaj leci i zrzuca prezenty! Przesuwaj palec w lewo i w prawo, aby złapać wszystkie {n} w skarpetę!','Masz wszystkie {n}! Dotknij dużego prezentu, aby otworzyć życzenia!'],
'fi':['Kerää Joulupukin lahjat!','Joulupukki lentää ohi ja pudottaa lahjoja! Liu’uta sormea vasemmalle ja oikealle ja ota kaikki {n} lahjaa sukkaan!','Kaikki {n} saatu! Kosketa isoa lahjaa avataksesi terveisesi!'],
'es':['¡Atrapa los regalos de Papá Noel!','¡Papá Noel pasa volando y suelta regalos! Desliza a izquierda y derecha para atrapar los {n} en el calcetín.','¡Los {n} atrapados! Toca el regalo grande para abrir tu felicitación.'],
'pt':['Apanhe os presentes do Papai Noel!','O Papai Noel passa voando e solta presentes! Deslize para a esquerda e para a direita para apanhar os {n} na meia!','Os {n} apanhados! Toque no presente grande para abrir a mensagem!'],
'sk':['Chyť darčeky Santa Clausa!','Santa Claus preletí a zhadzuje darčeky! Ťahaj prstom doľava a doprava a chyť všetkých {n} do ponožky!','Všetkých {n} chytených! Ťukni na veľký darček a otvor pozdrav!'],
'ko':['산타 할아버지의 선물을 받아라!','산타 할아버지가 날아가며 선물을 떨어뜨려요! 손가락을 좌우로 움직여 양말로 선물 {n}개를 모두 받아 보세요!','선물 {n}개를 모두 받았어요! 큰 선물 상자를 눌러 인사말을 열어 보세요!'],
'ja':['サンタさんのプレゼントをキャッチ！','サンタさんが飛びながらプレゼントを落とします！指を左右に動かして、くつ下で{n}個ぜんぶキャッチしよう！','{n}個ぜんぶキャッチ！大きなプレゼントをタップしてメッセージを開こう！'],
'zh':['接住圣诞老人的礼物！','圣诞老人飞过来撒礼物啦！左右滑动手指，用袜子接住全部 {n} 个礼物！','{n} 个礼物都接住了！点一点大礼盒，打开你的祝福！'],
'zh-TW':['接住聖誕老人的禮物！','聖誕老人飛過來灑禮物囉！左右滑動手指，用襪子接住全部 {n} 個禮物！','{n} 個禮物都接住了！點一下大禮盒，打開你的祝福！'],
'th':['รับของขวัญจากซานตาคลอส!','ซานตาคลอสบินผ่านมาแล้วโยนของขวัญลงมา! ลากนิ้วไปซ้ายขวาเพื่อใช้ถุงเท้ารับของขวัญให้ครบ {n} กล่อง!','รับครบ {n} กล่องแล้ว! แตะกล่องของขวัญใหญ่เพื่อเปิดคำอวยพร!'],
'ms':['Sambut hadiah Santa Claus!','Santa Claus terbang lalu menjatuhkan hadiah! Seret jari ke kiri dan kanan untuk menyambut kesemua {n} hadiah dengan stoking!','Semua {n} hadiah disambut! Sentuh hadiah besar untuk membuka ucapan!'],
}
_C2={'vi':'Rơi hụt 3 hộp là mất 1 hộp đã hứng đấy!','en':'Miss 3 gifts and you lose 1 you caught!','fr':'Si tu en rates 3, tu perds 1 cadeau déjà attrapé !','de':'Verpasst du 3 Geschenke, verlierst du 1 gefangenes!','it':'Se ne perdi 3, ne perdi 1 già preso!','pl':'Przegapisz 3 prezenty, stracisz 1 złapany!','fi':'Jos ohitat 3 lahjaa, menetät 1 saadun!','es':'¡Si fallas 3 regalos, pierdes 1 de los atrapados!','pt':'Se perder 3 presentes, perde 1 já apanhado!','sk':'Ak minieš 3 darčeky, stratíš 1 chytený!','ko':'선물 3개를 놓치면 받은 선물 1개가 사라져요!','ja':'プレゼントを3個とりこぼすと、キャッチ済みの1個が消えちゃう！','zh':'漏接 3 个礼物，就会失去 1 个已接到的！','zh-TW':'漏接 3 個禮物，就會失去 1 個已接到的！','th':'พลาด 3 กล่อง จะเสียกล่องที่รับไว้ไป 1 กล่อง!','ms':'Terlepas 3 hadiah, anda hilang 1 hadiah yang disambut!'}
CATCH={L:[_T[L][0],SANTA[L][SK.index('fin')],_T[L][1],_C2[L],_T[L][2]] for L in _T}
