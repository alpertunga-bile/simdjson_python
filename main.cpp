#include <cstddef>

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

  /*
   * Starting from the 499th line of the SIMDString.h file
   */

  str_class.def(py::init<std::nullptr_t>());
  str_class.def(py::init<>());
  str_class.def(py::init<std::size_t, StrClass::value_type>(), "count"_a,
                "c"_a);
  str_class.def(py::init<const StrClass &, std::size_t>(), "str"_a,
                "pos"_a = 0);
  str_class.def(py::init<const StrClass &, std::size_t, std::size_t>(), "str"_a,
                "pos"_a = 0, "count"_a = StrClass::npos);
  str_class.def(py::init<StrClass::const_pointer>(), "s"_a);
  str_class.def(py::init<StrClass::const_pointer, std::size_t>(), "s"_a,
                "count"_a = StrClass::npos);
  str_class.def(py::init<StrClass::const_pointer, std::size_t, std::size_t>(),
                "s"_a, "pos"_a = 0, "count"_a = StrClass::npos);
  str_class.def(py::init<const std::string &, std::size_t, std::size_t>(),
                "str"_a, "pos"_a = 0, "count"_a = StrClass::npos);
  str_class.def(py::init<std::initializer_list<StrClass::value_type>>(),
                "ilist"_a);
  str_class.def(py::init<const std::string &>());
  str_class.def(py::init<std::string &&>());

  str_class.def("data", py::overload_cast<>(&StrClass::data, py::const_));

  str_class.def("__getitem__", [](StrClass &self, StrClass::size_type index) {
    return self[index];
  });

  str_class.def(
      "at", py::overload_cast<StrClass::size_type>(&StrClass::at, py::const_));
  str_class.def("at", py::overload_cast<StrClass::size_type>(&StrClass::at));

  str_class.def("front", py::overload_cast<>(&StrClass::front, py::const_));
  str_class.def("front", py::overload_cast<>(&StrClass::front));

  str_class.def("back", py::overload_cast<>(&StrClass::back, py::const_));
  str_class.def("back", py::overload_cast<>(&StrClass::back));

  str_class.def("size", &StrClass::size);
  str_class.def_property("length", &StrClass::length, nullptr);

  str_class.def("is_empty", &StrClass::empty);
  str_class.def_property("empty", &StrClass::empty, nullptr);

  str_class.def("reserve", &StrClass::reserve, "new_length"_a = 0);
  str_class.def("shrink_to_fit", &StrClass::shrink_to_fit);

  str_class.def("resize", &StrClass::resize, "count"_a, "c"_a = '\0');

  // addition operations

  str_class.def(py::self + py::self);
  str_class.def(py::self += py::self);

  // check operations

  str_class.def(py::self > py::self, "str"_a);
  str_class.def(py::self < py::self, "str"_a);
  str_class.def(py::self >= py::self, "str"_a);
  str_class.def(py::self <= py::self, "str"_a);
  str_class.def(py::self == py::self, "str"_a);
  str_class.def(py::self == StrClass::const_pointer(), "s"_a);
  str_class.def(py::self != py::self, "str"_a);
  str_class.def(py::self != StrClass::const_pointer(), "s"_a);

  // find functions

  str_class.def("find",
                py::overload_cast<const StrClass &, std::size_t>(
                    &StrClass::find, py::const_),
                "str"_a, "pos"_a);
  str_class.def("find",
                py::overload_cast<StrClass::const_pointer, std::size_t>(
                    &StrClass::find, py::const_),
                "s"_a, "pos"_a);
  str_class.def(
      "find",
      py::overload_cast<StrClass::const_pointer, std::size_t, std::size_t>(
          &StrClass::find, py::const_),
      "s"_a, "pos"_a, "count"_a);
  str_class.def("find",
                py::overload_cast<StrClass::value_type, std::size_t>(
                    &StrClass::find, py::const_),
                "s"_a, "pos"_a);

  // variable functions

  str_class.def("equals", &StrClass::equals, "str"_a);

  str_class.def("__len__", &StrClass::length);
  str_class.def("__str__", &StrClass::c_str);
  str_class.def("__repr__", &StrClass::c_str);

  str_class.def(py::hash(py::self));

  str_class.def_property("value", &StrClass::c_str, nullptr);

  // to_string functions

  m.def("to_string", py::overload_cast<int>(&to_string<SIMDSTRING_ALIGNMENT>),
        "value"_a);
  m.def("to_string", py::overload_cast<long>(&to_string<SIMDSTRING_ALIGNMENT>),
        "value"_a);
  m.def("to_string",
        py::overload_cast<long long>(&to_string<SIMDSTRING_ALIGNMENT>),
        "value"_a);
  m.def("to_string",
        py::overload_cast<unsigned int>(&to_string<SIMDSTRING_ALIGNMENT>),
        "value"_a);
  m.def("to_string",
        py::overload_cast<unsigned long>(&to_string<SIMDSTRING_ALIGNMENT>),
        "value"_a);
  m.def("to_string",
        py::overload_cast<unsigned long long>(&to_string<SIMDSTRING_ALIGNMENT>),
        "value"_a);
  m.def("to_string", py::overload_cast<float>(&to_string<SIMDSTRING_ALIGNMENT>),
        "value"_a);
  m.def("to_string",
        py::overload_cast<double>(&to_string<SIMDSTRING_ALIGNMENT>), "value"_a);
  m.def("to_string",
        py::overload_cast<long double>(&to_string<SIMDSTRING_ALIGNMENT>),
        "value"_a);
}

auto main() -> int { return 0; }