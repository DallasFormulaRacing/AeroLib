# DFR AeroLib

## IMPORTANT

This code does not represent the finished product and is currently completely built upon the loose requirements provided by [@GHAFHA](https://github.com/GHAFHA). This README is however up to date with all current changes.

## Quick Setup / Install

Once you have downloaded the repo, either via clicking the green button in the top left of the repo and selecting **Download ZIP** or via cloning the repo locally, and [Python 3.11](https://www.python.org/downloads/) or higher, you can follow the below instructions.

1. If you have not already, use `pip` to install the package `pipenv`, you can do this by opening a command line and entering the following command `pip install pipenv`
2. Once you have pipenv, select the directory in which you unpacked/cloned the repo and run the command `pipenv install`
3. After the install process completes, you can then run the test script by using the following command `pipenv run python test.py`
4. Upon running this command, you should automatically be presented with a screen that looks like this, this is how all data will be displayed, based upon the supplied parameters when using the class.

![image](https://github.com/DallasFormulaRacing/AeroLib/assets/58915403/f131f85e-100d-4ed7-8d19-d53e289d6926)

## How to use the `display_plot` function

**As shown in the `test.py` file, it is currently necessary to double define the dataset that you wish to use when displaying data.**

1. Create a class object of the `handler.py` by adding the following code to your program. The plot_functions constructor takes one argument `file_path1`, which is the respective file path to the data that you wish to use upon initialization, (although this has little use with respect to the `display_plot` function, as we wanted to be able to supply a different data set each time if need be)

```py
from handler import plot_functions

plotFuncs = plot_functions(file_path1="data/aerodata.csv")
```

2. After you have created an object of the handler class, you can then call the `display_plot` function using the following code. (`display_plot` uses 4 arguments, `data_path` the file path to the CSV storing the data, `x` a `List` object that holds the indices of the required x values to be plotted, `y` a string object that contains the index of the y value to be plotted, and `to_file` which will write the processed data to a file.

```py
plotFunc.display_plot(data_path="data/aerodata.csv", x=["Rear Rideheight", "Front Rideheight"], y="ClA", to_file=False)
```

**The above example uses the file `data/aerodata.csv` as its source of data, and then plots the `Rear Rideheight` and `Front Rideheight` as a function of `ClA`. Finally, it does not write this data to a file, hence `to_file` being `False`**
