# Hangman game for Pepper robot
![karelInAction](https://github.com/Fapannen/Pepper-Akinator/blob/master/Pepper-Akinator/img/KarelFinal.jpg)

Play a game where robot thinks of a word and your task is to guess it letter by letter. You can also try to guess the whole word.

Pepper robot plays game with user. Start the game by telling one of the triggering words to robot.
Currently the triggering words are "Zahrajem si", "Hrajem" and "Let's play". If you want to stop the game, say "konec" when robot expects a letter.
Only Czech language is currently supported ( Both words and interaction )

## Demo
Demo run can be found [here](https://youtu.be/dvelpUd6uBg)

## Acknowledgements
Project contains code copied from [Salisu Wada github](https://github.com/salisuwy/Pepper-Robot-Displays-User-Input) - Displaying the user progress on tablet

## Description of the project and guidelines how to modify it
Project is designed to be easily-modified to your own set of words and language.

The logical structure of the project looks like this
![StructureOfTheProject](https://github.com/Fapannen/Pepper-Akinator/blob/master/Pepper-Akinator/img/structure.png)


### StartGame dialog
```
concept:(sibenice) ["zahrajem si" "šibenice" "hrajem"]
concept:(agree)    ["ano" "jasně" "samozřejmě" "jojo" "jistě" "jo"]
concept:(disagree) ["Ne" "Asi ne" "Teď ne"]

u:(~sibenice) Chceš si zahrát šibenici?
    u1:(~agree) Jdeme hrát $start=1
    u1:(~disagree) Škoda. Třeba příště $end=1
```

- "sibenice" concept specifies the triggering set of words to run the application. (You also need to modify the trigger values in project properties)
- "agree" set of words when user agrees to play the game
- "disagree" set of words when user disagrees to play the game


### InitializeGame python script
```
def onInput_onStart(self, start):
        words = ['univerzita', 'rododendron', 'koriandr', 'petrzelka', 'rozmaryn']
        chosen = words[random.randint(0, len(words) -1)]
        self.logger.info("Sending guessinWord to script")
        proxy = ALProxy("ALDialog")
        proxy.setConcept("guessWord","czc", [chosen])
        self.guessingWord(chosen)
```



```
 words = ['univerzita', 'rododendron', 'koriandr', 'petrzelka', 'rozmaryn']
```
- Specifies the words you want the robot to choose from. Add your own :) 


```
proxy.setConcept("guessWord","czc", [chosen])
```
- This command sets dynamic rule for dialog recognition. This allows robot to recognize the words that is being guessed, meaning the user can try to guess the whole word. Note that you need to change "czc" to your language in case you are modyfing the dialog


```
self.guessingWord(chosen)
```
Activate the output of the box with the word that has been chosen



### getUserInput dialog
Specifies words / letters that robot can recognize

```
dynamic:guessWord
concept:(exit)[konec]

concept:(a) [a á áčko]
concept:(b) [b bé béčko]
concept:(c) [c cé céčko]
```



```
dynamic:guessWord
```
This dynamic rule enables user to guess the whole word


```
concept:(exit)[konec]
```
Specifies the set of words used to exit the application.


```
concept:(a) [a á áčko]
```
Specify your language's alphabet and all possible pronunciations of the letter.


### processWord python script
Contains the main logic of the game. Only thing you might want to modify is the number of fails allowed. (line 220)


### alreadyGuessed / letterInWord / letterNotInWord / letterNotRecognized / wonGame / lostGame
Robot informs user what happened with his input


### showUserProgress python script
No need to modify anything here.

- Most of this part consists of [Salisu Wada's project](https://github.com/salisuwy/Pepper-Robot-Displays-User-Input)
- Displays user progress on tablet




![karel](https://github.com/Fapannen/Pepper-Akinator/blob/master/Pepper-Akinator/img/karelupload.jpg)
