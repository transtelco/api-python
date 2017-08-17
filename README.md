# api-python

This is a program written in python. It is an simple API it intially registers itself with consul, and afterward it just responds to calls.

## requirements

* Install [python - 3.6.1](https://www.python.org/downloads/)
* Install [pip](https://pip.pypa.io/en/stable/)

## running program

You can use the following command on a bash shell to get the program running.

```bash
# start the application must have consul running
export CONSUL_PORT=locahost
export CONSUL_HOST=8500
pip install -r requirements.txt 
FLASK_APP=api.py flask run
```

## dockerize program

```bash
docker build -t <dockerhub-user>/api-python:latest .
docker run -p 5000:5000 <dockerhub-user>/api-python
```
