from PIL import Image

import tensorflow as tf
import numpy as np

from inference import Inferer

IMG_SIZE = 400

inferer = Inferer()

MODEL_DICT = {
    "dr": "Models/mirnet_dr.tflite",
    "fp16": "Models/mirnet_fp16.tflite",
    "int8": "Models/mirnet_int8.tflite"
}

def model_bild():
    
    inferer = Inferer()
    
    inferer.build_model(
    num_rrg=3, num_mrb=2, channels=64,
    weights_path='low_light_weights_best.h5'
    
    )
    
    print("sucess")
    


# def preprocess_image(image_path):
#     original_image = Image.open(image_path)
#     width, height = original_image.size
#     preprocessed_image = original_image.resize(
#         (
#             IMG_SIZE,
#             IMG_SIZE
#         ),
#         Image.ANTIALIAS)
#     preprocessed_image = tf.keras.preprocessing.image.img_to_array(preprocessed_image)
#     preprocessed_image = preprocessed_image.astype('float32') / 255.0
#     preprocessed_image = np.expand_dims(preprocessed_image, axis=0)
    
#     return original_image, preprocessed_image

# def infer_tflite(model_type, image):
#     # interpreter = tf.lite.Interpreter(model_path=MODEL_DICT[model_type])
#     # input_index = interpreter.get_input_details()[0]["index"]
#     # output_index = interpreter.get_output_details()[0]["index"]
    
#     # interpreter.allocate_tensors()
#     # interpreter.set_tensor(input_index, image)
#     # interpreter.invoke()
#     # raw_prediction = interpreter.tensor(output_index)
#     # output_image = raw_prediction()
    
    
    
#     inferer.build_model(
#     num_rrg=3, num_mrb=2, channels=64,
#     weights_path='low_light_weights_best.h5'
# )

#     output_image = output_image.squeeze() * 255.0
#     output_image = output_image.clip(0, 255)
#     output_image = output_image.reshape(
#         (np.shape(output_image)[0], np.shape(output_image)[1], 3)
#     )
#     output_image = Image.fromarray(np.uint8(output_image))
    
#     print(type(output_image))
#     return output_image


def mirnet_run(path):
    # @title Run inference
    # model_type = "fp16" #@param ["dr", "fp16", "int8"]

    image_path = path
    
    model_bild()

    # for image_path in LOW_LIGHT_IMGS[:5]:
    # original_image, preprocessed_image = preprocess_image(image_path)
    # output_image = infer_tflite(model_type, preprocessed_image)
    
    original_image, output_image = inferer.infer(image_path)

    output_image.save("output_image.png")
    
# img_path = 'IMAGE.png'

# mirnet_run(img_path)
    
    
