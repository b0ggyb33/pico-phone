if (TARGET pico_audio_i2s)
    add_executable(lorem
            mp3.cpp
            )

    target_link_libraries(lorem PRIVATE
            mp3
            mp3_decoder
            pico_stdlib
            pico_audio_i2s
            )

    target_compile_definitions(lorem PRIVATE
            # compile time configuration of I2S
            PICO_AUDIO_I2S_MONO_INPUT=1
            #define for our example code
            USE_AUDIO_I2S=1
            )
    # create map/bin/hex file etc.
    pico_add_extra_outputs(lorem)
endif ()

add_subdirectory(src)
