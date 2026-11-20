# Mẫu 2 – "Ông già Noel say rượu" (WinkCard)

Bản chạy thử (hình tạm bằng vector): `docs/santa/index.html`
Mở không tham số = chế độ thử; link thật: `.../santa/?to=Lan&from=Minh&lang=vi&msg=...`

## 1. Hiểu kịch bản (em diễn giải, anh sửa nếu sai)
- Ông già Noel uống say, ngủ quên → phải **đổ nước** cho tỉnh.
- Kho có **6 chuồng**: 1 chú say rượu, 1 chuồng trống (chú đó ra sân nói chuyện với cô gái Noel, không chịu đi), 1 chú **ngoan chịu đi**, 3 chuồng "gây cười" (chuột, yêu tinh ngủ, kho rượu).
- Chú ngoan sẵn sàng nhưng xe **không có quà** → phải quay lại **mở cửa phòng quà**, chất quà lên xe.
- Ông già Noel + tuần lộc cất cánh, giao quà; **người nhận mở hộp quà** → lời chúc.

## 2. Luồng tương tác (máy trạng thái)
| # | Màn hình / việc | Người nhận chạm | Kết quả | Gợi ý hiện ra |
|---|---|---|---|---|
| 0 | Ông Noel nằm ngáy, chai rượu | **Xô nước** (có MŨI TÊN – chỉ bước này) | Xô bay tới, đổ nước, ông giật mình đứng dậy, run lập cập, nước nhỏ giọt | s1 (câu đố) |
| 1 | 6 chuồng + cặp (cô gái Noel + tuần lộc) ngoài sân | Chuồng 1 | Mở cửa: tuần lộc say lảo đảo, cầm chai | k1 (gag) |
| | | Chuồng 2 | Trống; nhắc "có tiếng cười ngoài sân" | k2 |
| | | Chuồng 4 | Rơm + chuột gặm bánh | k4 |
| | | Chuồng 5 | Yêu tinh ngủ | k5 |
| | | Chuồng 6 | Kho rượu bí mật | k6 |
| | | Cặp ngoài sân | Tuần lộc quay đi, tim bay: không chịu đi | kp |
| | | **Chuồng 3 (đúng)** | Tuần lộc nhảy ra, chạy xuống buộc vào xe | k3 (hint: mở cửa phòng nhỏ bên trái) |
| 2 | Xe trống | **Cửa phòng quà** | Cửa mở, sáng đèn, thấy đống quà | s3 |
| 3 | | **Đống quà** | 4 hộp quà bay lên xe lần lượt; ông Noel ra ngồi xe | s4 |
| 4 | | **Chiếc xe** | Cất cánh bay lên (để lại vệt sao), nhạc Jingle Bells bắt đầu | – |
| 5 | Cảnh giao quà: mái nhà tuyết rơi, xe bay ngang, hộp quà rơi xuống nảy | **Hộp quà** | Nắp bay, pháo giấy | s5 |
| 6 | Lời chúc cuối (chữ trên ảnh, không nền) | Nút "Xem lại" | tên người nhận + lời nhắn + người gửi + dòng tải WinkCard | – |

Quy tắc: chạm sai chỗ ở bước ít mục tiêu thì báo "Lạnh quá / Ấm dần / Nóng rồi"; các chuồng có thể mở theo **thứ tự bất kỳ**; sau mỗi câu gag, gợi ý chính tự hiện lại sau ~3,6 giây.

## 3. Danh sách ảnh cần vẽ (anh thay vào, em gắn)
Khổ chuẩn 720×1280 (tỉ lệ 9:16), WebP trong suốt cho sprite. Vị trí/kích thước hiện tại tính theo khung 360×640 (nhân đôi cho ảnh thật).

**Nền**
1. `yard_bg.webp` 720×1280 – trời đêm, trăng, nhà kho 6 ô chuồng **trống (bên trong tối + rơm)**, đất tuyết, căn phòng nhỏ bên trái. (Cửa/đối tượng tách riêng bên dưới.)
2. `deliv_bg.webp` 720×1280 – mái nhà phủ tuyết, ống khói, cửa sổ sáng, trời đêm.

**Chuồng và phòng quà**
3. `stall_door.webp` ~200×184 – cánh cửa chuồng gỗ (dùng chung 6 lần, mở bằng cách thu hẹp ngang).
4. `hut_door.webp` ~76×112 – cửa phòng quà; `hut_inside.webp` – bên trong sáng ấm.

**Trong chuồng (mỗi cái ~200×184, đáy là rơm)**
5. `st1_reindeer_drunk.webp` · 6. `st3_reindeer_good.webp` · 7. `st4_mouse.webp` · 8. `st5_elf_sleep.webp` · 9. `st6_wine.webp` (chuồng 2 để trống)

**Nhân vật / đạo cụ** (đứng/ngồi trên đất, nền trong suốt)
10. `santa_sleep.webp` (~100×36 đơn vị → 200×72 px) – nằm ngáy + chai
11. `santa_stand.webp` (~30×60) – đứng, ướt, run
12. `santa_sit.webp` – ngồi trên xe (nửa thân)
13. `reindeer_good.webp` (~50×55) – quay mặt sang phải, dùng khi buộc vào xe và khi bay
14. `reindeer_chat.webp` + `elf_girl.webp` – cặp đang nói chuyện (có thể vẽ chung một ảnh)
15. `bucket.webp` (~24×22) – xô nước
16. `sleigh_empty.webp` (~110×50) và `sleigh_load.webp` (đống quà để chồng lên)
17. `gift1..4.webp` (~14×14) – 4 hộp quà nhỏ trong phòng
18. `bigbox_body.webp`, `bigbox_lid.webp` (~80×60) – hộp quà lớn; nắp tách riêng để bật lên
19. (tuỳ chọn) `preview.jpg` 1200×630 cho ảnh xem trước khi chia sẻ link

Mỗi sprite nên vẽ có **một ít viền trong suốt** quanh nhân vật; em sẽ căn lại toạ độ khi ghép.

## 4. Âm thanh (đã có, tổng hợp bằng code, không tốn dung lượng)
Chuông cho mỗi lần chạm, tiếng nước (nhiễu lọc), tiếng pháo giấy, nhạc Jingle Bells khi cất cánh.

## 5. Dung lượng mục tiêu
HTML ~42 KB (nén ~15 KB) + ảnh 15–20 file WebP ≤ 800 KB tổng → dưới 1 MB.

## 6. Ghi chú khi đưa vào app
- Thêm mẫu vào `Templates.java` + ảnh bìa; link web: `.../santa/?to=&from=&lang=&msg=`.
- 17 ngôn ngữ: lời chúc cuối + dòng tải app đã có; các câu đố mới có bản Việt/Anh, cần dịch thêm nếu muốn.


## Cập nhật: chuồng dạng vuốt trái/phải (carousel)
- Cảnh 1: ảnh nền intro (Santa ngủ) + xô nước (mũi tên). Đổ nước -> cảnh sốc (ảnh Santa ôm đầu) -> vào kho.
- Kho = 7 ô vuốt: ô 0 sân (kho quà + xe), ô 1..6 là 6 tình huống chuồng.
  1 say rượu (kéo chuông) · 2 ham chơi với cô gái Noel (ảnh anh gửi) · 3 sẵn sàng (đi tiếp truyện, về sân tìm quà)
  4 ngủ quên · 5 trốn trong cỏ khô · 6 dây cương rối (chọn đúng đầu dây: giữa-phải)
- Chỉ chuồng 3 đẩy truyện; các chuồng khác là gag. Sau đó: kho quà -> chất quà -> xe cất cánh -> hộp quà -> lời chúc.
- Ảnh trong docs/santa/assets: intro_bg, santa_shock, elf_reindeer. Mẫu CHƯA đăng ký vào app Android.
