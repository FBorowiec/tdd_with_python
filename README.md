# TDD with GoogleTest

*"Deleted code is debugged code"* - **J.Sickel**

This is the repository where I keep all the relevant information about Test Driven Development with Python.
For more information about Test Driven Development visit:

[FBorowiec/tdd_with_gtest](https://github.com/FBorowiec/tdd_with_gtest)

## **Motivation**

Having a buggy code base causes lots of problems. It can affect schedules. Some portion of the development team has to stop new future development to go back and fix critical bugs. It can slow down development in general, as developers will be more weary to make changes when they are working in a buggy and brittle code base. And it can erode customer's confidence. Both because they are experiencing the bugs and because of slip schedules on new features while fixing those bugs. So what can a software developer do to eliminate as many bugs as possible in the code before it gets released? A multi layered safety net of tests in place that will catch any bugs that might get introduced. And the first layer of this safety net should be a sweep of automated unit tests. Units test verify the code at the level of functions and classes. They perform positive and negative test cases at the lowest level of the code. Every line of production code should have an associated unit test that verifies it's working as expected. Test driven development, or TDD, is a practice of writing unit tests before writing production code. This is backwards to the way most developers write code but it has many benefits. If there is a problem it's easy to track down as there's a  only a small amount of code written since the last test executed. And TDD gives  confidence to change the code as it is known immediately if anything has gotten broken by any particular code change.

_"Making large changes without tests is like doing aerial gymnastics without a net."_ - **Michael Feathers**, unit tester and author of Working Effectively with Legacy Code

## **Unit tests**

* Verify the code at a level of functions and classes
* Perform negative and positive test cases at the lowest level of the code
* Every line of production code should have an associated unit test to verify it's working as expected

### **Why Unit Test?**

* Software bugs hurt businesses
* Software testing catches the bugs before they get to the field
* Need several levels of safety nets
* Serves also the purpose of documenting what the code is actually doing
* Drives good object oriented design

### **Levels of Testing**

1. Unit testing:
    * Testing at the function level
    * This is generally the lowest level of testing and most comprehensive
    * A test should be written for each test case for a function (all positive and negative test cases)
    * Group of tests can be combined into test suites for better organization
    * Executes in the development environment rather than the production environment
    * Execution of the tests should be automated
    * They should be ran often so they should be fast
2. Component Testing:
    * Testing at the library and compiled binary level
    * This tests external interfaces of these components
3. System Testing (Integration tests):
    * Tests the external interfaces of a system which is a collection of sub-systems
4. Performance Testing:
    * Testing done at sub-system and system levels to verify timing and resource usages are acceptable

## **Test Driven Development (TDD)**

* Is a practice of writing unit tests before writing production code
* This has the benefit of knowing that each of the new lines of code are working as soon as they're written
* It's easier to track down problems as only a small amount of code has been implemented since the execution of the last test
* It gives more confidence in changing the code as the feedback loop is very short
* All test cases shouldn't be implemented at once but rather gradually as the code evolves
* _TDD has been created by Kent Beck in the 1990's as part of the Extreme Programming software development process_

### **RED -> GREEN -> REFACTOR workflow phases**

1. Writing a failing Unit test (RED phase)
2. Writing just enough production code to make that test pass (GREEN phase)
3. Refactoring the unit test and the production code to make it clean (REFACTOR phase)

### **Uncle Bob's (Robert Martin) 3 laws of TDD**

1. Thou shall not write any production code unit you ahve written a failing unit test
2. Thou shall not write more of a unit test than is sufficient to fail, and not compiling is failing
3. Thou shall not write more production code than is sufficient to pass the currently failing unit test

## **What is PyTest**

* PyTest is a Python unit testing framework.
* It provides the ability to create tests, test modules, test classes, and test fixtures.
* It uses the built-in Python assert statement which makes implementing unit tests much simpler than other Python unit testing frameworks.
* It also adds many useful command line arguments to help specify what tests should be run and in what order.

In PyTest, individual tests are Python functions with test at the beginning of the function name. The unit tests then execute production code and use the standard Python assert statement to perform verifications on results. Similar tests can be grouped together by including them in the same module or class.

### **XUnit style Setup and Teardown**

`def setup_module()`
`def teardown_module()`
`def setup_function()`
`def teardown_function()`
`def setup_class()`
`def teardown_class()`
`def setup_method()`
`def teardown_method()`

### **Test doubles**

It is possible to run unit tests in isolation using the concepts of dummies, fakes, stubs, spies, and Mocks. So what are test doubles? Almost all code that gets implemented will depend on another piece of code in the system. Those other pieces of code are often times trying to do things or communicate with things that are not available in the unit testing environment, or are so slow they would make our unit tests extremely slow. For example, if the code queries a third-party rest API on the internet, and that server is down for any reason, the test can't be run. Test doubles are the answer to that problem. They are objects that are created in the test to replace the real production system collaborators. There are many types of test doubles:

* **Dummy** objects are the simplest. They are simply placeholders that are intended to be passed around but not actually called or used in any real way. They'll often generate exceptions if they're called.
* **Fake** objects have a different and usually simplified implementation from the production collaborator that make them usable in the test code, but not suitable for production.
* **Stubs** provide implementations that do expect to be called, but respond with basic canned responses.
* **Spies** provide implementations that record the values that are passed into them. The tests can then use those recorded values for validating the code under test.
* **Mock objects** are the most sophisticated of all the test doubles. They have pre-programmed expectations about the ordering of calls, the number of times functions will be called, and the values that will be passed in. Mock objects will generate their own exceptions when these pre-programmed expectations are not met.

#### **Mock frameworks**

*Mock framework*s are libraries that provide easy-to-use API's for automatically creating any of these types of test doubles at runtime.
They provide easy API's for specifying the Mocking expectations in your unit test. They can be much more efficient than implementing custom Mock objects, because creating custom Mock objects can be time consuming, tedious, and error prone.

#### **`unittest.mock`**

*Unittest.mock* is a Mocking framework for Python. It's build into the standard unit test for Python, in version 3.3 and newer, and for older versions of Python, a back-ported version of the library is available on *pypi*, called Mock, and can be installed with the command `pip install Mock`.

*Unittest.mock* provides the Mock class, which is an extremely powerful class that can be used to create test objects that can be used as fakes, stubs, spies, or true Mocks for other classes or functions.
The Mock class has many initialization parameters for specifying how the object should behave, such as what in interface it should Mock, if it should call another function when it's called, or what value it should return.
Once a Mock object has been used, it has many built-in functions for verifying how it was used, such as how many times it was called, and with what parameters.
Mock provides many initialization parameters which can be used to control the Mock objects behavior:

* The `spec` parameter specifies the interface that the Mock object is implementing. If any attributes of the Mock object are called which are not in that interface, then the Mock will automatically generate an attribute exception.
* The `side_effect` parameters specifies a function that should be called when the Mock is called. This can be useful for more complicated test logic that returns different values depending on input parameters or generates exceptions.
* The `return_value` parameter specifies the value that should be returned when the Mock object is called. If the side_effect parameter is set, it's return value is used instead.

Mock provides many built-in functions for verifying how the Mock was called, including the following assert functions:

* The `assert_called` function will pass if the Mock was ever called with any parameters.
* The `assert_called_with` function will pass if the Mock was ever called with the specified parameter.
* The `assert_called_once` function will pass if the Mock was called exactly one time. The assert_called_with function will pass if the Mock was last called with the specified parameters.
* The `assert_called_once_with` function will pass if the Mock was called exactly once with the specified parameters.
* The `assert_any_call` function will pass if the Mock was ever called with the specified parameters.
* And the `assert_not_called` function will pass if the Mock was never called.

Mock provides these additional built-in attributes for verifying how it was called:

* The `assert_has_calls` function passes if the Mock was called with parameters specified in each of the passed in list of Mock call objects, and optionally in the order that those call objects are put into the list.
* The `called` attribute is a boolean which is true if the Mock was ever called.
* The `call_count` attribute is an integer value specifying the number of times the Mock object was called.
* The `call_args` attribute contains the parameters that the Mock was last called with.
* And the `call_args_list` attribute is a list with each entry containing the parameters that were used in call to the Mock object.

*Unittest.mock* also provides the *MagicMock* class. *MagicMock* is derived from Mock and provides a default implementation of the Python magic methods. These are the methods with double underscores at the beginning and end of the name, like `__str__`.

The following magic names are not supported by *MagicMock*, due to being used by Mock for other things, or because mocking them could cause other issues:

* `__get_attr__`
* `__set_attr__`
* `__init__`
* `__new__`
* `__prepare__`
* `__instancecheck__`
* `__subclasscheck__`
* `__del__`

When using *MagicMock*, the magic methods are already created and take note of the default values that are returned from those functions to ensure they match the needs of the test that's being implemented.
**PyTest** provides the Monkeypatch Test Fixture to allow a test to dynamically change modules and class attributes, dictionary entries, and environment variables.
**Unittest** provides a patch decorator which provides similar operations, but this can sometimes conflict with the PyTest Text Fixture decorators.

## How to run the code locally with *Bazel* already installed on host

### Bazel installation

[Install Bazel](https://docs.bazel.build/versions/master/install.html)

Once you have successfully installed *Bazel* you can run the code using:

```bash
bazel test //...
```

## Run the code inside a container

You can use my following Docker image to instantiate a container locally with Ubuntu and Bazel already installed:

```bash
docker run -it --rm framaxwlad/ubuntu_dev:latest
```

There you can simply clone the repository:

```bash
git clone https://github.com/FBorowiec/tdd_with_python.git
cd tdd_with_python/
```

And use the aforementioned commands to run the program:

```bash
bazel test //...
```

## **Best practices**

* Write the next simplest test case
* Do not jump into the complex test cases too quickly
* Use descriptive test names
* Test suites should name the class or function under test and the test names should describe the functionality being tested
* Keep tests fast
* Keep console output to a minimum to avoid cluttering
* Mock out any slow collaborators with test doubles that are fast
* Use code coverage tools
* Run tests multiple time and in random order
