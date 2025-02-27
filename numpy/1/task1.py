from PIL import Image
import numpy as np

def processing(file_path, pfile_path):
    img = Image.open(file_path)
    data = np.array(img)
    min = np.min(data)
    max = np.max(data)
    print(min, max)

    data_correct = np.clip((data - min) / (max - min) * 255, 0, 255).astype(np.uint8)

    min1 = np.min(data_correct)
    max1 = np.max(data_correct)
    print(min1, max1)

    image_correct = Image.fromarray(data_correct)
    image_correct.save(pfile_path)


for i in range(1, 4):
    file_path = f'lunar{i:02}_raw.jpg'
    pfile_path = f'lunar{i:02}_processed.jpg'
    processing(file_path, pfile_path)
