import json
import pandas as pd
file = open('instances_val2017.json')
data = json.load(file)
images = data['images']
ann = data['annotations']
cat = data['categories']
final = []
for i in range(2):
    tmp ={'image': {},'annotations':{}}
    tmp['info']= 'info'
    tmp['images'] = '[image]'
    tmp['annotation']='[annotations]'
    tmp['licenses']= '[licenses]'
    tmp['image']['id'] = images[i]['id']
    tmp['image']['width'] = images[i]['width']
    tmp['image']['height'] = images[i]['height']
    tmp['image']['filename'] = images[i]['file_name']
    tmp['annotations']['area'] = ann[i]['area']
    tmp['annotations']['bbox'] = ann[i]['bbox']
    tmp['annotations']['iscrowd'] = 0
    tmp['category'] = cat[i]['name']
    final.append(tmp)
