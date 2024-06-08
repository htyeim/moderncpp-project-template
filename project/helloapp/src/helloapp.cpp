#include <iostream>
#include <print>
#include <thread>

#include "hellolib.h"

int main(int argc, char* argv[]) {
  for (int i = 0; i < argc; ++i) {
    std::cout << argv[i] << "\n";
  }
  hello::hellolib hello{};
  std::thread th{&hello::hellolib::saySomething, hello, "hell thread"};

  int32_t error_code = hello.saySomething("Hello Modern C++ Development");
  if (error_code > 0) {
    std::print("Hello, world! {}\n", error_code);
  }
#ifdef WITH_OPENSSL
  error_code = hello.saySomethingHashed("Hello Modern C++ Development");
  if (error_code > 0) {
    return error_code;
  }
#endif
  th.join();
  return 0;
}
