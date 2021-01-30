add_subdirectory(mp3_decoder)

if (NOT TARGET mp3)
add_library(mp3 INTERFACE)

target_include_directories(mp3 INTERFACE ${CMAKE_CURRENT_LIST_DIR}/include)

target_sources(mp3 INTERFACE
  ${CMAKE_CURRENT_LIST_DIR}/Audio.cpp
)
endif()
