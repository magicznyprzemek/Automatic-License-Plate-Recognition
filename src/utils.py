def normalize(text: str) -> str:
    return text.replace(" ", "").replace("-", "").replace("=", "").upper()

def compute_iou(boxA, boxB) -> float:
    xA, yA = max(boxA[0], boxB[0]), max(boxA[1], boxB[1])
    xB, yB = min(boxA[2], boxB[2]), min(boxA[3], boxB[3])
    inter = max(0, xB - xA) * max(0, yB - yA)
    areaA = (boxA[2]-boxA[0]) * (boxA[3]-boxA[1])
    areaB = (boxB[2]-boxB[0]) * (boxB[3]-boxB[1])
    return inter / (areaA + areaB - inter + 1e-6)

def calculate_final_grade(acc: float, t: float) -> float:
    if acc < 60 or t > 60:
        return 2.0
    a_norm = (acc - 60) / 40
    t_norm = (60 - t) / 50
    score = 0.7 * a_norm + 0.3 * t_norm
    return round((2.0 + 3.0 * score) * 2) / 2
