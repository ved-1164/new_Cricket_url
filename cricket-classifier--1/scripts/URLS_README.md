# 🏏 Cricket Shot URL Dataset — `urls_by_class.yaml`

This file contains curated YouTube video URLs organized by **cricket batting shot class**.  
These videos are used as the raw data source for training the cricket shot classifier.  
The download script (`download_videos.py`) reads this file and saves each video into  
`data/raw_videos/<class>/`, so clips automatically inherit their class label.

> 📌 **This is `cricket-classifier--1` (Version 2)** — the extended dataset with 64 URLs.  
> For the original dataset (60 URLs), see `cricket-classifier-`.

---

## 📦 Dataset Summary

| Shot Class    | Total URLs | Source Breakdown                     |
|---------------|------------|---------------------------------------|
| `drive`       | 4          | 4 YouTube videos                      |
| `cut`         | 12         | 5 YouTube videos + 7 Shorts           |
| `pull_hook`   | 14         | 4 YouTube videos + 10 Shorts          |
| `sweep`       | 14         | 3 YouTube videos + 11 Shorts          |
| `defensive`   | 1          | 1 YouTube video                       |
| `glance`      | 6          | 6 Shorts                              |
| `innovative`  | 13         | 13 YouTube videos                     |
| `other`       | 0          | *(empty — reserved for future use)*   |
| **Total**     | **64**     |                                       |

---

## 🎯 Shot Classes

### 🟢 `drive` — 4 URLs
Straight, cover, and off-drives. Predominantly front-foot shots played along the ground.

| # | URL |
|---|-----|
| 1 | https://youtu.be/nPBgrDjRCcg |
| 2 | https://youtu.be/5p82ZiV8x7g |
| 3 | https://youtu.be/oruAq_GSLZ4 |
| 4 | https://youtu.be/Z2TMN715wmY |

---

### 🔵 `cut` — 12 URLs
Late cut and square cut shots played off short-pitched deliveries outside off stump.

| # | URL |
|---|-----|
| 1 | https://youtu.be/KBjsnhn6O2M |
| 2 | https://youtu.be/woRWcqgxnkM |
| 3 | https://youtu.be/MHXfJBF9b50 |
| 4 | https://youtu.be/LaeT_PTtdR4 |
| 5 | https://youtu.be/57VC_XG3CV8 |
| 6 | https://youtube.com/shorts/BmHPF5FBZ2Q |
| 7 | https://youtube.com/shorts/KIIcmo33rkA |
| 8 | https://youtube.com/shorts/jXbbcduGM3A |
| 9 | https://youtube.com/shorts/t0FcKVcMbWM |
| 10 | https://youtube.com/shorts/UA8OnOK2yhI |
| 11 | https://youtube.com/shorts/VVohPxkUbTQ |
| 12 | https://youtube.com/shorts/bKYOfYPI5_w |

---

### 🟠 `pull_hook` — 14 URLs
Pull and hook shots played against short-pitched deliveries targeting the body/head.

| # | URL |
|---|-----|
| 1 | https://youtu.be/NuhXrcjajaA |
| 2 | https://youtu.be/Ood03gSwnH4 |
| 3 | https://youtu.be/B2OXTZlHyUw |
| 4 | https://youtu.be/CUMiqWWtCZY |
| 5 | https://youtube.com/shorts/A_73UB5aBzQ |
| 6 | https://youtube.com/shorts/W27filBdIEc |
| 7 | https://youtube.com/shorts/WtgHTWzM3JY |
| 8 | https://youtube.com/shorts/4pwl3k9_Fcg |
| 9 | https://youtube.com/shorts/pAsw8GLvm_s |
| 10 | https://youtube.com/shorts/nU6nEmy7Iqw |
| 11 | https://youtube.com/shorts/nx4W2VYBwqM |
| 12 | https://youtube.com/shorts/-yKm6t5prvI |
| 13 | https://youtube.com/shorts/GCIf1BnxkQo |
| 14 | https://youtu.be/tQ6TDYtH8-U |

---

### 🟡 `sweep` — 14 URLs
Sweep shots played against spin, including paddle sweep and reverse sweep variations.

| # | URL |
|---|-----|
| 1 | https://youtu.be/EzH1F4XWZlw |
| 2 | https://youtu.be/57tCYf39gYY |
| 3 | https://youtu.be/fpLAkPx3s4s |
| 4 | https://youtube.com/shorts/njIyB--SHkQ |
| 5 | https://youtube.com/shorts/PHfwNK-hux8 |
| 6 | https://youtube.com/shorts/1Rpovdn3sW0 |
| 7 | https://youtube.com/shorts/TMKCUGXo8yg |
| 8 | https://youtube.com/shorts/RuGGRCSWc0E |
| 9 | https://youtube.com/shorts/X1ueUnnhAv0 |
| 10 | https://youtube.com/shorts/qEpgkJdl6B4 |
| 11 | https://youtube.com/shorts/KtaIWlcQ068 |
| 12 | https://youtube.com/shorts/nPAIwTlao3w |
| 13 | https://youtube.com/shorts/tJJBsEx-9oM |
| 14 | https://youtube.com/shorts/3Lhmoq1_pWs |

---

### 🛡️ `defensive` — 1 URL
Defensive pushes, both forward and back-foot, used to block deliveries.

> ⚠️ **Underrepresented class** — only 1 URL. Consider adding more before training.

| # | URL |
|---|-----|
| 1 | https://youtu.be/XAvMBiE3vk4 |

---

### 🔴 `glance` — 6 URLs
Leg glance / flick off the pads, typically played to fine-leg or square-leg.

| # | URL |
|---|-----|
| 1 | https://youtube.com/shorts/o7GZOCroNks |
| 2 | https://youtube.com/shorts/VEJljiJ0_ps |
| 3 | https://youtube.com/shorts/tdK3Sa7zyGk |
| 4 | https://youtube.com/shorts/LGO5p40-LG8 |
| 5 | https://youtube.com/shorts/O0xJ_bMWAD0 |
| 6 | https://youtube.com/shorts/utnTcV0oubk |

---

### 🟣 `innovative` — 13 URLs
Unorthodox and modern shots — scoops, ramps, switch-hits, Dilscoop, reverse hits, etc.

| # | URL |
|---|-----|
| 1 | https://youtu.be/iWSOLsz8zgQ |
| 2 | https://youtu.be/WFZerO-Se3I |
| 3 | https://youtu.be/xSPhnvWQRjE |
| 4 | https://youtu.be/yWZx0c45Yx8 |
| 5 | https://youtu.be/GjAoL-da7UU |
| 6 | https://youtu.be/nGko70vxgLk |
| 7 | https://youtu.be/FuhmIyKzG-4 |
| 8 | https://youtu.be/3-poARm43qU |
| 9 | https://youtu.be/U7Op519aeD0 |
| 10 | https://youtu.be/o83vJITr0_Y |
| 11 | https://youtu.be/RPdKNlfQ_7Y |
| 12 | https://youtu.be/PiOnPQgF-FM |
| 13 | https://youtu.be/hQZnqOc0s2I |

---

### ⚪ `other` — 0 URLs
Reserved for miscellaneous or ambiguous shots not fitting any defined class. Currently empty.

---

## 🚀 How to Use

### Download all videos
```bash
python scripts/download_videos.py
```
Videos will be saved to `data/raw_videos/<class>/` automatically.

### Add new URLs
Edit `urls_by_class.yaml` and add entries under the appropriate class:
```yaml
drive:
  urls:
    - https://youtu.be/your_new_url_here
```

---

## ⚠️ Class Imbalance Warning

The dataset is **not balanced**. Before training, consider:
- Adding more `defensive` videos (currently only **1**)
- Over-sampling underrepresented classes
- Using the `class_weights.json` file to apply weighted loss during training

| Class | Count | Status |
|-------|-------|--------|
| `drive` | 4 | ⚠️ Low |
| `cut` | 12 | ✅ OK |
| `pull_hook` | 14 | ✅ OK |
| `sweep` | 14 | ✅ OK |
| `defensive` | 1 | 🔴 Critical |
| `glance` | 6 | ⚠️ Low |
| `innovative` | 13 | ✅ OK |
| `other` | 0 | ⬜ Empty |

---

## 📁 Related Files

| File | Purpose |
|------|---------|
| `scripts/download_videos.py` | Downloads videos from this YAML |
| `scripts/segment_clips.py` | Segments downloaded videos into clips |
| `scripts/extract_poses.py` | Extracts pose keypoints from clips |
| `scripts/make_splits.py` | Generates train/val/test splits |
| `data/splits/class_index.json` | Maps class names to integer labels |
| `data/splits/class_weights.json` | Per-class weights for loss balancing |

---

*Last updated: May 2026 | Part of the Cricket Shot Classifier project by ved-1164*
