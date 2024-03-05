# Python Bit Calculator (Web)

Containerized python bit calculator web app with a single purpose - converting those bits

## Screenshot

![Python Bit Calculator (Web)](doc/bitcalc.png?raw=true)

## Basic Requirements

* Functional installations of [docker](https://www.docker.com/community-edition) and [docker-compose](https://docs.docker.com/compose/install/)
* A bit of time to get the containers running

## Quick start

* Copy `./config.py.example` to `./config.py`
* Copy development or prod docker-compose config to `./compose/docker-compose.yml`
  * Development: `./compose/docker-compose.yml.dev`
  * Hosting/production: `./compose/docker-compose.yml.prod`
* Open `./config.py` and set a non-default value for `SECRET_KEY`
* CD to `./compose` and run `docker-compose up`; wait for the images to build and start
* Open your browser and connect to `127.0.0.1` (or whatever IP and port you expect)

## About
This was primarily a learning exercise to build out a web UI for [pybitcalc](https://github.com/miliarch/pybitcalc). It kind of evolved to include docker containers. It's been a neat experience.

- Inspired by [Matisse's Bit Calculator](http://www.matisse.net/bitcalc)
- Units conform to [Ubuntu Units Policy](https://wiki.ubuntu.com/UnitsPolicy)
