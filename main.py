from embedder import generate_embedding_from_url
from utils import load_urls_from_file
import csv
import os

input_file = "data/sku_image_urls.txt"
output_file = "data/sku_image_embeddings.csv"

urls = load_urls_from_file(input_file)

os.makedirs("data", exist_ok=True)
with open(output_file, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["sku_id"] + [f"dim_{i}" for i in range(1024)])
    for sku_id, url in urls:
        vector = generate_embedding_from_url(url)
        if vector:
            writer.writerow([sku_id] + list(vector))

print(f"✅ Embeddings saved to {output_file}")
