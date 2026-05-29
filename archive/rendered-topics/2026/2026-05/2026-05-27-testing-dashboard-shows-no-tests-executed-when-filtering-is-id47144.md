---
topic_id: 47144
title: "Testing dashboard shows no tests executed when filtering is used"
date: 2026-05-27
url: https://discourse.slicer.org/t/47144
last_bumped: 2026-05-28T14:12:31.741Z
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

## Post #3 by @cpinter (2026-05-28 12:16 UTC)

<p>Well, good for you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> I tried again and I still don’t:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d66b826e2aca64dc6f8664dc685366023df5386.png" data-download-href="/uploads/short-url/b2IQ6vuVDWpi01nk15FwFa5ANPU.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d66b826e2aca64dc6f8664dc685366023df5386_2_690x378.png" alt="image" data-base62-sha1="b2IQ6vuVDWpi01nk15FwFa5ANPU" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d66b826e2aca64dc6f8664dc685366023df5386_2_690x378.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d66b826e2aca64dc6f8664dc685366023df5386_2_1035x567.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d66b826e2aca64dc6f8664dc685366023df5386_2_1380x756.png 2x" data-dominant-color="D7DCD7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1410×773 81.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To get this, I used this link<br>
<a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=6&amp;showfilters=1&amp;filtercombine=or&amp;field1=label&amp;compare1=63&amp;value1=SlicerRT&amp;field2=label&amp;compare2=63&amp;value2=GelDosimetry&amp;field3=label&amp;compare3=63&amp;value3=SlicerHeart&amp;field4=label&amp;compare4=63&amp;value4=SegmentRegistration&amp;field5=label&amp;compare5=63&amp;value5=SlicerVirtualReality&amp;field6=label&amp;compare6=63&amp;value6=SurfaceMarkup">CDash - MyExtensions</a><br>
in Chrome (Windows) and I went back a day to make sure the whole build and test was finalized for the shown day.</p>
<p>I just tried it in Firefox and Edge, and I see exactly the same (still on Windows).</p>

---

## Post #4 by @cpinter (2026-05-28 12:18 UTC)

<aside class="quote no-group" data-username="ebrahim" data-post="2" data-topic="47144">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/ebrahim/48/13403_2.png" class="avatar"> ebrahim:</div>
<blockquote>
<p>Maybe my filtering (build name contains “slicerrt”) is different – what’s your filtering to get this issue?</p>
</blockquote>
</aside>
<p>If I filter by Label then I get no tests as in my screenshots. If I filter by Build Name as you did, I can see the tests. Strange, because filtering gives the actual builds, just shows no tests. Also strange because this is the link I’ve been using for a decade, and it worked before.</p>

---

## Post #5 by @ebrahim (2026-05-28 13:23 UTC)

<p>Yep I am reproducing it now!</p>
<p>Opened a bug report: <a href="https://github.com/Kitware/CDash/issues/3749" class="inline-onebox">Filtering by label zeros out test results · Issue #3749 · Kitware/CDash · GitHub</a></p>
<p>It could be a newly introduced bug/behavior since i see the deployed <a href="http://cdash.org">cdash.org</a> is on a relatively new version</p>

---

## Post #6 by @cpinter (2026-05-28 14:12 UTC)

<p>Thank you very much <a class="mention" href="/u/ebrahim">@ebrahim</a> ! Good enough for me to know that it works with filtering on Build Name and that there is an issue to track this. Thanks again!</p>

---
