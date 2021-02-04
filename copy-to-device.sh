#!/bin/bash
sudo mount /dev/sda1 /mnt/pico/
sudo cp build/audio/wav/wav_i2s.uf2 /mnt/pico/
sudo sync
sudo umount /mnt/pico/
