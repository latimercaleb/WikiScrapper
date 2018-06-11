# WikiScrapper

## What is it?
Assuming the user is at the Wikipedia article for Wild Yak​ .
> What’s the lowest number of clicks to get to the article for the ​ Phil McGraw​ ?

## Acceptance Criteria
* Write a program that can take the URLs of two Wikipedia pages and output the
minimum number of clicks to get from one to the other.

* Your program should be runnable one the command line like this:
`$ my_program ‘Wild yak’ ‘Phil McGraw’`

* The program’s output should include each link that needs to be clicked to reach the final destination of Phil McGraw.

**Technical Constraints**
* None

## Implementation strategy
Our solution will use Python and Bash with cli serving as the interface to produce the results. Work will be done as a collective using slack as a medium of communication and git as a means of hosting and testing against the use case.

**Technical Challenges**
* Navigating to the page and generating the proper link to the end page
* Scrapping all active links on pages and storing them
* Optimization of use case and performance
