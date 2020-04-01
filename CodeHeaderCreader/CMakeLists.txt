# Minimal version of cmake
cmake_minimum_required(VERSION 3.0)

# Name of Project
project(CodeHeaderCreader)
set(PROJECT_VERSION_MAJOR 0)
set(PROJECT_VERSION_MINOR 1)

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_VERBOSE_MAKEFILE true)

enable_language(CXX)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_COMPILER clang++)
# Commen compile option
add_compile_options(-m64 -W -Wall)

# Source file list and output filename
set(OUTPUT_FL
    "${CMAKE_PROJECT_NAME}-${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}.out"
    )
set(SRC_LIST
    ClassHeader.cpp
    BulletProof.cpp
    main.cpp
    )

# Build
add_executable(${OUTPUT_FL} ${SRC_LIST})