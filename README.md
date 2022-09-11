## Pre Request
install python

### Create Virtual Environtment
1. Create venv
  ```sh
  $ python3 -m pip install --user virtualenv
  ```

2. Activating a virtual environment
  ```sh
  $ source env/bin/activate
  ```

3. Install library using pip
- jsonpath
- requests
- pytest
- pytest-html

  ```

### How to run
1. From your _Terminal_, go to the project directory
2. Run the test cases using the following command
  ```sh
  $ pytest --html=report.html --self-contained-html
  ```
4. Wait until tests executing has finished
5. See the output of tests result in the result folder then open `report.html`  using your browser

---
