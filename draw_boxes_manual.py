import cv2
import os
import re

# ==========================
# MANUAL IMAGE BOXER
# Draw boxes for every image
# ==========================

folder = input("Enter image folder path: ").strip()

output = os.path.join(folder, "boxed")
os.makedirs(output, exist_ok=True)

# --------------------------
# Load image files
# --------------------------
files = [f for f in os.listdir(folder)
         if f.lower().endswith((".jpg", ".jpeg", ".png"))]

# Sort by frame number if starts with number
def frame_num(name):
    m = re.match(r"(\d+)", name)
    return int(m.group(1)) if m else 999999

files.sort(key=frame_num)

print(f"Found {len(files)} images")

# --------------------------
# Process each image
# --------------------------
for i, file in enumerate(files):

    path = os.path.join(folder, file)
    img = cv2.imread(path)

    if img is None:
        continue

    clone = img.copy()

    print(f"\n[{i+1}/{len(files)}] {file}")
    print("Draw box and press ENTER")
    print("Press C to skip image")

    bbox = cv2.selectROI("Draw Box", img, False, False)
    cv2.destroyAllWindows()

    x, y, w, h = map(int, bbox)

    # Skip if no box drawn
    if w == 0 or h == 0:
        print("Skipped")
        continue

    # Draw rectangle
    cv2.rectangle(clone, (x, y), (x+w, y+h), (255,0,0), 2)

    save_path = os.path.join(output, file)
    cv2.imwrite(save_path, clone)

print("\nDone!")
