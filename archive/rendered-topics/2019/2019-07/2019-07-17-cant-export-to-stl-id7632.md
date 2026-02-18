# Can't Export to STL

**Topic ID**: 7632
**Date**: 2019-07-17
**URL**: https://discourse.slicer.org/t/cant-export-to-stl/7632

---

## Post #1 by @harsh (2019-07-17 15:05 UTC)

<p>I have tried to export a nrrd file of a large CT scan that I have gotten, I go to segment editor and then select the segment I want via the threshold function… I try to do ‘show 3D’ and it doesn’t work. I have 64gb<br>
(upgraded from 32gb) of ram available and a 500gb ssd.I want a STL of this. Any Idea how?</p>

---

## Post #2 by @cpinter (2019-07-17 15:07 UTC)

<aside class="quote no-group" data-username="harsh" data-post="1" data-topic="7632">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/57b2e6/48.png" class="avatar"> harsh:</div>
<blockquote>
<p>it doesn’t work</p>
</blockquote>
</aside>
<p>Please elaborate on what happens instead.<br>
Is there anything in the log? (About / Report an error)</p>

---

## Post #3 by @harsh (2019-07-17 15:25 UTC)

<p>application either crashes and force closes itself or goes to bad allocation, I feel as I am doing something wrong setting up the file.</p>

---

## Post #4 by @cpinter (2019-07-17 15:29 UTC)

<p>Is there anything in the log? (About / Report an error)</p>
<p>What is the resolution of the CT?</p>

---

## Post #5 by @harsh (2019-07-17 15:47 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="7632">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Is there anything in the log? (About / Report an error)</p>
</blockquote>
</aside>
<p>no.<br>
the resolution of the CT is really high, I’m not sure what it is exactly though however…</p>

---

## Post #6 by @cpinter (2019-07-17 15:53 UTC)

<p>You can check the resolution in the Volumes module.</p>
<p>If you disable smoothing (checkbox in the dropbown menu of the Show 3D button) then does it show up?</p>

---

## Post #7 by @lassoan (2019-07-19 04:11 UTC)

<aside class="quote no-group" data-username="harsh" data-post="5" data-topic="7632">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/57b2e6/48.png" class="avatar"> harsh:</div>
<blockquote>
<p>the resolution of the CT is really high</p>
</blockquote>
</aside>
<p>You may need to increase virtual memory size in your system settings (e.g., try to set it to 10x larger than the size of your CT image).</p>

---
