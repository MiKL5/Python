age      = 19
sentence = "I've {age} yo."

age      = 16
sentence = "I've {} yo.".format(age)

age      = 16
sentence = "I've {a} yo.".format(a.age)

age      = 16
sentence = "I've {a} yo , {}.".format(a.age) # erreur

age      = 16
sentence = "I've {0} yo , {0} I'm teenager.".format(a.age)

firstname = "Kevin"
age       = 16
sentence  = "He's {} yo , {} his name is.".format(age , firstname)

firstname = "Kevin"
age       = 16
sentence  = "He's {1} yo , {0} his name is.".format(firstname , age)