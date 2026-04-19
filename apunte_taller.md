CARATULA
i
ii

# Resumen

todo
iii
iv

# Agradecimientos

todo
v
vi

# ´Indice general

Resumen
III
1. Probabilidad y Estad´ıstica
1.1. Teor´ıa de Probabilidad . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1.1. Variables Aleatorias . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1.2. Momentos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2. Estad´ıstica . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1 1 2 4 9 1.2.1. Distribuci´on Emp´ırica e Histograma . . . . . . . . . . . . . . . . . . 10 1.2.2. Simulaci´on . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11 1.2.3. Estad´ıstica Frecuentista . . . . . . . . . . . . . . . . . . . . . . . . 12 1.2.4. Estad´ıstica Bayesiana . . . . . . . . . . . . . . . . . . . . . . . . . . 13 1.2.4.1. Estad´ısticos Suficientes . . . . . . . . . . . . . . . . . . . . 15 1.2.4.2. Test de hip´otesis . . . . . . . . . . . . . . . . . . . . . . . 16
2. Regresi´on en Inteligencia Artificial
2.2.1. Codificaci´on de variables categ´oricas
17 2.1. Relaci´on de Compromiso Sesgo/Varianza . . . . . . . . . . . . . . . . . . . 18 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21 2.2. Regresi´on Lineal . . . . . . . . . . . . . . . . . 23 2.3. Gradiente Descendente . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23 2.3.1. Normalizaci´on como pre-procesamiento . . . . . . . . . . . . . . . . 24 2.3.2. Learning Rate ´optimo . . . . . . . . . . . . . . . . . . . . . . . . . 26 2.4. Regresi´on Polin´omica . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28 2.4.1. Conjuntos de datos . . . . . . . . . . . . . . . . . . . . . . . . . . . 31 2.4.2. Regularizaci´on . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32 2.4.3. Etapa de validaci´on . . . . . . . . . . . . . . . . . . . . . . . . . . . 34 2.4.3.1. Validaci´on Cruzada . . . . . . . . . . . . . . . . . . . . . . 35
3. Clasificaci´on en Inteligencia Artificial
37 3.1. Optimalidad en Clasificaci´on . . . . . . . . . . . . . . . . . . . . . . . . . . 38 3.1.1. Clasificador Bayesiano . . . . . . . . . . . . . . . . . . . . . . . . . 38 3.1.2. Entrop´ıa Cruzada . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43 3.1.2.1. Elementos de Teor´ıa de Informaci´on . . . . . . . . . . . . 44 3.2. Regresi´on Log´ıstica . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46 3.2.1. Regresi´on Log´ıstica Binaria . . . . . . . . . . . . . . . . . . . . . . 47 3.2.2. Regresi´on Log´ıstica Categ´orica . . . . . . . . . . . . . . . . . . . . . 48
vii
´Indice general
3.2.3. Regresi´on Log´ıstica Polin´omica y Overfitting . . . . . . . . . . . . . 50 3.3. Figuras de M´erito en Clasificaci´on . . . . . . . . . . . . . . . . . . . . . . . 52 3.3.1. Figuras de M´erito en Clasificaci´on Binaria . . . . . . . . . . . . . . 52 3.3.2. Figuras de M´erito en Clasificaci´on Categ´orica . . . . . . . . . . . . 55 3.4. An´alisis del Discriminante . . . . . . . . . . . . . . . . . . . . . . . . . . . 56 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59 3.5. Vecinos m´as Cercanos . . . . . . . . . . . . . . . . . . . . . . . . . 62 3.6. M´aquina de Vectores Soporte 3.6.1. SVM est´andar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62 3.6.2. Parches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64 3.6.3. Dualidad en SVM . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66 3.7. ´Arboles de Decisi´on . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69 3.7.1. Podado . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74 3.7.2. Bosques Aleatorios . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
4. Aprendizaje no Supervisado
4.1.1.
77 4.1. Causalidad en Aprenizaje Semisupervisado . . . . . . . . . . . . . . . . . . 78 Influencia del aprendizaje semisupervisado en modelos causales . . . 81 4.2. Reducci´on de dimensi´on y Manifold . . . . . . . . . . . . . . . . . . . . . . 82 4.3. An´alisis de Componentes Principales . . . . . . . . . . . . . . . . . . . . . 86 . . . . . . . . . . . . . . . . . . . . . . 88 4.4. Clustering y el algoritmo K-Means 4.5. Algoritmo Expectaci´on-Maximizaci´on . . . . . . . . . . . . . . . . . . . . . 89 4.5.1. Modelo de Mezclas . . . . . . . . . . . . . . . . . . . . . . . . . . . 93 . . . . . . . . . . . . . . 94 4.5.2. An´alisis de Factores . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
4.5.1.1. Modelo de mezcla de Gaussianas
5. Procesamiento de Datos orientado a Aplicaciones Espec´ıficas
99 5.1. Procesamiento de Audio . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99 5.1.1. Espectrograma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99 5.1.2. Coeficientes Mel-Cepstrum . . . . . . . . . . . . . . . . . . . . . . . 99 5.2. Procesamiento de Texto . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99 5.3. Sistemas de Recomendaci´on . . . . . . . . . . . . . . . . . . . . . . . . . . 99 Ingenier´ıa de Caracter´ısticas . . . . . . . . . . . . . . . . . . . . . . . . . . 99 5.4. 5.4.1. Test de Independencia Chi-Cuadrado . . . . . . . . . . . . . . . . . 99 5.4.2. Tests ANOVA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
6. Modelos Bayesianos
100 Inferencia Bayesiana . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100 6.1.1. Redes Bayesianas . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
6.1.
viii
´Indice general
6.3.1. Mezcla de Gaussianas escalares en Bayes Variacional
6.1.2. Ejemplo de Modelo Bayesiano . . . . . . . . . . . . . . . . . . . . . 103 6.2. Bayes Naive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105 6.2.1. Bayes Naive Gaussiano . . . . . . . . . . . . . . . . . . . . . . . . . 106 6.2.2. Bayes Naive Multinomial . . . . . . . . . . . . . . . . . . . . . . . . 106 6.2.2.1. Entrenamiento de MNB . . . . . . . . . . . . . . . . . . . 107 6.3. Bayes Variacional Gaussiano . . . . . . . . . . . . . . . . . . . . . . . . . . 109 . . . . . . . . 110 6.3.1.1. Distribuci´on a posteriori en GVB . . . . . . . . . . . . . . 111 6.3.1.2. Distribuci´on Predictiva en GVB . . . . . . . . . . . . . . . 113 . . . . . . . . . . . . . . . 115 6.4.1. Algoritmos de Muestreo MCMC . . . . . . . . . . . . . . . . . . . . 117 6.4.1.1. Muestreo de Gibbs . . . . . . . . . . . . . . . . . . . . . . 117 6.4.1.2. Muestreo Metropolis . . . . . . . . . . . . . . . . . . . . . 119 . . . . . . . . . . . . . . . . 121 6.4.1.3. NUTS (No-U-Turn Sampler) 6.4.1.4. Ejemplo de Modelo Complejo . . . . . . . . . . . . . . . . 123 . . . . . . . . . . . . . . . . . . . . . . . . 124 Introducci´on a PyMC . . . . . . . . . . . . . . . . . . . . . . . . . . 125
6.4.2. Calidad de las muestras 6.4.3.
6.4. Monte Carlo por Cadenas de Markov (MCMC)
Bibliograf´ıa
128
ix
x

# 1


# Probabilidad y Estad´ıstica

Las expectativas sobre los objetivos que la inteligencia artificial podr´a alcanzar en los pr´oximos a˜nos tienden a ser muy ambiciosos. Avances constantes y no circunstanciales, solo ser´an posibles con el entendimiento absoluto en la materia, alej´andose del enfoque de prueba y error.
El boom de la inteligencia artificial lleg´o para quedarse. Cada vez m´as, las decisiones asociadas a actividades comerciales y/o tecnol´ogicas son tomadas en base a resultados algor´ıtmicos. Dichas decisiones, lejos de basarse en reglas r´ıgidas creadas por programadores, son tomadas en base al reconocimiento de patrones observados en experiencias estad´ısticas previas, definiendo lo que se conoce como el aprendizaje estad´ıstico. Aunque la inteligencia artificial nos ha llevado a conseguir logros notables en las ´ultimas d´ecadas, las expectativas por lo que este campo ser´a capaz de alcanzar en los pr´oximos a˜nos tienden a exagerarse m´as de lo que podr´ıa ser posible. Para evitar todo tipo de decepci´on, es imprescindible entonces lograr avances permanentes que eviten todo tipo de estancamiento. Avances constantes y no circunstanciales, solo ser´an posibles con el entendimiento absoluto en la materia, alej´andose del enfoque de prueba y error. El estudio de la matem´atica detr´as de estos m´etodos es indispensable para transitar este camino. Quiz´as la ´unica manera de comprender a la m´aquina sea con matem´atica.

## 1.1. Teor´ıa de Probabilidad

La probabilidad es una teor´ıa matem´atica que estudia el azar y la incertidumbre por medio de experimentos aleatorios [1]. La misma, se desarrolla en un marco conocido como espacio de probabilidad. Un espacio de probabilidad (Ω, A, P) consta de una terna formada por un espacio muestral Ω que posee todos los resultados posibles de un experimento aleatorio, una sigma-´algebra A que contiene todos los conjuntos medibles, y una medida de probabilidad P que justamente mide que tan probable es un evento; cada uno con ciertas caracter´ısticas. Las dos f´ormulas m´as caracter´ısticas para una P : A → [0, 1] son la f´ormula de probabilidades totales y la probabilidad condicional.
1
Cap´ıtulo 1. Probabilidad y Estad´ıstica
Propiedades 1.1
∅ ∀ i ̸= j y (cid:83)m
1. Sean A1, · · · Am ∈ A una partici´on de Ω (es decir Ai ∩ Aj = i=1 Ai = Ω), entonces para todo B ∈ A:
P(B) =
P(Ai ∩ B)
m (cid:88)
i=1
2. Sea B ∈ A un evento con P(B) > 0, entonces
P(A|B) =
P(A ∩ B) P(B)
Combinando estas dos f´ormulas surge la famosa regla de bayes:
P(Ak|B) =
P(B|Ak)P(Ak)
(cid:80)m
i=1
P(B|Ai)P(Ai)
(1.1)
(1.2)
(1.3)
Un concepto relacionado con estas expresiones matem´aticas es lo que se conoce como
independencia estad´ıstica.
Definici´on 1.1 Dos eventos A, B ∈ A son independientes si P(A ∩ B) = P(A)P(B).

### 1.1.1. Variables Aleatorias

Distribuci´on Notaci´on
PX(x)
Soporte
E[X]
var(X)
Bernoulli
Ber(p)
Binomial
Bin(n, p)
Geom´etrica
Geo(p)
Pascal
Pas(k, p)
Poisson
Poi(µ)
px(1 − p)1−x (cid:1)px(1 − p)n−x
(cid:0)n x
(1 − p)x−1p (cid:1)(1 − p)x−kpk
(cid:0)x−1 k−1
{0, 1}
{0, · · · , n}
N
{k, k + 1, · · · }
µxe−µ x!
N0
p
np
1 p
k p
µ
p(1 − p)
np(1 − p)
1−p p2 k 1−p p2
µ
Cuadro 1.1: Algunas de las variables discretas m´as habituales.
Trabajar con eventos gen´ericos puede ser tedioso. Las variables aleatorias son funciones X : Ω → R que permiten codificar los resultados de un experimento aleatorio en valores num´ericos. La medida de probabilidad sobre una variable aleatoria se caracteriza con la funci´on de distribuci´on FX(x) = P(X ≤ x). Se denomina ´atomo a todo x ∈ R tal que P(X = x) > 0 (discontinuidades de la funci´on de distribuci´on). Si la suma de las probabilidades de los ´atomos vale 1 la variable se denomina discreta. Si en cambio, la funci´on de distribuci´on es continua, la variable se denomina continua. En caso de no ser ni continua ni discreta se denomina variable mixta.
El uso de la funci´on de distribuci´on para efectuar c´alculos sigue siendo un poco inc´omodo, por eso surgen la funci´on de masa de probabilidad PX(x) = P(X = x) para
2
Cap´ıtulo 1. Probabilidad y Estad´ıstica
variables discretas y la funci´on de densidad de probabilidad pX(x) = F ′ X(x) para las variables continuas1. Cuando se habla de distribuci´on a secas, se hace referencia a la medida de probabilidad asociada, siendo indiferente si la variable se representa con la funci´on de distribuci´on, la masa de probabilidad o la densidad. Cuando se quiere hablar en general, y no se sabe si la variable es discreta o continua, se usar´a la notaci´on pX la cu´al debe interpretarse como masa o densidad seg´un corresponda. En este sentido, pX(x) debe ser una funci´on no negativa que integre 12. Se denomina soporte a X = {x ∈ R : pX(x) > 0}3. Algunas de las variables m´as conocidas pueden verse en el Cuadro 1.1 para el caso de las variables aleatorias discretas y en el Cuadro 1.2 para las variables continuas4.
Distribuci´on
Notaci´on
Uniforme
U(a, b)
Normal
N (µ, σ2)
Exponencial
exp(λ)
Gamma
Beta
Chi cuadrado
t-student
Γ(ν, β)
β(a, b)
χ2 k
tν
pX(x)
1 b−a
1√
2σ2
2πσ2 e− (x−µ)2 λe−λx
Γ(a+b)
βν Γ(ν) xν−1e−βx Γ(a)Γ(b)xa−1(1 − x)b−1 x k
2 −1e− x
2
1 k 2 ) 2 Γ( k 2 (cid:16) 2 ) Γ( ν+1 √ 2 ) νπΓ( ν
(cid:17)− ν+1
2
1 + t2 ν
Soporte E[X]
var(X)
[a, b]
R
[0, ∞)
[0, ∞)
[0, 1]
[0, ∞)
R
a+b 2
µ
1 λ
ν β
(b−a)2 12 σ2
1 λ2
ν β2
a a+b
ab (a+b)2(a+b+1)
k
0
2k
ν ν−2
Lomax
Lomax(α, β)
αβα (x+β)α+1
[0, ∞)
β α−1
β2α (α−1)2(α−2)
Cuadro 1.2: Algunas de las variables discretas m´as habituales.
As´ı como existen las variables aleatorias, se pueden definir los vectores aleatorios. En este contexto, las distribuciones involucradas reciben el nombre de conjunta (por ejemplo pXY (x, y)), marginal (pX(x) y pY (y)) y condicional (pX|Y =y(x) y pY |X=x(y)). Las Props. 1.1 tendr´an su contraparte con las funciones masa o las densidades.
Propiedades 1.2
1. Las distribuciones marginales pueden calcularse como
(cid:90)
pY (y) =
pXY (x, y)dx
(1.4)
X
1Siendo rigurosos, las variables con densidad son un subgrupo dentro de las variables continuas lla-
madas absolutamente continuas.
2En el caso de variables discretas, deben intercambiarse las integrales asociadas a dichas variables por
sumas o series seg´un corresponda.
3Siendo rigurosos, el soporte es la clausura de este conjunto. 4La varianza de la t-student solo existe para ν > 2. La media de la Lomax solo existe para α > 1 y su
varianza para α > 2.
3
Cap´ıtulo 1. Probabilidad y Estad´ıstica
2. Las distribuciones condicionales pueden calcularse como
pY |X=x(y) =
pXY (x, y) pX(x)
(1.5)
De igual manera, dos variables aleatorias (X, Y ) son independientes si y solo si su distribuci´on conjunta se puede factorizar como pXY (x, y) = pX(x)pY (y). Algunos de los vectores aleatorios m´as conocidos pueden verse a continuaci´on.
Definici´on 1.2 El vector aleatorio X = (X1, · · · , Xd) tiene distribuci´on normal multivariada X ∼ N (µ, Σ) si su densidad conjunta es de la forma:
p(X1, · · · , Xd) =
e− 1
2 (x−µ)T Σ−1(x−µ)
(1.6)
1 2 (cid:112)|Σ| (2π) d
De igual manera, el vector aleatorio X = (X1, · · · , Xd) tiene distribuci´on multinomial X ∼ Mn(n, [p1, · · · , pd]) si su funci´on de probabilidad conjunta es de la forma: (cid:32) d (cid:89)
(cid:40) d
(cid:88)
(cid:41)
(cid:33)
pxi i
1
xi = n, x ∈ Nd 0
(1.7)
P (X1, · · · , Xd) =
n! i=1 xi!
(cid:81)d
i=1
i=1
La probabilidad conjunta, siguiendo (1.5), siempre se puede factorizar de la forma pXY (x, y) = pY |X=x(y)pX(x). Dado que en probabilidad este tipo de descomposiciones es ´unica, cuando la conjunta es factorizada inmediatamente se conoce la marginal y la condicional. El siguiente ejemplo muestra como se puede factorizar anal´ıticamente este tipo de conjunta.
Ejemplo 1.1 Sea pXY (x, y) = e−x1{0 < y < x}, hallar pX(x) y pY |X=x(y).
En la factorizaci´on pXY (x, y) = pY |X=x(y)pX(x), la variable y aparece solamente en una de las distribuciones, por lo que el primer paso es separar todos los lugares donde aparezca dicha variable pXY (x, y) = 1{0 < y < x} · e−x1{x > 0}. Luego, completando la densidad condicional para que integren 1 en y (ayud´andose con el Cuadro 1.2), puede verse que
pXY (x, y) =
1 {0 < y < x} (cid:123)(cid:122) (cid:125) pY |X=x(y) En este caso, del Cuadro 1.2, se deduce que Y |X = x ∼ U(0, x) y X ∼ Γ(2, 1).
· xe−x1 {x > 0} (cid:123)(cid:122) (cid:125) (cid:124) pX (x)
(1.8)
1 x (cid:124)

### 1.1.2. Momentos

En muchas circunstancias, tener toda una funci´on que caracterice un experimento aleatorio es abrumador. Se denominan momentos a las magnitudes m´as relevantes que caracterizan a las variables aleatorias, caracterizadas por el operador esperanza E[·]. Los m´as representativos son la media E[X] = (cid:82) X x · pX(x)dx, que representa a la variable aleatoria como una constante, y la varianza var(X) = E[(X − E[X])2], que representa el error que
4
Cap´ıtulo 1. Probabilidad y Estad´ıstica
se comente al aproximar a la variable aleatoria con su media. Algunas de las propiedades b´asicas de los momentos se presentan a continuaci´on.
Propiedades 1.3 Propiedades de la esperanza.
1. Cuando se aplican funciones sobre variables aleatorias, no es necesario conocer
la distribuci´on de la nueva variable E[g(X)] = (cid:82)
X g(x)pX(x)dx.
2. La esperanza es lineal E[aX + b] = a · E[X] + b.
3. Las probabilidades son un caso particular de las esperanzas E[1{X ∈ A}] =
P(X ∈ A).
4. La varianza puede simplificar su c´alculo como var(X) = E[X 2] − E[X]2.
5. El comportamiento de la varianza frente a transformaciones afines es var(aX +
b) = a2 · var(X).
Adem´as, el siguiente teorema muestra en que sentido la media es la mejor aproximaci´on constante de una variable aleatoria y como la viarainza nos da una idea de su error. Se basa en utilizar como criterio el error cuadr´atico medio.
Propiedades 1.4 E[(Y − c)2] ≥ var(Y ) con igualdad si y solo si c = E[Y ].
Demostraci´on 1.1 (Prop. 1.4) Como demostraci´on, notar que la funci´on a minimizar se puede escribir como una par´abola convexa en funci´on de c (usando linealidad de la esperanza): E[Y 2] − 2cE[Y ] + c2. Con lo cu´al, su v´ertice se alcanza en c = E[Y ], y para dicho valor el m´ınimo vale E[(Y − E[Y ])2] = var(Y ).
Los vectores aleatorios tambi´en tienen sus momentos asociados, definidos a trav´es del operador esperanza. El momento m´as representativo de un vector (X, Y ) es su covarianza cov(X, Y ) = E[(X − E[X])(Y − E[Y ])]. La esperanza aplicadas sobre vectores aleatorios tambi´en tiene sus propiedades, algunas de las cuales pueden verse a continuaci´on,
Propiedades 1.5 (cid:82) X g(x, y)pXY (x, y)dxdy.
(cid:82) Y
1. Al igual que en el caso escalar, sigue valiendo que E[g(X, Y )] =
2. No es necesario conocer la distribuci´on marginal para calcular la media E[X] =
(cid:82) Y
(cid:82) X x · pXY (x, y)dxdy.
3. La linealidad sigue valiendo E[aX + bY + c] = a · E[X] + b · E[Y ] + c
5
Cap´ıtulo 1. Probabilidad y Estad´ıstica
4. La covarianza tambi´en puede simplificar su c´alculo como cov(X, Y ) = E[XY ] −
E[X] · E[Y ].
5. La varianza es un caso particular de la covarianza cov(X, X) = var(X)
6. La covarianza es sim´etrica cov(X, Y ) = cov(Y, X).
7. La covarianza es bilineal cov(aX + bY + c, αX + βY + γ) = a · α · var(X) + b ·
β · var(Y ) + (b · α + a · β) · cov(X, Y ).
8. La varianza de una suma puede calcularse utilizando la covarianza var(X+Y) =
var(X) + var(Y ) + 2 · cov(X, Y ).
9. El valor esperado de una variable truncada puede calcularse como E[g(X)|X ∈
A] =
E[g(X)·1{X∈A}] P(X∈A)
As´ı como la independencia factoriza las distribuciones, tambi´en factoriza las esperanzas. Pero la rec´ıproca no es v´alida. Es decir, si dos variables X e Y son independientes, luego E[g(X)h(Y )] = E[g(X)]E[h(Y )] y por lo tanto cov(X, Y ) = 0. Pero descorrelaci´on (covarianza nula) no implica independencia.
Los momentos caracterizan las vectores aleatorios. As´ı como la Prop. 1.4 demuestra que la constante que mejor aproxima a la variable aleatoria en t´erminos del error cuadr´atico medio es la media, la recta que mejor aproxima recibe el nombre de recta de regresi´on. La misma es definida a partir de los momentos como se muestra en el siguiente teorema.
Propiedades 1.6 E[(Y − (aX + b))2] ≥ var(Y ) − cov(X,Y )2 var(X)
con igualdad si y solo si
aX + b =
cov(X, Y ) var(X)
(X − E[X]) + E[Y ]
(1.9)
Demostraci´on 1.2 (Prop. 1.6) Para demostrarlo, notar que la funci´on a minimizar es
E[Y 2] + a2E[X 2] + b2 − 2aE[XY ] − 2bE[Y ] + 2abE[X]
(1.10)
Para buscar el m´ınimo, se puede igualar a cero las derivadas respecto de a y de b: 2aE[X 2] − 2E[XY ] + 2bE[X] = 2b − 2E[Y ] + 2aE[X] = 0
(1.11)
Luego b = E[Y ] − aE[X] y reemplazando
aE[X 2] − E[XY ] + E[X]E[Y ] − aE[X]2 = 0 → a =
cov(X, Y ) var(X)
(1.12)
para esos valores el error cuadr´atico medio es (cid:34)(cid:18) cov(X, Y ) var(X)
Y − E[Y ] −
E
(cid:19)2(cid:35)
(X − E[X])
6
Cap´ıtulo 1. Probabilidad y Estad´ıstica
= var(Y ) +
= var(Y ) −
cov(X, Y )2 var(X) cov(X, Y )2 var(X)
− 2
cov(X, Y )2 var(X)
(1.13)
(1.14)
Los momentos condicionales llevan al m´aximo el potencial de la esperanza. Sea φ(x) = E[Y |X = x] la media de la distribuci´on de Y |X=x (como funci´on de x) y E[Y |X] = φ(X) a la variable aleatoria construida evaluando a φ(x) en la variable aleatoria X. Algunas de las propiedades m´as importantes pueden verse a continuaci´on.
Propiedades 1.7 La esperanza y la varianza condicional poseen las siguientes propiedades.
1. E[Y ] = E[E[Y |X]]
2. E[Y g(X)] = E[E[Y |X]g(X)]
3. P(Y ∈ R) = E[P(Y ∈ R|X)]
4. var(Y ) = E[var(Y |X)] + var (E[Y |X])
La caracter´ıstica principal de la esperanza condicional es que es el mejor predictor a la
hora de estimar una variable aleatoria como puede verse en el siguiente teorema.
Propiedades 1.8 E[(Y − φ(X))2] ≥ E[var(Y |X)] con igualdad si y solo si φ(x) = E[Y |X = x].
Demostraci´on 1.3 (Prop. 1.8) La demostraci´on es sencilla: sumando y restando la esperanza condicional en la expresi´on a minimizar se observa que,
E[(Y − φ(X))2] = E[(Y − E[Y |X] + E[Y |X] − φ(X))2] (1.15) = E[(Y − E[Y |X])2] + E[(E[Y |X] − φ(X))2] + 2E[(Y − E[Y |X])(E[Y |X] − φ(X))] (1.16)
El primer sumando puede simplificando utilizando las propiedades de la esperanza condicional E[(Y − E[Y |X])2] = E[E[(Y − E[Y |X])2|X]] = E[var(Y |X)]. El segundo sumando simplemente se acota con E[(E[Y |X] − φ(X))2] ≥ 0 y la igualdad se da si y solo si φ(x) = E[Y |X = x]. El tercer sumando se anula usando las propiedades de la esperanza condicional E[(Y − E[Y |X])(E[Y |X] − φ(X))] = E[E[Y − E[Y |X]|X](E[Y |X] − φ(X))] = 0. Juntando los tres t´erminos el teore-
7
Cap´ıtulo 1. Probabilidad y Estad´ıstica
ma es probado: E[(Y − φ(X))2] ≥ E[var(Y |X)] con igualdad se da si y solo si φ(x) = E[Y |X = x].
Las propiedades 1.4, 1.6 y 1.8 son esenciales conceptualmente para la inteligencia arti-
ficial. Los resultados de estos teoremas implican que:
En t´erminos del error cuadr´atico medio, el mejor predictor es la esperanza condicional. Si nos restringimos a las rectas, el predictor ´optimo es la recta de regresi´on. Si en cambio buscamos un predictor constante, la mejor opci´on es la esperanza.
Si la esperanza condicional es una recta, necesariamente debe coincidir con la recta de regresi´on. Si la recta de regresi´on es una constante debe coincidir con la esperanza E[Y ].
En ning´un caso, el error cuadr´atico medio puede ser inferior a E[var(Y |X)]. Esto lo convierte en un l´ımite fundamental.
A continuaci´on se presentar´a un ejemplo de c´omputo de este tipo de magnitudes.
Ejemplo 1.2 En el mercado de smartphones, los dispositivos con mayor capacidad de almacenamiento suelen tener bater´ıas m´as duraderas. Modelar estos datos podr´ıa ayudar a estimar la duraci´on de la bater´ıa en funci´on de su capacidad de almacenamiento, algo ´util para los consumidores a la hora de elegir un nuevo dispositivo. Sea X la capacidad de almacenamiento de los smartphones (en TB) e Y la duraci´on de su bater´ıa (en d´ıas), con densidad de probabilidad conjunta de la forma:
pXY (x, y) =
· 1 (cid:8)0 < y < 1 + x2, 0 < x < 1(cid:9)
(1.17)
3 4
Calcular la duraci´on media de las bater´ıas, la recta de regresi´on y la esperanza condicional. Indicar cu´al es el error cuadr´atico medio asociado a cada aproximaci´on.
Lo primero a determinar es la factorizaci´on de la distribuci´on en la condicional Y |X = x (para caracterizar el comportamiento de Y como funci´on de x) y la marginal X (para medir correctamente cuanto se penalizan los errores). Al igual que en el Ej. 1.1, se separar´a todos los factores donde aparezca y y se completar´a la densidad para que integre 1 (utilizando la lista de distribuciones conocidas del Cuadro 1.2).
pXY (x, y) =
1
1 + x2 1 (cid:8)0 < y < 1 + x2(cid:9)
(cid:124)
(cid:123)(cid:122) pY |X=x(y)
·
3(1 + x2) 4
(cid:124)
1 {0 < x < 1} (cid:123)(cid:122) (cid:125) pX (x)
(1.18)
(cid:125)
donde puede verse Y |X=x ∼ U(0, 1 + x2) y X es una variable aleatoria continua con densidad bien determinada, pero sin ser ninguna de las mencionadas en el Cuadro 1.2. La esperanza y varianza condicional pueden observarse en el mencionado cuadro y determinar
8
Cap´ıtulo 1. Probabilidad y Estad´ıstica
que E[Y |X = x] = 1+x2 2 calcular todos los momentos asociados al problema.
y var(Y |X = x) = (1+x2)2
12
. El resto del problema es simplemente
(cid:90) 1
E[X k] =
Los momentos de X pueden obtenerse simplemente integrando polinomios xk 3(1 + x2) 4 de esta manera E[X] = 9 16, E[X 2] = 2 entonces var(X) = E[X 2] − E[X]2 = 107 las propiedades de la esperanza condicional.
5, E[X 3] = 5 35. La varianza ser´a 1280. La media de Y se pueden calcular utilizando
k + 1 16 y E[X 4] = 9
1 k + 3
(cid:18) 1
(1.19)
dx =
3 4
+
(cid:19)
0
E[Y ] = E[E[Y |X]] =
1 + E[X 2] 2
=
7 10
(1.20)
Para el caso de la varianza, puede hacerse el mismo tipo de an´alisis con var(Y ) =
E[var(Y |X)] + var (E[Y |X]). En este caso
E[var(Y |X)] =
var (E[Y |X]) =
1 + 2E[X 2] + E[X 4] 12
=
6 35 E[X 4] − E[X 2]2 4
var(X 2) 4
=
=
17 700
(1.21)
(1.22)
y por lo tanto var(Y ) = 137 700.
Por el lado de la covarianza cov(X, Y ) = E[XY ]−E[X]E[Y ], resta calcular la esperanza
del producto. La misma puede resolverse utilizando las Prop. 1.7. 3 E[XY ] = E[XE[Y |X]] = 16
E[X] + E[X 3] 2
=
(1.23)
y por lo tanto cov(X, Y ) = 7 analizar las diferentes aproximaciones en t´erminos del error cuadr´atico medio.
160. Finalmente utilicemos los resultados 1.4, 1.6 y 1.8, para
La constante que mejor aproxima a Y es su media E[Y ] = 7 medio es var(Y ) = 137
700 ≈ 0.196.
10, y el error cuadr´atico
La recta que mejor aproxima a Y es la recta de regresi´on cov(X,Y ) 56 107x + 217
535, y el error cuadr´atico medio es var(Y ) − cov(X,Y )2
var(X) (x − E[X])+E[Y ] = 18725 ≈ 0.173.
var(X) = 3236
La funci´on que mejor aproxima a Y es la asociada a la esperanza condicional E[Y |X = x] = 1+x2 2
, y el error cuadr´atico medio es E[var(Y |X)] = 6
35 ≈ 0.171.

## 1.2. Estad´ıstica

En la mayor´ıa de las aplicaciones, rara vez se conoce la distribuci´on exacta de las variables aleatorias. La estad´ıstica soluciona este inconveniente por medio de datos. Si bien el aprendizaje estad´ıstico busca reconocer patrones por medio de ejemplos, su an´alisis no debe reducirse al conjunto de datos con los que cuenta sino que dichos patrones deben poder generalizarse a nuevas muestras. En ese sentido, la inteligencia artificial es solamente
9
Cap´ıtulo 1. Probabilidad y Estad´ıstica
Figura 1.1: Ejemplo de funci´on de masa de probabilidad emp´ırica.
una gran m´aquina de estad´ıstica con suficiente automatizaci´on, c´alculo computacional y un poco de marketing. Pero no nos pisemos la manguera entre bomberos.

### 1.2.1. Distribuci´on Emp´ırica e Histograma

La primera pregunta que analizaremos en esta secci´on es como aproximar una distribuci´on por medio de datos. Uno de los m´etodos m´as simples para efectuar dicha aproximaci´on se conoce como distribuci´on emp´ırica [2, Cap´ıtulo 11]. La distribuci´on emp´ırica asume una distribuci´on discreta, donde la probabilidad de cada ´atomo corresponde a su frecuencia de aparici´on ˆP (x) = K n donde n es la cantidad de muestras totales, K la cantidad de muestras con valor x. Un ejemplo de funci´on de masa de probabilidad emp´ırica puede verse en la Fig. 1.1. Su funci´on de distribuci´on asociada ser´a entonces del tipo escalera.
Otro enfoque para enfrentar esta problem´atica es la estimaci´on de densidad por t´ecnicas no param´etricas [3, Cap´ıtulo 4], siendo el histograma su variante m´as sencilla. El histograma modela la variable como continua y asume una densidad constante por regiones. En cada regi´on asigna ˆp(x) = K n·V donde n es la cantidad de muestras totales, K la cantidad de muestras en dicha regi´on y V el volumen de la regi´on (en el caso escalar el ancho del intervalo). Este m´etodo garantiza que la probabilidad de cada regi´on sea proporcional a la cantidad de muestras que pertenecen a ella. Un ejemplo de funci´on histograma puede verse en la Fig. 1.2.
10
Cap´ıtulo 1. Probabilidad y Estad´ıstica
Figura 1.2: Ejemplo de funci´on histograma (densidad de probabilidad).

### 1.2.2. Simulaci´on

La generaci´on de datos sint´eticos es una parte esencial de la estad´ıstica. Ya sea para validar los modelos utilizados o para generar nueva informaci´on sobre una tarea, la simulaci´on de datos es un ´area sumamente importante en la tem´atica. En la pr´actica, cualquier software af´ın suele tener desarrollados algunos algoritmos generadores de n´umeros pseudoaleatorios, pero es razonable que no cuente con todas las distribuciones necesarias que el usuario necesite. El ejemplo m´as simple es la U(0, 1), que cualquier calculadora cient´ıfica puede simular. A partir de esos algoritmos, es necesario poder transformar las variables aleatorias generadas para que tengan cualquier distribuci´on deseada. El siguiente teorema muestra algunos de los resultados m´as importantes en el tema.
Propiedades 1.9 Para encontrar una transformaci´on que satisfaga una determinada distribuci´on pueden utilizarse los siguientes resultados
1. Sea U ∼ U(0, 1), luego la variable aleatoria Y = F −1
Y (U ) posee funci´on de
distribuci´on FY , donde F −1
es la inversa generalizada:
Y Y (u) = m´ın{y ∈ R : u ≤ FY (y)} F −1
(1.24)
2. Toda variable aleatoria X, con funci´on distribuci´on estrictamente creciente en un intervalo, evaluada en su propia funci´on de distribuci´on U = FX(X) posee distribuci´on uniforme U ∼ U(0, 1).
3. Sea X una variable aleatoria con funci´on de distribuci´on estrictamente creY (FX(X)) posee funci´on de distribuci´on
ciente en un intervalo, luego Y = F −1
11
Cap´ıtulo 1. Probabilidad y Estad´ıstica
FY .
La primera propiedad indica como poder transformar variables U(0, 1) en variables con cualquier distribuci´on que se necesite, la segunda explica como poder transformar variables con una determinada distribuci´on en U(0, 1), y la tercera combina los dos resultados anteriores.
En el caso de vectores, si se desea simular un vector aleatorio (X, Y ) ∼ pXY basta con generar una muestra de X ∼ pX, para luego usar dicho valor observado x para generar Y |X = x ∼ pY |X=x. En el Ej. 1.1, primero se generar´ıan muestras X ∼ Γ(2, 1) para luego generar muestras Y |X=x ∼ U(0, x) (una y para cada x).
Para simular una variable truncada X|X ∈ A, basta con generar datos de X ∼ pX, para luego usar solamente con los que cumplen x ∈ A (descartando el resto). Para simular un vector truncado (X, Y )|(X, Y ) ∈ A, basta con generar datos de X ∼ pX, generar sus correspondientes Y |X = x ∼ pY |X=x y luego quedarme con los pares (x, y) ∈ A.

### 1.2.3. Estad´ıstica Frecuentista

El objetivo de reconocer y estimar toda la distribuci´on de una variable aleatoria por medio de datos es sumamente ambicioso. En la mayor´ıa de los casos no se cuenta con una cantidad de datos suficiente para tal objetivo. Es entonces cuando surge la necesidad de incorporar supuestos previos sobre las variables involucradas, modelando el problema estad´ıstico. No es necesario que dichos supuestos sean totalmente ciertos, sino que basta con que balanceen el desempe˜no esperado, la complejidad del modelo y la cantidad de datos con las que se cuentan.
El modelado consiste en asumir informaci´on parcial en el conocimiento de la distribuci´on de la variable p(x|θ) [4]. Es decir que se conoce dicha distribuci´on exceptuando un conjunto de par´ametros θ ∈ Θ. La estad´ıstica frecuentista asume que las muestras son independientes e id´enticamente distribuidas para cada posible par´ametro, y a la distribuci´on conjunta del set de datos observados x = (x1, · · · , xn) se la conoce como verosimilitud:
L(θ) = p(x|θ) =
p(xi|θ)
(1.25)
n (cid:89)
La bondad de un estimador est´a dada por la relaci´on de compromiso sesgo/varianza,
i=1
como se puede ver en el siguiente teorema.
Propiedades 1.10 E[(ˆθ − θ)2|θ] = var(ˆθ|θ) + B2(θ), donde B(θ) = θ − E[ˆθ|θ] se denomina sesgo.
La demostraci´on puede verse al final de la secci´on. La relaci´on de compromiso sesgo/varianza explica que un buen estimador necesita tener simult´aneamente bajo sesgo y
12
Cap´ıtulo 1. Probabilidad y Estad´ıstica
baja varianza. Se habla de relaci´on de compromiso porque muchas de las soluciones m´as utilizadas para mejorar uno de los t´erminos termina perjudicando al otro.
Uno de los estimadores puntuales m´as utilizados en la estad´ıstica frecuentista, debido L(θ), es
a su consistencia, es el estimador de m´axima verosimilitud ˆθMV = arg max
θ∈Θ
decir elegir los par´ametros que maximicen la verosimilitud (los estimadores son funciones de la muestra observada). Bajo ciertas condiciones de regularidad dicha estimaci´on puede efectuarse igualando a cero la derivada del logaritmo5 de la verosimiltud: ∂ ∂θ
log p(xi|ˆθMV) = 0
(1.26)
n (cid:88)
i=1
donde log(·) hace referencia al logaritmo natural. Una vez caracterizados los par´ametros, el modelo es capaz de predecir el comportamiento de nuevas muestras no observadas. Sea xtest una muestra no observada en x, las predicciones se efectuan a trav´es del principio de invarianza: la estimaci´on por m´axima verosimilitud de cualquier funci´on de θ puede calcularse evaluando dicha funci´on en ˆθMV [5].
(cid:98)pMV(xtest) = p(xtest|ˆθMV)
(1.27)
Demostraci´on 1.4 (Prop. 1.10) El error cuadr´atico medio puede descomponerse como:
E[(ˆθ − θ)2|θ] = E[(ˆθ − E[ˆθ|θ] + E[ˆθ|θ] − θ)2|θ]
= E[(ˆθ − E[ˆθ|θ])2|θ] + (E[ˆθ|θ] − θ)2 + 2E[(ˆθ − E[ˆθ|θ])|θ](E[ˆθ|θ] − θ)
(1.28)
(1.29)
donde cada uno de los sumandos se puede simplificar como:
E[(ˆθ − E[ˆθ|θ])2|θ] = var(ˆθ|θ)
(E[ˆθ|θ] − θ)2 = B2(θ)
E[(ˆθ − E[ˆθ|θ])|θ](E[ˆθ|θ] − θ) = 0
Reemplazando en la expresi´on correspondiente el teorema fue demostrado.

### 1.2.4. Estad´ıstica Bayesiana

La estad´ıstica bayesiana busca verdades en contexto de incertidumbre, interpretando la probabilidad como una medida de credibilidad en un evento [6, Cap´ıtulo 1]. El modelo no solo representa el fen´omeno a predecir, sino tambi´en nuestra propia ignorancia sobre el mismo. Esto no quiere decir que las ciencias emp´ıricas est´an condenadas a decir “no se” a todas las hip´otesis que uno desea contrastar, sino que busca evitar mentir maximizando incertidumbre (no afirmar m´as de lo que se sabe) dada la informaci´on disponible (sin
5Por ser una funci´on mon´otona, no modifica la ubicaci´on de los m´aximos.
13
Cap´ıtulo 1. Probabilidad y Estad´ıstica
ocultar lo que efectivamente se sabe).
A nivel t´ecnico, la estad´ıstica bayesiana representa los par´ametros del modelo por medio de una variable aleatoria T con distribuci´on a priori pT (θ) [7]. En este tipo de modelos, la hip´otesis de independencia es v´alida cuando se conoce el par´ametro. Es decir que la verosimilitud de una muestra puede escribirse como pX|T =θ(x) = (cid:81)n i=1 pX|T =θ(xi). No se pierde generalidad en asumir que las variables son id´enticamente distribuidas6.
El coraz´on de la estad´ıstica bayesiana es la distribuci´on a posteriori, la cu´al se deduce por medio de la regla de bayes combinando la distribuci´on a priori con la verosimilitud.
pT |X=x(θ) ∝ pT (θ) ·
pX|T =θ(xi)
(1.30)
n (cid:89)
i=1
La distribuci´on a posteriori nos permite definir estimadores puntuales a partir de ella. En el caso de buscar par´ametros dentro de un conjunto Θ discreto, se suele elegir como estimador el m´aximo a posteriori ˆθMAP = arg max pT |X=x(θ). En el caso de Θ continuo, la elecci´on habitual suele ser la media a posteriori ˆθBAY = E[T |X = x].
θ∈Θ
Sin embargo, el verdadero potencial de la estad´ıstica bayesiana radica en hacer predicciones sin necesidad de estimadores puntuales. En este sentido, este tipo de estad´ıstica no solo puede resolver los mismos problemas que la frecuentista, sino que tambi´en pueden intentar resolver problemas donde la estad´ıstica cl´asica es insuficiente o iluminar el sistema subyacente con un modelado m´as flexible. Es entonces que se define la distribuci´on predictiva.
pXtest|X=x(xtest) =
pX|T =θ(xtest)pT |X=x(θ)dθ
(1.31)
donde Xtest es una variable aleatoria no vista en el conjunto de entrenamiento X. A continuaci´on se analizar´a un ejemplo mostrando como trabajar con este tipo de estad´ıstica anal´ıticamente.
Θ
Ejemplo 1.3 El tiempo de vida (en a˜nos) de un transistor es una variable aleatoria con distribuci´on exponencial de par´ametro θ. A priori se modela θ como una variable aleatoria con distribuci´on Γ(2, 3). Si en 20 transistores se observ´o una duraci´on total (cid:80)20
i=1 xi = 7.
1. Hallar la distribuci´on a posteriori del par´ametro θ.
2. Hallar la distribuci´on predictiva del tiempo de vida de un transistor.
Como primer paso en un problema bayesiano, hay que comenzar planteando la distribuci´on
6Se podr´ıa haber escrito pXi|T =θ(xi) en su lugar, pero no es necesario
14
(cid:90)
(cid:90)
Θ
(cid:90) ∞
Cap´ıtulo 1. Probabilidad y Estad´ıstica
a posteriori. En este caso evitaremos las constantes de proporcionalidad:
pT |X=x(θ) ∝ pT (θ) ·
n (cid:89)
i=1
pX|T =θ(xi) ∝ θe−3θ1{θ > 0} ·
20 (cid:89)
i=1
θe−θxi = θ21e−10θ1{θ > 0} (1.32)
Es decir, la variable se distribuye a posteriori como T |X=x ∼ Γ(22, 10). La distribuci´on
predictiva es de la forma
pXtest|X=x(xtest) =
pX|T =θ(xtest)pT |X=x(θ)dθ ∝
(cid:90) ∞
θe−θxtest1{xtest > 0} · θ21e−10θdθ
0
(1.33) Reconociendo el n´ucleo de la integral, se puede observar que el mismo es proporcional Γ(ν) xν−1e−λx1{x > 0}. Sabiendo que por ser
a la densidad de una Γ(ν, λ), es decir p(x) = λν densidad debe integrar 1:
1
pXtest|X=x(xtest) ∝
θ22e−θ(10+xtest)dθ · 1{xtest > 0} ∝
(10 + xtest)23 1{xtest > 0} (1.34) donde se utiliz´o ν = 23 y λ = 10+xtest. Esta distribuci´on se la conoce como Lomax (v´ease Cuadro 1.2) Xtest|X=x ∼ Lomax(22, 10).
0
Tanto a priori como a posteriori, la variable T es una Gamma. Este fen´omeno de mantenerse dentro de una familia ocurre por cierta compatibilidad entre la distribuci´on a priori y la verosimilitud (en este caso una exponencial, caso particular de la Gamma). Cuando se da este fen´omeno se dice que la distribuci´on a priori es una conjugada a priori. Las soluciones anal´ıticas suelen proponer conjugadas, como distribuci´on a priori, ya que as´ı garantizan que la distribuci´on a posteriori pertenezca a una familia conocida (la misma que la distribuci´on a priori ). Es simplemente una recomendaci´on para hacer sencillos (o al menos factibles) los c´alculos.
1.2.4.1. Estad´ısticos Suficientes
Un concepto muy ´util a la hora de efectuar inferencia es el de estad´ıstico suficiente. Un estad´ıstico S(X) se denomina suficiente para θ si la distribuci´on de X|S(X)=s no depende de θ. Es decir que toda la informaci´on que posee la muestra sobre θ se encuentra en el estad´ıstico. Adem´as, el teorema de Neyman-Fisher nos permite encontrar estad´ısticos suficientes de forma muy sencilla [4, Cap´ıtulo 6].
Propiedades 1.11 (Teorema de Neyman-Fisher) El estad´ıstico S(X) es suficiente, si y solo si su verosimilitud se puede descomponer como:
pX|T =θ(x) = g(θ, S(x)) · h(x)
(1.35)
En t´erminos bayesianos un estad´ıstico suficiente se interpreta como una independencia condicional X ⊥ θ|S(X)=s (es decir que la muestra y los par´ametros son independientes cuando se conoce el estad´ıstico suficiente). Este resultado implica que la distribuci´on a posteriori debe cumplir pT |X=x(θ) = pT |S(X)=s(x)(θ), y por lo tanto nos permite intercambiar
15
Cap´ıtulo 1. Probabilidad y Estad´ıstica
el conocimiento de toda la muestra por el del estad´ıstico suficiente. En el ejemplo anterior la distribuci´on solo depend´ıa de la muestra a trav´es de la suma, estad´ıstico suficiente para θ en una distribuci´on exponencial.
Esto nos permite hacer equivalencias sobre los datos de las variables observadas. En el Ej. 1.3, es equivalente pensar que se cuenta con 20 muestras exp(θ) que con una sola muestra Γ(20, θ)7. Otro ejemplo cl´asico donde se da este fen´omeno es en las variables Bernoulli, donde tambi´en la suma es estad´ıstico suficiente: es equivalente tener n muestras Ber(p) que una muestra Bin(n, p).
1.2.4.2. Test de hip´otesis
TODO
7La suma de 20 variables exp(θ) independientes e id´enticamente distribuidas se distribuye como una
Γ(20, θ)
16

# 2


# Regresi´on en Inteligencia Artificial

Tal vez el mayor desaf´ıo no sea aprender a usar la inteligencia artificial, sino redefinir nuestro aporte humano en un mundo que automatiza incluso la inteligencia.
El objetivo de la inteligencia artificial es resolver tareas de forma automatizada y con la mejor calidad posible. ´Esta tecnolog´ıa est´a modificando de forma acelerada la matriz laboral tal como la conoc´ıamos. Tareas que antes requer´ıan horas de redacci´on, an´alisis o asistencia t´ecnica ahora pueden ser resueltas en minutos por una inteligencia artificial entrenada para comprender y generar material con una sorprendente fluidez. Esta transformaci´on no se limita a sectores creativos o administrativos; tambi´en est´a empezando a influir en el desarrollo de software, la ingenier´ıa de datos y la automatizaci´on de procesos, ´areas donde muchos ingenieros se formaron creyendo que la demanda ser´ıa estable o creciente.
Esto plantea una pregunta inc´omoda pero necesaria: ¿qu´e lugar ocuparemos los profesionales en un entorno donde las m´aquinas no solo ejecutan, sino tambi´en piensan -al menos en t´erminos funcionales-? El rol del ingeniero ya no se limita a dise˜nar sistemas eficientes, sino que debe integrar consideraciones ´eticas, adaptarse a herramientas inteligentes y desarrollar una visi´on cr´ıtica sobre la tecnolog´ıa que crea. Tal vez el mayor desaf´ıo no sea aprender a usar estos modelos, sino redefinir nuestro aporte humano en un mundo que automatiza incluso la inteligencia.
En cualquier problema de aprendizaje supervisado, es decir inferir la etiqueta Y a partir del predictor X 1, siempre hay algunas magnitudes que se pueden destacar. El objetivo siempre ser´a minimizar el valor esperado de la llamada funci´on costo ℓ(x, y), el cu´al recibe el nombre de riesgo esperado E[ℓ(X, Y )]. La estimaci´on que minimice dicho riesgo se conocer´a como soluci´on ´optima y llamaremos error bayesiano al m´ınimo error posible capaz de ser alcanzado (asociado a la soluci´on ´optima). Estamos hablando de un l´ımite fundamental para el error que nunca podr´a ser mejorado independientemente de la tecnolog´ıa utilizada.
En particular, en este cap´ıtulo estudiaremos el problema de regresi´on, es decir esti-
1V´ease el Cap´ıtulo 4 para detalles precisos sobre el t´ermino.
17
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
mar Y = φ(X) utilizando el error cuadr´atico como funci´on costo ℓ(x, y) = (y − φ(x))2 (y por lo tanto el error cuadr´atico medio como riesgo esperado). En el cap´ıtulo anterior se demostr´o, Prop. 1.8, que la regresi´on ´optima es E[Y |X = x] y con ´esta el error alcanza el error bayesiano E[var(Y |X)]. Todo este resultado es la base del aprendizaje estad´ıstico: lo mejor que puedo hacer es utilizar la esperanza condicional como regresor y el menor error al que puedo aspirar es el bayesiano.
La inteligencia artificial lejos est´a de terminarse con este resultado. En la pr´actica, el problema radica en no conocer la distribuci´on de los datos, y por lo tanto no poder calcular fidedignamente la esperanza condicional. El aprendizaje estad´ıstico propone entonces aprender la esperanza condicional por medio de datos.

## 2.1. Relaci´on de Compromiso Sesgo/Varianza


    
(cid:124)
(cid:80)ntr
i=1 ℓ(xi, yi) para un conjunto de datos observado {(xi, yi)}ntr
La soluci´on inmediata que uno puede proponer al problema de regresi´on es la minimizaci´on del riesgo emp´ırico. Es decir, encontrar la funci´on φ(x) que minimice 1 i=1. El problema est´a en ntr que el verdadero objetivo es minimizar el riesgo esperado E[ℓ(X, Y )] que no necesariamente va a coincidir con el emp´ırico. En este sentido surge el gap de generalizaci´on: la capacidad de generalizar el comportamiento de los datos observados a datos desconocidos (representados por los valores esperados).

E[ℓ(X, Y )] (cid:125) (cid:123)(cid:122) (cid:124) Riesgo esperado
=
1 ntr (cid:124)
ntr(cid:88)
ℓ(xi, yi)
+
i=1
(cid:123)(cid:122) Riesgo emp´ırico
(cid:125)
E[ℓ(X, Y )] −
ntr(cid:88)
1 ntr (cid:123)(cid:122) Gap de generalizaci´on
i=1
ℓ(xi, yi)
    
(2.1)
(cid:125)
En este sentido, para disminuir el riesgo esperado se necesita simult´aneamente tratar de minimizar el riesgo emp´ırico y el gap de generalizaci´on; dos magnitudes de caracter´ısticas muy distinta [8, Secci´on 2.9]. Este problema es an´alogo al estimador param´etrico puntual estudiado en la Prop. 1.10: es una relaci´on de compromiso entre el sesgo (representado por el riesgo emp´ırico) y la varianza (representado por el gap).
Cuando hablamos de errores cuadr´aticos, hay que tener en consideraci´on que este tipo de error es una magnitud dif´ıcil de interpretar por no tener valor m´aximo. Si bien tener un error nulo implica desempe˜no perfecto, otro valor de error requiere contextualizarlo para catalogarlo como insuficiente o satisfactorio. En este sentido, el gap de generalizaci´on propone un marco interpretativo al ser una diferencia: ¿Que tanto m´as grande es el riesgo esperado con respecto al emp´ırico? En cambio el riesgo emp´ırico por si solo no es interpretable. Para darle un sentido se lo compara con el error bayesiano, ya que este es el error al que todo algoritmo desea alcanzar. En la pr´actica el error bayesiano suele ser
18
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
y
1
y
1
y
1
2
x
1
(a)
(cid:136)
(cid:136)
(cid:136)
1
(cid:136) (cid:136)
(b)
2
x
2
x
1
(c)
Figura 2.1: Regresores para el Ej. 2.1. (a) Soluci´on E[Y |X = x] asociada a la esperanza condicional, (b) soluci´on emp´ırica y (c) recta de regresi´on.
livianamente estimado con imaginaci´on: ¿Que error creo que se puede llegar a alcanzar en esta tarea? En muchos casos, el error humano es buen candidato.
A continuaci´on se analizar´a un ejemplo para entender las diferencias entre los riesgos
emp´ırico y esperado.
Ejemplo 2.1 Sea (X, Y ) un vector uniforme en el tri´angulo de v´ertices (0, 0), (1, 1) y (2, 0). Analizar posibles regresores para este problema.
Comencemos analizando la soluci´on ´optima. Al factorizar la distribuci´on conjunta uni-
forme, se observa una condicional uniforme (v´ease Ej. 1.2). En este caso,  
Si 0 < x < 1
U(0, x)
Y |X = x ∼
(2.2)

U(0, 2 − x) Si 1 < x < 2
y por lo tanto, soluci´on E[Y |X = x] asociada a la esperanza condicional puede verse gr´aficamente en la Fig. 2.1a. Anal´ıticamente, tanto la esperanza como la varianza condicional se definen a partir del Cuadro 1.2:  
Si 0 < x < 1
Si 0 < x < 1
 
x2 12
x 2
var(Y |X = x) =
(2.3)
E[Y |X = x] =

2−x 2
Si 1 < x < 2

(2−x)2 12
Si 1 < x < 2
En este caso el error bayesiano se puede calcular utilizando que el tri´angulo tiene ´area
unitaria:
E[var(Y |X)] =
(cid:90) 1
(cid:90) x
0
0
x2 12
dydx +
(cid:90) 2
(cid:90) 2−x
1
0
(2 − x)2 12
dydx =
1 24
(2.4)
Esas son la soluci´on ideal y el m´ınimo error esperado al que se puede aspirar. Sin embargo, dado un conjunto de datos {(xi, yi)}ntr i=1, cuando se elige una soluci´on minimizando el riesgo emp´ırico se encuentran regresores como el visto en la Fig. 2.1b. Esta soluci´on no solo minimiza 1 i=1 ℓ(xi, yi) sino que directamente alcanza error nulo. Sin embargo, ntr
(cid:80)ntr
19
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
o g s e i R
Esperado
Gap
Emp´ırico
Complejidad
Figura 2.2: Relaci´on de compromiso sesgo/varianza t´ıpica seg´un la teor´ıa cl´asica de generalizaci´on.
soluciones de este tipo suelen poseer un algo gap de generalizaci´on debido a un exceso de complejidad en el modelado, es decir un problema de varianza. En este caso, al darle libertad total a la elecci´on del regresor, se eligi´o un regresor mucho m´as complejo que el ´optimo E[Y |X = x]. Las soluciones que poseen un excesivo problema de varianza se dice que tienen overfitting, ya que ´estas se sobreajustan a los datos. Se suele interpretar este tipo de soluciones como algoritmos que memorizan en lugar de aprender.
En cambio, si uno asigna una complejidad excesivamente baja al regresor se encuentra con un problema de sesgo. En la Fig. 2.1c se postula la recta de regresi´on como posible regresor con este tipo de problema. Dentro de los regresores de complejidad lineal, la recta de regresi´on es el ´optimo (v´ease Prop 1.6). Posiblemente esta soluci´on tenga un muy bajo gap de generalizaci´on (ni siquiera se calcul´o utilizando los datos), sin embargo al tener una complejidad mucho m´as baja que la soluci´on ´optima, el riesgo emp´ırico ser´a importante. Las soluciones que poseen un excesivo problema de sesgo se dice que tienen underfitting, ya que ´estas se subajustan a los datos.
La Fig. 2.2 muestra como la teor´ıa cl´asica de generalizaci´on caracteriza esta relaci´on de compromiso. Los modelos de muy baja complejidad ven imposibilitado cualquier tipo de sobreajuste y tratar´an de forma similar los datos conocidos a los desconocidos (alcanzando un bajo gap de generalizaci´on). En contraposici´on, los modelos muy complejos pueden reducir el riesgo emp´ırico tanto como quieren pero corren el riesgo de sobreajustar. Encontrar el balance ´optimo, lejos de ser trivial, es problema principal de la inteligencia artificial.
La cantidad de datos con la que se cuenta juega un rol vital en este an´alisis. Si se
20
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
cuenta con la posibilidad de obtener m´as y m´as datos llegar´a un momento en que un modelo, de una complejidad determinada, no podr´a sobreajustarlos. Bajo ciertas hip´otesis de consistencia, el gap de generalizaci´on deber´a disminuir con el n´umero de muestras (en la medida que los promedios tiendan a los valores esperados en (2.1))2. En este sentido, aumentar la cantidad de datos soluciona problemas de varianza, pero no as´ı de sesgo (al tener m´as muestras, es m´as dif´ıcil representarlas a todas con una complejidad fija). En cualquier caso, se deber´a adaptar la complejidad del modelo a la cantidad de datos con las que se cuenta, pudiendo permitirse modelos m´as complejos cuando se cuenta con grandes cantidades de datos y limitando la misma cuando la cantidad es escueta.

## 2.2. Regresi´on Lineal

El objetivo del aprendizaje estad´ıstico es intentar disminuir simult´aneamente el riesgo emp´ırico y el gap de generalizaci´on para as´ı reducir el riesgo esperado (2.1). Pero mientras que el gap de generalizaci´on no se conoce, el riesgo emp´ırico es totalmente computable y por lo tanto podemos detectar f´acilmente cuando estamos en presencia de un problema de sesgo. La idea de la regresi´on lineal es muy sencilla: limitar al m´aximo la complejidad del modelo (soluciones lineales) para tener un gap de generalizaci´on moderado (evitar problemas de varianza) y posteriormente verificar si hay problema de sesgo. En caso de que no los haya podemos concluir que tenemos un aceptable riesgo esperado. En este sentido, la regresi´on lineal busca aprender la recta de regresi´on3 (v´ease Prop. 1.6) en lugar de la esperanza condicional, b´asicamente porque es una tarea mucho m´as sencilla4. i=1 un conjunto de datos con xi ∈ Rdx e yi ∈ R. Se propone buscar soluciones de la forma ˆy(x) = wT x+b con w ∈ Rdx y b ∈ R minimizando el riesgo emp´ırico. Es decir, un algoritmo de inteligencia artificial tiene dos etapas bien diferenciadas: una primera llamada entrenamiento donde se calcular´an los par´ametros (w y b en este caso) y una segunda etapa llamada predicci´on donde a cada x se le asignar´a un ˆy(x) (en este caso ˆy(x) = wT x + b). En el caso de la regresi´on lineal, el entrenamiento entonces buscar´a calcular
Sea {(xi, yi)}ntr
(w, b) = arg min w∈Rdx ,b∈R
ntr(cid:88)
1 ntr
(wT · xi + b − yi)2
(2.5)
i=1 Esta ecuaci´on define un problema de proyecci´on ortogonal de ´algebra lineal. Esto se puede analizar vectorizando la ecuaci´on. Definiendo X ∈ Rntr×(dx+1), y ∈ Rntr y w ∈
2Dado que el regresor elegido depende del mismo conjunto de datos con el que se mide el riesgo emp´ırico, el an´alisis es sofisticado (la ley de los grandes n´umeros no es suficiente para explicar el fen´omeno). Para m´as informaci´on ver [7, Secci´on 6.5]
3Para predictores unidimensionales es una recta, en general son hiperplanos. 4Ser´a una recta si X es escalar, un plano si tiene dos dimensiones, etc. En general ser´a un hiperplano.
21
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
Rdx+1 como




,
y =
X =
   
   
1 xT 1 1 xT 2 ... ... 1 xT ntr el problema (2.5) puede reducirse a minimizar J(w) = 1 ∥Xw − y∥2. Para ello basta con ntr analizar la primera derivada (gradiente) y la segunda derivada (matriz Hessiana) respecto a w (para m´as informaci´on sobre derivadas respecto vectores/matrices ver [9]). XT (Xw − y),
y1 y2 ... yntr
∇J(w) =
XT X
   
   
(2.6)
(2.7)
w =
b w
HJ (w) =
(cid:32)
(cid:33)
,
2 ntr
2 ntr
Es habitual en los problemas de regresi´on que ntr ≫ dx, lo cu´al se suele traducir en una matriz Hessiana inversible (teniendo en cuenta que los x fueron elegidos de forma aleatoria). En ese caso, ser´a tambi´en una matriz definida positiva y por lo tanto el problema ser´a convexo. Es decir que el resultado obtenido de igualar a cero el gradiente de J(w) ser´a efectivamente un m´ınimo. Se puede despejar entonces para encontrar el procedimiento del entrenamiento:
w = (XT X)−1XT y
(2.8)
La soluci´on es la pseudoinversa de la matriz X multiplicada por y. A continuaci´on
se presenter´a un ejemplo de como funciona la regresi´on lineal.
Ejemplo 2.2 Se desea hacer una regresi´on lineal (sin normalizar) sobre el siguiente conjunto de datos:
x
y
0.2
1.4
-1.4
-0.2
20.0
10.0
10.0
0.0
Hallar los par´ametros del modelo.
Predecir y para x = 0.1.
Basta con definir las matrices de (2.8):
(cid:32)
XT X =
1
1 0.2 1.4 −1.4 −0.2
1
1
(cid:33)

   
1 0.2 1.4 1 1 −1.4 1 −0.2 
(cid:33)−1 (cid:32)
w =
(cid:32)
4 0 0 4
1
1 0.2 1.4 −1.4 −0.2
1
1
(cid:33)
   

   
20 10 10 0
=

   
(cid:33)
(cid:32)
4 0 0 4
(cid:33)
(cid:32)
=
10 1
(2.9)
(2.10)
con lo cual b = 10 y w = 1; y finalmente ˆy(0.1) = 10.1.
22
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial

### 2.2.1. Codificaci´on de variables categ´oricas

La regresi´on lineal, as´ı como la mayor parte de los algoritmo de inteligencia artificial, requieren que los valores de sus entradas tengan valores num´ericos. Pero hay determinados tipos de variables, donde no es posible encontrar una relaci´on de orden, donde las mismas simplemente representa categor´ıas (con una cantidad finita de opciones posibles)5. Por ejemplo, podemos contar con una base de datos donde una de sus columnas represente el color de un objeto. Supongamos que los resultados posibles son rojo, verde, azul y negro. Si asignamos respectivamente los valores 0, 1, 2 y 3 estar´ıamos diciendo que el rojo est´a mas cerca del verde que del negro, lo cu´al sesgar´ıa nuestro an´alisis por ser falso. Para evitar este tipo de decisiones arbitrarias, se suele codificar a las variables categ´oricas sin relaci´on de orden espec´ıfica con representaciones One-Hot. Cada columna categ´orica, de K clases posibles, se convierte en K variables binarias donde siempre una y solamente una de ellas toma el valor 1. En nuestro ejemplo, codificar´ıamos el rojo con (1, 0, 0, 0), el verde con (0, 1, 0, 0), el azul con (0, 0, 1, 0) y el negro con (0, 0, 0, 1) (es decir 4 variables en total). Notar que dos colores cualesquiera distintos siempre est´an a una distancia geom´etrica de
√
2.
Es importante destacar que el proceso de codificaci´on se define durante el entrenamiento. Es decir, que si al momento de efectuar una predicci´on se le solicita al algoritmo una categor´ıa no vista anteriormente, se le suele asignar a todas las variables codificadas el valor 1. De esta manera simult´aneamente tendr´a una distancia constante al resto de K − 1), y una categor´ıa v´alida tendr´a m´as cerca al resto de categor´ıas las categor´ıas ( v´alidas que a esta codificaci´on particular. One-Hot permite procesar muy f´acilmente las variables categ´oricas, pero puede aumentar considerablemente la cantidad de variables de entrada o predictores.
√

## 2.3. Gradiente Descendente

La regresi´on lineal tiene la ventaja de contar con soluci´on anal´ıtica (2.8), pero la mayor´ıa de las funciones a minimizar no poseen esa ventaja. Adem´as si tenemos en cuenta que para un dx muy grande la inversa de la matriz presente en (2.8) no es computable, nos damos cuenta de la necesidad de contar con un m´etodo num´erico para minimizar funciones.
El m´etodo del gradiente descendente es un algoritmo num´erico de optimizaci´on presentado por Cauchy muchos a˜nos atr´as [10] y, sin embargo, es la esencia de la mayor´ıa de los algoritmos modernos de inteligencia artificial. La idea es sencilla: igualar a cero la
5En las variables que solo pueden tomar dos valores, la relaci´on de orden es intrascendente. En esta
secci´on nos referimos a variables con mayor cantidad de valores posibles.
23
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
J(θ)
J(θ)
θ
θ
(a)
(b)
Figura 2.3: Comparaci´on del comportamiento del gradiente descendente con distinto learning rate. (a) caso convergente y (b) caso divergente.
derivada de una funci´on a minimizar J(θ) num´ericamente. Es decir, avanzar poco a poco (de forma iterativa) en la direcci´on del m´aximo decrecimiento de la funci´on.
θt+1 = θt − α · ∇J(θt+1)
(2.11)
donde α > 0 recibe el nombre de learning rate o tasa de aprendizaje. Este tipo de par´amteros que no se deciden durante el entrenamiento reciben el nombre de hiperpar´ametro, para diferenciarlos de los par´ametros entrenables. Seg´un el valor de α, el comportamiento del algoritmo puede ser bien distinto. En la Fig. 2.3a se puede observar un ejemplo convergente del algoritmo. Paso a paso el algoritmo se va acercando al m´ınimo, aunque corre el riesgo de necesitar muchas iteraciones para alcanzar la convergencia. Sin embargo un learning rate muy grande, lejos de acelerar, puede generar comportamientos divergentes en el algoritmo como puede verse en la Fig. 2.3b.
Por desgracia no existe un optimizador universal que funcione para cualquier tarea y conjunto de datos [11], depender´a de en cada problema el encontrar un valor de α adecuado. En la pr´actica se suele apuntar al valor m´as grande que genere un comportamiento convergente, eligi´endolo por prueba y error. A continuaci´on analizaremos algunos detalles a tener en cuenta a la hora de utilizar este algoritmo.

### 2.3.1. Normalizaci´on como pre-procesamiento

El gradiente descendente, descripto en (2.11), tiene la caracter´ıstica en tener un mismo valor de α para todas las direcciones. El motivo de esto, tiene que ver con solamente tener que seleccionar un hiper-par´ametro en lugar de muchos. Sin embargo, puede que no exista un valor que satisfaga a todas las direcciones. Es por esto que surge la necesidad
24
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
(a)
(b)
Figura 2.4: Comparaci´on del gradiente descendente (a) sin y (b) con normalizaci´on de las variables de entrada a partir de las curvas de nivel.
de normalizar.
La normalizaci´on de cada componente permite poner a todas las variables en la misma unidad. Esta fuerza a todas las variables de entrada o predcitores a tener valor medio nulo y varianza unitaria (emp´ıricamente hablando). Formalmente asigna los valores
(x)k ←
(x)k − µk σk
(2.12)
donde las µk y σk son calculadas previo al entrenamiento como:
µk =
1 ntr
ntr(cid:88)
(xi)k,
i=1
σk =
1 ntr
ntr(cid:88)
i=1
[(xi)k − µk]2
(2.13)
(cid:118) (cid:117) (cid:117) (cid:116)
con ntr la cantidad de muestras de entrenamiento. La Fig. 2.4a muestra el comportamiento de la minimizaci´on por gradiente descendente sobre una superficie representada por las curvas de nivel, denotando un comportamiento err´atico (recordar que el gradiente es ortogonal a las curvas de nivel [12, Cap´ıtulo 13]). En contraste, la Fig. 2.4b muestra su contraparte normalizada, donde con menos iteraciones se logr´o optimizar los par´ametros. Cabe destacar que la normalizaci´on se define durante la etapa de entrenamiento, fijando los valores de µk y σk. A la hora de realizar una predicci´on, se utilizar´a la normalizaci´on ya calculada previamente.
El uso de la normalizaci´on no se restringe solamente a algoritmos optimizados por gradiente descendente. Adem´as de solucionar posibles problemas de convergencia, permite forzar media nula en los predictores hip´otesis de muchos m´etodos basados en ´algebra lineal del aprendizaje autom´atico. Tambi´en permite que sea pertinente la relaci´on entre los predictores. Supongamos por ejemplo que contamos con un conjunto de datos que posee como variables la superficie de una vivienda a cotizar y como otra variable la cantidad de habitaciones. No deber´ıa ser distinto decir que una vivienda posee 36m2 y 3 habitaciones
25
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
(12 veces m´as grande un n´umero que el otro) que 600cm2 y 3 habitaciones (200 veces m´as grande). En ese sentido es muy ´util cuando las magnitudes involucradas tienen diferentes unidades.
Sin embargo, vale resaltar que hay que tener muy claro el motivo de la normalizaci´on. Ya sea para ayudar la convergencia, para forzar media nula o para volver las magnitudes comparables, es necesario entender por que se utiliza. Normalizar preventivamente cualquier conjunto de datos suele traer muchos problemas.

### 2.3.2. Learning Rate ´optimo

En esta secci´on se buscar´an garant´ıas te´oricas de optimalidad para α. Esto es solamente un an´alisis te´orico, en la pr´actica el learning rate se suele elegir intentando tomar el m´aximo valor posible convergente. Esto est´a relacionado con asociar el α con la velocidad de convergencia, lo cu´al en rigor de verdad no es totalmente cierto. El presente an´alisis te´orico nos permitir´a entender las limitaciones de este tipo de asociaciones. Se estudiar´an garant´ıas sobre la velocidad de convergencia para un algoritmo de gradiente descendente sobre una funci´on J(θ) gen´erica (no necesariamente regresi´on lineal, pero sin perderla de vista), aunque con un m´ınimo de hip´otesis razonables de convexidad:
Existe un ´unico θ∗ tal que ∇J(θ∗) = 0.
La matriz Hessiana HJ (θ) existe y es definida positiva para todo θ.
A continuaci´on se utlizar´an algunos resultados matem´aticos conocidos. En primer lugar, se reescribir´a ∇J(θt) utilizando el teorema de Taylor de primer orden, alrededor del mencionado θ∗ [13, Ap´endice A.6]:
∇J(θt) = ∇J(θ∗) + HJ (˜θ) · (θt − θ∗) (2.14) para alg´un ˜θ en el segmento que une θt y θ∗. Notar que HJ (˜θ) es una matriz real, cuadrada y sim´etrica. Por lo tanto, por el teorema espectral [14, Secci´on 4.1], puede escribirse como HJ (˜θ) = QT ΛQ con una matriz de autovalores Λ diagonal y una de autovectores Q ortogonal QT Q = QQT = I. Utilizando este resultado y que ∇J(θ∗) = 0 se obtiene ∇J(θt) = QT ΛQ(θt − θ∗). En general, Λ y Q podr´an ser desconocidas (aunque en el caso de regresi´on lineal pueden calcularse ya que HJ ( ˜w) = 2 XT X no depende de ˜w). Con el ntr fin de estudiar la recurrencia, se reescribir´a la diferencia (θt+1 − θ∗) utilizando la definici´on del gradiente descendente (2.11):
θt+1 − θ∗ = θt − θ∗ − α∇J(θt)
= (cid:0)I − αQT ΛQ(cid:1) (θt − θ∗) = QT (I − αΛ) Q (θt − θ∗)
(2.15)
(2.16)
(2.17)
26
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
|1 − αλj|
|1 − αλj|
κ−1 κ+1
α
1 λm´ax
1 λm´ın
(a)
α∗
(b)
α
Figura 2.5: Resoluci´on gr´afica del problema (2.18). En (a) se resaltan los valores |1 − αλj| para los diferentes autovalores λj; y en (b) se resalta la resoluci´on del problema minmax.
Sea vt = Q (θt − θ∗), la relaci´on de recurrencia (2.17) puede escribirse como vt+1 = (I − αΛ) vt y por lo tanto vt = (I − αΛ)t v0. Hay una relaci´on directa entre la convergencia en θt y la convergencia en vt, por lo que para estudiar garant´ıas, ´esta ´ultima es suficiente. Como criterio de garant´ıa sobre la velocidad de convergencia se elegir´a un criterio de peor caso:
m´ın α
m´ax j
|1 − αλj|
s.t.
|1 − αλj| < 1 ∀ j
(2.18)
donde λj son los elementos de la diagonal de Λ. Es un problema minmax con restricciones. Por el lado de las restricciones, la matriz (I − αΛ) es naturalmente diagonal y la convergencia estar´a dada cuando cada coeficiente sea menor que uno en valor absoluto (por estar elevada a la cantidad de iteraciones). Como criterio de garant´ıa de velocidad se elige minimizar el peor caso de ´estos (su m´aximo). Es importante notar que el α obtenido de esta manera no ser´a el mejor posible en cada caso, sino el que me brinda garant´ıas.
Este problema minmax se puede resolver gr´aficamente [15, Cap´ıtulo 9]. En la Fig. 2.5a se muestran los los diferentes valores |1 − αλj| como funci´on de α. Cada curva en V obtiene su m´ınimo cuando α = 1 , y habr´a un valor m´ınimo y un valor m´aximo (ser´an λj positivos porque son autovalores de una matriz definida positiva). El m´aximo valor de estas curvas se puede ver en la Fig. 2.5b: la m´axima curva comienza siendo la de menor autovalor (λm´ın), hasta que se cruza con la curva de mayor autovalor (λm´ax). En el v´ertice, o m´ınimo valor de esta nueva curva, se encuentra justamente el learning rate ´optimo α∗. Para encontrar el valor hace falta intersectar las dos curvas: la semirrecta decreciente de la curva con m´ınimo autovalor con la semirrecta creciente de la curva con m´aximo autovalor. (2.19)
1 − α∗λm´ın = α∗λm´ax − 1 → α∗ =
2 λm´ın + λm´ax
27
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
La velocidad de convergencia estar´a asociada entonces al valor correspondiente a este
learning rate en el eje de las ordenadas:
1 −
λm´ın =
2 λm´ın + λm´ax
λm´ax − λm´ın λm´ax + λm´ın se denomina n´umero de condici´on de la matriz asociada HJ (˜θ). El donde κ = λm´ax λm´ın learning rate ´optimo no coincide con el m´aximo valor convergente; la condici´on |1 − αλj| < 1 para todo j se puede reescribir como 0 < α < 2 y por lo tanto la condici´on de λj convergencia es α < 2 . Un α muy grande convergente, puede implicar rebotes a la hora de converger como es el caso del ejemplo de la Fig. 2.4a.
κ − 1 κ + 1
(2.20)
λm´ax
=
Vale la pena volver a mencionar que este an´alsis es te´orico. En regresi´on lineal, donde se XT X, no se suele utilizar el valor α∗ principalmente porque
conoce la matriz HJ ( ˜w) = 2 ntr calcular los autovalores es tan costoso como invertir la matriz para utilizar (2.8).

## 2.4. Regresi´on Polin´omica

En la Secci´on 2.2 se present´o la regresi´on lineal como una soluci´on que garantiza baja complejidad; en caso de alcanzar un riesgo emp´ırico bajo hay ciertas garant´ıas de buen desempe˜no. El problema surge cuando el riesgo emp´ırico no alcanza un valor suficientemente satisfactorio, denotando que la complejidad del modelo es insuficiente.
El objetivo m´as ambicioso, en un problema de regresi´on, es estimar la regresi´on asociada a la esperanza condicional E[Y |X = x], ya que esta minimiza el error cuadr´atico medio (Prop. 1.8). Independientemente de la complejidad de la esperanza condicional, el teorema de Taylor indica que cualquier funci´on se puede aproximar como una combinaci´on lineal de coeficientes polin´omicos. Es entonces que surge la regresi´on polin´omica; utilizar una aproximaci´on lineal sobre un mapa polin´omico de los predictores vectoriz´andolos de la siguiente manera: x1,1 x2,1 ...
(2.21)
1 1 ... 1 xntr,1 xntr,2 x2
x1,2 x2,2 ...
x2 x2 ... ntr,1 x2
x1,1x1,2 x2,1x2,2 ...
x2 x2 ... ntr,2 xntr,1xntr,2
   
   
X =


2,1
1,1
2,2
1,2
donde xi,k es la muestra i-´esima de la variable k-´esima. El ejemplo presentado en (2.21) corresponde a un mapa polin´omico de orden 2. En general, el mapa polin´omico de orden ν contendr´a todos los productos cruzados de las variables hasta orden ν inclusive.
Propiedades 2.1 La vectorizaci´on correspondiente a un mapa polin´omico de orden ν sobre d predictores posee una cantidad de columnas (cid:0)d+ν
(cid:1).
ν
28
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
Underfitting
Overfitting
Adecuado
(a)
(b)
(c)
Figura 2.6: Comparaci´on entre regresores denotando (a) un ejemplo de subajuste, (b) uno de sobreajuste, y (c) uno con un ajuste razonable.
Demostraci´on 2.1 (Prop. 2.1) Los coeficientes de la vectorizaci´on de un mapa polin´omico pueden escribirse como
1a0 ·
d (cid:89)
k=1
xak i,k
para algunos ak ∈ N0,
d (cid:88)
k=0
ak = ν
(2.22)
donde los ak efect´uan una codificaci´on. Para determinar la cantidad de columnas del mapa, basta con resolver el problema combinatorio de cuantas maneras posibles se pueden elegir los ak. En (2.21), las codificaciones son de la forma (2, 0, 0), (1, 1, 0), (1, 0, 1), (0, 2, 0), (0, 0, 2) y (0, 1, 1). Para resolver el problema en general, es conveniente estudiarlo como un problema de conteo de objetos indistinguibles. Se cuenta con ν puntos para repartir en k + 1 recipientes (por lo tanto es necesario k separadores). Por ejemplo, el (1, 1, 0) de (2.21) ser´a representado como “ ×| × |” y el (0, 2, 0) como “ | × ×|”. Es decir que de las ν + d posiciones se eligen ν para colocar la × obteniendo as´ı (cid:0)d+ν
(cid:1) columnas.
ν
Es importante destacar que el mapa polin´omico entrega predictores en magnitudes no comparables. Por ejemplo, si una variable estaba medida en m, se incorporar´an nuevas variables medidas en m2, m3, etc. Por ese motivo es indispensable luego de utilizar un mapa polin´omico normalizar6. El siguiente ejemplo ilustra esta idea.
Ejemplo 2.3 Preprocesar el siguiente conjunto de datos, para iniciar el entrenamiento de una regresi´on polin´omica de orden 2. ¿Que cantidad de par´ametros tendr´a el modelo?
6La columna de unos no se normaliza Esta solamente se incorpora como requisito para efectuar pos-
teriormente la regresi´on lineal (para que exista el t´ermino constante).
29
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
x1
x2
1.2
0.8
1.0
2.3
1.3
1.6
Un mapa polin´omico de orden 2 con 2 variables generar´a un mapa de (cid:0)4
(cid:1) = 6 columnas (y por lo tanto tendr´a 6 par´ametros la regresi´on lineal posterior). Las columnas ser´an: la 1, x2 comunas de unos, las columnas x1, x2, x2 2 y x1x2. Calculando las columnas restantes se obtiene
2
x1
x2
x2 1
x2 2
x1x2
1.2
2.3
1.44
5.29
2.76
0.8
1.3
0.64
1.69
1.04
1.0
1.6
1.0
2.56
1.6
El siguiente paso es normalizar, ya que el mapa polin´omico genera variables incomparables en t´erminos de unidad. Calculando la media y el desv´ıo de cada columna, utilizando (2.13), se obtiene:
x1
x2
x2 1
x2 2
x1x2
1.0
1.73
1.03
3.18
1.8
0.16
0.42
0.33
1.53
0.72
µ
σ
Aplicando la normalizaci´on x−µ σ
e incorporando la columna de unos se obtiene el mapa
pedido.
bias
x1
x2
x2 1
x2 2
x1x2
1
1
1
1.22
1.35
1.26
1.38
1.34
-1.22
-1.03
-1.18
-0.97
-1.06
0.0
-0.32
-0.08
-0.4
-0.28
El problema de cambiar la regresi´on lineal por la polin´omica es que se pierde la caracter´ıstica de baja complejidad, pudiendo as´ı tener problemas de overfitting como se mencion´o en la Secci´on 2.1. En la Fig. 2.6 se muestran ejemplos de regresores, mostrando posibles problemas tanto de subajuste (complejidad insuficiente) como sobreajuste (complejidad excesiva). Recordando (2.1), mientras que el underfitting lo podemos detectar por
30
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
un alto riesgo emp´ırico el overfitting requiere conocer el gap de generalizaci´on, magnitud que no puede conocerse de forma exacta por depender de valores esperados. Es entonces que surge la necesidad de tener diferentes conjuntos de datos.

### 2.4.1. Conjuntos de datos

En general se necesitan datos para efectuar distintas funciones: para entrenar, para ajustar la relaci´on de compromiso sesgo/varianza y simplemente para estimar el riesgo esperado.
Conjunto de entrenamiento (train set): Datos utilizados para minimizar el riesgo emp´ırico. Sobre estos se produce el “aprendizaje”. Las variables definidas a partir de este conjunto se llaman par´ametros.
Conjunto de validaci´on (validation or development set): Datos utilizados para comparar modelos. Las variables definidas a partir de este conjunto (o definidas previas al entrenamiento) se llaman hiper-par´ametros.
Conjunto de testeo (test set): Datos utilizados para evaluar el desempe˜no final del algoritmo. Su ´unica funci´on es presentar estimadores insesgados de las m´etricas de error y no es imprescindible.
En el caso de una regresi´on polin´omica b´asica, se pueden entrenar varios modelos para diferentes valores de ν (cada uno de ellos entrenado con el conjunto de entrenamiento) y se elegir´a el valor de ν que minimice el error medido con el conjunto de validaci´on. Una vez elegido el ν y teniendo el modelo entrenado para ese valor, se procede a medir el error con el conjunto de testeo (estimando as´ı el riesgo esperado) para evaluar si la decisi´on fue o no satisfactoria. El mismo procedimiento se puede efectuar para elegir el valor del learning rate α o cualquier otro hiper-par´ametro involucrado.
En la bibliograf´ıa y en la documentaci´on muchas veces se habla de conjunto de testeo en general para referirse a todos los datos no usados durante el entrenamiento. Pero es importante tener en consideraci´on las diferencias entre validaci´on y testeo: la validaci´on se utiliza para tomar decisiones sobre el dise˜no del modelo, eligiendo hiper-par´ametros. Una vez que se utiliz´o dicho conjunto de datos para tomar una decisi´on, las estimaciones de error dejan de ser insesgadas: como se utilizaron los datos de validaci´on para elegir el modelo, analizar el desempe˜no del algoritmo con ellos mismo puede dejar de ser representativo. Sin embargo, si la validaci´on no es minuciosa, puede considerarse aceptable utilizarla como m´etrica de error (aunque sesgada, la estimaci´on puede ser suficiente). Contar con el conjunto de testeo puede ser prescindible, su ´unica funci´on es medir la eficacia
31
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
final del sistema. Es recomendable usarlo principalmente luego de validaciones exhaustivas o cuando no se efectuaron validaciones en absoluto (y es razonable en desconfiar en el desempe˜no del sistema). Incluso en el caso de contar con un solo predictor, se puede analizar el overfitting/underfitting de un algoritmo gr´aficamente sin necesidad de contar con el conjunto de testeo, como es el caso de la Fig. 2.6.
El problema con generar los diferentes conjuntos de datos es que disminuye la cantidad de datos usado durante el entrenamiento. No hay una regla para asignar proporciones a estos conjuntos, depender´a de cuantos datos se tenga, de la complejidad del modelo y de la dificultad de la tarea. Por ejemplo en el caso de regresi´on lineal, basta con tener solamente un conjunto de entrenamiento, ya que se asume que el gap de generalizaci´on es peque˜no por la complejidad del modelo. En lugar de validar el resultado, simplemente analizo si se alcanz´o o no un razonable riesgo emp´ırico.

### 2.4.2. Regularizaci´on

El problema de sesgo se detecta cuando el riesgo emp´ırico de entrenamiento es grande comparado con el supuesto error bayesiano. El mismo se soluciona aumentando la complejidad del modelo. En cambio, problema de varianza se detecta cuando el riesgo emp´ırico de validaci´on es grande comparado con el de entrenamiento, y la mejor manera de combatirlo es aumentando la cantidad de muestras. Por desgracia esto no siempre es posible, ya sea por la dificultad de obtener los datos o de procesarlos. Las t´ecnicas destinadas a combatir el overfitting sin incorporar nuevos datos se denominan regularizaci´on.
Existen diferentes t´ecnicas de regularizaci´on: generar datos sint´eticos para incorporarlos, incorporar ruido a las muestras para dificultar el sobreajuste, limitar la complejidad del modelo, entre otras. Pero quiz´as la m´as importante es el agregado de un t´ermino de penalizaci´on al riesgo a minimizar durante el entrenamiento. B´asicamente se busca perturbar la optimizaci´on del modelo, minimizando en lugar del riesgo emp´ırico, el riesgo regularizado:
J(θ) =
1 ntr
ntr(cid:88)
i=1
ℓ(xi, yi) + λ · R(θ)
(2.23)
donde λ ≥ 0 es un hiper-par´ametro que controlar´a el overfitting, y R(θ) recibe el nombre de regularizador. El resigo regularizado define una funci´on a optimizar durante el entrenamiento, rara vez es utilizado en la etapa de testeo. La incorporaci´on del regularizador tiene por objeto acercar la funci´on a optimizar J(θ) al riesgo esperado (2.1). En ese sentido, un buen regularizador ser´a aquel donde λR(θ) sea representativo del gap de generalizaci´on. Cuando λ = 0 la regularizaci´on es ignorada, mientras que para λ muy grandes lo que es ignorado son los datos.
El regularizador m´as utilizado en regresi´on polin´omica es el denominado L2, weight
32
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
decay o regularizaci´on de Tikhonov : R(w, b) = 1 ∥w∥2. Una primera interpretaci´on de ntr esta selecci´on es que el incorporar la norma cuadr´atica de los pesos w en la funci´on a minimizar tender´a a “apagar” coeficientes wj ≈ 0, y por lo tanto la complejidad efectiva del modelo bajar´a, tendiendo a disminuir el overfitting. Otra posible interpretaci´on es que limitando el valor de w lo que estamos haciendo es tendiendo a limitar el m´aximo valor posible de la funci´on costo ℓ(x, y) ≤ L, y por lo tanto limitando el gap de generalizaci´on y por lo tanto el overfitting.
E[ℓ(X, Y )] −
1 ntr
ntr(cid:88)
ℓ(xi, yi) ≤ L
(2.24)
i=1 En la pr´actica, en regresi´on polin´omica se suele dejar un ν fijo d´andole un margen suficiente de complejidad al modelo y controlar el overfitting con el hiper-par´ametro de regularizaci´on. Es decir que la etapa de validaci´on se efectuar´a sobre λ en lugar de ν. Esto es beneficioso porque permite un incremento controlado de la regularizaci´on ya que mientras λ ∈ R, ν ∈ N necesita dar saltos discretos.
Ejemplo 2.4 Hallar una soluci´on matricial al problema de regresi´on lineal sin sesgo y con regularizaci´on L2. Analizar el comportamiento para algoritmos no regularizados y muy regularizados.
El riesgo regularizado para este problema es de la forma
J(w) =
∥Xw − y∥2 +
∥w∥2
(2.25)
1 ntr
λ ntr
Basta con analizar la primera derivada (gradiente) y la segunda derivada (matriz Hessiana) respecto a w (para m´as informaci´on sobre derivadas respecto vectores/matrices ver [9]).
∇J(w) =
2 ntr
XT (Xw − y) +
2λ ntr
w,
HJ (w) =
2 ntr
(XT X + λ · I)
(2.26)
donde la matriz Hessiana es claramente definida positiva (y por lo tanto inversible). Esto implica que el problema es convexo y por lo tanto igualando a cero el gradiente equivale a minimizar el riesgo regularizado. Se puede despejar entonces:
w = (XT X + λ · I)−1XT y
(2.27)
Por un lado, si λ = 0 se obtiene como soluci´on w = X†y donde X† = (XT X)−1XT es la pseudoinversa. Por el otro si λ es muy grande (lo suficiente para que λ·I enmascare a XT X pero no tanto para que w ≈ 0) se obtiene w ≈ 1 λXT y. Esto quiere decir que un algoritmo regularizado interpreta la transpuesta como la operaci´on inversa. Esta operaci´on tiene un muy bajo costo computacional por lo que es utilizada para inversi´on de problemas f´ısicos bajo el nombre de Linear Back Projection [16].
33
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
Importante
Importante
e t n a t r o p m
i
o N
e t n a t r o p m
i
o N
(a)
(b)
Figura 2.7: Ejemplos de grilla para validar dos hiper-par´ametros, de los cuales solo uno importa fuertemente sobre el error. (a) Una grilla regular, y (b) una grilla aleatoria.

### 2.4.3. Etapa de validaci´on

La etapa de validaci´on est´a basada en el enfoque de prueba error. Por ejemplo, si se desea validar el hiperpar´ametro λ se deber´an realizar V entrenamientos diferentes, donde V es la cantidad de puntos de λ que deseo probar. Finalmente se termina decidiendo por el valor de λ que menor error de validaci´on genere. El problema principal de este enfoque aparese cuando se desea validar varios hiper-par´ametros. Por ejemplo, si queremos probar V valores de λ y V valores de α, necesitar´ıamos realizar V 2 simulaciones. La etapa de validaci´on es computacionalmente costosa, y es necesario tener en cuenta algunas consideraciones para no sufrir tanto esta particularidad. La cantidad de entrenamientos a efectuar crece exponencialmente con la cantidad de hiper-par´ametros a validar, fen´omeno que recibe el nombre de maldici´on de la dimensionalidad. Este fen´omeno est´a presente tambi´en con las muestras de entrenamiento: La necesidad de muestras crece exponencialmente con la cantidad de predictores.
Supongamos que se desean validar dos hiper-par´ametros, probando V valores para cada uno y efectuando V 2 entrenamientos en total. En el caso de que solamente uno de los hiperpar´ametros sea influyente sobre el error (a priori esta informaci´on era desconocida), se terminan realizando V 2 entrenamientos para probar solo V valores del hiper-par´ametro relevante. Este fen´omeno puede verse en la Fig. 2.7a, donde en los m´argenes se muestra una curva de como var´ıa el error de validaci´on con los respectivos hiper-par´ametros. En este ejemplo, vemos que se debieron realizar 9 entrenamientos para probar efectivamente solo 3 valores del hiper-par´ametro relevante.
Es por este motivo que al validar dos o m´as hiper-par´ametros se opta por efectuar una grilla aleatoria, como se muestra en la Fig. 2.7b. Al elegir valores al azar, es muy
34
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
probable que no haya valores repetidos y por lo tanto se terminen probando V 2 valores del hiper-par´ametro relevante. En este ejemplo, observando el margen superior, se puede ver que se probaron hiper-par´ametros con errores m´as bajos.
Otra recomendaci´on a la hora de validar par´ametros por grilla aleatoria es efectuarla por etapas. Por ejemplo, si cuento con la posibilidad de realizar 300 entrenamientos, quiz´as sea conveniente primero validar con 100 de ellos. Con esos resultados uno puede limitar la zona donde el error de validaci´on deba ser m´as chico, y hacer una segunda b´usqueda (con otros 100 entrenamientos) dentro de ese espacio limitado. Repitiendo por tercera vez con los 100 entrenamientos restantes logr´e concentrar muchos valores al rededor de la zona de mayor inter´es.
Por ´ultimo, hay muchos casos donde la cantidad de datos observados es limitada y no es posible reservarse un conjunto de validaci´on. Es entonces cuando surgen t´ecnicas un poco m´as sofisticadas.
2.4.3.1. Validaci´on Cruzada
La etapa de validaci´on es cr´ıtica en modelos de alta complejidad, ya que los hiperpar´ametros asociados con la regularizaci´on suelen ser muy sensibles. Este es el caso de λ en regresi´on polin´omica, el cu´al suele necesitar ser validado. El problema es que definir un conjunto de datos de validaci´on, como se mencion´o en la Secci´on 2.4.1, muchas veces es prohibitivo debido a que no se cuenta con suficientes datos. Sin embargo, existen algunas t´ecnicas para validar hiper-par´ametros sin necesidad de definir un conjunto de validaci´on, repitiendo el entrenamiento en m´ultiples ocasiones (y por lo tanto pagando un costo computaional). Estas t´ecnicas se conocen como validaci´on cruzada.
Leave-one-out cross-validation (LOOCV) es el m´etodo b´asico de validaci´on cruzada. Propone reservar una sola muestra para validaci´on y entrenar con el resto. Este proceso se repite para cada muestra, realizando ntr entrenamientos. El error entonces se puede estimar promediando el error de validaci´on de todos los entrenamientos. Para utilizar este m´etodo para validar un hiper-par´ametro se requiere realizar una gran cantidad de entrenamientos. Por ejemplo, supongamos que se desean probar V valores diferentes de λ en un algoritmo de regresi´on polin´omica. Por cada uno de estos valores, se deber´an hacer ntr entrenamientos, realizando en total V · ntr repeticiones (en contraste con definir un conjunto de validaci´on que solamente necesita V entrenamientos). Finalmente se elige el λ que genere menor error de validaci´on.
Una soluci´on intermedia entre LOOCV y definir un conjunto de validaci´on es el m´etodo conocido como K-Folds. En ´el, se propone separar el conjunto de datos de entrenamiento en K paquetes para entrenar con K − 1 de ellos y validar con el restante. Se repite el procedimiento K veces usando como conjunto de validaci´on siempre un paquete diferente,
35
Cap´ıtulo 2. Regresi´on en Inteligencia Artificial
y se define el error de validaci´on total como el promedio del error de validaci´on de cada experimento. De esta manera, para probar V valores de un hiper-par´ametro se deben realizar V · K entrenamientos, donde 1 < K ≤ ntr (LOOCV coincide con K = ntr). Un valor grande de K requiere efectuar muchos entrenamientos, pero un valor chico de K reduce demasiado la cantidad de muestras efectivas de entrenamiento. Si cada paquete K muestras, el entrenamiento efectivo se har´a con (K−1)·ntr contiene ntr muestras. La decisi´on de K depender´a mucho de la cantidad de muestras con las que se cuente.
K
36

# 3


# Clasificaci´on en Inteligencia Artificial

Utilizar un algoritmo para resolver una tarea es importante. Pero imaginemos el potencial de abrir el algoritmo y entender los por menores de su razonamiento. Quiz´as mirando el algoritmo nos veamos a nosotros mismos.
En la Secci´on 2.2.1 se discuti´o la problem´atica de no tener una relaci´on de orden clara en predictores categ´oricos. Es de esperar entonces que esta problem´atica tambi´en sea atendida cuando la variable categ´orica es la etiqueta. En estos casos, el error cuadr´atico medio como m´etrica de error deja de tener sentido y surge la necesidad de un nuevo paradigma. Estamos en presencia del problema de clasificaci´on.
Los algoritmos de clasificaci´on son fundamentales en el mundo real. En el d´ıa a d´ıa estamos rodeados de decisiones que implican asignar categor´ıas. Desde determinar si un correo es spam o leg´ıtimo, diagnosticar enfermedades, aprobar cr´editos o recomendar productos, la clasificaci´on permite automatizar procesos que antes requer´ıan juicio humano. En esencia, clasificar es simplificar: transformar un conjunto complejo de datos en una decisi´on concreta. Esta capacidad es clave para la eficiencia operativa, la personalizaci´on de servicios y la toma de decisiones informadas a gran escala. Sin algoritmos de clasificaci´on, gran parte de las aplicaciones modernas de la inteligencia artificial simplemente no ser´ıan viables.
El objetivo de un clasificador es estimar una funci´on Y = φ(X), donde Y ∈ Y es una variables categ´orica (Y finito) que recibe el nombre de clase. La funci´on costo elegida en este tipo de problemas es la hard error o loss 0-1 : ℓ(x, y) = 1{y ̸= φ(x)}. Esta m´etrica, a diferencia del error cuadr´atico, solo distingue entre aciertos y errores. El riesgo esperado es la probabilidad de error E [ℓ(X, Y )] = P(Y ̸= φ(X)). As´ı mismo se denomina accuracy1 o probabilidad de acierto a su probabilidad complementaria P(Y = φ(X)).
Al tomar una cantidad finita de valores posibles, cada clasificador φ : Rdx → Y define una partici´on del espacio Rdx donde la cantidad de elementos de la partici´on corresponde a la cantidad de clases o elementos de Y. A las fronteras que separan los elementos de dicha partici´on se las denomina frontera de decisi´on. Es importante destacar que los
1Se recomienda evitar traducciones literales como exactitud, ya que en el aprendizaje estad´ıstico
existen diversas m´etricas cuyas traducciones se pueden confundir.
37
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
elementos de la partici´on son conjuntos de nivel de la funci´on φ.
Al igual que el problema de regresi´on, lo esencial para entender el objetivo de un algoritmo, es interpretar cu´al es su soluci´on ´optima y cual es el error bayesiano asociado.

## 3.1. Optimalidad en Clasificaci´on

En la Prop. 1.8 se demostr´o que el regresor asociado a la esperanza condicional minimiza el error cuadr´atico medio y que su error bayesiano asociado es la esperanza de la varianza condicional. En los problemas de clasificaci´on, la funci´on costo ℓ(x, y) = 1{y ̸= φ(x)} tiene una naturaleza muy distinta al error cuadr´atico. Esta caracter´ıstica vuelve a la clasificaci´on un poco m´as compleja que la regresi´on, y es necesario desarrollar algunos conceptos para su estudio.

### 3.1.1. Clasificador Bayesiano

Se denomina clasificador bayesiano al clasificador ´optimo que minimiza la probabilidad de error alcanzando el error bayesiano [3, Cap´ıtulo 2]. Este clasificador ser´a presentado en el siguiente resultado.
Propiedades 3.1 P (Y ̸= φ(X)) ≥ 1 − E (cid:2)m´axy PY |X=X(y)(cid:3) con igualdad si y solo si φ(x) = arg m´axy PY |X=x(y).
La notaci´on PY |X=X(y) representa la probabilidad condicional PY |X=x(y) evaluada en
la variable aleatoria X.
Demostraci´on 3.1 (Prop. 3.1) La Prop. 1.7 permite definir una probabilidad como P(Y = φ(X)) = E[P(Y = φ(X)|X)]. La probabilidad condicional dentro de la esperanza es muy f´acil de acotar como:
P(Y = φ(X)|X = x) = PY |X=x(φ(x)) ≤ m´ax y∈Y PY |X=x(y). Luego
con igualdad si y solo si φ(x) = arg m´ax y∈Y
P(Y ̸= φ(X)) = 1 − E[P(Y = φ(X)|X)] ≥ 1 − E
PY |X=x(y)
(3.1)
(cid:20)
m´ax y∈Y
(cid:21) PY |X=X(y)
(3.2)
Este resultado define el clasificador bayesiano como φ(x) = arg m´axy PY |X=x(y). El mismo no es para nada sorprendente, indica que el mejor clasificador es el que elige siempre la opci´on m´as probable. Sin embargo, el error bayesiano requiere un esfuerzo de interpretaci´on. Sea Ry, el conjunto de x ∈ Rdx donde y es el m´aximo de PY |X=x(y)2. Es
2Para los x ∈ Rdx donde haya dos o m´as m´aximos de PY |X=x(y), se asigna dicho x a solo una de
dichas Ry elegida arbitrariamente (en ´ultima instancia, definen conjuntos de medida nula).
38
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
PY (1)pX|Y =1(x)
PY (2)pX|Y =2(x)
R1
R2
x
Figura 3.1: Grafico PY (y)pX|Y =y(x) para un ejemplo unidimensional de dos clases, resaltando la partici´on R1-R2 y el error bayesiano (sombreado).
decir que los Ry son los conjuntos de nivel del clasificador bayesiano: (cid:27)
(cid:26)
Ry =
x ∈ Rdx : PY |X=x(y) = m´ax y′∈Y
PY |X=x(y′)
(3.3)
Estos conjuntos definen una partici´on de Rdx, donde cada x pertenecer solo a uno de
los posibles Ry. Dicha partici´on permite reescribir el m´aximo de manera m´as amena:
m´ax y∈Y
PY |X=x(y) =
=
(cid:88)
y∈Y
(cid:88)
y∈Y
PY |X=x(y)1{x ∈ Ry}
PY (y)
pX|Y =y(x) pX(x)
1{x ∈ Ry}
(3.4)
(3.5)
Esta identidad reescribe el error bayesiano con una expresi´on f´acilmente comprensible
(cid:90)
Rdx (cid:90) (cid:88)
1 − E
(cid:20)
m´ax y
(cid:21)
PY |X(y|X)
= 1 −
= 1 −
=
(cid:88)
y∈Y
pX(x) m´ax
PY |X=x(y)dx
y
PY (y)pX|Y =y(x)dx
Ry
y∈Y PY (y)P(X ̸∈ Ry|Y = y)
(3.6)
(3.7)
(3.8)
El resultado (3.8) expresa al error bayesiano como la suma de los errores dentro de cada regi´on Ry. La Fig. 3.1 muestra el producto PY (y)pX|Y =y(x) para un ejemplo unidimensional de dos clases. Las regiones R1 y R2 son delimitadas a partir de PY |X=x(1) ≶ PY |X=x(2). Para cada x ∈ R, esas regiones son equivalentes a comparar PY (1)pX|Y =1(x) ≶ PY (2)pX|Y =2(x), ya que pX(x) es la misma de ambos lados3. El error bayesiano puede verse como la regi´on sombreada; es la suma del ´area bajo la curva de y = 1 que cae en R2 (sombreado azul) y la curva de y = 2 que cae en R1 (sombreado rojo).
3En general, el clasificador bayesiano al definirse a partir del operador argmax puede escribirse como
arg m´axy PY |X=x(y) = arg m´axy PY (y)pX|Y =y.
39
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
PY (1)pX|Y =1(x)
PY (0)pX|Y =0(x)
R0
R1
R0
x
Figura 3.2: Grafico PY (y)pX|Y =y(x) para el Ej. 3.1, resaltando la partici´on R0-R1 y el error bayesiano (sombreado).
El error bayesiano es un l´ımite fundamental, que no podr´a ser mejorado independientemente de la tecnolog´ıa. Cualquier otro clasificador siempre funcionar´a peor que el bayesiano. De igual manera, tambi´en existen l´ımites razonables a superar por cualquier clasificador. Llamamos clasificador azaroso al que decide al azar entre todas las clases, independientemente de la entrada, siendo su probabilidad de acierto de 1 K . A su vez, llamamos clasificador dummy al que decide siempre la clase m´as probable pero sin tener en cuenta la entrada, siendo su probabilidad de acierto m´axy PY (y). Un clasificador cualquiera φ(x) deber´a cumplir entonces:
PY (y)P(X ̸∈ Ry|Y = y) ≤ P(Y ̸= φ(X)) ≤ 1 −
(3.9)
1 K
PY (y)P(X ̸∈ Ry|Y = y) ≤ P(Y ̸= φ(X)) ≤ 1 − m´ax
y
PY (y)
(3.10)
(cid:88)
y∈Y (cid:88)
y∈Y
Cabe destacar que estos errores, tanto del clasificador azaroso como el dummy, no son fundamentales. Un clasificador puede tener errores peores que esto (imaginar el clasificador que se equivoca siempre). Pero el mismo carece de sentido (puede hasta ser conveniente hacer lo contrario a lo que el clasificador sugiere) desde la perspectiva del aprendizaje. A continuaci´on se estudar´an en detalle dos ejemplos para fijar los conceptos.
Ejemplo 3.1 Por un canal de comunicaciones se emiten bits de forma aleatoria, siendo el 40 % de ellos 1. Dependiendo del bit transmitido, la comunicaci´on es afectada por un ruido aditivo normal de media nula y varianzas: 4 si el bit es un 0 y 1 si el bit es un 1. Sea X la se˜nal recibida y Y el bit emitido. Hallar el clasificador bayesiano y su respectivo error. Expresar el resultado en funci´on de Φ(·) (funci´on de distribuci´on de la normal est´andar).
En este tipo de ejercicios es recomendable primero determinar la distribuci´on de los datos. En particular Y ∼ Ber(0.4) y X se define sumando al valor binario del bit Y
40
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
un ruido aditivo: X|Y =0 ∼ N (0, 4) y X|Y =1 ∼ N (1, 1). En la Fig. 3.2 pueden verse las curvas PY (y)pX|Y =y(x) para ambas clases. Para determinar las regiones R0 y R1 basta con analizar donde PY (0)pX|Y =0(x) ≶ PY (1)pX|Y =1(x), la cu´al se puede simplificar como:
0.6 √ 2 3 4
2π ≶ e (cid:18) 3 4
log
e− x2
8 ≶ 0.4 √ 2π
e− (x−1)2
2
8 − (x−1)2 x2
2
(cid:19)
≶ x2 8
−
+ x −
1 2
3 8
x2 − x +
1 2
+ log
3x2 − 8x + 4 − 8 log
≶ 0
(cid:19)
≶ 0
(cid:19)
x2 2 (cid:18) 3 4 (cid:18) 4 3
(3.11)
(3.12)
(3.13)
(3.14)
(3.15)
El lado izquiero de (3.15) es una p´arabola convexa de ra´ıces reales x− y x+ que har´an las veces de frontera de decisi´on. Dicha par´abola ser´a negativa (R0) para x− < x < x+, definiendo las regiones de la Fig. 3.2. Los valores de las ra´ıces se pueden calcular resolviendo la par´abola:
x− =
1 6
(cid:32)
(cid:115)
8 −
16 + 96 log
(cid:19)(cid:33)
(cid:18)4 3
≈ 0.23,
x+ =
(cid:32)
(cid:115)
8 +
16 + 96 log
(cid:19)(cid:33)
(cid:18) 4 3
1 6
≈ 2.43
(3.16)
El clasificador bayesiano se define a partir de que curva de la Fig. 3.2 es la m´as grande
en cada regi´on:
φ(x) = arg m´ax y∈Y
PY |X=x(y) =
 

0 x ≤ x− 1 x− < x ≤ x+ 0 x+ < x
(3.17)
Por ´ultimo, para el error bayesiano basta con sumar los errores sombreados en la Fig.
3.2 y expresarlos a partir de la funci´on de distribuci´on de la normal est´andar:
(cid:20)
1−E
m´ax y
(cid:21) PY |X=X(y)
= PY (0)P(X ∈ R1|Y = 0) + PY (1)P(X ∈ R0|Y = 1)
(3.18)
= 0.6P(x− < X ≤ x+|Y = 0) + 0.4P(X ≤ x−|Y = 1) + 0.4P(X > x+|Y = 1) (3.19)
(cid:20)
= 0.6
Φ
(cid:19)
(cid:18) x+ 2
− Φ
(cid:19)(cid:21)
(cid:18) x− 2
+ 0.4 (cid:2)Φ (cid:0)x− − 1(cid:1) + 1 − Φ (cid:0)x+ − 1(cid:1)(cid:3) ≈ 0.324
(3.20)
Dado que Y ∼ Ber(0.4), el error bayesiano es menor que el dummy 0.324 < 0.4.
Cualquier clasificador razonable tendr´a una probabilidad de error entre 0.324 y 0.4.
Ejemplo 3.2 Se quiere clasificar un conjunto de datos en dos clases. La etiqueta posee distribuci´on Y ∼ Ber(1/2), mientras que los predictores X ∈ R2 poseen distri-
41
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
x2
PY (0)pX|Y =0(x)
x1
R0
R1
PY (1)pX|Y =1(x)
Figura 3.3: Curvas de nivel de PY (y)pX|Y =y(x) y frontera de decisi´on para el Ej. 3.2.
(cid:32)(cid:34)
(cid:35)
(cid:34)
(cid:35)(cid:33)
buci´on X|Y =0 ∼ N
0 1 frontera de decisi´on y el clasificador bayesiano.
1 0 0 1
,
y X|Y =1 ∼ N
(cid:32)(cid:34)
(cid:35)
(cid:34)
,
0 0
2 0 0 1
(cid:35)(cid:33)
. Hallar la
En este caso se trata de un problema bidimensional. El clasificador bayesiano puede factorizarse como φ(x) = arg maxy PY |X=x(y) = arg maxy PY (y)pX|Y =y(x) y por lo tanto la frontera de decisi´on debe cumplir estar´a formada por todos los x ∈ R2 tales que:
PY (0)p(x|Y = 0) = PY (1)p(x|Y = 1)
e− 1
2 (x−µ0)T Σ−1
0 (x−µ0) =
1 (cid:112)|Σ1|
e− 1
2 (x−µ1)T Σ−1
1 (x−µ1)
1 (cid:112)|Σ0|
log
(cid:19)
(cid:18) |Σ1| |Σ0|
= (x − µ0)T Σ−1
0 (x − µ0) − (x − µ1)T Σ−1
1 (x − µ1)
(3.21)
(3.22)
(3.23)
donde (µk, Σk) son los par´ametros de X|Y =k. Sea x = (x1, x2), se pueden calcular todos las magnitudes involucradas en la frontera
= 2
|Σ1| |Σ0| 1 + (x2 − 1)2 0 (x − µ0) = x2 x2 1 2
1 (x − µ1) =
+ x2 2
(x − µ0)T Σ−1
(x − µ1)T Σ−1
(3.24)
(3.25)
(3.26)
La condici´on de la frontera de decisi´on puede escribirse como log(2) = x2
1
2 − 2x2 + 1 y
por lo tanto dicha frontera es: (cid:26)
x ∈ R2 : x2 =
x2 1 4 En la Fig. 3.3 se puede ver la frontera de decisi´on y una curva de nivel de cada factorizaci´on PY (y)pX|Y =y(x). En este caso, se puede observar que para definir el clasificador bayesiano basta con verificar que las medias de las gaussianas queden del lado correcto:
1 − log(2) 2
(3.27)
+
(cid:27)
42
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
φ(x1, x2) = arg m´ax y∈Y
PY |X=(x1,x2)(y) =
 

0 x2 > x2
1
4 + 1−log(2)
2
1 x2 ≤ x2
1
4 + 1−log(2)
2
(3.28)
de esta manera quedan definidas las regiones R0 y R1.

### 3.1.2. Entrop´ıa Cruzada

(cid:80)n
La funci´on costo hard error es problem´atica cuando se quiere resolver la minimizaci´on del riesgo emp´ırico 1 i=1 1 {yi ̸= φ(xi)} num´ericamente. No solo por los posibles problen mas de diferenciabilidad, sino porque su estructura “de saltos” no permite un recorrido por gradiente descendente efectivo (es dif´ıcil de aprender). Es entonces que surge la necesidad de m´etodos m´as sofisticados. Teniendo en cuenta que el objetivo de un problema de clasificaci´on es aprender el clasificador bayesiano arg maxy PY |X=x(y) (v´ease Prop. 3.1), en la pr´actica suele dividirse dicha tarea en dos operaciones:
Aprender toda la distribuci´on condicional PY |X(y|x).
Estimar a partir de la distribuci´on aprendida, el clasificador bayesiano qued´andose con el argumento m´aximo φ(x) = arg maxy PY |X=x(y).
Mientras que la segunda operaci´on es inmediata, el aprender PY |X(y|x) requiere definir una nueva funci´on costo, donde minimizar su valor esperado tenga a esta distribuci´on como valor ´optimo.
(cid:104)
(cid:105)
≥ E (cid:2)− log PY |X=X(Y )(cid:3) con igualdad si y solo Propiedades 3.2 E si ˆP (y|x) = PY |X(y|x) para todo (x, y), donde las esperanzas involucradas son con respecto a la verdadera distribuci´on conjunta de (X, Y ).
− log ˆP (Y |X)
La demostraci´on ser´a presentada en la siguiente secci´on. La funci´on costo log-loss ℓ(x, y) = − log ˆP (y|x) puede ser estudiada de forma an´aloga a las Props. 1.8 y 3.1, teniendo en cuenta que se estar´a optimizando una relaci´on probabil´ıstica ˆP (y|x) en lugar de una determin´ıstica φ(x). En este caso, el riesgo a minimizar E se denomine entrop´ıa cruzada, el valor ´optimo se alcanza con la verdadera distribuci´on PY |X y el error bayesiano asociado E (cid:2)− log PY |X=X(Y )(cid:3) recibe el nombre de entrop´ıa condicional. Los clasificadores entrenados con este paradigma permiten efectuar dos tipos de decisiones:
(cid:105) − log ˆP (Y |X)
(cid:104)
Sea x ∈ Rdx, llamamos predicci´on soft de un algoritmo a la predicci´on de las probabilidades estimadas ˆP (·|x). Esta estimaci´on es un vector de probabilidades de todas las clases posibles (son valores no negativos que suman 1). Su desempe˜no se suele medir con el riesgo a minimizar E[− log ˆP (Y |X)].
43
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
Sea x ∈ Rdx, llamamos predicci´on hard de un algoritmo a la predicci´on final de la clase estimada φ(x). Es decir, es una estimaci´on del valor de Y . Generalmente se ˆP (y|x). Su la suele definir a partir de la predicci´on soft como: φ(x) = arg m´axy∈Y desempe˜no se suele medir con la probabilidad de acierto P(Y = φ(X)).
3.1.2.1. Elementos de Teor´ıa de Informaci´on
Con el fin de interpretar las magnitudes involucradas en la Prop. 3.2 y efectuar su demostraci´on, es necesario presentar m´etricas de Teor´ıa de Informaci´on [2, Cap´ıtulo 2 y 8] conocidas como entrop´ıas. La primera m´etrica en cuesti´on busca medir la discrepancia entre distribuciones de probabilidad. Es este contexto se presenta la divergencia de Kullback Leibler, tambi´en conocida como entrop´ıa relativa.
Definici´on 3.1 Sean P (·) y Q(·) dos funciones de masa de probabilidad tales que si Q(y) = 0 entonces P (y) = 0. Se define la divergencia de Kullback Leibler como:
KL(P ∥Q) =
P (y) log
(cid:88)
y∈Y
(cid:19)
(cid:18) P (y) Q(y)
(cid:20)
= EP
log
(cid:19)(cid:21)
(cid:18) P (Y ) Q(Y )
(3.29)
donde el sub´ındice P en la esperanza hace referencia a que medida se utiliza para calcularla.
La divergencia de Kullback Leibler no es una distancia ya que no es sim´etrica4. Esta
caracter´ıstica se puede ver en el siguiente ejemplo.
Ejemplo 3.3 Sean P y Q dos distribuciones Bernoulli de par´ametros 1 tivamente. Calcular KL(P ∥Q) y KL(Q∥P ).
2 y 1
3 respec-
Las variables Bernoulli son variables de dos ´atomos {0, 1} por lo que su c´alculo es
inmediato.
(cid:18)
KL (P ∥Q) =
1 −
(cid:18)
KL (Q∥P ) =
1 −
(cid:19)
(cid:19)
1 2
1 3
log
log
(cid:18) 1 − 1 2 1 − 1 3 (cid:18) 1 − 1 3 1 − 1 2
(cid:19)
(cid:19)
+
+
1 2
1 3
log
log
(cid:19)
(cid:19)
(cid:18) 1 2 1 3 (cid:18) 1 3 1 2
=
=
1 2
1 3
log
log
(cid:19)
(cid:18)9 8 (cid:18)32 27
≈ 0.059 nats
(3.30)
(cid:19)
≈ 0.057 nats
(3.31)
donde nats es la unidad correspondiente al logaritmo natural.
A pesar de no ser una distancia, la divergencia de Kullback Leibler tiene sentido como
m´etrica discrepancia entre distribuciones debido a la siguiente propiedad.
Propiedades 3.3 KL(P ∥Q) ≥ 0 con igualdad si y solo si P (y) = Q(y) para todo y ∈ Y.
4Se asume la convenci´on 0 log(0) = 0 por su continuidad en el l´ımite.
44
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
x y que f ′′(x) = 1
Demostraci´on 3.2 (Prop. 3.3) Sea f (x) = x − 1 − log(x) con x > 0, es inmediato notar que f ′(x) = 1 − 1 x2 > 0. Debido a la convexidad de f (x), la funci´on alcanza su m´ınimo cuando f ′(x) = 0 (se alcanza en x = 1). Por lo tanto la funci´on f (x) ≥ f (1) = 0 es no negativa. Esto quiere decir que log(x) ≤ x − 1 con igualdad si y solo si x = 1. Luego (cid:18) Q(Y ) P (Y )
−KL (P ∥Q) = EP
(cid:20)Q(Y ) P (Y )
(cid:20)Q(Y ) P (Y )
≤ EP
= EP
(3.32)
− 1
− 1
(cid:19)(cid:21)
log
(cid:21)
(cid:21)
(cid:20)
con igualdad si y solo si P (y) = Q(y) para todo y ∈ Y. Esa ´ultima esperanza puede escribirse como:
EP
(cid:21)
(cid:20)Q(Y ) P (Y )
(cid:88)
=
P (y)
Q(y) P (y)
= 1
(3.33)
y∈Y Finalmente KL(P ∥Q) ≥ 0 con igualdad si y solo si P (y) = Q(y) para todo y ∈ Y.
Esta propiedad implica que la divergencia alcanza su m´ınimo cuando las distribuciones son iguales. Esta m´etrica permite proponer modelos cuyo valor ´optimo sea la verdadera distribuci´on. Con esto puede demostrarse la Prop. 3.2.
Demostraci´on 3.3 (Prop. 3.2) La demostraci´on es inmediata a partir de la Prop. 3.3:
(cid:105) (cid:104) − log ˆP (Y |X)
E
= E
log
(cid:34)
(cid:32)
(cid:33)(cid:35)
PY |X=X(Y ) ˆP (Y |X) PY |X=X∥ ˆP (·|X)
(cid:104)
(cid:16)
KL
= E ≥ E (cid:2)− log PY |X=X(Y )(cid:3) (cid:17) PY |X=x∥ ˆP (·|x)
(cid:16)
+ E (cid:2)− log PY |X=X(Y )(cid:3)
(cid:17)(cid:105)
+ E (cid:2)− log PY |X=X(Y )(cid:3)
(3.34)
(3.35)
(3.36)
donde tener en cuenta que KL
es funci´on de x.
Para terminar de interpretar la Prop. 3.2 es necesario estudiar las diferentes entrop´ıas. El concepto de entrop´ıa recibe su nombre por su analog´ıa con la termodin´amica y representa el valor esperado de la informaci´on que aporta conocer a una variable aleatoria [17]. Esta informaci´on depende de la probabilidad de ocurrencia de la variable a conocer. El saber que ma˜nana saldr´a el sol no contiene demasiada informaci´on porque es algo que ocurre siempre. En cambio, el saber que ma˜nana explota el sol contiene much´ısima informaci´on. En ese sentido la informaci´on es decreciente con la probabilidad. En ese sentido se definen la entrop´ıa y la entrop´ıa condicional.
H(Y ) = E[− log PY (Y )],
H(Y |X) = E[− log PY |X=X(Y )]
(3.37)
donde la esperanza presente en la entrop´ıa condicional es medida con respecto a la distribuci´on conjunta de (X, Y ). En este sentido H(Y |X) = E[H(PY |X=X)], donde H(PY |X=x) es funci´on de x. Adem´as, la entrop´ıa se define mediante logaritmos porque permite transcribir en sumas y restas las factorizaciones entre probabilidades como las de (1.5) en
45
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
σ(z)
1
σ′(z)
1 4
z
z
(a)
(b)
Figura 3.4: Comportamiento de (a) la funci´on sigmoide, y (b) su derivada.
H(X, Y ) = H(Y |X) + H(X) (la informaci´on de (X, Y ) es la suma de la informaci´on de X y la de Y que no est´a en X).
(cid:105) (cid:104) − log ˆP (Y |X)
Por otro lado, se denomina entrop´ıa cruzada a las magnitudes similares a la entrop´ıa, donde la medida con la cu´al se toma la esperanza difiere de la distribuci´on dentro del logaritmo. En el caso E es una entrop´ıa cruzada entre la verdadera PY |X=x y la modelada ˆP (·|x). La entrop´ıa cruzada puede escribirse como la entrop´ıa (en este caso condicional) sumada a la divergencia de Kullback Leibler, como se mostr´o en (3.35). Se suele interpretar como la verdadera entrop´ıa sumada a un t´ermino de error (medida en t´erminos de Kullback Leibler).

## 3.2. Regresi´on Log´ıstica

La regresi´on log´ıstica busca extender el concepto de regresi´on lineal estudiado en la Secci´on 2.2 al problema de clasificaci´on. El objetivo es plantear una soluci´on de muy baja complejidad (lineal), para tener ciertas garant´ıas de que el overfitting est´a controlado. La primera diferencia es que la magnitud a estimar {PY |X=x(y)}y∈Y, a diferencia de E[Y |X = x], debe pensarse como una funci´on vectorial (se deben estimar una funci´on por cada ´atomo Y en lugar de solo una). Otra diferencia es que la soluci´on debe cumplir ciertas condiciones relacionadas con ser una funci´on de masa de probabilidad en y. Al ser la probabilidad una magnitud acotada, no ser´a posible modelarla de forma lineal. En este tipo de problemas, lo que se busca que sea lineal es la frontera de decisi´on.
46
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial

### 3.2.1. Regresi´on Log´ıstica Binaria

El caso m´as simple de la clasificaci´on es la de dos clases: Sea que Y es una variable de Bernoulli5 con Y = {0, 1}. Luego es suficiente con estimar p(x) = PY |X=x(1), ya que PY |X=x(0) = 1−p(x) se puede calcular por el complemento (nuevamente basta con estimar un solo valor). Para garantizar que dicha estimaci´on se encuentre en el intervalo (0, 1) se modela ˆp(x) = σ(wT x + b) con w ∈ Rdx, b ∈ R y σ(z) = 1 1+e−z la funci´on sigmoide. Esta funci´on cumple las siguientes propiedades.
Propiedades 3.4 Sea p = σ(z) la funci´on sigmoide.
1. σ : R → (0, 1) es una funci´on creciente.
2. Su inversa es σ−1(p) = log p
1−p con p ∈ (0, 1).
3. Se derivada σ′(z) = σ(z)(1 − σ(z)) alcanza valores en (cid:0)0, 1
4
(cid:1).
Demostraci´on 3.4 (Prop. 3.4) El primer inciso es inmediato utilizando la monoton´ıa de la exponencial y evaluando en los l´ımites l´ımz→−∞ σ(z) = 0 y l´ımz→+∞ σ(z) = 1. La Fig. 3.4a muestra este comportamiento. Para el segundo inciso basta con despejar z de p = 1
1+e−z . Para el tercero se puede aplicar la regla de la cadena: (cid:18) 1
1 1 + e−z Finalmente reparametrizando σ′(z) = p(1 − p), se obtiene una par´abola c´oncava de ra´ıces p = 0 y p = 1. De esta manera su m´ınimo valor 0 se alcanza en p = 0 (z → −∞) y p = 1 (z → +∞), y su m´aximo valor 1 2 (z = 0). La Fig. 3.4b muestra este comportamiento.
1 + e−z = σ(z)(1 − σ(z))
4 se alcanza en p = 1
σ′(z) = −
(−e−z) =
1 + e−z
(3.38)
e−z
(cid:19)2
Para analizar la forntera de decisi´on que una predicci´on hard genera en este tipo de
modelos, se debe notar que las siguientes representaciones son equivalentes:
ˆP (1|x) = ˆP (0|x)
σ(wT x + b) = 1 − σ(wT x + b)
σ(wT x + b) = 1 2
wT x + b = 0
Finalmente la frontera de decisi´on es lineal ya que est´a formada por los predictores x ∈ Rdx tales que wT x + b = 0. Adem´as, las muestras x con wT x + b > 0 ser´an clasificadas como 1, mientras que las x tales que wT x + b < 0 ser´an clasificadas como 0.
5El an´alisis no cambia al suponer dos ´atomos cualesquiera.
47
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
En cambio, durante el entrenamiento se define como funci´on costo a la log-loss (cuyo valor esperado era la entrop´ıa cruzada) ℓ(x, y) = − log ˆP (y|x). Es decir que dicha funci´on costo es de la forma:
 
ℓ(x, y) =
− log (cid:0)1 − σ(wT x + b)(cid:1) Si y = 0

− log (cid:0)σ(wT x + b)(cid:1)
Si y = 1
(3.39)
= − (1 − y) log (cid:0)1 − σ(wT x + b)(cid:1) − y log (cid:0)σ(wT x + b)(cid:1)
(3.40)
y sus derivadas pueden calcularse a partir de la regla de la cadena:
∂ℓ(x, y) ∂w
∂ℓ(x, y) ∂b
= xσ(wT x + b) (cid:0)1 − σ(wT x + b)(cid:1)
(cid:20)
1 − y 1 − σ(wT x + b)
−
y σ(wT x + b)
(cid:21)
= x (cid:2)σ(wT x + b) (1 − y) − y (cid:0)1 − σ(wT x + b)(cid:1)(cid:3) = x (cid:2)σ(wT x + b) − y(cid:3)
= σ(wT x + b) (cid:0)1 − σ(wT x + b)(cid:1)
(cid:20)
1 − y 1 − σ(wT x + b)
−
y σ(wT x + b)
(cid:21)
= (cid:2)σ(wT x + b) − y(cid:3)
(3.41)
(3.42)
(3.43)
(3.44)
(3.45)
En este caso, el riesgo emp´ırico J(w, b) = 1 ntr
i=1 ℓ(xi, yi) no tendr´a un m´ınimo valor capaz de hallarse anal´ıticamente, pero si por gradiente descendente. El gradiente en cuesti´on tendr´a como componentes a
(cid:80)ntr
∂J(w, b) ∂w
=
1 ntr
(cid:2)σ(wT xi + b) − yi
(cid:3) ,
xi
∂J(w, b) ∂b
=
1 ntr
ntr(cid:88)
i=1
ntr(cid:88)
i=1
(cid:2)σ(wT xi + b) − yi
(cid:3)
(3.46) De alguna manera, lograr que el gradientes sea nulo tiende a inducir yi ≈ σ(wT xi + b)
(no tomar de forma literal, es una interpretaci´on).

### 3.2.2. Regresi´on Log´ıstica Categ´orica

Adaptar el modelo de regresi´on log´ıstica binaria descripto en la Secci´on 3.2.1 a una clasificaci´on multiclase tiene sus particularidades. Principalmente por el hecho que, por cada x ∈ Rdx, no se desea estimar una sola probabilidad sino una para cada y ∈ Y. Sea Y = {1, · · · , K} el conjunto de clases6, dos de las adaptaciones m´as habituales se conocen como el modelo identificable y el modelos softmax.
6Esta decisi´on es solamente para simplificar la notaci´on. Los resultados siguen siendo v´alidos para K
´atomos cualesquiera.
48
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
x2
x1
R2
R1
R3
Figura 3.5: Ejemplo de frontera de decisi´on para un algoritmo de regresi´on log´ıstica categ´orica.
Definici´on 3.2 Se denomina modelo de regresi´on log´ıstica identificable a
ˆP (y|x) =
  
ewT 1+(cid:80)K−1 j=1 e
y x+by wT j
x+bj
1 1+(cid:80)K−1
j=1 e
wT j
x+bj
y ∈ {1, · · · , K − 1}
y = K
donde el modelo contiene K − 1 vectores wj y K − 1 valores bj.
Definici´on 3.3 Se denomina modelo de regresi´on log´ıstica softmax a ewT y x+by j=1 ewT
· 1{y ∈ {1, · · · , K}}
ˆP (y|x) =
j x+bj
(cid:80)K
(3.47)
(3.48)
donde el modelo contiene K vectores wj y K valores bj.
Mientras que el primero tiene la ventaja de ser identificable (dos conjuntos de par´ametros distintos generan modelos diferentes) y contener menos par´ametros (y por lo tanto menos complejidad), el segundo es m´as sencillo de implementar. Por este motivo el modelo softmax es el m´as utilizado en la actualidad a pesar de estar sobreparametrizado; en general nos referiremos a este modelo como regresi´on log´ıstica categ´orica. El general, sea a = (a1, · · · , aK) llamamos softmax a la operaci´on matem´atica de softmax(k|a) = eak j=1 eaj . En este sentido el modelo de regresi´on log´ıstica softmax es el (cid:80)K softmax de la transformaci´on af´ın wT
k x + bk.
La predicci´on hard, en el caso de la regresi´on log´ıstica categ´orica softmax, posee una
expresi´on muy simple:
φ(x) = arg max
ˆP (y|x) = arg max
y∈Y
y∈Y
wT
y x + by
(3.49)
la cu´al tiene la caracter´ıstica de ser lineal. Es decir que las fronteras de decisi´on ser´an hiperplanos. En la Fig. 3.5 puede verse un ejemplo de frontera para este tipo de problemas.
49
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
(a)
(b)
(c)
3.6: Comparaci´on
Figura con subajuste, Imagen underfitting-and-overfitting-in-machine-learning/.
ejemplo con sobreajuste. https://www.geeksforgeeks.org/machine-learning/
entre con ajuste
razonable, y (c) uno
(b) uno de
clasificadores
denotando:
extra´ıda
(a)
un
Es importante destacar que la predicci´on hard es el argmax de wT soft el softmax de wT a constantes sumadas (es decir, que no dependan de k).
k x + bk y la predicci´on k x + bk. Ambas operaciones tienen la caracter´ıstica de ser indiferentes
Durante el entrenamiento se define como funci´on costo a la log-loss (cuyo valor esperado era la entrop´ıa cruzada) ℓ(x, y) = − log ˆP (y|x). Es decir que dicha funci´on costo es de la forma:
ℓ(x, y) = log
ewT
j x+bj
− (wT
y x + by)
(3.50)
(cid:32) K (cid:88)
(cid:33)
y sus derivadas pueden calcularse a partir de la regla de la cadena:
j=1
,
= x
∂ℓ(x, y) ∂wk
(cid:17) (cid:16) ˆP (k|x) − 1{y = k}
∂ℓ(x, y) ∂bk (cid:80)ntr En este caso, el riesgo emp´ırico J(θ) = 1 i=1 ℓ(xi, yi) (con θ = {(wy, by)}y∈Y) no ntr tendr´a un m´ınimo valor capaz de hallarse anal´ıticamente, pero si por gradiente descendente. El gradiente en cuesti´on tendr´a como componentes a (cid:16) ˆP (k|xi) − 1{yi = k} 1 ntr
(cid:16) ˆP (k|xi) − 1{yi = k}
= ˆP (k|x) − 1{y = k}
∂J(θ) ∂wk
∂J(θ) ∂bk
1 ntr
(3.51)
ntr(cid:88)
ntr(cid:88)
xi
=
=
(cid:17)
(cid:17)
,
i=1
i=1
De alguna manera, lograr que el gradientes sea nulo tiende a inducir un modelo que asigne toda su probabilidad a la etiqueta correcta ˆP (k|xi) ≈ 1{yi = k} (no tomar de forma literal, es una interpretaci´on).
(3.52)

### 3.2.3. Regresi´on Log´ıstica Polin´omica y Overfitting

El mapa polin´omico presentado en la Secci´on 2.4 puede aplicarse al problema de clasificaci´on de manera inmediata. Sea cu´al sea la frontera de decisi´on del clasificador bayesiano
50
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
que se desea aprender, la misma puede ser aproximada con polin´omios tan bien como se desee (incrementando el orden). La cantidad de par´ametros de un modelo de regresi´on log´ıstica binaria ser´a la misma que en el problema de regresi´on, mientras que en el caso de una regresi´on log´ıstica categ´orica softmax habr´a que multiplicarla por el n´umero de clases K. La normalizaci´on nuevamente es indispensable en este caso por tratarse de magnitudes de diferentes unidades y entrenar por gradiente descendente.
Al igual que en el problema de regresi´on, el problema de la versi´on polin´omica de clasificaci´on es que el aumentar la complejidad del modelo puede ocasionar overfitting. En la Fig. 3.6 podemos ver tres ejemplos de clasificadores. El primero propone una frontera lineal, mostrando un problema de sesgo, por presentar una complejidad insuficiente. El segundo un ajuste adecuado al problema, y el tercero un claro problema de varianza generando overfitting.
La manera de tratar estos fen´omenos es el mismo que en regresi´on. El problema de sesgo se detecta por riesgo emp´ırico alto y se soluciona aumentando la complejidad del modelo. En cambio, el problema de varianza se detecta por un alto gap de generalizaci´on y se soluciona incorporando m´as muestras o regularizando. Cabe destacar que para analizar el underfitting se suele focalizar en la log-loss como funci´on costo ya que es el objetivo de la optimizaci´on (predicci´on soft), pero para analizar el overfitting se suele analizar la loss 0-1 como funci´on costo para analizar la capacidad de generalizaci´on (predicci´on hard ). Mientras que durante el entrenamiento se minimiza la entrop´ıa cruzada emp´ırica, en validaci´on y testeo se analiza la probabilidad de error como objetivo ´ultimo.
Una de las opciones m´as habituales como regularizador es utilizar la penalizaci´on L2,
generando un riesgo emp´ırico regularizado para el caso binario de la forma: n (cid:88)
J(w, b) =
− log ˆP (yi|xi) +
∥w∥2
λ ntr
1 ntr
i=1
y para el caso categ´orico:
J(θ) =
1 ntr
n (cid:88)
i=1
− log ˆP (yi|xi) +
λ ntr
K (cid:88)
j=1
∥wj∥2
(3.53)
(3.54)
donde si se vectorizan todos los wj como una matriz, la suma de las normas recibe el nombre de norma Frobenius [9].
La etapa de validaci´on tambi´en funciona de forma an´aloga a la regresi´on. Supongamos que se desea validar λ, entonces se realizan entrenamientos para diferentes valores del hiperpar´ametro minimizando en cada uno (3.53) o (3.54). Luego se decide el valor de λ que alcance menor probabilidad de error medida con el conjunto de validaci´on.
Un detalle a tener en cuenta en la clasificaci´on (que no est´a presente en la regresi´on) es la calibraci´on [18]. El entrenamiento habitual de clasificaci´on consiste en estimar ˆP (y|x) ˆP (y|x). Sin embargo, la para luego quedarse con su argumento m´aximo φ(x) = arg maxy
51
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
etapa de validaci´on consiste en ajustar φ(x) sin tener en cuenta las predicciones soft. Si el an´alisis o aplicaci´on del algoritmo se va a basar en la decisi´on hard no hay problema. Pero seguir considerando ˆP (y|x) una estimaci´on de la probabilidad condicional puede ser problem´atico luego de la mencionada etapa de validaci´on.
La calibraci´on es una etapa posterior a la validaci´on que re-ajusta ˆP (y|x) deteriorando poco o nada la decisi´on hard φ(x). Suele aplicarse sobre un conjunto de datos de calibraci´on (diferente de los de entrenamiento, validaci´on y testeo). El m´etodo m´as sencillo se denomina temperature scaling y se basa en fijar un par´ametro de calibraci´on τ > 0, donde:
ˆPcal(y|x) =
e 1 τ (wT (cid:80)K j=1 e
y x+by)
1 τ (wT
j x+bj )
· 1{y ∈ {1, · · · , K}}
(3.55)
ˆPcal(y|x) = arg maxy
El modelo descripto en (3.55), permite ajustar τ para ajustar la decisi´on soft sin modiˆP (y|x). Una de las m´etricas ficar la probabilidad de error: arg maxy m´as importante para evaluar la calibraci´on es la entrop´ıa cruzada. Se elige τ > 0 que minimice la entrop´ıa cruzada medida con el conjunto de datos de calibraci´on. Esta m´etrica tiene la ventaja de poder minimizarse por gradiente descendente, en lugar de necesitar diversas pruebas como es el caso de la etapa de validaci´on. El desempe˜no final del modelo se eval´ua a partir de la entrop´ıa cruzada medida con el conjunto de testeo.

## 3.3. Figuras de M´erito en Clasificaci´on

Posterior al entrenamiento, dependiendo de que etapa de un clasificador se desee evaluar, las m´etricas a analizar pueden ser diferentes. Anteriormente se mencion´o como para medir el desempe˜no de las predicciones soft se utiliza la entrop´ıa cruzada, pero para medir el desempe˜no de las predicciones hard se utiliza la probabilidad de error o su complemento el accuracy. Sin embargo, est´as m´etricas no son las ´unicas relevantes.

### 3.3.1. Figuras de M´erito en Clasificaci´on Binaria

En el caso de la clasificaci´on binaria, existe dos tipos de errores posibles: falla de detecci´on o falsos negativos (predecir φ(x) = 0 cuando y = 1) y falsa alarma o falsos positivos (predecir φ(x) = 1 cuando y = 0). Dependiendo de la aplicaci´on, puede que uno de ellos sea mucho m´as grave que el otro, volviendo a la probabilidad de error una m´etrica poco adecuada. En estos casos se utilizan m´etricas llamadas precision y recall7. Recall = P (φ(X) = 1|Y = 1)
Precision = P (Y = 1|φ(X) = 1) ,
(3.56)
7Dado que muchas de las m´etricas poseen nombres que pueden ser considerados sin´onimos, es reco-
mendable evitar utilizar traducciones.
52
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
La m´etrica precision se utiliza cuando los falsos positivos tienen consecuencias graves. Por ejemplo, diagnosticar err´oneamente una enfermedad a una persona sana. La m´etrica recall se utiliza cuando cuando los falsos negativos tiene consecuencias graves. Por ejemplo, no detectar una transacci´on fraudulenta. Un clasificador que cree siempre detectar φ(x) = 1, tendr´a una excelente recall, pero no necesariamente buenas precision y accuracy.
Otro fen´omeno relacionado es que ocurre cuando las clases est´an muy desbalanceadas (uno de los valores de Y ocurre mucho m´as que el otro). Es muy posible que un clasificador dummy, que siempre elija la clase m´as probable, alcance un buen accuracy. Desde la perspectiva de la tarea a resolver, puede que en algunos contextos esta soluci´on sea satisfactoria. Pero desde la perspectiva del aprendizaje, el algoritmo no logr´o identificar ninguna caracter´ıstica de los datos. En conjuntos de datos desbalanceados, el desempe˜no del aprendizaje de un algoritmo se mide con el F1-score, una m´etrica que tiene en cuenta tanto la precision como la recall :
F1 = 2 ·
Precision · Recall Precision + Recall
= 2 · (Precision // Recall)
(3.57)
En el siguiente ejemplo se muestra como se estiman emp´ıricamente las mencionadas
m´etricas.
Ejemplo 3.4 Un clasificador es evaluado con un conjunto de testeo. El an´alisis inform´o 120 verdaderos positivos, 60 falsos negativos, 30 falsos positivos y 9790 verdaderos negativos. Calcular accuracy, precision, recall y F1-score.
Sea Y la verdadera etiqueta y φ(X) el clasificador aprendido, los n = 10000 datos del enunciado deben ser interpretarse de la siguiente manera:
Verdaderos Positivos: #(Y = 1, φ(X) = 1) = 120.
Falsos Negativos: #(Y = 1, φ(X) = 0) = 60.
Falsos Positivos: #(Y = 0, φ(X) = 1) = 30.
Verdaderos Negativos: #(Y = 0, φ(X) = 0) = 9790.
Las estimaciones emp´ıricas de las m´etricas se calculan como:
Accuracy = P(Y = φ(X)) ≈
Precision = P(Y = 1|φ(X) = 1) ≈
Recall = P(φ(X) = 1|Y = 1) ≈
= 0.991
#(Y = φ(X)) n #(Y = 1, φ(X) = 1) #(φ(X) = 1) #(Y = 1, φ(X) = 1) #(Y = 1)
F1 = 2 ·
Precision · Recall Precision + Recall
≈ 0.7273
53
(3.58)
(3.59)
= 0.8
≈ 0.6667
(3.60)
(3.61)
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
) 1 =
Y | 1 = )
X
( t φ ( P
Perfecto
azaroso
Clasificador

### EER

P(φt(X) = 1|Y = 0)
Figura 3.7: Curvas ROC para clasificadores de diferente calidad.
Mientras que el accuracy por si solo parece muy positivo, dependiendo de la aplicaci´on puede que la precision y la recall sean insuficientes. El desbalance de las clases #(Y = 0) = 9820 y #(Y = 1) = 180 sugiere que el accuracy sobreestima el aprendizaje y la F1 ≈ 0.7273 es una m´etrica m´as representativa (es un resultado moderadamente bueno). Este fen´omeno tambi´en pod´ıa detectarse comparando el accuracy contra la probabilidad de acierto dummy (siempre elegir la clase 0) 0.982. Si bien el accuracy es superior, su cercan´ıa sugiere relativizar este resultado.
Una manera de corregir posibles desbalances sin repetir el entrenamiento es sesgar m´as a una de las clases. Por ejemplo, la clasificaci´on binaria detecta un y = 1 cuando φ(x) = 1{ ˆP (1|x) > ˆP (0|x)} o su equivalente φ(x) = 1{ ˆP (1|x) > 1 2}. Una manera de sesgar la clasificaci´on es comparar la probabilidad del modelo φt(x) = 1{ ˆP (1|x) > t} contra un umbral 0 ≤ t ≤ 1. Para t = 0 el clasificador predecir´a siempre φt(x) = 1, para t = 1 predecir´a siempre φt(x) = 0, y para t = 1 2 el clasificador se comportar´a de forma equivalente a antes de sesgar las clases φt(x) = φ(x).
El desempe˜no de una familia de clasificadores φt(x) se suele evaluar con las denominadas curvas ROC (Receiver Operating Characteristic). En lugar de analizar el clasificador para un umbral t, las curvas ROC permiten estudiar el desempe˜no de toda la familia de clasificadores posibles. Estas curvas se definen como un gr´afico de la tasa de verdaderos positivos (TPR o recall ) P(φt(X) = 1|Y = 1) en funci´on de la tasa de falsos positivos (FPR) P(φt(X) = 1|Y = 0).
En la Fig. 3.7 pueden verse ejemplos de curvas ROC. Cada punto de la curva representa un valor de umbral distinto, pasando siempre por los puntos (1, 1) (correspondiente a t = 0) y (0, 0) (correspondiente a t = 1). Mientras que el clasificador perfecto se representa por el punto (0, 1), suele interpretarse como l´ımite inferior el clasificador azaroso
54
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
Clase predicha
A
A
30
B
C
3
0
a r e d a d r e v
e s a l C
B
2
25
C
1
2
4
27
(a)
Clase predicha
A
B
C
a r e d a d r e v
e s a l C
A
0.909 0.061 0.030
B
0.100 0.833 0.067
C
0
0.129 0.871
(b)
Figura 3.8: Ejemplo de matriz de confusi´on. (a) Sin normalizar; y (b) normalizando para representar P (ˆy|y).
φt(X) ∼ U(0, 1) independiente de Y (representado por la recta identidad). En ese sentido se considerar´a mejor o peor algoritmo en la medida que se acerquen m´as o menos al ´optimo o al clasificador azaroso. Por ejemplo, en la Fig. 3.7 la familia de clasificadores representada por la curva roja es mejor que la azul que a su vez es mejor que la verde.
Puede existir el caso donde que algoritmo sea mejor dependa de la regi´on. Una m´etrica num´erica muy utilizada para cuantificar el desempe˜no de una curva es el ´area bajo la curva (AUC, Area Under the Curve), siendo habitualmente un n´umero entre 1 2 (clasificador al azar) y 1 (clasificador perfecto). Otra m´etrica, un poco m´as sofisticada, para evaluar el desempe˜no de una curva ROC es el error de igual tasa (EER, Equal Error Rate). El EER se define como el error para el umbral que vuelve iguales a los dos errores EER = 1 − P(φt(X) = 1|Y = 1) = P(φt(X) = 1|Y = 0). B´asicamente est´a definida por la intersecci´on entre la curva ROC con la recta P(φt(X) = 1|Y = 0) + P(φt(X) = 1|Y = 1) = 1 como puede verse en la Fig. 3.7. Esta m´etrica no solamente permite caracterizar toda la curva con un solo n´umero, sino que tambi´en propone un umbral razonable para problemas donde no se conocen las consecuencias de los errores.

### 3.3.2. Figuras de M´erito en Clasificaci´on Categ´orica

As´ı como la clasificaci´on binaria tiene sus figuras de m´erito particulares, la clasificaci´on categ´orica tambi´en. Entre ellas, la m´as popular es la matriz de confusi´on: una matriz que representa los errores que se comente al predecir una clase en muestras de otra clase. En la Fig. 3.8a puede verse un ejemplo de matriz de confusi´on para una clasificaci´on de 3 clases A, B y C. Mientras que la diagonal de la matriz muestra los aciertos, el resto de la matriz muestra errores. Por ejemplo hubo 3 muestras de la clase B, clasificadas como la clase A. Estas matrices tambi´en se puede normalizar para representar probabilidades, como puede verse en la Fig. 3.8b. Las mismas pueden normalizarse para representar P (ˆy|y) (por fila),
55
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
P (y|ˆy) (por columna) o P (y, ˆy) (toda la matriz); siendo la primera la elegida en este ejemplo.
La m´etrica F1-score puede adaptarse tambi´en a este tipo de clasificaci´on (siempre se puede adaptar, pero ser´a recomendable utilizarla en clases desbalanceadas). B´asicamente se descompone la clasificaci´on categ´orica en K clasificaciones binarias del tipo una clase contra todas. Se denomina Macro-F1 al promedio de los F1-score de estas clasificaciones binarias. En el ejemplo de la Fig. 3.8 se puede calcular de las siguiente manera:
Para la clase A, se tienen 30 verdaderos positivos, 3 falsos positivos y 3 falsos negativos. Esto define una precision, una recall y un F1-score de 30 33 (las tres magnitudes son iguales).
Para la clase B, se tienen 25 verdaderos positivos, 6 falsos positivos y 5 falsos negativos. Esto define una precision de 25
30 y un F1-score de 50 61.
31, una recall de 25
Para la clase C, se tienen 27 verdaderos positivos, 3 falsos positivos y 4 falsos negativos. Esto define una precision de 27
31 y un F1-score de 54 61.
30, una recall de 27
Finalmente la Macro-F1 es el promedio de las F1-score previamente calculados. En este ejemplo es de aproximandamente 0.871.

## 3.4. An´alisis del Discriminante

En secciones anteriores se demostr´o que las soluciones ´optimas para diferentes funciones costo se definen a partir de la distribuci´on condicional de Y |X=x. El error cuadr´atico medio se minimiza estimando φ(x) = E[Y |X = x] (Prop. 1.8), la probabilidad de error con el clasificador bayesiano φ(x) = arg maxy PY |X=x(y) (Prop. 3.1) y la entrop´ıa cruzada estimando la verdadera probabilidad condicional ˆP (y|x) = PY |X=x(y) (Prop. 3.2). En todos los casos basta con modelar la distribuci´on condicional, sin hacer ninguna suposici´on sobre la marginal pX(x). Pero que sea suficiente con modelar la condicional de Y |X=x no impide modelar tambi´en la marginal de X.
Una primera distinci´on entre algoritmos de aprendizaje estad´ıstico es la de algoritmos discriminativos y generativos. Se llama algoritmo discriminativos a los que solamente modelan la distribuci´on condicional Y |X=x y generativos a los que modelan la conjunta (X, Y ). Los discriminativos poseen la ventaja de imponer menos hip´otesis, modelando solamente la relaci´on que se encarga de la predicci´on. En contraste, los algoritmos generativos requieren modelar tambi´en la distribuci´on marginal de los datos por lo que necesitan mayor cantidad de datos para estimarse. Pero estos ´ultimos poseen la ventaja de poder generar nuevos datos sint´eticos X ∼ pX.
56
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
Con la popularizaci´on de la inteligencia artificial, es por todos conocida la utilidad de los algoritmos generativos. Actualmente nos preguntamos como pudimos vivir tantos a˜nos sin una m´aquina que dibuje un conejo realista disfrazado de ´angel. Las aplicaciones de los modelos generativos pueden ser relevantes por si misma (como por ejemplo los modelos de lenguaje) o pueden servir para mejorar la etapa discriminativa. Se denomina aumento de datos, al procedimiento de incorporar datos sint´eticos previo a un entrenamiento. Sin embargo, estos datos deben usarse con cuidado porque no dejan de ser artificiales y de ninguna manera independientes a los datos utilizados para generarlos.
Uno de los modelos generativos m´as sencillo es el de mezcla de gaussianas (GMM, Gaussian Mixture Model). En ´el, se asume tanto que Y es una variable categ´orica Y ∼ Cat(c1, · · · , cK) como que la distribuci´on de X|Y =k ∼ N (µk, Σk). Es importante resaltar que, una vez estimados los par´ametros del modelo, ser´a posible simular nuevas realizaciones como k ← Cat(c1, · · · , cK) para luego simular x ← N (µk, Σk). En el GMM, la distribuci´on de los predictores es una mezcla de gaussianas: k (x−µk)
(3.62)
ˆp(x) =
K (cid:88)
cke− 1
2 (x−µk)T Σ−1 2 (cid:112)|Σk| dx
(2π)
k=1
y (x−µy)− 1
2 log |Σy|
y adem´as la distribuci´on condicional es de la forma: 2 (x−µy)T Σ−1
ˆP (y|x) ∝ elog(cy)− 1
1
k (x − µk) − 1
(3.63) En un modelo GMM, ˆP (y|x) es el softmax de la forma cuadr´atica δk(x) = log(ck) − 2(x − µk)T Σ−1 2 log |Σk|, la cu´al recibe el nombre de funci´on discriminante. La funci´on discriminante define las fronteras de decisi´on del problema8. El Ejemplo 3.2 es un caso de GMM, donde se observa una frontera cuadr´atica. Por este motivo, el algoritmo utilizado para modelar la GMM recibe el nombre de an´alisis del discriminante cuadr´atico (QDA, Quadratic Discriminant Analysis), donde las predicciones hard son definidas a partir de
φ(x) = arg max
ˆP (y|x) = arg max
δy(x)
y∈Y
y∈Y
(3.64)
De esta manera, la predicci´on soft ˆP (y|x) y la predicci´on hard φ(x) ser´an el softmax y el argmax de la funci´on discriminante δy(x) respectivamente.
Uno de los problemas de los modelos generativos es que al estimar tanto PY |X=x(y) como p(x), los modelos poseen mayor cantidad de par´ametros. Esta caracter´ıstica vuelve a estos modelos m´as complejos que sus contra-partes discriminativas, aumentando los riesgos de overfitting si no se tiene suficiente cantidad de muestras. Con el fin de bajar la complejidad, una habitual simplificaci´on es suponer todas las matrices de covarianza iguales (Σy = Σ para todo y ∈ Y), hip´otesis que recibe el nombre de homocedasticidad. Bajo esta hip´otesis, la distribuci´on condicional puede reescribirse agrupando constantes
8Las fronteras pueden parametrizarse como δi(x) = δj(x) con i ̸= j.
57
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
multiplicativas como:
2 µT
2µT
y Σ−1µy
ˆP (y|x) ∝ elog(cy)− 1
2 (x−µy)T Σ−1(x−µy) ∝ elog(cy)+xT Σ−1µy− 1
(3.65) donde se redefine la funci´on discriminante para este caso como una funci´on lineal ˜δk(x) = xT Σ−1µk + log(ck) − 1 k Σ−1µk. Por este motivo, el algoritmo utilizado para modelar la GMM recibe el nombre de an´alisis del discriminante lineal (LDA, Linear Discriminant Analysis), donde la predicci´on soft ˆP (y|x) y la predicci´on hard φ(x) ser´an el softmax y el argmax de la funci´on discriminante ˜δy(x) respectivamente. Es importante destacar que el modelo asociado a la regresi´on log´ıstica, analizada en la Secci´on 3.2, es un caso particular de LDA donde wk = Σ−1µk y b = log(ck) − 1 2µT Una de las caracter´ısticas de los algoritmos de LDA y QDA es que ambos desarrollan su etapa de entrenamiento a partir de computar estimadores puntuales. Es habitual utilizar para ello estimadores insesgados:
k Σ−1µk.
Dk = {xi : 1 ≤ i ≤ n ∧ yi = k}
ˆck =
ˆµk =
ˆΣk =
#(Dk) n 1 #(Dk)
(cid:88)
x
x∈Dk
1 #(Dk) − 1
(cid:88)
x∈Dk
(x − ˆµk)(x − ˆµk)T
ˆΣ =
1 n − K
K (cid:88)
(#(Dk) − 1) ˆΣk
k=1
(3.66)
(3.67)
(3.68)
(3.69)
(3.70)
donde en el caso de QDA se utilizan las ˆΣk (no es necesario calcular ˆΣ) y en el caso de LDA las ˆΣk solamente son un paso intermedio en el c´alculo de la covarianza del modelo ˆΣ. A continuaci´on se demostrar´a por que este tipo de estimadores son insesgados.
Demostraci´on 3.5 (Estimadores Insesgados) En primer lugar supongamos que X|Y =k ∼ N (µk, Σk) y Y ∼ Cat(c1, · · · , cK). Entonces #(Dk) ∼ Bin(n, ck) y por lo tanto E[ˆck] = ck. En segundo lugar, se puede observar que las medias pueden escribirse como ˆµk = 1 i=1 xi1{yi = k}. Se define y = (y1, · · · , yn), donde #(Dk) = f (y) es funci´on de las etiquetas. Utilizando las propiedades de la esperanza condicional (Props. 1.7):
#(Dk)
(cid:80)n
E[ˆµk] = E[E[ˆµk|y]] = E
1 #(Dk) Dado que los pares (x, y) son independientes entre ellos, E [xi|y] = E [xi|yi] = µyi.
E [xi|y] 1{yi = k}
(3.71)
i=1
(cid:34)
n (cid:88)
(cid:35)
Por lo tanto,
E[ˆµk] = E
(cid:34)
µk #(Dk)
n (cid:88)
i=1
(cid:35)
1{yi = k}
= µk
(3.72)
58
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
Repitiendo la misma idea con las covarianzas se observa
E[ ˆΣk] = E[E[ ˆΣk|y]] = E
(cid:34)
1 #(Dk) − 1
i=1
n (cid:88)
E (cid:2)(xi − ˆµk)(xi − ˆµk)T |y(cid:3) 1 {yi = k}
(cid:35)
(3.73) donde el producto dentro de la esperanza puede reescribirse como (xi− ˆµk)(xi− ˆµk)T = xixT i − xi ˆµT k . La esperanza de cada uno de estos t´erminos puede escribirse como: E[xixT
k − ˆµkxT
i + ˆµk ˆµT
(3.74)
i |y] = Σyi + µyiµT yi 1 #(Dk)
k |y] =
n (cid:88)
j=1
E[xi ˆµT
E[xixT
j |y]1 {yj = k}
=
E[ˆµkxT
i |y] =
E (cid:2)ˆµk ˆµT
k |y(cid:3) =
1 #(Dk) 1 #(Dk) 1 #(Dk)2
(cid:0)Σk + µkµT
k + (#(Dk) − 1)µyiµT k
(cid:0)Σk + µkµT
k + (#(Dk) − 1)µkµT yi
n (cid:88)
n (cid:88)
i=1
j=1
E[xixT
j |y]1 {yi = yj = k}
(cid:1)
(cid:1)
(3.75)
(3.76)
(3.77)
(3.78)
=
1 #(Dk)2
(cid:0)#(Dk)(Σk + µkµT
k ) + (#(Dk)2 − #(Dk))µkµT k
(cid:1)
(3.79)
Teniendo en cuenta los signos y la indicadora, cuando se haga la suma en (3.73), el producto µkµT k se cancelar´a ya que aparecer´a la misma cantidad de veces sumando que restando. En cambio, la covarianza Σk aparecer´a #(Dk) − 1 veces, y por lo tanto, el valor esperado de cada covarianza es E[ ˆΣk] = Σk.
Por ´ultimo, para el caso de LDA, supongamos que X|Y =k ∼ N (µk, Σ) y Y ∼ Cat(c1, · · · , cK). En este caso, las verdaderas covarianzas son iguales pero los estimadores ˆΣk son distintos. Los mismos se combinan como:
E[ ˆΣ] =
1 n − K
K (cid:88)
k=1
E
(cid:104) (#(Dk) − 1) ˆΣk
(cid:105)
(3.80)
Repitiendo de forma an´aloga al procedimiento anterior para (#(Dk)−1) ˆΣk se finaliza la demostraci´on:
E[ ˆΣ] =
1 n − K
K (cid:88)
k=1
E [(#(Dk) − 1)] Σ =
Σ = Σ
(3.81)
(cid:80)K
k=1 (nck − 1) n − K

## 3.5. Vecinos m´as Cercanos

Los algoritmos descriptos hasta el momento se denominan modelos param´etricos por asumir una familia para ˆP (y|x) indexada por medio de par´ametros. En contraposici´on, se definen los modelos no param´etricos a los algoritmos cuyos modelos no est´an definidos
59
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
ˆP (y|x)
4NN 1NN
x
(a)
(b)
Figura 3.9: Soluciones t´ıpicas del problema de KNN. (a) Frontera de decisi´on (hard ), y (b) probabilidades estimadas (soft).
por par´ametros. Un ejemplo de este tipo de algoritmos es el histograma presentado en la Sec. 1.2.1, el cu´al estima distribuciones en general fuera del paradigma de clasificaci´on.
La adaptaci´on habitual del histograma a problemas de clasificaci´on es bastante inmediata: Se modela ˆP (y) con su distribuci´on emp´ırica y ˆp(x|y) como una densidad constante por regiones (al igual que el histograma). Es decir, ˆP (y) = Ny donde Ny es la cantidad ntr de muestras correspondientes a la clase y-´esima y ntr la cantidad total de muestras de entrenamiento, y ˆp(x|y) = Ky Ny·V donde V es el volumen de la regi´on a la que pertenece el valor x y Ky la cantidad de muestras, etiquetadas como y, que pertenecen en dicha regi´on. Luego la probabilidad condicional (decisi´on soft) es de la forma:
ˆP (y|x) =
(cid:80)
ˆP (y)ˆp(x|y)
ˆP (k)ˆp(x|k)
k∈Y
=
Ky K
(3.82)
donde K = (cid:80) y∈Y Ky es la cantidad de muestras totales pertenecientes a la regi´on en cuesti´on. El resultado es esperable, la probabilidad se modela como una proporci´on de muestras de cada clase en la regi´on.
El algoritmo no param´etrico m´as sencillo se conoce como K−vecinos m´as cercanos (KNN, K−nearest neighbors) [3, Secci´on 4.4]. Mientras que el histograma prefija el volumen de las celdas V y computa la cantidad de muestras que caen en esa celda K, el m´etodo de KNN prefija la cantidad de vecinos y adapta el tama˜no de las celdas. Es decir, para computar (3.82) simplemente analizar la proporci´on de etiquetas en los K−vecinos m´as cercanos.
Por el lado de las decisiones hard, la frontera de decisi´on en este tipo de problemas se ˆP (y|x) =
puede definir por la clase mayoritaria dentro del vecindario φ(x) = arg maxy
60
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
ˆP (y|x)
0.5
0.5
1
1.5
2
2.5
x
Figura 3.10: Probabilidades estimadas para el Ej. 3.5.
arg maxy Ky. Un ejemplo habitual de frontera de decisi´on puede verse en la Fig. 3.9a. En cambio, las decisiones soft se puede ver que las probabilidades solo podr´an tomar valores posibles k K con k ∈ {0, · · · , K}. Un ejemplo habitual de estas probabilidades estimadas puede verse en la Fig. 3.9b, donde se puede observar la diferencia entre un algoritmo 1NN y 4NN. Un ejemplo de uso de este tipo de algoritmos puede verse a continuaci´on.
Ejemplo 3.5 Graficar ˆP (1|x) para una clasificaci´on binaria mediante un algoritmo 2NN cuyos datos de entrenamiento pueden verse en la siguiente tabla.
X 1.2
0.2
2.3
0.4
2.0
1.6
1.0
2.5
2.7
Y
0
1
0
0
0
1
1
1
1
Este tipo de ejemplos son ideales para terminar de comprender los detalles del algoritmo. Se recomienda comenzar el ejercicio ubicando las muestras sobre el eje de las abscisas como se muestra en la Fig. 3.10, en este caso en rojo las de y = 0 y en azul las de y = 1. Para comprender como se forma la estimaci´on ˆP (y|x) tomemos x = 0.5 como ejemplo. Las muestras m´as cercanas son x = 0.4 (etiquetada como y = 0) y x = 0.2 (etiquetada como y = 1). En este caso 1 de 2 muestras poseen etiqueta 1 y por lo tanto ˆP (1|0.5) = 1 2.
Generalizando esta metodolog´ıa a cualquier x ∈ R, podemos observar que para x negativos, los dos vecinos m´as cercanos corresponden a etiquetas diferentes ( ˆP (1|0.5) = 1 2). El foco debe colocarse en que valores hacen modificar esta probabilidad. A medida que se va incrementando x, se alcanza un punto donde la muestra de x = 0.2 deja de ser uno de los dos vecinos m´as cercanos y lo reemplaza x = 1, pero junto con x = 0.4 siguen siendo dos
61
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
(a)
(b)
Figura 3.11: Soluciones t´ıpicas al problema de SVM. (a) Versi´on est´andar, y (b) con m´argenes relajados.
vecinos de etiquetas diferentes. Este comportamiento cambia a partir de que los vecinos m´as cercanos sean x = 2 y x = 2.3 ambos con etiquetas y = 0 y por lo tanto ˆP (1|0.5) = 0. Esta tendencia se da cuando la muestra x = 2.3 est´a m´as cerca que la de x = 1.6, es decir cuando x > 1.6+2.3 2 = 1.95. La tendencia vuelve a cambiar cuando la muestra de x = 2.5 se vuelve m´as cercana que la de x = 2, lo cu´al ocurre a partir de x > 2.25 (etiquetas diferentes). El ´ultimo cambio se da cuando los dos vecinos comienzan a tener etiqueta y = 1, lo cu´al ocurre a partir de x > 2.5. La probabilidad estimada puede verse en la Fig. 3.10.

## 3.6. M´aquina de Vectores Soporte

La m´aquina de vectores soporte (support vector machine o SVM), es un algoritmo de aprendizaje supervisado con un enfoque diferente a otros m´etodos previamente mencionados. Su criterio de optimalidad se basa en maximizar el m´argen resultante entre las muestras y la frontera de decisi´on.

### 3.6.1. SVM est´andar

Supongamos un problema de clasificaci´on binaria y ∈ {−1, 1}, en el cu´al se propone una frontera de decisi´on lineal con ecuaci´on z(x) = wT · x + b = 0. Esta parametrizaci´on permite clasificar una muestra a partir de φ(x) = SIGNO[z(x)] (si bien este planteo no
62
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
tiene una estructura probabil´ıstica, se puede considerar a z(x) como una clasificaci´on soft).
Una muestra aleatoria se dice linealmente separables si existe una soluci´on lineal que separa perfectamente las muestras de ambas clases (error de entrenamiento nulo). Matem´aticamente esto se traduce en y · z(x) > 0 para toda muestra de entrenamiento (x, y). La versi´on est´andar de SVM busca encontrar la frontera ´optima para los conjuntos de datos que poseen esta caracter´ıstica. En este contexto, se define fi(w, b) = yiz(xi) > 0 para todo 1 ≤ i ≤ ntr. En la Fig. 3.11a puede verse un ejemplo de clasificaci´on con el criterio de SVM para el tipo de problema descripto anteriormente.
Algunos razonamientos son necesarios para expresar el problema de maximizar el m´argen en t´erminos matem´aticos. Por un lado, la ecuaci´on z(x) = wT · x + b = 0 define un hiperplano cuya direcci´on normal es w y por lo tanto este vector es ortogonal a la frontera. Sea x∗ la proyecci´on ortogonal de x sobre la frontera, es f´acil notar que w es paralelo a (x − x∗) y por lo tanto:
|wT (x − x∗)| = ∥w∥ · ∥x − x∗∥
(3.83)
Por otro lado, z(x∗) = 0 ya que x∗ pertenece a la frontera y por lo tanto z(x) = z(x) − z(x∗) = wT (x − x∗). Esto nos permite expresar la distancia entre la muestra i-´esima y la frontera ∥xi − x∗∥ como:
∥xi − x∗∥ =
|wT (xi − x∗)| ∥w∥
=
|z(xi)| ∥w∥
=
yi · z(xi) ∥w∥
=
fi(w, b) ∥w∥
(3.84)
donde se utiliz´o que las muestras son linealmente separables. Se define el margen unilateral m(w, b) como un criterio de peor caso para la distancia entre la muestra y la frontera:
m(w, b) = m´ın 1≤i≤ntr
fi(w, b) ∥w∥
=
fk(w, b) ∥w∥
(3.85)
donde k es el ´ındice ´optimo para esa minimizaci´on (y por lo tanto ser´a funci´on de w y b). Un primer criterio de optimalidad de SVM consiste en:
m´ax w,b
m(w, b)
s.t.
fi(w, b) > 0 ∀ 1 ≤ i ≤ ntr
(3.86)
Sea α > 0, esta claro que la regla de decisi´on z(x) ≷ 0 (o el clasificador φ(x) = SIGNO[z(x)]) no se ve afectada si se reescalan consistentemente los par´ametros w ← αw y b ← αb. Esto mismo ocurre con el margen unilateral, quien es invariante a este tipo de cambio de escala m(αw, αb) = m(w, b). Este fen´omeno est´a denotando la caracter´ıstica no identificable del modelo (v´ease Secci´on 3.2.2): hay infinitas maneras posibles de describir una soluci´on. SVM toma esta caracter´ıstica y la utiliza para simplificar el problema, resaltando que fk(αw, αb) = αfk(w, b). Se elegir´a entonces una escala tal que fk(w, b) = 1, logrando un margen de m(w, b) = 1
∥w∥ y un fi(w, b) ≥ 1 para todo 1 ≤ i ≤ n.
63
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
Las muestras donde fi(w, b) = 1 (yi(wT · x + b) = 1), se denominan vectores soportes. Tal como se puede ver en la Fig. 3.11a, estas muestras son las que tocan el margen, volvi´endose un soporte para toda la regla de decisi´on (la cual queda definida solo por ellas). Tienen la caracter´ıstica de tener al menos una por clase. De esta manera, el problema (3.86) se puede reescribir (monoton´ıa mediante) como:
m´ın w,b
1 2
∥w∥2
s.t.
yi(wT · xi + b) ≥ 1 ∀ 1 ≤ i ≤ ntr
(3.87)
El problema (3.87) se conoce como problema primal de SVM est´andar y es un ejemplo de un problema de optimizaci´on cuadr´atica. En la pr´actica suele implementarse una versi´on alternativa del problema conocida como problema dual por otorgar ciertas ventajas; m´as adelante se explorar´a esta equivalencia.
La versi´on est´andar de SVM tiene algunas limitaciones: es muy sensible a outliers (por ser un criterio de peor caso), solamente permite soluciones lineales y resuelve ´unicamente el problema de clasificaci´on binaria. Estas limitaciones son un inconveniente en la vida real, por lo que se suelen solucionar emparchando la versi´on est´andar. Es decir, se plantean peque˜nas variantes al problema con el fin de mitigar dichos inconvenientes.

### 3.6.2. Parches

En primer lugar, se plantea una variante donde se permita la penetraci´on de muestras dentro del margen. Esto permite insensibilizar un poco a la frontera de decisi´on frente a un outlier. La Fig. 3.11b muestra una soluci´on con m´argenes relajado a modo de ejemplo. Esto se logar redefiniendo el problema primal (3.87) de la siguiente manera:
m´ın w,b,ξ1,··· ,ξntr
1 2
∥w∥2 + C
ntr(cid:88)
i=1
ξi
s.t.
 

yi(wT xi + b) ≥ 1 − ξi
ξi ≥ 0
∀ 1 ≤ i ≤ ntr
(3.88)
donde C > 0 es un hiperpar´ametro que controla la penetraci´on de las muestras sobre el margen. El importante resaltar que este problema coincide con (3.87) cuando C → ∞ (lejos de lo que uno podr´ıa pensar a simple vista). Esto ocurre porque un C muy grande obliga a los ξi a tender a cero (notar que los ξi forman parte de las variables a optimizar). En cambio, si se elige un C → 0, no habr´a nada que evite que ξi → ∞, por lo que w → 0. Las variables ξi indican el grado de penetraci´on de cada muestra. Las muestras que respetan los m´argenes cumplen yi(wT xi + b) ≥ 1 (sin necesidad de los ξi), y por lo tanto la minimizaci´on llevar´a estas variables a cero ξi = 0. Un 0 < ξi < 1 indica una muestra que penetr´o el margen pero no traspas´o la frontera (sigue siendo clasificada correctamente), mientras un ξi > 1 indica una muestra clasificada err´oneamente.
Una segunda caracter´ıstica a emparchar es el tema de la linealidad. No siempre este
64
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
tipo de soluciones son adecuadas, sino que adem´as no cualquier conjunto de muestras es linealmente separable. Una soluci´on a este problema es proyectar las muestras sobre un espacio de mayor dimensi´on (quiz´as hasta infinita) o complejidad ϕ(xi), para luego poder separar las clases linealmente:
m´ın w,b
1 2
∥w∥2
s.t.
yi(wT · ϕ(xi) + b) ≥ 1 ∀ 1 ≤ i ≤ ntr
(3.89)
donde eligiendo adecuadamente esa transformaci´on ϕ(·), se puede reconfigurar el problema para que finalmente sea linealmente separable.
Como tercer parche surge la necesidad de adaptar este algoritmo a una tarea de clasificaci´on categ´orica. Existen dos maneras cl´asicas de adaptar algoritmos de clasificaci´on binaria a mayor cantidad de clases, ambos basados en la idea de entrenar muchos clasificadores binarios en paralelo.
one-vs-one: Se entrenan clasificadores binarios, teniendo en cuenta todas las combinaciones de pares de clases. Esto hace un total de K(K−1) clasificadores. La clasificaci´on final se efect´ua seleccionando a la clase con m´as votos.
2
one-vs-the-rest: Se entrenan K clasificadores binarios, donde cada uno toma una clase como positiva y el resto como negativa. Se clasifica seg´un φ(x) = arg m´ax k ϕ(x)+ bk.
wT
k
Mientras que one-vs-one tiene la ventaja de soler alcanzar el mejor desempe˜no, por probar todas las combinaciones, tiene la desventaja de necesitar repetir mayor cantidad de veces el entrenamiento O(K 2). En cambio, one-vs-the-rest, si bien suele ser sub´optimo, necesita solamente K entrenamientos.
Finalmente, como ´ultimo parche, cabe mencionar que este algoritmo puede adaptarse para una tarea de regresi´on. El algoritmo de SVM para regresi´on resuelve el siguiente problema:
m´ın w,b
1 2
∥w∥2
s.t.
|wT · xi + b − yi| ≤ ϵ ∀ 1 ≤ i ≤ ntr
(3.90)
para alg´un ϵ > 0 peque˜no. La condici´on de clases linealmente separables se reemplaza por error absoluto de estimaci´on lineal de a lo sumo ϵ. Es decir, dentro de todas las soluciones lineales con error de entrenamiento9 a lo sumo ϵ, se elige la de menor ∥w∥. Esta idea de elegir par´ametros de norma baja, viene de la mano con combatir el overfitting, tal como se discuti´o en la Sec. 2.4.2.
9Error absoluto y por muestra (criterio de peor caso). No confundir con el error cuadr´atico medio.
65
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial

### 3.6.3. Dualidad en SVM

La dualidad es una de las ideas centrales de la optimizaci´on matem´atica: muchos problemas pueden analizarse desde dos perspectivas complementarias, una “primal”, que describe directamente la tarea a resolver, y otra “dual”, que captura las limitaciones y/o costos asociados a las restricciones. Esta visi´on dual no solo aporta interpretaci´on geom´etrica, sino que tambi´en permite obtener cotas, condiciones de optimalidad y, en numerosos casos, reformular el problema de manera m´as eficiente o m´as f´acil de resolver. En problemas convexos, y bajo hip´otesis adecuadas, ambas perspectivas coinciden exactamente, dando lugar a la llamada dualidad fuerte, fundamento te´orico de numerosos algoritmos modernos en aprendizaje autom´atico y optimizaci´on.
Tomemos el problema est´andar de SVM con la inclusi´on de una transformaci´on ϕ(·)
que permita tipos de fronteras m´as all´a de las lineales (3.89). Llamamos
J1 = m´ın w,b
1 2
∥w∥2
s.t.
yi(wT · ϕ(xi) + b) ≥ 1 ∀ 1 ≤ i ≤ ntr
(3.91)
Dicho problema puede reescribirse usando multiplicadores de Lagrange αi (para mayor
informaci´on sobre el tema ver [12, Secci´on 13.7] y [19, Cap´ıtulo 5]):
J1 = m´ın w,b
m´ax αi≥0
1 2
∥w∥2 −
ntr(cid:88)
i=1
αi[yi(wT · ϕ(xi) + b) − 1]
(3.92)
La equivalencia entre (3.91) y (3.92) no es trivial, y requiere una explicaci´on adicional. Es importante notar que si se cumple la condici´on yi(wT ·ϕ(xi)+b) > 1 los multiplicadores que maximicen la expresi´on anterior deber´an ser nulos αi = 0, y si en cambio, la condici´on se da con igualdad yi(wT · ϕ(xi) + b) = 1 el multiplicador αi ser´ıa irrelevante ya que estar´ıa multiplicado por cero. Llegado el caso de que todas las muestras tengan alguna de estas dos caracter´ıstica, las expresiones matem´aticas (3.91) y (3.92) coinciden. Esto ocurrir´a absolutamente siempre, y dicha conclusi´on se puede razonar por el absurdo. Supongamos un par (w, b) que lograra que al menos una de las muestras cumpla yi(wT · ϕ(xi) + b) < 1; esto obligar´ıa a ese multiplicador αi → ∞ y por lo tanto J1 → ∞. Esto nunca se elegir´a pues se busca el (w, b) que minimicen la expresi´on. Por lo tanto, ambas expresiones son equivalentes.
Una importante caracter´ıstica a resaltar es que el multiplicador αi funciona como detector de vectores soportes. Si las muestras cumplen αi > 0 necesariamente deben ser vectores soportes 10.
La soluci´on del problema primal J1 define un problema de optimizaci´on del tipo m´ın − m´ax
10Por cuestiones num´ericas, suele traer complicaciones detectar vectores soportes como αi > 0. En la
pr´actica suele compararse αi > ϵ con ϵ > 0 un n´umero peque˜no.
66
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
con Lagrangiano11:
L ([w, b], [α1, · · · , αntr]) =
1 2
∥w∥2 −
ntr(cid:88)
i=1
αi[yi(wT · ϕ(xi) + b) − 1]
(3.93)
En este contexto, definimos su problema dual como un problema del tipo m´ax − m´ın
para el mismo Lagrangiano:
J2 = m´ax αi≥0
m´ın w,b
1 2
∥w∥2 −
ntr(cid:88)
i=1
αi[yi(wT · ϕ(xi) + b) − 1]
(3.94)
La relaci´on entre J1 y J2 es un problema habitual en la teor´ıa de optimizaci´on. En
particular, el siguiente teorema vincula ambas problem´aticas.
Propiedades 3.5 (Weak and Strongh duality) Sean J1 y J2 definidos como
J1 = m´ın x∈X
m´ax y∈Y
f (x, y),
J2 = m´ax y∈Y
m´ın x∈X
f (x, y)
(3.95)
Luego J1 ≥ J2. En particular, para el problema de SVM con J1 (3.92) y J2 (3.94), si las clases son linealmente separables de forma estricta (con un posible margen no nulo) vale con igualdad J1 = J2.
Demostraci´on 3.6 (Prop. 3.5) Para la primera afirmaci´on, notar que para todo par (x′, y′) ∈ X × Y:
m´ın x∈X
f (x, y′) ≤ f (x′, y′) ≤ m´ax y∈Y
f (x′, y)
(3.96)
Como la desigualdad vale para cualquier par (x′, y′), basta con tomar los extremos
de dicha inecuaci´on y elegir el x′ que minimice y el y′ que maximice:
J2 = m´ax y′∈Y
m´ın x∈X
f (x, y′) ≤ m´ın x′∈X
m´ax y∈Y
f (x′, y) = J1
(3.97)
La segunda parte de la demostraci´on se conoce como dualidad fuerte y su demostraci´on escapa a las pretensiones del presente manuscrito. Se recomienda ver [19, Cap´ıtulo 5].
Al intercambiar al m´ınimo con el m´aximo, el problema se simplifica notoriamente centr´andose, en primer lugar, en la optimizaci´on con respecto a los par´ametros (w, b). En primer lugar se plantea considerar fijos los multiplicadores αi y minimizar el Lagrangiano (3.93), igualando a cero sus derivadas:
∂ ∂w
∂ ∂b
L ([w, b], [α1, · · · , αntr]) = w −
ntr(cid:88)
i=1
αiyiϕ(xi)
L ([w, b], [α1, · · · , αntr]) = −
ntr(cid:88)
i=1
αiyi
(3.98)
(3.99)
11Se denomina Lagrangiano a la funci´on resultante a optimizar una vez incorporados las restricciones
del problema via multiplicadores de Lagrange.
67
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
Sean w∗ y b∗ los valores ´optimos, resultado de igualar a cero las derivadas anteriores. Mientras que de la primera ecuaci´on se deduce el valor de w∗ = (cid:80)ntr i=1 αiyiϕ(xi), la segunda impone una nueva condici´on αT y = 0 con α = (α1, · · · , αn) y y = (y1, · · · , yn). Utilizando estas dos identidades, el Lagrangiano se puede simplificar como:
L ([w∗, b∗], [α1, · · · , αn]) =
1 2
∥w∗∥2 − w∗T ·
n (cid:88)
i=1
αiyiϕ(xi) − b
n (cid:88)
i=1
αiyi +
n (cid:88)
i=1
αi
(3.100)
= αT 1 −
= αT 1 −
= αT 1 −
1 2 1 2
1 2
∥w∗∥2
n (cid:88)
n (cid:88)
i=1
j=1
αT Qα
αiαjyiyjϕ(xi)T ϕ(xj)
(3.101)
(3.102)
(3.103)
donde Q ∈ Rntr×ntr es una matriz cuyos coeficientes son Qi,j = yiyjϕ(xi)T ϕ(xj). Finalmente, J2 puede escribirse como:
J2 = m´ax
α
αT 1 −
1 2
αT Qα s.t. αT y, αi ≥ 0 ∀ 1, · · · , ntr
(3.104)
Una caracter´ıstica importante a resaltar es el hecho de que el problema pueda reducir su complejidad mediante el prec´omputo de los vectores soporte, ya que el ´unico t´ermino a computar previo a la optimizaci´on es Q. Sea S el conjunto de ´ındices de vectores soportes, αi = 0 para todo i ̸∈ S y por lo tanto:
αT Qα =
(cid:88)
(cid:88)
i∈S
j∈S
αiαjyiyjk(xi, xj)
(3.105)
donde k(xi, xj) = ϕ(xi)T ϕ(xj) se denomina kernel k : Rdx × Rdx → R. Esto implica que para entrenar solo es necesario computar esta magnitud entre los vectores soportes. Adem´as, el planteo dual permite generalizar el problema a cualquier tipo de kernel: no es relevante conocer ni el valor de ϕ(x) ni el valor de w∗, pudiendo estos tener dimensi´on infinita y nunca ser computados. Esto ocurre tambi´en para el c´omputo del bias b∗, ya que para todo i ∈ S debe ocurrir que yi(w∗T ϕ(xi) + b∗) = 1. En teor´ıa bastar´ıa conocer un solo vector soporte para poder despejar b∗, pero en la pr´actica se suele tomar el promedio para mitigar errores num´ericos:12
b∗ =
1 NS
(cid:88)
i∈S
(cid:0)yi − w∗T ϕ(xi)(cid:1) =
(cid:32)
1 NS
(cid:88)
i∈S
yi −
(cid:88)
j∈S
(cid:33)
αjyjk(xi, xj)
(3.106)
donde NS representa la cantidad de vectores soportes. Este comportamiento tambi´en se da durante las predicciones (validaci´on, testeo, etc.), ya que la clasificaci´on tanto a nivel
12Notar que 1 yi
= yi ya que yi ∈ {−1, 1}.
68
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
soft z(x) como a nivel hard φ(x) = SIGNO[z(x)] cumple:
z(x) = w∗T ϕ(x) + b∗ =
ntr(cid:88)
i=1
αiyiϕ(xi)T ϕ(x) + b∗ =
(cid:88)
i∈S
αiyik(xi, x) + b∗
(3.107)
donde solamente es necesario computar el kernel entre el vector a predecir y los vectores soportes. Este tipo de estructuras donde solamente se necesitan computar el kernel en pocas muestras se denomina sparse [20, Cap´ıtulo 7]. Si bien el problema primal puede o no ser m´as dif´ıcil (computacionalmente) de resolver que el dual, este ´ultimo tiene la ventaja de tener su estructura sparse (y por lo tanto aliviar las predicciones) y de poder utilizar funciones ϕ(·) de dimensi´on infinita (ya que no necesitan ser calculadas).
Algunos de los kernel m´as utilizados en la pr´actica son:
Lineal: k(x, x′) = xT x′.
Polin´omico: k(x, x′) = (cid:0)γ · xT x′ + r(cid:1)d (con valores prefijados de γ, r y d).
RBF o gaussiano: k(x, x′) = e−γ∥x−x′∥2 (con γ prefijado).

## 3.7.


## ´Arboles de Decisi´on

Es habitual en la bibliograf´ıa referirse a la mayor´ıa de los algoritmos de inteligencia artificial como cajas negras. Esta idea est´a relacionada con preguntarse sobre como un algoritmo razona, y por lo tanto va de la mano con el tipo de terminolog´ıa usada en el ´area. Desde t´erminos cl´asicos en la tem´atica como aprendizaje, entrenamiento o neurona hasta m´as modernos como inteligencia artificial o mecanismo de atenci´on, el marketing de los algoritmos trata de humanizar los diferentes procedimientos presentes en los mismos. Reflexionar sobre esta caracter´ıstica no solo deja de manifiesto que la inteligencia artificial no tiene tanto de inteligencia como uno puede suponer, sino que quiz´as tampoco tiene mucho de artificial. No es para nada artificial la inversi´on en tecnolog´ıa que recibi´o el ´area en las ´ultimas d´ecadas, ya que el exceso de humanizaci´on en los t´erminos usados refiere a una b´usqueda por cierta parte de la sociedad. Adem´as de ser una nueva pieza de tecnolog´ıa es un negocio muy rentable para algunas personas.
Intentando dejar de lado la parte sem´antica de la cuesti´on, tiene algo de cierto que a pesar de conocer perfectamente el riesgo emp´ırico minimizado durante el entrenamiento por los algoritmos, no contamos con una interpretaci´on conceptual sobre la relaci´on entre los valores de los par´ametros y las reglas de decisi´on resultante. En este sentido utilizaremos la idea de caja negra, siempre teniendo en cuenta lo relativo de los t´erminos que utilizamos para referirnos a los diferentes procesos. Utilizar un algoritmo para resolver una tarea es importante, pero imaginemos el potencial de abrir el algoritmo y entender
69
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
x2
t3
t2
B
A
E
x1 ≤ t1
C
D
x2 ≤ t2
x2 ≤ t3
A
B
x1 ≤ t4
E
t1
(a)
t4
x1
C
D
(b)
Figura 3.12: Gr´aficos CART. (a) Frontera de decisi´on; y (b) diagrama de ´arbol (por convenci´on, si la condici´on se cumple se va hacia la izquierda).
los por menores de su razonamiento. Si hay algo de emular el comportamiento humano en la inteligencia artificial, quiz´as mirando el algoritmo nos veamos a nosotros mismos.
Con esta idea es que surgen los arboles de clasificaci´on y regresi´on (CART, por sus siglas en ingl´es Clasification And Regression Trees). Restringiendo las posibles reglas de decisi´on a cuadr´ıculas, como puede verse la Fig. 3.12a, el algoritmo resultante puede graficarse con un diagrama de ´arbol donde cada nodo puede expresarse como la comparaci´on de uno de los predictores (x1 o x2 en este caso) contra un umbral. Un posible diagrama de ´arbol para la frontera de decisi´on mencionada13 puede verse en la Fig. 3.12b, donde por convenci´on se interpreta que satisfacer la condici´on implica un desplazamiento hacia la izquierda.
Se denomina ra´ız al nodo originario del ´arbol (en la Fig. 3.12b es el nodo que eval´ua si x1 ≤ t1), y hojas a los nodos terminales (A, B, C, D y E en este ejemplo). El entrenamiento consiste en aprender, para cada nodo m que no sea hoja, el ´ındice jm del predictor y el valor del umbral tm para el cu´al se comparar´a xjm ≤ tm. Una vez entrenado, la decisi´on final en un problema de clasificaci´on consistir´a en elegir la clase m´as frecuente en entrenamiento para cada hoja. En el caso de una tarea de regresi´on, el valor promedio de las etiquetas de cada hoja.
Matem´aticamente, el problema de optimizaci´on a resolver durante el entrenamiento puede modelarse calculando jm y tm para cada nodo. Sea Qm al conjunto de datos supervisado de entrenamiento presentes en el nodo m−´esimo, se definen los subconjuntos de
13Cada ´arbol representa una frontera, pero cada regla de decisi´on puede graficarse con varios diagramas
de ´arbol. La relaci´on no es biyectiva.
70
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
datos a izquierda QL
m(jm, tm) y QR QL
m(jm, tm) como:
m(jm, tm) = {(x, y) ∈ Qm : xjm ≤ tm} m(jm, tm) = {(x, y) ∈ Qm : xjm > tm}
QR
(3.108)
(3.109)
Con estos subconjuntos se define el problema de optimizaci´on a resolver (j∗
m, t∗
m) =
arg m´ın jm,tm
Gm(jm, tm), con
Gm(jm, tm) =
# (cid:0)QL
m(jm, tm)(cid:1) # (Qm)
H(QL
m(jm, tm)) +
# (cid:0)QR
m(jm, tm)(cid:1) # (Qm)
H(QR
m(jm, tm)) (3.110)
donde H(Q) es la funci´on impureza del conjunto de datos Q. Es razonable pensar que la impureza a izquierda pese poco si la proporci´on de muestras hacia ese lado es baja. Notar que Gm(jm, tm) es una m´etrica probabilista del la impureza posterior a la separaci´on del conjunto. Las funciones impurezas mide que tan desconcentrado es un nodo. Es razonable pensar entonces que si todas las muestras presentes en un nodo tienen la misma etiqueta, la impureza sea nula. De la misma manera, la impureza es m´axima cuando las proporciones son uniformes. Las funciones m´as habituales en problemas de clasificaci´on son la entrop´ıa y impureza de Gini, definidas como:
Gini: H(Q) = (cid:80)
k pk(1 − pk).
Entrop´ıa: H(Q) = (cid:80)
k −pk log2(pk).
donde pk hace referencia a la proporci´on emp´ırica en el conjunto de datos de la clase k−´esima. A continuaci´on se mostrar´a el comportamiento de estas m´etricas para un problema de clasificaci´on binaria.
Ejemplo 3.6 Para un conjunto de datos de dos clases de proporciones p y 1 − p, graficar las diferentes impurezas en funci´on de p.
Impureza de Gini: En este caso, la funci´on impureza toma el valor H(Q) = p(1 − p) + (1 − p)p = 2p(1 − p). Es una par´abola c´oncava que alcanza su valor m´aximo en p = 1
2. El gr´afico puede verse en la Fig. 3.13a.
2 y vale 1
dp = − log(p)+log(1−p)
Entrop´ıa: En este caso, la funci´on impureza puede escribirse, usando logartimos naturales, como H(Q) = −p log(p)−(1−p) log(1−p) . Derivando esta funci´on se observa que (cid:16) 1 dH(Q) p + 1
< 0. Se observa tambi´en un comportamiento c´oncavo (segunda derivada negativa) cuyo valor m´aximo se alcanza (cuando la derivada se anula) en p = 1 2 y vale 1. El gr´afico puede verse en la Fig. 3.13b.
dp2 = − 1
y d2H(Q)
log(2)
log(2)
log(2)
1−p
(cid:17)
71
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
Gini
0.5
Entrop´ıa
1
p
1
0.5
(a)
p
1
0.5
(b)
Figura 3.13: Funciones impureza para un problema de clasificaci´on binaria. (a) Impureza de Gini; y (b) Entrop´ıa.
La implementaci´on habitual de este tipo de algoritmos suele encontrar el ´optimo valor de Gm(jm, tm) por prueba y error. Cabe resaltar que este algoritmo no utiliza gradiente descendente, por lo que no posee problemas de convergencia. Adem´as, al comparar de a un predictor por vez, no tiene sentido normalizar los datos para este tipo de algoritmos. En el caso de un problema de regresi´on, el procedimiento es similar. Un ´arbol para este tipo de problemas asume una funci´on regresi´on constante por regiones. Las predicciones se efect´uan asignando el valor promedio de la hoja y la impureza utilizada es el error cuadr´atico medio:
H(Qm) =
(cid:88)
(y − φ(x))2
(3.111)
(x,y)∈Qm con φ(x) el valor promedio de las y−s correspondientes a la hoja a la que pertenece x.
Una de las caracter´ısticas m´as interesantes de los ´arboles, es que nos permite ponderar a los predictores pudiendo identificar cuales son importantes y cuales no. Esta din´amica rompe el fen´omeno de caja negra, d´andonos informaci´on sobre que variables son relevantes y cuales pueden ser omitidas. Se denomina Feature Importance de un predictor, a la suma de las ganancias (en impureza), de cada nodo (∆m) donde se haya utilizado dicho predictor para separar el conjunto con ∆m = H(Qm) − Gm(j∗ m). Habitualmente el resultado se expresa normalizado para que sumen 1.
m, t∗
Otra caracter´ıstica importante a tener en cuenta es cuando finalizar el ´arbol. Se llama ´arbol maximal al desarrollo del ´arbol hasta que todas las etiquetas del conjunto de entrenamiento de cada hoja sean iguales. B´asicamente cuando un nodo posee impureza nula se lo interpreta como hoja. El problema con los ´arboles maximales es el overfitting, ya que genera reglas muy dependientes del conjunto de entrenamiento. Alternativas para
72
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
x0 ≤ 0.349 gini = 0.58 [5, 4, 1]
x1 ≤ 1.649 gini = 0.5 [1, 4, 1]
gini = 0 [4, 0, 0]
x0 ≤ −0.942 gini = 0.32 [0, 4, 1]
gini = 0 [1, 0, 0]
x0 ≤ 0.349 gini = 0.58 [5, 4, 1]
x1 ≤ 1.649 gini = 0.5 [1, 4, 1]
gini = 0 [4, 0, 0]
gini = 0 [0, 2, 0]
x0 ≤ −0.44 gini = 0.444 [0, 2, 1]
x0 ≤ −0.942 gini = 0.32 [0, 4, 1]
gini = 0 [1, 0, 0]
gini = 0 [0, 0, 1]
gini = 0 [0, 2, 0]
gini = 0 [0, 2, 0]
gini = 0.444 [0, 2, 1]
(a) T1
x0 ≤ 0.349 gini = 0.58 [5, 4, 1]
(b) T2
x1 ≤ 1.649 gini = 0.5 [1, 4, 1]
gini = 0 [4, 0, 0]
x0 ≤ 0.349 gini = 0.58 [5, 4, 1]
gini = 0.32 [0, 4, 1]
gini = 0 [1, 0, 0]
gini = 0.5 [1, 4, 1]
gini = 0 [4, 0, 0]
(c) T3
(d) T4
gini = 0.58 [5, 4, 1]
(e) T5
Figura 3.14: Ejemplo de podado de ´arbol. (a) T1: ´Arbol maximal de 5 hojas, (b) T2: sub´arbol de 4 hojas, (c) T3: sub´arbol de 3 hojas, (d) T4: sub´arbol de 2 hojas, (e) T5: sub´arbol de 1 hoja.
73
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
evitar este problema es preestablecer la profundidad m´axima o prohibir la separaci´on en nodos con pocas muestras (menor a un n´umero prefijado). Sin embargo, la mejor manera de mitigar este problema es podando el ´arbol maximal.

### 3.7.1. Podado

Sea T un ´arbol determinado, L(T ) su respectivo conjunto de hojas y α el hiperpar´ametro de complejidad (multiplicador que regular´a la poda). Se denomina medida de costocomplejidad a
Hα(T ) =
(cid:88)
m∈L(T )
#(Qm) ntr
· H(Qm) + α · #(L(T ))
(3.112)
La poda se basa en quedarse con el sub´arbol del ´arbol maximal de menor costocomplejidad. B´asicamente, (3.112) consiste en definir un costo regularizado, tomando como t´ermino principal la impureza de las hojas (suma ponderada teniendo en cuenta la proporci´on) e incorporando una penalizaci´on a los ´arboles grandes. Para fijar ideas analicemos un ejemplo concreto.
Ejemplo 3.7 Sea el ´arbol de decisi´on maximal presentado en la Fig. 3.14a.
1. Indicar todos los posibles sub´arboles.
2. Indicar el costo-complejidad para cada sub´arbol, como funci´on de α.
3. Elegir el sub´arbol de menor costo-complejidad para α = 0.1 e indicar la feature
importance.
En la Fig. 3.14a se muestra un ´arbol maximal para una tarea de clasificaci´on de 3 clases. En colores se resaltan las hojas, utilizando un color diferente para la clase mayoritaria seg´un corresponda. Se indica condici´on de separaci´on, impureza de Gini y cantidad de muestras que llegan al nodo (ntr = 10). Mientras que el ´arbol maximal T1 posee 5 hojas, en las Figs. T2 3.14b, T3 3.14c, T4 3.14d y T5 3.14e representan sub´arboles de 4, 3, 2 y 1 hoja respectivamente. En total hay 5 opciones de ´arboles (se analizaron todos los sub´arboles posibles), y se buscar´a elegir el de menor costo-complejidad. Teniendo en cuenta la proporci´on de muestras de cada hoja, el costo complejidad Hα(T ) toma los siguientes valores dependiendo del valor de α :
Hα(T1) = 0 + 5α.
Hα(T2) = 0.13 + 4α.
Hα(T3) = 0.16 + 3α.
74
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
Figura 3.15: Costo-complejidad en funci´on del hiperpar´ametro de complejidad α para los diferentes sub´arboles.
Hα(T4) = 0.3 + 2α.
Hα(T5) = 0.58 + α.
Mientras que el ´arbol maximal T1 no posee impurezas, recibe la mayor penalizaci´on debido a su tama˜no. Este ser´a el indicado para valores de α muy bajos. En contraste, el sub´arbol T5 de un solo nodo posee la penalizaci´on m´as baja, pero su impureza se corresponde a la del nodo ra´ız. Ser´a el indicado para valores de α muy grandes. En la Fig. 3.15 puede verse las diferentes funciones costo-complejidad Hα(T ) en funci´on del hiperpar´ametro de complejidad α para los diferentes sub´arboles.
Es interesante notar como el sub´arbol T2 no minimiza el costo-complejidad para ning´un valor de α. Esto mismo ocurre siempre que hay dos sub´arboles distintos con la misma cantidad de hojas (las rectas son paralelas). Eso quiere decir que, detect´andolo de antemano, se puede reducir la cantidad de candidatos a sub´arbol ´optimo. Esto reduce significativamente el costo computacional de una potencial etapa de validaci´on.
En particular, para α = 0.1 el ´arbol ´optimo es T3. Para el c´omputo de la feature importance notar que hay un solo nodo de separaci´on utilizando x0 (se llamar´a nodo 0) y uno solo utilizando x1 (se llamar´a nodo 1). Sus impurezas son 0.58 y 0.5 respectivamente. Finalmente se calcula las ganancias:
75
Cap´ıtulo 3. Clasificaci´on en Inteligencia Artificial
∆0 = H(Q0) − G0(0, 0.349) = 0.58 −
(cid:18) 6 10
· 0.5 +
∆1 = H(Q1) − G1(1, 1.649) = 0.5 −
(cid:18) 5 6
· 0.32 +
4 10 1 6
· 0
= 0.28
(3.113)
(cid:19)
· 0
(cid:19)
= 0.233
(3.114)
Normalizando para que sumen 1, la importancia de cada predictor es 0.546 y 0.454
respectivamente.

### 3.7.2. Bosques Aleatorios

Los ´arboles de decisi´on no son solamente algotimos cuya funci´on es romper el esquema de caja negra, sino que fueron estado de arte en muchas aplicaciones durante mucho tiempo, incluso en algunas tareas lo siguen siendo. Su limitante principal son los problemas de overfitting, que incluso con podando puede ser muy relevante. Es entonces cuando surge la idea de sacrificar interpretabilidad de resultados en pos de mejorar el desempe˜no.
Los bosques aleatorios son un algoritmo capaz de logar esto. Est´an basados en un principio llamado Bagging: Entrenar m´ultiples algoritmos y decidir por mayor´ıa o promedio (en clasificaci´on o regresi´on respectivamente). Un algoritmo de m´ultiples ´arboles se llama bosque. Sean Y1, · · · , YB la predicci´on de B−algoritmos de la misma media E[Yb] = µ y la misma varianza var(Yb) = σ2, se puede notar que: 1 1 B B
(3.115)
σ2 B
B (cid:88)
B (cid:88)
= µ,
var
Yb
Yb
(cid:33)
(cid:32)
=
E
(cid:35)
(cid:34)
b=1
b=1
El promediado de resultados permite mantener el resultado medio mientras se reduce
la varianza14.
Una segunda cuesti´on a tener en cuenta a la hora de utilizar bosques, es como aleatorizar los algoritmo de manera que no se est´e promediando B ´arboles iguales. Habitualmente los ´arboles aleatorios lo hace con dos decisiones aleatorias. La primera consiste en no utilizar todos los dx predictores en todos los ´arboles sino que seleccionar al azar aproximadamente √ dx por ´arbol, fomentando as´ı que los ´arboles resultantes sean distintos. La segunda
aleatoridad consiste en utilizar una t´ecnica llamada Boostrap.
Boostrap consiste en utilizar datos diferentes en cada ´arbol. Para ello se generan B conjuntos de datos del mismo tama˜no que el conjunto de datos original ntr. La manera de armar estos conjuntos es eligiendo al azar ntr datos del conjunto original con reposici´on. Es interesante notar que la probabilidad de que un dato particular no forme parte de un conjunto es de ≈ 37 %. Esto puede observarse aplicando el siguiente l´ımite:
(cid:19)ntr
(cid:18)
1 −
1 ntr
→ e−1
(3.116)
14En clasificaci´on, si se piensan etiquetas en codificaci´on one-hot, promediar para luego elegir el m´aximo
equivale a elegir la respuesta mayoritaria.
76

# 4


# Aprendizaje no Supervisado

Los datos son la materia prima de la inteligencia artificial. Sacarle el mayor provecho posible a los mismos es el objetivo. No se puede dar el lujo de desperdiciar nada. Ah´ı radica el verdadero potencial de estos algoritmos.
En los Cap´ıtulos 2 y 3 se han estudiado algoritmos de aprendizaje supervisado. Es decir, dado un conjunto de datos {(xi, yi)}ntr i=1 entrenar un modelo que permita inferir Y a partir de X. El problema con este enfoque es que no permite utilizar los datos x que no tengan asociados su correspondiente etiqueta y. En la era de la informaci´on, el procesamiento de la misma puede ser la clave para la maduraci´on econ´omica competitiva de diferentes aplicaciones e industrias en la ciencia de datos. Cada pieza de informaci´on posee un valor intr´ınseco que no debe ser desaprovechado, lo que vuelve a las bases de datos cada vez m´as grandes. El problema es que la mayor parte de los datos disponibles no est´an etiquetados, y dependiendo de la aplicaci´on, el etiquetado puede ser muy costoso. En ese sentido es esencial utilizar los datos sin etiquetar.
Llamamos aprendizaje no supervisado al aprendizaje efectuado a partir de un conjunto de datos no etiquetados {xi}ntr i=1. Por si solo es muy pretencioso pretender informaci´on sobre una variable Y no observable. Sin embargo, eso no quita que no pueda ser beneficioso inferir algunas caracter´ısticas de X. En particular, se enmarcar´a el aprendizaje no supervisado en la tarea denominada autoencoder [21, Cap´ıtulo 14].
El autoencoder consiste en dos algoritmos, entrenados habitualmente en simult´aneo, llamados encoder o codificador y decoder o decodificador. B´asicamente las entradas X ∈ Rdx se codifican a un espacio latente Z ∈ Z para luego ser decodificados y estimar la variable original ˆX ∈ Rdx. En el caso de que el espacio latente Z sea finito, el problema recibe el nombre de clustering o agrupamiento. En cambio si Z = Rdz con dz < dx hablamos de un problema de manifold learning o reducci´on de dimensi´on.
Cabe destacar que el objetivo del autoencoder no es simplemente reconstruir una variable (que de por si es observable), sino obtener informaci´on sobre la distribuci´on de los datos, sus caracter´ısticas y secretos. En ese sentido, el aprendizaje no supervisado busca entender los datos. En l´ıneas generales, los autoencoders tienen tres tipos de aplicaciones:
Preprocesar los datos para una posterior tarea de regresi´on o clasificaci´on. Por ejem-
77
Cap´ıtulo 4. Aprendizaje no Supervisado
X
Y
{pX, pY |X}
(a)
Y
X
{pY , pX|Y }
(b)
{pXY }
X
Y
(c)
Figura 4.1: Relaciones causales entre variables. (a) Una relaci´on causal; (b) una anticausal; y (c) una relaci´on no causal.
plo, utilizar como entrada de la segunda tarea la variable latente o la reconstrucci´on de un autoencoder.
Resolver un problema espec´ıfico no supervisado por si mismo. Por ejemplo compresi´on de datos con p´erdida de informaci´on o un detector de anomal´ıas.
Interpretar un conjunto de datos. Por ejemplo reducir el espacio de predictores a dos dimensiones para poder visualizarlos o reducirlos a una dimensi´on para representarlos con un solo n´umero.
A continuaci´on se analizar´a la primera de estas aplicaciones. En este problema se necesitan tanto datos no supervisados para entrenar el autoencoder como datos supervisados para entrenar el regresor/clasificador. Este paradigma se conoce como aprendizaje semisupervisado y es de lo m´as habitual en la pr´actica: se cuenta con muchos datos sin etiquetar y unos pocos etiquetados. Pero es importante destacar que mientras que el objetivo del algoritmo supervisado es inferir (parcial o totalmente) la distribuci´on de pY |X=x(y), la del algoritmo no supervisado es hacer lo propio con pX(x). Mejorar el conocimiento de la distribuci´on marginal de X puede o no ser relevante para inferir la condicional Y |X=x. A continuaci´on se analizar´a que condiciones deben cumplirse para considerer relevante una etapa no supervisada para una posterior regresi´on/clasificaci´on.

## 4.1. Causalidad en Aprenizaje Semisupervisado

Determinar si el conocimiento de pX(x) ayuda a inferir pY |X=x(y) escapa al problema probabil´ıstico. En la teor´ıa de probabilidad, cualquier conjunta se puede construir multiplicando pXY (x, y) = pY |X=x(y)pX(x), denotando que pueden tener naturalezas totalmente diferentes. Para saber si este es el caso o no, hay que adentrarse m´as profundamente en el problema y analizar el modelo f´ısico subyacente que gener´o las variables. Es necesario adentrarse en la teor´ıa de causalidad.
La cantidad de lluvia y la cantidad de paraguas abiertos en una plaza son variables estad´ısticamente correlacionadas. Pero mientras que aumentar el nivel de la lluvia suele
78
Cap´ıtulo 4. Aprendizaje no Supervisado
aumentar la cantidad de paraguas, aumentar la cantidad de paraguas abiertos no aumenta el nivel de lluvia. En este ejemplo la cantidad de lluvia es la causa y la cantidad de paraguas es el efecto, definiendo una relaci´on lluvia → paraguas. Estudiar la relaci´on de causalidad entre las variables, nos permite caracterizar los mecanismos que las generaron. Pero en general requiere interpretar a las mismas a partir de su f´ısica, m´as all´a de la estad´ıstica. El principio de independencia de mecanismos causales1 dice que, el proceso causal generativo de las variables de un sistema se compone de mecanismos aut´onomos que no se informan ni influyen entre s´ı. En el caso probabil´ıstico, esto significa que la distribuci´on condicional de cada variable, dadas sus causas (es decir, su mecanismo), no informa ni influye en los dem´as mecanismos [22, Cap´ıtulo 2]. Este principio pone el foco en entender el proceso de generaci´on de las variables, tal como se programar´ıa la fuente en el caso de necesitar generar datos sint´eticos.
La Fig. 4.1 menciona todas las relaciones de causalidad posibles entre los datos X y las etiquetas Y . Se denomina relaci´on causal, Fig. 4.1a a la estructura donde X → Y . En esta se definen como mecanismos independientes pX(x) y pY |X=x(y), descartando la posibilidad de que una etapa no supervisada ayude a resolver un problema supervisado. Se denomina relaci´on anticausal, Fig. 4.1b a la estructura donde Y → X. En esta se definen como mecanismos independientes pY (y) y pX|Y =y(x), denotando una posible influencia entre pX(x) y pY |X=x(y). Lo mismo ocurre en las relaciones no causales, Fig. 4.1c, donde no hay una causalidad entre las variables.
El problema de este tipo de an´alisis radica en la dificultad de catalogar la relaci´on de causalidad. Es entonces, cuando surge la idea de intentar deducir estas relaciones a partir de la estad´ıstica. B´asicamente queremos corroborar si el modelo se corresponde a alguno de los siguientes:
Modelo causal: Se genera X ∼ pX, y luego Y = g(X, U ) con U ∼ pU independiente a X. Este modelo se caracteriza con pU y g(x, u).
Modelo anticausal: Se genera Y ∼ pY , y luego X = h(Y, V ) con V ∼ pV independiente a Y . Este modelo se caracteriza con pV y h(y, v).
La identificaci´on de estos modelos es imposible, ya que para cualquier conjunta pXY (x, y) siempre existe tanto un modelo causal pU y g(x, u) como un modelo anticausal pV y h(y, v). Esto se demuestra con la Prop. 1.9: Sea U ∼ U(0, 1) y g(x, u) = F −1 Y |X=x(u), la variable Y |X=x = g(x, U ) ∼ pY |X=x(y). Nuevamente caemos en la cuenta de que la causalidad est´a determinada por el modelo f´ısico, va m´as all´a de la estad´ıstica.
Sin embargo, los probabilistas somos obstinados. Si bien nunca se podr´a asegurar la relaci´on de causalidad observando la estad´ıstica, si se puede presuponer. Es decir, si bien
1No confundir independencia estad´ıstica con independencia de mecanismos. La primera estudia la
influencia entre variables aleatorias y la segunda la influencia entre las distribuciones.
79
Cap´ıtulo 4. Aprendizaje no Supervisado
no se tiene certeza, puede existir evidencia hacia un lado o hacia otro. La suposici´on en este tipo de an´alisis es que los modelos mas simples son m´as habituales que los complejos. Por lo tanto, si uno de los modelos es considerablemente m´as sencillo que el otro, se puede suponer que es el correcto. Este es el caso t´ıpico de la mezcla, donde simular primero la variable mezcladora categ´orica es mucho m´as sencillo que hacerlo al final. Otros ejemplos ser´an analizados a continuaci´on.
Ejemplo 4.1 Estudiar la relaci´on de causalidad para (X, Y ) ∼ U(Λ), donde Λ es de la forma:
y
2
1
Λ
1
x
En este tipo de ejercicios tenemos que analizar si es m´as sencillo descomponer la distribuci´on conjunta como pXY (x, y) = pY |X=x(y)pX(x) o como pXY (x, y) = pY |X=x(y)pX(x). Este ejemplo en particular caracteriza las distribuciones condicionales como:
Y |X=x ∼ U(x, x + 1) ≡ x + U(0, 1),
X|Y =y ∼
 
U(0, y)
0 < y < 1
(4.1)

U(y − 1, 1) 1 < y < 2
En este caso, Y |X=x posee una estructura muy sencilla, mientras que X|Y =y requiere hacer una definici´on partida. Podemos suponer que corresponde a una relaci´on causal X → Y , y el modelo est´a caracterizado por Y = g(X, U ) = X + U con U ∼ U(0, 1).
Ejemplo 4.2 Estudiar la relaci´on de causalidad para
pXY (x, y) = e−x1 {0 < y < x}
(4.2)
En el Ej. 1.1 se dedujo que Y |X=x ∼ U(0, x) ≡ x · U(0, 1). Por lo tanto, su modelo causal X → Y es Y = g(X, U ) = X · U con U ∼ U(0, 1). Sin embargo, tambi´en puede efectuarse la descomposici´on inversa:
pXY (x, y) = e−(x−y)1 {x > y} (cid:125)
e−y1 {y > 0} (cid:123)(cid:122) (cid:125) (cid:124) pY (y)
(cid:123)(cid:122) pX|Y (x|y) es decir que X|Y =y se distribuye como una exponencial corrida en y, y su modelo anticausal Y → X es X = h(Y, V ) = Y +V con V ∼ exp(1). Ambos modelos son sumamente sencillos y no hay evidencia suficiente para suponer cu´al es el modelo real.
(cid:124)
(4.3)
80
Cap´ıtulo 4. Aprendizaje no Supervisado

### 4.1.1.


### Influencia del aprendizaje semisupervisado en modelos


### causales

En cap´ıtulos anteriores se demostr´o que el resultado ´optimo para minimizar el error cuadr´atico medio es el regresor asociado a la esperanza condicional E[Y |X = x] (Prop 1.8), el resultado ´optimo para minimizar la probabilidad de error es el clasificador bayesiano arg maxy PY |X=x(y) (Prop. 3.1) y el ´optimo para la entrop´ıa cruzada en la verdadera probabilidad PY |X=x (Prop. 3.2). En todos los casos las soluciones ´optimas dependen solo de la distribuci´on condicional PY |X=x(y), sin ser relevante la distribuci´on marginal pX(x). Es por ese motivo que en modelos causales X → Y (donde pX(x) y PY |X=x(y) son mecanismos independientes), una etapa no supervisada que permita estimar pX(x) no afecta a las distribuciones ´optimas.
Mientras que en modelos anticausales o no causales la etapa no supervisada puede ser de gran ayuda para el aprendizaje, en modelos causales no parece recomendable. Sin embargo, aunque marginal, la etapa no supervisada puede tener influencia positiva en modelos causales. Dado que en la pr´actica los algoritmos no alcanzar la soluci´on ´optima, una etapa no supervisada puede ayudar a determinar que soluci´on sub´optima es mejor [22, Cap´ıtulo 5]. A continuaci´on se estudiar´an los tres tipos de funciones costo mencionadas anteriormente, para demostrar a que nos referimos.
Demostraci´on 4.1 (Error cuadr´atico medio) Sea ˆy = φ(x), en (1.16) se demostr´o la relaci´on entre el error cuadr´atico medio y su correspondiente error bayesiano:
E[(Y − φ(X))2] = E[var(Y |X)] + E[(E[Y |X] − φ(X))2]
(4.4)
El error cuadr´atico (E[Y |X = x] − φ(x))2 alcanza su valor m´ınimo para φ(x) = E[Y |X = x]. Sin embargo, de no alcanzarse, la diferencia entre el error cuadr´atico medio y el error bayesiano en (4.4) viene dado por su valor medio. Dicho valor medio se calcula a partir de la marginal pX(x).
Demostraci´on 4.2 (Probabilidad de error) Sea ˆy = φ(x), la relaci´on entre el probabilidad de acierto y su correspondiente error bayesiano se puede representar como:
(cid:20)
m´ax y∈Y
(cid:21) PY |X=X(y)
+ E
(cid:20)
m´ax y∈Y
(cid:21) PY |X=X(y) − PY |X=X(φ(X))
(4.5)
P(Y = φ(X)) = E
La diferencia m´axy∈Y PY |X=x(y) − PY |X=x(φ(x)) alcanza su valor m´ınimo para φ(x) = arg maxy PY |X=x(y). Sin embargo, de no alcanzarse, la diferencia entre la
81
Cap´ıtulo 4. Aprendizaje no Supervisado
Figura 4.2: Ejemplo de manifold, donde los datos pueden caracterizarse con dos valores: m´odulo y fase. La imagen fue extra´ıda de https://en.wikipedia.org/wiki/Nonlinear_ dimensionality_reduction.
probabilidad de acierto y el valor ´optimo E (cid:2)m´axy∈Y PY |X=X(y)(cid:3) en (4.5) viene dado por su valor medio. Dicho valor medio se calcula a partir de la marginal pX(x).
Demostraci´on 4.3 (Entrop´ıa Cruzada) Sea ˆP (y|x), la predicci´on soft de un clasificador, en (3.35) se demostr´o la relaci´on entre la entrop´ıa cruzada y su correspondiente error bayesiano (cid:105) − log ˆP (Y |X)
+ E (cid:2)− log PY |X=X(Y )(cid:3)
(cid:104) KL
= E
(4.6)
(cid:17)(cid:105)
E
(cid:16)
(cid:104)
La divergencia de Kullback Leibler KL
alcanza su m´ınimo para ˆP (y|x) = PY |X=x(y). Sin embargo, de no alcanzarse, la diferencia entre el la entrop´ıa cruzada y el error bayesiano en (4.6) viene dado por su valor medio. Dicho valor medio se calcula a partir de la marginal pX(x).
PY |X=X∥ ˆP (·|X) (cid:16)
(cid:17) PY |X=x∥ ˆP (·|x)

## 4.2. Reducci´on de dimensi´on y Manifold

Cualitativamente, llamaremos manifold o variedad al espacio efectivo en el que habitan los datos. Ejemplos de manifolds pueden ser curvas en el plano o superficies en el espacio. En la Fig. 4.2 puede verse un ejemplo pr´actico de este fen´omeno. En ´esta, se estudia una base de datos con muchos predictores (uno por cada p´ıxel de la imagen) de letras “A”. En definitiva, esta base de datos se puede describir mediante dos valores: el tama˜no de la letra y el ´angulo de inclinaci´on. Es decir que con un dz = 2 es suficiente para explicar la naturaleza de los datos.
82
Cap´ıtulo 4. Aprendizaje no Supervisado
(a)
(b)
(c)
Figura 4.3: Ejemplo de aprendizaje en una tarea de reducci´on de dimensi´on [24]. (a) Para un algoritmo con overfitting; (b) para uno con encoder biyectivo; y (c) para un algoritmo con correcto manifold learning.
Cabe resaltar que el objetivo de la reducci´on de dimensi´on no es simplemente reconstruir los datos. Sino reconstruirlos a partir de una representaci´on relevante para explicar alg´un fen´omeno o resolver otra tarea. Si no se reconocen patrones en la naturaleza de los datos no hay aprendizaje. De hecho, existen transformaciones biyectivas T : Rdx → R que podr´ıan utilizarse como encoder [23, Capitulo 19] (y T −1 como decoder ). Pero las representaciones latentes obtenidas de esta manera no ser´an relevantes por no aportar informaci´on sobre la distribuci´on de los datos.
La Fig. 4.3a muestra un ejemplo de aprendizaje de un encoder capaz de reconstruir cualquier valor. Si el ancho de las l´ıneas es suficientemente fino, todas las muestras caer´an sobre la curva, pero la estructura aprendida nada tiene que ver con el manifold. La Fig. 4.3b muestra un algoritmo con overfitting y la Fig. 4.3c un correcto aprendizaje. En un autoencoder es tan importante no memorizar el conjunto de datos como no aprender una transformaci´on biyectiva, se desea aprender el manifold. La regularizaci´on de los autoencoders deben balancear estos conceptos.
Cuando el espacio de entrada es de dos dimensiones, como es el caso de la Fig. 4.3, puede visualizarse f´acilmente la soluci´on aprendida y corroborar si hay problemas de overfitting, underfitting o biyecciones. Pero en dimensiones m´as grandes se necesitan m´etodos m´as sofisticados. As´ı como el subajuste se verifica observando el error de entrenamiento y el sobreajuste comparando los errores de entrenamiento y validaci´on, detectar una soluci´on biyectiva requiere otro tipo an´alisis. Para corroborar si un determinado autoencoder codifica adecuadamente los datos, pero no cualquier tipo de entrada, se utiliza un detector de anomal´ıas.
Para ello, se define un segundo conjunto de testeo pero de caracter´ısticas an´omalas, es decir, un conjunto de datos con una distribuci´on claramente diferente a pX(x). Si el error cuadr´atico2 entre la imagen y la reconstrucci´on es grande para el caso del conjunto de
2Este error cuadr´atico no es un error cuadr´atico medio, porque se define para una sola muestra.
83
Cap´ıtulo 4. Aprendizaje no Supervisado
(a)
(b)
(c)
Figura 4.4: Ejemplo de detector de anomal´ıas. Se verifica el funcionamiento de un autoencoder entrenado con im´agenes de d´ıgitos manuscritos frente a una clara anomal´ıa. La imagen original fue extra´ıda de https://www.clipartmax.com/max/m2i8d3m2m2b1K9d3/.
testeo an´omalo y bajo para el conjunto de testeo original, se puede concluir que el autoencoder no aprendi´o una transformaci´on biyectiva. Un ejemplo de este fen´omeno puede verse en la Fig. 4.4, para un autoencoder entrenado con im´agenes de d´ıgitos manuscritos de 28 × 28 p´ıxeles en escala de grises. Tomando una imagen con una distribuci´on totalmente diferente, y adapt´andola al formato de 28 × 28 en escala de grises, podemos ver que el autoencoder reconstruye una imagen fuertemente err´onea. En el siguiente ejemplo se detallar´a como utilizar un autoencoder como detector de anomal´ıas.
Ejemplo 4.3 Se utiliza un autoencoder para implementar un detector de anomal´ıas. Los errores cuadr´aticos de cada muestra fueron
0.1,
0.8,
1.3,
1.9,
2.2
Sabiendo que las ´unicas muestras realmente an´omalas fueron las de error 1.3 y 2.2.
Graficar la curva ROC. Indicar los puntos correspondientes a todos los umbrales posibles e interporlar dichos puntos con rectas.
Indicar el EER y el AUC, basado en la interpolaci´on anterior.
Para un detector de anomal´ıas, se define como detector φt(x) = 1{(x − ˆx)2 > t} para t > 0: un clasificador que considerar´a anomal´ıa a muestras con alto error cuadr´atico de reconstrucci´on. Para las 5 muestras dadas, ser´an pocos los valores de t que modifican realmente la clasificaci´on. Para t ∈ (−∞; 0.1) todos los clasificadores ser´an iguales, lo mismo para t ∈ [0.1, 0.8), para t ∈ [0.8, 1.3), para t ∈ [1.3, 1.9), para t ∈ [1.9, 2.2) y para t ∈ [2.0, ∞). En total la curva ROC estar´a formada por 6 puntos.
84
Cap´ıtulo 4. Aprendizaje no Supervisado
) 1 =
Y | 1 = )
X
( t φ ( P
Perfecto
azaroso
Clasificador

### EER

P(φt(X) = 1|Y = 0)
Figura 4.5: Curvas ROC para el detector de anomal´ıas del Ej. 4.3.
En la Fig. 4.5 puede verse la curva ROC en cuesti´on. Cada umbral corresponde a un punto que ser´a calculado de forma emp´ırica, estudiando la proporci´on de muestras que cumplen la condici´on:
Para t ∈ (−∞; 0.1), todas las muestras poseen un φt(x) = 1 y por lo tanto el punto de la ROC ser´a el (1, 1).
Para t ∈ [0.1, 0.8), todas las muestras an´omalas Y = 1 son consideradas an´omalas φt(x) = 1 y de las 3 muestras regulares Y = 0, dos ser´an consideradas an´omalas. 3, 1(cid:1). Por lo tanto el punto de la ROC es el (cid:0) 2
Para t ∈ [0.8, 1.3), todas las muestras an´omalas son consideradas an´omalas y de las 3 muestras regulares, solo una ser´a consideradas an´omalas. Por lo tanto el punto de la ROC es el (cid:0) 1
3, 1(cid:1).
Para t ∈ [1.3, 1.9), una de dos anomal´ıas ser´a bien clasificada mientras que de las 3 muestras regulares solo una ser´a consideradas an´omalas. Por lo tanto el punto de la ROC es el (cid:0) 1
(cid:1).
3, 1
2
Para t ∈ [1.9, 2.2), todas las muestras regulares ser´an bien clasificadas, pero solo una (cid:1). de las dos anomal´ıas ser´a detectada. Por lo tanto el punto de la ROC es el (cid:0)0, 1
2
Para t ∈ [2.0, ∞), todas las muestras ser´an consideradas regulares y por lo tanto el punto de la ROC es el (0, 0).
Gr´aficamente se puede observar que el EER se dar´a en la intersecci´on de las rectas 3. Es decir 3. Para el caso del ´area basta con sumar ´areas de rect´angulos para notar que
P(φt(X) = 1|Y = 1) = 1 − P(φt(X) = 1|Y = 0) y P(φt(X) = 1|Y = 0) = 1 que EER = 1 AUC = 5 6.
85
Cap´ıtulo 4. Aprendizaje no Supervisado
xi
αiv1
Figura 4.6: Ejemplo de reducci´on de dimensi´on (2D a 1D) utilizando PCA. En verde se destaca la proyecci´on sobre el manifold de una de las muestras.

## 4.3. An´alisis de Componentes Principales

El m´etodo lineal m´as utilizado en reducci´on de dimensi´on se denomina PCA (An´alisis de Componentes Principales). PCA utiliza teor´ıa de subespacios para proyectar ortogonalmente las muestras dentro del manifold hallado. Como todo subespacio, tiene la caracter´ıstica de pasar por el origen. Por este motivo es imprescindible normalizar en media a (cid:80)ntr los datos3 (˜xi)j = (xi)j − µj con µj = 1 i=1(xi)j. Ocasionalmente se puede normalizar ntr tambi´en en varianza, pero solo se reserva para casos particulares donde se necesite interpretar cuantitativamente el manifold (y por lo tanto las magnitudes deben estar en las mismas unidades para ser comparables) o para solucionar algunos problemas num´ericos (diferentes a los del gradiente descendente estudiados en la Secci´on 2.3.1, relacionados con el n´umero de condici´on de la matriz involucrada).
Dado un conjunto de datos de media muestral nula {˜xi}ntr
i=1, llamamos direcci´on principal v1 al versor que minimiza el error cuadr´atico medio entre los datos ˜xi y su proyecci´on ortogonal αiv1:
∥˜xi − αiv1∥2
s.t.
vT 1 (˜xi − αiv1) = 0 ∀ i = 1, · · · , ntr
(4.7)
v1 = arg min v1∈Rdx : ∥v1∥2=1
1 ntr
ntr(cid:88)
i=1
donde αi representa al valor de la muestra i-´esima en el espacio proyectado, y la condici´on vT 1 (˜xi − αiv1) = 0 induce la ortogonalidad entre el espacio a proyectar y el error de dicha proyecci´on. La Fig. 4.6 muestra un ejemplo de dos dimensiones de PCA. Las muestras (indicadas con puntos azules) son proyectadas ortogonalmente sobre un espacio de dimensi´on reducida (la recta roja). Utilizando el hecho que v1 posee norma unitaria, se puede deducir al valor de αi de la condici´on de ortogonalidad como αi = vT 1 ˜xi. Esta condici´on excede a las muestras de entrenamiento, incluso en inferencia, para proyectar cualquier valor ˜x basta con computar α = vT 1 ˜x. Pero volviendo a la etapa de entrenamiento, el
3Por (xi)j nos referimos a la componente j-´esima del vector xi.
86
(4.8)
(4.9)
(4.10)
(4.11)
Cap´ıtulo 4. Aprendizaje no Supervisado
versor v1 debe cumplir:
v1 = arg min v1∈Rdx : ∥v1∥2=1
= arg min v1∈Rdx : ∥v1∥2=1
= arg max v1∈Rdx : ∥v1∥2=1
1 ntr
1 ntr
1 ntr
ntr(cid:88)
i=1
ntr(cid:88)
[˜xi − (vT
1 ˜xi)v1]T [˜xi − (vT
1 ˜xi)v1]
∥˜xi∥2 − (vT
1 ˜xi)2
i=1
ntr(cid:88)
i=1
(vT
1 ˜xi)2
(cid:32)
vT 1
1 ntr
ntr(cid:88)
i=1
(cid:33)
˜xi ˜xT i
v1
= arg max v1∈Rdx : ∥v1∥2=1 i=1 ˜xi ˜xT
(cid:80)ntr
La matriz Σ = 1 ntr
i es una covarianza muestral por ser muestras de media nula. Este tipo de problema de optimizaci´on con restricciones puede resolverse utilizando el multiplicador de Lagrange λ, definiendo la funci´on:
1 v1 − 1)
J(v1) = vT
1 Σv1 − λ(vT Para encontrar el ´optimo basta con igualar a cero la primera derivada (gradiente) respecto a v1 (para m´as informaci´on sobre derivadas respecto vectores/matrices ver [9]): ∇J(v1) = 2Σv1 − 2λv1 = 0, es decir Σv1 = λv1. Esta condici´on se cumple para todos los autovectores v1 de la matriz Σ con el correspondiente autovalor asociado λ. Sea (λ, v1) ∈ V el conjunto de pares autovalores-autoversores de la matriz Σ, la optimizaci´on de (4.8) es: (4.13)
(4.12)
λ
v1 = arg max (λ,v1)∈V
λ · ∥v1∥2 = arg max (λ,v1)∈V
Es decir que la direcci´on principal v1 corresponde al autoversor asociado al autovalor m´as grande. Este procedimiento se puede repetir para encontrar el 2do, 3er, etc. componente principal. El resultado son el 2do, 3er, etc autovalor con su autovector como direcci´on.
A continuaci´on se analizar´a como debe ser interpretada la etapa de inferencia en el contexto de autoencoders. Supongamos una reducci´on de dimensi´on de dx a dz para el espacio latente Z = Rdz con dz ≤ dx, y sea V ∈ Rdx×dz la matriz formada con los dz autovectores principales. El encoder queda definido por la operaci´on z = VT x mientras que el decoder hace lo propio con la operaci´on ˆx = Vz; ambas transformaciones lineales. Por ser los autovectores ortonormales debe cumplirse que VT V = I, pero solo en el caso de que la matriz cuente con todos los autovectores (ya que la matriz V ser´a inversible) ser´a v´alido que VVT = I. El porcentaje de energ´ıa perdida en la reconstucci´on puede medirse por la proporci´on de autovalores despreciados (los autovalores son no negativos).
87
Cap´ıtulo 4. Aprendizaje no Supervisado
Edad
0-9 10-19 20-29 30-39
40-49
50-59
60-69
70-79 ≥ 80
Total
Italia
0 % 0 % 0 %
0 % 0.1 % 0.2 % 2.5 % 6.4 % 13.2 % 4.4 %
(0/43)
(0/85)
(0/296)
(0/470)
(1/891)
(3/1453)
(37/1471)
(114/1785)
(202/1532)
(357/8026)
China
0 % 0.2 % 0.2 % 0.2 % 0.4 % 1.3 % 3.6 %
8 % 14.8 % 2.3 %
(0/0)
(1/549)
(7/3619)
(18/7600)
(38/8571)
(130/10008)
(309/8583)
(312/3918)
(208/1408)
(1023/44672)
Cuadro 4.1: Paradoja de Simpson presente sobre la tasa de letalidad del Covid-19 [25]. El total parecer´ıa indicar una letalidad mayor en Italia, sin embargo al desagregar la informaci´on por rango etario se observa que la tendencia era la contraria.

## 4.4. Clustering y el algoritmo K-Means

El problema de clustering, es decir codificar sobre un espacio finito Z = {1, · · · , K}, debe ser interpretado como el equivalente no supervisado de la clasificaci´on. En el, a cada muestra x se le asigna una clase k como etapa de codificaci´on. Para la decodificaci´on, basta con reemplazar cada clase con un representante ˆx ∈ Rdx de la misma, habitualmente llamado centroide. Al haber solamente K valores v´alidos de centroides, se vuelve imposible aprender un encoder biyectivo y por lo tanto es un problema menos a verificar. En cuanto a aplicaciones, existen de lo m´as diversas: separar datos, comprimir informaci´on, caracterizar comportamientos est´andar, entre otros. Pero uno de los m´as importantes es evitar la llamada Paradoja de Simpson. La paradoja de Simpson es un fen´omeno estad´ıstico en el cu´al una tendencia que aparece en varios grupos de datos desaparece cuando estos grupos se combinan y en su lugar aparece la tendencia contraria para los datos agregados. Un ejemplo de este fen´omeno puede verse en el Cuadro 4.1. En ´el, se observan los primeros datos de tasa de letalidad del Covid-19 en Italia y China. A primera vista, la informaci´on parecer´ıa indicar que el virus fue m´as letal en Italia (4.4 %) que en China (2.3 %). Sin embargo, cuando la informaci´on es desagregada por rango etario, se observa que consistentemente el Covid-19 fue m´as letal en China en todos los grupos. Lo que est´a pasando es que en Italia los pacientes mor´ıan porque su poblaci´on era m´as longeva, pero esto no ten´ıa que ver con las caracter´ısticas del virus. Dividir la poblaci´on en clases evit´o llegar a conclusiones incorrectas.
El algoritmo m´as sencillo para resolver el problema de clustering se denomina Kmeans. Este algoritmo se basa en encontrar, de forma iterativa, los centroides de cada clase (como el centro de masa de la nube de puntos) y asignar cada muestra al centroide m´as cercano. Prefijados el n´umero de clases K e inicializando los centroides eligiendo K muestras al azar del conjunto de datos de entrenamiento, K-means propone iterar hasta la convergencia entre:
88
Cap´ıtulo 4. Aprendizaje no Supervisado
Minimizaci´on (M): Asignar a cada muestra xi la clase k correspondiente al centroide µk m´as cercano zi = arg m´ın
∥xi − µk∥.
k=1,··· ,K
Expectaci´on (E): Recalcular cada centroide como el punto medio dentro de la (cid:88)
clase correspondiente µk =
1 #(zi = k)
xi.
i: zi=k
Cabe destacar que una caracter´ıstica relevante de los algoritmos de aprendizaje no supervisado es su sensibilidad al punto de inicializaci´on. En este tipo de algoritmos se suele necesitar correr el algoritmo muchas veces y analizar la consistencia de los resultados.
Ejemplo 4.4 Clusterizar, via algoritmo K-means, el siguiente conjunto de datos. Incializar los centroides como (0, 3) y (1, 1). Indicar los resultados parciales de cada paso del algoritmo.
idx x1 x2 3 0 0
1
2
3
1
2
3
1
0
2
Cabe destacar que en este ejemplo K = 2 ya que se informan dos centroides.
Como primer paso M, se asignar´a un valor zi = 1 a las muestras m´as cercanas al µ1 = (0, 3) y un valor zi = 2 a las m´as cercanas al µ2 = (1, 1). En este caso z0 = 1, z1 = 2, z2 = 2 y z3 = 2.
Como primer paso E, se recalcularan los centroides µ1 = (0, 3) y µ2 = (2, 1).
El 2do paso M vuelve a asignar una clase a cada muestra. Esta asignaci´on vuelve a ser z0 = 1, z1 = 2, z2 = 2 y z3 = 2, denotando la convergencia alcanzada.

## 4.5. Algoritmo Expectaci´on-Maximizaci´on

En problemas de aprendizaje no supervisado ambiciosos, donde se desea caracterizar totalmente la distribuci´on de los datos, el estimador de m´axima verosimilitud discutido en la Secci´on 1.2.3 es un buen punto de partida. Sin embargo, el problema con este tipo de algoritmos radica en que el estimador no tiene soluci´on anal´ıtica para modelos medianamente sofisticados. Una soluci´on num´erica puede tampoco ser satisfactoria en grandes dimensiones, por volverse r´apidamente un problema computacionalmente intratable. Es entonces cuando surge la necesidad de relajar el problema de optimizaci´on presente en este tipo de estimadores con un algoritmo iterativo.
89
Cap´ıtulo 4. Aprendizaje no Supervisado
Un primer detalle a tener en cuenta es el v´ınculo entre maximizar la verosimilitud y minimizar la entrop´ıa cruzada emp´ırica. Dicho v´ınculo se evidencia utilizando la monoton´ıa del logaritmo y la independencia entre muestras:
arg max θ∈Θ
p(x|θ) = arg max
n (cid:89)
p(xi|θ) = arg min
θ∈Θ
1 n
n (cid:88)
i=1
θ∈Θ
i=1
− log p(xi|θ)
(4.14)
donde esta relaci´on demuestra lo relevante que pueden ser las m´etricas de informaci´on (v´ease Secci´on 3.1.2.1) en este tipo de algoritmos. Entre estas m´etricas, vale la pena destacar a la divergencia de Kullback Leibler, la cu´al cuantifica la discrepancia entre dos distribuciones4. Recordando que esta magnitud es siempre mayor o igual que cero con igualdad si y solo si las distribuciones son las mismas (Prop. 3.3), podemos reescribir al estimador como:
ˆθMV = arg max
θ∈Θ
log p(x|θ) = arg max
θ∈Θ
m´ax q∈P
log p(x|θ) − KL (q(·|x)∥p(·|x, θ))
(4.15)
donde P es la familia de todas las posibles distribuciones condicionales de un vector aleatorio z|x. La t´ecnica descripta en la presente secci´on requiere una selecci´on delicada de el vector z para cada problema. Una buena selecci´on radicar´a en elegir una variable noobservable del problema relevante para el mismo, el conocimiento espec´ıfico de la tarea a resolver es vital para este tipo de algoritmos. Este tipo de variables no observables, presentes en el algoritmo, har´an las veces de variables latentes. A su vez se define la cota inferior esperada (Expected Lower BOund ) como:
ELBO(θ, q) = log p(x|θ) − KL (q(·|x)∥p(·|x, θ))
(4.16)
donde su m´aximo alcanza la log-verosimilitud de la muestra (es una cota inferior).
El algoritmo Expectaci´on-Maximizaci´on (o algoritmo EM), propone relajar el problema de optimizaci´on descripto en (4.15) resolviendo las dos maximizaciones de forma iterativa. Es decir, partiendo de un θ0 ∈ Θ, el algoritmo propone iterar para t ∈ N entre los pasos de expectaci´on y maximizaci´on:
E) q(t) = arg max
ELBO(θ(t−1), q),
M ) θ(t) = arg max
ELBO(θ, q(t))
(4.17)
q∈P
θ∈Θ
La soluci´on de este algoritmo ˆθ, en principio no tiene por que coincidir con el estimador de m´axima verosimilitud ˆθMV, por lo que ser´a considerada sub´optima. Sin embargo, en muchas familias param´etricas dicha soluci´on ser´a alcanzada, con habitual sensibilidad al punto de inicializaci´on θ0. En general, lo que siempre est´a asegurada es la monoton´ıa de la verosimilitud. Es decir que en cada paso del algoritmo, la verosimilitud solo puede mejorar (aunque sin garant´ıas de alcanzar p(x|ˆθMV)).
4En rigor de verdad, en la Secci´on 3.1.2.1 fue definida la divergencia de Kullback Leibler para variables discretas. Sin embargo, ´esta puede generalizarse de forma inmediata al caso continuo. V´ease [2, Cap´ıtulo 8] para m´as detalles.
90
Cap´ıtulo 4. Aprendizaje no Supervisado
Propiedades 4.1 p(x|θ(t)) ≥ p(x|θ(t−1)).
Demostraci´on 4.4 (Prop. 4.1) El algoritmo EM maximizaciones sucesivas, logrando as´ı una cadena acendente de ELBOs
ELBO (cid:0)θ(t−1), q(t)(cid:1) ≤ ELBO (cid:0)θ(t), q(t)(cid:1) ≤ ELBO (cid:0)θ(t), q(t+1)(cid:1)
(4.18)
En particular, el paso E se puede analizar estudiando la Prop. 3.3 aplicada a (4.16) (elegir el q(t) que haga cero la divergencia de Kullback Leibler). Esto nos lleva a identidades del tipo p(x|θ(t−1)) = ELBO (cid:0)θ(t−1), q(t)(cid:1) y p(x|θ(t)) = ELBO (cid:0)θ(t), q(t+1)(cid:1). Reemplazando estas identidades en (4.18) la propiedad es demostrada.
El paso M o maximizaci´on, recibe su nombre por representar una maximizaci´on num´erica (igualando a cero la derivada de alguna expresi´on). Su expresi´on puede simplificarse utilizando la siguiente cadena de razonamientos:
ELBO(θ, q) = Eq
(cid:20)
p(x|θ) − log
q(Z|x) p(Z|x, θ) = Eq [log p(x, Z|θ)|X = x] − Eq [log q(Z|x)|X = x]
X = x
(cid:21)
(cid:12) (cid:12) (cid:12) (cid:12)
(4.19)
(4.20)
donde el t´ermino restante no depende de θ y por lo tanto no influir´a en este paso. Es decir, el paso M se basa en resolver
∂ ∂θ
E
q(t) [log p(x, Z|θ)|X = x] = 0
(4.21)
Por su parte, el paso E o expectaci´on, simplemente elige q(t)(z|x) = p(z|x, θ(t−1)) para volver cero la divergenica de Kullback Leibler de (4.16). El mismo puede interpretarse como un proxy para el c´omputo de E q(t) [log p(x, Z|θ)|X = x], magnitud necesaria en el pr´oximo paso M. Dado que su funci´on puede reducirse a calcular una esperanza es que recibe el nombre de expectaci´on (spanglish). En resumen, el algoritmo EM puede simplificarse como:
E) q(t)(z|x) = p(z|x, θ(t−1)),
M )
∂ ∂θ
E
q(t) [log p(x, Z|θ)|X = x]
(cid:12) (cid:12) (cid:12) (cid:12)θ=θ(t)
= 0
(4.22)
A continuaci´on se analizar´a un ejemplo para fijar conceptos.
Ejemplo 4.5 Los habitantes de Smallville pueden ser considerados trabajador registrado, trabajador informal o desempleado con probabilidades θ 2 respectivamente, donde 0 ≤ θ ≤ 1. El municipio posee 10.000 habitantes y cuenta con 4.000 trabajadores registrados.
2 y 1
2, 1−θ
1. Estimar θ por m´axima verosimilitud.
2. Deducir matem´aticamente una recursi´on, v´ıa algoritmo EM, que permita esti-
mar θ.
91
Cap´ıtulo 4. Aprendizaje no Supervisado
3. Se denomina puntos fijos a los valores de θ que no var´ıan al iterar un paso del algoritmo. Encontrar los puntos fijos del problema de recursi´on definido por EM.
4. ¿A que punto converge el problema si θ0 = 0.999? Analizar resultado.
Sea X la cantidad de trabajadores registrados, Y la cantidad de trabajadores informales y Z la cantidad de desempleados.
1. La ´unica variable observable es x = 4000, ya que con los datos p´ublicos uno no puede distinguir con precisi´on entre informales y desempleados. En este caso, la probabilidad estimada por m´axima verosimilitud es 4000 5. A su vez, el principio de invarianza nos dice que si dicha probabilidad es modelada como θ 2, entonces ˆθMV = 4 5.
10000 = 2
2
2 , 1
2, 1−θ
2. Por la naturaleza del modelo, las variables aleatorias involucradas forman un vector con distribuci´on (X, Y, Z) ∼ Mn(10000, (cid:2) θ (cid:3)) (v´ease Def. 1.2). Podemos elegir como variable latente, tanto la cantidad de trabajadores informales como la cantidad de desempleados, ya que ambas son variables relevantes del problema. En particular, 1 2−θ ), elegimos Z para mantener la nomenclatura. Luego Z|X = 4000 ∼ Bin(6000, definiendo p(z|x, θ) y por lo tanto el paso E. La distribuci´on es binomial por dejar definido experimentos del tipo ´exito/fracaso (es o no desempleado), la cantidad de experimentos (potenciales desempleados) son 6000 ya que 4000 de los 10000 ciudadanos son sabidos formales, y la probabilidad fue calculada como ser desempleado sabiendo que no es formal:
P(desempleado|no formal) =
P(desempleado) 1 − P(formal)
=
1 2 1 − θ 2
=
1 2 − θ
(4.23)
Por el lado del paso M, se puede utilizar la funci´on de la probabilidad de la multinomial como5:
log P (x, z|θ) = kx,z + x log
+ (10000 − x − z) log
(4.24)
θ 2
1 − θ 2
donde kx,z acapara constantes que no dependen de θ. Luego, Q(t) [log P (4000, Z|θ)|X = 4000] = θ 2
+ (6000 − E
k + 4000 log
Q(t) [Z|X = 4000]) log
E
1 − θ 2
(4.25)
donde k acapara constantes que no dependen de θ. El algoritmo queda definido con un paso E que define Q(t) a partir de θ(t−1) computando E Q(t) [Z|X = 4000] = 2−θ(t−1) , y un paso M que define θ(t) a partir de Q(t) igualando a cero la derivada de
6000
5Utilizaremos P y Q may´usculas, en lugar de p y q, para resaltar que las variables involucradas son
discretas.
92
Cap´ıtulo 4. Aprendizaje no Supervisado
la expresi´on (4.25):
4000 θ
−
6000 − E
Q(t) [Z|X = 4000]
1 − θ
= 0
Las siguientes recursiones son soluciones equivalentes: 4000 θ(t) = 2(1 − θ(t)) =
6000 − 6000 1 − θ(t) (cid:18)
2−θ(t−1)
3 −
(cid:19)
θ(t)
(cid:18)
2 =
5 −
y por lo tanto
3 2 − θ(t−1)
3 2 − θ(t−1) (cid:19)
θ(t)
θ(t) =
2
5 − 3
2−θ(t−1)
=
4 − 2θ(t−1) 7 − 5θ(t−1)
(4.26)
(4.27)
(4.28)
(4.29)
(4.30)
3. Para los puntos fijos basta con buscar los valores de θ = θ(t) = θ(t−1). Para ellos
puede despejarse 5θ2 − 9θ + 4 = 0. Esta par´abola tiene soluciones θ = 4
5 y θ = 1.
4. Los puntos fijos indican los ´unicos valores a los que puede converger el algoritmo. En este caso hay dos: el estimador de m´axima verosimilitud θ = ˆθMV y la no existencia de trabajadores informales θ = 1. Mientras que una es la soluci´on que buscamos, la otra contradice el modelo propuesto. Sin embargo, la naturaleza de ambas es muy diferente. Mientras que θ = ˆθMV es una soluci´on atractiva, θ = 1 es repulsiva. Queda al lector probar que incluso inicializando muy cerca de θ = 1 (θ0 = 0.999), el algoritmo converge a θ = ˆθMV.
El ejemplo anterior funciona a modo pedag´ogico, obviamente cuando es sencillo calcular el estimador de m´axima verosimilitud no tiene sentido plantear el algoritmo EM. A continuaci´on se presentan algunos de los modelos m´as habituales en el uso de este algoritmo.

### 4.5.1. Modelo de Mezclas

Los modelos m´as habituales en el uso del algoritmo EM son los que caracterizan a las muestras xi como mezclas. En ese contexto, cada variable xi posee su correspondiente variable mezcladora zi. Sea una muestra n−dimensional de pares independientes (X, Z), con Z ∼ Cat({c1, · · · , cK}) y θ = {ck, θk}K k=1, donde los θk representan los par´ametros de la distribuci´on X|Z = k. Este tipo de modelos se denomina soft-clustering, porque no solamente se asocia una etiqueta para cada x, sino que se caracteriza la probabilidad de pertenecer a cada cluster a partir de Q(k|x).
En cuanto a su implementaci´on, notar que para el paso E basta con utilizar la indepeni=1 P (zi|xi, θ(t−1)) (la variable k indexa los valores
dencia entre las muestras Q(t)(z|x) = (cid:81)n
93
Cap´ıtulo 4. Aprendizaje no Supervisado
de Z). Es decir que Q(t)(k|x) = P (k|x, θ(t−1)), donde
Q(t)(k|x) =
c(t−1) k m=1 c(t−1)
m
(cid:80)K
· p(x|Zi = k, θ(t−1)
)
k
· p(x|Zi = m, θ(t−1) m )
(4.31)
Con esta distribuci´on se calcula la esperanza necesaria para el paso M
E
Q(t) [log p(x, Z|θ)|X = x] =
=
n (cid:88)
i=1 n (cid:88)
E
Q(t) [log p(Zi|θ) + log p(xi|Zi, θ)|Xi = xi]
(4.32)
K (cid:88)
Q(t)(k|xi) [log ck + log p(xi|Zi = k, θk)]
(4.33)
i=1
k=1
con la restricci´on de (cid:80)K k=1 ck = 1. Dicha restricci´on puede incorporarse al problema utilizando multiplicadores de Lagrange. Es decir, que en el paso M se elegir´a como θ(t) los par´ametros que igualen a cero la derivada de:
J(θ) =
n (cid:88)
K (cid:88)
i=1
k=1
Q(t)(k|xi) [log ck + log p(xi|Zi = k, θk)] + λ
1 −
(4.34)
(cid:32)
(cid:33)
K (cid:88)
k=1
ck
Esta expresi´on se deber´a derivar respecto a cada ck y cada θk. Por el lado de ck se
obtiene:
∂J(θ) ∂ck
=
n (cid:88)
Q(t)(k|xi) ck
− λ = 0 → ck =
n (cid:88)
Q(t)(k|xi)
(4.35)
1 λ
Notar que, para que (cid:80)K
i=1 k=1 ck = 1, es necesario que λ = n, obteniendo entonces la
i=1
condici´on:
c(t) k =
1 n
n (cid:88)
i=1
Q(t)(k|xi)
Por el lado de los par´ametros θk se deber´a resolver:
∂J(θ) ∂θk
=
n (cid:88)
i=1
Q(t)(k|xi)
∂ log p(xi|Zi = k, θk) ∂θk
= 0
(4.36)
(4.37)
Mientras que (4.31) y (4.36) aplican para cualquier modelo de mezcla, (4.37) deber´a adaptarse a cada modelo particular. En este contexto, el m´as habitual se conoce como mezcla de Gaussianas.
4.5.1.1. Modelo de mezcla de Gaussianas
El modelo m´as utilizado por este algoritmo es el de mezcla de gaussianas. En ´el, se utilizan distribuciones normales multivariadas de la forma X|Z = k ∼ N (µk, Σk), donde θk = (µk, Σk). Es decir, que (4.37) se traduce en dos conjuntos de par´ametros a actualizar: µk y Σk. En este caso, es f´acil notar que 1 log p(x|Z = k, θk) = cte − 2
(x − µk)T Σ−1
k (x − µk)
log |Σk| −
(4.38)
1 2
94
Cap´ıtulo 4. Aprendizaje no Supervisado
donde cte es un t´ermino que no depende de θk (y por lo tanto se eliminar´a al calcular la derivada). Al derivar respecto de la media se obtiene (para detalles acerca de la derivada respecto a vectores y matrices ver [9]):
por lo tanto, la actualizaci´on de la media se deber´a efectuar con la siguiente ecuaci´on:
∂ log p(x|Z = k, θk) ∂µk
= Σ−1
k (x − µk)
(4.39)
n (cid:88)
i=1
Q(t)(k|xi)Σ−1
k (xi − µk) = 0 → µ(t)
k =
(cid:80)n
i=1 Q(t)(k|xi) · xi (cid:80)n i=1 Q(t)(k|xi)
En cambio, al derivar respecto de la covarianza se obtiene:
∂ log p(x|Z = k, θk) ∂Σk
= −
1 2
Σ−1
k +
1 2
Σ−1
k (x − µk)(x − µk)T Σ−1
k
(4.40)
(4.41)
Esto quiere decir que, para la covarianza, (4.37) se traduce en:
n (cid:88)
i=1
Q(t)(k|xi)
(cid:20)
−
1 2
Σ−1
k +
1 2
Σ−1
k (xi − µk)(xi − µk)T Σ−1
k
con lo cu´al, la actualizaci´on de la covarianza deber´a ser:
Σ(t)
k =
(cid:80)n
i=1 Q(t)(k|xi) · (xi − µ(t) (cid:80)n i=1 Q(t)(k|xi)
k )(xi − µ(t)
k )T
(cid:21)
= 0
(4.42)
(4.43)
Es decir, que el algoritmo EM queda definido por las ecuaciones (4.31), (4.36), (4.40)
y (4.43).

### 4.5.2. An´alisis de Factores

El uso de variables latentes permite plantear el problema de reducci´on de dimensi´on (v´ease Sec. 4.2), desde una perspectiva m´as general, como un problema estoc´astico. Se modelan los datos observados como:
X = µ + W · Z + ϵ (4.44) donde µ ∈ Rdx, W ∈ Rdx×dz , Z ∼ N (0, I) (de dimensi´on dz) y ϵ ∼ N (0, Ψ) (de dimensi´on dx) con Ψ ∈ Rdx×dx una matriz diagonal y con Z y ϵ independientes. En particular, si se restringe el problema a una covarianza esf´erica Ψ = σ2I, se obtiene un algoritmo conocido como Probabilistic PCA.
Este modelo separa los datos como una suma de factores: la media µ, un factor representativo del manifold W Z y un ruido ϵ independiente de todo lo dem´as. Combinando la normalidad de las variables aleatorias con la aditividad de los factores, queda asegurada tanto la normalidad conjunta entre (X, Z) como condicional Z|X = x y X|Z = z, lo cu´al simplifica bastante los c´alculos del modelo. Para este problema, los par´ametros son
95
Cap´ıtulo 4. Aprendizaje no Supervisado
{µ, W, Ψ} y ser´an aprendidos por el algoritmo EM.
Esta caracterizaci´on estoc´astica, permite plantear el problema de reducci´on de dimensi´on, utilizando como encoder como E[Z|X = x] y como decoder E[X|Z = z] (las esperanzas condicionales minimizan el error cuadr´atico medio como se demostr´o en la Prop. 1.8). Este modelo puede ser utilizado como una variante de PCA (v´ease Sec. 4.3), tambi´en lineal, con el agregado de funcionar tambi´en como m´etodo generativo: pasando por el decoder a variables latentes generadas como Z ∼ N (0, I), es factible generar nuevas muestras.
La etapa de predicci´on (testeo, validaci´on, etc.) quedar´a definido por las expresiones E[Z|X = x] y como decoder E[X|Z = z], donde el decoder se puede ver inmediatamente de (4.44) que X|Z = z ∼ N (µ + W z, Ψ) y por lo tanto E[X|Z = z] = µ + W z. El encoder en cambio ser´a calculado durante el paso E: q(t)(z|x) = (cid:81)n i=1 p(zi|xi, θ(t−1)), es decir que q(t)(z|x) = p(z|x, θ(t−1)).
En cuanto a su entrenamiento, se descomponer´a el los previamente pasos definidos E y M. En cuanto al paso E, se desea caracterizar los par´ametros de la distribuci´on de Z|X = x (la cu´al ser´a normal). En primer lugar, la distribuci´on Z ∼ N (0, I) es definida por el modelo, mientras que X ∼ N (µ, W W T + Ψ) (utilizando la independencia entre Z y ϵ, y las propiedades vectoriales de la covarianza [9]6). Entonces, la conjunta posee distribuci´on:

 
X
Z



  ∼ N
 
 


  ,
 
µ
0
W W T + Ψ W
W T
I


 
 
donde la covarianza cruzada es consecuencia de
E[(X − µ)(Z − 0)T ] = E[(W Z − ϵ)Z T ] = W
(4.45)
(4.46)
Una vez reconocida la distribuci´on conjunta como normal multivariaza, la condicional
puede deducirse con propiedades de esta familia de distribuciones [9]:
Z|X = x ∼ N (cid:0)W T (W W T + Ψ)−1(x − µ), I − W T (W W T + Ψ)−1W (cid:1)
(4.47)
Dos importantes caracter´ısticas a resaltar de (4.47) son la linealidad del encoder E[Z|X = x] = W T (W W T + Ψ)−1(x − µ) y la heterocedasticidad (covarianza constante, no depende de x), definiendo Σ = I − W T (W W T + Ψ)−1W . En este caso llamamos tambi´en mi = W T (W W T + Ψ)−1(xi − µ) para las muestras de entrenamiento.
Las expresiones de mi y Σ requieren el c´omputo de una inversa de una matriz de dimensi´on dx. Dado que en el problema de reducci´on de dimensi´on, dz < dx, suele aliviar el c´omputo reescribiendo las expresiones utilizando propiedades de las inversas matriciales
6Es esta secci´on se utilizar´an diversas propiedades matriciales. Se recomienda al lector seguir las
deducciones consultando simult´aneamente este apunte y el libro [9].
96
Cap´ıtulo 4. Aprendizaje no Supervisado
[9]:
mi = ΣW T Ψ−1(xi − µ),
Σ = (I + W T Ψ−1W )−1
(4.48)
(cid:80)n
En cuanto al paso M hay varias consideraciones a tener en cuenta. En primer lugar, para simplificar el an´alisis se aplicar´a EM solamente sobre θ = {W, Ψ} y se estimar´a la media utilizando la media muestral µ = 1 i=1 xi (la cu´al ser´a calculada previa a la iteraci´on n de EM por no necesitar actualizarse). Esto no es necesario de imponerlo para llegar a los mismos resultados, asumiendo solamente µ(0) = 1 i=1 xi y buscando su recursi´on n por EM se demuestra el mismo resultado (ser´a demostrado al final del cap´ıtulo). Pero el excluirlo de antemano facilita el an´alisis. En segundo lugar, una vez establecido el valor de la media, queda de manifiesto que (cid:80)n i=1 mi = 0. En tercer lugar, el modelo propuesto, no solamente asume la independencia entre las muestras, sino que tambi´en impone una p(z) independiente de los par´ametros (normal est´andar). Esto permite reescribir la esperanza necesaria para el paso M como:
(cid:80)n
E
q(t) [log p(x, Z|θ)|X = x] =
n (cid:88)
i=1
q(t) [log p(Zi)] + E E
q(t) [log p(xi|Zi, θ)|Xi = xi]
(4.49)
donde la primera esperanza no depende del par´ametro (su derivada ser´a nula) y la segunda es de la forma
E
q(t) [log p(x|Z, θ)|X = x] =
(4.50)
−
dx 2
log(2π) −
1 2
log |Ψ| −
1 2
E
q(t)
(cid:2)(x − µ − W Z)T Ψ−1(x − µ − W Z)(cid:12)
(cid:12) X = x(cid:3)
En cuarto lugar cabe destacar que, bajo q(t)(·|xi), U = xi − µ − W Z ∼ N (xi − µ −
W mi, W ΣW T ). Luego, la esperanza anterior puedo escribirla como [9]:
E
q(t)[U T Ψ−1U |Xi = xi] = Tr(Ψ−1W ΣW T ) + (xi − µ − W mi)T Ψ−1(xi − µ − W mi) (4.51) Teniendo todas estas cuestiones en cuenta se puede definir a la funci´on cuya derivada
ser´a igualada a cero:
J(W, Ψ) = cte −
n 2
log |Ψ| −
n 2
Tr(Ψ−1W ΣW T ) −
1 2
n (cid:88)
(xi − µ − W mi)T Ψ−1(xi − µ − W mi)
i=1
(4.52)
Derivando respecto de W y utilizando propiedades matriciales [9]:
∂J(W, Ψ) ∂W
= −nΨ−1W Σ −
1 2
n (cid:88)
i=1
(cid:2)2Ψ−1W mimT
i − 2Ψ−1(xi − µ)mT i
(cid:3)
(4.53)
Igualando a cero y despejando W :
W =
(xi − µ)mT i
(cid:32) n
(cid:88)
i=1
(cid:33) (cid:32) n
(cid:88)
i=1
(cid:33)−1
mimT
i + Σ
97
(4.54)
Cap´ıtulo 4. Aprendizaje no Supervisado
(cid:32) n
(cid:88)
=
ximT i
(cid:33) (cid:32) n
(cid:88)
mimT
i + Σ
(cid:33)−1
(4.55)
i=1 A continuaci´on se computar´a la derivada respecto de Ψ y se utilizar´an propiedades
i=1
matriciales [9]:
∂J(W, Ψ) ∂Ψ
= −
n 2
Ψ−1 +
n 2
Ψ−1W ΣW T Ψ−1 +
1 2
n (cid:88)
i=1
Igualando a cero y despejando Ψ:
W ΣW T + (xi − µ − W mi)(xi − µ − W mi)T
Ψ =
=
1 n
1 n
n (cid:88)
i=1 n (cid:88)
i=1
Ψ−1(xi − µ − W mi)(xi − µ − W mi)T Ψ−1
(4.56)
(4.57)
(xi − µ)(xi − µ)T − W mi(xi − µ)T − (xi − µ)mT
i W T + W (mimT
i + Σ)W T
Utilizando la expresi´on anteriormente encontrada de W : (cid:34) n n (cid:88)
(cid:88)
(xi − µ)(xi − µ)T − W
Ψ =
1 n
i=1
i=1
(cid:35)
mixT i
(4.58)
(4.59)
Cabe aclarar que, dado que nuestro modelo impone un Ψ diagonal, nos terminamos quedando con la diagonal de la matriz encontrada (solo importa derivar con respecto a los elementos de la diagonal). En definitiva, el algoritmo EM en este caso propone iterar entre un paso E (4.48) y un paso M definido por las expresiones (4.55) y (4.59).
Demostraci´on 4.5 (Incorporar µ en el algoritmo EM) Se desea demostrar que al incorporar µ a la recursi´on EM, con condici´on inicial µ(0) = 1 i=1 xi, µ(t) = µ(0) n para todo t ∈ N. Como las recursiones de EM solo dependen del paso anterior, es suficiente con mostrar que µ(1) = µ(0) (el resto de la demostraci´on es inducci´on). Esto es v´alido siempre y cuando se verifique que su valor tampoco depende del resto de par´ametros que si se va actualizando.
(cid:80)n
Es importante notar que la expresi´on (4.48) asegura, al menos, (cid:80)n
i=1 m(1)
i = 0.
Redefiniendo la funci´on a minimizar teniendo en cuenta la media n (cid:88)
J(µ, W, Ψ) = g(W, Ψ) −
(xi − µ − W mi)T Ψ−1(xi − µ − W mi)
1 2
i=1
y derivando respecto de µ se obtiene
∂J(µ, W, Ψ) ∂µ
= −
n (cid:88)
i=1
Ψ−1(xi − µ − W mi)
Por lo tanto, igualando a cero esta derivada puede observarse que: n (cid:88)
n (cid:88)
(cid:16)
(cid:17)
xi − W (1)m(1)
i
=
µ(1) =
1 n
1 n
xi
i=1
i=1
98
(4.60)
(4.61)
(4.62)

# 5


# Procesamiento de Datos orientado a Aplicaciones Espec´ıficas

El algoritmo no manda, castiga ni interroga, sino que sugiere, optimiza y predice. Esa suavidad operativa no lo vuelve menos violento, sino que m´as eficaz, porque captura al sujeto desde sus deseos y lo vuelve c´omplice de su propia subordinaci´on.
TODO

## 5.1. Procesamiento de Audio


### 5.1.1. Espectrograma


### 5.1.2. Coeficientes Mel-Cepstrum


## 5.2. Procesamiento de Texto


## 5.3. Sistemas de Recomendaci´on


## 5.4.


## Ingenier´ıa de Caracter´ısticas


### 5.4.1. Test de Independencia Chi-Cuadrado


### 5.4.2. Tests ANOVA

Comparaci´on medias de normales varianza conocida Comparaci´on medias de normales
varianza desconocida Coparaci´on de varianza de normales Asint´otico
99

# 6


# Modelos Bayesianos

Es tan cierto que la inteligencia artificial solamente reproduce datos, como que los datos lo reproducen todo. Ley de los Grandes N´umeros.
Tras una implementaci´on particularmente dif´ıcil de un algoritmo, los programadores suelen desconfiar de cu c´odigo y probarlo con un ejemplo trivial. Si lo supera comienzan a probar dicho c´odigo con ejemplos m´as y m´as complejos. Cuando el c´odigo ya super´o cuatro o cinco pruebas de ´estas, el programador empieza a creer que posiblemente no haya errores en ese c´odigo. En esto consiste el pensamiento bayesiano: actualizar las creencias tras considerar nueva evidencia [6].

## 6.1.


## Inferencia Bayesiana

La estad´ıstica bayesiana, discutida en la Secci´on 1.2.4, posee caracter´ısticas particulares. Su filosof´ıa radica en buscar verdades en contextos de incertidumbre, modelando no solo el problema a resolver sino tambi´en nuestra ignorancia sobre el mismo [7]. Algunas de las caracter´ısticas t´ecnicas son:
Sea T una variable aleatoria representativa de los par´ametros y las variables no observables del modelo, con distribuci´on a priori pT (θ).
La estad´ıstica bayesiana supone una relaci´on causal T → X, donde X es cualquier conjunto aleatorio de muestras a observar.
La relaci´on anterior implica la independencia entre las muestras cuando se conoce el par´ametro. Es decir que la verosimilitud de una muestra puede escribirse como pX|T =θ(x) = (cid:81)n
i=1 pX|T =θ(xi).
La distribuci´on a posteriori es proporcional al producto de la prior y la verosimilitud
pT |X=x(θ) ∝ pT (θ) ·
pX|T =θ(xi)
(6.1)
n (cid:89)
i=1
100
Cap´ıtulo 6. Modelos Bayesianos
Por ´ultimo, se define la distribuci´on predictiva bayesiana como:
(cid:90)
pXtest|X=x(xtest) =
pX|T =θ(xtest)pT |X=x(θ)dθ = E [p(xtest|T )|X = x]
(6.2)
donde Xtest es una variable aleatoria no vista en el conjunto de entrenamiento X.
Θ
A continuaci´on se presenta un ejemplo de como calcular anal´ıticamente este tipo de
distribuciones.
Ejemplo 6.1 Lucas dispara a un blanco y el disparo impacta en un punto aleatorio (X, 0) con X (en dec´ımetros) una variable aleatoria con distribuci´on normal de media nula y varianza 1/τ , donde τ representa la precisi´on de Lucas. A priori la precisi´on τ tiene una distribuci´on chi-cuadrado de 8 grados de libertad. Lucas tiro 10 veces al blanco y observ´o (cid:80)10
i = 17. En virtud a la informaci´on muestral,
i=1 x2
1. Hallar la distribuci´on a posteriori.
2. Hallar la distribuci´on predictiva.
Como primer paso en un problema bayesiano, hay que comenzar planteando la distribuci´on a posteriori. En este caso evitaremos las constantes de proporcionalidad:
pT |X=x(τ ) ∝ pT (τ ) ·
n (cid:89)
i=1
pX|T =τ (xi) ∝ τ 3e−τ /21{τ > 0} ·
10 (cid:89)
√
i=1
τ e− τ
2 x2 i
(6.3)
donde se utiliz´o la informaci´on de que la versoimilitud es normal y la distribuci´on a priori es chi-cuadrado (v´ease Cuadro 1.2). Utilizando el dato muestreal del enunciado, podemos observar que pT |X=x(τ ) ∝ τ 8e−9τ 1{τ > 0}, es decir que la variable se distribuye a posteriori como T |X=x ∼ Γ(9, 9) (v´ease Cuadro 1.2). La distribuci´on predictiva es de la forma
pXtest|X=x(xtest) =
pX|T =τ (xtest)pT |X=x(τ )dτ ∝
(cid:90)
(cid:90) ∞
√
τ e− τ
2 x2
test · τ 8e−9τ dτ
(6.4)
Reconociendo el n´ucleo de la integral, se puede observar que el mismo es proporcional
Θ
0
a la densidad de una Γ(ν, β). Sabiendo que por ser densidad debe integrar 1:
pXtest|X=x(xtest) ∝
(cid:90) ∞
−τ
17 2 e
τ
(cid:18)
9+
x2 test 2
(cid:19)
(cid:18)
dτ ∝
9 +
(cid:19)− 19
2
(6.5)
x2 test 2
0 2 . Es decir que la densidad predictiva es proporcional , y por lo tanto es una t-student de 18 grados de
2 y λ = 9 + x2 donde se utiliz´o ν = 19 (cid:17)− 18+1 (cid:16) 1 + x2
a pXtest|X=x(xtest) ∝ libertad Xtest|X=x ∼ t18 (v´ease Cuadro 1.2).
test 18
test
2
Tanto a priori como a posteriori, la variable T es una Gamma (la chi-cuadrado es un caso particular de Gamma). Este fen´omeno de mantenerse dentro de una familia ocurre por cierta compatibilidad entre la distribuci´on a priori y la verosimilitud (en este caso una normal). Cuando se da este fen´omeno se dice que la distribuci´on a priori es una conjugada a priori. Las soluciones anal´ıticas suelen proponer conjugadas, como distribuci´on
101
Cap´ıtulo 6. Modelos Bayesianos
U
V
X
Y
Figura 6.1: Ejemplo de red bayesiana, donde se puede apreciar tanto relaciones de causalidad como independencia.
a priori, ya que as´ı garantizan que la distribuci´on a posteriori pertenezca a una familia conocida (la misma que la distribuci´on a priori ). Es simplemente una recomendaci´on para hacer sencillos (o al menos factibles) los c´alculos. Los problemas de la estad´ıstica bayesiana, pueden representarse f´acilmente con grafos denominados redes bayesianas.

### 6.1.1. Redes Bayesianas

Se denomina modelo gr´afico a todo modelo probabil´ıstico capaz de representarse con un grafo. En particular el modelado bayesiano es un modelo gr´afico. Existen diferentes grafos que se pueden utilizar para describir los modelos, siendo las redes bayesianas el est´andar en este tipo de estad´ıstica.
Se denomina red bayesiana a un grafo ac´ıclico dirigido que representa la relaci´on de causalidad e independencia de sus variables [7, Secci´on 3.5]. Por un lado, la causalidad est´a determinada por la direcci´on de sus v´ınculos y presenta una configuraci´on a implementar para generar muestras del modelo (v´ease Secci´on 4.1). Por otro lado, dos variables aleatorias cualesquiera son condicionalmente independientes dados los valores de sus padres causales (y por lo tanto las ra´ıces son independientes).
En la Fig. 6.1 puede verse un ejemplo de red bayesiana, donde el color gris hace referencia a las variables observables. La causalidad nos indica como podr´ıamos simular el modelo:
Muestrear U , ya que es ra´ız del grafo: u ← U ∼ pU .
Muestrear X|U = u, ya que a su nodo le llega una conexi´on desde U : x ← X ∼ pX|U =u.
Muestrear V |U = u: v ← V ∼ pV |U =u.
Muestrear Y |U = u, W = w: y ← Y ∼ pY |U =u,W =w.
Este an´alisis es conceptual, en la pr´actica no se habitual generar muestras de variables observables. Adem´as, el procedimiento antes descripto nos define la factorizaci´on de la
102
Cap´ıtulo 6. Modelos Bayesianos
Figura 6.2: Ejemplo Secci´on 6.1.2, representa los mensajes recibidos durante los diferentes d´ıas. El ejemplo fue tomado de [6].
distribuci´on conjunta:
pXY U V (x, y, u, v) = pU (u) · pX|U =u(x) · pV |U =u(v) · pY |U =u,W =w(y)
(6.6)
Esta factorizaci´on nos impone condiciones de independencia. Por ejemplo, dado U = u, X y V son independientes ya que:
(cid:82)
pXV |U =u(x, v) =
Y pXY U V (x, y, u, v)dy pU (u)
= pX|U =u(x) · pV |U =u(v)
(6.7)

### 6.1.2. Ejemplo de Modelo Bayesiano

La esencia de la estad´ıstica bayesiana es interpreta la probabilidad como una medida de credibilidad en un evento, es dice buscar verdades en contexto de incertidumbre. La falta de certeza en las ciencias emp´ıricas, lejos de volverlas absurdas, permite evitar afirmar m´as de lo que se sabe sin ocultar lo que efectivamente se conoce. Los m´etodos bayesianos no solo pueden adaptarse a intentar resolver los mismos problemas que la estad´ıstica frecuentista (por ejemplo predicciones), sino que tambi´en pueden intentar resolver problemas donde la estad´ıstica cl´asica es insuficiente o iluminar el sistema subyacente con un modelado m´as flexible. Veamos el siguiente ejemplo [6].
Un usuario proporciona una serie de recuentos diarios de mensajes de whatsapp enviados. Tiene curiosidad por saber si los h´abitos de env´ıo de mensajes han cambiado con el tiempo. En la Fig. 6.2 puede verse la cantidad de mensajes recibidos en los diferentes d´ıas. La hip´otesis es que el arribo de mensajes ten´ıa cierta tendencia y en alg´un momento cambio a otra diferente. Se desea plantear un modelo capaz de representar esta informaci´on.
La cantidad de mensajes en un d´ıa deber´a ser modelada como una variable discreta cuyos ´atomos es N0. Por ejemplo, se elegir´a una Xi ∼ Poi(λi). Esta ser´a la ´unica variable observable del modelo. Analizando los datos, parecer´ıa que el valor de λi aumenta en alg´un momento durante las observaciones. ¿C´omo podemos representar matem´aticamente esta
103
Cap´ıtulo 6. Modelos Bayesianos
i=1,...,n
λi
Xi
β1
β2
τ
Figura 6.3: Red bayesiana del modelo propuesto para caracterizar el arribo de mensajes.
observaci´on? Supongamos que alg´un d´ıa τ durante el per´ıodo de observaci´on, el par´ametro λi se incrementa repentinamente. Entonces realmente tenemos dos tasas: una para el per´ıodo anterior a τ y otro para el resto del per´ıodo:
 
λi =

β2
i ≥ τ
β1
i < τ
(6.8)
Tanto β1 como β2 toman valores reales no negativos. Por ejemplo, se puede elegir β1, β2 ∼ E(α). Es importante notar que se definen como variables aleatorias independientes e id´enticamente distribuidas (para evitar sesgar a alguna tasa). En este punto, uno podr´ıa definir α como variable aleatoria o asignarle un valor fijo. Asignar un valor fijo para α ser´ıa menos influyente en el modelo que haberlo asignado en los λs, b´asicamente por estar m´as lejos de la variable observable a nivel grafo. Por el contrario, ser´ıa m´as influyente que suponerlo una variable aleatoria y asignarle un valor a los par´ametros de esta nueva variable. Para este an´alisis, donde solamente se quiere estudiar el cambio de tasa, es suficiente con fijar un valor razonable. Notar que
E[Xi] = E [E[Xi|λi]] =
 

E [β1]
i < τ
E [β2]
i ≥ τ
=
1 α
(6.9)
1 (cid:80)n i=1 Xi
1 n
es un buen candidato a valor. La ´ultima variable a definir es por lo que α = τ . Debido a la varianza de los datos, es dif´ıcil caracterizarla en detalle. Podemos asignar entonces la creencia menos informativa posibles a priori τ ∼ U {1 : n}, donde se asumir´a τ independiente de β1 y β2.
En la Fig. 6.3 puede verse la red bayesiana del modelo descripto. La potencia del modelado bayesiano radica en poder modelar f´acilmente situaciones pr´acticas donde la estad´ıstica cl´asica parece quedarse corta. El problema est´a en que calcular la distribuci´on predictiva de un modelo de estas caracter´ısticas es computacionalmente inviable, al menos
104
Cap´ıtulo 6. Modelos Bayesianos
Y

# · · ·

X1
Xd
Figura 6.4: Red bayesiana del modelo gr´afico bayes naive. Los predictores son independientes conocida la clase.
de forma exacta. En el resto del cap´ıtulo iremos analizando las fortalezas y debilidades de algunos modelos gr´aficos, llendo de las m´as simples a las m´as complejas incrementando el potencial poco a poco.

## 6.2. Bayes Naive

Uno de los modelos gr´aficos m´as f´aciles de analizar son los conocido como bayes naive. La hip´otesis naive en un problema de clasificaci´on modela una relaci´on de causalidad Y → X, donde las diferentes componentes Xj|Y =k son independientes, tal como puede verse en la red bayesiana de la Fig. 6.4. En este tipo de modelos, la probabilidad asignada a cada clase, cuando se observa una muestra, es de la forma:
p(y|x) ∝ p(y)
d (cid:89)
j=1
p(xj|y)
(6.10)
Estos modelos se llaman bayes naive por combinar la hip´otesis naive con la regla de bayes de (6.10). No es necesariamente un modelo bayesiano en el sentido de interpretar los par´ametros como variables aleatorias ni mucho menos calcular una predictiva. De hecho, el c´alculo de una predictiva en bayes naive se suele volverse prohibitivo ya que implica resolver la integral sobre una productoria [7, Secci´on 9.3].
Est´a claro que dif´ıcilmente en la pr´actica las componentes ser´an independientes dada la clase a la que pertenecen, de ah´ı radica el nombre de naive (ingenuo). Sin embargo, proponer modelos simples puede ser beneficioso incluso si no se cumplen el la pr´actica, ya que este tipo de modelos suele poseer menos par´ametros y por lo tanto necesita menos datos para ser entrenado.
La simpleza de bayes naive, radica en la separaci´on del modelo Xj|Y =k para cada clase. Nos permite modelar cada clase por separado para finalmente combinarlas por una p(y) usualmente estimada con la proporci´on de muestras de entrenamiento de esa clase: Y ∼ Cat({c1, · · · , cK}) con ck = #{yi=k} . A continuaci´on vamos a estudiar dos modelos bayes naive que utilizan estimadores puntuales: el primero de la estad´ıstica cl´asica y el segundo del modelado bayesiana propiamente dicha.
n
105
Cap´ıtulo 6. Modelos Bayesianos

### 6.2.1. Bayes Naive Gaussiano

El modelo bayes naive gaussiano (GNB) propone modelar el problema como una (k)), donde los
mezcla de gaussianas naives: Y ∼ Cat({c1, · · · , cK}) y Xj|Y =k ∼ N (µ(k) j par´ametros ser´an estimados utilizando los estimadores est´andar.
, σ2 j
Este modelo est´a muy relacionado con los modelos de LDA y QDA estudiados anteriormente. Los tres m´etodos asumen un modelo de mezclas de gaussianas, su diferencia radica en las hip´otesis que hacen sobre las matrices de covarianza, como puede verse en la Fig. 6.5. Sea Σk la matriz de covarianza asociadas a la clase k-´esima.
QDA acepta como covarianza cualquier conjunto de matrices definidas positiva. Suelen estimarse como Σk = 1
(x − µ(k)) (cid:0)x − µ(k)(cid:1)T .
(cid:80)
|Dk|−1
x∈Dk
LDA acepta como coviarianza cualquier matriz (definida positiva) pero todas deben iguales. A partir de las matrices de covarianza de QDA, la covarianza de LDA puede computarse como Σ = 1
(cid:80)K
k=1(|Dk| − 1)Σk.
n−K
GNB permite tener matrices diferentes pero todas deben ser diagonales diagonales. A partir de las matrices de covarianza de QDA, las covarianzas de GNB pueden , · · · , σ2(k) computarse como Σk = DIAG
(cid:17)
(cid:16)
.
σ2(k) 1
d
(cid:80)
x∈Dk
|Dk|−1
(xj − µ(k)
j )2, pero el resultado final ser´ıa el mismo.
Por razones computacionales, en el caso de GNB, no se calcula toda la covarianza para luego quedarse con la ra´ız. En cambio, suele implementarse un c´alculo de la forma σ2(k) j = 1 QDA es el modelo m´as completo de los tres, pero al necesitar estimar mayor cantidad de par´ametros requiere mayor cantidad de muestras para ser entrenado correctamente. Entre GNB y LDA, la cantidad de par´ametros ser´a superior en un caso o en el otro seg´un la relaci´on entre la cantidad de clases K y la cantidad de predictores d. De cualquier manera, no solo es importante tener en cuenta la cantidad de par´ametros, sino que tan bien representadas est´an las hi´otesis en el conjunto de datos con el que se cuenta.

### 6.2.2. Bayes Naive Multinomial

El modelo bayes naive multinomial (MNB) propone modelar para cada clase Y = k un proceso de Bernoulli generalizado Xj|Y = k ∼ Cat({θ(k) V }), donde se respeta la hi´otesis naive. Hablamos de proceso en este caso, porque queremos definir un modelo capaz de entregar muestras de dimensi´on variable. Este tipo de modelado suele utilizarse en procesamiento de texto, donde cada texto posee una cantidad diferente de palabras. A su vez, supondremos que cada clase posee probabilidad ck, es decir, Y ∼ Cat({c1, · · · , cK}).
1 , · · · , θ(k)
106
Cap´ıtulo 6. Modelos Bayesianos
(a)
(b)
(c)
Figura 6.5: Comparaci´on de algoritmos para un ejemplo de dos dimensiones. (a) Modelo LDA, (b) modelo QDA, y (c) modelo GNB. La diferencia de sus modelos radica en las covarianzas de cada clase.
Para una muestra d-dimensional x = (x1, · · · , xd), (6.10) puede escribirse como:
p(y|x) ∝ cy ·
d (cid:89)
j=1
θ(y) xj
= cy ·
V (cid:89)
m=1
(cid:0)θ(y)
m
(cid:1)Nm
(6.11)
donde Nm representa la cantidad de variables Xj que tomaron el valor m y son estad´ısticos suficientes en este modelo. El cambio de variable en la productoria nos permite iterar en los valores m que pueden tomar los predictores, en lugar necesitar iterar en la cantidad j de los mismos. Sea N = (N1, · · · , NV ), no solamente se puede notar que (cid:80)V m=1 Nm = d, sino que tambi´en nos define la distribuci´on multinomial de estos estad´ısticos N|Y =k ∼ Mn(d, [θ(k) V ]). El uso de este estad´ıstico nos permite resolver la inferencia como una soluci´on lineal de la log-probabilidad
1 , · · · , θ(k)
log p(y|x) = cte + log(cy) +
V (cid:88)
m=1
Nm log (cid:0)θ(y)
m
(cid:1)
(6.12)
1 , · · · , θ(k) simplemente hay que haber estimado previamente los par´ametros ck y (θ(k) todo k = 1 · · · , K. Estos par´ametros ser´an estimados en la etapa de entrenamiento.
V ) para
6.2.2.1. Entrenamiento de MNB
La probabilidad de cada clase ser´a simplemente estimada por la proporci´on de muestras , como suele hacerse en cualquier
que hay en el conjunto de entrenamiento ck = #{yi=k} modelo naive. Los θs en cambio ser´an modelados de forma bayesiana.
n
Supongamos que contamos con un datos {(Ni, yi)}n
i=1, donde cada muestra Ni tendr´a asociada una cantidad de predictores d diferente. Debido a la hip´otesis naive, es v´alido separar los problemas por clase. Es decir que para cada clase k se utilizar´an solamente
107
Cap´ıtulo 6. Modelos Bayesianos
los datos con {yi = k} distribuidos seg´un las probabilidades (θ(k) V ). A su vez, dado que las variables Nm cuentan ocurrencias, puedo compactar todas las muestras de entrenamiento de cada clase en una sola, utilizando suficiencia estad´ıstica de las variables categ´oricas
1 , · · · , θ(k)
n (cid:88)
˜N (k)
m =
Ni,m · 1{yi = k}
(6.13)
i=1
Esto quiere decir por ejemplo, que en un problema de procesamiento de texto, podemos pensar que tenemos un solo texto por clase, concatenando todos los textos de dicha clase en uno solo. Esto implica que ( ˜N (k) V ]), donde ˜d(k) representa la cantidad de “palabras” que posee el “texto concatenado” de la clase k. Notar que hemos definido una variable aleatoria Tk representativa de los par´ametros del modelo. Dicha variable ser´a modelada a priori como Tk ∼ Dir([α1, · · · , αV ]), donde el vector aleatorio tendr´a distribuci´on Dirichlett.
V ) ∼ Mn( ˜d(k), [θ(k)
1 , · · · , θ(k)
V )|Tk=(θ(k)
, · · · , ˜N (k)
1 ,··· ,θ(k)
1
Definici´on 6.1 El vector aleatorio (θ1, · · · , θV ) tiene distribuci´on Dirichlett de par´ametros (α1, · · · , αV ) si su densidad conjunta es de la forma: (cid:81)V m=1 Γ(αm) (cid:88) (cid:17) (cid:16)(cid:80)V m=1 αm
p(θ1, · · · , θV ) =
θm = 1, θm ≥ 0
θαm−1 m
(6.14)
(cid:40) V
(cid:32) V
(cid:89)
· 1
m=1
m=1
(cid:41)
(cid:33)
Γ
La principal propiedad de este tipo de vectores es que sus marginales posee distribuη̸=m αη), una variable aleatoria utilizada para modelar probabi- . Con este modelo, la distribuci´on a posteriori
ci´on beta Tm ∼ β(αm, (cid:80) lidades cuya esperanza es E[Tm] = αm puede calcularse como:
η=1 αη
(cid:80)V
(cid:16)
p
1 , · · · , θ(k) θ(k) (cid:16) ˜N (k)
V | ˜N (k) , · · · , ˜N (k)
1
∝ P
1
, · · · , ˜N (k)
V
(cid:17)
1 , · · · , θ(k)
V
(cid:17)
(cid:16)
· p
1 , · · · , θ(k) θ(k)
(cid:17)
(cid:32) V
(cid:89)
∝
(θ(k)
m ) ˜N (k)
m
m=1
V |θ(k) (cid:33) (cid:32) V
(cid:89)
m=1 ∼ Dir([ ˜N (k)
(θ(k)
m )αm−1 · 1 (cid:8)θ(k)
m ≥ 0(cid:9)
· 1
V (cid:33)
(cid:41)
θ(k) m = 1
(cid:40) V
(cid:88)
m=1
(6.15)
(6.16)
con lo cu´al Tk| ˜N (k) como estimador puntual bayesiano la media a posteriori se obtiene que
V + αV ]). De esta manera, utilizando
,··· , ˜N (k)
1 + α1, · · · , ˜N (k)
V
1
m = E[Tm| ˜N (k) θ(k)
1
, · · · , ˜N (k)
V ] =
˜N (k)
m + αm ˜N (k)
η + αη
η=1
(cid:80)V
.
(6.17)
Mientras que GNB es un modelo gr´afico con estimadores puntuales cl´asicos, MNB utiliza estimadores puntuales bayesianos. Sin embargo, todav´ıa nos estamos conformando con hacer una estimaci´on puntual en lugar de un c´alculo predictivo. A continuaci´on veremos cuanto es necesario complejizar al modelo para efectivamente poder hacer dicho c´alculo.
108
Cap´ıtulo 6. Modelos Bayesianos

## 6.3. Bayes Variacional Gaussiano

La estad´ıstica bayesiana basa su supuesto en considerar a los par´ametros parte del espacio latente, los que se sumar´an a las variables no observables propias del modelo (como la variable mezcladora en un problema de clustering). Sea Z el vector de variables no observable, en general ser´a prohibitivo calcular la distribuci´on a posteriori p(z|x) en modelos complejos. Una alternativa es aproximar dicha distribuci´on minimizando la divergencia de Kullback Leibler:
arg m´ın q∈P
KL (q(·|x)∥p(·|x))
(6.18)
donde q(z|x)1 cumple ciertas restricciones P que permitan limitar el modelo posible de forma que sea factible emplear un estudio anal´ıtico. Dicha divergencia puede descomponerse como KL (q(·|x)∥p(·|x)) = log p(x) − ELBO(q(·|x)), donde
ELBO(q(·|x)) = H(q(·|x)) + Eq [log p(x, Z)|X = x]
(6.19)
donde H(q(·|x)) representa la entrop´ıa como funci´on de x. Similar al algoritmo EM, la cota inferior esperada (ELBO) acota la verosimilitud de forma maximizar una cota fomente la maximizaci´on de la misma ELBO(q(·|x)) ≤ log p(x) (ya que la divergencia de Kullback Leibler es no negativa). Esta log-verosimilitud debe ser entendida por muestra, por lo que la para la log-verosimilitud de un conjunto simplemente se sumar´ıan los ELBOs. A su vez, este mismo fen´omeno se da acotando a:
ELBO(q) = Eq [− log p(x|z)|x] − KL (q(·|x)∥p(·)) ≤ Eq [− log p(x|z)|x]
(6.20) donde Eq [− log p(x|z)|x] es la entrop´ıa cruzada asociada a un autoencoder de encoder q(·|x) y decoder p(·|z). Es decir que la maximizaci´on de la ELBO tambi´en tender´a a aumentar dicha magnitud.
Minimizar la divergencia de Kullback Leibler (6.18) equivale a maximizar la ELBO. Para poder tratar el problema, se suele asumir como restricci´on sobre P la llamada Mean field approximation: Suponer que q se puede factorizar como productos de densidades tratables, separando entre las variables ocultas u y los par´ametros ϕ. Es decir, sea z = (u, ϕ) se relaja el problema suponiendo q(z|x) = q1(u|x)q2(ϕ|x) para todo q ∈ P. Con esta hip´otesis, la entrop´ıa de la distribuci´on producto se descompone como suma H(q(·|x)) = H(q1(·|x)) + H(q2(·|x)) y la esperanza del logaritmo de la conjunta se puede descomponer en dos sentidos:
Eq [log p(x, Z)|X = x] =
(cid:90)
q1(u|x)
q2(ϕ|x)
U (cid:90)
=
(cid:18)(cid:90)
Φ
(cid:18)(cid:90)
(cid:19)
q2(ϕ|x) log p(x, u, ϕ)dϕ
du
(6.21)
q1(u|x) log p(x, u, ϕ)du
dϕ
(6.22)
(cid:19)
U El algoritmo bayes variacional propone resolver el problema (6.18) de forma iterativa:
Φ
1Notar que estamos haciendo un an´alisis para toda la muestra x.
109
Cap´ıtulo 6. Modelos Bayesianos
i=1,...,n xi
π
ui
k=1,...,K
µk
λk
Figura 6.6: Red bayesiana del modelo bayes variacional gaussiano.
suponer q1 fijo para optimizar en q2 para luego dejar fijo q2 para optimizar en q1. (cid:90)
q1(·|x) = arg m´ax
q1(u|x) log
q1
U (cid:90)
Φ
q2(u|x) log
eE1(x,u) q1(u|x) eE2(x,ϕ) q2(ϕ|x)
du
dϕ
q2(·|x) = arg m´ax
q2
donde
E1(x, u) =
E2(x, ϕ) =
(cid:90)
Φ
(cid:90)
U
q2(ϕ|x) log p(x, u, ϕ)dϕ ≡ f (q2)
q1(u|x) log p(x, u, ϕ)du ≡ f (q1)
(6.23)
(6.24)
(6.25)
(6.26)
El problema de optimizaci´on (6.23) equivale a minimizar la divergencia de Kullback Leibler entre q1(u|x) y k1eE1(x,u), donde k1 es una constante de proporcionalidad para que la expresi´on sea una densidad/probabilidad en u. De manera similar ocurre con q2(ϕ|x) y k2eE2(x,ϕ) para el problema (6.24). Entonces, el algoritmo bayes varaicional consiste en iterar entre q1(u|x) ∝ eE1(x,u) y q2(ϕ|x) ∝ eE2(x,ϕ).

### 6.3.1. Mezcla de Gaussianas escalares en Bayes Variacional

Para entender las complicaciones para efectuar los c´alculos, incluso en un problema simple, supongamos el modelo de mezcla de gaussianas escalares graficado en la Fig. 6.6. Este problema se lo conoce como Bayes Variacional Gaussiano (GVB) [20, Secci´on 10.2]. Interpretando su red bayesiana, la distribuci´on del modelo puede escribirse como
p(x, u, π, λ, µ) = p(π)
p(λk)p(µk|λk)
P (ui|π)p(xi|ui, µ, λ)
(6.27)
(cid:32) K (cid:89)
(cid:33) (cid:32) n (cid:89)
(cid:33)
k=1
i=1
donde u|π ∼ Cat(π) y x|u, µ, λ ∼ N (µu, λ−1 u ). A priori supondremos distribuciones conjugadas a priori con la verosimilitud: π ∼ Dir(α), λk ∼ Γ(ν, β) y µk|λk ∼ N (m, (δλk)−1). Los par´ametros de este modelo ser´an entonces α, ν, β, m y δ. En este caso u = (u1, · · · , un) y ϕ = (π, µ, λ) con π = (π1, · · · , πK), µ = (µ1, · · · , µK) y λ = (λ1, · · · , λK). Un caso particular cuando K = 1 y δ → ∞ fue estudiando en el Ej. 6.1, donde la distribuci´on a posteriori de la precisi´on (inversa de la varianza) es una Gamma y la distribuci´on predic-
110
Cap´ıtulo 6. Modelos Bayesianos
tiva es una t-student.
Utilizar como distribuci´on a priori una media gaussiana y una precisi´on Gamma, es una familia muy estudiada en la bibliograf´ıa y recibe el nombre de distribuci´on normalgamma.
Definici´on 6.2 Un vector aleatorio normal-gamma (ν, β, m, δ) tiene una densidad conjunta de la forma:
(cid:114)
p(λ, µ) =
βν Γ(ν)
−λ
λν− 1 2 e
δ 2π
(cid:18) β+ δµ2
2 −δmµ+ δm2
2
(cid:19)
1{λ > 0}
(6.28)
donde λ ∼ Γ(ν, β) y µ|λ ∼ N (m, (δλ)−1).
Teniendo en cuenta todas estas definiciones, a continauci´on se proceder´a a calcular la distribuci´on a posteriori y la predictiva del modelo.
6.3.1.1. Distribuci´on a posteriori en GVB
Bajo la hip´otesis mean field approximation, q(u, π, λ, µ|x) = Q1(u|x)q2(π, λ, µ|x), por
lo que
E1(x, u) = cte +
n (cid:88)
(cid:90)
i=1
q2(π|x) log P (ui|π)dπ +
n (cid:88)
(cid:90) (cid:90)
i=1
q2(µ, λ|x) log p(xi|ui, µ, λ)dµdλ
(6.29)
donde “cte” hace referencia t´erminos que no dependen de q2. De forma an´aloga
E2(x, π, λ, µ) = log p(π) +
+
+
n (cid:88)
K (cid:88)
i=1
n (cid:88)
k=1 K (cid:88)
i=1
k=1
K (cid:88)
k=1
log p(λk) +
K (cid:88)
k=1
log p(µk|λk)
Q1(ui = k|x) log P (ui = k|π)
Q1(ui = k|x) log p(xi|ui = k, µ, λ)
(6.30)
En primer lugar, se considerar´a Q1 fijo y conocido para computar q2. Esto se conoce como actualizaci´on de los par´ametros a posteriori. Es decir, asumiendo que las familias elegidas son conjuntadas a priori, los par´ametros a priori son α, ν, β, m y δ tendr´an sus contra-partes a posteriori α∗, ν∗, β∗, m∗ y δ∗ (los cuales puede ser diferentes para cada clase). Lo primero a notar es la factorizaci´on. Sea γi,k = Q1(ui = k|x), luego q2(π, λ, µ|x) ∝ eE2(x,π,λ,µ):
q2(π, λ, µ|x) ∝ p(π)
p(λk)p(µk|λk)
(cid:32) K (cid:89)
(cid:33) K (cid:89)
(cid:80)n e
i=1 γi,k[log πk+log N (xi|µk,λ−1
k )]
(6.31)
k=1
k=1
y por lo tanto q2(π, λ, µ|x) = q2(π|x) (cid:81)K k=1 q2(µk, λk|x) (es decir, se acaba de demostrar la relaci´on de independiencia, resta calcular q2(π|x) y q2(µk, λk|x) para cada k). Dado que
111
Cap´ıtulo 6. Modelos Bayesianos
el logaritmo de la densidad normal es una magnitud cuadr´atica en las muestras, podemos definir los siguientes estad´ısticos suficientes:
n (cid:88)
n (cid:88)
n (cid:88)
Nk =
γi,k,
fk =
γi,kxi,
sk =
γi,kx2 i
(6.32)
y por lo tanto, el ´ultimo exponente de (6.31) puede simplificarse como:
i=1
i=1
i=1
Nk log πk −
Nk 2
log(2π) +
Nk 2
log(λk) −
λk 2
(sk − 2fkµk + Nkµ2 k)
(6.33)
Para computar q2(π|x), basta por juntar los t´erminos de (6.31) donde aparece π
(cid:32) K (cid:89)
(cid:33)
(cid:40) K (cid:88)
(cid:41)
q2(π|x) ∝
παk−1 k
eNk log πk
1
πk = 1, πk ≥ 0
(6.34)
k=1
k=1
con lo cual π|x ∼ Dir([α1 + N1, · · · , αK + NK]), es decir α∗ q2(µk, λk|x), resta analizar:
q2(µk, λk|x) ∝ λν−1
k
(cid:124)
e−βλk1{λk > 0} (cid:125)
(cid:123)(cid:122) ∝p(λk)
λ1/2 k e (cid:124)
−δλk (µk −m)2 2
(cid:123)(cid:122) ∝p(µk|λk)
(cid:125)
Nk λ k e 2
k = αk + Nk. Para el c´alculo de
−λk (sk −2fk µk +Nk µ2 k ) 2
(6.35)
ν+ ∝ λ k
Nk 2 − 1
2
−λk
e
(cid:18)
β+
δµ2 2 −δmµk+ δm2 k
2 +
sk 2 −fkµk+
(cid:19)
Nk µ2 k 2
1{λk > 0}
(6.36)
Se puede apreciar que esta distribuci´on es una normal-gamma. Para calcular los par´ametros a posteriori basta con comparar la expresi´on con (6.28) (con los par´ametros a posteriori ν∗
k, β∗
k, m∗
k, δ∗
k) y despejar:
k − 1 ν∗
2 = ν + Nk
2 − 1 2.
δ∗ 2 = δ+Nk k
2
.
k = δm + fk.
km∗ δ∗ k + δ∗ β∗
2
km∗ 2 = β + δm2 k
2 + sk 2 .
Es decir, ν∗
k = ν + Nk
2 , δ∗
k = δ + Nk y m∗
k = δm+fk δ+Nk
. Para el caso de β∗
k, se puede calcular
como:
β∗ k = β +
δm2 2
+
sk 2
−
(δm + fk)2 2(δ + Nk)
(6.37)
(cid:16) δm+fk δ+Nk
con lo cual µk|λk, x ∼ N
2sk − (δm+fk)2 2(δ+Nk) En segundo lugar, se considerar´a q2 fijo y conocido para calcular Q1. Esto se conoce como actualizaci´on de la distribuci´on de las variables ocultas. Para calcular dicha distribuci´on, se utilizar´an las siguientes propiedades de las distribuciones Gamma y Beta.
2Nk, β + δm2
y λk|x ∼ Γ
1 λk(δ+Nk)
2 + 1
ν + 1
,
(cid:17)
(cid:16)
(cid:17)
.
Propiedades 6.1 Sean λ ∼ Γ(ν, β) y π ∼ β(a, b), la esperanza del logaritmo de estas variables se calcula como E[log λ] = ψ(ν)−log(β) y E[log π] = ψ(a)−ψ (a + b),
112
Cap´ıtulo 6. Modelos Bayesianos
donde ψ(·) es la funci´on digamma ψ(z) = Γ′(z) Γ(z) .
Lo primero a notar para el c´omputo de Q1(u|x) ∝ eE1(x,u) es la independencia de sus
variables:
Q1(u|x) ∝
n (cid:89)
i=1
(cid:82) q2(π|x) log P (ui|π)dπ+(cid:82) (cid:82) q2(µ,λ|x) log p(xi|ui,µ,λ)dµdλ =
e
n (cid:89)
i=1
Q1(ui|x)
(6.38)
entonces basta con calcular cada Q1(ui = k|x). Sean los par´ametros de q2 definidos como π|x ∼ Dir(α∗), µk|λk, x ∼ N (m∗
k, (δ∗
k, β∗ kλk)−1) y λk|x ∼ Γ (ν∗ k )−log(β∗ k ) c)+ − 1 2 2
c=1 α∗
k)−ψ((cid:80)K
k). Luego Eq2 [λk(xi−µk)2|x]
ψ(ν∗
(6.39)
η̸=k α∗
η). La esperanza de la ´ultima expresi´on puede
Q1(ui = |x) ∝ eψ(α∗ k, (cid:80)
donde se us´o que πk|x ∼ β(α∗ calcularse con
Eq2[λk(xi − µk)2|x] = Eq2[λkEq2[(xi − µk)2|λk, x]|x] = Eq2[λkEq2[(xi − m∗ k + m∗ = Eq2[λk ν∗ k β∗ k
k)2 + Eq2[(µk − m∗ 1 δ∗ k
k − µk)2|λk, x]|x]
(cid:0)(xi − m∗
(xi − m∗
k)2 +
+ 0
=
k)2|λk, x] + 2(xi − m∗
k)Eq2[m∗
k − µk|x](cid:1) |x]
Finalmente, se puede despejar una f´ormula para las probabilidades: (m∗
ψ(α∗
ψ(ν∗
−
k)−ψ((cid:80)K
c=1 α∗
c)+
k )−log(β∗ k ) 2
k−xi)2
− 1 2δ∗ k
ν∗ k 2β∗ k
Q1(ui = k|x) ∝ e
(6.40)
(6.41)
(6.42)
(6.43)
(6.44)
En resumen, la distribuci´on a posteriori en un problema de GVB se calcula inicializando
γi,k (por ejemplo con el algoritmo EM) e iterando entre:
Calcular (α∗
k, m∗
k, δ∗
k, ν∗
k, β∗
k) a partir de γi,k como
n (cid:88)
α∗
k = αk +
γi,k, m∗
k =
i=1 n (cid:88)
δ∗ k = δ +
γi,k,
ν∗ k = ν +
β∗ k = β +
i=1
δm2 2
+
1 2
n (cid:88)
i=1
γi,kx2
i −
δm + (cid:80)n δ + (cid:80)n
i=1 γi,kxi i=1 γi,k n (cid:88)
γi,k
1 2 (δm + (cid:80)n 2(δ + (cid:80)n
i=1
i=1 γi,kxi)2 i=1 γi,k)
Calcular γi,k = ρi,k
(cid:80)K
c=1 ρi,c
a partir de (α∗, m∗
ψ(α∗
k)−ψ((cid:80)K
c=1 α∗
c)+
ρi,k = e
k, ν∗ k, δ∗ k, β∗ k) como k )−log(β∗ ψ(ν∗ ν∗ k ) − 1 k 2β∗ 2δ∗ 2 k k
−
(m∗
k−xi)2
(6.45)
(6.46)
(6.47)
(6.48)
6.3.1.2. Distribuci´on Predictiva en GVB
Por un lado, la distribuci´on a posteriori q2 estimada durante el entrenamiento cumple la relaci´on de independencia q2(π, λ, µ|x) = q2(π|x) (cid:81)K k=1 q2(µk, λk|x). Por el otro, una nueva muestra xtest (que no pertenezca al conjunto de entrenaimento x) pertenecer´a a un modelo de mezcla p(xtest|π, µ, λ) = (cid:80)K k ). Juntando ambas consideraciones
k=1 πk · N (xtest|µk, λ−1
113
Cap´ıtulo 6. Modelos Bayesianos
podemos ver que la distribuci´on predictiva tambbi´en es una mezcla:
p(xtest|x) = E[p(xtest|ϕ)|x] K (cid:88)
E[πk|x] · E
=
(cid:34) (cid:114)
λk 2π
e
−λk 2 (xtest−µk)2
(cid:35)
x
(cid:12) (cid:12) (cid:12) (cid:12) (cid:12)
k=1 K (cid:88)
=
k=1
k, (cid:80)
α∗ k c=1 α∗ c
(cid:80)K
· ˜pk(xtest|x)
(6.49)
(6.50)
(6.51)
donde se utiliz´o que πk|x ∼ β(α∗ η). La distribuci´on predictiva es una mezcla cuyos pesos son la proporci´on de los α∗; resta calcular las nuevas densidades ˜pk(xtest|x). Para ello, notar que (µk, λk)|x tienen una distribuci´on normal-gamma (6.28) de par´ametros (ν∗
η̸=k α∗
k, β∗
k, m∗
k, δ∗
k):
˜pk(xtest|x) ∝
∝
(cid:90) ∞
(cid:90) ∞
0 (cid:90) ∞
−∞ (cid:90) ∞
0
−∞
(cid:112)
λke
k − 1 ν∗ −λk 2 (xtest−µk)2λ k
2
−λk e
(cid:18)
β∗ k+
k µ2 δ∗ 2 −δ∗ k
km∗
kµk+
2
(cid:19)
km∗ δ∗ k 2
dµkdλk (6.52)
(cid:18)
β∗ k+
−λk
λν∗ k e
δ∗ k µ2 2 −δ∗ k
km∗
kµk+
2 km∗ δ∗ k 2 +
µ2 k 2 −xtestµk+
x2 test 2
(cid:19)
dµkdλk
(6.53)
Nuevamente el interior de la integral es una distribuci´on normal-gamma. Como toda densidad integra 1, basta con reconocer los par´ametros (˜ν, ˜β, ˜m, ˜δ) de la nueva distribuci´on para resolver la integral. Igualando con (6.28), se obtiene:
˜ν − 1
2 = ν∗
k
2 + 1
2
k
2 = δ∗ ˜δ ˜δ ˜m = δ∗
km∗
k + xtest k + δ∗
˜β + ˜δ ˜m2
2 = β∗
2
km∗ 2 + x2 k
test 2
k + 1
2, ˜δ = δ∗
k + 1 y
km∗ k
˜m = xtest+δ∗ δ∗ k+1 ˜β = β∗
De las primeras tres ecuaciones es inmediato notar que ˜ν = ν∗ . Para la ecuaci´on de ˜β basta con notar que (xtest + δ∗ km∗ δ∗ k 2(δ∗ 2 km∗ (δ∗ k
x2 test 2 2 + x2 test)(δ∗
km∗
k +
k)2
k)2
−
+
2
= β∗
k +
km∗ k + 1) k + 1) − (xtest + δ∗ 2(δ∗ 2 + δ∗
k + 1) kx2
test + x2 2(δ∗
test − x2 k + 1)
test − 2δ∗
km∗
kxtest − δ∗ k
= β∗
k +
= β∗
k +
δ∗ k
2m∗ k
2 + δ∗
km∗ k
k(xtest − m∗ δ∗ k + 1)
2(δ∗
k)2
(6.54)
(6.55)
(6.56)
(6.57)
2
2m∗ k
Como en la ´unica variable que aparece xtest es en ˜β, podemos decir que la integral es
˜pk(xtest|x) ∝ ˜β−˜ν, es decir:
˜pk(xtest|x) ∝
(cid:18)
β∗ k +
(cid:19)−(ν∗
k +1/2)
(6.58)
δ∗ k(xtest − m∗ k + 1)
2(δ∗
k)2
114
Cap´ıtulo 6. Modelos Bayesianos
(cid:18)
∝
1 +
δ∗ kν∗ k k + 1)β∗ k
(δ∗
(xtest − m∗ 2ν∗ k
k)2
2ν∗ k +1 2
(cid:19)−
(6.59)
Este tipo distribuci´on se conoce como t-student generalizada.
(6.60)
(6.61)
Definici´on 6.3 Una variable aleatoria tiene distribuci´on t-Student Generalizada: X ∼ t(µ, Λ, ν) si su densidad es de la forma (cid:18)
(cid:19)− ν+1
(cid:114)
2
p(x) =
(cid:1) Γ (cid:0) ν+1 (cid:1) Γ (cid:0) ν
2
2
Λ πν
1 + Λ
(x − µ)2 ν
Por lo tanto, la densidad predictiva es una mezcla de t-students de la forma:
p(xtest|x) =
K (cid:88)
k=1
α∗ k c=1 α∗ c
(cid:80)K
(cid:18)
· t
xtest
(cid:12) (cid:12) (cid:12) (cid:12)
m∗ k,
kν∗ δ∗ k k + 1)β∗ k
(δ∗
(cid:19)
, 2ν∗ k
Al ser una mezcla, esta distribuci´on permite hacer predicciones (en el sentido frecuen-
tista de la palabra) para el problema de clustering asociado ˜p(k|xtest, x) donde
˜p(k|xtest, x) ∝
α∗ k c=1 α∗ c
(cid:80)K
(cid:18)
· t
xtest
m∗ k,
(cid:12) (cid:12) (cid:12) (cid:12)
δ∗ kν∗ k k + 1)β∗ k
(δ∗
(cid:19)
, 2ν∗ k
(6.62)
donde en el caso de necesitar una predicci´on dura se quedar´a con su argumento m´aximo. Finalmente hemos analizado la distribuci´on predictiva de un modelo relativamente simple. Incluso en modelos escalares, que propongan distribuciones conjugadas a priori, el estudio anal´ıtico es complejo. Esto demuestra la necesidad de contar con m´etodos num´ericos que permitan abordar el tema.

## 6.4. Monte Carlo por Cadenas de Markov (MCMC)

Efectuar el c´alculo con distribuciones predictivas, evaluando la integral directamente, puede ser computacionalmente inviable ya que rara vez se cuenta con una forma cerrada o conocida para la distribuci´on a posteriori. Para resolver este problema, se plantea una soluci´on Monte Carlo: combinar m´etodos de muestreo con la ley de los grandes n´umeros.
E [p(xtest|T )|X = x] ≈
1 tmax
tmax(cid:88)
t=1
pX|T =θt(xtest)
(6.63)
donde θ1, · · · , θtmax son muestras generadas a partir de la distribuci´on a posteriori.
En cap´ıtulos anteriores se discuti´o por que la inteligencia artificial no es m´as que una mezcla de patrones encontrados en datos observados con ruidos aleatorios. Sin embargo, la ley de los grandes n´umeros nos muestra el potencial de los datos: cualquier comportamiento esperado puede aproximarse tan bien como uno desee si se cuenta la cantidad de datos suficiente. Este resultado da que pensar acerca de como y cuando entregamos nuestros datos. Quiz´as estemos alimentando nuestro reemplazo.
115
Cap´ıtulo 6. Modelos Bayesianos
El problema con este m´etodo es que dif´ıcilmente podamos generar muchas muestras independientes. Es entonces cuando surge el Muestreo Monte Carlo por Cadenas de Markov (MCMC) como una alternativa [20, Cap´ıtulo 11]. Una cadena de Markov es una secuencia de variables aleatorias {θt}t∈N que cumple la propiedad de falta de memoria: la distribuci´on del pr´oximo estado depende ´unicamente del estado actual, y no del pasado completo. Formalmente,
p(θt+1|θt, θt−1 · · · , θ0) = p(θt+1|θt) = P (θt → θt+1)
(6.64)
donde P (θt → θt+1) es la densidad de transici´on de θt a θt+1 (en la estad´ıstica bayesiana todas estas distribuciones ser´an computadas impl´ıcitamente a posteriori de observar los datos de entrenamiento). Cuando las probabilidades de transici´on no dependen del tiempo t, se dice que la cadena es homog´enea. Una distribuci´on π se dice estacionaria para una cadena de Markov si no var´ıa su estad´ıstica al propagarse por la cadena;
(cid:90)
π(θ′) =
π(θ)P (θ → θ′) dθ
(6.65)
es decir, que la distribuci´on de θ y θ′ sea la misma (que la distribuci´on de θ no var´ıe al efectuar un paso en la cadena). Una condici´on suficiente para asegurar esto es que la conjunta de ambas sea sim´etrica:
π(θ)P (θ → θ′) = π(θ′)P (θ′ → θ)
(6.66)
la cual se cumple de forma trivial si θ = θ′ (repetir el estado actual no afecta la condici´on (6.66) correspondiente al estado estacionario).
La idea general del MCMC es construir una cadena de Markov homog´enea {θt}t∈N cuya distribuci´on estacionaria sea la distribuci´on a posteriori. Bajo ciertas condiciones, el teorema de ergodicidad garantiza que el promedio de los valores generados por la cadena converge a la esperanza, dando por v´alida (6.63) aunque no se trate de muestras independientes. Para una cadena de Markov homogenea, dichas condiciones se pueden resumir en:
Irreducible: La transici´on θ → θ′ debe poder ser alcanzada en una cantidad finita de pasos para todo θ y θ′.
´Aperi´odica: La transici´on θ → θ (mantener el estado actual) debe tener probabilidad positiva.
Recurrente positiva: El tiempo esperado para volver al estado actual es finito.
Los algoritmos utilizados para los modelos bayesianos fueron construidos para cumplir con estas condiciones. A continuaci´on se presentar´a un ejemplo de c´alculo para calcular el estado estacionario de una cadena de Markov homog´enea.
116
Cap´ıtulo 6. Modelos Bayesianos
Ejemplo 6.2 Encontrar el estado estacionario de una cadena de Markov homog´enea, donde θ es una variable discreta que toma valores en {0, 1, 2} y las probabilidades de 

transici´on se definen con la matriz P =
0.7 0.2 0.1 0.4 0.6 0.0 0.0 0.9 0.1
 
 .
No es dif´ıcil probar que esta cadena es irreducible, aperi´odica y recurrente positiva. Toda cadena de Markov irreducible en un espacio de estados finitos tiene una distribuci´on estacionaria ´unica. Se desea encontrar π(0), π(1) y π(2) (representadas por un vector π), tal que se cumpla (6.65). Para variables discretas y finitas eso se puede representar como π = P · π con 1T · π = 1, donde 1 es un vector con todas sus entradas en 1. Escribiendo todo eso como un sistema de ecuaciones se obtiene

   
0.7 0.2 0.1 0.4 0.6 0 0.9 0.1 0 1 1 1

   

·
 
π(0) π(1) π(2)

  =

   

   
π(0) π(1) π(2) 1
(6.67)
La segunda ecuaci´on 0.4π(0) + 0.6π(1) = π(1) implica que π(0) = π(1). De la tercera 0.9π(1) + 0.1π(2) = π(2) se obtiene que π(1) = π(2). Reemplazando podemos ver que se cumple la primera ecuaci´on 0.7π(0) + 0.2π(1) + 0.1π(2) = π(0) y, dado que deben sumar 1 (cuarta ecuaci´on), se obtiene π(0) = π(1) = π(2) = 1 3.

### 6.4.1. Algoritmos de Muestreo MCMC

El objetivo de los algoritmos de muestreo es generar un proceso cuya secuencia de muestras sea erg´odica. Esto no siempre es sencillo, ya que puede no disponerse de toda la informaci´on necesaria sobre las distribuciones.
En la Fig. 6.7 puede verse un ejemplo de experimento de muestreo. Se denomina tune a la cantidad de muestras a descartar para considerar que se alcanz´o el estado estacionario, y draws a la cantidad de muestras efectivas que fueron generadas. Se suelen generar varias cadenas y verificar los resultados en cada una (cantidad definida en chains). Una disparidad de resultados en las cadenas evidencia que no se alcanz´o el mencionado estado estacionario. Dependiendo del tipo de variable aleatoria a muestrear, conviene usar una u otra estrategia. A continuaci´on se presentar´an algunos de los muestreos m´as habituales.
6.4.1.1. Muestreo de Gibbs
Supongamos que, debido a su complejidad, no podemos simular muestras de π(x, y), pero que s´ı es posible generar muestras de las condicionales π(x|y) y π(y|x) (conocidas y
117
Cap´ıtulo 6. Modelos Bayesianos
tune = 4
θ(1) 0
θ(1) 1
θ(1) 2
θ(1) 3
θ(1) 4
θ(1) 5
θ(1) 6
θ(1) 7
θ(1) 8
θ(1) 9
θ(1) 10
θ(2) 0
θ(2) 1
θ(2) 2
θ(2) 3
θ(2) 4
θ(2) 5
θ(2) 6
θ(2) 7
θ(2) 8
θ(2) 9
θ(2) 10
3 = s n i a h c
θ(3) 0
θ(3) 1
θ(3) 2
θ(3) 3
θ(3) 4
θ(3) 5
θ(3) 6
θ(3) 7
θ(3) 8
θ(3) 9
θ(3) 10
Figura 6.7: Ejemplo de experimento de muestreo. En este caso se simularon tres cadenas independientes (chains = 3), se esperaron cuatro pasos para considerar que se alcanz´o el estado estacionario (tune = 4) y se recolectaron siete muestras efectivas en el presunto estado estacionario (draws = 7).
draws = 7
f´aciles de muestrear). El muestreo de Gibbs consiste en, a partir de un x0, iterar alternadamente entre yt ∼ π(y|xt) y xt+1 ∼ π(x|yt). Luego de suficientes pasos, al alcanzar el estado estacionario, los pares (x, y) estar´an distribuidos por π(x, y). En la siguiente secci´on se demostrar´a por qu´e este proceso cumple (6.66).
Esta t´ecnica se extiende a m´as dimensiones muestreando de una componente a la vez. El problema con este muestreo es que es necesario conocer perfectamente todas las distribuciones condicionales, lo cual en la pr´actica suele ser problem´atico en muchos casos. Una excepci´on importante la constituyen las variables Bernoulli, donde se pueden computar todas las probabilidades necesarias.
A continuaci´on se demostrar´a que el muestreo de Gibbs posee a la distribuci´on a pos-
teriori como estado estacionario y se mostrar´a un ejemplo de aplicaci´on.
Demostraci´on 6.1 (Estado estacionario) Notar que, en esta cadena de Markov donde θ = (x, y) , el proceso evoluciona como
(x0, y0) → (x1, y0) → (x1, y1) → (x2, y1) → (x2, y2) → (x3, y2) → (x3, y3) → · · ·
(6.68) Para corroborar que cumple la condici´on suficiente de estacionariedad (6.66) to-
memos un paso de Gibbs (xt, yt) → (xt+1, yt):
π(xt, yt)π(xt+1|yt) = π(xt+1, yt)π(xt|yt)
(6.69)
donde todas las distribuciones son computadas a posteriori (la notaci´on queda impl´ıcita). Es f´acil notar que, si la medida de probabilidad es la misma, la identidad (6.69) representa la misma distribuci´on conjunta de (xt, yt, xt+1) en ambos lados de la igualdad.
118
Cap´ıtulo 6. Modelos Bayesianos
Ejemplo 6.3 Sea la distribuci´on correspondiente al modelo gr´afico: P (x, y) ∝ exT a+yT b+xT W y · 1{x ∈ {0, 1}dx, y ∈ {0, 1}dy }
(6.70)
donde {a, b, w} son valores conocidos. Explicar el procedimiento para muestrear esta distribuci´on utilizando muestreo de Gibbs.
Este tipo de distribuci´on se conoce como modelo de Boltzmann restringido. Supongamos que buscamos muestrear esta distribuci´on utilizando el muestreo de Gibbs. Se puede ver que la constante de proporcionalidad ser´ıa computacionalmente pesada de buscarla para altas dimensiones, pero sus condicionales son m´as sencillas. Empezando por P (y|x), se puede ver que sus componentes son independientes:
P (y|x) ∝ e(b+W T x)T y · 1{y ∈ {0, 1}dy } =
dy (cid:89)
j=1
e[b+W T x]j yj · 1{yj ∈ {0, 1}}
(6.71)
y por lo tanto P (yj = 1|x) ∝ e[b+W T x]j y P (yj = 0|x) ∝ 1. Juntando esta informaci´on puede verse que y|x ∼ Ber(σ(b + W T x))2 es una vector Bernoulli de componentes independientes. An´alogamente, puede deducirse que x|y ∼ Ber(σ(a + W y)).
En este caso, podr´ıan generarse muestras inicializando x0 y k = 0 e iterando entre:
Se genera un yk a partir de Ber(σ(b + W T xk)).
Se genera un xk+1 a partir de Ber(σ(a + W yk)).
k ← k + 1.
6.4.1.2. Muestreo Metropolis
El muestreo Metropolis es usado t´ıpicamente en variables aleatorias discretas no binarias (como Poisson, geom´etrica, hipergeom´etrica, etc.) que toman valores en los enteros Z, as´ı como tambi´en en variables continuas donde no hay diferenciabilidad debido al modelo. Su caracter´ıstica esencial es que solamente le basta con conocer la distribuci´on (conjunta, de todos los par´ametros simult´aneamente) salvo una constante de proporcionalidad. Es decir que si π(θ) = f (θ) Z con Z > 0, es suficiente con conocer f (θ) (que habitualmente se plantea como distribuci´on a priori por la verosimilitud).
Este tipo de muestreo propone transicionar de θt a θt+1 con el siguiente algoritmo
sim´etrico:
1. Se genera una θ′ = θt + δ, donde δ es una variable aleatoria; en el caso que θ′ no est´e en el soporte de la variable (por ejemplo una Poisson no puede tomar valores negativos), se repite el proceso. Para el caso discreto, t´ıpicamente se propone que
2La funci´on sigmoide es σ(z) = 1
1+e−z = ez
ez+1 .
119
Cap´ıtulo 6. Modelos Bayesianos
δ ∼ U{−1, 0, 1} (uniforme discreta de 3 ´atomos) y para el caso continuo se propone δ ∼ N (0, σ2).
2. Se sortea una variable aleatoria Bernoulli de probabilidad α(θt, θ′). Si dicha variable
vale 1, θt+1 = θ′. Caso contrario θt+1 = θt.
donde
α(θa, θb) = m´ın
1,
(cid:26)
(cid:27)
f (θb) f (θa)
(6.72)
con π(θ) = f (θ) Z (no depende de la constante de normalizaci´on). A continuaci´on se efectuar´a un an´alisis para demostrar´a que la distribuci´on a posteriori cumple la condici´on de estacionariedad dada por (6.66).
Demostraci´on 6.2 (Estado Estacionario - Caso Discreto) La probabilidad de transici´on del caso discreto descripta anteriormente es de la forma
P (θt → θt+1) =

 
α(θt,θt−1) 3
α(θt,θt+1) 3
θt+1 = θt − 1
θt+1 = θt + 1
1 − α(θt,θt−1)+α(θt,θt+1)
3
θt+1 = θt
0
Otros
(6.73)
El ´unico caso no trivial que vale la pena analizar en (6.66) es que ocurre si θt+1 =
θt ± 1; en los dem´as casos, la condici´on se cumple autom´aticamente. En este caso
Se puede ver que si π(θ) = f (θ)
π(θt)
= π(θt+1)
α(θt, θt+1) 3
α(θt+1, θt) 3 Z , la ecuaci´on en cuesti´on puede reducirse a
f (θt)α(θt, θt+1) = f (θt+1)α(θt+1, θt)
(6.74)
(6.75)
Utilizando el α(θa, θb) definido en (6.72), se puede comprobar la identidad (6.75). El primer t´ermino cumple que f (θt)α(θt, θt+1) = m´ın{f (θt), f (θt+1}, y de forma an´aloga para el otro t´ermino f (θt+1)α(θt+1, θt) = m´ın{f (θt+1), f (θt)}. De esta manera, queda garantizando que la distribuci´on a posteriori es un estado estacionario de la cadena.
Demostraci´on 6.3 (Estado Estacionario - Caso Continuo) La transici´on del caso continuo tiene una distribuci´on mixta: una mezcla entre una normal y una masa puntual (delta de Dirac) en θt+1 = θt. Dado que el ´unico caso relevante a chequear de (6.66) es el caso donde θt+1 ̸= θt, basta con analizar la parte continua: P (θt → θt+1) = α(θt, θt+1) · N (θt+1|θt, σ2) donde N (x|µ, σ2) hace referencia a la densidad de
120
Cap´ıtulo 6. Modelos Bayesianos
una normal de par´ametros µ y σ2 evaluada en x. En este caso la condici´on (6.66) puede escribirse como:
π(θt) · α(θt, θt+1) · N (θt+1|θt, σ2) = π(θt+1) · α(θt+1, θt) · N (θt|θt+1, σ2)
(6.76)
La condici´on anterior puede reducirse a f (θt)α(θt, θt+1) = f (θt+1)α(θt+1, θt) usando que la normal es sim´etrica respecto a la media N (θt|θt+1, σ2) = N (θt+1|θt, σ2). De esta manera llegamos a la misma identidad que en el caso discreto y por lo tanto, podemos concluir que la distribuci´on a posteriori cumple la condici´on de estacionariedad (6.66).
6.4.1.3. NUTS (No-U-Turn Sampler)
El algoritmo NUTS (No-U-Turn Sampler) es un m´etodo de muestreo, basado en Metr´opolis, para variables aleatorias continuas con distribuci´on a posteriori diferenciable. La versi´on completa del algoritmo [26] puede verse en la Fig. 6.8; a continuaci´on se presentar´an las ideas generales. En lugar de sumar un ruido aleatorio, el algoritmo introduce una variable auxiliar r ∈ Rd cuyo objetivo es actuar como direcci´on de exploraci´on de la distribuci´on a posteriori. Esta variable se genera en cada iteraci´on a partir de una distribuci´on normal est´andar multivariada. A partir de ella se define la funci´on de energ´ıa como:
H(θ, r) = − log π(θ) +
1 2
∥r∥2
(6.77)
Esta funci´on de energ´ıa combina la log-posterior de θ con una penalizaci´on cuadr´atica sobre r y tiene un papel central en la determinaci´on de la calidad de las propuestas. En cada iteraci´on, partiendo del estado actual (θt, r), el algoritmo genera una secuencia de nuevas propuestas (θ, r) mediante un m´etodo num´erico que utiliza la informaci´on del gradiente de la energ´ıa. Este procedimiento se conoce como integraci´on tipo leapfrog, y consiste en aplicar transformaciones que mantengan aproximadamente constante el valor de H(θ, r). As´ı como el gradiente descendente desplaza los par´ametros hacia la direcci´on de decrecimiento de la funci´on objetivo, la integraci´on leapfrog desplaza los par´ametros sobre una curva de nivel de H(θ, r). Durante la etapa tune, leapfrog ajustar´a el paso del algoritmo para que el nivel de aceptaci´on de un nuevo estado sea target_accept (par´ametro predefinido por el usuario).
Una caracter´ıstica distintiva de NUTS es que, en lugar de requerir un n´umero fijo de pasos de integraci´on (como en otros algoritmos relacionados), a partir de θt, construye din´amicamente un ´arbol de posibles (θ, r), expandi´endose hacia adelante y hacia atr´as, hasta que detecta que continuar expandiendo llevar´ıa a una regi´on ya visitada o a una direcci´on contraria a la actual, seg´un un criterio geom´etrico. Esta condici´on de detenci´on
121
Cap´ıtulo 6. Modelos Bayesianos
Figura 6.8: Algoritmo NUTS presentado por Hoffman en [26].
122
Cap´ıtulo 6. Modelos Bayesianos
V
W
X
Figura 6.9: Ejemplo de modelado de 3 variables V → W → X, donde la ´unica variable observable es X.
se conoce como la “No-U-Turn”. Una vez elegido un candidato (θ′, r′), se acepta el cambio θt+1 = θ′ con una determinada probabilidad, por el contrario, se decide por θt+1 = θt.
Una vez finalizado este per´ıodo, el algoritmo congela sus par´ametros de control y comienza a generar las muestras v´alidas. En el contexto de modelos con par´ametros continuos, NUTS es especialmente eficiente en espacios de alta dimensi´on, ya que genera propuestas informadas por la geometr´ıa local de la distribuci´on, evitando caminatas aleatorias ineficientes y generando muestras con menor autocorrelaci´on. Esto lo convierte en el algoritmo por defecto en muchas librer´ıas bayesianas modernas como PyMC.
6.4.1.4. Ejemplo de Modelo Complejo
En la Fig. 6.9 se muestra un ejemplo de modelado con tres variables V → W → X, donde la ´unica variable observable es X = x. Supongamos que a priori V ∼ exp(2), que W |V =v ∼ Poi(v) y que X|W =w ∼ χ2(w + 1). En este caso, las cadenas se generan con el siguiente procedimiento.
1. Se inicializa v0, usualmente utilizando una muestra de la distribuci´on a priori exp(2).
2. Se inicializa w0, a partir de su distribuci´on latente Poi(v0) o eventualmente con
Poi(0.5) (usando la media de V en lugar de su valor).
3. Se actualiza V , definiendo v1. Como V es una variable aleatoria continua con densidad derivable, habitualmente se utilizar´a NUTS aplicando sobre la distribuci´on a posteriori π(v, w0) ∝ p(x|w0)P (w0|v)p(v) ∝ Poi(w0|v)·exp(v|2), donde Poi(·|µ) es la funci´on de probabilidad de una Poisson de media µ y exp(·|λ) es la funci´on de densidad de una exponencial de intensidad λ. En este caso se absorbi´o la verosimilitud como constante de proporcionalidad por no depender v.
4. Se actualiza W , definiendo w1. Al tratarse de una variable discreta, se recomienda utilizar el muestreo Metr´opolis. Para el muestreo se utilizar´a la distribuci´on a posteriori π(v1, w) ∝ p(x|w)P (w|v1)p(v1) = χ2(x|w + 1) · Poi(w|v1) donde χ2(·|ν) es la funci´on de densidad de una chi-cuadrado de ν grados de libertad. En este caso se absorbi´o la distribuci´on a priori p(v1) como constante de proporcionalidad por no depender w.
123
Cap´ıtulo 6. Modelos Bayesianos
5. Se repite el paso (3) definiendo v2 y se contin´ua iterando la cantidad de pasos que
sea necesario.

### 6.4.2. Calidad de las muestras

Para evaluar la calidad de las muestras de un experimento de MCMC, suelen considerarse dos propiedades: la ergodicidad y la estacionariedad. Gracias al teorema de ergodicidad, podemos aproximar esperanzas a partir de promedios sin pretender que las muestras sean independientes. El problema radica en que la velocidad de convergencia y la varianza de dicho promedio no son las mismas que en el caso de variables independientes. En MCMC, se denomina tama˜no de muestra efectiva (Effective Sample Size, ESS) a la cantidad de datos independientes necesarios para alcanzar la misma varianza que posee el promedio de las muestras. Se define como
ESS =
tmax 1 + 2 (cid:80)kmax
t=1 ρt
(6.78)
donde ρt es la autocorrelaci´on de la cadena y kmax es el valor a partir del cual las autocorrelaciones se vuelven peque˜nas o negativas. La ecuaci´on (6.78) ser´a demostrada m´as adelante. Esta ESS se conoce como bulk y se utiliza para c´alculos predictivos. Para intervalos de confianza suele usarse otro ESS denominado tail.
Otra caracter´ıstica importante, adem´as de la ergodicidad, es verificar si las muestras fueron generadas una vez alcanzado el estado estacionario. Supongamos que se cuenta con una simulaci´on con varias cadenas independientes. Si todas convergieron a la misma distribuci´on, entonces la varianza entre cadenas deber´ıa ser similar a la varianza dentro de cada cadena. Se denomina R-hat (o ˆR, tambi´en conocido como diagn´ostico Gelman–Rubin) al cociente entre estas varianzas. Si las cadenas a´un no convergieron, habr´a m´as variabilidad entre las mismas, y ˆR ser´a mayor que 1. En la pr´actica suele considerarse ˆR > 1.01 una se˜nal de alerta y un valor ˆR > 1.1 suele considerarse un problema a resolver.
Demostraci´on 6.4 (C´alculo de ESS) En c´alculo predictivo num´erico, la hip´otesis de trabajo es aproximar una esperanza con el promedio de las densidades pX|T =θi(x) en lugar de los par´ametros pero, en la pr´actica, se suele analizar la varianza de los par´ametros para estandarizar resultados. No ser´ıa particularmente complejo trabajar con las verosimilitudes evaluadas en los par´ametros, pero no hay grandes diferencias. En ´ultima instancia, bajo ciertas condiciones de regularidad, deber´ıan ser comparables ambas ESS.
Sea θ1, · · · , θtmax un conjunto de muestras id´enticamente distribuidas y sea ¯θ el promedio de las mismas; es simple ver que la varianza si fueran independientes ser´ıa de σ2 , la varianza se
ESS , donde σ2 = var(θi). En el caso de existir un ρt = cov(θi,θi+t)
σ2
124
Cap´ıtulo 6. Modelos Bayesianos
puede calcular como:
var(¯θ) = var
(cid:32)
(cid:33)
θt
=
tmax(cid:88)
t=1
1 t2 max
tmax(cid:88)
tmax(cid:88)
i=1
j=1
cov (θi, θj)
(6.79)
1 tmax (cid:32)
=
=
1 t2 max
σ2 tmax
σ2 · tmax + 2σ2
tmax−1 (cid:88)
tmax(cid:88)
(cid:32)
1 + 2
tmax−1 (cid:88)
(cid:18)
1 −
t=1
t tmax
i=1
j=i+1 (cid:19)
· ρt
(cid:33)
ρj−i
(cid:33)
(6.80)
(6.81)
donde se aplic´o el cambio de variables t = j −i. Bajo las hip´otesis usuales en modelos MCMC, es razonable que tanto ρt como 1 − t se vayan achicando a medida que tmax se avanza en la cadena. Los algoritmos suelen truncar la suma, en un kmax, cuando las autocorrelaciones se vuelven peque˜nas o negativas. Con este procedimiento suele ocurrir que kmax ≪ tmax, por lo que despreciando t tmax kmax(cid:88)
se puede aproximar: (cid:33)
(cid:32)
(6.82)
var(¯θ) ≈
σ2 tmax
1 + 2
ρt
t=1
Igualando este resultado con la expresi´on de la varianza para variables indepen-
dientes σ2
ESS, y despejando, se obtiene (6.78) finalizando la demostraci´on.
En resumen, cuando se desarrolla un algoritmo MCMC lo primero a analizar es si se alcanz´o el estado estacionario observando ˆR. Caso contrario se aumentar´a la etapa tune o se reparametrizar´a el modelo (en el caso del muestreo NUTS tambi´en se puede modificar el target_accept). Una vez alcanzado la performance deseada, se procede a evaluar si se cuenta con suficientes muestras para utilizar el teorema erg´odico observando el ESS. En caso no ser suficiente, una primera opci´on ser´ıa aumentar las muuestras draws. Si el problema persiste, se debe volver al inicio mejorando el estado estacionario.

### 6.4.3.


### Introducci´on a PyMC

PyMC es una biblioteca de Python para inferencia estad´ıstica bayesiana, que permite construir modelos probabil´ısticos complejos y realizar inferencia sobre ellos de forma automatizada [6]. Es muy intuitivo de usar, el programador debe simplemente describir el grafo a implementar.
Supongamos que queremos implementar el modelo descripto en la Sec. 6.1.2. El mismo
puede ser definido mediante el siguiente c´odigo
import pymc as pm import numpy as np
125
Cap´ıtulo 6. Modelos Bayesianos
Figura 6.10: Modelo de PyMC generado por model_to_graphviz.
Figura 6.11: Gr´afico de las densidades/probabilidades a posteriori generado la funci´on plot_posterior de PyMC.
count_data = np.loadtxt("txtdata.csv") n_count_data = len(count_data) idx = np.arange(n_count_data) # Index alpha = 1.0/count_data.mean() with pm.Model() as model:
beta_1 = pm.Exponential("beta_1", alpha) beta_2 = pm.Exponential("beta_2", alpha) tau = pm.DiscreteUniform("tau", lower=0, upper=n_count_data - 1) lambda_func = pm.math.switch(tau > idx, beta_1, beta_2) lambda_ = pm.Deterministic("lambda",lambda_func) observation = pm.Poisson("obs", lambda_, observed=count_data)
126
Cap´ıtulo 6. Modelos Bayesianos
pm.model_to_graphviz(model)
donde la ´ultima instrucci´on pm.model_to_graphviz(model) grafic´o la Fig. 6.10 como resultado. El c´odigo describe el grafo dentro del entorno Model, mencionando que datos corresponden a la variable observable (count_data). Para muestrear la distribuci´on a posteriori, basta con utilizar el comando sample indicando en n´umero de draws, tune y chains deseado.
with model:
trace = pm.sample(draws=1000, tune=1000, chains=2)
import arviz as az summary = az.summary(trace, var_names=["beta_1","beta_2","tau"]) print(summary)
donde la funci´on summary nos permite conocer el ESS y el ˆR por variable. El objeto trace contiene las muestras generadas durante el proceso.
beta_1_samples = trace.posterior[’beta_1’].values beta_2_samples = trace.posterior[’beta_2’].values tau_samples = trace.posterior[’tau’].values lambda_samples = trace.posterior[’lambda’].values _ = pm.plot_posterior(trace.posterior[[’beta_1’,’beta_2’,’tau’]])
donde la funci´on plot_posterior gener´o el gr´afico de las densidades/probabilidades a posteriori de la Fig. 6.11.
En el caso de quererse calcular la distribuci´on predictiva o sus derivados (alguna probabilidad, la esperanza, la varianza), se deber´an combinar las muestras de trace para lograrlo (usualmente se recomienda trabajar cada cadena por separado para corroborar que los resultados sean estacionarios). Pero, puede existir el caso donde lo que efectivamente se desee son muestras de la distribuci´on predictiva3. Para ello basta con programar:
with model:
posterior_pred = pm.sample_posterior_predictive(trace,predictions=True)
pred_samples = posterior_pred.predictions[’obs’].values
La funci´on sample_posterior_predictive genera una cantidad de muestras igual a las observadas durante el entrenamiento en cada paso de la cadena. Por lo que si uno desea un solo ejemplo de muestra, podr´ıa quedarse con pred_samples[0,-1]: De la cadena (0) quedarse con el ´ultimo (−1) eslab´on.
3Un muestreo de una distribuci´on aproximada por muestreo. La calidad de estas muestras es menor debido al doble muestreo, por lo que no es recomendable usarlas para estimar la distribuci´on predictiva.
127

# Bibliograf´ıa

[1] W. Feller, An Introduction to Probability Theory and Its Applications, Volume I.
USA: Society for Industrial and Applied Mathematics, 1969.
[2] T. M. Cover and J. A. Thomas, Elements of Information Theory. Wiley Series in
Telecommunications and Signal Processing, Wiley-Interscience, 2006.
[3] R. Duda, P. Hart, and D. Stork, Pattern Classification. John Wiley, 2 ed., 2001.
[4] G. Casella and R. Berger, Statistical Inference. Duxbury advanced series in statistics
and decision sciences, Thomson Learning, 2nd ed., 2002.
[5] P. W. Zehna, “Invariance of Maximum Likelihood Estimators,” The Annals of Mathe-
matical Statistics, vol. 37, no. 3, p. 744, 1966.
[6] C. Davidson-Pilon, Bayesian Methods for Hackers: Probabilistic Programming and
Bayesian Inference. Addison-Wesley Professional, 1st ed., 2015.
[7] K. P. Murphy, Machine Learning: A Probabilistic Perspective. The MIT Press, 2012.
[8] T. Hastie, R. Tibshirani, and J. Friedman, The Elements of Statistical Learning.
Springer Series in Statistics, Springer New York Inc., 2001.
[9] K. Petersen and M. Pedersen, The Matrix Cookbook. Technical University of Den-
mark, 2012.
[10] A. Cauchy, “M´ethode g´en´erale pour la r´esolution des syst`emes d’´equations simul-
tan´ees,” Comp. Rend. Sci. Paris, vol. 25, pp. 536–538, 1847.
[11] D. Wolpert and W. Macready, “No free lunch theorems for optimization,” IEEE
Transactions on Evolutionary Computation, vol. 1, pp. 67–82, April 1997.
[12] T. M. Apostol, Mathematical analysis. Addison-Wesley series in mathematics,
Reading, MA: Addison-Wesley, 1974.
[13] D. G. Luenberger and Y. Ye, Linear and Nonlinear Programming. New York: Sprin-
ger, 3rd ed., 2008.
[14] R. A. Horn and C. R. Johnson, Matrix Analysis. Cambridge University Press, 2nd ed.,
2012.
[15] A. H. Sayed, Adaptive Filters. Hoboken, NJ: Wiley–IEEE Press, 1st ed., Apr. 2008.
Hardcover.
128
Bibliograf´ıa
[16] M. G. Gonz´alez, M. Vera, A. Dreszman, and L. J. Rey Vega, “Diffusion assisted image reconstruction in optoacoustic tomography,” Optics and Lasers in Engineering, vol. 178, 2024.
[17] C. Shannon, “A Mathematical Theory of Communication,” Bell System Technical
Journal, vol. 27, pp. 379–423, 623–656, 1948.
[18] L. Ferrer and D. Ramos, “Evaluating posterior probabilities: Decision theory, proper
scoring rules, and calibration,” Transactions on Machine Learning Research, 2025.
[19] S. Boyd and L. Vandenberghe, Convex Optimization. New York: Cambridge Univer-
sity Press, 2004.
[20] C. M. Bishop, Pattern Recognition and Machine Learning. Information Science and
Statistics, Springer-Verlag New York, Inc., 2006.
[21] I. Goodfellow, Y. Bengio, and A. Courville, Deep Learning. MIT Press, 2016. http:
//www.deeplearningbook.org.
[22] J. Peters, D. Janzing, and B. Scholkopf, Elements of Causal Inference: Foundations
and Learning Algorithms. The MIT Press, 2017.
[23] M. Aigner and G. M. Ziegler, Proofs from THE BOOK. Springer Publishing Com-
pany, Incorporated, 4th ed., 2009.
[24] M. Vera, L. Rey Vega, and P. Piantanida, “Information flow in Deep Restricted Boltzmann Machines: An analysis of mutual information between inputs and outputs,” Neurocomputing, vol. 507, pp. 235–246, 2022.
[25] J. von K¨ugelgen, L. Gresele, and B. Sch¨olkopf, “Simpson’s paradox in covid-19 case fatality rates: A mediation analysis of age-related causal effects,” IEEE Transactions on Artificial Intelligence, vol. 2, no. 1, pp. 18–27, 2021.
[26] M. Hoffman and A. Gelman, “The No-U-Turn sampler: adaptively setting path lengths in hamiltonian monte carlo,” Journal of Machine Learning Research, vol. 15, p. 1593–1623, Jan. 2014.
129