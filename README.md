# Devops labs
## Galimzhanov Daniyar

Simple web app showing current Moscow Time

## Installation

```git clone https://github.com/a1d4r/devops.git``` \
```pip3 install -r requirements.txt``` 

## Docker installation

```docker pull totenhund/python_app_devops:latest  ```\
```docker run -p 5000:5000 totenhund/python_app_devops ```


## App endpoints

```/``` - showing moscow time

```/visits``` - showing how many times root page was visited

Visits are stored in counter.txt file
