import os, shutil

src = "C:\\Users\\user\\Desktop\\Images"
dst = "C:\\Users\\user\\Desktop\\Jpg files"
os.makedirs(dst, exist_ok=True)

for file in os.listdir(src):
    if file.endswith(".jpg"):
        shutil.move(os.path.join(src, file), os.path.join(dst, file))
print("All .jpg files moved.")
