with open("result.bin", "rb") as f:
    chars = f.read()
values = [ord(c) for c in chars]
with open("wav.h", "w") as f:
    f.write("int16_t data_snd_wav [] = {")
    for lower, upper in zip(values[::2], values[1::2]):
        print(lower + (upper << 8))
        signed_16 = str((upper << 8) + lower)
        f.write(signed_16+",")

    f.write("}; int data_snd_wav_len=" + "{};".format(len(values)/2))

