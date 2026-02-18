# Using Python for image registration

**Topic ID**: 5207
**Date**: 2018-12-27
**URL**: https://discourse.slicer.org/t/using-python-for-image-registration/5207

---

## Post #1 by @dinank (2018-12-27 21:32 UTC)

<p>Operating system: Linux<br>
Slicer version: 4.8.1</p>
<p>I am new to Slicer and I have a task to register MRI and CT volumes using Rigid registration. I have a large data and do not want to repeat the process many times for different patients, as I currently do. I was wondering if it is possible to streamline this process, where I just use the file locations of MRI and CT volumes and Slicer does registration and saves a new file. I use Python for analyzing the images so was hoping if there was a way that I can use Python for this.<br>
Thanks!</p>

---

## Post #2 by @pieper (2018-12-29 17:53 UTC)

<p>Yes, writing a script to run registration on your data should be straightforward.</p>
<p>This would be a good place to start learning about how:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules#Scripted_Modules" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules#Scripted_Modules</a></p>
<p>Also you should look at the <a href="https://github.com/JoostJM/SlicerCaseIterator" rel="nofollow noopener">CaseIterator</a> as a start point for looping through collections of data.</p>

---
