# only build I2S example if library is available
if (TARGET pico_audio_i2s)
    add_executable(wav_i2s
            wav.c
            )

    target_link_libraries(wav_i2s PRIVATE
            pico_stdlib
            pico_audio_i2s
            )

    target_compile_definitions(wav_i2s PRIVATE
            # compile time configuration of I2S
            PICO_AUDIO_I2S_MONO_INPUT=1
            #define for our example code
            USE_AUDIO_I2S=1
            )
    # create map/bin/hex file etc.
    pico_add_extra_outputs(wav_i2s)
endif ()
