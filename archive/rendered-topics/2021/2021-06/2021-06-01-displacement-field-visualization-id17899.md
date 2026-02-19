---
topic_id: 17899
title: "Displacement Field Visualization"
date: 2021-06-01
url: https://discourse.slicer.org/t/17899
---

# Displacement field visualization

**Topic ID**: 17899
**Date**: 2021-06-01
**URL**: https://discourse.slicer.org/t/displacement-field-visualization/17899

---

## Post #1 by @Loc_Tran (2021-06-01 12:25 UTC)

<p>Hello all,</p>
<p>I have one cardiac CT volume and one displacement field. I would like to apply a transform to both the volume node and the displacement field node to see the short axis view of the heart and how the deformation field looks like on the view. First, I created new transform for the CT volume, and checked the Interaction in 3D view box. Then, I applied the transform on my displacement field. Finally, I rotated the interactive volume to get a new view. Below is what I got</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4ce4938d5e5b771cf99f8d37bef5de26cafaf356.png" data-download-href="/uploads/short-url/aYe0DU2LggIyU7aQCiU4Bmbq6IS.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4ce4938d5e5b771cf99f8d37bef5de26cafaf356_2_690x257.png" alt="Capture" data-base62-sha1="aYe0DU2LggIyU7aQCiU4Bmbq6IS" width="690" height="257" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4ce4938d5e5b771cf99f8d37bef5de26cafaf356_2_690x257.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4ce4938d5e5b771cf99f8d37bef5de26cafaf356_2_1035x385.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4ce4938d5e5b771cf99f8d37bef5de26cafaf356_2_1380x514.png 2x" data-dominant-color="7C797B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1914×715 75.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
original view (before the rotation)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8bea013784149de14357dcd4207b846c7f8637e.png" data-download-href="/uploads/short-url/sDRUe8Utg5cOsQUmVvSzT4Ga1Pg.png?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8bea013784149de14357dcd4207b846c7f8637e_2_690x256.png" alt="Capture1" data-base62-sha1="sDRUe8Utg5cOsQUmVvSzT4Ga1Pg" width="690" height="256" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8bea013784149de14357dcd4207b846c7f8637e_2_690x256.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8bea013784149de14357dcd4207b846c7f8637e_2_1035x384.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8bea013784149de14357dcd4207b846c7f8637e_2_1380x512.png 2x" data-dominant-color="8F7779"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">1919×712 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
view after the rotation</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc1230649fac2e96091383a6780971c2de42caf7.png" alt="Capture2" data-base62-sha1="voQ0Pei9yii9hzxFi4f6lB2nScL" width="620" height="485"><br>
transform info</p>
<p>The volume after transformation looks good but the displacement field looks wrong. I was wondering if you could show me how to display the displacement field on my rotated view. Thank you in advance for your help.</p>

---

## Post #2 by @lassoan (2021-06-01 13:53 UTC)

<p>In transform visualization the measurement frame is always the same as the visualization frame, which is the world coordinates system. If you simply rotate the displacement field then that rotation is concatenated to the transformation - and this is what you show in the screenshot above. This is the correct and expected behavior.</p>
<p>If you want to show the volume’s displacements in the rotated coordinate system, then you need to do a change of basis. If <code>BulkTransform</code> is your change-of-basis transform then you need to clone that transform and invert it (<code>BulkTransform Copy (-)</code>) and make it the child transform of your transformed displacement field transform (implementing the basis transform <em>inv(P)</em> * <em>M</em> * <em>P</em>). If you visualize this <code>BulkTransform Copy (-)</code> transform then you will see the displacement vectors that you wanted.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68f3529850e78b923b9733383b689c49ddcbb1e5.png" alt="image" data-base62-sha1="eYqYlfQ3NrgyVcoSaMJY0wkG7wp" width="390" height="182"></p>

---

## Post #3 by @Loc_Tran (2021-06-01 18:06 UTC)

<p>Thank you so much for your help. It worked.</p>

---
