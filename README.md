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

# PyBoss

![Boss](Images/boss.jpg)

The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.

The scripts in this project convert your employee records to the new required format. The Python script does the following:

- Imports the `employee_data.csv` file, which currently holds employee records like the below:

```csv
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
```

- Then converts and exports the data to use the following format instead:

```csv
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA
```

- In summary, the required conversions are as follows:

  - The `Name` column should be split into separate `First Name` and `Last Name` columns.

  - The `DOB` data should be re-written into `MM/DD/YYYY` format.

  - The `SSN` data should be re-written such that the first five numbers are hidden from view.

  - The `State` data should be re-written as simple two-letter abbreviations.

- State abbreviations dictionary was used to map the state abbreviations [Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5).

# PyParagraph

![Language](Images/language.png)

In this challenge, you get to play the role of chief linguist at a local learning academy. As chief linguist, you are responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, you've since come up with a fairly simple set of metrics for assessing complexity.

Use the main.py Python script to automate the analysis of any such passage using these metrics. Your script does the following:

- Import all the text files in the raw_data directory. The text files will contain paragraph text of your choosing.

- Assess the passage for each of the following:

  - Approximate word count

  - Approximate sentence count

  - Approximate letter count (per word)

  - Average sentence length (in words)

- As an example, this passage:

> “Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold.”

...would yield these results:

```output
---------------------------------------------------
Paragraph Analysis raw_data/paragraph_3.txt
---------------------------------------------------
Approximate Word Count: 121
Approximate Sentence Count: 6
Average Letter Count per Word: 4.55
Average Sentence Length: 20.17
```
