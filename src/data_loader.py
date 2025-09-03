import xml.etree.ElementTree as ET
import pandas as pd
from pathlib import Path

def load_annotations(xml_path: Path, images_dir: Path, limit: int = None):
    tree = ET.parse(str(xml_path))
    root = tree.getroot()
    records = []
    for img in root.findall("image"):
        fn = img.attrib["name"]
        for box in img.findall("box"):
            if box.attrib["label"] != "plate":
                continue
            coords = [float(box.attrib[a]) for a in ("xtl","ytl","xbr","ybr")]
            text = next(
                (att.text.strip() for att in box.findall("attribute") if att.attrib["name"] == "plate number"),
                ""
            )
            records.append([fn, *coords, text])
    df = pd.DataFrame(records, columns=["filename","xmin","ymin","xmax","ymax","plate_text"])
    unique_files = df["filename"].unique().tolist()
    if limit:
        unique_files = unique_files[:limit]
    return df, unique_files
