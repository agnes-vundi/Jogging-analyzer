### Jogging-analyzer
 jogging is important for one's health and sprit!
 
 Note: This was part of my studies course work project.
 
 **Program Behavior**
 
 Program starts by asking the user the number of days they want to analyze:
 
 
 ```
 Enter the number of days:
 ```
 
 When the user has entered the number of days, the program starts inquiring the number of kilometers the user jogged in each day:
 
 
 ```
 Enter day X running length:
 ```
 
 
 Where X is a placeholder for the number of the day, starting from 1.

 If the user enters zero kilometers in three consecutive days, the program should print:
 
 
 ```
 You had too many consecutive lazy days!
 ```
 
 
Then the program should quit without any further output.

When the user has entered jogging data for X days, the program displays its judgement in one of the following formats.

If the average of the kilometers jogged per day is less than 3.00 kilometers, the program should print: 
 
 
 ```
 Your running mean of Y.YY km was too low!
 ```
 
 
 On the other hand, if the average is 3.00 kilometers or more, the printout should be:
 
 
 ```
 You were persistent runner! With a mean of Y.YY km.
 ```
 
 
In both cases above Y.YY is the placeholder for the average of the jogging distances expressed with two decimals.

Program ends after the printout
 
 
 **Example Runs**
 An example of the output when the program works correctly.
 
 
```
Enter the number of days: 7
Enter day 1 running length: 3
Enter day 2 running length: 0
Enter day 3 running length: 0
Enter day 4 running length: 7
Enter day 5 running length: 8
Enter day 6 running length: 5.4
Enter day 7 running length: 7.1

You were persistent runner! With a mean of 4.36 km.
```
 
 
 
 
 
 
 
 
 
 
 
 
 
