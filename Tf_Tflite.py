import tensorflow as tf

in_path = "./model/frozen_graph.pb"
out_path = "./model/frozen_graph.tflite"
# out_path = "./model/quantize_frozen_graph.tflite"

# 模型输入节点
input_tensor_name = ["input/x"]
input_tensor_shape = {"input/x":[1, 784]}
# 模型输出节点
classes_tensor_name = ["out/fc2"]

converter = tf.lite.TFLiteConverter.from_frozen_graph(in_path,
                                            input_tensor_name, classes_tensor_name,
                                            input_shapes = input_tensor_shape)
#converter.post_training_quantize = True
tflite_model = converter.convert()

with open(out_path, "wb") as f:
    f.write(tflite_model)