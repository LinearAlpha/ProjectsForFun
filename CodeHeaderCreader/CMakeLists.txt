# Minimal version of cmake
cmake_minimum_required(VERSION 3.0)

# Name of Project
project(CodeHeaderCreader)
set(PROJECT_VERSION_MAJOR 0)
set(PROJECT_VERSION_MINOR 1)

include(CTest)
enable_testing()

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_VERBOSE_MAKEFILE true)

# Source file list and output filename
set(OUTPUT_FL
    "${CMAKE_PROJECT_NAME}-${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}.out"
    )
set(SRC_LIST
    HEAD_FORMAT.cpp
    bullet.cpp
    timeMade.cpp
    main.cpp
    )

# Common comfiler
set(CMAKE_CXX_COMPILER "g++")

# Commen compile option
add_compile_options(-std=c++11 -m64 -W -Wall -E -v -O2 )
SET ( CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BUILD_TYPE} )
SET ( CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BUILD_TYPE}/lib )
SET ( CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BUILD_TYPE}/lib )

# Build
add_executable(${OUTPUT_FL} ${SRC_LIST})

target_link_libraries(${OUTPUT_FL} -lm)
set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)