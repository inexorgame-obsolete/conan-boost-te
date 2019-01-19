cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(CXX_STANDARD "c++17")
if(${CMAKE_CXX_COMPILER_ID} STREQUAL GNU)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++1z -fno-exceptions -pedantic -pedantic-errors -Wall -Wextra -Werror -fconcepts")
elseif (${CMAKE_CXX_COMPILER_ID} STREQUAL Clang OR ${CMAKE_CXX_COMPILER_ID} STREQUAL AppleClang)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++1z -fno-exceptions -pedantic -pedantic-errors -Wall -Wextra -Werror")
elseif (${CMAKE_CXX_COMPILER_ID} STREQUAL MSVC)
    set(MSVC_STD_FLAG "/std:c++17" CACHE STRING "Language Standard Version. /std:[c++17|c++latest]  ")
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${MSVC_STD_FLAG} /W3 /EHsc")
else()
    message(WARNING "Unsupported compiler!")
endif()


add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
