package com.jookata.thiepdong;

import android.content.ClipData;
import android.content.ClipboardManager;
import android.content.Intent;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.google.android.gms.ads.AdRequest;
import com.google.android.gms.ads.AdView;

import java.util.Locale;

/** Màn nhập tên người nhận/người gửi, xem thử và chia sẻ link. */
public class CreateActivity extends AppCompatActivity {
    static final String EXTRA_TEMPLATE = "template";

    private Template template;
    private EditText etTo;
    private EditText etFrom;
    private EditText etMsg;
    private Spinner spLang;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        template = Templates.find(getIntent().getStringExtra(EXTRA_TEMPLATE));
        if (template == null) {
            finish();
            return;
        }

        setContentView(R.layout.activity_create);
        SystemBars.pad(findViewById(R.id.root));

        etTo = findViewById(R.id.et_to);
        etFrom = findViewById(R.id.et_from);
        etMsg = findViewById(R.id.et_msg);
        spLang = findViewById(R.id.sp_lang);
        String[] names = new String[Lang.ALL.length];
        for (int k = 0; k < names.length; k++) names[k] = Lang.ALL[k].name;
        ArrayAdapter<String> la = new ArrayAdapter<>(this, android.R.layout.simple_spinner_item, names);
        la.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spLang.setAdapter(la);
        // Mặc định theo ngôn ngữ của máy
        spLang.setSelection(Lang.defaultIndex(Locale.getDefault()));

        findViewById(R.id.btn_preview).setOnClickListener(v -> preview());
        findViewById(R.id.btn_share).setOnClickListener(v -> share());
        findViewById(R.id.btn_copy).setOnClickListener(v -> copy());

        AdView adView = findViewById(R.id.adView);
        adView.loadAd(new AdRequest.Builder().build());
    }

    private String text(EditText e, int max) {
        String s = e.getText().toString().trim();
        return s.length() > max ? s.substring(0, max) : s;
    }

    private Lang lang() {
        return Lang.ALL[spLang.getSelectedItemPosition()];
    }

    private String link(boolean asset) {
        return LinkBuilder.build(asset ? Config.ASSET_BASE : Config.WEB_BASE, template,
                text(etTo, Config.MAX_NAME), text(etFrom, Config.MAX_NAME), text(etMsg, Config.MAX_MSG),
                lang().code, asset);
    }

    private void preview() {
        Intent i = new Intent(this, PreviewActivity.class);
        i.putExtra(PreviewActivity.EXTRA_URL, link(true));
        startActivity(i);
    }

    private void share() {
        String intro = lang().intro;
        Intent send = new Intent(Intent.ACTION_SEND);
        send.setType("text/plain");
        send.putExtra(Intent.EXTRA_TEXT, intro + "\n" + link(false));
        startActivity(Intent.createChooser(send, getString(R.string.share_chooser)));
    }

    private void copy() {
        ClipboardManager cm = (ClipboardManager) getSystemService(CLIPBOARD_SERVICE);
        if (cm != null) {
            cm.setPrimaryClip(ClipData.newPlainText("card", link(false)));
            Toast.makeText(this, R.string.copied, Toast.LENGTH_SHORT).show();
        }
    }
}
