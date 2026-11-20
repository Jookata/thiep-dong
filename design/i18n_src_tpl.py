# -*- coding: utf-8 -*-
# Tên + mô tả MẪU THIỆP hiển thị trong app Android, từ mẫu số 3 trở đi (mẫu 1, 2 nằm trong i18n_src_c.py).
# Mỗi mẫu mới thêm MỘT mục: TPL['<id>']={lang:(tiêu đề, mô tả)} đủ 16 ngôn ngữ. build_i18n.py tự chèn thành
# chuỗi tpl_<id>_title / tpl_<id>_desc (Android: res/values*/strings.xml).
TPL={}
TPL['catch']={
'vi':('Thiệp Noel: Hứng quà ông già Noel','Ông già Noel bay ngang thả quà, kéo chiếc tất hứng đủ 9 hộp, hộp quà lớn sẽ mở ra lời chúc có tên người nhận.'),
'en':('Christmas card: Catch Santa’s gifts','Santa flies by dropping gifts. Drag the stocking to catch all 9, then the big gift opens with a greeting for the recipient.'),
'fr':('Carte de Noël : Attrape les cadeaux','Le Père Noël passe en lâchant des cadeaux. Glissez la chaussette pour en attraper 9, puis le grand cadeau s’ouvre sur un message pour le destinataire.'),
'de':('Weihnachtskarte: Fang die Geschenke','Der Weihnachtsmann wirft Geschenke ab. Fange alle 9 mit dem Strumpf, dann öffnet sich das große Geschenk mit einem Gruß für den Empfänger.'),
'it':('Biglietto di Natale: Prendi i regali','Babbo Natale lascia cadere regali. Muovi la calza per prenderne 9, poi il grande regalo si apre con gli auguri per il destinatario.'),
'pl':('Kartka świąteczna: Złap prezenty','Mikołaj zrzuca prezenty. Przesuwaj skarpetę, by złapać 9, a duży prezent otworzy się z życzeniami dla odbiorcy.'),
'fi':('Joulukortti: Kerää lahjat','Joulupukki pudottaa lahjoja. Liikuta sukkaa ja ota 9 kiinni, niin iso lahja aukeaa ja paljastaa vastaanottajan terveiset.'),
'es':('Tarjeta de Navidad: Atrapa los regalos','Papá Noel suelta regalos. Mueve el calcetín para atrapar 9 y el regalo grande se abrirá con una felicitación para el destinatario.'),
'pt':('Cartão de Natal: Apanhe os presentes','O Papai Noel solta presentes. Mova a meia para apanhar 9 e o presente grande abre com uma mensagem para o destinatário.'),
'sk':('Vianočná pohľadnica: Chyť darčeky','Santa Claus zhadzuje darčeky. Pohybuj ponožkou, chyť 9 a veľký darček sa otvorí s pozdravom pre príjemcu.'),
'ko':('크리스마스 카드: 선물 받기','산타 할아버지가 선물을 떨어뜨려요. 양말을 움직여 9개를 받으면 큰 선물 상자가 열리며 받는 사람에게 인사말이 나타나요.'),
'ja':('クリスマスカード：プレゼントキャッチ','サンタさんが落とすプレゼントを、くつ下を動かして9個キャッチ。大きなプレゼントが開いて、受取人へのメッセージが現れます。'),
'zh':('圣诞贺卡：接礼物','圣诞老人飞过撒下礼物，移动袜子接住 9 个，大礼盒就会打开，露出给收件人的祝福。'),
'zh-TW':('聖誕賀卡：接禮物','聖誕老人飛過灑下禮物，移動襪子接住 9 個，大禮盒就會打開，露出給收件人的祝福。'),
'th':('การ์ดคริสต์มาส: รับของขวัญ','ซานตาคลอสโยนของขวัญลงมา ลากถุงเท้าไปรับให้ครบ 9 กล่อง แล้วกล่องของขวัญใหญ่จะเปิดออกพร้อมคำอวยพรถึงผู้รับ'),
'ms':('Kad Krismas: Sambut hadiah','Santa Claus menjatuhkan hadiah. Gerakkan stoking untuk menyambut 9 hadiah, kemudian hadiah besar terbuka dengan ucapan untuk penerima.'),
}
TPL['flappy']={
'vi':('Thiệp Noel: Xe tuần lộc bay','Chạm để xe tuần lộc bay qua cây thông và đàn tuần lộc say ngủ, qua đủ 5 chặng ông già Noel sẽ thả quà kèm lời chúc có tên người nhận.'),
'en':('Christmas card: Flying Sleigh','Tap to fly the reindeer sleigh past pine trees and sleepy reindeer. After 5 gates Santa drops the gift with a greeting for the recipient.'),
'fr':('Carte de Noël : Traîneau volant','Touchez pour faire voler le traîneau entre les sapins et les rennes endormis. Après 5 passages, le Père Noël lâche le cadeau avec un message pour le destinataire.'),
'de':('Weihnachtskarte: Fliegender Schlitten','Tippe, um den Rentierschlitten an Tannen und schlafenden Rentieren vorbeizusteuern. Nach 5 Durchgängen wirft der Weihnachtsmann das Geschenk mit einem Gruß für den Empfänger ab.'),
'it':('Biglietto di Natale: Slitta volante','Tocca per far volare la slitta tra gli abeti e le renne addormentate. Dopo 5 passaggi Babbo Natale lascia cadere il regalo con gli auguri per il destinatario.'),
'pl':('Kartka świąteczna: Latające sanie','Dotykaj, aby sanie leciały między choinkami i śpiącymi reniferami. Po 5 przelotach Mikołaj zrzuci prezent z życzeniami dla odbiorcy.'),
'fi':('Joulukortti: Lentävä reki','Napauta, niin pororeki lentää kuusien ja nukkuvien porojen ohi. Viiden väylän jälkeen Joulupukki pudottaa lahjan ja vastaanottajan terveiset.'),
'es':('Tarjeta de Navidad: Trineo volador','Toca para que el trineo vuele entre los pinos y los renos dormidos. Tras 5 pasos, Papá Noel suelta el regalo con una felicitación para el destinatario.'),
'pt':('Cartão de Natal: Trenó voador','Toque para o trenó voar entre os pinheiros e as renas adormecidas. Após 5 passagens, o Papai Noel solta o presente com uma mensagem para o destinatário.'),
'sk':('Vianočná pohľadnica: Lietajúce sane','Ťukaj, aby sane leteli medzi jedľami a spiacimi sobmi. Po 5 prelete Santa Claus zhodí darček s pozdravom pre príjemcu.'),
'ko':('크리스마스 카드: 하늘을 나는 썰매','화면을 터치해 순록 썰매를 전나무와 잠든 순록 사이로 날려요. 5번 통과하면 산타가 선물을 떨어뜨리고 받는 사람에게 인사말을 전해요.'),
'ja':('クリスマスカード：空飛ぶそり','タップしてトナカイのそりを、モミの木と眠るトナカイの間で飛ばそう。5回通過するとサンタがプレゼントを落とし、受取人へのメッセージが現れます。'),
'zh':('圣诞贺卡：飞行雪橇','点击屏幕让驯鹿雪橇飞过松树和熟睡的驯鹿。通过 5 关后，圣诞老人会扔下礼物，并送上给收件人的祝福。'),
'zh-TW':('聖誕賀卡：飛行雪橇','點擊螢幕讓馴鹿雪橇飛過松樹和熟睡的馴鹿。通過 5 關後，聖誕老人會丟下禮物，並送上給收件人的祝福。'),
'th':('การ์ดคริสต์มาส: เลื่อนบิน','แตะเพื่อให้เลื่อนกวางเรนเดียร์บินผ่านต้นสนและกวางที่หลับอยู่ ผ่านครบ 5 ช่อง ซานตาคลอสจะทิ้งของขวัญพร้อมคำอวยพรถึงผู้รับ'),
'ms':('Kad Krismas: Kereta Salji Terbang','Ketik untuk menerbangkan kereta salji melepasi pokok pine dan rusa yang tidur. Selepas 5 laluan, Santa Claus menjatuhkan hadiah dengan ucapan untuk penerima.'),
}
TPL['birthday']={
'vi':('Thiệp Sinh nhật: Hộp quà bất ngờ','Chọn đúng hộp quà để có bánh kem, cắm nến, thắp sáng rồi thổi nến. Tấm thiệp chúc mừng sinh nhật hiện ra cùng bài Happy Birthday.'),
'en':('Birthday card: Surprise Box','Pick the right gift box to find a cake, place the candle, light it and blow it out. A birthday greeting card appears with the Happy Birthday song.'),
'fr':('Carte d’anniversaire : Boîte surprise','Choisis la bonne boîte pour trouver un gâteau, pose la bougie, allume-la et souffle-la. Une carte d’anniversaire apparaît avec la chanson Joyeux anniversaire.'),
'de':('Geburtstagskarte: Überraschungsbox','Wähle die richtige Schachtel, um eine Torte zu finden, stecke die Kerze auf, zünde sie an und puste sie aus. Danach erscheint die Geburtstagskarte mit dem Geburtstagslied.'),
'it':('Biglietto di compleanno: Scatola a sorpresa','Scegli la scatola giusta per trovare la torta, metti la candelina, accendila e spegnila. Appare il biglietto di auguri con la canzone Tanti auguri.'),
'pl':('Kartka urodzinowa: Pudełko niespodzianka','Wybierz właściwe pudełko, aby znaleźć tort, wbij świeczkę, zapal ją i zdmuchnij. Pojawi się kartka urodzinowa z piosenką Sto lat.'),
'fi':('Syntymäpäiväkortti: Yllätysrasia','Valitse oikea rasia löytääksesi kakun, aseta kynttilä, sytytä se ja puhalla sammuksiin. Esiin tulee syntymäpäiväkortti ja onnittelulaulu.'),
'es':('Tarjeta de cumpleaños: Caja sorpresa','Elige la caja correcta para encontrar la tarta, coloca la vela, enciéndela y sóplala. Aparece la tarjeta de cumpleaños con la canción de Cumpleaños feliz.'),
'pt':('Cartão de aniversário: Caixa surpresa','Escolha a caixa certa para encontrar o bolo, coloque a vela, acenda e sopre. O cartão de aniversário aparece com a canção de Parabéns.'),
'sk':('Narodeninová pohľadnica: Škatuľka prekvapenie','Vyber správnu škatuľku, nájdi tortu, zapichni sviečku, zapáľ ju a sfúkni. Zobrazí sa narodeninová pohľadnica s piesňou na želanie.'),
'ko':('생일 카드: 깜짝 선물 상자','알맞은 상자를 골라 케이크를 찾고, 초를 꽂아 불을 붙인 뒤 불어서 끄세요. 생일 축하 노래와 함께 축하 카드가 나타나요.'),
'ja':('バースデーカード：サプライズボックス','正しい箱を選んでケーキを見つけ、ろうそくを立てて火をつけ、吹き消そう。バースデーソングとともにお祝いカードが現れます。'),
'zh':('生日贺卡：惊喜盒子','选对礼盒找到蛋糕，插上蜡烛、点亮再吹灭。生日歌响起，生日贺卡缓缓出现。'),
'zh-TW':('生日賀卡：驚喜盒子','選對禮盒找到蛋糕，插上蠟燭、點亮再吹熄。生日歌響起，生日賀卡緩緩出現。'),
'th':('การ์ดวันเกิด: กล่องเซอร์ไพรส์','เลือกกล่องให้ถูกเพื่อพบเค้ก ปักเทียน จุดไฟแล้วเป่าให้ดับ การ์ดอวยพรวันเกิดจะปรากฏพร้อมเพลงวันเกิด'),
'ms':('Kad Hari Lahir: Kotak Kejutan','Pilih kotak yang betul untuk menjumpai kek, letakkan lilin, nyalakan dan tiup. Kad ucapan hari lahir muncul bersama lagu Selamat Hari Lahir.'),
}
