---
topic_id: 10015
title: "Failed To Run Slicer Codes In Pycharm Whats Wrong With My Se"
date: 2020-01-30
url: https://discourse.slicer.org/t/10015
---

# Failed to run slicer codes in PyCharm, what's wrong with my settings?

**Topic ID**: 10015
**Date**: 2020-01-30
**URL**: https://discourse.slicer.org/t/failed-to-run-slicer-codes-in-pycharm-whats-wrong-with-my-settings/10015

---

## Post #1 by @Illusion (2020-01-30 03:47 UTC)

<p>Operating system: Tried both Windows10 and Linux Ubuntu<br>
Slicer version:4.10.2<br>
Expected behavior:Run and debug slicer in PyCharm using codes from <a href="https://github.com/Slicer/SlicerNotebooks/blob/master/01_Data_Loading_and_Visualization.ipynb" rel="nofollow noopener">https://github.com/Slicer/SlicerNotebooks/blob/master/01_Data_Loading_and_Visualization.ipynb</a><br>
following <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools</a><br>
Actual behavior:<br>
Always being not able to run codes,</p>
<p>pydevd_pycharm.settrace(‘localhost’, port=4567, stdoutToServer=True, stderrToServer=True)<br>
Waiting for process connection…<br>
Connected to pydev debugger (build 193.5233.109)<br>
Expected: %s to exist.<br>
None</p>

---

## Post #2 by @lassoan (2020-01-30 03:58 UTC)

<p>You don’t run code. Slicer runs code that are in scripted modules or that you type in the Python console and if you put a breakpoint in the code then you can do step-by-step debugging from there.</p>

---

## Post #3 by @Illusion (2020-01-30 04:01 UTC)

<p>Hi Iassoan,</p>
<p>Thank you for your reply.<br>
But I cannot understand. I am not able to type anything in the Python console:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6469e252e0a295bcf7fc2783660586c259de3683.png" data-download-href="/uploads/short-url/ekiBmwwuXYCk9JAAO6njGWQc2R5.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6469e252e0a295bcf7fc2783660586c259de3683.png" alt="Capture" data-base62-sha1="ekiBmwwuXYCk9JAAO6njGWQc2R5" width="690" height="237" data-dominant-color="C0DCC3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1063×366 16.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you please let me know what should I do in detail?</p>

---

## Post #4 by @lassoan (2020-01-30 04:07 UTC)

<p>It seems that you missed this step described in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools#Start_debugging">instructions page</a>: “Important: once Slicer is paused at a breakpoint, you can open a terminal, where you can enter Python commands (you have access to all Slicer variables, it has auto-complete, etc). Click the small terminal icon  <em>Show Python Prompt</em>  to open the Python console.”</p>
<p>                    <a href="https://www.slicer.org/w/img_auth.php/a/a2/PyCharmDebugConsole.png" target="_blank" class="onebox" rel="nofollow ugc noopener">
            <img src="https://www.slicer.org/w/img_auth.php/a/a2/PyCharmDebugConsole.png" width="690" height="441">
          </a>

</p>
<p>If you click that button (the second from the bottom) then the output window turns into an interactive Python console.</p>

---

## Post #5 by @Illusion (2020-01-30 04:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="10015">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>once Slicer is paused at a breakpoint</p>
</blockquote>
</aside>
<p>How to pause in Slicer? I did not find a “pause” button, nor being able to add a breakpoint in the Slicer. <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @lassoan (2020-01-30 04:29 UTC)

<p>Pause option is in the “Run” menu. If you click it then Slicer will break as soon as it executes some Python code.</p>
<p>Slicer will also pause automatically at any breakpoints that you added (this is the usual way of pausing the program).</p>

---

## Post #7 by @Illusion (2020-01-30 04:42 UTC)

<p>So sorry that I am not able to find it. <img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=9" title=":joy:" class="emoji" alt=":joy:"><br>
<img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=9" title=":sweat_smile:" class="emoji only-emoji" alt=":sweat_smile:"><br>
Could you please show a screenshot of the “Run” menu and “Pause” option in Slicer?<br>
Thank you very much!</p>

---

## Post #8 by @lassoan (2020-01-30 04:46 UTC)

<p>It’s here:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d73f030b7e96c45e9c8df53fb7078b1cc6ad77a.png" data-download-href="/uploads/short-url/hTO4YQW6zQCLv10FSQ3VFdQCuo2.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d73f030b7e96c45e9c8df53fb7078b1cc6ad77a_2_409x500.png" alt="image" data-base62-sha1="hTO4YQW6zQCLv10FSQ3VFdQCuo2" width="409" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d73f030b7e96c45e9c8df53fb7078b1cc6ad77a_2_409x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d73f030b7e96c45e9c8df53fb7078b1cc6ad77a_2_613x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d73f030b7e96c45e9c8df53fb7078b1cc6ad77a_2_818x1000.png 2x" data-dominant-color="5C5E5F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">898×1096 88.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But as I wrote, it is rarely used and instead you normally pause by inserting breakpoints.</p>

---

## Post #9 by @Illusion (2020-03-09 22:55 UTC)

<p>Hi Iassoan,</p>
<p>I am now able to manually type into the PyCharm python console after pausing the program.<br>
However, I have no idea how to debug a script. All I can do now is to copy the code one line by one line every time I want to run something. <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=9" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"></p>
<p>Could you please let me know, how could I run a script while being able to debug with breakpoint without using extension wizard introduced in the tutorial example?</p>
<p>Thank you very much!</p>

---

## Post #10 by @lassoan (2020-03-09 23:47 UTC)

<p>You have several options.</p>
<ol>
<li>
<p>Copy-paste code line-by-line to the Python console in Slicer</p>
</li>
<li>
<p>Use SlicerJupyter module to use Slicer as a Jupyter kernel. No need to copy-paste, you can run a cell at a time (it is easy to split/merge cells). You can combine this with method 1.</p>
</li>
<li>
<p>Put your code into a Slicer module (you can change the code without restarting Slicer: save the changes then save the file hit Reload button in Slicer) and insert a breakpoint where you want to start step-by-step debugging. You can combine this with method 1 and even method 2.</p>
</li>
</ol>

---

## Post #11 by @Illusion (2020-03-10 01:06 UTC)

<p>Hi Iassoan,</p>
<p>To use PyCharm for debugging, is the “Extension Wizard” under “Developer Tool” the only way to add a new Module? And is it also the only way to debug a script in PyCharm?</p>

---

## Post #12 by @lassoan (2020-03-10 01:26 UTC)

<aside class="quote no-group" data-username="Illusion" data-post="11" data-topic="10015">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/e19b73/48.png" class="avatar"> Illusion:</div>
<blockquote>
<p>To use PyCharm for debugging, is the “Extension Wizard” under “Developer Tool” the only way to add a new Module? And is it also the only way to debug a script in PyCharm?</p>
</blockquote>
</aside>
<p>Creating a skeleton module (where you can copy-paste your script into) using Extension Wizard should not take more than a few minutes. Doing manually would take more time and would be more error-prone, so I would recommend using Extension Wizard. You might be able to run script from a file manually (using importlib), but reloading might be a bit tricky, and again, this is simpler using the module template, which shows a Reload (and Reload&amp;Test) button, which reloads the file by a single click.</p>

---
