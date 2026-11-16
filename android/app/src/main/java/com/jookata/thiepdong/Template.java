package com.jookata.thiepdong;

/** Một mẫu thiệp. "path" là tên thư mục trong docs/ (ví dụ "noel"). */
final class Template {
    final String id;
    final String path;
    final int titleRes;
    final int descRes;
    final int coverRes;

    Template(String id, String path, int titleRes, int descRes, int coverRes) {
        this.id = id;
        this.path = path;
        this.titleRes = titleRes;
        this.descRes = descRes;
        this.coverRes = coverRes;
    }
}
