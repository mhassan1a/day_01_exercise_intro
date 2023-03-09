## Introductory Exercises
Thank you for taking our course. Completing the following tasks will prepare you for the exercise sessions in the coming weeks. Machine learning on larger scales often requires using central compute clusters, which run on Linux. Consequently, we will use workstations running Ubuntu Linux.


### Task 1: Setting up your repository.
- Configure GitHub for ssh access. You need to generate a key pair and add the public key to your GitHub account.
  - To generate your key follow the steps in: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
  - How to add a key is described here: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
- Open a terminal by pressing `Ctrl+Alt+T`.
- Clone this repository by running `git clone git@github.com:Machine-Learning-Foundations-in-Python/day_01_exercise_intro.git` in the terminal. Navigate into this directory by typing `cd day_01_exercise_intro`.

In Vscode, you can now open a rendered version of this readme. Right-click the file and select `open Preview`.

### Task 2: Downloading and installing Miniconda.
- Navigate to `https://docs.conda.io/en/latest/miniconda.html` in your favorite browser.
The HRZ-Pool computers run Ubuntu Linux. Download the `Miniconda3 Linux 64-bit` file.

- Open the terminal on your machine by pressing `Ctrl+Alt+T`. Navigate into the Downloads folder by typing `cd Downloads`. Before running the installer, set the executable bit by typing `chmod +x Miniconda3-latest-Linux-x86_64.sh`. Install Miniconda via `./Miniconda3-latest-Linux-x86_64.sh` .


### Task 3: Setting up Vscode for python development
- Click on the extensions tab or press `Ctrl+Shift+X`. Install the `Python` and `Remote-SSH` extensions. Choose the versions provided by Microsoft.
- Make the Miniconda interpreter your default in Vscode by pressing `Ctrl+Shift+P`. A terminal opens. Type `select interpreter` and press enter. In the following dialogue, choose the `base` environment. 

### Task 4: Installing dependencies
- Open a terminal by pressing `Ctrl+Alt+T`. Navigate into this directory by typing `cd path_to_this_folder`. Type

  ```bash
  pip install -r requirements.txt
  ```
To install the python packages required for this exercise.

### Task 5: Run an automatic test.
- Scientific software must provide reproducible results. Automatic testing ensures our software runs reliably. We recommend Nox for test automation `https://nox.thea.codes/en/stable/`. 
- To run some of the tests we prepared for you type,
    ```bash
    nox -s test
    ```
  The python extension provides test integration into Vscode. To use it, click on the lab-flask icon on the left sidebar. When opening it for the first time, it asks you for a configuration.
  Click the `Configure Python Tests` button and select `pytest` in the ensuing prompt. In the next step, Vscode wants to know the location of the test folder. Choose `tests`. 
  Vscode will now display your tests on the sidebar on the left. Click the play symbol next to the tests folder to run all tests.

### Task 6: Implement and test a python class.
- Open `src/my_code.py` and finish the `__init__` function of the `Complex` class. The idea here is to implement support for complex numbers. Double-check your code by running `nox -s test`. 

### Task 7: Breakpoints
- Click on a line number in `my_code.py`. A red dot appears. Press the `debug_test` button in the `Testing` tab, Python will pause, and you can use the build-in `Debug console`` to explore the data at this point.

### Task 8: Implement the remaining functions in my_code.py
- Implement and test the `add`, `radius`, `angle`, and `multiply` functions.

### Task 9: Plotting
- Run `python ./src/julia.py` to comput a plot of the Julia set with your `Complex` class (see: https://en.wikipedia.org/wiki/Julia_set for more information).
- In `src/julia.py` use `plt.plot` and `plt.imshow` to visualize the julia-set. Feel free to play with `c` to create different sets.


### Task 10: Getting nox to help you format your code.
- Professionally written python code respects coding conventions. Type `nox -s format` to have `nox` format your code for you.

### Optional Task 11: Linting
- `nox` can do even more for you! A basic syntax error at the wrong place can cost days of computation time. Type
  ```bash
  nox -s lint
  ```
  to check your code for formatting issues and syntax errors.

### Optional Task 12: Typing
- Take a look at https://docs.python.org/3/library/typing.html . `nox` can help you by checking your code for type problems and incorrect function signatures.
  ```bash
  nox -s typing
  ```
