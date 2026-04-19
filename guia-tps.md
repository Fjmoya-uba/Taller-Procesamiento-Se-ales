
### FACULTAD DE INGENIER˝A


### UBA


# TALLER DE PROCESAMIENTO DE SE(cid:209)ALES


# (TA136)


# Gu(cid:237)a de Trabajos PrÆcticos


# Versi(cid:243)n 1.2


# Primer cuatrimestre 2025


## Gu(cid:237)a 1

1
1.1 (cid:207) Sin utilizar loops (for/while) convertir a escala de grises la imagen pikachu_ vs_charmander.jpeg implementando las siguientes tØcnicas: (a) m´ınpR,G,Bq`m´axpR,G,Bq
2
(b) R`G`B
3
(c) 0.3R ` 0.59G ` 0.11B (utilice el comando @)
c: Utilice las funciones imread e imshow (matplotlib).
1.2 (cid:207) Sin utilizar loops (for/while), utilizando indexaci(cid:243)n edite la imagen AFALogo. bmp para
(a) Cortar las letras dentro del logo.
(b) Cortar las estrellas y transponerlas.
(c) Generar una mascara separando el color de fondo del logotipo.
(d) Cambiar el color de fondo de negro a blanco.
(e) Espejar la imagen (izquierda a derecha).
(f) Dibujar una grilla sobre la imagen cada 4 p(cid:237)xeles.
(g) Agregar la 3era estrella.
1.3 Sea la funci(cid:243)n de densidad de probabilidad
pXY px, yq “
4 5
␣ 0 ă y ă 1 ` x3, 0 ă x ă 1
(
1
(a) Calcular y gra(cid:28)car en una misma (cid:28)gura el soporte, la esperanza condicional ErY |X “ xs y la recta de regresi(cid:243)n.
(b) Calcular el error bayesiano. c: Las œnicas integrales que debe resolver son con respecto a la marginal pX pxq. El resto de los cÆlculos debe hacerse utilizando propiedades. 1.4 (cid:207) Una conocida cadena de comida rÆpida desea predecir la ganancia de una sucursal en funci(cid:243)n de la cantidad de habitantes de la ciudad para decidir si conviene abrirla o no. El archivo mc.txt contiene la base de datos a utilizar. La primera columna es la poblaci(cid:243)n de la ciudad (de a 10.000 personas) y la segunda es la ganancia (de a $USD 10.000). Los valores negativos indican pØrdidas.
(a) Implemente su propio c(cid:243)digo, utilizando matrices, para realizar una regresi(cid:243)n lineal que minimice el error cuadrÆtico medio. (cid:190)Cuanto vale dicho error?
(b) Visualizar los datos con scatter (matplotlib) y superponer la recta de regresi(cid:243)n estimada sobre ellos.
(c) Diseæe una grilla de puntos que permita gra(cid:28)car el riesgo emp(cid:237)rico (en un grÆ(cid:28)co 3d) en funci(cid:243)n de los parÆmetros (w y b), utilizando plot_surface (matplotlib).
2
Compruebe que los parÆmetros encontrados en el inciso (a) son efectivamente los que minimizan el riesgo.
(d) Predecir la ganancia de una ciudad de 35.000 habitantes.
(e) Repetir la regresi(cid:243)n lineal utilizando LinearRegression (sklearn). Comparar resultados. 1.5 (cid:207) Una inmobiliaria desea automatizar la tarea de tazar terrenos. El archivo inmobiliaria.txt contiene la base de datos de casas en Portland, Oregon. La primer columna corresponde con dimensi(cid:243)n del terreno (en pies cuadrados), la segunda corresponde a la cantidad de dormitorios y la tercera al precio (en d(cid:243)lares).
(a) Realizar una regresi(cid:243)n lineal utilizando gradiente descendente (elegir el learning rate con prueba y error). Gra(cid:28)car el error cuadrÆtico medio en funci(cid:243)n de las iteraciones del entrenamiento y comparar con el error asociado a la soluci(cid:243)n matricial.
(b) Predecir el costo de una propiedad de 1650 pies cuadrados y 3 dormitorios. Comparar resultado con la soluci(cid:243)n matricial.
(c) Calcular el learning-rate (cid:243)ptimo y volver a entrenar el algoritmo usando este valor. Repetir los incisos anteriores para este entrenamiento. 1.6 (cid:207) Una inmobiliaria desea automatizar la tarea de tazar terrenos. El archivo inmobiliaria.csv contiene la base de datos de casas en California.
(a) Explorar los datos usando read_csv (pandas). Indicar cantidad de muestras, nombre y tipo de dato de cada feature.
(b) Indicar la proporci(cid:243)n de las variables categ(cid:243)ricas representando probabilidades. c: Si no sabe que tipo de variable aleatoria es la categ(cid:243)rica, deberÆ buscar dicha informaci(cid:243)n.
(c) Para analizar las variables numØricas utilice el comando pairplot (seaborn). Explique que representan los grÆ(cid:28)cos.
(d) Utilice el comando SimpleImputer (sklearn) para completar los valores faltantes con los mÆs frecuentes.
(e) Utilice el comando get_dummies (pandas) para codi(cid:28)que las variables categ(cid:243)ricas como one-hot. c: En caso de no conocer el concepto, buscar informaci(cid:243)n sobre one-hot encoding.
(f) Utilice el comando train_test_split (sklearn) para de(cid:28)nir dos conjuntos con las proporciones 75 % y 25 %. Gra(cid:28)que los histogramas de ambos conjuntos (superpuestos) de la mediana del valor de las propiedades.
(g) Utilice el comando StandardScaler (sklearn) para normalizar cada variable exceptuando a la mediana del valor de la propiedad. Utilice el conjunto de entrenamiento para (cid:28)jar la normalizaci(cid:243)n y apliquela a ambos conjuntos.
(h) Realizar una regresi(cid:243)n lineal para predecir la mediana del valor de la propiedad en funci(cid:243)n del resto de las variables. Indicar el ECM de entrenamiento y testeo.
3
1.7 Hallar una soluci(cid:243)n matricial al problema de regresi(cid:243)n lineal sin sesgo y con regularizaci(cid:243)n L2. (cid:190)A que se aproxima la soluci(cid:243)n si el algoritmo estÆ muy regularizado (pero no tanto como para pensar que es cero)? 1.8 (cid:207) Se desea estimar la cantidad de agua que (cid:29)uye por una presa a partir de la variaci(cid:243)n del nivel de agua. El archivo represa.csv contiene los datos a utilizar, de(cid:28)niendo los conjuntos de entrenamiento, validaci(cid:243)n y testeo.
(a) Visualice los tres dataset a partir de un grÆ(cid:28)co scatter utilizando colores diferentes para cada conjunto.
(b) Realice una regresi(cid:243)n lineal utilizando LinearRegression de sklearn. Gra(cid:28)que la recta de regresi(cid:243)n estimada sobre la el scatter.
(c) Realice una regresi(cid:243)n polin(cid:243)mica de orden 8 sin regularizaci(cid:243)n. Gra(cid:28)que la funci(cid:243)n de regresi(cid:243)n estimada sobre el scatter.
(d) Utilizando sklearn.linear_model.Ridge, repetir el inciso anterior regularizando con λ “ 1 y λ “ 100.
(e) Gra(cid:28)car el error cuadrÆtico medio en funci(cid:243)n del hiperparÆmetro de regularizaci(cid:243)n λ ě 0 para el conjunto de entrenamiento y validaci(cid:243)n. (cid:190)Que valor minimiza el error de validaci(cid:243)n?
(f) Calcular el error cuadrÆtico medio de testeo para el hiperparÆmetro elegido en el inciso anterior.
4

## Gu(cid:237)a 2

2.1 Por un canal de comunicaciones se emiten bits de forma aleatoria, siendo el 75 % de ellos 1. Dependiendo del bit transmitido, la comunicaci(cid:243)n es afectada por un ruido aditivo normal de media nula y varianzas: 4 si el bit es un 0 y 1 si el bit es un 1. Sea X la seæal recibida y Y el bit emitido.
(a) Hallar y gra(cid:28)car pX pxq.
(b) Hallar y gra(cid:28)car PY |X p1|xq.
(c) (cid:190)Para que valores de x ocurre que PY |X p1|xq ą PY |X p0|xq?
(d) Calcular el error bayesiano expresando el resultado de las integrales en funci(cid:243)n de Φp¨q (funci(cid:243)n de distribuci(cid:243)n de la normal estÆndar), para luego computar los cuantiles. Comparar el resultado contra un clasi(cid:28)cador al azar y contra un clasi(cid:28)cador dummy.
2.2 Sean p y q dos distribuciones Bernoulli de parÆmetros 1 Calcular KLpp}qq y KLpq}pq. Expresar el resultado en nats.
2 y 1
3 respectivamente.
2.3 Sea p “ σpzq la funci(cid:243)n sigmoide. (a) Calcular la funci(cid:243)n inversa σ´1ppq con p P p0, 1q.
(b) Calcular la derivada σ1pzq. Encontrar sus valores (cid:237)n(cid:28)mo y supremo, y (en caso que existan) los puntos donde los alcanza.
(c) Escribir la derivada en funci(cid:243)n de p. 2.4 (cid:207) Un profesor desea estimar si un alumno va a aprobar o no la materia en base a la nota de dos parcialitos. El archivo parcialitos.txt contiene una base de datos con las notas de cada estudiante en los parcialitos y si, efectivamente, aprob(cid:243) o no la materia (1 es aprobar).
(a) Hallar una expresi(cid:243)n anal(cid:237)tica para la funci(cid:243)n costo y su gradiente.
(b) Realizar una regresi(cid:243)n log(cid:237)stica utilizando LogisticRegression (sklearn) y gra(cid:28)car la frontera de decisi(cid:243)n sobre un scatter.
(c) Predecir si un estudiante con notas 45 y 85 aprobar(cid:237)a la materia.
(d) Gra(cid:28)car la curva ROC del clasi(cid:28)cador, implementando su propio c(cid:243)digo. Indicar el punto correspondiente a la decisi(cid:243)n tomada en el inciso pbq y el EER. 2.5 (cid:207) El gerente de producci(cid:243)n de una fÆbrica de circuitos integrados desea predecir si un determinado integrado pasarÆ el control de calidad. El archivo microchips. txt posee datos de la evaluaci(cid:243)n de dos pruebas diagn(cid:243)stico de diferentes integrados, y una tercer columna que indica si pasaron el mencionado control (1 es pasar la inspecci(cid:243)n).
(a) Construir un mapa polin(cid:243)mico hasta orden 6 inclusive. (cid:190)Como puede relacionar la cantidad de parÆmetros con el grado del polinomio y la cantidad de features? Encontrar una expresi(cid:243)n matemÆtica que vincule esas magnitudes.
5
(b) Realizar una regresi(cid:243)n log(cid:237)stica utilizando LogisticRegression (sklearn) y gra(cid:28)car la frontera de decisi(cid:243)n sobre un scatter sin regularizaci(cid:243)n.
(c) Realizar una regresi(cid:243)n log(cid:237)stica y gra(cid:28)car la frontera de decisi(cid:243)n sobre un scatter con regularizaci(cid:243)n L2 y λ “ 1000.
(d) Realizar una regresi(cid:243)n log(cid:237)stica y gra(cid:28)car la frontera de decisi(cid:243)n sobre un scatter con regularizaci(cid:243)n L2 y λ “ 1. c: Funciones como meshgrid (numpy) y contour (matplotlib) pueden ser œtiles para gra(cid:28)car las fronteras. 2.6 (cid:207) La base de datos MNIST posee imÆgenes de los d(cid:237)gitos manuscritos (del 0 al 9). Se desea entrenar un clasi(cid:28)cador que, a partir de una imagen, prediga que d(cid:237)gito aparece en ella.
(a) Cargar la base de datos utilizando tensorflow.keras.datasets.mnist.load_ data. Utilizando imshow (matplotlib) represente 10 muestras del conjunto de testeo elegidas al azar.
(b) Realizar una regresi(cid:243)n log(cid:237)stica e indicar el accuracy de entrenamiento y testeo.
(c) Utilizando ConfusionMatrixDisplay (sklearn) represente la matriz de confusi(cid:243)n normalizada (testeo) para mostrar la probabilidad de cada predicci(cid:243)n para cada clase con 3 decimales. 2.7 (cid:207) Se denomina formante a las frecuencias donde se dan los picos de intensidad en el espectro de un sonido. El archivo formantes.txt contiene ejemplos de los 3 primeros formantes del sonido de las vocales /a/, /o/ y /u/. Utilizando solamente los dos primeros formantes:
(a) Gra(cid:28)car las muestras en un scatter, representando los formantes de cada vocal con colores distintos.
(b) Superponer a la grÆ(cid:28)ca anterior las medias y las covarianzas de cada gaussiana (una curva de nivel) del modelo de LDA.
(c) Implementar un algoritmo de LDA para clasi(cid:28)car los formantes.
(d) Gra(cid:28)car la predicci(cid:243)n de las muestras y la frontera de decisi(cid:243)n.
(e) Generar 50 muestras sintØticas y gra(cid:28)carlas junto a las fronteras. Representar los formantes de cada vocal con colores distintos. c: Tenga en cuenta que, ademÆs de las medias y varianzas, deberÆ utilizar las probabilidades ck aprendidas durante el entrenamiento. Funciones como random. choice y random.multivariate_normal (numpy) pueden ser œtiles. 2.8 (cid:207) [ver Ejercicio 2.5] La fÆbrica de circuitos integrados desea predecir si un determinado integrado pasarÆ el control de calidad a partir del archivo microchips. txt.
(a) Gra(cid:28)car la frontera de decisi(cid:243)n de un algoritmo 1NN sobre el scatter de la base de datos. (cid:190)Que puede decir del error de entrenamiento? (cid:190)Puede extraer una conclusi(cid:243)n general al respecto?
6
(b) Repetir para un 7NN. Relacionar el valor de K con los conceptos de over(cid:28)tting y regularizaci(cid:243)n. (c) Gra(cid:28)car ˆP p1|xq para un algoritmo 1NN y 7NN entrenados solamente con la primera de las pruebas diagn(cid:243)stico. c: La funci(cid:243)n argsort (numpy) puede ser œtil. El algoritmo KNN debe estar implementado con una sola funci(cid:243)n, de modo que Østa pueda usarse para todo k P N y cualquier cantidad de features. 2.9 (cid:207) El archivo ejs_svm.pkl contiene un par de bases de datos. Utilizando la base de datos 1er Dataset:
(a) Implementar una clasi(cid:28)caci(cid:243)n SVM utilizando solve_qp (qpsolvers), resolviendo el problema primal. Gra(cid:28)car la frontera de decisi(cid:243)n y las rectas de vectores soportes sobre un scatter.
(b) Repetir el inciso (a) resolviendo el problema dual.
(c) Repetir el inciso (a) relajando los mÆrgenes (utilizando C “ 1) y resolviendo el problema primal.
(d) Hallar el problema dual con mÆrgenes relajados. Puede buscarlo en la bibliograf(cid:237)a o deducirlo. c: Se recomienda practicar la deducci(cid:243)n.
(e) Repetir el inciso (a) relajando los mÆrgenes (utilizando C “ 1) y resolviendo el problema dual. 2.10 (cid:207) El archivo ejs_svm.pkl contiene un par de bases de datos. Utilizando la base de datos 2do Dataset, implementar una clasi(cid:28)caci(cid:243)n SVM con Kernel gaussiano (γ “ 50) utilizando svm.SVC (sklearn) con C “ 1. Gra(cid:28)car la frontera de decisi(cid:243)n y las curvas de vectores soportes sobre un scatter. 2.11 (cid:207) Se desea incursionar en la temÆtica de clasi(cid:28)caci(cid:243)n de gØnero musical. (a) Utilizando load (librosa) cargar los primeros 5 segundos del archivo mi_perro_ dinamita.mp3. Gra(cid:28)car la seæal temporal en funci(cid:243)n del tiempo (en segundos). Repetir con los primeros 20 segundos del archivo exclusive.mp3.
(b) Reproducir los audio utilizando Audio (IPython).
(c) Utilizando ShortTimeFFT (scipy.signal), gra(cid:28)car para cada seæal un par de espectrogramas, uno resaltando las caracter(cid:237)sticas temporales y el otro las espectrales (es decir, utiliza el paquete para calcular la (cid:27)t y gra(cid:28)ca a partir de imshow).
(d) Generar etiquetas que indiquen de que archivo proven(cid:237)a cada frame e implementar una clasi(cid:28)caci(cid:243)n SVM con Kernel gaussiano utilizando svm.SVC (sklearn) con C “ 1. Se recomienda utilizar una (cid:27)t de 64 puntos, un solapamiento del 50 %, descartar la parte simØtrica del espectro y utilizar ventana de hamming de la misma cantidad de puntos de la (cid:27)t. c: El mØtodo aqu(cid:237) descripto estÆ tratando los datos de cada ventana como muestras iid.
(e) Construir una base de datos de testeo con los siguientes 30 segundos de cada audio a partir del minuto de cada canci(cid:243)n. Evaluar el accuracy del clasi(cid:28)cador en la nueva base de datos.
7
(f) Repetir el ejercicio para (cid:27)ts de 32, 128 y 256 puntos. Extraer conclusiones 2.12 (cid:207) La cromatograf(cid:237)a de ultra alta performance acoplada a espectrometr(cid:237)a de masas de alta resoluci(cid:243)n permite el diagn(cid:243)stico del cÆncer de pr(cid:243)stata. El archivo prostata.csv posee datos de la abundancia de concentraci(cid:243)n de diferentes compuestos qu(cid:237)micos y el resultado del diagn(cid:243)stico: sano, cÆncer, benigno y post-cirug(cid:237)a. Se desea predecir el diagn(cid:243)stico en funci(cid:243)n del resto de los indicadores.
(a) Las muestras sin etiquetas representan errores de medici(cid:243)n. Construir un conjunto de datos con las muestras vÆlidas.
(b) Utilizando cost_complexity_pruning_path (sklearn) y utilizando la entrop(cid:237)a como impureza, calcular todos los α relevantes para la poda de un Ærbol de decisi(cid:243)n.
(c) Utilizando GridSearchCV (sklearn) optimizar el valor de α para un 4-fold, utilizando como mØtrica la F1 macro. Gra(cid:28)car los valores de F1 cross-validada en funci(cid:243)n de α. (cid:190)QuØ α maximiza dicha mØtrica?
(d) Utilizando plot_tree (sklearn) gra(cid:28)car el Ærbol podado. Indicar la cantidad de nodos y hojas.
(e) Encontrar los 5 features mÆs relevantes segœn la Gini importance. c: Es importante resolver todo el ejercicio utilizando solo 1 fit. 2.13 (cid:207) [ver Ejercicio 2.6] La base de datos FASHION-MNIST posee la mismas caracter(cid:237)sticas que la MNIST pero para clasi(cid:28)car 10 tipos de ropa. Se desea entrenar un clasi(cid:28)cador que a partir de una imagen prediga que d(cid:237)gito aparece en ella.
(a) Cargar la base de datos utilizando tensorflow.keras.datasets.fashion_ mnist.load_data. Utilizando imshow (matplotlib) represente 10 muestras del conjunto de testeo elegidas al azar. (cid:190)Que tipo de prenda representa cada categor(cid:237)a?
(b) Utilizando RandomForestClassifier (sklearn), entrenar un bosque aleatorio de 100 Ærboles con impureza Gini. Indicar el accuracy de entrenamiento y testeo.
(c) Utilizando ConfusionMatrixDisplay (sklearn) represente la matriz de confusi(cid:243)n normalizada (testeo) para mostrar la probabilidad de cada predicci(cid:243)n para cada clase con 3 decimales.
(d) Gra(cid:28)car en una imagen los 100 p(cid:237)xeles mÆs relevantes segœn la Gini importance. Indique con un punto negro los mencionados p(cid:237)xeles y deje el resto en blanco.
8

## Gu(cid:237)a 3

a. Aprendizaje No Supervisado
3.1 Dos variables f(cid:237)sicas pX, Y q poseen una densidad de probabilidad conjunta de la forma
pXY px, yq “
4x`2 q
e´p2x` y 2x ` 1
¨ 1tx ą 0, y ą 0u.
Encontrar un mecanismo simple que permita generar una de las variables aleatorias en funci(cid:243)n de la otra y un ruido independiente. Sugiera que variable posiblemente sea la causa y cual el efecto. c: Notar que si T „ Epλq, entonces kT „ Epλ{kq con k ą 0. 3.2 (cid:207) [ver Ejercicio 2.13] Utilizando la base de datos FASHION-MNIST, se desea entrenar un algoritmo de PCA.
(a) Utilizando linalg.eig (numpy), calcular y gra(cid:28)car el porcentaje de energ(cid:237)a en funci(cid:243)n del nœmero de componentes principales.
(b) Gra(cid:28)car el error cuadrÆtico medio de testeo en funci(cid:243)n del nœmero de componentes principales. c: Mucha atenci(cid:243)n a no repetir c(cid:243)mputos. Es decir, aprovechar la reconstrucci(cid:243)n con k componentes principales para el cÆlculo de k ` 1 componentes.
(c) Gra(cid:28)car 10 imÆgenes reconstruidas de testeo (elegidas al azar) utilizando 1, 100 y 784 componentes principales.
(d) Gra(cid:28)car un scatter de las dos primeras componentes principales de las imagenes de testeo, indicando en diferentes colores las clases.
(e) Se desea evaluar el desempeæo del algoritmo de PCA como detector de anomal(cid:237)as. Para ello, construir una base de datos combinando el conjunto de datos de testeo con el conjunto de datos de testeo de la base de datos MNIST (d(cid:237)gitos).
(f) Diseæar un detector de anomal(cid:237)as comparando el error cuadrÆtico contra un umbral. Gra(cid:28)car la curva ROC y marcar el equal error rate para 1, 100 y 784 componentes principales. Interpretar resultados. 3.3 (cid:207) [ver Ejercicio 2.7] Utilizando los dos primeros formantes de la base de datos formantes.txt:
(a) Implementar K-means para 3 clusters. Utilizar, como condici(cid:243)n de parada, tanto cantidad de iteraciones (100 por ejemplo) como convergencia.
(b) Gra(cid:28)car un scatter de la clasi(cid:28)caci(cid:243)n (cid:28)nal de los datos de entrenamiento, resaltando los centroides.
(c) Gra(cid:28)car las fronteras de decisi(cid:243)n, superpuestos a un scatter con las verdaderas etiquetas. 3.4 (cid:207) Se desea comprimir la imagen pikachu_vs_charmander.jpeg a 16 colores, utilizando cluster.KMeans (sklearn).
9
(a) Tomando cada pixel como muestras diferentes, implementar un K-means de 16 clusters.
(b) Utilizar los centroides como diccionario, para convertir cada pixel en un centroide (utilizando el algoritmo previamente entrenado). Utilizar imshow (matplotlib) para gra(cid:28)car la imagen ya codi(cid:28)cada.
(c) Calcular la cantidad de bits necesarios para guardar la imagen antes y despuØs de comprimirla (teniendo en cuenta el etiquetado y los centroides).
3.5 Los habitantes de Smallville pueden ser considerados trabajador registrado, trabajador informal o desempleado con probabilidades θ 2 respectivamente, donde 0 ď θ ď 1. El municipio posee 10.000 habitantes y cuenta con 4.000 trabajadores registrados.
2 y 1
2 , 1´θ
(a) Estimar θ por mÆxima verosimilitud.
(b) Deducir matemÆticamente una recursi(cid:243)n, v(cid:237)a algoritmo EM, que permita estimar θ.
(c) Se denomina puntos (cid:28)jos a los valores de θ que no var(cid:237)an al iterar un paso del algoritmo. Encontrar los puntos (cid:28)jos del problema de recursi(cid:243)n de(cid:28)nido por EM. (d) (cid:207) (cid:190)A que punto converge el problema si θ0 “ 0.99? Analizar resultado. 3.6 (cid:207) Se desea utilizar el algoritmo EM para aproximar la distribuci(cid:243)n de una variable aleatoria a una mezcla de gaussianas.
(a) Generar 100 muestras de una mezcla de gaussianas con pesos 0.1, 0.4, 0.2, 0.3, medias ´4, 0, 4, 5 y varianzas 1, 1.96, 1.44, 1 respectivamente.
(b) Implementar el algoritmo EM para entrenar una mezcla de 6 gaussianas a partir de los datos generados. Inicializar el algoritmo a partir de K-Means. c: Si bien es evidente que los centroides representan las medias de las gaussianas, no es tan claro pensar como inicializar los pesos y varianzas. Justi(cid:28)car su criterio de inicializaci(cid:243)n.
(c) Repetir el inciso anterior utilizando GaussianMixture (sklearn).
(d) Gra(cid:28)car las dos densidades de probabilidad aprendidas, la densidad con que se inicializan (K-Means) y la verdadera en un mismo grÆ(cid:28)co. 3.7 (cid:207) En el archivo instrumentos.zip encontrarÆ audios de diferentes instrumentos musicales. Se desea clasi(cid:28)car entre las 5 clases de instrumentos presentes en la base de datos. Reservando el œltimo archivo de cada instrumento para el conjunto de testeo, se desea entrenar un clasi(cid:28)cador adaptando el algoritmo EM como se menciona a continuaci(cid:243)n.
(a) Utilizando ShortTimeFFT (scipy.signal). Extraer un espectrograma de cada seæal y normalizar en media y varianza a partir del conjunto de datos de entrenamiento. c: Una buena selecci(cid:243)n de criterios es utilizar una (cid:27)t de 64 puntos, un solapamiento del 50 %, descartar la parte simØtrica del espectro y utilizar ventana de hamming de la misma cantidad de puntos de la (cid:27)t.
(b) Entrenar 5 mezclas de 6 gaussianas diagonales cada una (una por cada instrumento).
10
(c) Para todas las combinaciones de desea evaluar que tan veros(cid:237)mil es que las muestras de la clase i-Øsima correspondan al modelo j-Øsimo. Indicar las log-verosimilitud correspondientes en un cuadro de doble entrada.
(d) Asumiendo una probabilidad de cada clase proporcional a la cantidad de muestras de entrenamiento de cada instrumento, calcular las probabilidades a posteriori. Es decir, indicar en un cuadro de doble entrada la probabilidad de la clase j-Øsima para las muestras correspondientes al instrumento i-Øsimo P pj|Diq. c: La funci(cid:243)n softmax (scipy) puede ser œtil.
(e) Sea xptq la seæal correspondiente al audio de testeo de la guitarra. Gra(cid:28)car log P pj|xptqq en funci(cid:243)n del tiempo, para cada uno de los 5 instrumentos (indexados por j). 3.8 (cid:207) La base de datos fetch_olivetti_faces (sklearn) contiene 400 imÆgenes de rostros.
(a) Construir un c(cid:243)digo que cargue los datos de sklearn, cuando estos estØn disponibles, y en caso contrario los cargue del archivo olivetti.npy. Elegir 6 imÆgenes al azar y gra(cid:28)carlas.
(b) Encontrar las relaciones matemÆticas que de(cid:28)nen el algoritmo EM. Puede deducirlas (recomendado) o buscarlas en la bibliograf(cid:237)a. En caso de elegir la segunda, explicar detalladamente como se implementar(cid:237)a.
(c) Utilizando FactorAnalysis (sklearn) reducir la dimensi(cid:243)n a un espacio latente normal de dimensi(cid:243)n 2. Inicializar la matriz Ψ con la diagonal de la matriz de covarianza emp(cid:237)rica de los datos y utilizar la implementaci(cid:243)n lapack.
(d) Se desea explorar el manifold del algoritmo entrenado previamente. De(cid:28)na una grilla regular de 10 ˆ 10 entre r´2, 2s. Cada punto de esa grilla (100 en total) debe ser reconstruido en una imagen (utilizando el decoder entrenado) y mostrar los 100 rostros reconstruidos en una grilla representativa del espacio latente.
b. Aplicaciones espec(cid:237)(cid:28)cas
3.9 (cid:207) La base de datos fetch_20newsgroups (sklearn) posee textos sobre 20 t(cid:243)picos diferentes.
(a) Construir un c(cid:243)digo que cargue los datos de sklearn, cuando estos estØn disponibles, y en caso contrario los cargue del archivo 20news.pkl. Cargar los conjuntos de entrenamiento y testeo omitiendo headers, footers y quotes de las categor(cid:237)as alt.atheism,talk.religion.misc,comp.graphics,sci.space.
(b) Utilizando TfidfVectorizer (sklearn) pre-procesar los datos. c: Se recomienda convertir todo a minœsculas, utilizar como Stop Words las estÆndar del idioma inglØs, descartar el 80 % de las palabras mÆs frecuentes y utilizar la transformaci(cid:243)n tf-idf.
(c) Utilizando LogisticRegression(sklearn), entrenar un clasi(cid:28)cador log(cid:237)stico y evaluar el accuracy con el conjunto de testeo.
3.10 (cid:207) Se desea estudiar relaciones entre pa(cid:237)ses y sus capitales. El archivo country-list. csv contiene la informaci(cid:243)n correspondiente.
11
(a) Descargar las representaciones pre-entrenadas FastText en idioma inglØs. c: El modelo preentrenado puede descargarse en https://dl.fbaipublicfiles. com/fasttext/vectors-crawl/cc.en.300.bin.gz
(b) Utilizando load_model (fasttext), cargar las representaciones pre-entrenadas.
(c) Combinar los pa(cid:237)ses y las capitales de country-list.csv para implementar una funci(cid:243)n que conteste a la pregunta A es a B como C es a ... dando 3 opciones posibles. Para ello, combine las vectorizaciones de A, B y C y devuelva las 3 palabras mas cercanas de la base de datos que acaba de de(cid:28)nir. c: Ej. France es a Paris como England es a ... (London).
(d) Utilizando las vectorizaciones de las palabras de la base de datos, entrenar un algoritmo PCA que reduzca la dimensi(cid:243)n a 2, utilizando decomposition.PCA (sklearn). Gra(cid:28)car las representaciones reducidas de Italy, Rome, France, Paris, Germany y Berlin uniendo los pa(cid:237)ses con sus capitales. 3.11 (cid:207) Se desea crear un sistema para recomendar pel(cid:237)culas. El archivo movies. csv posee una base de datos donde usuarios cali(cid:28)caron (del 1 al 5) diferentes pel(cid:237)culas (0 signi(cid:28)ca sin cali(cid:28)car).
(a) Agregar un usuario a la base de datos con al menos 10 pel(cid:237)culas cali(cid:28)cadas.
(b) Utilizando gradiente descendente entrenar un (cid:28)ltro colaborativo con un espacio latente de dimensi(cid:243)n 10 y λ “ 10. Gra(cid:28)car el riesgo regularizado emp(cid:237)rico en funci(cid:243)n del nœmero de iteraciones (al menos 2000).
(c) Crear un rating ponderando en partes iguales la salida del (cid:28)ltro colaborativo y la cali(cid:28)caci(cid:243)n media de las pel(cid:237)culas.
(d) Recomendar las 10 pel(cid:237)culas con mÆs alto rating al usuario creando en (a).
12

## Gu(cid:237)a 4

4.1 Lucas dispara a un blanco y el disparo impacta en un punto aleatorio pX, 0q con X (en dec(cid:237)metros) una variable aleatoria con distribuci(cid:243)n normal de media nula y varianza 1{τ , donde τ representa la precisi(cid:243)n de Lucas. A priori la precisi(cid:243)n τ tiene una distribuci(cid:243)n chi-cuadrado de 8 grados de libertad. Lucas tiro 10 veces al blanco y observ(cid:243)
i “ 17. En virtud a la informaci(cid:243)n muestral,
ř
i“1 x2
10
(a) Hallar la distribuci(cid:243)n a posteriori.
(b) Hallar la distribuci(cid:243)n predictiva. c: Mirar con cariæo la distribuci(cid:243)n t-student.
(c) Estimar la probabilidad de que su pr(cid:243)ximo tiro se aleje del centro en menos de 2.1 dec(cid:237)metros. c: Se recomienda calcular el cuantil con un software. 4.2 (cid:207) [ver Ejercicio 2.7] Utilizando los dos primeros formantes de la base de datos formantes.txt:
(a) Utilice el comando train_test_split (sklearn) para de(cid:28)nir dos conjuntos con las proporciones 70 % y 30 %.
(b) Implementar un modelo GNB. Gra(cid:28)car las muestras en un scatter, las fronteras de decisi(cid:243)n y resaltar medias y covarianzas de cada gaussiana (una curva de nivel) del modelo.
(c) Repetir el inciso anterior para LDA y QDA, programando su propio c(cid:243)digo.
(d) Clasi(cid:28)car el conjunto de testeo con cada mØtodo. Indicar la porcentaje de acierto. 4.3 (cid:207) [ver Ejercicio 3.9] Utilizando fetch_20newsgroups (sklearn): (a) Cargar los conjuntos de entrenamiento y testeo omitiendo headers, footers y quotes.
(b) Utilizando CountVectorizer (sklearn) pre-procesar los datos. c: Se recomienda convertir todo a minœsculas, utilizar como Stop Words las estÆndar del idioma inglØs, descartar el 95 % de las palabras mÆs frecuentes y descartar las palabras vistas 1 sola vez.
(c) Bajo las hip(cid:243)tesis de Multinomial Naive Bayes con α “ p1, 1, ¨ ¨ ¨ , 1q, hallar los estimadores bayesianos puntuales para las probabilidades de cada palabra.
(d) A partir de la estimaci(cid:243)n anterior, evaluar el accuracy con el conjunto de testeo. 4.4 (cid:207) [ver Ejercicio 3.6] Utilizando los datos del ejercicio Ejercicio 3.6, implementar un Variational Bayes Gaussiano. Suponer a priori m “ 0, δ “ ν “ β “ 0.05 y α “ p1, 1, 1, 1, 1, 1q, y utilizar el algoritmo EM para inicializar las probabilidades.
(a) Con la distribuci(cid:243)n a posteriori generar 3 muestras de parÆmetros y gra(cid:28)car la densidad de X|µ, λ, π para cada uno de esos conjuntos de parÆmetros. Comparar con la densidad verdadera y con la estimada por el algoritmo EM.
13
(b) Gra(cid:28)car la densidad predictiva. Comparar con la densidad verdadera y con la estimada por el algoritmo EM. c: Las funciones gamma y digamma (scipy) pueden ser œtiles.
4.5 (cid:207) Estimar mediante un Monte-Carlo de 20 puntos
ş
2 ´1
e´t2{2 ? 2π
dt si
(a) Las variables aleatorias se sortean de forma uniforme.
(b) Las variables aleatorias se sortean de forma normal.
Repetir el experimento 100 veces e indicar el error promedio en cada caso. 4.6 (cid:207) [ver Ejercicio 4.4] Utilizando los datos del ejercicio Ejercicio 3.6, entrenar un modelo Markov Chain Monte-Carlo con pymc. Suponer a priori m “ 0, δ “ ν “ β “ 0.05 y α “ p1, 1, 1, 1, 1, 1q, y simular 3 cadenas de 500 experimentos cada una. Gra(cid:28)car la densidad predictiva para cada cadena. Comparar con la densidad verdadera, con la estimada por el algoritmo EM y con la predictiva estimada utilizando Bayes Variacional. 4.7 (cid:207) Se desean modelar los resultados de un partido de futbol. Para esto, se propone asumir que la cantidad de goles que marca un equipo es una funci(cid:243)n de su potencia ofensiva combinada con la fuerza defensiva del rival. TambiØn se debe tener en cuenta la ventaja de la local(cid:237)a. El modelo se verÆ as(cid:237):
potencial local = ventaja local(cid:237)a + ataque local + defensa visitante potencial visitante = ataque visitante + defensa local
Notar que mientras tener alto ataque es positivo, tener alta defensa es negativo. Cada equipo tendrÆ su propio rating de ataque y defensa, pero estÆs dependerÆn de una distribuci(cid:243)n comœn (si bien cada equipo de fœtbol es claramente diferente entre s(cid:237), todos juegan en la misma liga). Vamos a suponer que el ataque y defensa (inicial) de cada equipo son variables aleatorias normales de media nula. A priori, la precisi(cid:243)n (inversa de la varianza) de ataque y la de defensa (comunes a todos los equipos) serÆn variables aleatorias gamma de parÆmetros 0.1 y 0.1.
Dado que existen innumerables combinaciones de parÆmetros que potencialmente podr(cid:237)an darnos los mismos resultados, se propone restar las cali(cid:28)caciones medias (es decir, el promedio de todos los equipos) tanto de ataque como defensa para garantizar la identi(cid:28)cabilidad. Esto obliga al modelo a brindarnos un resultado reproducible y mantiene los parÆmetros en un rango realista. De esta manera se construye el ataque y defensa (cid:28)nal de cada equipo.
Una vez de(cid:28)nidos los potenciales tanto del local como del visitante, es necesario modelar la cantidad de goles de cada equipo. La cantidad de goles de cada equipo se supondrÆn Poisson de media epotencial (para que sean positivos).
Por œltimo, para la ventaja de local(cid:237)a se supondrÆ una (cid:29)at-distribution prior
(buscar informaci(cid:243)n al respecto).
(a) La base de datos liga_arg.csv contiene todos los resultados del futbol argentino desde el profesionalismo. Armar un conjunto de datos de entrenamiento con todas las competiciones iniciadas en el 2020 o posterior.
14
(b) Construir la arquitectura descripta. Utilizando model_to_graphviz (pymc) mostrar el grafo del modelo. c: En el modelo aqu(cid:237) descripto no tiene mucha relevancia las muestras predcitivas, sino que el foco debe estar sobre las posteriors.
(c) Entrenar el modelo bayesiano con los datos del inciso paq. Utilizando plot_ posterior (pymc) gra(cid:28)car la distribuci(cid:243)n a posteriori de la ventaja de local(cid:237)a.
(d) Reportar los 5 equipos con mejores ataques esperados. Repetir con los de mejores defensas.
(e) Diseæar una funci(cid:243)n que, dado un equipo local y uno visitante, estime la cantidad de goles esperados por cada equipo en un partido. Estimar el valor esperado del resultado global en un cruce ida y vuelta entre River y Boca (dos partidos, uno local River y el otro local Boca). c: Si X|A “ a „ Poipeaq, entonces ErXs “ EreAs.
(f) Diseæar una funci(cid:243)n que, dado un equipo local y uno visitante, estime la probabilidad que gane el local, empate y gane el visitante. c: Si X|A “ a „ Poipeaq y Y |B “ b „ Poipebq, entonces PpX ą Y q “ ErPpX “ i, Y “ j|A “ a, B “ bqs. Para su implementaci(cid:243)n numØrica asuma que la mÆxima cantidad de goles por un equipo es 10 (a la hora de implementarlo la serie se aproxima con una sumatoria hasta 10).
i´1 j“0
8 i“0
ř
ř
(g) Construir un conjunto de datos de testeo con la œltima fecha jugada del campeonato local al momento de resolver el ejercicio (solo tener en cuenta los partidos donde ambos equipos aparezcan en el conjunto de datos de entrenamiento). Utilizar como predicci(cid:243)n hard la mÆxima probabilidad estimada dentro de las 3 clases de(cid:28)nidas en el inciso anterior. Reportar el porcentaje de acierto.

### BIBLIOGRAF˝A SUGERIDA

15
1. (cid:16)Pattern Recognition and Machine Learning(cid:17), C. Bishop. 2. (cid:16)The Elements of Statistical Learning: Data Mining, Inference, and Predic-
tion(cid:17), J. Hastie, T. Tibshirani, R. Friedman.
3. (cid:16)Machine Learning: A Probabilistic Perspective(cid:17), K. Murphy. 4. (cid:16)Introduction to Machine Learning with Python: A Guide for Data Scien-
tists(cid:17), A. M(cid:252)ller, S. Guido.
5. (cid:16)Bayesian Methods for Hackers: Probabilistic Programming and Bayesian
Inference(cid:17), C. Davidson-Pilon.
6. (cid:16)Pattern Classi(cid:28)cation(cid:17), R. Duda, P. Hart, D. Stork. 7. (cid:16)Deep Learning(cid:17), I. Goodfellow, Y. Bengio, A. Courville. 8. (cid:16)Elements of Information Theory(cid:17), T. Cover, J. Thomas. 9. (cid:16)Elements of Causal Inference: Foundations and Learning Algorithms(cid:17), J.
Peters, D. Janzing, B. Sch(cid:246)lkopf.
10. (cid:16)Foundations of Machine Learning(cid:17), M. Mohri, A. Rostamizadeh, A. Talwal-
kar.
11. (cid:16)Data Analysis: A Bayesian Tutorial(cid:17), D. Sivia and J.Skilling. 12. (cid:16)The Bayesian Choice: From Decision-Theoretic Foundations to Computatio-
nal Implementation(cid:17), C. Robert.