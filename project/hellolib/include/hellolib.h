#include <string>

#include "hellolib_export.h"

namespace hello {
class HELLOLIB_EXPORT hellolib {
  int a{0};

 public:
  [[nodiscard]] int32_t saySomething(
      const std::string &something) const noexcept;
#ifdef WITH_OPENSSL
  [[nodiscard]] int32_t saySomethingHashed(
      const std::string &something) const noexcept;
#endif
};
}  // namespace hello