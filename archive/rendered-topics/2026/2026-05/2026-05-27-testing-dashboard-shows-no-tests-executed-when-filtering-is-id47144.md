---
topic_id: 47144
title: "Testing dashboard shows no tests executed when filtering is used"
date: 2026-05-27
url: https://discourse.slicer.org/t/47144
last_bumped: 2026-05-27T17:48:06.436Z
---

# Testing dashboard shows no tests executed when filtering is used

**Topic ID**: 47144
**Date**: 2026-05-27
**URL**: https://discourse.slicer.org/t/testing-dashboard-shows-no-tests-executed-when-filtering-is-used/47144

---

## Post #1 by @cpinter (2026-05-27 08:48 UTC)

<p>Hi all,</p>
<p>I wanted to look at the test results of some extensions today. First I thought that the factory machine does not run any tests, because filtering on SlicerRT I saw this (and I know the extension has around 70 tests):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83a12384e6f19a20ac12e3a3810927f971047f45.png" data-download-href="/uploads/short-url/iMrMMsNdck6dWIk74mAOUHmx7tH.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83a12384e6f19a20ac12e3a3810927f971047f45_2_690x90.png" alt="image" data-base62-sha1="iMrMMsNdck6dWIk74mAOUHmx7tH" width="690" height="90" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83a12384e6f19a20ac12e3a3810927f971047f45_2_690x90.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83a12384e6f19a20ac12e3a3810927f971047f45_2_1035x135.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83a12384e6f19a20ac12e3a3810927f971047f45.png 2x" data-dominant-color="BAC4CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1331×175 17.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Started investigating, and it seems that this may be an issue in the dashboard filtering, because if I remove the filter and search for SlicerRT in the long list, this is what I see.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70530061a923961c243b260f8075cce5de57641f.png" data-download-href="/uploads/short-url/g1Fj0qvYOPy828ana0gxfBaRf9t.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70530061a923961c243b260f8075cce5de57641f_2_690x63.png" alt="image" data-base62-sha1="g1Fj0qvYOPy828ana0gxfBaRf9t" width="690" height="63" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70530061a923961c243b260f8075cce5de57641f_2_690x63.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70530061a923961c243b260f8075cce5de57641f_2_1035x94.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70530061a923961c243b260f8075cce5de57641f_2_1380x126.png 2x" data-dominant-color="D9D7C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1483×136 15 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I chose a slightly older date so that it can be seen that the timestamps match exactly.</p>
<p>Has there been any update in this code lately? This used to work.<br>
<a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>
<p>Thanks a lot!</p>

---

## Post #2 by @ebrahim (2026-05-27 17:48 UTC)

<p>I do see the tests executed when filtering:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/19ea11aceca6412ad2983fc8b5724a722608f9f8.png" data-download-href="/uploads/short-url/3HfquPUddMmW65vH0Fk8DNfbWMU.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19ea11aceca6412ad2983fc8b5724a722608f9f8_2_690x142.png" alt="image" data-base62-sha1="3HfquPUddMmW65vH0Fk8DNfbWMU" width="690" height="142" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19ea11aceca6412ad2983fc8b5724a722608f9f8_2_690x142.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19ea11aceca6412ad2983fc8b5724a722608f9f8_2_1035x213.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/19ea11aceca6412ad2983fc8b5724a722608f9f8_2_1380x284.png 2x" data-dominant-color="D8DCE3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1902×394 55.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Maybe my filtering (build name contains “slicerrt”) is different  – what’s your filtering to get this issue?</p>

---
