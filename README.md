# Overview of the Algorithm

## High Level Algorithm
Retrieve google results for query through xgoogle library. Rank them.
Retrieve results from the White House scraper. Rank them.
If the sum of these results' weights is less than a given threshold,
Append one of the top 5 highest weighted keywords (mod query length) to the original query and go to google again, ranking those results with the rest.

## Ranking Algorithm
Given a result that has properties such as 'title', 'desc', and 'url', extract the keywords into a KeywordList for each section of the result.
A KeywordList is essentially a dictionary which maps keywords to a list of all the places they appear in the section. So for example the string:
'The quick brown fox the' with keywords ['the', 'quick'] would create a keyword list like so: {'the': [0, 21], 'quick': [4]}
This keyword list is then passed to a SignalVector. A SignalVector contains a set of signals that this keyword list is passed through. Each one of those
signals returns a number where higher indicates more relevant. This resulting vector of numbers is the multiplied by a coefficient vector which represents
the weighting of each individual signal. This generates a single number for a result.

## Signals
The weight signal simply adds the weights of all keywords in all sections of the result

The location signal adds only the weights of the keywords in the 'title' secion of the result

The proximity signal loops through all keywords and all of their occurences and calculates the distance from the end of the word to the beggining of each other keyword occurence. It then
takes an average of the distances between keywords and uses that as a measure for how close these keywords appear together.

This approach allows us to rely entirely on the coefficient vector for deciding how valuable each of these signals are. For example: if we decided that keywords in the title are twice as important
as those in the body we could assign a vector like this: {'weight': 1, 'location': 1, 'proximity': 0}. Since the weight signal adds both the keywords from the 'desc' and the 'title' and the location
signal does just the 'title', we end up with something like weight-of-desc + weight-of-title + weight-of-title => weight-of-desc + 2 * weight-of-title.

## What Worked

* The White House scraper works extremely well. It allows us to pull in actual petitions when users search for terms that appear somewhere on the whitehouse petition site.
* The linear algebra approach to signal weighting. This allowed us to manipulate the coefficients until results were within our liking. It made small changes to our algorithm easy.
* Using a threshold to determine if the query needed manipulation. This allows us to make it non-obvious to users because we aren't manipulating their query all the time.
* The code is written in a way that would very easily allow for the addition of new signals if time had allowed. Very flexible code.

## What Didn't

* We were initially just simply tacking on 'petition' when a query needed to be manipulated. This worked extremely well, however, it was also extremely obvious.
We found that instead picking from the top 5 keywords modulo the length of the query string we were able to manipulate the query well enough with it being too obvious.
* The proximity signal is a little bit slow and does not add that much to the differentiation of results. We are considering removing it.

## Results
