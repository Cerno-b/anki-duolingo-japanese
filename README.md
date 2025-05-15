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
have access to ChatGPT, but you don't strictly need it.

### Step 1
Open your Duolingo website (not the app) and navigate to `PRACTICE -> Words`. 
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
your python setup. This script fixes the weird line breaks for the import. Note that this
script will write back to the same file, so back up any manual changes to that file
before running the script.
### Step 4
The next step is a bit of manual work: You have to get the correct kana 
transcriptions for any kanji you see in the file. So open up the `duolingo.txt` 
file in a text editor and spot all the lines that contain kanji. You can either 
do the transcriptions manually, or use ChatGPT, which is what I do. Here 
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

It's advisable to copy the whole line as it might help ChatGPT infer nuances, e.g. 
十分 can be *10 minutes* (じゅっぷん) or *enough* (じゅうぶん) which cannot be transcribed uniquely 
from the kanji alone

If you don't trust ChatGPT, you can instead take the transcription directly from the Duolingo website.
Go to `CHARACTERS -> KANJI` and copy the hiragana/katakana transcriptions for each Kanji. 
Don't forget to separate the transcription with a semicolon in the text file as in the ChatGpt example output above. 
Doing it this way also helps you to not miss any kanji and you have the new kanji neatly organised by
unit.

### Step 5	
Now you can take these lines and replace them in your `duolingo.txt` file. You 
may also want to make sure that ChatGPT got this right. Double check that the 
lines with kanji now have an extra semicolon with the kana transcription at the end. The 
lines that already only contain kana can stay as they are.
### Step 6
Run the second script `02_prep_import.py`. This will create a new 
`duolingo_import.txt` file. 
### Step 7
Open Anki on your computer
### Step 8
Sync and backup your current deck, to be safe if anything goes wrong.
### Step 9
Import the new vocabulary from your `duolingo_import.txt` as described above 
in section [Importing the deck](#importing-the-deck). 
### Step 10
Sync again to update the deck on all your devices.
### Step 11 (optional)
If you want to archive your import files in order to keep track of what you added
when and to check later which new vocabulary you have to add to prevent gaps or duplicates,
you can run `03_archive.py`. This will move your `duolingo.txt` and `duolingo_import.txt`
to the archive directory with the current date. It will also create a new empty `duolingo.txt`
file so you're ready for your next import in the future.
