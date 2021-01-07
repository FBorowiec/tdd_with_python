load("@rules_python//python:defs.bzl", "py_test")
load("@tdd_with_python_deps//:requirements.bzl", "requirement")

py_test(
    name = "fizzbuzz_with_pytest",
    srcs = ["fizzbuzz_with_pytest.py"],
    deps = [requirement("pytest")],
)
