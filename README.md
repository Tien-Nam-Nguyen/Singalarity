# Facial recognition on video

![COVER](Figure/cover.png)


1. Create a conda environment .conda


2. Clone and build dlib from source:
```console
$ git clone https://github.com/davisking/dlib.git
$ cd dlib
$ mkdir build
$ cd build
$ cmake .. -DDLIB_USE_CUDA=1 -DUSE_AVX_INSTRUCTIONS=1 -DCUDAToolkit_ROOT=/path/to/your/nvcc/bin/
$ cmake --build .
$ cd ..
$ python setup.py install --set DLIB_USE_CUDA=1
```


3. Install dependencies:
```console
$ cd project/
$ pip install -r requirements.txt
```


4. Image augmentation:
```console
$ cd Image/
$ python augmentation.py
```


5. Image encode:
```console
$ python encode.py
$ cd ..
```


6. Run Django server:
```console
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```


7. Post video:

![POST-video](Figure/postvid.png)

![RESPONSE-video](Figure/responsevid.png)


8. Download video 

![DOWNLOAD-video](Figure/url.png)






