package com.jookata.thiepdong;

import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.android.gms.ads.AdRequest;
import com.google.android.gms.ads.AdView;
import com.google.android.gms.ads.MobileAds;

/** Màn chọn mẫu thiệp. */
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        SystemBars.pad(findViewById(R.id.root));

        MobileAds.initialize(this, status -> { });
        AdView adView = findViewById(R.id.adView);
        adView.loadAd(new AdRequest.Builder().build());

        RecyclerView list = findViewById(R.id.list);
        list.setLayoutManager(new LinearLayoutManager(this));
        list.setAdapter(new TemplateAdapter());
    }

    private void open(Template t) {
        Intent i = new Intent(this, CreateActivity.class);
        i.putExtra(CreateActivity.EXTRA_TEMPLATE, t.id);
        startActivity(i);
    }

    private final class TemplateAdapter extends RecyclerView.Adapter<TemplateAdapter.Holder> {
        @NonNull
        @Override
        public Holder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
            View v = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_template, parent, false);
            return new Holder(v);
        }

        @Override
        public void onBindViewHolder(@NonNull Holder h, int position) {
            final Template t = Templates.ALL.get(position);
            h.cover.setImageResource(t.coverRes);
            h.title.setText(t.titleRes);
            h.desc.setText(t.descRes);
            h.itemView.setOnClickListener(v -> open(t));
            h.use.setOnClickListener(v -> open(t));
        }

        @Override
        public int getItemCount() {
            return Templates.ALL.size();
        }

        final class Holder extends RecyclerView.ViewHolder {
            final ImageView cover;
            final TextView title;
            final TextView desc;
            final View use;

            Holder(@NonNull View v) {
                super(v);
                cover = v.findViewById(R.id.cover);
                title = v.findViewById(R.id.title);
                desc = v.findViewById(R.id.desc);
                use = v.findViewById(R.id.btn_use);
            }
        }
    }
}
