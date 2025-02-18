cmake_minimum_required(VERSION 3.14) # I like pie
include(CheckTypeSize)
include(CheckSymbolExists)
include(CheckLibraryExists)
include(TestBigEndian)

project(soundswallower VERSION 0.3.2
  DESCRIPTION "An even smaller speech recognizer")

if(CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME)
  include(CTest)
  enable_testing()
endif()

CHECK_INCLUDE_FILE(unistd.h HAVE_UNISTD_H)
CHECK_INCLUDE_FILE(stdint.h HAVE_STDINT_H)
CHECK_INCLUDE_FILE(sys/types.h HAVE_SYS_TYPES_H)
CHECK_INCLUDE_FILE(sys/stat.h HAVE_SYS_STAT_H)
CHECK_SYMBOL_EXISTS(snprintf stdio.h HAVE_SNPRINTF)
CHECK_SYMBOL_EXISTS(popen stdio.h HAVE_POPEN)

# Testing endianness is stupidly hard with CMake
if(EMSCRIPTEN)
  # FIXME: and doesn't work at all with emscripten, maybe it's just
  # always little-endian?
  set(WORDS_BIGENDIAN 0)
else()
  test_big_endian(WORDS_BIGENDIAN)
endif()

configure_file(config.h.in config.h)
add_definitions(-DHAVE_CONFIG_H)

# Did I mention that CMake is really stupid
if(MSVC)
  add_compile_options(/W3) # /WX)
else()
  add_compile_options(-Wall -Wextra) # -Wpedantic -Werror)
endif()

# For MSVC/vscode in Windows: don't warn about functions only MS considers deprecated
add_definitions(-D_CRT_SECURE_NO_WARINIGS)
add_definitions(-D_CRT_SECURE_NO_DEPRECATE)

# Put all the output in one place
set (CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})
set (CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})
set (CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

if(EMSCRIPTEN)
  # Specific configuration for JavaScript build
  add_subdirectory(src)
  add_subdirectory(js)
elseif(SKBUILD)
  # Specific configuration for Python extension build
  add_subdirectory(src)
  add_subdirectory(py)
else()
  # C shared library build
  option(BUILD_SHARED_LIBS "Build using shared libraries" ON)
  # Build the core library source (needs to go after BUILD_SHARED_LIBS
  # option because CMake is magically stupid)
  add_subdirectory(src)
  add_subdirectory(include/soundswallower)
  if(CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME AND BUILD_TESTING)
    add_subdirectory(tests)
  endif()
  install(TARGETS soundswallower DESTINATION lib)
  set_target_properties(soundswallower PROPERTIES
    VERSION ${CMAKE_PROJECT_VERSION}
    SOVERSION ${CMAKE_PROJECT_VERSION_MAJOR}
    )
endif()

