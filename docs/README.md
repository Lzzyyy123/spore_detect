# ACF-YOLOv8s

ACF-YOLOv8s: an Enhanced YOLOv8 Model for Detection of Fungal Spores with Various Morphological Variants

## Getting Started

### Installation

- Clone this repo:

  ```
  git clone git@github.com:Lzzyyy123/spore_detect.git
  cd spore_detect
  ```

- Install prerequisites with:

  ```
  pip install -r requirements.txt
  ```

### Data preparation

- dataset

  The dataset is available here: https://pan.baidu.com/s/1fmQIBgKf211UiXL81LGNVA?pwd=1234 (extraction code: 1234)

- route

  Replace the train/val/test path in 

  ```
  dataset/data.yaml
  ```

### Val

run val.py or 

cli:

```
python val.py
```

results in:

```
runs/val/ACF-YOLO
```

### Train

run train.py or

cli:

```
python val.py
```

results in:

```
runs/train/ACF-YOLO
```

