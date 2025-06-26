def load_urls_from_file(filepath):
    pairs = []
    with open(filepath, "r") as f:
        for line in f:
            if "," in line:
                sku_id, url = line.strip().split(",", 1)
                pairs.append((sku_id.strip(), url.strip()))
    return pairs
