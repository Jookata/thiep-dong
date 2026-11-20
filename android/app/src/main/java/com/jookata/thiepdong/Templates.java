package com.jookata.thiepdong;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Danh sách mẫu, chia theo nhóm.
 * Thêm mẫu mới: thêm một dòng vào design/cards.py rồi chạy design/build_i18n.py (ALL bên dưới được sinh tự động).
 * Thêm nhóm mới: thêm một dòng vào CATEGORIES (và chuỗi cat_* trong design/i18n_src_c.py).
 */
final class Templates {
    static final class Category {
        final String id;
        final int nameRes;

        Category(String id, int nameRes) {
            this.id = id;
            this.nameRes = nameRes;
        }
    }

    static final List<Category> CATEGORIES = Collections.unmodifiableList(Arrays.asList(
            new Category("xmas", R.string.cat_xmas),
            new Category("birthday", R.string.cat_birthday),
            new Category("newyear", R.string.cat_newyear)
    ));

    static final List<Template> ALL = Collections.unmodifiableList(Arrays.asList(
            // BEGIN-GEN (sinh tự động từ design/cards.py bởi design/build_i18n.py, đừng sửa tay)
            new Template("noel", "noel", "xmas", R.string.tpl_noel_title, R.string.tpl_noel_desc, R.drawable.cover_noel),
            new Template("santa", "santa", "xmas", R.string.tpl_santa_title, R.string.tpl_santa_desc, R.drawable.cover_santa),
            new Template("catch", "catch", "xmas", R.string.tpl_catch_title, R.string.tpl_catch_desc, R.drawable.cover_catch),
            new Template("flappy", "flappy", "xmas", R.string.tpl_flappy_title, R.string.tpl_flappy_desc, R.drawable.cover_flappy),
            new Template("yuki", "yuki", "xmas", R.string.tpl_yuki_title, R.string.tpl_yuki_desc, R.drawable.cover_yuki),
            new Template("korea", "korea", "xmas", R.string.tpl_korea_title, R.string.tpl_korea_desc, R.drawable.cover_korea),
            new Template("birthday", "birthday", "birthday", R.string.tpl_birthday_title, R.string.tpl_birthday_desc, R.drawable.cover_birthday),
            new Template("nen", "nen", "birthday", R.string.tpl_nen_title, R.string.tpl_nen_desc, R.drawable.cover_nen),
            new Template("newyear", "newyear", "newyear", R.string.tpl_newyear_title, R.string.tpl_newyear_desc, R.drawable.cover_newyear)
            // END-GEN
    ));

    static List<Template> inCategory(String category) {
        List<Template> out = new ArrayList<>();
        for (Template t : ALL) {
            if (t.category.equals(category)) out.add(t);
        }
        return out;
    }

    static Template find(String id) {
        for (Template t : ALL) {
            if (t.id.equals(id)) return t;
        }
        return null;
    }

    private Templates() {}
}
