import os

from conan import ConanFile
from conan.tools.cmake import cmake_layout
from conan.tools.files import copy


class ImGuiExample(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    # options = "pkg/openssl:shared=False"

    def requirements(self):
        self.requires("openssl/[>=3.2.1]")
        self.requires("doctest/[>=2.4.11]")
        self.requires("implot/[>=0.16]")
        self.requires("imgui/[>=1.90.5]")
        self.requires("glfw/3.4")
        self.requires("glew/2.2.0")

    def generate(self):
        copy(self, "*glfw*", os.path.join(self.dependencies["imgui"].package_folder,
             "res", "bindings"), os.path.join(self.source_folder,"conan_generate", "imgui", "bindings"))
        copy(self, "*opengl3*", os.path.join(self.dependencies["imgui"].package_folder,
             "res", "bindings"), os.path.join(self.source_folder,"conan_generate","imgui", "bindings"))

    def build_requirements(self):
        self.tool_requires("cmake/[>=3.29.0]")

    # def layout(self):
    #     cmake_layout(self)

