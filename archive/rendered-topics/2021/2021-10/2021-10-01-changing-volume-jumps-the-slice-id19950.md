# Changing volume jumps the slice

**Topic ID**: 19950
**Date**: 2021-10-01
**URL**: https://discourse.slicer.org/t/changing-volume-jumps-the-slice/19950

---

## Post #1 by @joachim (2021-10-01 13:29 UTC)

<p>In the Data module I may have several scalar volumes from the same scanning but with different postprocessing, or manually modified in Slicer like crop volume or an image filter.</p>
<p>My problem is that if I change the current visible volume (press the closed “eye” button in Data module), the slice(s) jumps to the center of this volume. Is this a <a href="https://i.imgur.com/RyECgQB.jpg" rel="noopener nofollow ugc">bug or a feature</a>? Or is there a setting to prevent this? Because when I now use ITK SimpleFilters on an image and want to look at the difference for a specific slice, the slice position is reset so I have to scroll back to this slice. However, jump to center does not happen when I change volume in a slice controller’s drop-down selector (this does not help when I work with the SimpleFilters module anyway).</p>

---

## Post #2 by @mikebind (2021-10-01 18:15 UTC)

<p>I also found this default behavior annoying and unexpected.  I expected clicking the eye to be basically the same as switching the background image volume on all the slice views, i.e. that it would not change the location or orientation of the slice views, just change which volume I was viewing at that location.  I began to write a response to you expressing support for having the option to change the behavior, and thought about how this should be implemented.  What came to mind was that it would make sense to have this option available on a context menu by right-clicking on the eye.  It occurred to me that I had never tried actually doing that.  I tried it, and this feature is already available  <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> Here is a screenshot.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d0eb8a8922c5288e5556a562eb7f43b5bbcd87b.png" alt="image" data-base62-sha1="dhdWAJh7P7slwXZsqgRXCgNndZF" width="409" height="172"></p>
<p>We just want to uncheck those boxes which reset the view and orientation.</p>

---

## Post #3 by @joachim (2021-10-04 08:32 UTC)

<p>Thank you, this was exactly my problem and a fully working solution <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=10" title=":smiley:" class="emoji" alt=":smiley:"> I was searching for this setting but couldn’t find it. Slicer’s right click menus contains several secrets.</p>

---
