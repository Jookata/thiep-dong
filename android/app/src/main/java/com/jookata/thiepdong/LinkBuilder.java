package com.jookata.thiepdong;

import android.net.Uri;
import android.util.Base64;

import java.nio.charset.StandardCharsets;

/** Ghép link thiệp: tên người nhận, người gửi, lời chúc (đã mã hoá), ngôn ngữ nằm ngay trong link. */
final class LinkBuilder {

    /** Khoá XOR. Phải trùng với WC.KEY trong docs/i18n.js. Chỉ để link không đọc ra chữ, không phải bảo mật. */
    private static final String KEY = "w1nk-c4rd-2026";

    /** Lời chúc riêng -> base64url(XOR(UTF-8, KEY)). Trang web giải mã bằng WC.dec(). */
    static String encodeMsg(String msg) {
        byte[] u = msg.getBytes(StandardCharsets.UTF_8);
        byte[] k = KEY.getBytes(StandardCharsets.UTF_8);
        for (int i = 0; i < u.length; i++) {
            u[i] = (byte) (u[i] ^ k[i % k.length]);
        }
        return Base64.encodeToString(u, Base64.URL_SAFE | Base64.NO_WRAP | Base64.NO_PADDING);
    }

    /**
     * @param base  Config.WEB_BASE (link chia sẻ) hoặc Config.ASSET_BASE (xem thử trong app)
     * @param asset true nếu là file nhúng trong app (phải ghi rõ index.html)
     */
    static String build(String base, Template t, String to, String from, String msg, String lang, boolean asset) {
        String page = base + t.path + "/" + (asset ? "index.html" : "");
        Uri.Builder b = Uri.parse(page).buildUpon();
        if (!to.isEmpty()) b.appendQueryParameter("to", to);
        if (!from.isEmpty()) b.appendQueryParameter("from", from);
        if (!msg.isEmpty()) b.appendQueryParameter("m", encodeMsg(msg));
        b.appendQueryParameter("lang", lang);
        return b.build().toString();
    }

    private LinkBuilder() {}
}
