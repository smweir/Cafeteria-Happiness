Cafeteria Happiness Simulation
This Python program simulates the exploration-exploitation trade-off in selecting cafeterias. It models different strategies for choosing between three cafeterias, each with varying levels of happiness and uncertainty, over multiple trials.

Features:
Exploit-Only Strategy: Always chooses the cafeteria with the highest initial happiness.
Explore-Only Strategy: Cycles through all cafeterias evenly for a set number of days.
E-Greedy Strategy: Balances exploration and exploitation by choosing randomly with a probability e and exploiting the best-known cafeteria otherwise.
Simulation: Runs multiple trials of each strategy and compares the average happiness and regret against the theoretical optimum.

How It Works:
Cafeteria Happiness: Each cafeteria has a normal distribution of happiness (mean and standard deviation) for each visit.
Strategies:
Exploit Only: Choose the cafeteria that initially provides the most happiness.
Explore Only: Visit all cafeterias equally.
E-Greedy: With probability e, explore a random cafeteria; otherwise, exploit the best one.
Simulation: The program runs the simulation over t trials, computes the average happiness for each strategy, and calculates regret (the difference between the achieved happiness and the theoretical optimum).
