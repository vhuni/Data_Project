# Stock Prediction

> Creates a model to predict daily stock prices of Amazon.

Note: Project in early development stage.

## Requirements
  - Amazon web service account: EC2 instance and S3 bucket
  - Amazon IAM key: for .pem, access_key and secret_key
  - Docker: pull tensorflow image from docker hub to run modelling in container

## Usage
Clone or fork this repository.

1. Run docker and pull tensorflow image (latest-jupyter gives tensorflow access to jupyter notebook)

```bash
docker pull tensorflow/tensorflow:latest-jupyter
```
2. Create container from tensorflow image
```bash
docker run -it --name tf tensorflow/tensorflow:latest-jupyter bash
```
3. Clone or fork repository (leave directory open)
4. Open jupyter notebook in browser (link to notebook provided by step no.2)
5. Copy stock_prediction.ipynb from Data_project folder to notebook (leave browser open)
6. Create Amazon web service EC2 instance and S3 bucket (open in new browser)
(skip to step no.6c if you have existing ec2 and s3) 
6a. download .pem key when creating ec2 instance
6b. download csv file when creating s3 bucket
6c. select instance 
6d. under connect tab select SSH and copy the code
example:
```bash
ssh -i "new_ssh.pem" ubuntu@ec2-3-135-190-123.us-east-2.compute.amazonaws.com
```
7. Open Windows PS and paste SSH code similar to example (ubuntu or ec2-user will appear as root when connected)
8. Copy scraper.py to ec2 instance
example:
```bash
scp -i "new_ssh.pem" "scraper.py" ubuntu@ec2-3-135-190-123.us-east-2.compute.amazonaws.com:/home/ubuntu/
```
9. Create venv and install requirements as pip
example:
```bash
create venv: python3 -m venv my_app/env
activate venv : source ~/my_app/env/bin/activate
```
```bash
(env) - pip3 install pandas
      - pip3 install boto3
      - pip3 install requests
```
9a. (optional) Test scraper.py
```bash
python3 scraper.py 
```




