# -*- coding: utf-8 -*-
# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import cv2
import os
from tqdm import tqdm

!wget --no-check-certificate \
  https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip \
  -O /content/cats_and_dogs_filtered.zip

import os
import zipfile

local_zip = '/content/cats_and_dogs_filtered.zip'

zip_ref = zipfile.ZipFile(local_zip, 'r')

zip_ref.extractall('/content')
zip_ref.close()

DATADIR = '/content/cats_and_dogs_filtered/train'
CATEGORIES = ['cats','dogs']
IMG_SIZE =100

training_data=[]

def create_training_data():

    for category in CATEGORIES:

        path=os.path.join(DATADIR, category)

        class_num=CATEGORIES.index(category)

        for img in os.listdir(path):

            try:

                img_array=cv2.imread(os.path.join(path,img))

                new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))

                training_data.append([new_array,class_num])

            except Exception as e:

                pass

create_training_data()

print(len(training_data))

lenofimage = len(training_data)

X=[]
y=[]

for categories, label in training_data:
    X.append(categories)
    y.append(label)
X= np.array(X).reshape(lenofimage,-1)

X.shape

X = X/255.0

X[1]

y=np.array(y)

y.shape

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y)

from sklearn.svm import SVC
svc = SVC(kernel='linear',gamma='auto')
import time
start = time.time()
svc.fit(X_train, y_train)

end = time.time()
print("time taken to create model",end-start)

y2 = svc.predict(X_test)

train_acc = svc.score( X_train, y_train )

print("training accuracy", train_acc * 100)

from sklearn.metrics import accuracy_score
cf= accuracy_score(y_test,y2)*100
print("Accuracy on testing data is",cf)

from sklearn.metrics import confusion_matrix

cf_m = confusion_matrix(y_test,y2)

import seaborn as sns

sns.heatmap(cf_m,annot=True)

from sklearn.metrics import classification_report
print(classification_report(y_test,y2))

result = pd.DataFrame({'original' : y_test,'predicted' : y2})

result







