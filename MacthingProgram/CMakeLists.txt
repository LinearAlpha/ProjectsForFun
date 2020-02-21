# Minimal version of cmake
cmake_minimum_required(VERSION 3.0)

# Name of Project
project(MachingProgram)
set(PROJECT_VERSION_MAJOR 0)
set(PROJECT_VERSION_MINOR 1)

include(CTest)
enable_testing()

set(CMAKE_VERBOSE_MAKEFILE true)

# Source file list and output filename
set(OUTPUT_FL
    "${CMAKE_PROJECT_NAME}-${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}.out"
    )
set(SRC_LIST
    main.cpp
    fileIO.cpp
    )

# Common comfiler
set(CMAKE_C_COMPILER "gcc")
set(CMAKE_CXX_COMPILER "g++")

# Commen compile option
add_compile_options(-Wall)

# Build
add_executable(${OUTPUT_FL} ${SRC_LIST})

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)