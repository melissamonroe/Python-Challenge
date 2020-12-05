# Python Aventures - Py Me Up, Charlie

## Background

PyBank and PyPoll use Python scripting skills in these real-world situations. Use PyBank to analyze financial records. Use PyPoll to streamline vote counting process.

## PyBank

![Revenue](Images/profitLoss.jpg)

- Use the PyBank/main.py Python script for analyzing financial records. Use financial data set called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Simplified accounting records.)

- The Python script in PyBank analyzes the records to calculate each of the following:

  - The total number of months included in the dataset

  - The net total amount of "Profit/Losses" over the entire period

  - Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  - The greatest increase in profits (date and amount) over the entire period

  - The greatest decrease in losses (date and amount) over the entire period

- Here is an example analysis:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

- The financial script prints the analysis both to the terminal and exports a text file with the results.

## PyPoll

![Vote Counting](Images/votehere.jpg)

- PyPoll/main.py Python script is designed to help a small, rural town modernize its vote counting process.

- The poll data set is called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. The Python script analyzes the votes and calculates each of the following:

  - The total number of votes cast

  - A complete list of candidates who received votes

  - The percentage of votes each candidate won

  - The total number of votes each candidate won

  - The winner of the election based on popular vote.

- Here is an example of the analysis report:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

- In addition, the Election Results report analysis prints to the terminal and exports a text file with the results in to the Analysis directory.
