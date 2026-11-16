package com.jookata.thiepdong;

import android.net.Uri;

/** Ghép link thiệp: tên người nhận, người gửi, lời chúc, ngôn ngữ nằm ngay trong link. */
final class LinkBuilder {

    /**
     * @param base  Config.WEB_BASE (link chia sẻ) hoặc Config.ASSET_BASE (xem thử trong app)
     * @param asset true nếu là file nhúng trong app (phải ghi rõ index.html)
     */
    static String build(String base, Template t, String to, String from, String msg, String lang, boolean asset) {
        String page = base + t.path + "/" + (asset ? "index.html" : "");
        Uri.Builder b = Uri.parse(page).buildUpon();
        if (!to.isEmpty()) b.appendQueryParameter("to", to);
        if (!from.isEmpty()) b.appendQueryParameter("from", from);
        if (!msg.isEmpty()) b.appendQueryParameter("msg", msg);
        b.appendQueryParameter("lang", lang);
        return b.build().toString();
    }

    private LinkBuilder() {}
}
