#include "third-party/SIMDString/SIMDString.h"

#include "third-party/pybind11/include/pybind11/operators.h"
#include "third-party/pybind11/include/pybind11/pybind11.h"

constexpr int SIMDSTRING_ALIGNMENT = 64;

PYBIND11_MODULE(simdstring, m) {
  m.doc() = "SIMDString python package";

  namespace py = pybind11;
  using StrClass = SIMDString<SIMDSTRING_ALIGNMENT>;
  using namespace pybind11::literals;

  auto str_class = py::class_<StrClass>(m, "SIMDString");

  str_class.def(py::init<const char *>());
  str_class.def(py::init<const std::string &>());
  str_class.def(py::init<std::string &&>());

  str_class.def("length", &StrClass::length);
  str_class.def("data", py::overload_cast<>(&StrClass::data, py::const_));

  str_class.def("__repr__", &StrClass::c_str);

  str_class.def_property("value", &StrClass::c_str, nullptr);

  // to_string functions

  m.def("to_string", py::overload_cast<int>(&to_string<SIMDSTRING_ALIGNMENT>));
  m.def("to_string", py::overload_cast<long>(&to_string<SIMDSTRING_ALIGNMENT>));
  m.def("to_string",
        py::overload_cast<long long>(&to_string<SIMDSTRING_ALIGNMENT>));
  m.def("to_string",
        py::overload_cast<unsigned int>(&to_string<SIMDSTRING_ALIGNMENT>));
  m.def("to_string",
        py::overload_cast<unsigned long>(&to_string<SIMDSTRING_ALIGNMENT>));
  m.def("to_string", py::overload_cast<unsigned long long>(
                         &to_string<SIMDSTRING_ALIGNMENT>));
  m.def("to_string",
        py::overload_cast<float>(&to_string<SIMDSTRING_ALIGNMENT>));
  m.def("to_string",
        py::overload_cast<double>(&to_string<SIMDSTRING_ALIGNMENT>));
  m.def("to_string",
        py::overload_cast<long double>(&to_string<SIMDSTRING_ALIGNMENT>));
}

auto main() -> int { return 0; }