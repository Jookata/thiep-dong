package com.jookata.thiepdong;

/** Một mẫu thiệp. "path" là tên thư mục trong docs/ (ví dụ "noel"). "category" là id nhóm (xem Templates.CATEGORIES). */
final class Template {
    final String id;
    final String path;
    final String category;
    final int titleRes;
    final int descRes;
    final int coverRes;

    Template(String id, String path, String category, int titleRes, int descRes, int coverRes) {
        this.id = id;
        this.path = path;
        this.category = category;
        this.titleRes = titleRes;
        this.descRes = descRes;
        this.coverRes = coverRes;
    }
}
