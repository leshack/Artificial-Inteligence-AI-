import random


class Environment(object):
    def __init__(self):
        self.locationcondition = {'A': random.randint(0, 1), 'B': random.randint(0, 1)}
        # RANDOM CONDITION


# score is a measure of performance, if it cleans a square, it gets awarded a point
class Sreflexagent(Environment):
    def __init__(self, environment):
        print("Current Environment condition")
        print(environment.locationcondition)
        # place vacuum at random location
        vacuumlocation = 1
        score = 0

        # if vacuum is at location A, print its placed at A, then if its dirty, clean it, else move to B
        if vacuumlocation == 0:
            print("1: vacuum is randomly placed at Location A")
            # covers {[1] [1]} and {[1] [0]}
            if environment.locationcondition['A'] == 1:
                print("2. Location A is dirty")
                environment.locationcondition['A'] == 0
                score = score + 1
                print("3. Location A has been cleaned")
                print("4. moving to location B")
                if environment.locationcondition['B'] == 1:
                    print("5. Location B is dirty")
                    environment.locationcondition['B'] == 0
                    score = score + 1
                    print("6. Location B has been cleaned")
                    print("score:", score)
                else:
                    print("5. Location B is clean")
                    print("score:", score)
            # covers {[0] [0]} and {[0] [1]}
            else:
                print("2. Location A is clean, moving to location B")
                # if B is dirty clean, else say its clean
                if environment.locationcondition['B'] == 1:
                    print("3. Location B is dirty")
                    environment.locationcondition['B'] == 0
                    score = score + 1
                    print("4. Location B has been cleaned")
                    print("score:", score)
                else:
                    print("3. Location B is clean")
                    print("score:", score)

        # if location starts with B...
        elif vacuumlocation == 1:
            print("1. vacuum is randomly placed at Location B")
            # covers {[1] [1]} and {[0] [1]}
            if environment.locationcondition['B'] == 1:
                print("2. Location B is dirty")
                environment.locationcondition['B'] == 0
                score = score + 1
                print("3. Location B has been cleaned")
                print("4. moving to location A")
                if environment.locationcondition['A'] == 1:
                    print("5. Location A is dirty")
                    environment.locationcondition['A'] == 0
                    score = score + 1
                    print("6. Location A has been cleaned")
                    print("score:", score)
                else:
                    print("5. Location A is clean")
                    print("score:", score)
            # covers {[0] [0]} and {[1] [0]}
            else:
                # move to A
                print("2. location B is clean, moving to Location A")
                # if A is dirty
                if environment.locationcondition['A'] == 1:
                    print("3. Location A is dirty")
                    environment.locationcondition['A'] == 0
                    score = score + 1
                    print("4. Location A has been cleaned")
                    print("score:", score)
                else:
                    print("3. Location A is clean")
                    print("score:", score)


# print(Environment.locationcondition)
theEnvironment = Environment()
thevacuum = Sreflexagent(theEnvironment)