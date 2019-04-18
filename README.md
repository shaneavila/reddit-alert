# Reddit Scraper

A simple post notification system from people you follow on Reddit.<br>
![alt text](https://i.imgur.com/r4tS5go.png "Mobile View")
![alt text](https://i.imgur.com/FiQQBVI.png "Desktop View")

Usage
---
Place all packages in a directory then ```cd``` into the directory and run:<br> 
```javac main/*.java heuristics/*.java movements/*.java states/*.java``` then ```java main.Main```<br>

Overview (Informed Search)
---
Informed search algorithms show that if given certain criteria for a desired solution, or a set of rules to follow, it will steer the algorithm to find the solution. The purpose of informed search is to show how the solution was found. Given an initial state, informed search will expand the state to try to see if it can find a solution (goal state) within the given criteria also known as the heuristic function. The heuristic function is an estimate for the cost to the goal from the current state. 

Implementation
---
- [A*](https://en.wikipedia.org/wiki/A*_search_algorithm "Best-First Search")

Heuristics
---
To ensure that A* finds an optimal solution, the heuristics need to be admissible. An admissible heuristic never overestimates the cost of the path. The heuristics used are Hamming and Manhattan distance.
- Hamming Distance: the number of tiles that are not in the goal position
- Manhattan Distance: the sum of the distances of the tiles from their goal position
