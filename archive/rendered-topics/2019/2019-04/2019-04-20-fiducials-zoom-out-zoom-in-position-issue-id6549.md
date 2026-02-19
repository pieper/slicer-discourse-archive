---
topic_id: 6549
title: "Fiducials Zoom Out Zoom In Position Issue"
date: 2019-04-20
url: https://discourse.slicer.org/t/6549
---

# Fiducial's zoom-out zoom-in position issue

**Topic ID**: 6549
**Date**: 2019-04-20
**URL**: https://discourse.slicer.org/t/fiducials-zoom-out-zoom-in-position-issue/6549

---

## Post #1 by @michalikthomas (2019-04-20 09:14 UTC)

<p>Placed fiducial seems to be at an incorrect position after zoom-out and again zoom-in inside slice plane view. See attached screenshots for demonstration.</p>
<ol>
<li>On the left there is the initial state - in the view, there is a volumetric node in the background, yellow is a polygonal model and green markup fiducial.</li>
<li>The view after zooming-out (using mouse scroll wheel + ctrl)</li>
<li>The view after zooming-in. Volume and model nodes seem to be (relative to each other) in the right position, but markup fiducial lies way away.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45c0a638133f86f634bd0d2a84202030019bb775.png" data-download-href="/uploads/short-url/9X3H4iP8MB85y8R5XpPPP6SfV0F.png?dl=1" title="slicer-slice-view-zoomin" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45c0a638133f86f634bd0d2a84202030019bb775_2_690x209.png" alt="slicer-slice-view-zoomin" data-base62-sha1="9X3H4iP8MB85y8R5XpPPP6SfV0F" width="690" height="209" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45c0a638133f86f634bd0d2a84202030019bb775_2_690x209.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45c0a638133f86f634bd0d2a84202030019bb775_2_1035x313.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45c0a638133f86f634bd0d2a84202030019bb775.png 2x" data-dominant-color="292726"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer-slice-view-zoomin</span><span class="informations">1355×412 34.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This view issue is just temporal, and it is back to normal after moving back and forth to the previous/next slice and back. Then the fiducial is again displayed in the middle of the yellow model as it was at the very beginning. The same “recovery” can also be achieved by resetting fiducial position which invokes fiducial redraw and then it is again in the right place.</p>
<p>Slicer version: Slicer-4.10.1-linux-amd64-2<br>
OS: Ubuntu 18.10</p>
<p>Does anyone face the same behavior?</p>

---

## Post #2 by @pieper (2019-04-25 21:15 UTC)

<p>Can you try again using the current nightly build?  There was an issue where fiducials and segments would tend to ‘swim’ with respect to the background and that has been resolved as part of the markups rework.  I wouldn’t have expected it to have this effect, but if you are zooming in and out very quickly it might.</p>

---

## Post #3 by @michalikthomas (2019-04-25 22:09 UTC)

<p>I have checked current nightly build and everything works perfectly as expected.</p>

---
