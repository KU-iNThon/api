FROM python:3.9-slim-bullseye AS builder

WORKDIR /app
COPY . .
RUN apt-get update && apt-get upgrade && apt-get install locales git -y && locale-gen en_US.UTF-8 &&  \
    python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt # 21.1MB

FROM python:3.9-slim-bullseye AS deployer

WORKDIR /app
COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
CMD ["uvicorn", "main:app", "--port=7777", "--host=0.0.0.0"]
