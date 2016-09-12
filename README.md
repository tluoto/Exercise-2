# Exercise-2
The exercise for this week is meant to help you better understand data types and lists in Python, and practice saving files to GitHub.
Below you have a series of "problems" in which you will be asked to either download and modify, or create new script files.
After making you changes, you will need to upload them to GitHub.
The answers to the questions in this week's exercise should be given by modifying the end of this document in the [section titled Answers](#answers).

## Problem 1 - Making changes to a file in GitHub
Your first task for this week is to make some modifications to the broken script [`cattreats.py`](cattreats.py) that is included in this week's exercise.
The script should allow users to find a cat's favorite treat by setting the `SelectedCat` variable.
Fix this script so that it works as expected, and don't worry about the case of a user entering a cat name that is not on the list.
**There are 3 major code problems you must fix to get the code working properly**.
Commit your changes after each fix.

## Problem 2 - Creating and uploading a script to GitHub
Create a script called `days_in_month.py` that allows users to select a month and have the number of days in that month printed to the screen.
For example, if the user sets month to "February", the script will display

```
The number of days in February is 28
```
You script should

- Display the number of days in a selected month, set by defining the variable `SelectedMonth` near the top of the script.
- Work for all 12 months in a normal year. You can assume it is not a [leap year](https://en.wikipedia.org/wiki/Leap_year).
- Use the basic script format described in [this week's lesson](https://github.com/Python-for-geo-people/Diving-into-Python/blob/master/Lesson/writing-scripts.md#writing-our-scripts-the-right-way).
- Be uploaded to your GitHub repository for this week's lesson with the name `days_in_month.py`.

**Hint**: For this script you will likely need two lists and to use the `.index()` method.
These were covered in [this week's lesson](https://github.com/Python-for-geo-people/Diving-into-Python/blob/master/Lesson/python-basic-elements1.md#lists-and-indices).

## Problem 3 - Answering questions using Markdown
The last task in this week's exercise is to make some changes to this `README.md` file to provide answers to the following questions.

1. Under the heading for Problem 1 (`## Problem 1`), list the changes you needed to make to the code (in regular English, not Python code) to get it working.
You are welcome to use a numbered list if you like.
You can read about how to format numbered lists on the GitHub page about [GitHub-flavored Markdown](https://help.github.com/articles/basic-writing-and-formatting-syntax/).
2. Add a heading for Problem 2 and beneath it list some of the challenges you faced in creating your own Python script from scratch.
What parts of the code were most difficult to create?
What things were you able to take from other resources in this week's lesson?
Any other comments about the difficulties in creating your own script?
3. Add a heading for Problem 3 and beneath it give your comments about this week's lesson.

    - What did you like?
    - What did you dislike?
    - What would you change?
4. Lastly, just for fun, add an image of an animal that you like along with a short caption giving its name and anything special you might like to add.
You can add an image by linking to a website, or by uploading an image to your GitHub repository and linking to that.
Since we've spoken briefly about software licencing, we suggest that you search for images in a repository that includes licencing information such as [Wikimedia Commons](https://commons.wikimedia.org/wiki/Main_Page) or [Pixabay](https://pixabay.com/).
You are, of course, also welcome to upload your own animal images.
You can add under the Problem 3 heading.

# Answers
## Problem 1
Even though not quite a error in itself (because user could give wrong inputs), I had to change value of variable SelectedCat from 7 anything between 0-6 or (-7) - (-1), because indexes in list start from 0 and so there is no cats in list of 7 cats with index 7.

Then I noticed there was only 6 treats for 7 cats, so I decided to add treat 'Small dogs' for cat 'Snowball II' 

Then code had new variable defining index of wanted cat, but because already input was created to use index instead of name, this row only gave error message, because Cats.index(SelectedCat) would return index of item SelectedCat in list Cats. If input SelectedCat would have been given as name of cat instead of its index, this row would have been needed, but now I just removed it.

And because SelectedCat was index of wanted cat, not its name, last row of code had to be changed so that name and treat of wanted cat was given as items in corresponding lists with wanted index, so Cats[SelectedCat] and Treats[SelectedCat]

## Problem 2
There was no real challenges here because this exercise was pretty much copy of exercise 1 with different variables. Hardest part was probably finding how to upload file to github.

This exercise was about lists and especially .index() from this weeks lessons.

## Problem 3
I did like the fact that first real exercises were simple and more concentrated on learning how to use github as working environment. Maybe one thing that needs little more explanations is problem 1, because at least I had some difficulties in finding out how to commit new versions of script after each fix.

![Text shown if image does not load](Images/thornydevil.JPG)<br/>
*Figure 1: A Thorny devil (just because these little fellows are just so cute)*


