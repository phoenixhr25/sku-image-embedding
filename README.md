# SKU Image Embedding Generator

This project uses Google's MediaPipe image embedding model to generate 1024-dimensional feature vectors for SKU product images from URLs.

## 🔧 Features

- Batch processing of SKU image URLs
- Generates 1024-dim vector embeddings using MediaPipe
- Saves results into a structured CSV file
- Easy to extend for downstream ML or similarity tasks

## 📦 Installation

```bash
pip install -r requirements.txt
```

## 🚀 Run

1. Place your SKU URLs in `data/sku_image_urls.txt` (format: `sku_id,image_url`)
2. Run:

```bash
python main.py
```

3. Output will be saved to `data/sku_image_embeddings.csv`

## 📁 Example Input (sku_image_urls.txt)

```
sku001,https://storage.googleapis.com/mediapipe-assets/image_embedder/cat.jpg
sku002,https://storage.googleapis.com/mediapipe-assets/image_embedder/cat.jpg
```

## ✨ Output Format (CSV)

- Column 1: SKU ID
- Column 2–1025: Embedding vector values

## 👤 Author

Avery · External Brain Project · 2025
