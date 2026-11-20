# Mẫu 3 – "Hứng quà rơi" (`docs/catch/`)

Bản chạy thử: `docs/catch/index.html`. Mở không tham số = chế độ thử (nhập tên người nhận, người gửi, chọn ngôn ngữ). Link thật: `.../catch/?to=Lan&from=Minh&lang=vi&m=<lời chúc mã hoá>`.
Đã đăng ký vào app Android (`Templates.java`, `cover_catch.webp`, chuỗi trong `design/i18n_src_tpl.py`). Chưa đưa lên GitHub.

## Kịch bản
1. Màn mở: tên người gửi/nhận (hoặc ô nhập ở chế độ thử) + nút "Mở thiệp".
2. Ông già Noel ngồi xe trượt, 2 tuần lộc kéo, bay qua lại phía trên làng tuyết. Chân tuần lộc chạy bằng 2 dáng `rw1/rw2` lấy từ mẫu `santa`.
3. Cứ ~1 giây ông thả 1 hộp quà (đội xe ngắn gọn, bay nhanh). Người nhận kéo ngón tay sang trái/phải, chiếc tất đi theo và hứng. Hụt thì hộp tan trên đường và sáng 1 trong 3 chấm đỏ cạnh bảng điểm; hụt đủ 3 hộp thì bị TRỪ 1 hộp đã hứng (ô tắt, chấm đỏ về 0). Lần hụt đầu có câu nhắc `c2`.
4. Hứng đủ 9 hộp (HUD 9 ô trên đầu): đội bay đi hẳn, hộp quà lớn rơi xuống giữa đường, có mũi tên chỉ.
5. Chạm hộp quà lớn: nắp bay, pháo giấy, lời chúc cuối (tên người nhận, lời nhắn mã hoá, người gửi, dòng tải WinkCard, nút xem lại).

## Chữ (16 ngôn ngữ)
`design/i18n_src_d.py` (khoá: title, fin, c1, c2, c3). `fin` dùng lại đúng câu của Santa. `{n}` = số hộp (9), `{to}` = tên người nhận. Sửa xong chạy `python3 design/build_i18n.py`.

## Hình
- Thật (anh gửi): `bg.webp` (làng tuyết, 720x1280), `sleigh.webp` (ông Noel ngồi xe, nền trong suốt, KHÔNG có tuần lộc).
- Lấy từ mẫu santa: `rw1.webp`, `rw2.webp` (tuần lộc, gốc quay trái nên được lật sang phải).
- Hình tạm bằng vector, anh sẽ thay: chiếc tất, hộp quà nhỏ (5 màu), hộp quà lớn (thân + nắp tách riêng).

## Chỉnh nhanh (đầu khối GAME trong `index.html`)
`SPEED` tốc độ bay (150), `FW`/`SL_W`/`RD_W` độ dài đội xe, số 3 trong `onMiss()` là số hộp hụt bị trừ, tuyết: vòng lặp 130 hạt, `FALL` tốc độ rơi, `HALF` độ rộng miệng tất, `NEED` số hộp (chỉ đổi được khi thử với `?dbg&need=3`), `FY` độ cao đường bay.
Thử nhanh: thêm `?dbg&need=3` vào địa chỉ (chỉ hứng 3 hộp). Không dùng `dbg` trong link thật.

## Quy tắc chơi bổ sung
- Người chơi đứng yên (tất không di chuyển quá ~1,5 giây): KHÔNG thả hộp quà xuống vùng quanh chiếc tất, để khỏi nhận quà miễn phí. Phải di chuyển thì quà mới rơi về phía mình.
- Hết 3 phút không chạm gì (đang chơi hoặc đang chờ mở hộp quà lớn) thì tự quay về màn hình bắt đầu (`IDLE_RESET`). Màn lời chúc cuối thì không tự thoát.
- Nhạc Jingle Bells CHỈ bật khi mở hộp quà lớn; các âm thanh khi chơi (chuông, nhận/hụt quà) giữ nguyên.
