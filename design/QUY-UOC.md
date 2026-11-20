# Quy ước WinkCard (mọi mẫu thiệp phải theo, để làm ở nhiều cửa sổ chat vẫn đồng bộ)

Dự án: app Android "WinkCard" (Jookata) gửi thiệp động; người nhận chỉ mở link web trên GitHub Pages (`https://jookata.github.io/thiep-dong/<mẫu>/`). Người dùng xưng "anh", gọi Claude là "em", nói tiếng Việt.
Mẫu có sẵn để học theo: `docs/noel/` (mẫu 1), `docs/santa/` (mẫu 2, nhiều cảnh), `docs/catch/` (mẫu 3, trò chơi), `docs/flappy/` (mẫu 4, trò chơi bay kiểu Flappy Bird), `docs/korea/` (mẫu 9, Giáng sinh Hàn Quốc: bìa, lật trang, chạm lần lượt bé trai, bé gái, chú chó rồi tuyết rơi + lời chúc), `docs/newyear/` (mẫu 8, Chúc mừng năm mới: chạm đồng hồ, pháo hoa), `docs/nen/` (mẫu 7, sinh nhật đơn giản: bìa, lật trang, thổi nến), `docs/yuki/` (mẫu 6, Giáng sinh Nhật Bản: lật trang + tuyết), `docs/birthday/` (mẫu 5, sinh nhật: chọn hộp, cắm và thổi nến, font trong `docs/shared/fonts`). Mở một mẫu có sẵn đọc kỹ TRƯỚC khi viết mẫu mới; chép nguyên khung, không tự chế khác.

## 1. Cấu trúc và việc cần làm cho mẫu mới `<id>`
1. `docs/<id>/index.html` (+ `assets/*.webp`, `preview.jpg` 1200x630). Một file HTML, JS thuần, không thư viện.
2. Chữ: thêm `design/i18n_src_<x>.py` (khoá `XK`, bảng `XXX={lang:[...]}` đủ **16 ngôn ngữ**: vi, en, fr, de, it, pl, fi, es, pt, sk, ko, ja, zh, zh-TW, th, ms), nối vào `design/build_i18n.py` (assert độ dài + thêm tên mẫu vào vòng sinh `texts.js`), rồi chạy `python3 design/build_i18n.py`. KHÔNG sửa tay `docs/i18n.js`, `docs/*/texts.js`, `strings.xml`, `Lang.java`.
3. Câu chúc cuối khoá `fin` ("Giáng sinh an lành, {to}!"): dùng lại đúng bản dịch của mẫu Santa cho các mẫu Giáng sinh. Chỗ trống trong chữ: `{to}` tên người nhận, `{from}` người gửi, `{n}` số đếm riêng của mẫu.
4. Cập nhật `README.md` (danh sách mẫu) và viết `design/<id>-kich-ban.md` (kịch bản, danh sách hình thật/hình tạm, chỉnh nhanh).
5. **Android: mọi mẫu phải có mặt trong app**: KHÔNG sửa tay `Templates.java`; thêm dòng `('<id>','xmas|birthday|newyear')` vào `design/cards.py`, ảnh bìa `design/covers/<id>.webp` 360x640, tên + mô tả 16 ngôn ngữ vào `TPL` (xem mục cuối), rồi `build_i18n.py` sinh `Templates.java`, chép ảnh bìa và chuỗi `tpl_<id>_*`. Nhóm hiện có: Giáng sinh (`xmas`), Sinh nhật (`birthday`), Năm mới (`newyear`).
6. **Quảng cáo:** màn Xem thử của app (`activity_preview.xml` + `PreviewActivity`) luôn có banner AdMob dưới cùng (ID test `admob_banner_id` trong `res/values/ads.xml`, thay ID thật trước khi phát hành). KHÔNG đặt quảng cáo trên trang web người nhận. Làm xuyên suốt, không cần anh nhắc lại.
7. GitHub: chỉ đưa lên khi anh bảo ("chạy tốt rồi đưa lên GitHub"). Mặc định mọi mẫu mới chỉ chạy thử. Anh làm mỗi thiệp ở một cửa sổ chat riêng trong cùng dự án, nên luôn đọc `design/QUY-UOC.md` và mẫu mới nhất trước khi làm.
8. Mẫu trò chơi: bỏ nhạc nền lúc chơi nếu anh dặn (mẫu `catch` chỉ bật nhạc khi mở hộp quà); nếu người chơi bận (~3 phút không chạm) thì quay về màn đầu.

## 2. Link và tham số (giống nhau mọi mẫu)
`?to=<người nhận>&from=<người gửi>&lang=<mã>&m=<lời chúc mã hoá>`; `msg=` (chữ thường, không mã hoá) vẫn đọc được. Giới hạn: tên 30 ký tự, lời chúc 160.
- `lang` qua `WC.norm()`, mặc định theo `navigator.language`, không có thì `en`.
- Lời chúc `m` = base64url(XOR(UTF-8, khoá `w1nk-c4rd-2026`)); dùng `WC.enc/WC.dec` trong `docs/i18n.js`, đừng viết lại.
- `hasParams = to || from || lang`. Không có tham số = **chế độ thử**: ô "Tên người nhận", "Tên người gửi", "Lời chúc riêng (không bắt buộc, 160 ký tự)", chọn ngôn ngữ (16); nhớ bằng localStorage (khoá `<id>Demo`: to, from, msg, lang; mặc định Lan/Minh/để trống/vi). Ô lời chúc nối với biến `custom`, hiện ở màn cuối. Có tham số: ẩn khung nhập, hiện "Từ:/Gửi:".
- Chữ chung lấy từ `WC.COMMON` (anon, fromLine, toLine, open, lblTo, lblFrom, note, sign, replay, dl...), ghép bằng `WC.build(TX)`; script: `<script src="../i18n.js">` rồi `<script src="texts.js">`.

## 3. Khung giao diện (chép từ mẫu có sẵn)
- `.stage` tỉ lệ 9:16 (`--w:min(100vw,calc(100vh*.5625))`, `container-type:size`), mọi cỡ chữ/khoảng cách dùng `cqw`. Cảnh là `<svg viewBox="0 0 360 640">`, toạ độ trong khung 360x640. Nền ảnh 720x1280 WebP.
- Màn mở `#start` (thẻ giữa màn, biểu tượng emoji, tiêu đề, "Từ/Gửi" hoặc ô nhập thử, nút "Mở thiệp"); lời gợi ý `#msg` ở trên (chữ trắng có bóng, KHÔNG nền); toast; nút âm thanh `#snd`.
- Màn cuối: `#msg.final` chữ trên ảnh, không nền: dòng chúc vàng (tên người nhận) → lời nhắn riêng (nếu có) → "Thương gửi, {from}" (nếu có) → "Tải WinkCard tại <link Play>" → nút "Xem lại" (`location.reload()`). Link Play: `https://play.google.com/store/apps/details?id=com.jookata.thiepdong`.
- Âm thanh tổng hợp bằng WebAudio (không file): `chime`, `noise`, nhạc Jingle Bells. Chỉ khởi tạo sau khi chạm "Mở thiệp".
- `<head>`: title "WinkCard · <tên mẫu>", description song ngữ, og:title/og:description/og:image (`.../<id>/preview.jpg`), twitter summary_large_image.

## 4. Hình ảnh
- Hình thật do anh gửi; chỗ chưa có thì vẽ tạm bằng vector (hộp quà `giftBox`, chiếc tất...) để làm khung, ghi rõ trong `design/<id>-kich-ban.md` là hình tạm. Anh sẽ vẽ lại rồi gửi để thay.
- Hình dùng chung giữa nhiều mẫu nằm ở `docs/shared/`, mẫu gọi bằng `../shared/<tên>.webp` (Android nhúng cả `docs/` nên Xem thử vẫn chạy offline). Mẫu mới cần nhân vật đã có thì lấy từ `docs/shared/`; hình riêng của mẫu (nền, ảnh bìa) để trong `docs/<id>/assets/`. Không sửa/ghi đè hình trong `shared/` nếu chưa kiểm tra mọi mẫu đang dùng nó. Đường dẫn ghép bằng code (`'assets/'+tên+số`) thì giữ bản chép riêng. `python3 design/share_assets.py` báo cáo hình trùng (thêm `--apply` để gom). Có sẵn: ông già Noel `sw1..4` (bước say), `santa_flat`, `santa_shock`; tuần lộc `rw1/rw2` (2 dáng chạy, gốc quay TRÁI nên lật `scale(-1 1)` để quay phải; chân hoạt động bằng cách đổi qua lại 2 ảnh ~7 lần/giây, con thứ hai lệch pha); xe `sleigh.webp`; nền nhà tuyết `deliv_bg`.
- Ảnh anh gửi có nền trắng/ô vuông thì tách nền (alpha) rồi lưu WebP; kiểm tra bằng cách xem ảnh thật trước khi ghép.

## 5. Cách chạy thử và giao
- Chạy thử bằng Chrome headless + Playwright (có thể `executable_path='/usr/bin/google-chrome'`), chụp màn hình các bước, kiểm tra không có lỗi console, thử cả `?to=..&from=..&lang=zh&m=<WC.enc(...)>`.
- Mẫu có trò chơi: cho phép `?dbg&need=3` (chỉ khi có `dbg`) và `window.__<id>` để kiểm thử tự động; không để ảnh hưởng link thật.
- Giao: nén cả thư mục `thiep-dong` thành `thiep-dong.zip` + (khi tiện) đăng bản chạy thử lên artifact để anh mở trên điện thoại. Cuối câu trả lời nói rõ cái gì là hình tạm, cái gì chưa thử trên điện thoại thật.
- Trước khi làm mẫu mới trong cửa sổ chat mới: tìm lại các chat cũ trong cùng dự án (conversation_search "Thiệp Noel tương tác", "thiệp thứ ...") và đọc file zip/`design/*.md` anh gửi để khỏi làm lệch.


## Thêm thiệp mới và đưa lên GitHub (quy trình một lệnh)
1. Tạo thư mục `docs/<id>/` (index.html, texts.js sinh tự động, preview.jpg 1200x630, assets/).
2. Thêm một dòng `('<id>','<nhóm>')` vào `design/cards.py` (nguồn duy nhất của danh sách thiệp).
3. Thêm ảnh bìa `design/covers/<id>.webp` (360x640) và tên + mô tả 16 ngôn ngữ vào `TPL` (`design/i18n_src_tpl.py` hoặc file `i18n_src_*.py` của thiệp rồi gắn vào `build_i18n.py`).
4. `python3 design/build_i18n.py` sinh: bản dịch từng thiệp, chuỗi Android, `Templates.java` (khối BEGIN-GEN/END-GEN, KHÔNG sửa tay) và chép ảnh bìa vào `res/drawable-nodpi/`.
5. `python3 design/check.py` kiểm tra file thiếu, cú pháp JS, đủ 16 ngôn ngữ.
6. `./cap-nhat.sh [file.zip] "lời nhắn"` nhận zip mới (nếu có), chạy 4 và 5, rồi commit + push. Web và Android đi chung một lần đẩy. GitHub Actions kiểm tra lại sau mỗi lần đẩy.

## Kiểu thiệp "bìa + lật trang" (mẫu 6, 7, 8, 9: yuki, nen, newyear, korea)
Bìa chỉ ghi "Gửi: {to}"; sau 8 giây hiện lời nhắc mở thiệp (`hint`, kèm tên); chạm thì bìa lật 3D (4 giây) sang cảnh trong; chưa hiện chữ chúc cho tới khi người nhận làm đúng thao tác (chạm đồng hồ, thổi nến...). Màn mở có tiêu đề kèm tên (`titleTo`), không dùng chữ "bạn" khi đã có tên. Chép từ `docs/nen/index.html`.


### Mẫu korea (nhân vật chạm lần lượt)
Cảnh nền trống `assets/scene.webp` + 3 nhân vật PNG tách nền `boy/girl/dog.webp` đặt theo % màn hình (`left/top/width` trong `index.html`, cùng toạ độ `BOX` để bấm). Bấm đúng chỗ nhân vật kế tiếp (trai, gái, chó); sau 6 giây không bấm hiện vòng sáng + chữ gợi ý `tap`; nhân vật cuối hiện thì tuyết rơi, nhạc bật, lời chúc hiện ở phần trời phía trên. Muốn đổi vị trí: sửa cả style của `#c0..#c2` và mảng `BOX`.
