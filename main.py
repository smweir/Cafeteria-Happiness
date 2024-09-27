import random

## Given Cafeteria Examples
h1 = 10
d1 = 8
h2 = 15
d2 = 6
h3 = 12
d3 = 5


def main():
    # Call statement to run simulation
    simulation(100000, 10)


def exploitOnly():
    c1 = random.normalvariate(10, 8)
    c2 = random.normalvariate(15, 6)
    c3 = random.normalvariate(12, 5)
    highest_happiness = max(c1, c2, c3)
    total = c1 + c2 + c3
    if highest_happiness == c1:
        for i in range(297):
            total += random.normalvariate(10, 8)
    elif highest_happiness == c2:
        for i in range(297):
            total += random.normalvariate(15, 6)
    elif highest_happiness == c3:
        for i in range(297):
            total += random.normalvariate(12, 5)
    return total


def exploreOnly():
    ## Output Variable
    total_happiness = 0

    ## Loop for each cafe for 100 days
    days = 100
    while days != 0:
        Caf1 = random.normalvariate(10, 8)
        Caf2 = random.normalvariate(15, 6)
        Caf3 = random.normalvariate(12, 6)
        total_happiness += Caf1 + Caf2 + Caf3
        days -= 1

    ## return statement
    return total_happiness


def eGreedy(e=10):
    import random
    cafeterias = []
    happiness = 0
    for days in range(0, 300):
        if days != 0:
            best = cafeterias.index(max(cafeterias))
        C1 = random.normalvariate(10, 8)
        C2 = random.normalvariate(15, 6)
        C3 = random.normalvariate(12, 5)
        checker = random.random()


        if checker <= e/100:
            check_random = True
        else:
            check_random = False
        if days < 3:
            if days == 0:
                cafeterias.append(C1)
                happiness += C1
            elif days == 1:
                cafeterias.append(C2)
                happiness += C2
            elif days == 2:
                cafeterias.append(C3)
                happiness += C3
        elif not check_random:
            if best == 0:
                happiness += C1
            elif best == 1:
                happiness += C2
            elif best == 2:
                happiness += C3
        elif check_random:
            caf_to_visit = random.randint(0, 2)
            if caf_to_visit == 0:
                cafeterias[0] = C1
                happiness += C1
            elif caf_to_visit == 1:
                cafeterias[1] = C2
                happiness += C2
            elif caf_to_visit == 2:
                cafeterias[2] = C3
                happiness += C3
    return happiness


def simulation(t, e):
    ## Greatest average happiness of the three cafeterias
    bigHapp = max(h1, h2, h3)

    ## Optimum Happiness
    OptimumHappiness = 300 * bigHapp

    ## Expected Happiness
    exploitExpectHapp = h1 + h2 + h3 + 297 * bigHapp
    exploreExpectHapp = 100 * h1 + 100 * h2 + 100 * h3
    eVal = e / 100
    eGreedyExpectHapp = (1 - eVal) * 300 * bigHapp + eVal * 100 * h1 + eVal * 100 * h2 + eVal * 100 * h3

    ## Expected Regret
    exploitExpectRegret = OptimumHappiness - exploitExpectHapp
    exploreExpectRegret = OptimumHappiness - exploreExpectHapp
    eGreedyExpectRegret = OptimumHappiness - eGreedyExpectHapp

    ## Total Happiness
    totalHappExploit = 0
    totalHappExplore = 0
    totalHappEGreedy = 0
    for i in range(0, t):
        totalHappExploit += exploitOnly()
        totalHappExplore += exploreOnly()
        totalHappEGreedy += eGreedy(e)
        i += 1

    ## Average Happiness
    avgHappExploit = totalHappExploit / t
    avgHappExplore = totalHappExplore / t
    avgHappEGreedy = totalHappEGreedy / t

    ## Average Regret
    avgRegretExploit = OptimumHappiness - avgHappExploit
    avgRegretExplore = OptimumHappiness - avgHappExplore
    avgRegretEGreedy = OptimumHappiness - avgHappEGreedy

    ## Print Statements
    print("\nSimulation of " + str(t) + " Times:")
    print("\nOptimum Happiness: " + str(OptimumHappiness))
    print("\nExpected Happiness of Each Method\nExploit: " + str(exploitExpectHapp) + "\nExplore: " + str(
        exploreExpectHapp) + "\neGreedy: " + str(eGreedyExpectHapp))
    print("\nExpected Regret of Each Method\nExploit: " + str(exploitExpectRegret) + "\nExplore: " + str(
        exploreExpectRegret) + "\neGreedy: " + str(eGreedyExpectRegret))
    print("\nAverage Happiness of Each Method\nExploit: " + str(avgHappExploit) + "\nExplore: " + str(
        avgHappExplore) + "\neGreedy: " + str(avgHappEGreedy))
    print("\nAverage Regret of Each Method\nExploit: " + str(avgRegretExploit) + "\nExplore: " + str(
        avgRegretExplore) + "\neGreedy: " + str(avgRegretEGreedy) + "\n")


main()

