¡Hola Mundo Flask!
==================

> Servidor mínimo de ejemplo de [Flask](https://flask.palletsprojects.com/en/2.2.x/), para el apunte [Introducción a MVC Web del lado del servidor con Flask](https://docs.google.com/document/d/1ZOYhNiR2UBSSIelIVUn2QPFO0OlDbvUqBeOTPc6xFCw/edit#)
>
> Basado en [Hola Mundo Spark](https://github.com/dds-utn/jpa-proof-of-concept-template/tree/hola-mundo-spark) y su correspondiente apunte [Introducción a MVC Web del lado del servidor con Spark](https://docs.google.com/document/d/1EFxqHstgtZ5jI5_plso6nfhvSXXcaT4iyE1qaZuPtXg/edit) y


## Instalación

```bash
# 1. Preparación de entorno. Estos dos primeros comandos son opcionales
$ python -m venv .venv
$ source .venv/bin/activate

# 2. Instalación del proyecto y todas sus dependencias
$ pip install -e .
```

## Inicio del servidor

```bash
# Inicio del entorno. Este paso es opcional.
# Si previamente NO preparaste un entorno, ignorarlo.
# De igual forma, si YA ejecutaste este comando en esta terminal, ignorarlo
$ source .venv/bin/activate

# Inicio del servidor
$ flask --debug --app hmf run --port 9000
```