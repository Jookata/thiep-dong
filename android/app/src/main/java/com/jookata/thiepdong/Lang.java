package com.jookata.thiepdong;

/** FILE SINH TỰ ĐỘNG từ design/build_i18n.py. Danh sách ngôn ngữ của thiệp. */
final class Lang {
    final String code;
    final String name;
    final String intro;

    Lang(String code, String name, String intro) {
        this.code = code;
        this.name = name;
        this.intro = intro;
    }

    static final Lang[] ALL = {
            new Lang("vi", "Tiếng Việt", "Mình gửi bạn một tấm thiệp động, chạm vào để mở nhé:"),
            new Lang("en", "English", "I made an animated card for you. Tap to open it:"),
            new Lang("fr", "Français", "Je t’ai fait une carte animée. Touche pour l’ouvrir :"),
            new Lang("de", "Deutsch", "Ich habe dir eine animierte Karte gemacht. Tippe, um sie zu öffnen:"),
            new Lang("it", "Italiano", "Ho creato un biglietto animato per te. Tocca per aprirlo:"),
            new Lang("pl", "Polski", "Zrobiłem dla ciebie animowaną kartkę. Dotknij, aby ją otworzyć:"),
            new Lang("fi", "Suomi", "Tein sinulle animoidun kortin. Avaa se napauttamalla:"),
            new Lang("es", "Español", "Te hice una tarjeta animada. Toca para abrirla:"),
            new Lang("pt", "Português", "Fiz um cartão animado para você. Toque para abrir:"),
            new Lang("sk", "Slovenčina", "Urobil som pre teba animovanú pohľadnicu. Ťukni a otvor ju:"),
            new Lang("ko", "한국어", "움직이는 카드를 만들었어요. 눌러서 열어 보세요:"),
            new Lang("ja", "日本語", "動くカードを作ったよ。タップして開いてね："),
            new Lang("zh", "简体中文", "我为你做了一张动态贺卡，点开看看吧："),
            new Lang("zh-TW", "繁體中文", "我為你做了一張動態賀卡，點開看看吧："),
            new Lang("th", "ไทย", "ฉันทำการ์ดภาพเคลื่อนไหวมาให้ แตะเพื่อเปิดดูนะ:"),
            new Lang("ms", "Bahasa Melayu", "Saya buat kad animasi untuk awak. Sentuh untuk membukanya:"),
    };

    /** Chọn ngôn ngữ thiệp mặc định theo ngôn ngữ của máy. */
    static int defaultIndex(java.util.Locale loc) {
        String l = loc.getLanguage();
        String c = l;
        if ("zh".equals(l)) {
            String r = loc.getCountry();
            c = ("TW".equals(r) || "HK".equals(r) || "MO".equals(r) || "Hant".equals(loc.getScript())) ? "zh-TW" : "zh";
        }
        for (int i = 0; i < ALL.length; i++) if (ALL[i].code.equals(c)) return i;
        return 1; // English
    }

}
