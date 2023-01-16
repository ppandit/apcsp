'''
Start working on Quiz 2 (basketball coach program)
Create two lists
One list has 5 starters
Other list has 6 bench players
Display the starters players
Display the bench players
Ask user to substitute one starter for one bench player (need two inputs)
Display the starters and bench player lists again
Ask user again for another substitute or do exit()
'''

starters = ["Jeff", "George", "Clay", "Robert", "Matt"]
bench = ["Harold","Tom", "Vijay", "Sam", "Neil", "Steve"]
numStarters = len(starters)
numBench = len(bench)
again = True

# Not used in the program
def displayStarters():
  i = 0
  print("*** STARTERS ***")
  while (i < numStarters):
    print(starters[i])
    i += 1

# Not used in this program
def displayBenchPlayers():
    i = 0
    print("*** Bench ***")
    while (i < numBench):
      print(bench[i])
      i += 1

def displayPlayers():
    print("*** STARTERS ***", "\t\t", "*** Bench ***")
    i = 0
    tab6 = "\t\t\t\t\t\t"
    tab5 = "\t\t\t\t\t"
    tab4 = "\t\t\t\t"
    tab3 = "\t\t\t"
    tab2 = "\t\t"
    while (i < numBench):
        if (i < numStarters):
            if (len(starters[i]) > 4):
                print(i, "\t", starters[i], tab3, i + 5, " ", bench[i])
                # print('Number one portal is {0}, {1}, and {other}.'
                #      .format('Geeks', 'For', other ='Geeks'))
            else:
                print(i, "\t", starters[i], tab4, i+5," ", bench[i])
        else:
            #print(" ", "\t", " ", tab5, i+5, " ", bench[i])
            print(" ", tab6, i + 5, " ", bench[i])
        i += 1



def substitute(sPlayer, bPlayer):
    starterIndex = -1
    benchIndex = -1

    i = 0
    while (i < numStarters):
        if (starters[i] == sPlayer):
            starterIndex = i
            break;
        i += 1

    j =0
    while(j < numBench):
      if (bench[j] == bPlayer):
          benchIndex = j
          break
      j += 1

    print("TIMEOUT CALLED")
    print("Now substituting" , sPlayer, " with ", bPlayer)
    temp = starters[starterIndex]
    starters[starterIndex] = bench[benchIndex]
    bench[benchIndex] = temp
    print("GAME RESUMES")


if __name__ == '__main__':
    displayPlayers()
    while (again == True):
        s, b = input("Enter the starter name and the bench player names separated by space: ").split(" ", 2)
        substitute(s, b)
        displayPlayers()
        response = input("Subsitute again? Y or N  ")
        if (response == 'N' or response == 'n'):
            again = False