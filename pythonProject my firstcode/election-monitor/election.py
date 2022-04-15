# ELECTION WINNER PICKER ALGORITHM
votes_casted = []
while True:
    print("choose one of the candidates from these three contestants; "
          "\n>Obi \n>Ada \n>Uzo \nType in the name of your choice below")
    a = input("> name: ")
    a = a.lower()
    votes_casted.append(a)
    if a == "off":
        break
print(votes_casted.count("obi"), "is Obi's number of votes")
print(votes_casted.count("ada"), "is Ada's number of votes")
print(votes_casted.count("uzo"), "is uzo's number of votes")
election_winner = max(votes_casted, key=votes_casted.count)
print(F"The winner of the election is {election_winner}")

"""
Copyright: 2021
Author Ibeh Chinazo Kizito
"""
