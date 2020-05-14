import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow
import zipfile
import cv2
from distutils.version import StrictVersion
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
# This is needed since the notebook is stored in the object_detection folder.
from requests import Session
from tensorflow_core.python import get_default_graph

sys.path.append("..")
from object_detection.utils import ops as utils_ops
# This is needed to display the images.
#%matplotlib inline
from utils import label_map_util

from utils import visualization_utils as vis_util
# What model to download.
MODEL_NAME = 'COCO'

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_FROZEN_GRAPH = MODEL_NAME + '/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt')
detection_graph = tensorflow.Graph()
with detection_graph.as_default():
  od_graph_def = GraphDef()
  with gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
    serialized_graph = fid.read()
    od_graph_def.ParseFromString(serialized_graph)
    tensorflow.import_graph_def(od_graph_def, name='')
category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)
def run_inference_for_single_image(image, graph):
    if 'detection_masks' in tensor_dict:
        # The following processing is only for single image
        detection_boxes = tensorflow.squeeze(tensor_dict['detection_boxes'], [0])
        detection_masks = tensorflow.squeeze(tensor_dict['detection_masks'], [0])
        # Reframe is required to translate mask from box coordinates to image coordinates and fit the image size.
        real_num_detection = tensorflow.cast(tensor_dict['num_detections'][0], tensorflow.int32)
        detection_boxes = tensorflow.slice(detection_boxes, [0, 0], [real_num_detection, -1])
        detection_masks = tensorflow.slice(detection_masks, [0, 0, 0], [real_num_detection, -1, -1])
        detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
            detection_masks, detection_boxes, image.shape[0], image.shape[1])
        detection_masks_reframed = tensorflow.cast(
            tensorflow.greater(detection_masks_reframed, 0.5), tensorflow.uint8)
        # Follow the convention by adding back the batch dimension
        tensor_dict['detection_masks'] = tensorflow.expand_dims(
            detection_masks_reframed, 0)
    image_tensor = get_default_graph().get_tensor_by_name('image_tensor:0')

    # Run inference
    output_dict = sess.run(tensor_dict,feed_dict={image_tensor: np.expand_dims(image, 0)})

    # all outputs are float32 numpy arrays, so convert types as appropriate
    output_dict['num_detections'] = int(output_dict['num_detections'][0])
    output_dict['detection_classes'] = output_dict[
        'detection_classes'][0].astype(np.int64)
    output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
    output_dict['detection_scores'] = output_dict['detection_scores'][0]
    if 'detection_masks' in output_dict:
        output_dict['detection_masks'] = output_dict['detection_masks'][0]
    return output_dict
cap = cv2.VideoCapture(0)
with detection_graph.as_default():
    with Session() as sess:
        # Get handles to input and output tensors
        ops = get_default_graph().get_operations()
        all_tensor_names = {output.name for op in ops for output in op.outputs}
        tensor_dict = {}
        for key in [
          'num_detections', 'detection_boxes', 'detection_scores',
          'detection_classes', 'detection_masks'
        ]:
            tensor_name = key + ':0'
            if tensor_name in all_tensor_names:
                tensor_dict[key] = get_default_graph().get_tensor_by_name(
              tensor_name)

        while True:
            ret, image_np = cap.read()
            # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
            image_np_expanded = np.expand_dims(image_np, axis=0)
            # Actual detection.
            output_dict = run_inference_for_single_image(image_np, detection_graph)
            # Visualization of the results of a detection.
            vis_util.visualize_boxes_and_labels_on_image_array(
                image_np,
                output_dict['detection_boxes'],
                output_dict['detection_classes'],
                output_dict['detection_scores'],
                category_index,
                instance_masks=output_dict.get('detection_masks'),
                use_normalized_coordinates=True,
                line_thickness=8)
            cv2.imshow('object_detection', cv2.resize(image_np, (1400, 800)))
            if cv2.waitKey(25) & 0xFF == ord('q' or 'Q'):
                cap.release()
                cv2.destroyAllWindows()
                break
