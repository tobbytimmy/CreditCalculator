#Credit Calculator
This is a program that calculates the amount of debt you have or the 
number of months left to pay off the credit
## Getting Started

Download the project repo ZIP and extract it.

Extract the ZIP file.
### Prerequisites

```
Python 3.7
```


## Running the tests


Open the Command Line or Terminal and go to the directory of the project.

Then run the program while passing the required arguments.

### Input Arguments

* --type, which indicates the type of payments: "annuity" or "diff" (differentiated).
* --payment, that is a monthly payment.
* --principal is used for calculations of both types of payment
* --periods parameter denotes the number of months and/or years needed to repay the credit.
* --interest is specified without a percent sign. Note that it may accept a floating-point value.

### Break down into end to end tests

```
python main.py --type=diff --principal=1000000 --periods=10 --interest=10

Output- 
Month 1: paid out 108334
Month 2: paid out 107500
Month 3: paid out 106667
Month 4: paid out 105834
Month 5: paid out 105000
Month 6: paid out 104167
Month 7: paid out 103334
Month 8: paid out 102500
Month 9: paid out 101667
Month 10: paid out 100834

Overpayment = 45837

```

```
main.py --type=annuity --principal=1000000 --periods=60 --interest=10

Output:
Your annuity payment = 21248
Overpayment = 274880

```



## Built With

* Python 3.7- The programming language used.

## Authors

* **Oluwatobi Olutimehin** 

