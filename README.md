# anki-duolingo-japanese

Anki deck builder for the Duolingo Japanese Course, also contains ready-made 
decks to import into Anki.

# Concept

This is a personal project to transfer my current Duolingo Japanese vocabulary 
workload to Anki, since Duolingo does not have a good Spaced Repetition (SRS) 
system for learning vocabulary.

If you want to use the decks that I built, be my guest, but note that they do 
not contain the full Duolingo course, just the parts up to the point where I 
currently am. Also keep in mind that Duolingo may restructure courses and 
shuffle around or change vocabulary sets.

This project has two parts

1. The Anki decks (up to my current level)
2. Python code to extract vocabulary from your personal Duolingo account.

## The Anki deck

You can find the deck in the `by_section` folder where I am updating the decks 
as I go along with the course. There is a `history` folder but that is just for 
me to keep track of the changes I extract from my own Duolingo page.

The Anki deck has a format that works for me, but your mileage may vary. If you 
have suggestions for improvement, let me know, but so far I find this fairly 
workable. 

I decided to create two templates for each entry (Front and Back), because I 
would like to have both directions to be slightly different from each other.

The Front template is laid out like this:

**front face**

	newspaper

**back face**

	新聞
	しんぶん

The Back template looks like this:

**front face**
	
	新聞

**back face**

	newspaper
	しんぶん

So you see that Front template has the English term on the front face and 
kanji/kana as the back face.

The Back template has the kanji as the front face, and English/kana as the 
back face. 

This way I get no unwanted kana hints for the kanji I am learning, but the 
card will still show how the kanji is pronounced when I read the back face.

## Importing the deck

When importing the deck, use the following Anki settings:

* Field separator: Semicolon
* Allow HTML: YES, otherwise the line breaks will not work
* Note type: basic
* Deck: Whatever deck you want to add this to
* Existing notes: I prefer duplicate here, because some imports may collide with existing cards, like に and ふたつ for the number two
* Match scope: Note Type
* Field Mapping: leave as is (japanese example, english example, "front")

## Creating your own deck

If you want to build your own deck as you go along with your Duolingo course, 
you can follow these steps to export your current vocabulary state.
You need any recent python version to run the code and I would suggest you 
have access to ChatGPT.

### Step 1
Open your Duolingo website (not the app) and navigate to "PRACTICE" -> "Words". 
This is your word list. Click on "load more" at the bottom to reveal as much of 
the vocabulary as you want to export.
### Step 2 
Copy/paste the table (and just the table) into the `duolingo.txt` file inside 
the repo's main directory. Double check that it only contains the table, and
do not change anything besides what you pasted (leave the weird line breaks
as they are)
### Step 3
Run the first python file `01_fix_lines.py` by calling `python 01_fix_lines.py` 
from the command line. Double-clicking the script might also work, depending on 
your setup. This script fixes weird line breaks for the import. Note that this
script will write back to the same file, so avoid doing any manual changes
before running the script.
### Step 4
The next step is a bit of manual work: You have to get the correct kana 
transcriptions for any kanji you see in the file. So open up the `duolingo.txt` 
file in a text editor and spot all the lines that contain kanji. You can either 
try to do the transcriptions yourself, or use ChatGPT, which is what I do. Here 
is the prompt I use:


	Transcribe the following to kana please and add the result to the end separated by semicolon:

	will have, drink, having;飲みます
	check emails;メールを読みます
	four o'clock;四時
	eat, am going to eat, will eat;食べます

This should result in something like this:
	
	will have, drink, having;飲みます;のみます
	check emails;メールを読みます;めーるをよみます
	four o'clock;四時;よじ
	eat, am going to eat, will eat;食べます;たべます

### Step 5	
Now you can take these lines and replace them in your `duolingo.txt` file. You 
may also want to make sure that ChatGPT got this right. Double check that the 
lines with kanji now have an extra semicolon with the kana transcription. The 
lines that already only contain kana can stay as they are.
### Step 6
Run the second script `02_prep_import.py`. This will create a new 
`duolingo_import.txt` file. 
### Step 7
I would advise you to keep the `duolingo.txt` and `duolingo_import.txt` files 
(I save mine in my `history` folder), so you will know what block of vocabulary 
you need to copy next as you advance your Duolingo journey.
### Step 8
Open Anki on your computer
### Step 9
Sync and backup your current deck, to be safe if anything goes wrong.
### Step 10
Import the new vocabulary from your `duolingo_import.txt` as described above 
in section [Importing the deck](#importing-the-deck). 
### Step 11
Sync again to update the deck on all your devices.