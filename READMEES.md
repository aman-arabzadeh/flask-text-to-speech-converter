# Aplicación web de Texto a Voz

![Estrellas](https://img.shields.io/github/stars/aman-arabzadeh/flask-text-to-speech-converter?style=flat&label=Estrellas)
![Último commit](https://img.shields.io/github/last-commit/aman-arabzadeh/flask-text-to-speech-converter?label=%C3%9Altimo%20commit)
![Tamaño de la imagen (v1.0)](https://img.shields.io/docker/image-size/amankoray/flask-web-gtts-app/v1.0?label=Tama%C3%B1o%20de%20imagen%20%28v1.0%29)
![Pulls de Docker (repo)](https://img.shields.io/docker/pulls/amankoray/flask-web-gtts-app?label=Pulls%20del%20repositorio)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este proyecto es una aplicación web basada en Flask, construida con Python, HTML y CSS.
Convierte texto escrito en voz natural usando Google Text-to-Speech (gTTS).

Creé este proyecto para escuchar textos, artículos y libros en línea en varios idiomas.
Las personas usuarias pueden introducir cualquier texto, elegir un idioma y la app genera un archivo MP3 que puede reproducirse o descargarse.

---

![Process](images/image.png)

---

### Ejemplo de salida de voz

Puedes escuchar un ejemplo del habla generada a continuación:

https://github.com/user-attachments/assets/399f7290-9730-4750-a43a-0c4c80a2cb9a

<p align="center">
  <img src="images/interface.png" width="50%" style="height:auto;" />
</p>

<br>
<p align="center">
  <img src="images/interface2.png" width="50%" style="height:auto;" />
</p>

---

# Imagen de Docker

También he contenedorizado este proyecto usando **Docker**.
Puedes obtener la imagen desde **Docker Hub** y ejecutarla al instante en tu propio sistema — sin configuración manual.

**Repositorio en Docker Hub:**
[flask-web-gtts-app](https://hub.docker.com/repository/docker/amankoray/flask-web-gtts-app/general)

### Ejecútalo en 2 pasos sencillos

```bash
# 1. Descarga la imagen desde Docker Hub
docker pull amankoray/flask-web-gtts-app:v1.0

# 2. Ejecuta el contenedor
docker run -p 5000:5000 amankoray/flask-web-gtts-app:v1.0
```

Luego abre tu navegador y visita:
http://localhost:5000

¡Eso es todo! Tendrás la Aplicación web de Texto a Voz funcionando en segundos en tu máquina.

---

## Enlaces úti

- [Documentación de Flask](https://flask.palletsprojects.com/en/stable/)
- [gTTS (Google Text-to-Speech) en PyPl](https://pypi.org/project/gTTS/)
- [Descargas oficiales de Python](https://www.python.org/downloads/)
- [Lista de idiomas compatibles con gTTS](https://gtts.readthedocs.io/en/latest/module.html#available-languages)
- [Flask (web_framework)](<https://en.wikipedia.org/wiki/Flask_(web_framework)>)

---
