# Temel alınacak Python imajı
FROM python:3.11-slim

# Çevre değişkenleri (Python'un logları hemen terminale basması için)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Çalışma dizinini ayarla
WORKDIR /app

# Gerekli kütüphaneleri kopyala ve yükle
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Tüm kodları kopyala
COPY . /app/

# Portu dışarı aç
EXPOSE 8000

# Django sunucusunu başlat
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]