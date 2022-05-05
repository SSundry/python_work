  #Check whether a person is 18 years old
age= 18
age== 18
  #True

  #Test to see if two numbers are not equal
answer= 17
if answer!= 42:
    print("That is not the correct answer. Please try again!\n")

#You can include various mathematical comparisons in the conditional statements
age = 19

age < 21
#True

age <= 21
#True

age > 21
#False

age >= 21
#False

#'and' checks whether all of the conditions are true for the exp. to be True
age_0 = 22
age_1 = 18
age_0>= 21 and age_1>= 21
#False b/c 18 is not greater than 21
age_1= 23
age_0>= 21 and age_1>= 21
#True b/c 23 is greater than 21

#'or' checks whether at least one of the conditions are true for the exp. to be True
age_0 = 22
age_1 = 18
age_0>= 21 or age_1>= 21
#True b/c age_0 is greater than 21
age_0= 16
age_0>= 21 or age_1>= 21
#False b/c neither is greater than 21