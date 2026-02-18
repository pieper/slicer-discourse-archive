# Size of buttons in user interface

**Topic ID**: 12098
**Date**: 2020-06-18
**URL**: https://discourse.slicer.org/t/size-of-buttons-in-user-interface/12098

---

## Post #1 by @ada (2020-06-18 16:29 UTC)

<p>Hello all,</p>
<p>I am writing my own custom module in python but I have some problem to create a custom user interface.<br>
I have some (basic) questions about it:</p>
<ul>
<li>Is it possible to define the size (width and height) of a QPushButton ?</li>
<li>How can I set several buttons side by side in a same row ?</li>
<li>How can I display an icon/logo into a QPushButton ?</li>
</ul>
<p>Is it possible to do all these things without using Qt Designer? only with basic python code?</p>
<p>Thank you for your help,<br>
Best</p>

---

## Post #2 by @pieper (2020-06-18 17:33 UTC)

<p>Yes, all this is possible with python.  Best thing to do is read through the related <a href="https://doc.qt.io/">Qt documentation</a> - for the most part the entire public API is available through python in slicer with just small syntax differences from the C++ examples.  Also you can look at the python code in any <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Scripted">scripted modules</a> and copy any patterns for interfaces you like.</p>

---

## Post #3 by @lassoan (2020-06-20 21:48 UTC)

<p>Here is an example of a module (not a simple one, but still may be useful) that uses style sheets that make buttons and other widgets larger so that Slicer can be used on a touch-screen tablet: <a href="https://github.com/PerkLab/CentralLineTutor/tree/master/CentralLineTutor">https://github.com/PerkLab/CentralLineTutor/tree/master/CentralLineTutor</a></p>

---

## Post #4 by @ada (2020-06-22 08:22 UTC)

<p>Thank you for your help.</p>

---

## Post #5 by @mau_igna_06 (2021-05-29 22:13 UTC)

<p>I’m interested in examples of GUI customized for touch-screen applications. Are there any examples available? (The link you posted earlier is not working)</p>

---

## Post #6 by @lassoan (2021-05-30 00:42 UTC)

<p>That repository seems to be private, but this one is public: <a href="https://github.com/SlicerIGT/LumpNav" class="inline-onebox">GitHub - SlicerIGT/LumpNav: Slicer extension for ultrasound-guided breast tumor resection (lumpectomy)</a></p>

---
