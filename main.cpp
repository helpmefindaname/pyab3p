#include <pybind11/pybind11.h>
#include "ab3p_source/Ab3P.h"
#include <pybind11/stl.h>
#include <pybind11/functional.h>

namespace py = pybind11;

PYBIND11_MODULE(pyab3p, m) {
    py::class_<AbbrOut>(m, "AbbrOut")
        .def(py::init<>())
        .def_readonly("short_form", &AbbrOut::sf)
        .def_readonly("long_form", &AbbrOut::lf)
        .def_readonly("strat", &AbbrOut::strat)
        .def_readonly("short_form_offset", &AbbrOut::sf_offset)
        .def_readonly("long_form_offset", &AbbrOut::lf_offset)
        .def_readonly("prec", &AbbrOut::prec)
        .def("__str__", [](AbbrOut &abrout) {
            return "AbbrOut(" + abrout.sf + " -> " + abrout.lf + ")";
        })
        .def("__repr__", [](AbbrOut &abrout) {
            return "AbbrOut(" + abrout.sf + " -> " + abrout.lf + ")";
        });

    py::class_<Ab3P>(m, "Ab3p")
        .def(py::init<>())
        .def("get_abbrs", [](Ab3P &ab3p, char *text) {
            try {
                return ab3p.get_abbrs(text);
            } catch (const std::runtime_error &e) {
                throw py::value_error(e.what());
            }
        });
}