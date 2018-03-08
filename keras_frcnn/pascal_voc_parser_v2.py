import scipy.io as sio
import cv2
import numpy as np
def get_box(path, img_width, img_height):
	lab = sio.loadmat(path[0:-1])['label'][0, :]
	y1 = int(round(lab[0] * img_height))
	x1 = int(round(lab[1] * img_width))
	y2 = y1 + int(round(lab[3] * img_height))
	x2 = x1 + int(round(lab[2] * img_width))
	return x1, y1, x2, y2

def get_data_v2(train_path,test_path):
 all_imgs = []
 classes_count={'Foot':0}
 class_mapping={'Foot':1}
 f_train = open(train_path)
 train_lines = f_train.readlines()
 f_test = open(test_path)
 test_lines = f_test.readlines()
 for train_i in train_lines:
		all_path = train_i.split(";", 2)
		img_path = all_path[0]; box_path = all_path[1]
		img = cv2.imread(img_path)
		(img_height, img_width, img_depth)=np.shape(img)
		annotation_data = {'filepath': img_path, 'width': img_width,
						   'height': img_height, 'bboxes': []}
		annotation_data['imageset'] = 'trainval'
		x1, y1, x2, y2 = get_box(path=box_path, img_width=img_width, img_height=img_height)
		annotation_data['bboxes'].append(
			{'class': 'Foot', 'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2, 'difficult': False})
		all_imgs.append(annotation_data)
		classes_count['Foot'] += 1
 for test_i in test_lines:
		all_path = test_i.split(";", 2)
		img_path = all_path[0]
		box_path = all_path[1]
		annotation_data = {'filepath': img_path, 'width': img_width,
							   'height': img_height, 'bboxes': []}
		annotation_data['imageset'] = 'test'
		x1, y1, x2, y2 = get_box(path=box_path, img_width=img_width, img_height=img_height)
		annotation_data['bboxes'].append(
				{'class': 'Foot', 'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2, 'difficult': False})
 all_imgs.append(annotation_data)
 classes_count['Foot'] += 1
 return all_imgs, classes_count, class_mapping

if __name__ == '__main__':

 train_path = 'E:\PROJECT\keras-frcnn\data_txt\\train.txt'
 test_path = 'E:\PROJECT\keras-frcnn\data_txt\\test.txt'
 output = 'E:\PROJECT\keras-frcnn\\test_results\\'
 all_imgs, classes_count, class_mapping = get_data_v2(train_path=train_path,
														 test_path=train_path,
														 img_width=399,
														 img_height=866)
 anchor_scale = []
 anchor_ratio = []
 for indx, img_i in enumerate(all_imgs):
  gt_xmin = img_i['bboxes'][0]['x1']
  gt_ymin = img_i['bboxes'][0]['y1']
  gt_xmax = img_i['bboxes'][0]['x2']
  gt_ymax = img_i['bboxes'][0]['y2']
  for scale in anchor_scale:
   for ration in anchor_ratio:
    anchor_x =gt_xmax






  # cv2.imwrite(outpath, img)filename = img_path.split('\\',len(img_path))[-1]
  # img[xmin:xmax, ymin] = 255;img[xmin:xmax, ymax] = 255  print(indx)
  # img_path = img_i['filepath']
  #
  # outpath = output + filename
  # img[xmin, ymin:ymax] = 255;img[xmax, ymin:ymax] = 255

