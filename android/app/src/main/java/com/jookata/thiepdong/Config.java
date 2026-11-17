package com.jookata.thiepdong;

/** Cấu hình dùng chung. Đổi WEB_BASE nếu anh dùng tên miền riêng. */
final class Config {
    /** Nơi đặt thư mục docs/ (GitHub Pages). Link người gửi chia sẻ sẽ trỏ về đây. */
    static final String WEB_BASE = "https://jookata.github.io/thiep-dong/";
    /** Bản nhúng trong app, dùng cho "Xem thử". */
    static final String ASSET_BASE = "file:///android_asset/";

    static final int MAX_NAME = 30;
    static final int MAX_MSG = 160;

    private Config() {}
}
