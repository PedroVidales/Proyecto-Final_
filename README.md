# Proyecto-Final_



## Índice

1.[Archivos](#archivos)\
2.[Extracción y transformación de datos](#extracción)\
3.[Análisis del sentimiento](#análisis del sentimiento)\
4.[Conclusiones](#conclusiones)


<a name="Archivos"/>

## Archivos

Extracción de dataset en kaggle con información relativa a los alojamientos de Airbnb en Madrid.
Trabajamos sobre varios archivos csv.

1. calendar.csv
2. listings_detailed.csv
3. neighbourhoods.geojson
4. review_detailed

Utilizamos la API de Google Maps para encontrar los atractivos turísitos cercanos a cada alojamiento de Airbnb.



<a name="extracción"/>
 
## Extracción de datos y transformación.

La extracción se basó en encontrar los archivos y usar la API, como mencionaba en el apartado enterior, después seguimos distintos procesos:

1. Limpieza de todos los archivos tanto de valores nulos como duplicados.
2. Transformación: transformamos los propios datos de cara a nuestro objetivo.



<a name="análisis"/>


## Análisis del sentimiento

Valoramos todos los registros de comentarios del archivo review.csv de tal forma que los identifique como comentarios negativos o positivos
para estudiar y analizar el medio o la manera de lograr tener ya no solamente reseñas, si no buenas. Una vez conseguido esto enfrentaremos 
la relación que tienen los amenities en primero, y la ubicación en segundo lugar.



<a name="Conclusiones"/>


## Conclusiones

Atendiendo a los resultados obtenidos y visualizados mediantes gráficas de librerías de Python y Tableau podemos determinar lo siguiente:

1. Existe una relación clara entre la cantidad de amenities y las buenas o malas reseñas. Sería conveniente analizar en profundidad para detectar
que amenitie o amenities son, por norma general, los que más decantan la balanza tanto en el sentido negativo del comentario como del positivo.

2.Por otro lado y haciendo referencia a la ubicación del alojamiento, parece claro cuales son las zonas mas recomandables para establecer este negocio. También sería muy interesante profundizar el análisis y comprobar cuales son los  factores que rodean a las zonas con mayor ratio positivo/negativo para deliberar exactamente el lugar óptimo para establecer el alojamiento atendiendo a criterios como la comunicación, las áreas culturales,los establecimientos, etc...

3. El siguiente paso será realizar un estudio de la relación que tienen los comentarios negativos y positivos en función del tipo de apartamento.
	
