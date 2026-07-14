import cv2
import numpy as np

def compute_memnet_score(image_path, model_weights, model_def):
    # 1. Load the Caffe model into OpenCV's DNN module
    net = cv2.dnn.readNetFromCaffe(model_def, model_weights)
    
    # 2. Load the image you want to analyze
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Could not load image at {image_path}")
        
    # 3. Preprocess the image according to MemNet specifications:
    # - Resizes the image to 227x227 pixels
    # - Subtracts the official ImageNet training mean values (BGR order)
    blob = cv2.dnn.blobFromImage(
        image, 
        scalefactor=1.0, 
        size=(227, 227), 
        mean=(104.0, 117.0, 123.0), 
        swapRB=False, 
        crop=True
    )
    
    # 4. Pass the processed image tensor through MemNet
    net.setInput(blob)
    output = net.forward()
    
    # 5. Extract the final floating-point memorability score
    memorability_score = float(output[0][0])
    return memorability_score

# --- Execution ---
if __name__ == "__main__":
    MODEL_DEF = "deploy.prototxt"
    MODEL_WEIGHTS = "external_predictor.caffemodel"
    
    # Target image file
    IMAGE_PATH = "vhighmem.jpeg" 
    
    try:
        score = compute_memnet_score(IMAGE_PATH, MODEL_WEIGHTS, MODEL_DEF)
        print("\n" + "="*30)
        print(f"Image analyzed: {IMAGE_PATH}")
        print(f"MemNet Memorability Score: {score:.4f}")
        print("="*30)
    except Exception as e:
        print(f"Error running MemNet: {e}")
