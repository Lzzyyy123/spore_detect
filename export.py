import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

# onnx onnxsim onnxruntime onnxruntime-gpu

if __name__ == '__main__':
    model = YOLO('AFM-YOLOv8s.pt')
    model.export(format='onnx', simplify=True, opset=13)