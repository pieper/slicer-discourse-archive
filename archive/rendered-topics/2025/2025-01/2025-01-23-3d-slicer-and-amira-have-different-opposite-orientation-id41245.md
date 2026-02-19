---
topic_id: 41245
title: "3D Slicer And Amira Have Different Opposite Orientation"
date: 2025-01-23
url: https://discourse.slicer.org/t/41245
---

# 3d Slicer and Amira have different(opposite) orientation

**Topic ID**: 41245
**Date**: 2025-01-23
**URL**: https://discourse.slicer.org/t/3d-slicer-and-amira-have-different-opposite-orientation/41245

---

## Post #1 by @Puja_Ghosh (2025-01-23 19:13 UTC)

<p>Why MRI data orientation of 3d Slicer and Amira is opposite? the left and right side is opposite to each other? Can anyone please tell why this happens? which one is correct?</p>

---

## Post #2 by @pieper (2025-01-23 19:30 UTC)

<p>This material should help you understand:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html</a></p>

---

## Post #3 by @Puja_Ghosh (2025-01-23 20:23 UTC)

<p>Thank you for the link. But I have a few more questions about it. If 3D slicer store data in LPS then why it works in RAS? Won’t it be confusing? MRI dicom file is mostly in LPS then if 3D slicer is using file in RAS to view, isn’t 3D slicer showing wrong view?</p>

---

## Post #4 by @muratmaga (2025-01-23 21:15 UTC)

<p>Slicer’s handles the RAS/LPS conversion and writing LPS to disk correctly.<br>
You may want to look into what Amira does.</p>
<p>Also are you talking mirroring in 3D view or in slice views (the latter can be due to using different conventions of looking at slice view: radiology vs neurology)</p>

---

## Post #5 by @Puja_Ghosh (2025-01-24 17:11 UTC)

<p>Thank you for the information Prof. I am confused about the view of both Amira and 3d slicer. When I load data I get the left and right totally opposite in Amira and 3d slicer. (Small information: The patient lay down on the left side for the scan. ) Then which view should be correct?<br>
The above one is 3d slicer and below one is amira.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cebd32414feffd41650f4375174add9337d104c.jpeg" data-download-href="/uploads/short-url/dg1b84uEfcTPX9n1h8iSlkHtp9O.jpeg?dl=1" title="emmi114_3dslicer_copy" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cebd32414feffd41650f4375174add9337d104c_2_690x383.jpeg" alt="emmi114_3dslicer_copy" data-base62-sha1="dg1b84uEfcTPX9n1h8iSlkHtp9O" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cebd32414feffd41650f4375174add9337d104c_2_690x383.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cebd32414feffd41650f4375174add9337d104c_2_1035x574.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cebd32414feffd41650f4375174add9337d104c_2_1380x766.jpeg 2x" data-dominant-color="434849"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">emmi114_3dslicer_copy</span><span class="informations">1920×1067 95.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3b896a0f016deac6f59e5f9a41ce2760e266d06.jpeg" data-download-href="/uploads/short-url/rVqAiQ1XWWiH80rIaCiB8dqA7v8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3b896a0f016deac6f59e5f9a41ce2760e266d06_2_690x429.jpeg" alt="image" data-base62-sha1="rVqAiQ1XWWiH80rIaCiB8dqA7v8" width="690" height="429" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3b896a0f016deac6f59e5f9a41ce2760e266d06_2_690x429.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3b896a0f016deac6f59e5f9a41ce2760e266d06_2_1035x643.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3b896a0f016deac6f59e5f9a41ce2760e266d06_2_1380x858.jpeg 2x" data-dominant-color="45474A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1194 95.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @muratmaga (2025-01-24 17:27 UTC)

<aside class="quote no-group" data-username="Puja_Ghosh" data-post="5" data-topic="41245">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/puja_ghosh/48/77922_2.png" class="avatar"> Puja_Ghosh:</div>
<blockquote>
<p>Then which view should be correct?</p>
</blockquote>
</aside>
<p>There is no right, just different convention. Neurological convention, what slicer uses by default, shows the patient’s R on your L in slice view (because you are typically facing the patient directly).</p>
<p>Looks like Amira is using the radiological convention. Hence the mirroring in the transverse sections (red slice in Slicer), everything else seems normal. If you enable the 3D view in the amira, I think you can confirm that (there should be no mirroring in 3D view).</p>

---

## Post #7 by @Puja_Ghosh (2025-01-24 17:33 UTC)

<p>This is the 3d view in Amira and the left of 3d slicer is the right of amira, and vice versa. (small information: when we take data from patient, we take the data when we are facing towards patient directly, i.e. our left is patients right) In this case, which convention I should choose ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ecaa731a9205b6f0d1913458c0edf7c92d4376a.jpeg" data-download-href="/uploads/short-url/fO6HEeX6qIME4cg1RYHcH2ucjBE.jpeg?dl=1" title="image (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ecaa731a9205b6f0d1913458c0edf7c92d4376a_2_680x500.jpeg" alt="image (1)" data-base62-sha1="fO6HEeX6qIME4cg1RYHcH2ucjBE" width="680" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ecaa731a9205b6f0d1913458c0edf7c92d4376a_2_680x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ecaa731a9205b6f0d1913458c0edf7c92d4376a_2_1020x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ecaa731a9205b6f0d1913458c0edf7c92d4376a_2_1360x1000.jpeg 2x" data-dominant-color="497A7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image (1)</span><span class="informations">1920×1410 96.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @muratmaga (2025-01-24 17:42 UTC)

<p>Well you are using segmentation instead of volume rendering to look at the data, so things are a little different between two images. But from what I can tell, yes, you seem to have a mirroring issue.</p>
<p>If these are DICOMs then I would look into Amira for the cause of issue.</p>

---

## Post #9 by @Puja_Ghosh (2025-01-24 17:46 UTC)

<p>So Amira is showing mirroring issue not 3d slicer? and as we are taking patient directly facing them, then we should use the data which matches with the patients left and right. Isn’t it? In this case, 3d slicer is showing the exact view of patient?</p>

---

## Post #10 by @muratmaga (2025-01-24 17:50 UTC)

<p>If this data came as DICOM originally, yes, I suspect the issue is in Amira. As Slicer’s DICOM module is used a lot for medical data and a big issue like this would have came up earlier.</p>
<p>Slice views have nothing to do how the image is taken. it is simply a display convention (think of how you would look at image on a transparent medium,. You can look at it from behind, you can look at it from front. It doesn’t change the image itself).</p>

---

## Post #11 by @Puja_Ghosh (2025-01-24 17:57 UTC)

<p>The data comes as Dicom. And thank you so much Prof for clearing the confusions. Thanks again.</p>

---

## Post #12 by @jamesobutler (2025-01-24 19:59 UTC)

<p>You can change whether patient right is screen left or not. See the below forum post</p>
<aside class="quote quote-modified" data-post="8" data-topic="29883">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/a-bit-of-confusion-about-the-slicer-coordinate-system/29883/8">A bit of confusion about the slicer coordinate system</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In Edit-&gt;Application Settings you can change whether patient right is screen left or not. 
[image] 
That work came out of the following PR if you are curious about the conversation that led to it.
  </blockquote>
</aside>


---

## Post #13 by @Puja_Ghosh (2025-01-24 21:17 UTC)

<p>Thank you James for the information. I looked into the views of orientation and my data shows that the patient is screen left. Can you please tell me what does that mean? and how the orientation works?</p>

---
