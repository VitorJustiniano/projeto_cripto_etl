FROM quay.io/astronomer/astro-runtime:12.8.0

#Copia o requirements.txt da raiz do projeto para dentro do container
COPY requirements.txt .

#instala as dependencias
RUN pip install --no-cache-dir -r requirements.txt