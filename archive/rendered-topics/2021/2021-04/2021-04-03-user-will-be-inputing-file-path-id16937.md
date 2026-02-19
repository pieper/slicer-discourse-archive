---
topic_id: 16937
title: "User Will Be Inputing File Path"
date: 2021-04-03
url: https://discourse.slicer.org/t/16937
---

# User will be inputing file path

**Topic ID**: 16937
**Date**: 2021-04-03
**URL**: https://discourse.slicer.org/t/user-will-be-inputing-file-path/16937

---

## Post #1 by @abatpool (2021-04-03 08:01 UTC)

<p>I require the user to input path of file, from which i will be reading marker coordinate. So as raw_input function is unsupported in python, is there any other function or way to achieve this.</p>
<p>user_input = raw_input("Enter the path of your file: ")<br>
filepath = str(user_input)</p>
<p>The above code incurs errors at python interactor, so let me know ,the way around it.<br>
Thanks in advance!!!</p>

---

## Post #2 by @Andinet_Enquobahrie (2021-04-03 11:37 UTC)

<p><a class="mention" href="/u/abatpool">@abatpool</a></p>
<p>You can use the replacement  <em>input</em> function which exists in Python 3</p>
<pre><code class="lang-auto">filepath = input("Enter the path of your file: ")
</code></pre>
<p>The <em>input</em> built-in function returns a string type so you don’t need additional casting.</p>
<p>Best,<br>
Andinet</p>

---

## Post #3 by @abatpool (2021-04-06 06:06 UTC)

<p>oh yes. thank you <a class="mention" href="/u/andinet_enquobahrie">@Andinet_Enquobahrie</a> . Have a great day ahead!!</p>

---

## Post #4 by @Guglielmo_Baccani (2021-05-04 08:26 UTC)

<p>Dear slicers, thank you for this post.<br>
I have a similar problem: I want the user to specify some inputs from the python interactor. You can copy the following code into the python interactor to figure out what my problem is:</p>
<pre><code class="lang-auto">while(True):
  a = input("Insert a character or press 'q' to quit: ")
  print('Your character: ', a)
  if a == 'q':
    break</code></pre>
<p>Before writing the second input, I have to press the down key to avoid messing with the input and output lines.<br>
It is possible to avoid this and make the input and output lines follow each other neatly?</p>

---

## Post #5 by @lassoan (2021-05-04 16:55 UTC)

<p>Do you mean that within Slicer application, you would want user to type input in the Python interactor instead of using graphical user interface (in your module GUI, in a popup window, etc.)?</p>

---

## Post #6 by @Guglielmo_Baccani (2021-05-05 09:56 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a> thank you for your activity in this forum: your answers have been helpful to me in several occasions.<br>
My goal is to create a debugging mode for my module so that I can pause code execution at certain points to observe partial results. The solution I found is to wait for a user input in the python interactor which would then allow the execution to proceed or pause.<br>
Would you suggest putting “continue” and “stop” buttons in the GUI? Where can I find examples?</p>

---

## Post #7 by @lassoan (2021-05-05 14:54 UTC)

<p>For interactive debugging, you can attach a debugger and there you can do anything. Inspect variables, change variable values, run any commands, etc. See step-by-step instructions <a href="https://github.com/SlicerRt/SlicerDebuggingTools#python-debugger">here</a>.</p>

---
