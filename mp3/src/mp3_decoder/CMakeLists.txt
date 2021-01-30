if (NOT TARGET mp3_decoder)
add_library(mp3_decoder INTERFACE)

target_include_directories(mp3_decoder INTERFACE ${CMAKE_CURRENT_LIST_DIR}/include)

target_sources(mp3_decoder INTERFACE
  ${CMAKE_CURRENT_LIST_DIR}/mp3_deocder.cpp
  
)
endif()
