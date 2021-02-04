import sys
from scipy.io import wavfile

rate, data = wavfile.read(sys.argv[1])
print(rate)

with open("audio/wav/wav.h", "w") as f:
    f.write("int16_t data_snd_wav[] = {")
    f.write(", ".join(str(item) for item in data))
    f.write("}; int data_snd_wav_len = " + "{};".format(len(data)))
