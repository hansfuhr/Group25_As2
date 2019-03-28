<h1>Hans Fuhrmann-Assignment 3</h1>
<h1>Project name: AutoBot 2.0</h1>
<h1>Github repository: </h1>
https://github.com/hansfuhr/Group25_As2/tree/HansFuhr_As3
<br>For the graph showing the different features developed on a separate branch go here:
https://github.com/hansfuhr/Group25_As2/network
<h2>About the project</h2>
This project is called Autobot and is essentially an AI that assists a user in picking a car, truck, SUV, minivan, or motorbike. This is done by asking the user a series of questions which helps Autobot predict what the user will prefer. Autobot is mainly for users who may have limited knowledge of what type of vehicle they are interested in.

<h2>Navagation for software</h2>
There are 4 separate python files, each is the same program but some features needed to be separated. 
- VehicleList initiates a database and adds all vehicles available. This is the original autobot program with all
features that simply improved the original program.
- VehicleListGUI is the same as VehicleList however it includes a very basic GUI
- VehicleListClient & VehicleListServer are also the same as VehicleList, however it has the functionality to
have a client and a server via sockets. Simply run the server then the client, and the program will be running through sockets.

<h2>Code organization</h2>
In VehicleList.py the codes are organized into 4 parts separated by comments.
1. Database of cars
2. Text input for text matching check
3. Function for text finding 
4. Methods for compiling 

<h2>Features programmed for Assignment 3</h2>
1. Make a simple GUI so that the user is typing into a nicer 
interface and can view a recent history of the conversation. <br>
-This improved the look of the program, as console output is not as nice as a GUI
<br>

2. Add an extra topic to your agent's repertoire. 
Ensure this topic has similarities with the original topic.<br>
-Autobot now offers motorbikes and minivans in addition to the original cars, trucks, and suvs. This allows the program to be more functional for a wider variety of users.
<br>Snippet of conversation that demonstrates this feature:<br><br>
Autobot: What are some important aspects you want in 
your vehicle?<br>
User: type<br>
Autobot: Are you a car, truck, suv, minivan, or motorbike kind of person?
Car, truck, SUV, motorbike, or van:<br>
User: motorbike<br>
Autobot: I have found 10 vehicles that match your criteria!

3. Add a feature that enables your agent to 
give at least 5 different reasonable responses when the user enters something outside the two topics.<br>
-When the user says they do not wish to talk about vehicles, autobot now can offer some knowledge on various non-car-related topics
This helps to be more open to users that decide they don't want a car.<br>Snippet of conversation that demonstrates this feature:<br><br>
Autobot: I'm sorry, do you want to talk about something else?<br>
User: Yes<br>
Autobot: Do you want to know the price of a McDonald's Big Mac?<br>
User: Sure<br>
Autobot: A Big Mac is $3.99!
4. Add a feature that enables your agent to handle spelling 
mistakes of the words that your agent is supposed to recognize.<br>
-When the user enters a response, if no words match what Autobot is expecting, a spellcheck function is initiated.
This function gives the user the opportunity to re-enter a misspelled word. This helps with conversation flow.
<br>Snippet of conversation that demonstrates this feature:<br><br>
Autobot: Hello, my name is Autobot, can I help you find a vehicle today?<br>
User: Yas pleez<br>
Autobot: I'm sorry, you entered an unrecognized word. Maybe it was a spelling mistake.
Would you like to try again?<br>
User: Yes<br>
Autobot: Welcome to Autobot, can I assist you today?<br>
User: Yes please (Now program continues as usual)<br>

5. Language toolkit: Sentiment Analysis<br>
-Autobot can now detect the sentiment of the user depending on the types of words they enter, if they are positive autobot gives more positive responses, if they are neutral autobot gives neutral responses, and if the user is negative autobot attempts to cheer them up. 
This helps to make Autobot smarter in it's responses. 
<br>Snippet of conversation that demonstrates this feature:<br><br>
Happy sentiment: <br>
Autobot: How is your day going today? <br>
User: Really good! Thanks<br>
Autobot: That's good to hear :)<br><br>
Not so happy sentiment:<br>
Autobot: How is your day going today? <br>
User: Bad, I feel sick<br>
Autobot: Aw :( well maybe a car will cheer you up!<br>

6. Language toolkit: POS tagging<br>
-Autobot can now detect punctuation, as POS tagging splits the words even when puncuation is entered. This immensely helps with conversation flow
<br>Snippet of conversation that demonstrates this feature:<br><br>
Without POS tagging: <br>
Autobot: Can I help you find a car today? <br>
User: Yes!<br>
Autobot: Unrecognized response (Error)<br><br>
With POS tagging:<br>
Autobot: Can I help you find a car today? <br>
User: Yes!<br>
Autobot: Great! Let's start with a few questions (Program continues)<br>
7. Conversation with another agent (built by a student in this class) via sockets<br>
-The sockets program runs the same as the original program, but now it is running through a client-server input-output instead of
the entire program just running in one console. This has many applications with autobot, as you could have multiple clients and have
another student's chatbot act as the client and talk to autobot via sockets!<br>
<h2>Based on your system, include a list of at least 5 features that you can extract from your code or design that can be shared with others as an API.</h2>
One - The database of cars that was carefully crafted can be reused for many other types of car-related programs.<br>
Two - The spell checking function could be used with any program that requires input without mistakes<br>
Three - The type of GUI I created could easily be used as a template to create other GUI applications<br>
Four - My sentiment analysis functions could easily be implemented in another program to detect sentiment of any given sentance<br>
Five - Lastly, my runagain() function could be used in any program that has a recurring theme, simply replace the parts that reference autobot and apply them to your program, and the function will work!<br>


