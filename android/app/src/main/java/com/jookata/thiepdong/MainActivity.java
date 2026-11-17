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
import com.google.android.material.tabs.TabLayout;

import java.util.ArrayList;
import java.util.List;

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
        final TemplateAdapter adapter = new TemplateAdapter();
        list.setAdapter(adapter);

        final TextView empty = findViewById(R.id.empty);
        TabLayout tabs = findViewById(R.id.tabs);
        for (Templates.Category c : Templates.CATEGORIES) {
            tabs.addTab(tabs.newTab().setText(c.nameRes));
        }
        tabs.addOnTabSelectedListener(new TabLayout.OnTabSelectedListener() {
            @Override
            public void onTabSelected(TabLayout.Tab tab) {
                show(adapter, empty, tab.getPosition());
            }

            @Override
            public void onTabUnselected(TabLayout.Tab tab) { }

            @Override
            public void onTabReselected(TabLayout.Tab tab) { }
        });
        show(adapter, empty, 0);
    }

    /** Hiện các mẫu thuộc nhóm đang chọn; nhóm chưa có mẫu thì báo "sắp ra mắt". */
    private void show(TemplateAdapter adapter, TextView empty, int categoryIndex) {
        String cat = Templates.CATEGORIES.get(categoryIndex).id;
        adapter.setItems(Templates.inCategory(cat));
        empty.setVisibility(adapter.getItemCount() == 0 ? View.VISIBLE : View.GONE);
    }

    private void open(Template t) {
        Intent i = new Intent(this, CreateActivity.class);
        i.putExtra(CreateActivity.EXTRA_TEMPLATE, t.id);
        startActivity(i);
    }

    private final class TemplateAdapter extends RecyclerView.Adapter<TemplateAdapter.Holder> {
        private List<Template> items = new ArrayList<>();

        void setItems(List<Template> list) {
            items = list;
            notifyDataSetChanged();
        }

        @NonNull
        @Override
        public Holder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
            View v = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_template, parent, false);
            return new Holder(v);
        }

        @Override
        public void onBindViewHolder(@NonNull Holder h, int position) {
            final Template t = items.get(position);
            h.cover.setImageResource(t.coverRes);
            h.title.setText(t.titleRes);
            h.desc.setText(t.descRes);
            h.itemView.setOnClickListener(v -> open(t));
            h.use.setOnClickListener(v -> open(t));
        }

        @Override
        public int getItemCount() {
            return items.size();
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
