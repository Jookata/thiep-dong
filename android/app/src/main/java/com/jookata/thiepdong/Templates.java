package com.jookata.thiepdong;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Danh sách mẫu, chia theo nhóm.
 * Thêm mẫu mới: thêm thư mục docs/<ten>/ rồi thêm một dòng vào ALL.
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
            new Template("noel", "noel", "xmas", R.string.tpl_noel_title, R.string.tpl_noel_desc, R.drawable.cover_noel),
            new Template("santa", "santa", "xmas", R.string.tpl_santa_title, R.string.tpl_santa_desc, R.drawable.cover_santa)
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
