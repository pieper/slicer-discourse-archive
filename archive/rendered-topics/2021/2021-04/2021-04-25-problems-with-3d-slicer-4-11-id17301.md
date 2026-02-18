# Problems with 3D slicer 4.11

**Topic ID**: 17301
**Date**: 2021-04-25
**URL**: https://discourse.slicer.org/t/problems-with-3d-slicer-4-11/17301

---

## Post #1 by @aseman (2021-04-25 05:45 UTC)

<p>Slicer version:4.11<br>
Hi 3D slicer experts and all<br>
I want to  use 3D slicer 4.11, but when I load RT plan , its error is: could not loud RT PLAN as a RT.<br>
Also, when I want to install new extensions such as “LongitudinalPETCT”  there isn’t this extension, while in slicer 4.10.2 I could install it.<br>
can you help me for these problems and how can I solve them?<br>
Thanks a lot</p>

---

## Post #2 by @lassoan (2021-04-25 13:16 UTC)

<p>RT plan loading has been hugely improved since 4.10. Much more of the plan is loaded that represented in the scene. Therefore, it is possible that some issues in the RT plan file were ignored but now causing problems.</p>
<p>Please share an anonymized data set so that we can investigate. If you share your application logs then it may give us some hints about what goes wrong.</p>
<aside class="quote no-group" data-username="aseman" data-post="1" data-topic="17301">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/c0e974/48.png" class="avatar"> aseman:</div>
<blockquote>
<p>LongitudinalPETCT” there isn’t this extension, while in slicer 4.10.2 I could install it</p>
</blockquote>
</aside>
<p>Not all maintainers can keep their extensions compatible with Slicer core changes.</p>
<p>I tried to help out with the updating this extension to Slicer-4.11 but many changes were necessary to migrate from the legacy Editor module to the new Segment Editor and the module’s workflow was somewhat unclear, so I could not complete the work. I still haven’t given up, but I’m not actively working on it anymore.</p>
<p>What feature of LongitudinalPETCT extension do you need?</p>

---
