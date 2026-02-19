---
topic_id: 21238
title: "Tool Similar To Remove Islands For This Scenario"
date: 2021-12-27
url: https://discourse.slicer.org/t/21238
---

# Tool similar to "remove islands" for this scenario

**Topic ID**: 21238
**Date**: 2021-12-27
**URL**: https://discourse.slicer.org/t/tool-similar-to-remove-islands-for-this-scenario/21238

---

## Post #1 by @JoeCrozier (2021-12-27 15:24 UTC)

<p>Hello, hopefully this question is ‘allowed’ given its probably a matter of preference.  I have a scene with a segmentation like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdfe60edb49f9315f13cfb99b97008ce7a75e111.jpeg" data-download-href="/uploads/short-url/r6Lfe7IpJEO0u4FPzhiWr5O33sl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bdfe60edb49f9315f13cfb99b97008ce7a75e111_2_690x473.jpeg" alt="image" data-base62-sha1="r6Lfe7IpJEO0u4FPzhiWr5O33sl" width="690" height="473" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bdfe60edb49f9315f13cfb99b97008ce7a75e111_2_690x473.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bdfe60edb49f9315f13cfb99b97008ce7a75e111_2_1035x709.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdfe60edb49f9315f13cfb99b97008ce7a75e111.jpeg 2x" data-dominant-color="4A4641"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1160×796 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Is there a tool for quickly eliminating the particles circled in red?  They’re not “islands” as they technically connect somewhere, but they’re very clearly (to the human eye at least) not the bone I’m intending to get.</p>
<p>I guess my question is:   I’ve just been using either scissors or going slice by slice with erase to clean it up.  Is there something faster?</p>

---

## Post #2 by @lassoan (2021-12-27 21:07 UTC)

<p>Smoothing effect with Median (or maybe Erode) method should take care of this. You can apply Island effect → Keep largest island after this to remove large disconnected regions.</p>
<p>You may also increase the threshold value a bit, which will make the noise pattern more disconnected therefore making Island effect → Keep largest island remove more noise.</p>

---
