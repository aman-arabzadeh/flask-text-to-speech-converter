# Text to Speech Web App

![Stars](https://img.shields.io/github/stars/aman-arabzadeh/flask-text-to-speech-converter?style=flat)
![Last commit](https://img.shields.io/github/last-commit/aman-arabzadeh/flask-text-to-speech-converter)
![Docker Image Size (v1.0)](https://img.shields.io/docker/image-size/amankoray/flask-web-gtts-app/v1.0?label=Docker%20Image%20Size%20%28v1.0%29)
![Docker Pulls (repo)](https://img.shields.io/docker/pulls/amankoray/flask-web-gtts-app?label=Docker%20Pulls%20%28repo%29)

Available languages:  
[English](README.md) | [Svenska](READMESE.md) | [Español](READMEES.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is a Flask-based web application built with Python, HTML, and CSS.
It converts written text into natural speech using Google Text-to-Speech (gTTS).

I built this project to listen to text, articles, and books online in multiple languages.
Users can enter any text, choose a language, and the app generates an MP3 file that can be played or downloaded.

---

![Process](images/image.png)

---

### Example Speech Output

You can listen to an example of the generated speech below:

https://github.com/user-attachments/assets/399f7290-9730-4750-a43a-0c4c80a2cb9a

<p align="center">
  <img src="images/interface.png" width="50%" style="height:auto;" />
</p>

<br>
<p align="center">
  <img src="images/interface2.png" width="50%" style="height:auto;" />
</p>

---

# Docker Image

I’ve also containerized this project using **Docker**.  
You can pull the image from **Docker Hub** and run it instantly on your own system — no manual setup needed.

**Docker Hub Repository:**  
[flask-web-gtts-app](https://hub.docker.com/repository/docker/amankoray/flask-web-gtts-app/general)

### Run it in 2 simple steps

```bash
# 1. Pull the image from Docker Hub
docker pull amankoray/flask-web-gtts-app:v1.0

# 2. Run the container
docker run -p 5000:5000 amankoray/flask-web-gtts-app:v1.0
```

Then open your browser and visit:  
[http://localhost:5000](http://localhost:5000)
That’s it! You’ll have the **Text-to-Speech Web App** running in seconds on your machine

---

## Useful Links

- [Flask Documentation](https://flask.palletsprojects.com/en/stable/)
- [gTTS (Google Text-to-Speech) on PyPI](https://pypi.org/project/gTTS/)
- [Python Official Downloads](https://www.python.org/downloads/)
- [List of Supported gTTS Languages](https://gtts.readthedocs.io/en/latest/module.html#available-languages)
- [Flask (web_framework)](<https://en.wikipedia.org/wiki/Flask_(web_framework)>)

---
