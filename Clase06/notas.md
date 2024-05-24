## NumPy arange vs linspace

### Arange

**Inicio**, **Limite**(excluido), **Paso**

También podés crear vectores a partir de un rango de valores:

```python
>>> np.arange(4)
array([0, 1, 2, 3])
```

También un vector que contiene elementos equiespaciados, especificando el primer número, el límite, y el paso.

```python
>>> np.arange(2, 9, 2) # o np.arange(2, 10, 2)
array([2, 4, 6, 8])
```

El límite derecho nunca está en la lista.

## Linspace

**Inicio**, **Limite**, **Cantidad de elementos**

También podés usar np.linspace() para crear un vector de valores equiespaciados especificando el primer número, el último número, y la cantidad de elementos:

```python
>>> np.linspace(0, 10, num=5)
array([ 0. ,  2.5,  5. ,  7.5, 10. ])
```

## Numpy axis

axis = 0: columnas
axis = 1: filas

```python
>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> np.max(a, axis=0)
array([4, 5, 6])
>>> np.max(a, axis=1)
array([3, 6])
```
