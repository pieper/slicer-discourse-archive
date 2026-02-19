---
topic_id: 13076
title: "Loading 4D Volume As Sequence Using Python Script"
date: 2020-08-18
url: https://discourse.slicer.org/t/13076
---

# Loading 4D volume as Sequence using python script

**Topic ID**: 13076
**Date**: 2020-08-18
**URL**: https://discourse.slicer.org/t/loading-4d-volume-as-sequence-using-python-script/13076

---

## Post #1 by @CJohnson (2020-08-18 16:13 UTC)

<p>Operating system: Windows 10<br>
Slicer version: Slicer 4.11.0<br>
Expected behavior: Load 4D volume nrrd file as sequence using script<br>
Actual behavior: volume is loaded as vtkMRMLMultiVolumeNode</p>
<p>Hi All<br>
I can’t find the right methods to load the 4D volume nrrd file as a Sequence with the vtkMRMLScalarVolumeNode being created in the Subject Hierarchy.</p>
<p>I have the Sequences Extension installed and have saved a multivolume file as a nrrd file. I can load this manually using the Add Data dialog with the “Volume Sequence” option in the description dropdown.</p>
<p>How do I do this using scripting?</p>

---

## Post #2 by @adamrankin (2020-08-18 16:21 UTC)

<p>Is there a <code>slicer.util.loadSequence</code> function?</p>

---

## Post #3 by @CJohnson (2020-08-18 16:33 UTC)

<p>Unfortunately there isn’t.</p>

---

## Post #4 by @lassoan (2020-08-18 16:46 UTC)

<p>You can use <code>slicer.util.loadNodeFromFile</code>. For example:</p>
<pre><code>sequenceNode = slicer.util.loadNodeFromFile("c:/tmp/something.seq.nrrd", "SequenceFile")
</code></pre>
<p>I’ve <a href="https://github.com/Slicer/Slicer/commit/752f5f9161cf27c830303f26b4bd74feb72669ba">added a <code>slicer.uitil.loadSequence</code> convenience function</a> to make this easier to figure out.</p>

---

## Post #5 by @CJohnson (2020-08-18 18:10 UTC)

<p>Typing this into the Python Interactor (as well as my code) gives me a runtime error:</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\Carol\AppData\Local\NA-MIC\Slicer 4.11.0-2019-07-15\bin\Python\slicer\util.py”, line 398, in loadNodeFromFile<br>
raise RuntimeError(errorMessage)<br>
RuntimeError: Failed to load node from file: D:\BainesWork…\ImageVolumes\DCE\ShortName.seq.nrrd</p>

---

## Post #6 by @lassoan (2020-08-18 18:13 UTC)

<p>Make sure you specify path correctly (using forward-slash, double-backslash, or raw string):</p>
<aside class="quote quote-modified" data-post="14" data-topic="2837">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/subprocess-call-does-not-work/2837/14">Subprocess.call does not work!</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    FYI, since backslash (\) is an escape character in Python, you cannot simply use it in a string literal in Python. 
The easiest is to indicate that you specify a raw string by prepending an r character before the string. This is correct: 
somePath = r"F:\someFolder\python.exe"

If you need to use a regular string then backslash can be entered by typing double-backslash. This is correct: 
somePath = "F:\\someFolder\\python.exe"

You may also use Unix-type separators. This is correct: 
somePath = …
  </blockquote>
</aside>

<p>If you still have issues, upgrade to latest Slicer Preview Release.</p>

---

## Post #7 by @CJohnson (2020-08-18 20:36 UTC)

<p>This does work with the latest nightly version of Slicer.</p>
<p>Thank you.</p>

---
