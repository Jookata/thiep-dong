# -*- coding: utf-8 -*-
# Nguồn bản dịch: mẫu 4 "Flappy Noel" (xe tuần lộc bay qua cây thông và đàn tuần lộc say ngủ)
# Chữ sinh ra docs/flappy/texts.js qua build_i18n.py.
from i18n_src_b import SANTA
FK=['title','fin','h1','ouch','drop']
_T={
'vi':('Xe tuần lộc bay giao quà','Chạm vào màn hình để xe bay lên! Tránh cây thông và đàn tuần lộc say ngủ nhé!','Úi! Thử lại nào!','Hô hô hô! Quà đây!'),
'en':("Santa's Flying Sleigh",'Tap the screen to fly! Dodge the pine trees and the sleepy drunk reindeer!','Oops! Try again!',"Ho ho ho! Here's your gift!"),
'fr':('Le traîneau volant du Père Noël',"Touchez l'écran pour voler ! Évitez les sapins et les rennes ivres endormis !",'Oups ! Réessayez !','Ho ho ho ! Voici ton cadeau !'),
'de':('Der fliegende Weihnachtsschlitten','Tippe auf den Bildschirm, um zu fliegen! Weiche den Tannen und den schlafenden betrunkenen Rentieren aus!','Hoppla! Versuch es noch einmal!','Ho ho ho! Hier ist dein Geschenk!'),
'it':('La slitta volante di Babbo Natale','Tocca lo schermo per volare! Evita gli abeti e le renne ubriache addormentate!','Ops! Riprova!','Ho ho ho! Ecco il tuo regalo!'),
'pl':('Latające sanie Mikołaja','Dotknij ekranu, aby lecieć! Omijaj choinki i śpiące pijane renifery!','Ups! Spróbuj jeszcze raz!','Ho ho ho! Oto twój prezent!'),
'fi':('Joulupukin lentävä reki','Napauta näyttöä lentääksesi! Väistä kuuset ja nukkuvat humalaiset porot!','Hups! Yritä uudelleen!','Ho ho ho! Tässä lahjasi!'),
'es':('El trineo volador de Papá Noel','Toca la pantalla para volar. Esquiva los pinos y los renos borrachos dormidos.','¡Ups! ¡Inténtalo otra vez!','¡Jo jo jo! ¡Aquí tienes tu regalo!'),
'pt':('O trenó voador do Papai Noel','Toque na tela para voar! Desvie dos pinheiros e das renas bêbadas adormecidas!','Ops! Tente de novo!','Ho ho ho! Aqui está o seu presente!'),
'sk':('Lietajúce sane Santa Clausa','Ťukni na obrazovku a leť! Vyhni sa jedliam a spiacim opitým sobom!','Ups! Skús znova!','Ho ho ho! Tu je tvoj darček!'),
'ko':('산타의 하늘을 나는 썰매','화면을 터치해서 날아요! 전나무와 술에 취해 잠든 순록을 피하세요!','앗! 다시 도전!','호호호! 선물이에요!'),
'ja':('サンタの空飛ぶそり','画面をタップして飛ぼう！モミの木と、酔って眠っているトナカイをよけてね！','おっと！もう一度！','ホッホッホ！プレゼントだよ！'),
'zh':('圣诞老人的飞行雪橇','点击屏幕飞起来！躲开松树和喝醉睡着的驯鹿！','哎呀！再试一次！','呵呵呵！礼物来啦！'),
'zh-TW':('聖誕老人的飛行雪橇','點擊螢幕飛起來！閃開松樹和喝醉睡著的馴鹿！','哎呀！再試一次！','呵呵呵！禮物來囉！'),
'th':('เลื่อนบินของซานตาคลอส','แตะหน้าจอเพื่อบิน! หลบต้นสนและกวางเรนเดียร์เมาที่นอนหลับ!','อุ๊ย! ลองอีกครั้ง!','โฮ่ โฮ่ โฮ่! ของขวัญมาแล้ว!'),
'ms':('Kereta Salji Terbang Santa','Ketik skrin untuk terbang! Elakkan pokok pine dan rusa mabuk yang sedang tidur!','Alamak! Cuba lagi!','Ho ho ho! Ini hadiah anda!'),
}
# câu chúc cuối 'fin' dùng lại đúng bản dịch của mẫu Santa (quy ước)
FLAPPY={L:[v[0],SANTA[L][1],v[1],v[2],v[3]] for L,v in _T.items()}
