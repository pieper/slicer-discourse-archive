# Accessing Slicer's Transform Module through terminal

**Topic ID**: 11301
**Date**: 2020-04-26
**URL**: https://discourse.slicer.org/t/accessing-slicers-transform-module-through-terminal/11301

---

## Post #1 by @MachadoL (2020-04-26 00:41 UTC)

<p>Hey Guys,  I am trying to do a bash script to run several times the routine <code>converter</code> from Slicer <code>Transforms</code> module.<br>
But no clue so far. I google it for a while.</p>
<p>Any help is appreciated.<br>
Thanks.</p>

---

## Post #2 by @lassoan (2020-04-26 01:25 UTC)

<p>See how to run scripts in Slicer from the command-line: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Launching_Slicer">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Launching_Slicer</a></p>
<p>Nowadays I would not implement any batch processing in bash, as you can write much more robust, maintainable, and platform-independent scripts in Python. If you already installed Slicer then you have Python already, while bash (and all the essential linux command-line tools) are not generally available on Windows. Also, if you implement something in Python, you can easily move it into a proper module inside Slicer, with a GUI, or copy content from modules into your processing script.</p>

---

## Post #3 by @gcsharp (2020-04-26 01:34 UTC)

<p>Hey Leo my friend.  In addition to Andras’s sage guidance you need to give example code.  Is this within Slicer or outside scripting?  Best, Greg</p>

---

## Post #4 by @MachadoL (2020-04-26 01:47 UTC)

<p>Alright. You got me… I’ll try to run as a python script and give you feedback.</p>

---

## Post #5 by @MachadoL (2020-04-26 01:53 UTC)

<p>You’re right professor… I was trying to do through bash… But didn’t find solution… I’ll try python and see if I can make it work.<br>
Best,</p>

---
