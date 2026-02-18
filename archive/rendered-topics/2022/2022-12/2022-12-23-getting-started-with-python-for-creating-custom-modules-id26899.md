# Getting started with python for creating custom modules

**Topic ID**: 26899
**Date**: 2022-12-23
**URL**: https://discourse.slicer.org/t/getting-started-with-python-for-creating-custom-modules/26899

---

## Post #1 by @Tobias (2022-12-23 13:15 UTC)

<p>Hi,<br>
We use 3D slicer and markup as a tool in education and also a combination of different datasets and markup during the examination of students.</p>
<p>Some students think it is a bit difficult to do this manually, hence I am staring the process to develop an extension that should combine choosing the dataset as well as handling markups.</p>
<p>I have started with the extention wizard that gives you the ability to choose between different datasets (but to threshold).</p>
<p>If anyone could give me some advice on the following it would be very appreciated:</p>
<ol>
<li>where do I find a list of the commands that slicer cand respond to? For instance after choosing a dataset in the dropdown list. I want it to be the active one in slicer</li>
<li>Is there a way to load parts from a different module easily into another? In that case is there a resource on how to make this calls?</li>
</ol>
<p>I would of course also be very thankful for any other advice to get me going.</p>

---

## Post #2 by @lassoan (2022-12-24 05:16 UTC)

<aside class="quote no-group" data-username="Tobias" data-post="1" data-topic="26899">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/c67d28/48.png" class="avatar"> Tobias:</div>
<blockquote>
<p>where do I find a list of the commands that slicer cand respond to? For instance after choosing a dataset in the dropdown list. I want it to be the active one in slicer</p>
</blockquote>
</aside>
<p>Hundreds of thousands of commands are available in Slicer (entire Qt, VTK, SimpleITK library, Python core libraries, etc. are already bundled and you can install any number of additional Python packages), so giving an exhaustive list is impossible.</p>
<p>I would recommend to start with the <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx?raw=true">PerkLab bootcamp’s Slicer programming tutorial</a>. There are also a number of Slicer tutorials on youtube - see for example <a href="https://www.youtube.com/playlist?list=PLTuWbByD80TORd1R-J7j7nVQ9fot3C2fK">these</a>.</p>
<aside class="quote no-group" data-username="Tobias" data-post="1" data-topic="26899">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/c67d28/48.png" class="avatar"> Tobias:</div>
<blockquote>
<p>Is there a way to load parts from a different module easily into another? In that case is there a resource on how to make this calls?</p>
</blockquote>
</aside>
<p>Yes, there are lots of reusable widgets. You can find instructions <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features">here</a> for finding any Slicer feature that you want to use in Python.</p>
<p>If you don’t find anything in tutorials or examples in the script repository then you can also always ask here.</p>

---
