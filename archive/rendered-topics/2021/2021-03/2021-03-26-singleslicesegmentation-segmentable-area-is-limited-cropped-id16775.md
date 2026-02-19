---
topic_id: 16775
title: "Singleslicesegmentation Segmentable Area Is Limited Cropped"
date: 2021-03-26
url: https://discourse.slicer.org/t/16775
---

# SingleSliceSegmentation segmentable area is limited/cropped

**Topic ID**: 16775
**Date**: 2021-03-26
**URL**: https://discourse.slicer.org/t/singleslicesegmentation-segmentable-area-is-limited-cropped/16775

---

## Post #1 by @LoganWade (2021-03-26 12:19 UTC)

<p>Hi, I am trying to use the SingleSliceSegmentation Module to track indiviual images to use with the AIGT code published by Ungi, T., King, F., Kempston, M., Keri, Z., Lasso, A., Mousavi, P., . . . Fichtinger, G. (2014). Spinal Curvature Measurement by Tracked Ultrasound Snapshots. Ultrasound in medicine &amp; biology, 40(2), 447-454. doi:<a href="https://doi.org/10.1016/j.ultrasmedbio.2013.09.021" rel="noopener nofollow ugc">https://doi.org/10.1016/j.ultrasmedbio.2013.09.021</a></p>
<p>However, there seems to be a very strange bug happening in that i can only perform paint segmentation in a very small area and I am not sure what is limiting this. In the image below, you can  see i have filled out the volume that it is allowing me to segment.</p>
<p>I have tried to perform this without performing volume reconstruction and after performing volume reconstruction and there does not appear to be a difference.</p>
<p>Any help would be much appreciated</p>
<p>Thanks, Logan</p>
<p>Slicer version 4.11<br>
3D ultrasound data was collected with OptiTrack and Telemed ultrasound hardware.<br>
motion capture and ultrasound data were combined to create the ImageToReference-Image</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94c1c75cfb494852358fb467438e4af88db38690.jpeg" data-download-href="/uploads/short-url/ldXPKCS8Tn9PGnO6qWB1Z2Cjcxq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/94c1c75cfb494852358fb467438e4af88db38690_2_690x360.jpeg" alt="image" data-base62-sha1="ldXPKCS8Tn9PGnO6qWB1Z2Cjcxq" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/94c1c75cfb494852358fb467438e4af88db38690_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/94c1c75cfb494852358fb467438e4af88db38690_2_1035x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/94c1c75cfb494852358fb467438e4af88db38690_2_1380x720.jpeg 2x" data-dominant-color="989EA6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1003 321 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52c4b6702b1e2ab1ae8f527a9ad1d1476d866e7a.jpeg" data-download-href="/uploads/short-url/bOcBFan9l6u6KMd01KStb3DfzNU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52c4b6702b1e2ab1ae8f527a9ad1d1476d866e7a_2_690x359.jpeg" alt="image" data-base62-sha1="bOcBFan9l6u6KMd01KStb3DfzNU" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52c4b6702b1e2ab1ae8f527a9ad1d1476d866e7a_2_690x359.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52c4b6702b1e2ab1ae8f527a9ad1d1476d866e7a_2_1035x538.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52c4b6702b1e2ab1ae8f527a9ad1d1476d866e7a_2_1380x718.jpeg 2x" data-dominant-color="979BA7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1000 312 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2021-03-26 16:08 UTC)

<p>What does your transform hierarchy look like?</p>

---

## Post #3 by @LoganWade (2021-03-29 07:57 UTC)

<p>Hi Kyle, Here is the data structure after performing volume reconstruction.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1ff17f9ad15ed65322f809f7d8ea875eddf54aa.png" data-download-href="/uploads/short-url/n75pjN2pWVVqfv7Axspt5MwLEQG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1ff17f9ad15ed65322f809f7d8ea875eddf54aa_2_690x359.png" alt="image" data-base62-sha1="n75pjN2pWVVqfv7Axspt5MwLEQG" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1ff17f9ad15ed65322f809f7d8ea875eddf54aa_2_690x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1ff17f9ad15ed65322f809f7d8ea875eddf54aa_2_1035x538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1ff17f9ad15ed65322f809f7d8ea875eddf54aa_2_1380x718.png 2x" data-dominant-color="9798A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×999 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/525764d924a3207b13657203fa9e06981ee0fe1e.png" alt="image" data-base62-sha1="bKqonyO3JgICGOR9eB3duYHz5VA" width="472" height="300"></p>

---

## Post #4 by @LoganWade (2021-04-15 08:56 UTC)

<p>Hi <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>,</p>
<p>Do you have any idea what might be causing this issue?</p>
<p>Regards,</p>
<p>Logan</p>

---

## Post #5 by @Sunderlandkyl (2021-04-16 17:40 UTC)

<p>I don’t see the segmentation in the transform hierarchy. Can you make sure that the same transform is applied to both the segmentation and the ultrasound image?</p>

---

## Post #6 by @LoganWade (2021-04-23 08:18 UTC)

<p>Hi <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a></p>
<p>When I start doing segmentations this is what my data tree looks like.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/690707acaec6c03d3188cdbde548db6e0b4ee9cc.png" alt="image" data-base62-sha1="eZ7c9DSd9OHAj9HMm6MLjP85D88" width="390" height="181"></p>
<ol>
<li>Do I need to perform volume reconstruction before doing segmentation?</li>
<li>Should the Segmentation be within the Logan2_ImageToReference-ImageToReference tree? I have tried this but performing segmentation like this extremely slows down the processing of every single click and furthermore, you end up the segmentation in the 3D view being smaller and in the wrong location.</li>
</ol>
<p>I cannot find any information for how the single slice segmentation is actually meant to work? It is very frustrating because opening slicer and doing the exact same steps results in different results, sometimes it will not even draw a segmentation on any frame, sometimes it is only 1 frame out of the whole sequence and then other times it will do most of the area except for having an border that also is never in the same place.</p>

---

## Post #7 by @Sunderlandkyl (2021-04-23 16:26 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, Do you remember what the required steps are to use SingleSliceSegmentation?</p>

---

## Post #8 by @lassoan (2021-04-23 17:03 UTC)

<p>You need to put the segmentation under the same transform as the image. The segmentation’s geometry is specified the first time you select a master volume, so if you have already started segmentation under the wrong transform then delete the segmentation node, put it under the same parent as the image, and then start the segmentation.</p>
<p>Sequences should be set up similarly carefully (a new sequence browser needs to be created and a new sequence must be added to it that uses the segmentation node as proxy node).</p>
<p>These steps are very error-prone to perform manually. Current users create these scenes using Python scripts. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> I think we must fix this as part of the Canarie project (make the module automatically create all the necessary nodes and set parent transforms, etc.).</p>

---
