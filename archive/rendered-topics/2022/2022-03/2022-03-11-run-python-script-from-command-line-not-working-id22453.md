# Run python script from command line not working

**Topic ID**: 22453
**Date**: 2022-03-11
**URL**: https://discourse.slicer.org/t/run-python-script-from-command-line-not-working/22453

---

## Post #1 by @bserrano (2022-03-11 13:05 UTC)

<p>Hi all,</p>
<p>I want to do the same processing to several volumes so it would be very useful to use slicer code from<br>
command line.<br>
What I want is: open volume → process → export processed volume. I guess I can do it with the same code I’m using in the python interactor one by one.</p>
<p>I’ve been searching in other posts how to do it. I tried:</p>
<pre><code class="lang-auto">C:\Users\Belen\AppData\Local\NA-MIC\"Slicer 4.11.20210226"\Slicer.exe --python-script "C:\Users\Belen\Desktop\pruebaSlicer.py" -no-splash --no-main-window | more
</code></pre>
<p>and --launch python-real instead --python-script but none of them are working.</p>
<p><code>C:\Users\Belen\AppData\Local\NA-MIC\"Slicer 4.11.20210226"\Slicer.exe</code> opens slicer but <code>C:\Users\Belen\AppData\Local\NA-MIC\"Slicer 4.11.20210226"\Slicer.exe --help | more</code> is not showing anything.</p>
<p>I do not know what I am doing wrong.</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2022-03-11 22:12 UTC)

<p>Hi -</p>
<p>This has to do with the way windows handles output.  You don’t always see output in the command console the way you would on a linux or mac system (some windows expert can explain the details).  But Slicer does run the script and if you need to get output from it you can write to a file.</p>
<p>For example if you run this script you should see the output printed in the python console for a second before the program disappears. (Assumes you had the python console open when you last exited slicer and you don’t use the --no-main-window option).</p>
<pre><code class="lang-auto">print(40+2)
qt.QTimer.singleShot(1000, exit)
</code></pre>

---

## Post #3 by @cpinter (2022-03-11 22:20 UTC)

<p>I usually do batch processing within the same Slicer session. I process one dataset, close the scene (<code>slicer.mrmlScene.Clear()</code>) and can proceed with the next one.</p>
<p>Btw I also think your script should work and it may be an issue with the output the way you do it.</p>

---

## Post #4 by @bserrano (2022-03-12 11:31 UTC)

<p>Hi,</p>
<p>I runned this script but nothing is happening. It seems like Slicer is not running the code.</p>
<p>(base) C:\Users\Belen&gt;C:\Users\Belen\AppData\Local\NA-MIC"Slicer 4.11.20210226"\Slicer.exe --python-script C:\Users\Belen\Desktop\pruebaSlicer.py</p>
<p>And pruebaSlicer.py:</p>
<pre><code class="lang-auto">print(40+2)
qt.QTimer.singleShot(1000, exit)```</code></pre>

---

## Post #5 by @pieper (2022-03-12 15:44 UTC)

<p>Do you still have the three backtick characters after the second line?  (the <code>```</code>). These would be a python syntax error that might not be reported.  Make sure whatever is in your script file works when typed into the python console in Slicer.</p>

---

## Post #6 by @bserrano (2022-03-12 22:46 UTC)

<p>No, I do not have the ``` (it was a typo). When I run the command, slicer did not even open. But it opens if I do not write “–python-script …”</p>

---

## Post #7 by @bserrano (2022-03-12 23:01 UTC)

<p>Oh, I already make it. I changed directory to the slicer.exe path. It’s weird… thank you so much. I will try the processing code.</p>

---

## Post #8 by @lassoan (2022-03-13 03:06 UTC)

<p>The problem was that Slicer executable path was specified with an incorrect syntax (misplaced quotation mark). It seems that Windows can tolerate this, but the command-line argument parser in the Slicer launcher is more strict.</p>
<p>Solution: a path that contain spaces must be quoted by placing a quotation mark at the beginning and at the end.</p>
<p>For example, instead of this (incorrect):</p>
<aside class="quote no-group" data-username="bserrano" data-post="1" data-topic="22453">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p><code>C:\Users\Belen\AppData\Local\NA-MIC\"Slicer 4.11.20210226"\Slicer.exe</code></p>
</blockquote>
</aside>
<p>Slicer.exe path must be specified like this:</p>
<pre><code>"C:\Users\Belen\AppData\Local\NA-MIC\Slicer 4.11.20210226\Slicer.exe"
</code></pre>

---

## Post #9 by @bserrano (2022-03-15 09:49 UTC)

<p>Thanks for the explanation.<br>
I noticed that when I run the script (no --no-main-window) the code continues running even when I close the program (slicer). How can I stop the execution without having to do it by killing a process?</p>

---

## Post #10 by @pieper (2022-03-15 12:37 UTC)

<p>You can call <code>exit()</code> when your processing is finished.</p>

---

## Post #11 by @bserrano (2022-03-15 13:54 UTC)

<p>I meant something similar to ctrl+C for the cmd.</p>

---

## Post #12 by @lassoan (2022-03-17 01:19 UTC)

<p>Slicer launcher (Slicer.exe) is built as a GUI application in the official Slicer installation packages. GUI applications are not killed if you hit Ctrl-C.</p>
<p>There is a trick that you can use if you really must use Ctrl-C instead of the X button. We include a console-mode launcher <code>PythonSlicer.exe</code>, you can rename that and replace the original GUI-mode <code>Slicer.exe</code> launcher. The console-mode launcher will respond to Ctrl-C on the latest Slicer Preview Release (because there the SlicerApp-real.exe executable is also built as a console application). However killing the process like this will not result in a clean exit, because objects are not destructed so VTK will report memory leaks. Stable releases might be built with error leak reporting disabled, but that will not stop on Ctrl-C (because in that version SlicerApp-real.exe is not a console application yet). If you want a solution for a clean exit from the command prompt using Ctrl-C then you need to build Slicer yourself or wait for the new Slicer Stable Release (expected in a week or so).</p>
<p>What is your overall goal? How would you like to launch and stop Slicer?</p>

---

## Post #13 by @bserrano (2022-03-21 07:47 UTC)

<p>Ok, many thanks for the explanation.</p>
<p>I am just curious. I have codes that operate on many models and sometimes it is very useful to be able to terminate the execution of the program abruptly, in the same way as with another console program.</p>

---

## Post #14 by @lassoan (2022-03-21 12:30 UTC)

<p>Your can use the latest Slicer Preview Release with the console-mode launcher as described above; and ignore the listed memory leaks.</p>
<p>Alternatively, you can terminate the process tree using Processes Explorer (Sysinternals utility); or look up the the SlicerApp-real.exe process and terminate it.</p>

---
