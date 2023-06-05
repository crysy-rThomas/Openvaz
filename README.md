# Project Name

## Description

Ce projet vise à automatiser le processus de scan de vulnérabilité et de déploiement d'un environnement WordPress à l'aide d'un Dockerfile. Plus précisément, le projet se concentre sur l'utilisation d'OpenVAS pour effectuer le scan des ports ouverts et des vulnérabilités de l'instance WordPress déployée.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation

- Création d’une image custom pour la base de données.
- sudo docker build -t bddimage .
- sudo docker load < bddimage.tar
- adresse wordpress openvaz https://10.0.2.15:8083 
- adresse openvas https://192.30.0.4:443

## Usage

Installation et configuration de Openvas avec lancement automatisé d'un scan périodique


## Contributing

Contributions to Openvaz are welcome and encouraged! To contribute, simply fork this repository, make your changes, and submit a pull request.

---
