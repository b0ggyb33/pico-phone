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

## Physical connections

Pin 26 on pico to BCLK on amp
Pin 27 on pico to LRCCLK on amp
Pin 28 on pico to DIN on amp

pin 30 on pico to vin on amp
pin XX on pico to gnd on amp

amp SD to ground to disable

amp mono out to phone handset

## Development Log

* 2020-01-29 Played sine wave to a phone speaker
* 2020-01-27 Compiled audio example from [pico-playground](https://github.com/raspberrypi/pico-playground/tree/master/audio)

## Useful Links
* [pico sdk c++ pdf](https://datasheets.raspberrypi.org/pico/getting-started-with-pico.pdf)
