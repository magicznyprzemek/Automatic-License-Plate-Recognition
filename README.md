# License Plate Recognition 

This repository implements an end-to-end solution for Automatic License Plate Recognition (ALPR). It reads raw images and XML annotations, detects license plates with a pretrained YOLO model, runs OCR on detected crops, and computes metrics such as detection IoU and OCR accuracy.

To repozytorium zawiera kompleksowe rozwiązanie do automatycznego rozpoznawania tablic rejestracyjnych (ALPR). Wczytuje surowe obrazy i adnotacje w formacie XML, wykrywa tablice modelem YOLO, wykonuje OCR na wyciętych fragmentach i oblicza metryki, takie jak IoU detekcji oraz dokładność OCR.

## Setup ENG

1. Clone the repository
   `git clone https://github.com/magicznyprzemek/Automatic-License-Plate-Recognition`

2. Create a virtual environment
   `python3 -m venv venv && source venv/bin/activate`

3. Install dependencies 
   `pip install --upgrade pip`  
   `pip install -r requirements.txt`

4. Place your dataset into the data/raw folder (photos and annotations)
   `python3 scripts/download_dataset.py`

6. Run the license-plate detector accuracy evaluation
   `python3 -m scripts.run_evaluation \
  --images data/raw/photos \
  --annotations data/raw/annotations.xml \
  --yolo_weights weights/yolov5s.pt \
  --limit 100 \
  --use_gpu`

## Setup PL

1. Sklonuj repozytorium  
   `git clone https://github.com/magicznyprzemek/Automatic-License-Plate-Recognition`

2. Stwórz wirtualne środowisko  
   `python3 -m venv venv && source venv/bin/activate`

3. Zainstaluj zależności  
   `pip install --upgrade pip`  
   `pip install -r requirements.txt`

4. Umieść dane w folderze `data` (photos i annotations) 
   `python3 scripts/download_dataset.py`

6. Uruchom ocenę dokładnosci detektora tablic rejestracyjnych
   `python3 -m scripts.run_evaluation \
  --images data/raw/photos \
  --annotations data/raw/annotations.xml \
  --yolo_weights weights/yolov5s.pt \
  --limit 100 \
  --use_gpu`
