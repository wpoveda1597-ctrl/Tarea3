# Tarea3

Procesamiento en batch:

1. Ejecutar Putty con usuario vboxuser y bigdata

2. Dentro de putty, ejecutar el comando de wget para descargar el archivo
wget https://www.datos.gov.co/api/v3/views/qijw-htwa/query.csv -O query.csv

3. Crear el archivo batch.py usando el comando
nano batch.py

4. Copiar el código encontrado en Github de batch.py

5. Guardar el archivo

6. Ejecutar el comando para lanzar el código
spark-submit batch.py
