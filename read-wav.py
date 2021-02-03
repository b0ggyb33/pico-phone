from pydub import AudioSegment
from scipy.io import wavfile

rate, data = wavfile.read("data/cantina.wav")
print(rate)

with open("cantina_data.h", "w") as f:
    f.write("int16_t data_cantina_wav[] = {")
    f.write(", ".join(str(item) for item in data))
    f.write("}; int data_cantina_wav_len = " + "{};".format(len(data)))
