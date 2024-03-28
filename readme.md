# Web Sitemap Crawler

Este proyecto contiene un script en Python que lee las URLs de los sitemaps de un archivo `sitemaps.txt` y las escribe en un archivo `urls.txt`.

## Descripción

El script `extract-urls.py` realiza las siguientes acciones:

1. Lee las URLs de los sitemaps de un archivo `sitemaps.txt`.
2. Para cada URL de sitemap, hace una solicitud GET para obtener el contenido del sitemap.
3. Analiza el contenido del sitemap y extrae todas las URLs.
4. Escribe las URLs en un archivo `urls.txt`.

## Instalación de Python 3

Este proyecto requiere Python 3. Si no lo tienes instalado, puedes descargarlo desde la [página oficial de Python](https://www.python.org/downloads/).

Para instrucciones detalladas sobre cómo instalar Python 3 en Windows, puedes consultar este [manual de instalación](https://misterdigital.es/instalando-python-3-en-windows/).

## Creación del entorno virtual

Para crear un entorno virtual en la carpeta `venv`, ejecuta el siguiente comando:

```bash
python -m venv venv
```

## Requisitos de instalación

Para instalar las dependencias necesarias, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```