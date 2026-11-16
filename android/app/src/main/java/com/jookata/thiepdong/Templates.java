package com.jookata.thiepdong;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/** Danh sách mẫu. Thêm mẫu mới: thêm thư mục docs/<ten>/ và một dòng ở đây. */
final class Templates {
    static final List<Template> ALL = Collections.unmodifiableList(Arrays.asList(
            new Template("noel", "noel", R.string.tpl_noel_title, R.string.tpl_noel_desc, R.drawable.cover_noel)
    ));

    static Template find(String id) {
        for (Template t : ALL) {
            if (t.id.equals(id)) return t;
        }
        return null;
    }

    private Templates() {}
}
