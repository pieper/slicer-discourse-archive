# Love totalSegmentator!-anyway to batch output multiple studies?

**Topic ID**: 27828
**Date**: 2023-02-15
**URL**: https://discourse.slicer.org/t/love-totalsegmentator-anyway-to-batch-output-multiple-studies/27828

---

## Post #1 by @artycho (2023-02-15 16:13 UTC)

<p>Operating system: windows 10<br>
Slicer version: 5.2.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello, Great work on the TotalSegmentator!<br>
Cannot believe that TotalSegmentator can precisely identify so many organs at one time!</p>
<p>I have two questions on total segmentator:</p>
<ol>
<li>
<p>I would like to use T.S. for multiple studies, is there a command line that I can use to batch open a patient in the slicer database, have T.S. segment the organs, then save the ROIs as nifti file, or better yet, have the CT housenfield values saved?<br>
I am very eager to use T.S. on a very large database of patients. I have the patients all imported in 3d slicer database.</p>
</li>
<li>
<p>There are a few organs that are not yet identified on T.S, such as thyroid, various muscles, etc. Is there a way to “train” the T.S. to identify these organs if I submit ROIs?</p>
</li>
</ol>
<p>Thank you, and keep up the great work!</p>

---

## Post #2 by @rbumm (2023-02-15 16:50 UTC)

<p>Hi,</p>
<aside class="quote no-group" data-username="artycho" data-post="1" data-topic="27828">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/e19b73/48.png" class="avatar"> artycho:</div>
<blockquote>
<p>I would like to use T.S. for multiple studies, is there a command line</p>
</blockquote>
</aside>
<p>there is no official script yet but it should be easy to write in Python, because all necessary functions are disclosed  in the <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/d9b4f6e7a2eae05d099836aa8d314a59df066262/TotalSegmentator/TotalSegmentator.py#L283">TotalSegmentator extension logic</a>.</p>
<aside class="quote no-group" data-username="artycho" data-post="1" data-topic="27828">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/e19b73/48.png" class="avatar"> artycho:</div>
<blockquote>
<p>There are a few organs that are not yet identified on T.S, such as thyroid, various muscles, etc. Is there a way to “train” the T.S. to identify these organs if I submit ROIs?</p>
</blockquote>
</aside>
<p>TotalSegmentator is undergoing active development and you could post a request under “issues” in <a href="https://github.com/wasserth/TotalSegmentator">TotalSegmentator Github</a>, where the original code is hosted. Our extension just wraps this code for ease of use in 3D Slicer.</p>
<p>You could even <a href="https://github.com/wasserth/TotalSegmentator#retrain-model-on-your-own">train the engine</a> yourself according to its developer, but there is another option as <a class="mention" href="/u/pieper">@pieper</a> pointed out: Train back MONAILabel with Totalsegmentator results and add missing structures there.</p>

---

## Post #3 by @rbumm (2023-02-16 09:37 UTC)

<p>Maybe <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/master/PythonScripts/processAllCTInDir.py">this python script</a> (not a beauty, but working) can give you an idea how to involve an extension logic, scan directories for input files, and process them.</p>

---
