# Multithreading in extension

**Topic ID**: 6941
**Date**: 2019-05-27
**URL**: https://discourse.slicer.org/t/multithreading-in-extension/6941

---

## Post #1 by @n2018 (2019-05-27 18:21 UTC)

<p>Hello! I am trying to implement multithreading in my own extension to 3DSlicer, here is the approximate scheme:<br>
from Logic.run() ThreadA is started<br>
from ThreadA.run ThreadB is started<br>
in ThreadB.run there is infinite loop. I need to add the time.sleep in ThreadB.run function but when I do it the thread doesn’t work in the loop and does only one iteration. And when I close the 3DSlicer program I see in my logs that threadB runs in the loop, seems that slicer main thread blocks another threads… I implemented the same scheme without slicer environment and everything works in the way I want, could you please tell me the reason of described behavior or maybe there is another way to run thread from logic class?</p>

---

## Post #2 by @lassoan (2019-05-29 17:29 UTC)

<p>In general, in Slicer I would recommend <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python" rel="nofollow noopener">doing parallel processing by running a CLI module</a>. Slicer executes CLI modules in the background, taking care of synchronization, safely passing inputs and outputs, etc. For background tasks you can use timers.</p>
<p>This may or may not be ideal for your use case. We would need to know much more about your requirements and constraints do give good advice.</p>

---

## Post #3 by @n2018 (2019-05-30 15:12 UTC)

<p>I will read about CLI but it seems more complicated than my implementation through python threads. About my case: I have several tasks on the server and want to check their status though slicer application and upload the results of them to the slicer environment when they are done, that’s why I need a thread that works in a loop, sends http requests from the queue within timeout and reloads my nodes, for some reason it is blocked after time.sleep  when it is running in slicer environment, in simple python environment everything is ok.</p>

---

## Post #4 by @lassoan (2019-05-30 15:35 UTC)

<p>Since the background tasks do not perform computationally intensive operations in the Slicer process, there is no need to use threads for this but you can use timers instead. The advantage of timers is that your code runs in the main thread, so you can access all data in the scene, without the need of requiring any synchronization mechanisms.</p>

---

## Post #5 by @n2018 (2019-05-30 15:49 UTC)

<p>what do you mean by the word timer? does slicer environment provide special timers? could you please explain how can I run a background process in slicer environment not using threads?<br>
I am reading about running commands from cli modules but don’t understand how I can implement my own cli module through python because all implementations which I’ve found are written on c++</p>

---

## Post #6 by @lassoan (2019-05-30 17:50 UTC)

<p>There are timers available in several libraries that are bundled with Slicer (Qt, VTK, etc.), but I usually prefer Qt timers, as they have are robust and have very simple API. See a <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Automatically_load_volumes_that_are_copied_into_a_folder" rel="nofollow noopener">timer example in the script repository</a> or check out Qt documentation.</p>

---

## Post #7 by @n2018 (2019-05-30 19:33 UTC)

<p>Is it important to run it definitely through the main process and does scriptable module have several processes in it? I wonder because I tried to run my background thread using qt.Timer through class Logic.run or onApplyButton functions and GUI is frozen every time the thread makes computations and when i run it through the setUp function everything is ok, I want to have an opportunity to start my thread through logic or onApplyButton function because otherwise these thread will work all the time which is not the desired behaviour</p>

---

## Post #8 by @n2018 (2019-05-30 19:41 UTC)

<p>It seems that it was because I have another timeout (time.sleep) in my thread and that’s why gui was frozen. So qt.timer solved my problem, thanks for your help!</p>

---

## Post #9 by @lassoan (2019-05-30 19:43 UTC)

<p>For future reference, if you must run time-consuming operation in the Slicer process then you can run it as a <a href="https://discourse.slicer.org/t/how-to-run-python-based-cli-modules/4627">CLI module, which can be implemented in Python</a>.</p>

---
