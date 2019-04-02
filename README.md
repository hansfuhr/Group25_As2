<h1>Jae Ung Kim-Assignment 3</h1>
<h1>Project name: AutoBot 2.0</h1>

<h2>About the project</h2>
This project is called Autobot and is essentially an AI that assists a user in picking a car, truck, SUV, motorcycles, and bicycles. This is done by asking the user a series of questions which helps Autobot predict what the user will prefer. Autobot is mainly for users who may have limited knowledge of what type of vehicle they are interested in.

<h2>Navagation for software</h2>

VehicleList.py contains all updated features from A2 listed below.

<h2>Code organization</h2>
In VehicleList.py the codes are organized into 4 parts separated by comments.
1. Database of cars
2. Text input for text matching check
3. Function for text finding 
4. Methods for compiling 

<h2>Features programmed for Assignment 3</h2>

1. (2 points): Add an extra topic to your agent's repertoire. Ensure this topic has
similarities with the original topic. For example, if your original topic is
volleyball, you may want to add basketball as a second topic.

- added motorcycles to database

sample output: 

  (AutoBot)   Are you a car, truck, suv, or motorcycle kind of person? Car, truck, SUV, or motorcycle:\
  (Input)     motorcycle\
  (AutoBot)   I have found 9 vehicles that match your criteria!
  (AutoBot)   Here is a/an motorcycle. \
              It is a 2019 Kawasaki Ninja ZX-6R, it seats 2 \
              and gets 35 miles to the gallon. \
              You can walk away with this motorcycle for $11999\
              Are you happy with this vehicle?\
  (Input)     Yes

2. (3 points): Add a feature that enables your agent to give at least 5 different
reasonable responses when the user enters something outside the two topics.

- added reseponses to answers that are not related to the topic (selecting a vehicle)

sample output:

  (AutoBot)   We can't recognize what you mean by that :(\
              Would you like to try again? (y/n)\
  (Input)     y\
  (AutoBot)   Do you want to know about computers? (y/n)\
  (Input)     y\
  (AutoBot)   Apple's macbook is so expensive\
              Did you know if you fully upgrade macbook pro 15 with touchbar\
              You have to pay like 8400 dollars\
              WooooooW\
              Have a nice day\
3. (5 points): Add a feature that enables your agent to handle spelling mistakes of
the words that your agent is supposed to recognize. Do not hardcode your
solution. Develop a general feature you can use for all the words your agent
has, rather than hardcoding a bunch of possible mistakes people could make.
For example, use the Porter Stemmer, or some other pre-established algorithm.
    o If user inputs spelling mistakes or random inputs in greetings, AutoBot asks whether it is a spelling mistake 
      and if it is, allow user to correct it and if not we ask user if they want to hear something else other than selecting a vehicle
      - Sample Output:
        (AutoBot)   Welcome to Autobot, can I assist you today?\
        (Input)     suer
        (AutoBot)   We can't recognize what you mean by that :(
        (Input)     "Was it a spelling error? Would you like to try again? (y/n)"
        (Input)     y
        (AutoBot)   Welcome to Autobot, can I assist you today?\
        (Input)     sure

4. (10 points each): Use of language toolkits, incorporate feature to improve your
conversation's flow:\
    o Synonym recognition - WordNet (you'll need a Java API to it)\
    - AutoBot can generate synonmy of word 'happy' if user feels like not talking about anything to brighten up his/her day!
    - Sample Output:
      (AutoBot)   Hello, my name is Autobot, can I help you find a vehicle today?
                  We currently have 124 vehicles in our inventory.
      (Input)     wefqef
      (AutoBot)   We can't recognize what you mean by that :(  
                  Was it a spelling error? Would you like to try again? (y/n)
      (Input)     n
      (AutoBot)   Okay, maybe you want to know about computers instead! (y/n)
      (Input)     n
      (AutoBot)   Alright than! Maybe I will tell you the synonyms of 'happy' to brighten up your day!
                  {'well-chosen', 'felicitous', 'happy', 'glad'}
                  Have a nice day!
    o POS tagging - Stanford toolkit, OpenNLP\
      - AutoBot can recognize punctuations like humans do using NLTK library, this helps AutoBot to talk like humans almost.\
      - Implemented "words = nltk.word_tokenize(sentance)" to all words declarations to use nltk library. \
      - Sample Output: \
        With POS\
        (AutoBot)   Welcome to Autobot, can I assist you today?\
        (Input)     Sure!\
        (AutoBot)   "I love the enthusiasm, let's get you behind the wheel of a new car!"\
       
