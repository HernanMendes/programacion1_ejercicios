## 5.1 Debuggear programas

### Assert

El comando `assert` se usa para un control interno del programa. Si la expresión que queremos verificar es `False`, se levanta una excepción de tipo `AssertionError`. La sintaxis de `assert` es la siguiente.

```python
assert <expresion> [, 'Mensaje']
```

Por ejemplo

```python
assert isinstance(10, int), 'Necesito un entero (int)'
```

## **5.3 Comprensión de listas**

**Sintaxis general**

```python
[<expresión> for <variable> in <secuencia> if <condición>]
```

Lo que signigica

```python
resultado = []
for variable in secuencia:
    if condición:
        resultado.append(expresión)
```

La comprensión de listas viene de la matemática (definición de conjuntos por comprensión).

```python
a = [x * x for x in s if x > 0] # Python

a = {x^2 | x ∈ s, x > 0}        # Matemática
```

Tambien es similar a la estructura de las queries en SQL.

Si cambiás los corchetes  (`[`,`]`) por llaves (`{`, `}`), obtenés algo que se conoce como comprensión de conjuntos. Vas a obtener valores únicos.

Ejemplo:

```python
>>> nombres = {s['nombre'] for s in camion}
>>> nombres
{'Caqui', 'Durazno', 'Lima', 'Mandarina', 'Naranja'}
>>>
```

Si especificás pares `clave:valor`, podés 
construir un diccionario. Por ejemplo:

```python
>>> stock = {nombre: 0 for nombre in nombres}
>>> stock
{'Caqui': 0, 'Durazno': 0, 'Lima': 0, 'Mandarina': 0, 'Naranja': 0}
>>>
```