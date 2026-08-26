cmake_minimum_required(VERSION 4.4.0)

set(YADA_ROOT ${CMAKE_CURRENT_SOURCE_DIR})
set(YADA_FUNCS "${YADA_ROOT}/include")

project(yada-terminal)

add_executable(yada-text)

add_subdirectory(src)
