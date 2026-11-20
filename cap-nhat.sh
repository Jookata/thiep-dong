#!/bin/bash
# Cập nhật thiệp + app Android lên GitHub chỉ bằng MỘT lệnh (chạy trong thư mục repo đã clone trên máy anh):
#   ./cap-nhat.sh ~/Downloads/thiep-dong.zip "Thêm thiệp Tết"     # nhận file zip mới rồi đẩy lên
#   ./cap-nhat.sh "Sửa chữ thiệp noel"                            # đã sửa trực tiếp trong thư mục, chỉ đẩy lên
set -e
cd "$(dirname "$0")"
ZIP=""; MSG="Cập nhật thiệp"
if [ -n "$1" ] && [ "${1##*.}" = "zip" ]; then ZIP="$1"; MSG="${2:-$MSG}"; elif [ -n "$1" ]; then MSG="$1"; fi
if [ -n "$ZIP" ]; then
  T=$(mktemp -d); unzip -q "$ZIP" -d "$T"; S="$T/thiep-dong"; [ -d "$S" ] || S="$T"
  # docs/ và design/ đồng bộ đúng như bản mới (file nào bỏ đi thì xóa theo); android/ và store/ chỉ ghi đè/thêm
  rm -rf docs design; cp -R "$S/docs" docs; cp -R "$S/design" design; rm -rf design/__pycache__
  cp -R "$S/android/." android/
  cp -R "$S/store/." store/
  cp "$S/README.md" README.md; cp "$S/cap-nhat.sh" cap-nhat.sh 2>/dev/null || true
  mkdir -p .github && [ -d "$S/.github" ] && cp -R "$S/.github/." .github/
  rm -rf "$T"
fi
python3 design/build_i18n.py     # sinh lại bản dịch + danh sách thiệp Android (an toàn khi chạy lại)
python3 design/check.py          # dừng nếu thiếu file hoặc lỗi cú pháp
git add -A
git commit -m "$MSG" || echo "Không có thay đổi mới."
git push
echo "Xong. Web (GitHub Pages) và mã Android đã nằm chung một lần đẩy."
