import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"  # Set it to GPU:1

import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))
