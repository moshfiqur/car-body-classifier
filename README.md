# Car body classifier

A simple tensorflow image classifier to address an image classification problem of detecting the car body type and 
pulling out other features from images related to my work.

I installed tensorflow in virtualenv mode explained in the doc [here](https://www.tensorflow.org/install/install_mac).

This repo contains an image downloader python script (img_dl.py), which can search and download 100 images from Google 
search. Images can be downloaded by providing related search string and a download path. I wanted to classify four 
different kinds of car body types: sedan, station wagon, suv and pickup trucks. I jus performed some google search to 
find out appropriate image, download 100 of each car types in tf_images folder under the sub-directory of each car 
body types names. 

The trainer script is in retrain.py which is available in tensorflow's official [repo](https://github.com/tensorflow/tensorflow).

To retrain the system, first download enough image using img_dl.py in the following folders:
*tf_images/sedan*, *tf_images/suv*, *tf_images/station_wagon* and *tf_images/pickup_trucks*. 

**The sub-directory name is important. Because sub directory name will be the class name for the images inside that directory.**

To start the retrain, run the following command:

```
python image_retraining/retrain.py 
    --bottleneck_dir=tf_files/bottlenecks 
    --how_many_training_steps 500 
    --model_dir=tf_files/inception 
    --output_graph=tf_files/retrained_graph.pb 
    --output_labels=tf_files/retrained_labels.txt 
    --image_dir=tf_images
```

If everything goes well, you will see the training accuracy in command line. The accuracy for my training case was 81.5.

```
Final test accuracy = 81.5% (N=27)
```

Now the image classifier can be tested as:

```python label_image.py test_images/bmw-sedan-0.jpg```

It gave me quite good result comparing that I only used around 100 images for training of each class:

```
sedan (score = 0.62541)
suv (score = 0.25076)
station wagon (score = 0.11597)
pickup trucks (score = 0.00786)
```

For the other test image:
```python label_image.py test_images/VW-truck.jpg```

```
pickup trucks (score = 0.85396)
suv (score = 0.14084)
station wagon (score = 0.00314)
sedan (score = 0.00206)
```


