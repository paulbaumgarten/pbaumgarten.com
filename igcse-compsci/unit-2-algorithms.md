# Unit 2 Algorithms

This unit aligns to the syllabus and textbook as follows:

* Syllabus: 2.1.1 Problem solving & design; 2.1.2 Pseudocode & flowcharts
* Textbook: Chapter 9: Problem solving and design; Chapter 10: Pseudo code and flowcharts

## 01: Computational thinking

> Computational thinking is strictly not in the iGCSE syllabus. However, it is actually very helpful for beginner programmers to consider the thinking skills assocated with computational problem solving. 

Computational thinking is what allows us to go from the quick and simple little programs we've been writing, to solving more meaningful problems.

There are commonly four thinking skills associated with this.

1. Decomposition - Can I divide this into sub-problems?
2. Pattern recognition - Can I find repeating patterns?
3. Abstraction - Can generalise this to make an overall rule?
4. Algorithm design - Can I document the programming steps for any of this?

For a walk through on using these thinking skills, make use of:

* My [introductory video on Computational thinking](https://youtu.be/2bvt6PCBVPo)
* My [introductory slides on Computational thinking](unit-2-computational-thinking-slides.pdf)

Some other general advice I would give to new programmers is:

* Just start - A blank screen can be overwhelming
* Don’t start at the start - Programs are not novels, you read and write a program by jumping around
* Start with something you know - Build the user interface and work back from there
* Don’t be afraid to Google - Prioritise results from forums such as stackoverflow
* Test & print a lot

Once you've digested the slides or video, have a go at a couple of problems of your own:

* Problem 1: Create an age calculator. Prompt the user for (1) their birthdate and (2) the current date, calculate their age, checking whether they have had their birthday yet or not.

* Problem 2: Create a money change calculator. Given a set of possible coins available to the shop attendant, and an amount of change they must provide the customer, calculate how many of each coin they should give the customer. For example if a country has 1cent, 5cent, 10cent, & 50cent coins and you need to provide 67cents of change, the clerk would give 1x50cent, 1x10cent, 1x5cent, and 2x1cent coins. 

* Additional problems: Try one of my general [programming problems](programming-problems.md).

## 02: Systems & algorithms

Introducing
Top-down design & structure diagrams
What is an algorithm
Documenting algorthms

## 03: Testing algorithms

As our programs become more complicated, having a proper testing regieme becomes increasingly important. It is no longer good enough to run our program with a "typical" value, get the expected result and consider it "working".

A well designed testing regieme will consider four different types of input data:

* Normal data: This is the data you have intended for your program to encounter.
* Erroneous & abnormal data: Data your program should not receive as an input.
* Extreme data: The extreme values of what is possible to receive as an input.
* Boundary data: Data on the edge of what your program may receive as inputs.

Example: An alarm app that requires you to enter a time for the alarm in 24 hour format.

| ----------- | ----------- |
| Normal data | 06:30, 07:00, 16:00 |
| Erroneous data | 09:00am, Seven, -17:00, 4 o'clock, 25:00, 8:75, 5pm |
| Extreme data | 00:00, 23:59 |
| Boundary data | 00:00, 23:59, 24:00, 05:60 |

(Of course, you could modify the app's requirements so that it can correctly interpret some of the "erroneous data" so it can become "normal data")

The question then becomes, how do you want your app to respond to the various types of data? And does it respond in the manner you intend? This is what is required of a proper testing regieme.

It may also be necessary to state some assumptions when devising your test data if the problem scenario is not sufficiently clear.

Practice creating the four types of test data for the following problems:

* Activity 9.5, 9.6, 9.7, 9.8 (Textbook pages 119, 120).
* A currency conversion app that will convert HKD to USD.
* A date reminder app that will accept dates in the style of dd/mm/yyyy.
* A two factor authentication app that requires someone to enter their Hong Kong mobile phone number so an SMS message can be sent. (hint: check [wikipedia](https://en.wikipedia.org/wiki/Telephone_numbers_in_Hong_Kong) for the rules of what constitutes valid mobile phone numbers in HK) 

## 04: Validation checks

* Range checks
* Length checks
* Type checks
* Character checks
* Format checks
* Presence checks

## 05: Validation checks (2)

* Check digits

## 06: Validation checks (3)

Activity 9.9 through 9.13 (textbook pages 123-124)

## 07: Verification checks

* Double entry
* Screen/visual check
* Parity check
* Checksum

## 08: Trace tables

A tool to manually test your algorithm.

Activity 9.14 through 9.17 (textbook 127-129)

## 09: Trace tables (2)

## 10: Reading pseudo code

What is pseudo code?

"Pseudo" is defined as "not actually but having the appearance of; pretended; false or spurious; sham; almost, approaching, or trying to be." ([reference](https://www.dictionary.com/browse/pseudo)).

So pseudo-code is pretend-code. It is not a geunine, real programming language. The intent behind the idea is that it is a generic, language agnostic tool that can be used to communicate algorithms between programmers regardless of what language they may be specialists in. That is, something that can be read and understood by all programmers because it is so clear and simple.

The following is an example of pseudo-code you will see in this course. You should be able to read it, understand what it is conveying and convert it into your own programming language without difficulty.

```txt
PRINT "I can count! What number should I count up to?"
INPUT Target
N ← 1
WHILE N < Target
   PRINT N
   N ← N + 1
PRINT "Told you I could do it!"
```

A note about pseudo code: What it is supposed to be verses what it is in the iGCSE course...

    While the idea of pseudo-code is supposed to be a language-agnostic, generic undefined tool for documenting algorithms, that is not compatible with the notion of exam marking schemes. As a result, pseudo code for our course is actually quite perscriptively defined. While you don't have to be syntatically perfect, you are expected to write pseudocode that is very clear and to the same level of detail as defined within the syllabus. In otherwords, while not a real programming language, you do need to learn it and practice it for it will appear in your exams.

Syntax of pseudo code for the iGCSE course:

* Chapter 10, page 134-139 of the textbook.

## 11: Tracing pseudo code

## 12: Writing pseudo code

## 13: Flowchart syntax

Just like pseudo-code, flowcharts are intended to be a language-agnostic way of communicating algorithms from one programmer to another. Also just like pseudo-code, the course syllabus has mandated a set of symbols for you to learn.

Syntax of flowcharts for the iGCSE course:

* Chapter 10, page 142 of the textbook.

## 14: Ethical considerations

## 15,16,17: Unit review exercises

* Chapter 9 review questions: Page 132-133.
* Chapter 10 review questions: Page 144-145.
* [70 pseudocode practice questions](distribute/pseudocode-70-questions.pdf) (I have the solutions for these for you to self-check)

Let me know once you have completed those. I am happy to create additional review questions as needed.

## 18: Unit test

