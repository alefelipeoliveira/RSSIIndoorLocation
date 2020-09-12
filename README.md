# RSSIIndoorLocation

This repository is dedicated to test a dataset of RSSI Indoor Location Algorithm, currently using Trilateration and KNN.

## Installation

To install this project start downloading the git repository:
```
$ git clone https://github.com/alefelipeoliveira/RSSIIndoorLocation.git
```

## Requirements

Libraries ```matplotib```, ```streamlit```, ```pandas```, ```copy``` and ```statistics``` are necessary.
```
$ pip install matplotlib streamlit pandas copy statistics
```
## Run

Streamlit creates a frontend environment to run different algorithms in the datasets, after installed strealit library, is possible to run the application in the local file, with the command
```
$ streamlit run .\main.py
```

 ## Related Publication
 
This project use the dataset from the following papers:
 
S. Sadowski, P. Spachos, K. Plataniotis, "Memoryless Techniques and Wireless Technologies for Indoor Localization with the Internet of Things", IEEE Internet of Things Journal.

https://github.com/pspachos/RSSI-Dataset-for-Indoor-Localization-Fingerprinting

BELMONTE-HERNÁNDEZ, A.; HERNÁNDEZ-PEÑALOZA, G.; GUTIÉRREZ, D. M.; ÁLVAREZ, F. Swiblux:Multi-sensor deep learning fingerprint for precise real-time indoor tracking.IEEE Sensors Journal, IEEE, v. 19, n. 9,p. 3473–3486, 2019.

http://www.gatv.ssr.upm.es/~abh/
