# WinkCard (thiep-dong)

Thiệp điện tử động, tương tác: **người gửi** tạo thiệp bằng app Android (Java), **người nhận** chỉ cần chạm vào link web, không cần cài gì.

```
docs/      Web (GitHub Pages): mỗi mẫu thiệp một thư mục, ví dụ docs/noel/
           docs/shared/   Hình dùng chung giữa các mẫu (xe, tuần lộc, ông Noel, cây thông); mẫu gọi bằng ../shared/tên.webp
           docs/privacy/  Chính sách quyền riêng tư (dùng cho Google Play)
android/   Dự án Android Studio (Java). Nhúng docs/ vào app để "Xem thử" chạy offline
store/     Icon 512, feature graphic 1024x500, nội dung gợi ý cho trang Google Play
```

Link thiệp: `https://jookata.github.io/thiep-dong/noel/?to=Lan&from=Minh&lang=vi&msg=...`
(`to` người nhận, `from` người gửi, `lang` vi/en, `msg` lời chúc riêng, không bắt buộc).
Mở `noel/` không có tham số sẽ ra chế độ thử (có ô nhập tên).

## 1. Đưa lên GitHub + bật web

```bash
cd thiep-dong
git init -b main
git add .
git commit -m "WinkCard: web Noel + app Android"
gh repo create Jookata/thiep-dong --public --source=. --push
```
Rồi vào **Settings → Pages → Deploy from a branch → main, thư mục /docs**. Sau 1–2 phút trang chạy tại `https://jookata.github.io/thiep-dong/`.
Nếu đổi tên repo hoặc dùng tên miền riêng, sửa `WEB_BASE` trong `android/app/src/main/java/com/jookata/thiepdong/Config.java` và `og:image` trong `docs/noel/index.html`.

## 2. Chạy thử app

Mở thư mục `android/` bằng Android Studio (JDK 17), chờ Gradle sync, bấm Run. Nếu Studio gợi ý nâng AGP/Gradle thì cứ nâng.
App đang dùng **ID TEST của AdMob**, an toàn để chạy thử.

## 3. Phát hành lên Google Play

1. **AdMob:** tạo app trong AdMob, thay App ID trong `AndroidManifest.xml` và ID banner trong `res/values/ads.xml`.
2. **Ký app:** Android Studio → Build → Generate Signed App Bundle (AAB). Tạo keystore mới và **sao lưu kỹ** (file `.jks` đã bị `.gitignore` chặn, đừng đưa lên GitHub). Nên bật Play App Signing.
3. **Play Console:** tạo app → dán nội dung từ `store/listing.md` → tải icon/feature graphic trong `store/` + ảnh chụp màn hình thật từ app → điền Data safety, phân loại nội dung, khai báo có quảng cáo, URL chính sách: `https://jookata.github.io/thiep-dong/privacy/` → tải AAB lên.
4. App đã nhắm **Android 16 (API 36)** đúng quy định Google Play hiện hành cho app mới. Kiểm tra lại mục "Target API level" trước khi gửi duyệt vì quy định đổi hằng năm.
5. Nếu bán ở EEA/Anh: cần form đồng ý quảng cáo (Google UMP) trước khi tải quảng cáo. Bản này chưa có.

## 4. Thêm mẫu thiệp mới (Tết, sinh nhật…)

1. Tạo `docs/tet/index.html` (+ `assets/`), dùng cùng cách đọc `to / from / lang / msg` như `docs/noel/`.
2. Thêm hình bìa `android/app/src/main/res/drawable-nodpi/cover_tet.webp` và chuỗi tên/mô tả trong `values/strings.xml` và `values-en/strings.xml`.
3. Thêm một dòng vào `Templates.java`. Link chia sẻ tự dùng `docs/tet/`.

## Ghi chú

- Hình chó/mèo/ngôi sao trong thiệp Noel đang là hình vẽ tạm, sẽ thay bằng ảnh cùng phong cách.
- Nhạc đang là Jingle Bells (nhạc phổ cập) tổng hợp bằng trình duyệt; có thể thay bằng bản thu có bản quyền rõ ràng.
- Tên người nhận/lời chúc nằm trong link nên người nào có link đều thấy; nhật ký của GitHub Pages có thể ghi lại địa chỉ truy cập (đã nêu trong chính sách quyền riêng tư).

## Ngôn ngữ, mã hoá lời chúc, nhóm thiệp

- **16 ngôn ngữ** của thiệp: vi, en, fr, de, it, pl, fi, es, pt, sk, ko, ja, zh (giản thể), zh-TW (phồn thể), th, ms. Chữ giao diện app cũng có đủ 16 ngôn ngữ.
- Bản dịch nằm ở `design/i18n_src_a.py` (chung + Noel), `i18n_src_b.py` (Santa), `i18n_src_c.py` (giao diện app). Sửa xong chạy `python3 design/build_i18n.py` để sinh lại `docs/i18n.js`, `docs/*/texts.js`, `android/.../res/values*/strings.xml` và `Lang.java`. Đừng sửa tay các file sinh ra.
- **Lời chúc riêng** trong link được mã hoá XOR + base64url (tham số `m`), khoá `w1nk-c4rd-2026` ở `LinkBuilder.java` và `docs/i18n.js`. Link cũ dùng `msg=` chữ thường vẫn đọc được. Đây chỉ là che mắt cho link không đọc ra chữ, không phải bảo mật.
- **Nhóm thiệp** trong app: Giáng sinh, Sinh nhật, Đón năm mới (hai nhóm sau đang trống, hiện "sắp ra mắt"). Thêm mẫu mới ở `Templates.java`.
- Mẫu hiện có: `noel` (Đêm Noel trong rừng), `santa` (Ông già Noel say rượu), `catch` (Hứng quà ông già Noel thả)  `flappy` (Xe tuần lộc bay qua cây thông, kiểu Flappy Bird) `yuki` (Giáng sinh Nhật Bản, lật trang + tuyết rơi) và `korea` (Giáng sinh Hàn Quốc, chạm gọi 3 nhân vật) thuộc nhóm Giáng sinh, , `birthday` (Chọn hộp quà, thổi nến) và `nen` (Thổi nến đang cháy, lật trang) thuộc nhóm Sinh nhật, và `newyear` (Chạm đồng hồ điểm 12 giờ, pháo hoa) thuộc nhóm Năm mới. Cả chín đã đăng ký trong `Templates.java` của app Android (mẫu mới nào cũng phải đăng ký đủ). Màn Xem thử của app có banner AdMob dưới cùng (ID test).
- Quy ước chung để mọi mẫu giống nhau (làm ở nhiều cửa sổ chat khác nhau): xem `design/QUY-UOC.md` (cũng là nội dung skill `winkcard-thiep`).


## Cập nhật nhanh
Trên máy đã clone repo: `./cap-nhat.sh ~/Downloads/thiep-dong.zip "Thêm thiệp mới"` (có zip) hoặc `./cap-nhat.sh "Sửa chữ"` (đã sửa trực tiếp). Lệnh này tự sinh bản dịch và danh sách thiệp Android, kiểm tra lỗi rồi commit + push. Danh sách thiệp nằm ở một chỗ: `design/cards.py`. Chi tiết: `design/QUY-UOC.md`.
