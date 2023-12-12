FROM python

WORKDIR /app

RUN mkdir /app/model_data

COPY ./src.py /app/src.py
COPY ./model_data/dataset.gguf /app/model_data/dataset.gguf

RUN pip install llama-cpp-python
RUN pip install Flask

ENV SERVICE_PORT=5005

CMD ["python", "src.py"]