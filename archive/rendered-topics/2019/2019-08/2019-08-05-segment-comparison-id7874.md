---
topic_id: 7874
title: "Segment Comparison"
date: 2019-08-05
url: https://discourse.slicer.org/t/7874
---

# Segment Comparison

**Topic ID**: 7874
**Date**: 2019-08-05
**URL**: https://discourse.slicer.org/t/segment-comparison/7874

---

## Post #1 by @acalles2307 (2019-08-05 01:52 UTC)

<p>Hi, I’m new using 3d slicer, I’m a radiation oncologist. Recently I am carrying out a project in which I intend to compare the contours of radiotherapy, where I basically want to compare the use or improvement of a new learning system and application of an atlas made by experts, in students (residents) of this specialty.</p>
<p>Where residents will contour a clinical case in a TPS (CT) before teaching and after teaching (atlas and the new learning system that i mencionated). To make the comparisons we will use the dice similarity metrics and hausdorff distance metrics. The atlas made by experts will be compared with the contour of the students made before teaching and after teaching. And so evaluate the variance between the groups, before and after.</p>
<p>I really don’t have much time on this, but reading on the forum I came to the following conclusion: I must take the dicom rt from the TPS, then import them into the 3D Slicer and compare the contours with segment comparison of the slicer rt.</p>
<p>So far and so it sounds simple … but trying to make a test using sample date of 3D Slicer, specifically CTChest and the segment editor, creating two segments of heart quite similar but not the same (because is manually), but says coefficient always gives me 0 despite that the segments and hausdorff distance metrics change give me very large values.</p>
<p>Thank you very much for your help, I know that these concepts are very basic for you but for me they are new.</p>

---

## Post #2 by @cpinter (2019-08-05 02:29 UTC)

<p>Thanks for the detailed explanation about your project! What you describe is I think the correct way to do this.</p>
<p>I did what you described and reported as a problem and it worked for me. I don’t have a lot of information about how you did the test, but I have a hunch:<br>
Are you sure you did not overwrite the first heart segment with the second one? Segment Editor’s default settings do that. If you go down to Masking options and change “Overwrite other segments” to “None” (or if you use the latest nightly we renamed it to “Modify other segments” and “Overlap allowed”), then the second segment will not erase those parts in the first one.<br>
Since I worked mostly in RT use cases, I would have preferred an overlap allowed default, but apparently the most frequent use cases of Slicer prefer the erasing method.</p>

---

## Post #3 by @acalles2307 (2019-08-06 02:30 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d963b19f223456396d46ac39eb27b026ae77417.png" data-download-href="/uploads/short-url/b4mDgFfh6s8lkVq0aITaLcvXLRJ.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d963b19f223456396d46ac39eb27b026ae77417_2_690x427.png" alt="imagen" data-base62-sha1="b4mDgFfh6s8lkVq0aITaLcvXLRJ" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d963b19f223456396d46ac39eb27b026ae77417_2_690x427.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d963b19f223456396d46ac39eb27b026ae77417.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d963b19f223456396d46ac39eb27b026ae77417.png 2x" data-dominant-color="CBCCCD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">1019×631 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f764613ac5692b982b9a4d276be45c0f59cf3ef.png" data-download-href="/uploads/short-url/fU2oLObcs6jgsgT6m73Q5BBedC7.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f764613ac5692b982b9a4d276be45c0f59cf3ef_2_690x433.png" alt="imagen" data-base62-sha1="fU2oLObcs6jgsgT6m73Q5BBedC7" width="690" height="433" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f764613ac5692b982b9a4d276be45c0f59cf3ef_2_690x433.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f764613ac5692b982b9a4d276be45c0f59cf3ef.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f764613ac5692b982b9a4d276be45c0f59cf3ef.png 2x" data-dominant-color="CECFD1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">1013×637 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>thats the value that the slicer give to me in the test. sorry but i dont find where is the masking options. <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=12" title=":confused:" class="emoji" alt=":confused:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @lassoan (2019-08-06 03:08 UTC)

<p>You need to activate an effect to see masking options.</p>

---
