FROM python:3.11-slim
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./prediction_endpoint.py /app/prediction_endpoint.py
COPY ./newsgroups_model.joblib /app/newsgroups_model.joblib
CMD ["uvicorn", "prediction_endpoint:app", "--host", "0.0.0.0", "--port", "8000"]