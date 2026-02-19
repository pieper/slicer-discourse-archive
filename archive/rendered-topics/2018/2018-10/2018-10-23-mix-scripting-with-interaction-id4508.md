---
topic_id: 4508
title: "Mix Scripting With Interaction"
date: 2018-10-23
url: https://discourse.slicer.org/t/4508
---

# Mix scripting with interaction

**Topic ID**: 4508
**Date**: 2018-10-23
**URL**: https://discourse.slicer.org/t/mix-scripting-with-interaction/4508

---

## Post #1 by @kayarre (2018-10-23 17:33 UTC)

<p>I am working on a script that can load matching images  and segmentation from levelset. I want to programmatically load each pair, .e.g. case 1, case 2, etc. and then perform edits to the segmentation and then after the manual edits are complete continue the script to do additional processsing/saving and move to the next data pair.</p>
<p>is there a way to combine scripting with interactive input?</p>

---

## Post #2 by @lassoan (2018-10-23 18:03 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerCaseIterator">Case iterator extension</a> is developed for this purpose. It is a simple scripted module, so it should be easy to customize or enhance it as needed. Pull requests with fixes and improvements are welcome.</p>

---

## Post #3 by @kayarre (2018-10-23 22:35 UTC)

<p>this seems overly complicated at the moment. is there a simpler example out there?</p>
<p>I tried the extension but it fails to load. I filed a bug about it. <a href="https://github.com/JoostJM/SlicerCaseIterator/issues" rel="nofollow noopener">https://github.com/JoostJM/SlicerCaseIterator/issues</a></p>

---

## Post #4 by @lassoan (2018-10-26 05:36 UTC)

<aside class="quote no-group" data-username="kayarre" data-post="3" data-topic="4508">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>I tried the extension but it fails to load.</p>
</blockquote>
</aside>
<p>Thanks for testing this. The issue is now fixed. You can fix it locally on your computer by removing the first line (the Python shebang) of SlicerCaseIterator.py.</p>
<aside class="quote no-group" data-username="kayarre" data-post="3" data-topic="4508">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>this seems overly complicated at the moment. is there a simpler example out there?</p>
</blockquote>
</aside>
<p>It should be easy to use this module - see documentation <a href="https://github.com/JoostJM/SlicerCaseIterator">here</a>. If you have any questions feel free to post them here.</p>
<p><a class="mention" href="/u/joostjm">@JoostJM</a></p>

---

## Post #5 by @lassoan (2023-03-21 03:03 UTC)



---
