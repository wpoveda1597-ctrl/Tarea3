# 
#Importar clases de PySpark para poder crear DataFrames
#
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, concat, lit
#Crear sesión de Spark
spark = SparkSession.builder.appName("ColegiosBogota").getOrCreate()
spark.sparkContext.setLogLevel("WARN")
# 
#-------------Cargar datos
#
print("\n" + "Cargar Datos:")
#Buscar el archivo en la ruta del usuario de vboxuser
file_path = "file:///home/vboxuser/query.csv"  
#Leer el archivo csv del file_path, header true es para definir la primera línea como encabezados
df = spark.read.csv(file_path, header=True, inferSchema=True)
#Mostrar los registros cargados al dataframe
print(f"Registros cargados: {df.count()}")
#
#Limpieza, Transformación y EDA
#

print("\n" + "Operaciones de Limpieza, Transformación y EDA")

#Limpieza
#Seleccionaremos solo datos relevantes del DataFrame, como el nombre del Colegio, el tipo de Zona, de Establecimiento y Calendario
dflimpio = df.select("nombreestablecimiento", "zona", "tipo_Establecimiento", "calendario")
#Validar si dentro de las filas hay datos vacíos para limpiarlos
dflimpio = dflimpio.dropna()
print("Se limpiaron filas innecesarias")

#Transformación
#Se concatenará las 2 columnas de zona y calendario en una nueva columna llamada perfil
dflimpio = dflimpio.withColumn("perfil", concat(col("zona"), lit("-"), col("calendario")))
dflimpio = dflimpio.drop("zona", "calendario")
print ("Se concatenaron 2 filas")

#Análisis exploratorio de datos (EDA)
# Se usará groupby para agrupar las filas por el perfil concatenado, luego contar cuantas filas hay por cada grupo
conteo_perfil = dflimpio.groupBy("perfil").count()
print ("Se agruparon las filas en base al perfil")
# 
#----------Visualizar resultados
# 
print("\n" + "Visualización de resultados:")
#Mostrar los primeros 5 registros
print("\n" + "Primeros 5 registros luego de limpiar y transformar:")
dflimpio.show(5, truncate=False)
#Mostrar la tabla con el conteo de colegios por la variable concatenada de Zona y Calendario
print("\n" + "Conteo de establecimientos por Zona y Calendario):")
conteo_perfil.show()
#Mostrar el esquema final para verificar las columnas creadas
print("\n" + "Esquema final del DataFrame:")
dflimpio.printSchema()
