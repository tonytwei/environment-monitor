FROM python:3.10
WORKDIR /backend
COPY . /backend
EXPOSE 8000
ENV FLASK_RUN_PORT 8000
ENV FLASK_RUN_HOST 0.0.0.0
RUN pip install -r requirements.txt
CMD python app.py