import cv2
from ultralytics import YOLO
from paddleocr import PaddleOCR
from .utils import normalize

class PlateDetector:
    def __init__(self, yolo_weights: str, use_gpu: bool = False):
        self.yolo = YOLO(yolo_weights)
        self.ocr = PaddleOCR(use_angle_cls=True, lang="en", use_gpu=use_gpu)

    def detect_and_recognize(self, image):
        # YOLO detection
        res = self.yolo(image)
        if not res or not res[0].boxes:
            return None, ""
        boxes = res[0].boxes.data.cpu().numpy()
        best = max(boxes, key=lambda b: b[4])
        x1,y1,x2,y2 = map(int, best[:4])
        crop = image[y1:y2, x1:x2]
        # OCR
        ocr_res = self.ocr.ocr(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB), cls=True)
        # wybór najlepszego tekstu
        candidates = []
        for line in (ocr_res[0] if ocr_res else []):
            txt, conf = line[1]
            candidates.append((normalize(txt), conf))
        if not candidates:
            return [x1,y1,x2,y2], ""
        return [x1,y1,x2,y2], max(candidates, key=lambda x: x[1])[0]
