¡Hola Mundo Flask!
==================

> Servidor mínimo de ejemplo de [Flask](https://flask.palletsprojects.com/en/2.2.x/), para el apunte [Introducción a MVC Web del lado del servidor con Flask](https://docs.google.com/document/d/1ZOYhNiR2UBSSIelIVUn2QPFO0OlDbvUqBeOTPc6xFCw/edit#)
>
> Basado en [Hola Mundo Spark](https://github.com/dds-utn/jpa-proof-of-concept-template/tree/hola-mundo-spark) y su correspondiente apunte [Introducción a MVC Web del lado del servidor con Spark](https://docs.google.com/document/d/1EFxqHstgtZ5jI5_plso6nfhvSXXcaT4iyE1qaZuPtXg/edit) y


## Instalación

```bash
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -e .
```

## Inicio del servidor

```bash
$ flask --debug --app hmf run --port 9000
```