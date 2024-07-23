import os, tqdm
from ultralytics import YOLO

if __name__ == '__main__':
    error_result = []
    for yaml_path in tqdm.tqdm(os.listdir("AFM-YOLOv8s.yaml")):
        if 'rtdetr' not in yaml_path and 'detect' not in yaml_path:
            try:
                model = YOLO(f'{yaml_path}')
                model.info(detailed=True)
                model.profile([640, 640])
                model.fuse()
            except Exception as e:
                error_result.append(f'{yaml_path} {e}')
    
    for i in error_result:
        print(i)