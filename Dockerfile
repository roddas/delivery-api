FROM python:3.8
WORKDIR /application
COPY . .
RUN pip install flask
ENTRYPOINT [ "python" ]
CMD ["app.py"]