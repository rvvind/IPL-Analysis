# IPL Analysis
A simple python program that reads the current points table and results as CSV files, and attempts to predict the winners for the remaining fixtures as well as the final points table. 

## To Use
1. Update two files - `IPL '24 Predictions - Points Table.csv`, `IPL '24 Predictions - Results.csv` with the current information. The defaults in the file as of 4/9/24.
2. If the home team venue has to be changed, update the `IPL '24 Predictions - HomeVenues.csv` file.
3. Execute `iplanalysis.py`.
   1.  Program will print the results for all the matches listed in the fixtures.
   2.  It will print the final points table.
  
## Prediction Algorithms
1. The default algorithm predicts the winner in the following way
   1. If both teams have a positive difference between For versus Against ratio, favor the home team to win. If venue is neutral, favor the team with greater difference to win.
   2. If both teams have a negative difference between For versus Against ratio, favor the home team to win. If venue is neutral, favor the team with lesser difference to win.
   3. If one team has a negative For versus Against ratio, and the other team has a positive For versus Against ratio, favor the team with the positive difference.
2. More algorithms can be added.

## Results
1. Up to date Match level predictions - https://github.com/rvvind/IPL-Analysis/blob/master/IPL%20'24%20Predictions%20-%20Fixtures.csv
2. Predicted Final points table -
   1. 4/9/24: https://github.com/rvvind/IPL-Analysis/blob/master/Predicted%20Points%20Table%20-%204-9-24.csv
