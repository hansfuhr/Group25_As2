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

<h2>1. (2 points) Extra Topic </h2>

- added motorcycles to database<br/><br/>
sample output:<br/>
  (AutoBot)   Are you a car, truck, suv, or motorcycle kind of person? Car, truck, SUV, or motorcycle:<br/>
  (Input)     motorcycle<br/>
  (AutoBot)   I have found 9 vehicles that match your criteria!<br/>
  (AutoBot)   Here is a/an motorcycle.<br/>
              It is a 2019 Kawasaki Ninja ZX-6R, it seats 2<br/>
              and gets 35 miles to the gallon.<br/>
              You can walk away with this motorcycle for $11999<br/>
              Are you happy with this vehicle?<br/>
  (Input)     Yes<br/>

<h2>2. (3 points): Out of topic conversations.</h2>
- added reseponses to answers that are not related to the topic (selecting a vehicle)<br/><br/>
sample output:<br/>
  (AutoBot)   We can't recognize what you mean by that :(<br/>
              Would you like to try again? (y/n)<br/>
  (Input)     y<br/>
  (AutoBot)   Do you want to know about computers? (y/n)<br/>
  (Input)     y<br/>
  (AutoBot)   Apple's macbook is so expensive<br/>
              Did you know if you fully upgrade macbook pro 15 with touchbar<br/>
              You have to pay like 8400 dollars<br/>
              WooooooW<br/>
              Have a nice day<br/>
<h2>3. (5 points) Spelling checker</h2>
    o If user inputs spelling mistakes or random inputs in greetings, AutoBot asks whether it is a spelling mistake 
      and if it is, allow user to correct it and if not we ask user if they want to hear something else other than selecting a vehicle<br/><br/>
      - Sample Output:<br/>
        (AutoBot)   Welcome to Autobot, can I assist you today?<br/>
        (Input)     suer<br/>
        (AutoBot)   We can't recognize what you mean by that :(<br/>
        (Input)     "Was it a spelling error? Would you like to try again? (y/n)"<br/>
        (Input)     y<br/>
        (AutoBot)   Welcome to Autobot, can I assist you today?<br/>
        (Input)     sure<br/>
<h2>4. Language toolkits to improve conversation's flow:</h2>
<h3>(10 points) Synonym recognition - WordNet (you'll need a Java API to it)</h3>
    - AutoBot can generate synonmy of word 'happy' if user feels like not talking about anything to brighten up his/her day!<br/><br/>
    - Sample Output:<br/>
      (AutoBot)   Hello, my name is Autobot, can I help you find a vehicle today?<br/>
                  We currently have 124 vehicles in our inventory.<br/>
      (Input)     wefqef<br/>
      (AutoBot)   We can't recognize what you mean by that :(<br/>
                  Was it a spelling error? Would you like to try again? (y/n)<br/>
      (Input)     n<br/>
      (AutoBot)   Okay, maybe you want to know about computers instead! (y/n)<br/>
      (Input)     n<br/>
      (AutoBot)   Alright than! Maybe I will tell you the synonyms of 'happy' to brighten up your day<br/>
                  {'well-chosen', 'felicitous', 'happy', 'glad'}<br/>
                  Have a nice day<br/>
<h3>(10 points) POS tagging - Stanford toolkit, OpenNLP</h3>
      - AutoBot can recognize punctuations like humans do using NLTK library, this helps AutoBot to talk like humans almost.<br/>
      - Implemented "words = nltk.word_tokenize(sentance)" to all words declarations to use nltk library.<br/><br/>
      - Sample Output:<br/>
        With POS<br/>
        (AutoBot)   Welcome to Autobot, can I assist you today?<br/>
        (Input)     Sure!<br/>
        (AutoBot)   "I love the enthusiasm, let's get you behind the wheel of a new car!"<br/>
        
 <h3>(10 points) Sentimental analysis tools</h3>
      - This was actaully already implemented in our A2 since we had two separate greetings depending on user inputs. If they entered "good", we had greetings_good function that will motivate them even more to suit their needs. On the other hand, if they answered "bad" we had greetings_bad function to cheer them up <br/><br/>
      - Sample Output: <br/> 
      ex1) "Happy" <br/>
      (AutoBot) How is your day going today? <br/>
      (Input) Good!<br/>
      (AutoBot) I love the enthusiasm, let's get you behind the wheel of a new car!<br/><br/>
      ex2) "Sad"<br/>
      (AutoBot) How is your day going today? <br/>
      (Input) bad<br/>
      (AutoBot) That's awful, maybe a car can cheer you up!<br/>

<h2> Documentation (30 points) </h2>
<h3> Readme.md (2 points) - DONE </h3>
<h3> Explanations of each implementations made for A3 in Readme File (5 points) - DONE </h3>
<h3> Provide a Level 0 DFD for your system with description (3 points) </h3>

<h3> Provide a Level 1 DFD for your system with description (5 points) </h3>

<h3> Submission of your GitHub repository.</h3>
- Graph showing different features developed on a separate branch and the commits made in the
repository.<br/><br/>
- https://github.com/hansfuhr/Group25_As2/network<br/>

<h2>Feasible conversation with new features</h2>
Hello, my name is Autobot, can I help you find a vehicle today?<br/>
We currently have 124 vehicles in our inventory.<br/>
hiii hows it going<br/>
We can't recognize what you mean by that :(  <br/>
Was it a spelling error? Would you like to try again? (y/n)<br/>
y<br/>
Good day! My name is Autobot, can we get you rolling in a new vehicle?<br/>
yes<br/>
Before I help you, could you please enter your name?<br/>
Name:Jae<br/>
Pleasure to meet you Jae<br/>
How is your day going?<br/>
good<br/>
That's awesome, let's get into some car details then.<br/>
What are some important aspects you want in your vehicle?<br/>
Currently we support the following features: <br/>
 -Fuel Efficiency <br/>
 -Seating <br/>
 -Price <br/>
 -Type of vehicle<br/>
 -Brand<br/>
price<br/>
What is the maximum you would like to spend?<br/>
Price $:500000<br/>
I have found 122 vehicles that match your criteria!<br/>
Here is a/an truck. <br/>
It is a 2019 Toyota Tundra, it seats 5 <br/>
and gets 14 miles to the gallon. <br/>
You can walk away with this truck for $39625<br/>
Are you happy with this vehicle?<br/>
no<br/>
Here is a/an suv. <br/>
It is a 2019 Lexus RX 450H, it seats 5 <br/>
and gets 31 miles to the gallon. <br/>
You can walk away with this suv for $64500<br/>
Are you happy with this vehicle?<br/>
no<br/>
Here is a/an car. <br/>
It is a 2019 Tesla Model S, it seats 7 <br/>
and gets 999 miles to the gallon. <br/>
You can walk away with this car for $124600<br/>
This vehicle is also electric!<br/>
Are you happy with this vehicle?<br/>
sure<br/>
Would you like to know lease option for this vehicle?<br/>
yes<br/>
In how many years would you like to pay off your Model S?<br/>
5<br/>
The rate would be $958.46 bi-weekly for the next 5 year/years<br/>
Would you like to search for another vehicle?<br/>
no<br/>
My pleasure Jae, have a great day!<br/>

<h3> two short dialogues when my agent is not able to handle the conversation properly </h3>
Good day! My name is Autobot, can we get you rolling in a new vehicle?<br/>
We currently have 124 vehicles in our inventory.<br/>
suuure<br/>
We can't recognize what you mean by that :(  <br/>
Was it a spelling error? Would you like to try again? (y/n)<br/>
n<br/>
Okay, maybe you want to know about coffee instead! (y/n)<br/>
n<br/>
Alright than! Maybe I will tell you the synonyms of 'happy' to brighten up your day!<br/>
{'glad', 'felicitous', 'happy', 'well-chosen'}<br/>
Have a nice day!<br/>

<b>Next one</b><br/><br/>
Good day! My name is Autobot, can we get you rolling in a new vehicle?<br/>
We currently have 124 vehicles in our inventory.<br/>
NOPE<br/>
We can't recognize what you mean by that :(  <br/>
Was it a spelling error? Would you like to try again? (y/n)<br/>
NOPE<br/>
Okay, maybe you want to know about coffee instead! (y/n)<br/>
y<br/>
Do you want to learn about coffee ? (y/n)<br/>
y<br/>
Coffee contains caffeine<br/>
Did you know you can get addicted to caffeine?<br/>
Bet, you didnt' know :) <br/>
Have a nice day!<br/>

<b> Limitations: </b> </br>
  We can see from short conversations above, if user keeps inputing false responses to questions, it can lead to program not being useful and just terminate the system without helping the user. 
  
<h2> 5 features that I can extract to use for other APIs</h2>
<b> Spellchecker can be used with other APIs to check spelling mistakes for their systems.</b><br/>
<b> Synonym recognition can be used in other APIs to make their systems recognize synonms using nltk library. </b><br/>
<b> I can literally use the same chatbot system with other categories by just changing the database.</b><br/>
<b> POS tagging can be used in other programs to let the machine learn the way humans speak (recognize punctuations.) </b><br/>
<b> Easy to add / delete / update databases for my system so we can make a smart chatbot if we want to easily. </b><br/>

