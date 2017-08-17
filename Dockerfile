
FROM python:3.6.2

ADD requirements.txt ./
RUN pip install -r requirements.txt

ADD api.py ./
ENV FLASK_APP=api.py
EXPOSE 5000
ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"] 
