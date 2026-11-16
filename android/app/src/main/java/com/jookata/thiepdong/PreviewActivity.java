package com.jookata.thiepdong;

import android.annotation.SuppressLint;
import android.graphics.Color;
import android.os.Bundle;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import androidx.appcompat.app.AppCompatActivity;

/** Xem thử thiệp: chạy chính trang web nhúng trong app (chỉ cho phép file trong assets). */
public class PreviewActivity extends AppCompatActivity {
    static final String EXTRA_URL = "url";

    private WebView web;

    @SuppressLint("SetJavaScriptEnabled")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        String url = getIntent().getStringExtra(EXTRA_URL);
        if (url == null || !url.startsWith(Config.ASSET_BASE)) {
            finish();
            return;
        }

        setContentView(R.layout.activity_preview);
        SystemBars.pad(findViewById(R.id.root));

        web = findViewById(R.id.web);
        web.setBackgroundColor(Color.parseColor("#04070D"));
        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        s.setMediaPlaybackRequiresUserGesture(false);
        s.setAllowContentAccess(false);
        web.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
                // Chặn mọi điều hướng ra ngoài thư mục assets
                return !request.getUrl().toString().startsWith(Config.ASSET_BASE);
            }
        });
        web.loadUrl(url);
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (web != null) web.onPause();
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (web != null) web.onResume();
    }

    @Override
    protected void onDestroy() {
        if (web != null) {
            web.stopLoading();
            web.destroy();   // dừng nhạc khi thoát
            web = null;
        }
        super.onDestroy();
    }
}
