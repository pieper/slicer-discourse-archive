# Changetracker module is not loaded

**Topic ID**: 17759
**Date**: 2021-05-24
**URL**: https://discourse.slicer.org/t/changetracker-module-is-not-loaded/17759

---

## Post #1 by @Chenglin_Zhu (2021-05-24 12:27 UTC)

<p>Hello!<br>
I am new to Slicer. After I installed the ChangeTracker extension and restarted the program, I could not open it from the module menu. The module menu says “Changetracker module is not loaded”.<br>
Could anyone help me with it?<br>
Thank you</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5dff5284b1bdf2aedb256bb2654861925b91b560.png" data-download-href="/uploads/short-url/dpxqGdel965tYh4JyYoEgfIIzyo.png?dl=1" title="Screen Shot 2021-05-24 at 2.57.04 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dff5284b1bdf2aedb256bb2654861925b91b560_2_690x458.png" alt="Screen Shot 2021-05-24 at 2.57.04 PM" data-base62-sha1="dpxqGdel965tYh4JyYoEgfIIzyo" width="690" height="458" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dff5284b1bdf2aedb256bb2654861925b91b560_2_690x458.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dff5284b1bdf2aedb256bb2654861925b91b560_2_1035x687.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5dff5284b1bdf2aedb256bb2654861925b91b560.png 2x" data-dominant-color="EDEFF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-05-24 at 2.57.04 PM</span><span class="informations">1350×898 86.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-05-24 15:58 UTC)

<p>Thanks for reporting this. I’ve sent a <a href="https://github.com/fedorov/ChangeTrackerPy/pull/17">pull request</a> to fix incompatibilities with recent Slicer versions. If the suggested changes get integrated then the extension will be available in the Extensions manager the following day.</p>
<p>Note that Slicer has improved a lot in recent years, therefore there is a good chance you can accomplish the same task using core modules and other extensions (using Segment Editor, Segment Statistics core modules, Segment Registration extension, etc.).</p>

---

## Post #3 by @lassoan (2021-05-25 03:42 UTC)

<p>The fix has been integrated, therefore ChangeTracker should be available for latest Slicer Stable Release and latest Slicer Preview Release from tomorrow.</p>

---

## Post #4 by @Chenglin_Zhu (2021-05-25 15:58 UTC)

<p>Thank you for the prompt response!</p>

---
