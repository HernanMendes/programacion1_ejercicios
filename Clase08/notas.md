## Piping

Por omisión, la salida impresa es dirigida a sys.stdout (usualmente la pantalla), la entrada se lee de sys.stdin (usualmente el teclado), y la recapitulación de errores es dirigida a sys.stderr (usualmente, la pantalla otra vez).

Las entradas y salidas de stdio pueden estar ligadas al teclado, a la pantalla, a una impresora, a diferentes archivos o incluir cosas más extrañas como pipes, etc.

```bash
bash % python3 prog.py > resultados.txt
# o si no
bash % cmd1 | python3 prog.py | cmd2
```

Esta sintaxis se llama "piping" o redireccionamiento y significa: ejecutar cmd1, enviar su salida como entrada a prog.py invocado desde la terminal, y la salida de éste será la entrada para cmd2.


## Terminación del programa

La terminación y salida del programa se administran a través de excepciones.

```python
raise SystemExit
raise SystemExit(codigo_salida)
raise SystemExit('Mensaje informativo')
```

O, alternativamente:

```python
import sys
sys.exit(codigo_salida)
```

Es estándar que un codigo de salida de 0 indica que no hubo problemas y otro valor, que los hubo, donde el valor indica que tipo de problema hubo.


## El comando #!

Bajo Unix (Linux es un Unix) una línea que comienza con #! ejecutará un script en el intérprete Python. Por ejemplo, si agregás la siguiente línea al comienzo de tu script podés ejecutar directamente el script (sin invocar manualmente a Python en la misma línea).

```python
#!/usr/bin/env python3
# prog.py
```

...

Bajo Linux, para ejecutar el archivo prog.py vas a necesitar habilitar su permiso de ejecución. Podés habilitar este permiso de ejecución así ... (bajo windows esto no es necesario, ya que el programa que estás ejecutando es formalmente el interprete de python):

```bash
bash % chmod +x prog.py
# Ahora lo podés ejecutar
bash % ./prog.py
... salida ...
```

Resumen

    El contrato de una función especifica qué condiciones se deben cumplir para que la función pueda ser invocada (precondición), y qué condiciones se garantiza que serán válidas cuando la función termine su ejecución (poscondición).
    La documentación tiene como objetivo explicar qué hace el código, y está dirigida a quien desee utilizar la función o módulo.
    Es una buena práctica incluir el contrato en la documentación.
    Si una función modifica un valor mutable que recibe por parámetro, eso debe estar explícitamente aclarado en su documentación.
    Los comentarios tienen como objetivo explicar cómo funciona el código y por qué se decidió implementarlo de esa manera, y están dirigidos a quien esté leyendo el código fuente.
    Los invariantes de ciclo son las condiciones que deben cumplirse al comienzo de cada iteración de un ciclo.
