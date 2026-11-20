# Mẫu 4: Xe tuần lộc bay (id `flappy`) – kịch bản, chỉ chạy thử

Kiểu Flappy Bird. Link: `https://jookata.github.io/thiep-dong/flappy/` (chưa đưa lên GitHub).

## Luồng
1. Bấm "Mở thiệp": xe trượt tuyết + tuần lộc + ông già Noel chở hộp quà to bay từ trái vào, dừng ở 1/3 màn hình (x=120/360), nhấp nhô chờ.
2. Chạm màn hình lần đầu: bắt đầu chơi. Mỗi lần chạm xe bay lên, không chạm thì rơi. Cảnh cuộn từ phải sang trái.
3. Vật cản dưới: cây thông. Vật cản trên: chồng 1-6 chú tuần lộc say ngủ, xếp so le và quay ngược chiều nhau. Cây thông: ảnh `tree.webp` của thiệp Noel, ép hẹp. Qua đủ `NEED=5` cặp thì thắng.
4. Va chạm (cây, tuần lộc, đất): xe lộn xuống, báo "Úi! Thử lại nào!", làm lại từ 0. Mỗi lần thua khe hở rộng thêm 8 (tối đa +32).
5. Thắng: cảnh trượt từ nửa trái (cánh đồng tuyết) sang nửa phải của ảnh nền (nhà gỗ, cây thông đèn). Ông già Noel thả hộp quà xuống tuyết trước nhà, nhạc Jingle Bells nổi lên, xe bay đi, hộp mở bung pháo giấy, hiện lời chúc cuối (`fin`).

## Chỉnh nhanh (đầu khối GAME trong index.html)
`NEED` (số cặp, 5), `G0` khe hở (175), `V` tốc độ cuộn (100), `GRAV`/`FLAP` (1000/-310), `SP` khoảng cách (190), `S` cỡ xe (.5).
Kiểm thử: `?dbg&need=2` (chỉ khi có `dbg`), `window.__flappy`.

## Hình
- Dùng chung (`docs/shared/`): xe `sleigh`, tuần lộc chạy `rw1/rw2`, tuần lộc say `reindeer_drunk/2`, ông Noel `santa_flat`, cây `tree`. Riêng: nền `flappy/assets/bg_field.webp` (ảnh anh gửi 1330x1182, hiển thị 720x640, nửa trái để chơi, nửa phải để giao quà).
- Tạm (vẽ vector): hộp quà to, mặt đất tuyết cuộn. Ông Noel vẫn dùng dáng ngủ ngồi `santa_flat` (chưa có hình ông tỉnh).
- Chữ: `design/i18n_src_flappy.py` (16 ngôn ngữ) -> `python3 design/build_flappy_i18n.py` sinh `docs/flappy/texts.js`.

## Việc còn lại để vào app Android
- `Templates.java`: `new Template("flappy","flappy","xmas",R.string.tpl_flappy_title,R.string.tpl_flappy_desc,R.drawable.cover_flappy)`
- Ảnh bìa `cover_flappy.webp` (360x640, đã làm) -> `res/drawable-nodpi/`.
- Tên + mô tả 16 ngôn ngữ vào `design/i18n_src_tpl.py` (`TPL['flappy']`), rồi chạy `build_i18n.py`.
