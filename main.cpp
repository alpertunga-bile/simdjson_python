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

  // -------------------------------------------------------------------------------------
  // -- ctors

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

  // -------------------------------------------------------------------------------------
  // -- assign functions

  str_class.def(
      "assign",
      static_cast<StrClass &(StrClass::*)(const StrClass &, StrClass::size_type,
                                          StrClass::size_type)>(
          &StrClass::assign),
      "str"_a, "pos"_a = 0, "count"_a = StrClass::npos);
  str_class.def("assign",
                static_cast<StrClass &(StrClass::*)(StrClass::const_pointer,
                                                    StrClass::size_type)>(
                    &StrClass::assign),
                "s"_a, "count"_a);
  str_class.def("assign",
                static_cast<StrClass &(StrClass::*)(StrClass::const_pointer)>(
                    &StrClass::assign),
                "s"_a);
  str_class.def(
      "assign",
      static_cast<StrClass &(StrClass::*)(StrClass::size_type,
                                          const StrClass::value_type)>(
          &StrClass::assign),
      "count"_a, "c"_a);
  str_class.def("assign",
                static_cast<StrClass &(
                    StrClass::*)(std::initializer_list<StrClass::value_type>)>(
                    &StrClass::assign),
                "ilist"_a);

  // -------------------------------------------------------------------------------------
  // -- functions

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

  // -------------------------------------------------------------------------------------
  // -- insert functions

  str_class.def("insert",
                static_cast<StrClass &(
                    StrClass::*)(StrClass::size_type, const StrClass &,
                                 StrClass::size_type, StrClass::size_type)>(
                    &StrClass::insert),
                "pos"_a, "str"_a, "pos2"_a, "count"_a = StrClass::npos);
  str_class.def(
      "insert",
      static_cast<StrClass &(StrClass::*)(StrClass::size_type,
                                          const StrClass &)>(&StrClass::insert),
      "pos"_a, "str"_a);
  str_class.def("insert",
                static_cast<StrClass &(StrClass::*)(StrClass::size_type,
                                                    StrClass::const_pointer)>(
                    &StrClass::insert),
                "pos"_a, "s"_a);
  str_class.def("insert",
                static_cast<StrClass &(
                    StrClass::*)(StrClass::size_type, StrClass::const_pointer,
                                 StrClass::size_type)>(&StrClass::insert),
                "pos"_a, "s"_a, "count"_a);
  str_class.def("insert",
                static_cast<StrClass &(
                    StrClass::*)(StrClass::size_type, StrClass::size_type,
                                 StrClass::value_type)>(&StrClass::insert),
                "pos"_a, "count"_a, "c"_a);

  str_class.def("resize", &StrClass::resize, "count"_a, "c"_a = '\0');

  // -------------------------------------------------------------------------------------
  // -- functions

  str_class.def(
      "copy",
      py::overload_cast<StrClass::pointer, StrClass::size_type,
                        StrClass::size_type>(&StrClass::copy, py::const_),
      "dest"_a, "count"_a, "pos"_a = 0);

  // -------------------------------------------------------------------------------------
  // -- replace functions

  str_class.def("replace",
                static_cast<StrClass &(
                    StrClass::*)(StrClass::size_type, StrClass::size_type,
                                 const StrClass &)>(&StrClass::replace),
                "pos"_a, "count"_a, "str"_a);
  str_class.def("replace",
                static_cast<StrClass &(
                    StrClass::*)(StrClass::size_type, StrClass::size_type,
                                 const StrClass &, StrClass::size_type,
                                 StrClass::size_type)>(&StrClass::replace),
                "pos"_a, "count"_a, "str"_a, "pos2"_a,
                "count2"_a = StrClass::npos);
  str_class.def("replace",
                static_cast<StrClass &(
                    StrClass::*)(StrClass::size_type, StrClass::size_type,
                                 StrClass::const_pointer, StrClass::size_type)>(
                    &StrClass::replace),
                "pos"_a, "count"_a, "s"_a, "count2"_a);
  str_class.def("replace",
                static_cast<StrClass &(
                    StrClass::*)(StrClass::size_type, StrClass::size_type,
                                 StrClass::const_pointer)>(&StrClass::replace),
                "pos"_a, "count"_a, "s"_a);
  str_class.def("replace",
                static_cast<StrClass &(
                    StrClass::*)(StrClass::size_type, StrClass::size_type,
                                 StrClass::size_type, StrClass::value_type)>(
                    &StrClass::replace),
                "pos"_a, "count"_a, "count2"_a, "c"_a);

  // -------------------------------------------------------------------------------------
  // -- functions

  str_class.def("clear", &StrClass::clear);

  str_class.def("erase",
                static_cast<StrClass &(StrClass::*)(StrClass::size_type,
                                                    StrClass::size_type)>(
                    &StrClass::erase),
                "pos"_a = 0, "count"_a = StrClass::npos);

  // -------------------------------------------------------------------------------------
  // -- addition operations

  str_class.def(py::self + py::self);
  str_class.def(py::self + StrClass::const_pointer());
  str_class.def(StrClass::const_pointer() + py::self);
  str_class.def(py::self + StrClass::value_type());
  str_class.def(StrClass::value_type() + py::self);
  str_class.def(py::self += py::self);
  str_class.def(py::self += StrClass::value_type());
  str_class.def(py::self += StrClass::const_pointer());
  str_class.def(py::self += std::initializer_list<StrClass::value_type>());

  str_class.def("push_back", &StrClass::push_back, "c"_a);
  str_class.def("pop_back", &StrClass::pop_back);

  // -------------------------------------------------------------------------------------
  // append functions

  str_class.def(
      "append",
      static_cast<StrClass &(StrClass::*)(const StrClass &, StrClass::size_type,
                                          StrClass::size_type)>(
          &StrClass::append),
      "str"_a, "pos"_a, "count"_a = StrClass::npos);
  str_class.def(
      "append",
      static_cast<StrClass &(StrClass::*)(const StrClass &)>(&StrClass::append),
      "str"_a);
  str_class.def("append",
                static_cast<StrClass &(StrClass::*)(StrClass::size_type,
                                                    StrClass::value_type)>(
                    &StrClass::append),
                "count"_a, "c"_a);
  str_class.def("append",
                static_cast<StrClass &(StrClass::*)(StrClass::const_pointer,
                                                    StrClass::size_type)>(
                    &StrClass::append),
                "s"_a, "t"_a);
  str_class.def("append",
                static_cast<StrClass &(StrClass::*)(StrClass::const_pointer)>(
                    &StrClass::append),
                "s"_a);
  str_class.def("append",
                static_cast<StrClass &(
                    StrClass::*)(std::initializer_list<StrClass::value_type>)>(
                    &StrClass::append),
                "ilist"_a);

  // -------------------------------------------------------------------------------------
  // -- functions

  str_class.def("swap", &StrClass::swap, "str"_a);

  str_class.def("starts_with",
                py::overload_cast<StrClass::value_type>(&StrClass::starts_with,
                                                        py::const_),
                "c"_a);
  str_class.def("starts_with",
                py::overload_cast<const StrClass::pointer>(
                    &StrClass::starts_with, py::const_),
                "s"_a);
  str_class.def(
      "ends_with",
      py::overload_cast<StrClass::value_type>(&StrClass::ends_with, py::const_),
      "c"_a);
  str_class.def("ends_with",
                py::overload_cast<StrClass::const_pointer>(&StrClass::ends_with,
                                                           py::const_),
                "s"_a);

  str_class.def("substr",
                py::overload_cast<StrClass::size_type, StrClass::size_type>(
                    &StrClass::substr, py::const_),
                "pos"_a, "count"_a = StrClass::npos);

  str_class.def(
      "contains",
      py::overload_cast<StrClass::value_type>(&StrClass::contains, py::const_),
      "c"_a);

  str_class.def("contains",
                py::overload_cast<StrClass::const_pointer>(&StrClass::contains,
                                                           py::const_),
                "s"_a);

  // -------------------------------------------------------------------------------------
  // -- find functions

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

  str_class.def("rfind",
                py::overload_cast<const StrClass &, StrClass::size_type>(
                    &StrClass::rfind, py::const_),
                "str"_a, "pos"_a = StrClass::npos);
  str_class.def("rfind",
                py::overload_cast<StrClass::const_pointer, StrClass::size_type>(
                    &StrClass::rfind, py::const_),
                "s"_a, "pos"_a = StrClass::npos);
  str_class.def(
      "rfind",
      py::overload_cast<StrClass::const_pointer, StrClass::size_type,
                        StrClass::size_type>(&StrClass::rfind, py::const_),
      "s"_a, "pos"_a, "count"_a);
  str_class.def("rfind",
                py::overload_cast<StrClass::value_type, StrClass::size_type>(
                    &StrClass::rfind, py::const_),
                "c"_a, "pos"_a = StrClass::npos);

  // -------------------------------------------------------------------------------------
  // -- find_first_of functions

  str_class.def("find_first_of",
                py::overload_cast<const StrClass &, StrClass::size_type>(
                    &StrClass::find_first_of, py::const_),
                "str"_a, "pos"_a = 0);
  str_class.def("find_first_of",
                py::overload_cast<StrClass::const_pointer, StrClass::size_type>(
                    &StrClass::find_first_of, py::const_),
                "s"_a, "pos"_a = 0);
  str_class.def("find_first_of",
                py::overload_cast<StrClass::value_type, StrClass::size_type>(
                    &StrClass::find_first_of, py::const_),
                "c"_a, "pos"_a = 0);
  str_class.def("find_first_of",
                py::overload_cast<StrClass::const_pointer, StrClass::size_type,
                                  StrClass::size_type>(&StrClass::find_first_of,
                                                       py::const_),
                "s"_a, "pos"_a, "count"_a);

  // -------------------------------------------------------------------------------------
  // -- find_first_not_of functions

  str_class.def("find_first_not_of",
                py::overload_cast<const StrClass &, StrClass::size_type>(
                    &StrClass::find_first_not_of, py::const_),
                "str"_a, "pos"_a = 0);
  str_class.def("find_first_not_of",
                py::overload_cast<StrClass::const_pointer, StrClass::size_type>(
                    &StrClass::find_first_not_of, py::const_),
                "s"_a, "pos"_a = 0);
  str_class.def("find_first_not_of",
                py::overload_cast<StrClass::value_type, StrClass::size_type>(
                    &StrClass::find_first_not_of, py::const_),
                "c"_a, "pos"_a = 0);
  str_class.def("find_first_not_of",
                py::overload_cast<StrClass::const_pointer, StrClass::size_type,
                                  StrClass::size_type>(
                    &StrClass::find_first_not_of, py::const_),
                "s"_a, "pos"_a, "count"_a);

  // -------------------------------------------------------------------------------------
  // -- find_last_of functions

  str_class.def("find_last_of",
                py::overload_cast<StrClass::const_pointer, StrClass::size_type,
                                  StrClass::size_type>(&StrClass::find_last_of,
                                                       py::const_),
                "s"_a, "pos"_a, "count"_a);
  str_class.def("find_last_of",
                py::overload_cast<const StrClass &, StrClass::size_type>(
                    &StrClass::find_last_of, py::const_),
                "str"_a, "pos"_a = StrClass::npos);
  str_class.def("find_last_of",
                py::overload_cast<StrClass::value_type, StrClass::size_type>(
                    &StrClass::find_last_of, py::const_),
                "c"_a, "pos"_a = StrClass::npos);

  // -------------------------------------------------------------------------------------
  // -- find_last_not_of functions

  str_class.def("find_last_not_of",
                py::overload_cast<StrClass::const_pointer, StrClass::size_type,
                                  StrClass::size_type>(
                    &StrClass::find_last_not_of, py::const_),
                "s"_a, "pos"_a, "count"_a);
  str_class.def("find_last_not_of",
                py::overload_cast<const StrClass &, StrClass::size_type>(
                    &StrClass::find_last_not_of, py::const_),
                "str"_a, "pos"_a = StrClass::npos);
  str_class.def("find_last_not_of",
                py::overload_cast<StrClass::value_type, StrClass::size_type>(
                    &StrClass::find_last_not_of, py::const_),
                "c"_a, "pos"_a = StrClass::npos);

  // -------------------------------------------------------------------------------------
  // -- compare functions

  str_class.def(
      "compare",
      py::overload_cast<StrClass::size_type, StrClass::size_type,
                        const StrClass &>(&StrClass::compare, py::const_),
      "pos"_a, "count"_a, "str"_a);
  str_class.def(
      "compare",
      py::overload_cast<StrClass::size_type, StrClass::size_type,
                        const StrClass &, StrClass::size_type,
                        StrClass::size_type>(&StrClass::compare, py::const_),
      "pos"_a, "count1"_a, "str"_a, "pos2"_a, "count2"_a);
  str_class.def("compare",
                py::overload_cast<StrClass::const_pointer>(&StrClass::compare,
                                                           py::const_),
                "s"_a);
  str_class.def("compare",
                py::overload_cast<StrClass::size_type, StrClass::size_type,
                                  StrClass::const_pointer>(&StrClass::compare,
                                                           py::const_),
                "pos"_a, "count"_a, "s"_a);
  str_class.def("compare",
                py::overload_cast<StrClass::size_type, StrClass::size_type,
                                  StrClass::const_pointer, StrClass::size_type>(
                    &StrClass::compare, py::const_),
                "pos"_a, "count1"_a, "s"_a, "count2"_a);

  // -------------------------------------------------------------------------------------
  // check operations

  str_class.def(py::self == py::self, "str"_a);
  str_class.def(py::self == StrClass::const_pointer(), "s"_a);
  str_class.def(StrClass::const_pointer() == py::self);
  str_class.def(py::self != py::self, "str"_a);
  str_class.def(py::self != StrClass::const_pointer(), "s"_a);
  str_class.def(StrClass::const_pointer() != py::self);

  str_class.def(py::self > py::self, "str"_a);
  str_class.def(py::self < py::self, "str"_a);
  str_class.def(py::self >= py::self, "str"_a);
  str_class.def(py::self <= py::self, "str"_a);

  str_class.def(StrClass::const_pointer() < py::self);
  str_class.def(StrClass::const_pointer() <= py::self);
  str_class.def(StrClass::const_pointer() > py::self);
  str_class.def(StrClass::const_pointer() >= py::self);

  // -------------------------------------------------------------------------------------
  // -- variable functions

  str_class.def("equals", &StrClass::equals, "str"_a);

  str_class.def("__len__", &StrClass::length);
  str_class.def("__str__", &StrClass::c_str);
  str_class.def("__repr__", &StrClass::c_str);

  str_class.def(py::hash(py::self));

  str_class.def_property("value", &StrClass::c_str, nullptr);

  // -------------------------------------------------------------------------------------
  // -- conversion functions

  m.def("stoi",
        py::overload_cast<const StrClass &, StrClass::size_type *, int>(
            &stoi<SIMDSTRING_ALIGNMENT>),
        "str"_a, "pos"_a = nullptr, "base"_a = 10);

  m.def("stol",
        py::overload_cast<const StrClass &, StrClass::size_type *, int>(
            &stol<SIMDSTRING_ALIGNMENT>),
        "str"_a, "pos"_a = nullptr, "base"_a = 10);

  m.def("stoll",
        py::overload_cast<const StrClass &, StrClass::size_type *, int>(
            &stoll<SIMDSTRING_ALIGNMENT>),
        "str"_a, "pos"_a = nullptr, "base"_a = 10);

  m.def("stoul",
        py::overload_cast<const StrClass &, StrClass::size_type *, int>(
            &stoul<SIMDSTRING_ALIGNMENT>),
        "str"_a, "pos"_a = nullptr, "base"_a = 10);

  m.def("stoull",
        py::overload_cast<const StrClass &, StrClass::size_type *, int>(
            &stoull<SIMDSTRING_ALIGNMENT>),
        "str"_a, "pos"_a = nullptr, "base"_a = 10);

  m.def("stof", py::overload_cast<const StrClass &, StrClass::size_type *>(
                    &stof<SIMDSTRING_ALIGNMENT>, "str"_a, "pos"_a = nullptr));

  m.def("stod", py::overload_cast<const StrClass &, StrClass::size_type *>(
                    &stod<SIMDSTRING_ALIGNMENT>, "str"_a, "pos"_a = nullptr));

  m.def("stold", py::overload_cast<const StrClass &, StrClass::size_type *>(
                     &stold<SIMDSTRING_ALIGNMENT>, "str"_a, "pos"_a = nullptr));

  // -------------------------------------------------------------------------------------
  // -- to_string functions

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