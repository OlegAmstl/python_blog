FROM python:3.10-slim
RUN mkdir /app
COPY requirements.txt /app
EXPOSE 8000
RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY ./ /app
WORKDIR /app

CMD ["gunicorn", "python_blog.wsgi:application", "--bind", "0:8000" ]