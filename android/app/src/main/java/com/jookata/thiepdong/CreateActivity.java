package com.jookata.thiepdong;

import android.content.ClipData;
import android.content.ClipboardManager;
import android.content.Intent;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.RadioButton;
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
    private RadioButton rbVi;

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
        rbVi = findViewById(R.id.rb_vi);
        RadioButton rbEn = findViewById(R.id.rb_en);

        // Mặc định theo ngôn ngữ của máy
        boolean vi = "vi".equals(Locale.getDefault().getLanguage());
        rbVi.setChecked(vi);
        rbEn.setChecked(!vi);

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

    private String lang() {
        return rbVi.isChecked() ? "vi" : "en";
    }

    private String link(boolean asset) {
        return LinkBuilder.build(asset ? Config.ASSET_BASE : Config.WEB_BASE, template,
                text(etTo, Config.MAX_NAME), text(etFrom, Config.MAX_NAME), text(etMsg, Config.MAX_MSG),
                lang(), asset);
    }

    private void preview() {
        Intent i = new Intent(this, PreviewActivity.class);
        i.putExtra(PreviewActivity.EXTRA_URL, link(true));
        startActivity(i);
    }

    private void share() {
        String intro = getString("vi".equals(lang()) ? R.string.share_intro_vi : R.string.share_intro_en);
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
