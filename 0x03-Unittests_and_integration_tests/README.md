# 0x03. Unittests and Integration Tests

## UnitTests
### Back-end
#### Integration tests
**Weight:** 1

Project started: Apr 4, 2024 6:00 AM  
Project deadline: Apr 9, 2024 6:00 AM  
Checker released: Apr 5, 2024 12:00 PM  
Auto review: Will be launched at the deadline  

Unit testing is the process of testing that a particular function returns expected results for different sets of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low-level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

**Execute your tests with**

```
$ python -m unittest path/to/test_file.py
```

### Resources
- [unittest](https://docs.python.org/3/library/unittest.html) — Unit testing framework
- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html) — Mock object library
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/11121507/how-to-mock-a-readonly-property-with-mock)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- The difference between unit and integration tests.
- Common testing patterns such as mocking, parametrizations, and fixtures.

## Requirements
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

### Required Files
- [utils.py](utils.py)
- [client.py](client.py)
- [fixtures.py](fixtures.py)

## Tasks

### 0. Parameterize a unit test
- Create a `TestAccessNestedMap` class that inherits from `unittest.TestCase`.
- Implement the `TestAccessNestedMap.test_access_nested_map` method to test that the method returns what it is supposed to.
- Decorate the method with `@parameterized.expand` to test the function for specific inputs.

### 1. Parameterize a unit test
- Implement `TestAccessNestedMap.test_access_nested_map_exception` to test exception handling.

### 2. Mock HTTP calls
- Define the `TestGetJson(unittest.TestCase)` class and implement the `TestGetJson.test_get_json` method.
- Use `unittest.mock.patch` to mock `requests.get` and ensure it returns a `Mock` object with a `json` method.

### 3. Parameterize and patch
- Implement the `TestMemoize(unittest.TestCase)` class with a `test_memoize` method.
- Use `unittest.mock.patch` to mock a method and test memoization.

### 4. Parameterize and patch as decorators
- Declare the `TestGithubOrgClient(unittest.TestCase)` class and implement the `test_org` method.
- Use `@patch` as a decorator to mock `get_json` and `@parameterized.expand` to parametrize the test.

### 5. Mocking a property
- Implement the `test_public_repos_url` method to unit-test `GithubOrgClient._public_repos_url`.
- Use `patch` to mock `GithubOrgClient.org` and test the result.

### 6. More patching
- Implement `TestGithubOrgClient.test_public_repos` to unit-test `GithubOrgClient.public_repos`.
- Use `@patch` to mock `get_json` and `patch` as a context manager to mock `_public_repos_url`.

### 7. Parameterize
- Implement `TestGithubOrgClient.test_has_license` to unit-test `GithubOrgClient.has_license`.
- Parametrize the test with specific inputs.

### 8. Integration test: fixtures
- Create the `TestIntegrationGithubOrgClient(unittest.TestCase)` class and implement `setUpClass` and `tearDownClass`.
- Use `@parameterized_class` to parameterize the class with fixtures found in `fixtures.py`.

### 9. Integration tests (advanced)
- Implement `test_public_repos` to test `GithubOrgClient.public_repos`.
- Implement `test_public_repos_with_license` to test with license filtering.

---
© 2024 ALX, All rights reserved.
