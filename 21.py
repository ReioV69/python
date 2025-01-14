# Reio Viikmaa 14.01.25
# 21
import os

    # Kontrolli, kas thumb kataloog on olemas, kui ei ole, siis loo see
thumb_dir = "img_thumb"
if not os.path.exists(thumb_dir):
        os.makedirs(thumb_dir)