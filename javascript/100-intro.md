# 1 - Introduction to Javascript

This book has been written as a supplemental resource to the classroom based lessons I teach, or to accompany my introduction to programming with Javascript videos on Youtube. It contains all the demonstrated programming on the videos, summaries of the explanations given in those videos, and a set of practice exercises for students to complete for each skill. This book has not been written to be used as a stand alone resoure for learning programming without a teacher or tutor.  The written explainations have been deliberately kept short, intended to be more of a "reminder/prompt" of an idea rather than a full introduction to an idea.

As a teacher of secondary school students, and the fact that I wrote this book in the process of preparing resources to use for my own lessons, the book is largely pitched at the 12-17 age range.

I have videos on my YouTube channel that parallel many of the concepts and exercises in this book. I encourage you to check them out to help you along your programming adventures.  Additionally any files you may need to complete exercises, any corrections to errors that went to print, along with guides to other useful Python tricks that may not have made it into the book, can all be found at my website.

* [https://pbaumgarten.com/python](https://pbaumgarten.com/python)
* [https://youtube.com/pbaumgarten](https://youtube.com/pbaumgarten)

## Getting Javascript

One easy thing about Javascript is you already have it on your computer without perhaps realising it. It is built into your favourite web browser.

That said, to actually write Javascript it would be helpful to have an editor that is a little more intelligent than, say, Notepad. There are several very good free text editors designed for programmers and I recommend you downloading and installing one of these (if you are a student of mine, you likely already have a suitable editor on your school computer):

* [Visual Studio Code @ https://code.visualstudio.com/](https://code.visualstudio.com/)
* [Atom @ https://atom.io/](https://atom.io/)
* [Brackets @ http://brackets.io/](http://brackets.io/)

The other thing you will want is the development tools for your web browser. I will focus on the Chrome web browser in this book, but Firefox has equally good tools you can use as well. To access the Chrome DevTools, simply right click anywhere on a website and choose *Inspect*.

If you are stuck with getting an editor and/or the Chrome development tools installed and working, watch the first video in my Learning Javascript series.

Enough jibber jabber... time to get underway!

Have fun programming!

Mr Baumgarten.

---

## Let's get started!

Given Javascript runs in the web browser, that means it works very closely with HTML and CSS which are a couple of other web based languages you will need to gain some familiarity with. The fact you need to gain familarily with more than one language at once is probably the biggest downside of using Javascript as your first programming language. To that end, I'm going to be keeping the HTML/CSS fairly simple at the start, section 1 is "just" Javacript. We do, however, need a HTML page that contains enough information to tell the browser to execute our Javascript, so I'll just give it to you here. Type it into your text editor, and then save and forget for now. I'll explain the HTML when we get to part 2.

Save as `firstprogram.html`:

```html
<html>
    <body>
    </body>
    <script type="application/javascript">
    "use strict";

    alert("Hello world!");
    </script>
</html>
```

Once you've saved in your text editor, locate the file in Windows or Mac Finder and double click to open it in your web browser. If you get a pop-up like the below then congratulations, you have successfully got your first program up and running!

![Screenshoot](img/js-helloworld.png)

From here on, you will need to copy and paste (or re-type) all except the `alert("Hello world!");` and re-use it for any new programs we make. The line starting with the `alert` is the only actual Javascript programming code we have provided, the rest is the template content you "just need".  As previously said, don't worry too much about it now, the HTML will be explained in part 2.

---