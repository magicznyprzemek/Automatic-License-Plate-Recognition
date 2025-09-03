#!/usr/bin/env python3
import argparse
from pathlib import Path
from src.evaluate import main


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--images",      type=Path, default="data/raw/photos")
    parser.add_argument("--annotations", type=Path, default="data/raw/annotations.xml")
    parser.add_argument( "--yolo_weights",  type = str,     default = "models/license_plate_detector.pt")
    parser.add_argument("--limit",       type=int,  default=100)
    parser.add_argument("--use_gpu",     action="store_true")
    args = parser.parse_args()
    main(args)
