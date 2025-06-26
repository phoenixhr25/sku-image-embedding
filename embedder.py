import mediapipe as mp
import numpy as np
from PIL import Image
import io
import requests

# Set up MediaPipe Image Embedder
mp_image = mp.Image
mp_embedder = mp.tasks.vision.ImageEmbedder
BaseOptions = mp.tasks.BaseOptions
ImageEmbedderOptions = mp.tasks.vision.ImageEmbedderOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = ImageEmbedderOptions(
    base_options=BaseOptions(model_asset_path=mp_embedder.MODULE_PATH),
    running_mode=VisionRunningMode.IMAGE
)
embedder = mp_embedder.create_from_options(options)

def generate_embedding_from_url(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            image = Image.open(io.BytesIO(response.content)).convert("RGB")
            np_image = np.array(image)
            mp_img = mp.Image(image_format=mp.ImageFormat.SRGB, data=np_image)
            result = embedder.embed(mp_img)
            return result.embeddings[0].embedding
    except:
        return None
