#include <pybind11/pybind11.h>
#include "ab3p_source/Ab3P.h"
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include <pybind11/embed.h>

namespace py = pybind11;

std::string getModulePath()
{
    py::object module = py::module::import("word_data");
    py::list module_paths = module.attr("__path__");
    return module_paths[0].cast<std::string>();
}

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

    py::class_<iret::Ab3P>(m, "Ab3p")
        .def(py::init([]() {
            return new iret::Ab3P(getModulePath());
        }))
        .def("get_abbrs", [](iret::Ab3P &ab3p, char *text) {
            try {
                return ab3p.get_abbrs(text);
            } catch (const std::runtime_error &e) {
                throw py::value_error(e.what());
            }
        });
}