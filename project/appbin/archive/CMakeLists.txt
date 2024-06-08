# find_package(behaviortree_cpp REQUIRED)

# file(GLOB_RECURSE all_imp_srcs CONFIGURE_DEPENDS *.cpp)
# list(FILTER all_imp_srcs EXCLUDE REGEX "app_.*.cpp$")
# if (all_imp_srcs)
#     add_library(${MY_ARCHIVE_LIB} SHARED ${all_imp_srcs} )
# endif()

find_package(implot REQUIRED)
find_package(imgui REQUIRED)
find_package(glfw3 REQUIRED)
find_package(glew REQUIRED)

file(GLOB_RECURSE imgui_bindings_h CONFIGURE_DEPENDS ${CMAKE_SOURCE_DIR}/conan_generate/imgui/bindings/*.h)
file(GLOB_RECURSE imgui_bindings_cpp CONFIGURE_DEPENDS ${CMAKE_SOURCE_DIR}/conan_generate/imgui/bindings/*.cpp)

# for each "src/app_x.cpp", generate target "app_x"
file(GLOB_RECURSE all_app_srcs CONFIGURE_DEPENDS app_imgui_implot.cpp)
foreach(v ${all_app_srcs})

    string(REGEX MATCH "archive/.*" relative_path ${v})
    # message(${relative_path})
    string(REGEX REPLACE "archive/" "" target_name ${relative_path})
    string(REGEX REPLACE ".cpp" "" target_name ${target_name})

    add_executable(${target_name} ${imgui_bindings_h} ${imgui_bindings_cpp} ${v})
    TARGET_LINK_LIBRARIES(${target_name}
        PRIVATE
            imgui::imgui
            implot::implot
            GLEW::GLEW
            glfw
            )
    target_compile_definitions(${target_name} PUBLIC IMGUI_IMPL_OPENGL_LOADER_GLEW)
    target_include_directories(${target_name}
        PRIVATE 
            ${TARGET_INCLUDE_FOLDER}
            ${CMAKE_CURRENT_SOURCE_DIR}/../hellolib/include
            # Any other extra include required
            ${CMAKE_SOURCE_DIR}/conan_generate/imgui
    )
endforeach()
