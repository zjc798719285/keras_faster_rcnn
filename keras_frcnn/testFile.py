from keras_frcnn.pascal_voc_parser import get_data
from keras_frcnn.pascal_voc_parser_v2 import get_data2
from keras_frcnn import data_generators, config, data_generators_v2, config_v2
from keras_frcnn import resnet as nn
import keras.backend as K
import numpy as np
train_path = 'E:\PROJECT\\barefoot_fast_rcnn\data_txt\\train.txt'
test_path = 'E:\PROJECT\\barefoot_fast_rcnn\data_txt\\mini_test.txt'

All_img, Classes_count, Class_mapping = get_data2(train_path=train_path,
                                                  test_path=test_path,
                                                  img_height=128,
                                                  img_width=59)
all_imgs, classes_count, class_mapping = get_data("E:\PROJECT\keras-frcnn\VOCtrainval_11-May-2012")
C = config.Config()
C2 = config_v2.Config()
Train_imgs = [s for s in All_img if s['imageset'] == 'trainval']
data_gen_Train = data_generators_v2.get_anchor_gt(Train_imgs,
                                               Classes_count,
                                               C2, nn.get_img_output_length,
                                               K.image_dim_ordering(),
                                               mode='train')
train_imgs = [s for s in all_imgs if s['imageset'] == 'trainval']
data_gen_train = data_generators.get_anchor_gt(train_imgs,
                                               classes_count,
                                               C, nn.get_img_output_length,
                                               K.image_dim_ordering(),
                                               mode='train')
x, y, img = next(data_gen_Train)
X, Y, img_data = next(data_gen_train)
print(np.shape(all_imgs))
print(np.shape(classes_count))
print(np.shape(class_mapping))