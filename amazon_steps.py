steps = []

def findSteps(steps,T):
    if T == 0:
        print(steps)
    elif T > 0:
        findSteps(steps+[1],T-1)
        findSteps(steps+[2],T-2)

findSteps(steps,4)