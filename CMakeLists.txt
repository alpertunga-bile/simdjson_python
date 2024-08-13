cmake_minimum_required(VERSION 3.5.0)
project(simdstring VERSION 0.1.0 LANGUAGES C CXX)

include(CTest)
enable_testing()

include(setup.cmake)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(NOT MSVC)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++20")
endif()

enable_iwyu()

set(PXD_THIRD_PARTY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/third-party)
set(PXD_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/includes)
set(PXD_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/sources)

set(PYBIND11_FINDPYTHON ON)
add_subdirectory(${PXD_THIRD_PARTY_DIR}/pybind11)

set(PXD_HEADER_FILES
)

set(PXD_SOURCE_FILES
    ${PXD_THIRD_PARTY_DIR}/SIMDString/SIMDString.cpp
    ${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp
)

include_directories(
    ${PXD_THIRD_PARTY_DIR}/SIMDString
    ${PXD_THIRD_PARTY_DIR}/pybind11/include
)

set(COMMON_STD_HEADERS

)

set(LIBS_TO_LINK
)

pybind11_add_module(${PROJECT_NAME} MODULE ${PXD_SOURCE_FILES})

target_link_libraries(${PROJECT_NAME} PRIVATE ${LIBS_TO_LINK})

target_precompile_headers(
    ${PROJECT_NAME} PRIVATE
    ${COMMON_STD_HEADERS}
    ${PXD_HEADER_FILES}
)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
        