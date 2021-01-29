# Pico Phone

make a landline play mp3 with raspberry pi pico

## Requirements
* [pico-sdk](https://github.com/raspberrypi/pico-sdk)
* [pico-extras](https://github.com/raspberrypi/pico-extras)

## BOM

* raspberry pi pico
* [adafruit i2s class d mono amp](https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp)
* Landline phone

## Changes to sdk

* changed i2s data pin to 26
* changed i2s clock pin to 28

## Development Log

* 2020-01-29 Played sine wave to a phone speaker
* 2020-01-27 Compiled audio example from [pico-playground](https://github.com/raspberrypi/pico-playground/tree/master/audio)

## Useful Links
* [pico sdk c++ pdf](https://datasheets.raspberrypi.org/pico/getting-started-with-pico.pdf)
