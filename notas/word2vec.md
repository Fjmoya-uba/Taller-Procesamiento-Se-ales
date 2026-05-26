# Word2Vec: Representación vectorial de palabras

## El problema

Las redes neuronales trabajan con números. Una palabra como "king" no es un número, entonces hay que convertirla. La solución naive es un **one-hot vector**: si tenés un vocabulario de $K$ palabras, "king" es un vector de $K$ dimensiones con un 1 en su posición y ceros en el resto.

El problema es doble:
- Si $K = 1.000.000$, cada palabra ocupa un vector de un millón de dimensiones — una cantidad enorme de memoria para guardar básicamente nada
- No captura ninguna relación semántica: "king" y "queen" son tan distintos como "king" y "banana"

Se necesita algo más compacto y útil.

---

## La idea de Word2Vec

Word2Vec es un **encoder**: convierte palabras en vectores numéricos densos (embeddings) que capturan relaciones semánticas. En el contexto del curso, cumple el mismo rol que las features MFCC en el TP3 de audio — convierte datos crudos en una representación numérica útil para el modelo downstream.

La observación clave es que **palabras que aparecen en contextos similares tienen significados similares**. "King" y "queen" aparecen frecuentemente cerca de "throne", "crown", "royal", "realm". "Banana" aparece cerca de "fruit", "yellow", "peel". Esa diferencia de contexto es lo que el modelo va a capturar.

---

## Arquitectura

Una red neuronal de **una sola capa oculta**. Nada complejo:

$$\text{one-hot}(\text{king}) \xrightarrow{W} \vec{v}_{\text{king}} \in \mathbb{R}^{300} \xrightarrow{W'} \text{softmax} \rightarrow P(\text{palabra vecina})$$

La matriz $W \in \mathbb{R}^{K \times 300}$ es el corazón del modelo. Cada fila es el **embedding** de una palabra — sus 300 features aprendidos. Multiplicar el one-hot de "king" por $W$ simplemente selecciona la fila correspondiente:

$$\vec{e}_k \cdot W = \vec{v}_k \quad \text{(fila } k \text{ de } W\text{)}$$

Es un lookup disfrazado de multiplicación matricial. Los 300 features no tienen interpretación directa — son dimensiones abstractas que emergieron del entrenamiento para minimizar el error de predicción.

---

## La tarea de entrenamiento (Skip-gram)

Dada una palabra central, predecir sus palabras vecinas dentro de una ventana de $\pm n$ posiciones (típicamente $n=2$).

Para la oración *"The king wore the crown"* con ventana de 2:

| Central (pos) | Vecinas | Pares generados |
|---|---|---|
| the (0) | king, wore | 2 |
| king (1) | the, wore, the | 3 |
| wore (2) | the, king, the, crown | 4 |
| the (3) | king, wore, crown | 3 |
| crown (4) | wore, the | 2 |

**Total: 14 pares** para una sola oración de 5 palabras.

---

## El entrenamiento: un jaloncito por par

Para cada par (central, vecina), el objetivo es maximizar $P(\text{vecina} \mid \text{central})$. Esa probabilidad depende del producto escalar entre los dos vectores:

$$P(\text{vecina} \mid \text{central}) = \sigma(\vec{v}_{\text{central}} \cdot \vec{v}_{\text{vecina}})$$

donde $\sigma$ es la sigmoide $\sigma(x) = \frac{1}{1+e^{-x}}$, que mapea cualquier número a $(0, 1)$.

El ajuste (jalón) que recibe $\vec{v}_{\text{central}}$ en cada par es:

$$\Delta \vec{v}_{\text{central}} = \alpha \cdot \underbrace{(1 - \sigma(\vec{v}_{\text{central}} \cdot \vec{v}_{\text{vecina}}))}_{\text{magnitud}} \cdot \underbrace{\vec{v}_{\text{vecina}}}_{\text{dirección}}$$

### Magnitud del jalón

| Situación geométrica | Producto escalar | Magnitud del jalón |
|---|---|---|
| Vectores opuestos | Negativo | Grande — el modelo está muy equivocado |
| Vectores perpendiculares | 0 | Medio — el modelo predice 50/50 |
| Vectores alineados | Positivo alto | Chico — el modelo ya predice bien |

El jalón es proporcional al error. Cuando dos vectores ya están alineados, casi no se mueven. Cuando están opuestos, se corrigen fuertemente. Es un sistema de control con retroalimentación negativa.

### Dirección del jalón

El jalón siempre apunta hacia el vector de la vecina. Ambos vectores del par se acercan mutuamente.

---

## Por qué "the" no queda cerca de "king"

"The" aparece en el 50% de todas las oraciones. Sus jalones vienen de todas las direcciones — hacia "king", hacia "cat", hacia "ran", hacia "park"... Con el tiempo esos jalones se cancelan entre sí y "the" queda en el centro del espacio, cerca de todo y de nada.

"Crown" en cambio aparece casi exclusivamente en contextos de realeza. Sus jalones son consistentes: siempre hacia "king", "queen", "throne", "royal". Todos jalan en la misma dirección y el vector converge a una región específica del espacio.

Usando la analogía del apunte del curso: es como un objeto atado con resortes. Los resortes de stopwords tiran en todas las direcciones y se anulan. Los resortes de palabras temáticas tiran hacia el mismo lugar y dominan.

---

## Negative Sampling: el truco computacional

Calcular el softmax sobre $K = 1.000.000$ palabras en cada paso es prohibitivo. La solución: **Negative Sampling**.

Para cada par positivo (king, crown) se toman ~5 pares negativos aleatorios (king, banana), (king, integral)... y el modelo solo aprende a distinguir los pares reales de los falsos. Es un clasificador binario en vez de multiclase:

$$\mathcal{L} = -\log \sigma(\vec{v}_{\text{king}} \cdot \vec{v}_{\text{crown}}) - \sum_{i=1}^{5} \log \sigma(-\vec{v}_{\text{king}} \cdot \vec{v}_{\text{ruido}_i})$$

Esto reduce el cómputo de $O(K)$ a $O(1)$ por paso.

---

## Convergencia

Word2Vec no para cuando el jalón cae por debajo de una tolerancia. Usa un **learning rate decreciente**:

$$\alpha_t = \alpha_0 \cdot \left(1 - \frac{t}{T}\right)$$

donde $t$ es la iteración actual y $T$ el total. Arranca en $\alpha_0 \approx 0.025$ y baja linealmente hasta casi 0 al final. Los jalones se van apagando solos. Se corre el corpus completo 5 veces (5 epochs).

Las palabras muy frecuentes se descartan aleatoriamente con cierta probabilidad en cada epoch (**subsampling**) para reducir la redundancia de stopwords sin eliminarlas.

---

## El resultado: geometría semántica

Después del entrenamiento, $W$ está fija y se usa como tabla de consulta. La arquitectura de predicción se descarta — ya no importa. Solo importan los vectores.

Lo que emerge es una geometría rica: las relaciones semánticas se traducen en operaciones vectoriales. El ejemplo clásico:

$$\vec{\text{king}} - \vec{\text{man}} + \vec{\text{woman}} \approx \vec{\text{queen}}$$

Esto no fue diseñado. "King" y "queen" comparten vecinas de realeza (throne, crown, royal) pero difieren en vecinas de género (he/she, his/her, prince/princess). El modelo aprendió una dirección en $\mathbb{R}^{300}$ que separa géneros, y otra que captura realeza. La resta cancela una y preserva la otra.

---

## Comparación con el pipeline del curso

| TP3 (audio) | Word2Vec (texto) |
|---|---|
| Señal de audio | Texto crudo |
| MFCC, energía, ZCR | Embedding de 300 dimensiones |
| Diseñado a mano | Aprendido del corpus |
| Entrada al clasificador | Entrada al modelo downstream |

La diferencia clave: los MFCC fueron diseñados por ingenieros con conocimiento del dominio. Los embeddings de Word2Vec emergen solos del entrenamiento — nadie le dijo qué poner en cada dimensión.

---

## Limitación principal → motiva FastText

Si en el entrenamiento nunca apareció la palabra "FastTexting", Word2Vec no tiene embedding para ella. Se queda en blanco. Esta limitación es la que FastText viene a resolver.
