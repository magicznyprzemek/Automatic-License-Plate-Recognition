import time
import cv2
from .data_loader import load_annotations
from .detector import PlateDetector
from .utils import compute_iou, calculate_final_grade

def main(args):
    df, files = load_annotations(args.annotations, args.images, limit=args.limit)
    detector = PlateDetector(args.yolo_weights, use_gpu=args.use_gpu)
    correct, iou_list = 0, []
    start = time.time()

    for fn in files:
        img = cv2.imread(str(args.images / fn))
        if img is None:
            continue
        pred_box, recog = detector.detect_and_recognize(img)
        gt = df[df.filename == fn].iloc[0]
        gt_box = list(map(int, gt[["xmin","ymin","xmax","ymax"]]))
        gt_text = gt.plate_text.replace(" ","").replace("-","").upper()

        if pred_box:
            if recog == gt_text:
                correct += 1
            iou_list.append(compute_iou(pred_box, gt_box))
        else:
            iou_list.append(0.0)

    total_time = time.time() - start
    acc = 100 * correct / len(files)
    grade = calculate_final_grade(acc, total_time)

    print(f"Images: {len(files)}")
    print(f"Accuracy: {acc:.2f}%")
    print(f"Total time: {total_time:.2f}s")
    print(f"Grade: {grade}")
