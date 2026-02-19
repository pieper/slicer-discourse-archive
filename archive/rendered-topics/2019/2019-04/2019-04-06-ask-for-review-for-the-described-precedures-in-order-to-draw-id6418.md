---
topic_id: 6418
title: "Ask For Review For The Described Precedures In Order To Draw"
date: 2019-04-06
url: https://discourse.slicer.org/t/6418
---

# Ask for review for the described precedures in order to draw ROIs and measure volumes.

**Topic ID**: 6418
**Date**: 2019-04-06
**URL**: https://discourse.slicer.org/t/ask-for-review-for-the-described-precedures-in-order-to-draw-rois-and-measure-volumes/6418

---

## Post #1 by @otanit (2019-04-06 03:32 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.1<br>
Expected behavior: Draw ROIs manually without artifacts and measure the ROI volumes correctly.<br>
Actual behavior: Stripe artifacts or scattered dots appeared in the slice next to the slice I draw ROIs using Draw Effect, Paint Effect and Eraser in the Segment Editor module.</p>
<p>Dear the member of the 3D Slicer Forum,</p>
<p>I tried the following procedures in order to delete artifacts, however, I am not sure they are appropriate for drawing ROIs on the brain image and measure ROI volumes correctly.<br>
Thus, I would like to have your review for the following procedures I performed, and have your advice if they are not appropriate.</p>
<p>Although the stripe artifacts could be deleted, the angle of the brain (i.e. AC-PC line in the sagittal slice) was changed after clicking the icon in the Segment Editor module (please see the yellow circle of the attached first file named “ICON”).</p>
<p>I could correct this change by going to Transforms module, create new Linear Transform, and apply “gray scale MRI (in this case, file named “b12”)” to Transformed box (but not apply “Segmentation”).<br>
Please see red circles in the attached second file named “Transforms”.</p>
<p>Then, I could draw color with Paint Effect and Draw Effect on the corrected brain position going to Segment Editor module.<br>
In this step, I selected Segmentation in the column of “Segmentation” and b12 (the file name of gray scale MRI)  in the column of “Master volume” (please see red circles in the attached third file named “Segment Editor”).</p>
<p>At last, I went to the Segment Statistics module, select Segmentation in the column of “Segmentation”  and b12 (the name of the gray scale file) in the column of “Scalar volume”, and click Apply.</p>
<p>I would like to have your advice if there is any misunderstanding for the procedures above.<br>
I appreciate your time and kind advice.</p>
<p>Best wishes,<br>
otanit</p>
<p>First file ICON: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/4209a0e4a8c48882357335dcd3a45620d5ca3e4a.jpeg" data-download-href="/uploads/short-url/9qc8NOKaqfb9KxrEqxxioi9C3Wi.jpeg?dl=1" title="ICON" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4209a0e4a8c48882357335dcd3a45620d5ca3e4a_2_690x388.jpeg" alt="ICON" data-base62-sha1="9qc8NOKaqfb9KxrEqxxioi9C3Wi" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4209a0e4a8c48882357335dcd3a45620d5ca3e4a_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4209a0e4a8c48882357335dcd3a45620d5ca3e4a_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/4209a0e4a8c48882357335dcd3a45620d5ca3e4a.jpeg 2x" data-dominant-color="6F6A6A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ICON</span><span class="informations">1280×720 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> !<br>
Second file Transforms: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6eb8cd593d2fe9bf5f52257c73116729829c431.jpeg" data-download-href="/uploads/short-url/uFgQeBRbgFP1rKuyzwZlNvNx8Od.jpeg?dl=1" title="Transforms" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6eb8cd593d2fe9bf5f52257c73116729829c431_2_690x388.jpeg" alt="Transforms" data-base62-sha1="uFgQeBRbgFP1rKuyzwZlNvNx8Od" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6eb8cd593d2fe9bf5f52257c73116729829c431_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6eb8cd593d2fe9bf5f52257c73116729829c431_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6eb8cd593d2fe9bf5f52257c73116729829c431.jpeg 2x" data-dominant-color="716D6E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Transforms</span><span class="informations">1280×720 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Third file Segment Editor: <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54d3ef2a04bd5f6c76343f81433d54bb7a9ab51c.jpeg" data-download-href="/uploads/short-url/c6qaORrGiG0MhOkju2MHezf79Yo.jpeg?dl=1" title="Segment%20Editor" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54d3ef2a04bd5f6c76343f81433d54bb7a9ab51c_2_690x388.jpeg" alt="Segment%20Editor" data-base62-sha1="c6qaORrGiG0MhOkju2MHezf79Yo" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54d3ef2a04bd5f6c76343f81433d54bb7a9ab51c_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54d3ef2a04bd5f6c76343f81433d54bb7a9ab51c_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54d3ef2a04bd5f6c76343f81433d54bb7a9ab51c.jpeg 2x" data-dominant-color="757174"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Segment%20Editor</span><span class="informations">1280×720 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @rkikinis (2019-04-07 19:13 UTC)

<p>Hi,</p>
<p>it sounds like a complicated workflow. Let’s see if there are other recommendations from the community. If I understand it correctly, you are interested in performing a reorientation of a data set using the AC-PC line and then manually paint gyrus on the reoriented coronal views. Is this correct?</p>

---

## Post #3 by @otanit (2019-04-08 01:41 UTC)

<p>Thank you for your response and confirmation.</p>
<p>Yes, it is correct.<br>
I am trying to draw gyrus manually on the brain corrected by AC-PC line.<br>
I had to perform several procedures in order to delete appeared<br>
artifacts.<br>
I would like to confirm whether the procedures I perfromed for drawing<br>
ROIs and calculating ROI volumes were correct, since I have to avoid<br>
huge waste of time caused by my misunderstanding.</p>
<p>I appreciate the member’s time and any advice for this consultation.</p>
<p>Best wishes,<br>
otanit</p>

---

## Post #4 by @Amine (2019-04-08 06:37 UTC)

<p>Hi, i suggest you use reformat module to change slice angle and not transform the whole volume.<br>
As for what you call artifacts its perfectly normal since you did use a spheric brush, try using threshold paint in segmenteditorextraeffects (you need to download it) with a bigger brush, its easier to clean up afterwards, or you could segment the cortex first then use scissor tool+ logical operations to cut it with the help of the 3d view.<br>
However i see you have spheric brush uchecked. What kind of artifacts do you exaclty get?</p>

---

## Post #5 by @otanit (2019-04-10 08:08 UTC)

<p>Dear Amine,</p>
<p>I apologize my late response for your advice.<br>
I tried a lot of things including segmenteditorextraeffects.<br>
However, I could not address the problems.<br>
I think I could not understand your advice and perform the necessary procedures appropriately.</p>
<p>I found other way, although I am not sure it is appropriate.<br>
If the following procedures are not appropriate, I would like to have your advice.<br>
At first I went to the Segment Editor module, and clicked the icon next to the Segmentation box in order to align slice views to segmentation.<br>
Second, I went to the Transforms module, moved only the gray scale MRI file from the Transformable box to Transformed box, and change the Rotation to adjust AC-PC line.<br>
Third, I went to the Segment Editor module again, and draw ROIs using Paint Effect and Draw Effect.<br>
I could avoid artifacts by performing the procedures above.</p>
<p>I would like to know whether these procedures are correct for drawing ROIs manually without artifacts, and whether I can measure ROI volumes correctly with these drawn ROIs.<br>
I appreciate your time and kind advice.</p>
<p>Best wishes,<br>
otanit</p>

---

## Post #6 by @lassoan (2019-04-11 00:11 UTC)

<p>If you slice through the volume in two different views and the shape and size of segments are correct on all slices then the computed volumes will be correct, too.</p>

---

## Post #7 by @otanit (2019-04-12 08:33 UTC)

<p>I appreciate your kind advice.<br>
The shape and size of segments are correct on all slices.<br>
I hope my drawings will be measured correctly by segment statistics module.<br>
However, I have another trouble when I save the labelmap on the way of drawing and try to open it again in order to re-start drawing.<br>
I will post this problem in another title.<br>
Best,</p>

---

## Post #8 by @Amine (2019-04-14 06:30 UTC)

<p>Hi, the steps you described do not use anything specific to adress the issue you report(just rotating the volume), however if the results do satisfy you thats okay.<br>
I do recommend using segment editor extra effects since its the new reference editor, the old editor module is rather obsolete when you compare the functions.<br>
To use threshold paint start by finding a threshold that contains your structures (go to threshold and slide the bar until you get a satisfying value) then enter it under Masking options(scroll down to find it in segment editor) --&gt; editable: inside threshold and enter the value you found. Your painting will now only affect that zone and should reduce leaking into other parts.</p>

---

## Post #9 by @otanit (2019-04-17 08:47 UTC)

<p>I appreciate your kind advice.<br>
I didn’t know how to use the threshold icon.<br>
I will try to use it following your advice, and find the appropriate range for drawing.<br>
Thanks a lots.</p>

---
