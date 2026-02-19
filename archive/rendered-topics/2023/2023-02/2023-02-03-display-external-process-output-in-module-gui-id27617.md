---
topic_id: 27617
title: "Display External Process Output In Module Gui"
date: 2023-02-03
url: https://discourse.slicer.org/t/27617
---

# Display external process output in module GUI

**Topic ID**: 27617
**Date**: 2023-02-03
**URL**: https://discourse.slicer.org/t/display-external-process-output-in-module-gui/27617

---

## Post #1 by @Saima (2023-02-03 02:00 UTC)

<p>Hi Andras,<br>
I wrote a scripted module and I am calling an external python using subprocess_checkoutput.</p>
<p>Is there a way to get the terminal output into a GUI component to let the user of a module know about the program is still running.</p>
<p>Which GUI component is good for displaying the program processing?<br>
how can I capture the terminal output?</p>
<p>regards,<br>
Saima</p>

---

## Post #2 by @Saima (2023-02-07 04:30 UTC)

<p>how can I get the gui box with errors and progress bar in python scripted module</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee7493bd56a968640586792565d016773ed9a482.png" alt="image" data-base62-sha1="y1tp0aaFNcwzO1BTS2mzogWerTk" width="572" height="285"></p>

---

## Post #3 by @lassoan (2023-02-07 14:03 UTC)

<p>You can have a look at other modules that print process output in the module GUI, for example <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/d9b4f6e7a2eae05d099836aa8d314a59df066262/TotalSegmentator/TotalSegmentator.py#L748-L749">TotalSegmentator</a>.</p>

---

## Post #4 by @Saima (2023-02-09 06:01 UTC)

<p>Hi Andras,<br>
Could you please let me know which part of the code refers to the output display and what is the name of the GUI component used.</p>
<p>regards,<br>
Saima</p>

---

## Post #5 by @lassoan (2023-02-15 04:10 UTC)

<p>The line that I posted the link to (<code>self.logProcessOutput()</code>) notifies the GUI about the new output by calling the <code>self.log</code> callback. I would recommend to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/python.html#python-debugging">attach a debugger</a> add a breakpoint in <code>logProcessOutput</code> and execute the code step by step so that you can see what methods are called, check type of any variables, etc.</p>

---

## Post #6 by @Saima (2023-03-02 02:32 UTC)

<p>Sorry Andras, but I am finding it hard to see how the textbox below the apply button is attached to the log for displaying all the output.</p>
<p>Could you please help. I simply want to display the back end interpreter outputs in the textbox while the program is running.<br>
regards,<br>
Saima</p>

---

## Post #7 by @Saima (2023-03-02 04:46 UTC)

<p>Hi andras,<br>
Thank you so much I managed to use the code from totalsegmentator to output the interpreter output into the GUI component.</p>
<p>Thank you</p>
<p>regards.,<br>
saima</p>

---

## Post #8 by @Saima (2023-03-02 05:30 UTC)

<p>Hi Andras,<br>
I did the implementation and it shows output correctly but I do not understand about logCallback</p>
<p>regards,<br>
Saima</p>

---

## Post #9 by @lassoan (2023-03-02 06:32 UTC)

<p>You can search on the web for “Python callback” or “Python hook” for more information. For example: <a href="https://stackoverflow.com/questions/1319074/how-can-i-provide-a-callback-to-an-api" class="inline-onebox">python - How can I provide a "callback" to an API? - Stack Overflow</a></p>

---

## Post #10 by @Saima (2023-03-03 02:10 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="27617">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>or “Python callback” or “Python hook” for more information. F</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
Thank you so much for all your suggestions and help.</p>
<p>could you please suggest the best way to avoid any force quit by slicer. I successfully wrote the python scripted module. The purpose is to run 300 images and get the segmentation automatically using bratstoolkit and managing the directories it create for 300 images. On top of that I am using 3D Slicer to apply the transform to the segmented region of interest to get it aligned with the original MRI for each of these images and saving the transformed segmentation.</p>
<p>The slicer windows pop up telling to force quit or wait? how to get rid of this issue? I did wait every time and then it runs fine but how to avoid this issue?</p>
<p>Also i am using the nightly build version of slicer not the stable release.</p>
<p>Thank you</p>
<p>regards,<br>
Saima</p>

---

## Post #11 by @lassoan (2023-03-03 02:13 UTC)

<p>The question in this topic has been answered. If you have a new question then please create a new topic. Be specific. If you just say that Slicer hangs but we don’t know what you did then of course we have no idea what to do about it.</p>

---
