# This is an example of a script in SCVU which is hanging on for dear life. It extracts data from a txt file, but fails when the txt file has incorrect formatting, namely non-numerical file data, missing coordinate points, insufficient coordinate points (<3), or coordinate values outside the expected range. 
# Refactor this code to implement error handling and appropriate logging, ensuring that it logs appropriate error messages, returning None and closing the file when an error occurs instead of crashing.


from typing import List, Tuple
import os

def load_yolo_labels(
    txt_path: str,
) -> List[Tuple[int, List[Tuple[float, float]]]]:
    """
    Load YOLO segmentation labels from file.

    Reads YOLO segmentation format labels where each line contains:
    class_id x1 y1 x2 y2 ... xn yn (normalized polygon coordinates which are each between 0 and 1)

    Returns list of (class_id, polygon_points) tuples. Returns empty list if file
    doesn't exist or is empty.
    """
    labels = []

    with open(txt_path, "r") as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split()
            cls_id = int(parts[0])
            coords = [
                (float(parts[i]), float(parts[i + 1]))
                for i in range(1, len(parts), 2)
            ]
            labels.append((cls_id, coords))

    return labels

labels_dir = ".labels"
for txt_path in os.listdir(labels_dir):
    if txt_path.endswith(".txt"):
        full_path = os.path.join(labels_dir, txt_path)
        print (f"Loading labels from {full_path}")
        labels = load_yolo_labels(full_path)
        print(f"Loaded labels: {labels}")