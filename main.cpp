#include "third-party/SIMDString/SIMDString.h"

#include "third-party/pybind11/include/pybind11/operators.h"
#include "third-party/pybind11/include/pybind11/pybind11.h"

constexpr int SIMDSTRING_ALIGNMENT = 64;

PYBIND11_MODULE(simdstring, m) {
  m.doc() = "SIMDString python package";

  namespace py = pybind11;
  using StrClass = SIMDString<SIMDSTRING_ALIGNMENT>;

  auto str_class = py::class_<StrClass>(m, "SIMDString");

  str_class.def(py::init<const char *>());
  str_class.def(py::init<const std::string &>());

  str_class.def("__repr__", &StrClass::c_str);

  str_class.def_property("value", &StrClass::c_str, nullptr);
}

auto main() -> int { return 0; }