cmake_minimum_required(VERSION 4.4.0)

target_sources(yada-text
    PRIVATE
        main.c
    PUBLIC
        FILE_SET HEADERS
        BASE_DIRS
            ${YADA_FUNCS}
        FILES
            ${YADA_FUNCS}/yadafuncs.h
)

target_include_directories(yada-text
    PRIVATE
        ${YADA_FUNCS}
)
