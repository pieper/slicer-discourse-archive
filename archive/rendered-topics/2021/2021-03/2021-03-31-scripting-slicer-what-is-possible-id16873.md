---
topic_id: 16873
title: "Scripting Slicer What Is Possible"
date: 2021-03-31
url: https://discourse.slicer.org/t/16873
---

# Scripting Slicer - What is possible?

**Topic ID**: 16873
**Date**: 2021-03-31
**URL**: https://discourse.slicer.org/t/scripting-slicer-what-is-possible/16873

---

## Post #1 by @Hball99 (2021-03-31 10:45 UTC)

<p>Hello there!<br>
I am quite new to Slicer and I am having difficulties to understand what is actually possible with Slicer Scripting and what not.</p>
<p>So my problem is the following: I know that I can script modules that I can import into Slicer GUI. But what I want to do, is to use all the slicer functions in a seperate python script outside of the Slicer GUI by just importing the module “slicer”.</p>
<p>I have seen that there is a big script repository at<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository</a><br>
but is that a script repository only for slicer modules? Or can I use all those functions also in arbitrary python scripts as long as I import slicer correctly?</p>
<p>If that would be possible, I have another question regarding the installation of slicer. Right now, I have just downloaded slicer from the homepage <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a>. But then there is a different installation guide for developers at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html" class="inline-onebox" rel="noopener nofollow ugc">Windows — 3D Slicer documentation</a> .<br>
Do I have to install that on top of the regular programm or instead? Or don’t I need that at all? Because I cannot figure out how to import slicer packages into any python script.</p>
<p>I hope I was able to tell what exactly my problem is. Also sorry, I am quite new to all of this. To give a bit of context: my ultimate goal is to script the problem that I have 200 .nrrd Segementations that I want to convert to nii.gz (Labelmap-) Volumes while being able to define a reference Volume for each Segmentation.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2021-03-31 17:17 UTC)

<p>Slicer has a built-in python, but we don’t package slicer something you can import into other python environments (we’ve talked about this as a goal, but it’s not the way things are now).</p>
<p>So any of the example scripts expect you to have a slicer environment to operate in.  If you start slicer with the <code>--no-main-window</code> option and the <code>--python-script &lt;script&gt;.py</code> it will work like a regular python environment, or <code>Slicer --no-main-window --python-code "slicer.app.pythonConsole().show()"</code> will pop up a console with the slicer commands available but no other gui unless you create one.</p>
<p>HTH</p>

---
