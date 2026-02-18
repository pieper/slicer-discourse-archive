# Combining Segmentations of Different MRI files

**Topic ID**: 3238
**Date**: 2018-06-19
**URL**: https://discourse.slicer.org/t/combining-segmentations-of-different-mri-files/3238

---

## Post #1 by @rnahum (2018-06-19 23:06 UTC)

<p>Hello!<br>
I segmented the sagittal, coronal, and axial views of MRI scans of three separate .nrrd files and I made an individual segmentation for each view. Is there a way that I can combine these three segmentations into one segmentation in slicer?</p>
<p>Operating system:Windows<br>
Slicer version: 4.8.1<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @Mustafa (2018-06-19 23:34 UTC)

<p><a class="mention" href="/u/rnahum">@rnahum</a> Do you want them to be in one orientation? Or, do you want to simply overlay segmentations?</p>

---

## Post #3 by @rnahum (2018-06-20 00:03 UTC)

<p><a class="mention" href="/u/mustafa">@Mustafa</a>  Just overlay the segmentations</p>

---

## Post #4 by @lassoan (2018-06-20 00:08 UTC)

<p>In summary: if the goal is 3D reconstruction then acquire a single volume with isotropic pixel spacing. See this post for more details: <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2?u=lassoan">Combining volumes - what am I missing?</a></p>

---

## Post #5 by @rnahum (2018-06-20 00:18 UTC)

<p>Does this method combine the MRI scans, and will I have to redo the segmentations? Is there a way to just combine the segmentations?</p>

---

## Post #6 by @Mustafa (2018-06-22 21:48 UTC)

<aside class="quote no-group" data-username="rnahum" data-post="5" data-topic="3238" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/f04885/48.png" class="avatar"> rnahum:</div>
<blockquote>
<p>Does this method combine the MRI scans, and will I have to redo the segmentations? Is there a way to just combine the segmentations?</p>
</blockquote>
</aside>
<p>I prepared a recipe for you. Hope, it will help.</p>
<p>1-) In what format (dcm, nii, etc.) do you store your segmentations?  Are they loadable to Slicer? If yes, please proceed.</p>
<p>2-) Let us say you overlay segmentations from three different orientations . I don’t expect a meaningful result out of this because location and shape of segmentations are very different on each volumes. We, homo sapiens, can correlate a semantic to axial, coronal and sagittal otherwise they are way different matrices from each other when computer reads them.</p>
<p>3-) Instead of <span class="hashtag-raw">#2</span>, revisit <span class="hashtag-raw">#1</span> and pick an orientation and convert two others into the first one. This step involves in squeezing&amp; rotating volumes that  I have never done it on Slicer.</p>
<p>4-) I am not able to test now but you may not even need to convert anything (neglect <span class="hashtag-raw">#3</span>) because Slicer automatically extracts three orientations and visualizes once you load a volume. Therefore, let us say, you can save axial view of coronal and axial view of sagittal and the axial itself.</p>
<p>5-) Then overlay two psudeoaxials and the axial itself.</p>
<p>These five steps are all for segmentations. I expects the size of segmentation masks are same with original scans. Hence, in terms of matrix size convenience there shouldnt be any problem. Matrix is matrix whether they are segmentations or not.</p>
<p>Sorry for the late reply.</p>
<p>Best Regards,</p>
<p>Mustafa</p>

---

## Post #7 by @Mustafa (2018-06-22 21:50 UTC)

<p>They are in nrrd.  That’s good.</p>

---

## Post #8 by @rnahum (2018-06-22 21:56 UTC)

<p><a class="mention" href="/u/mustafa">@Mustafa</a> thank you!</p>
<p>I have one more question: can I load the other segmentations from the other two views into the segmentation of the third view using the segment editor module? or will I need to use a different module?</p>

---

## Post #9 by @rnahum (2018-06-22 22:48 UTC)

<p>Also would the pseudoaxials just be the segmentations of the coronal and sagittal views?</p>

---

## Post #10 by @lassoan (2018-06-22 23:52 UTC)

<aside class="quote no-group" data-username="rnahum" data-post="8" data-topic="3238">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/f04885/48.png" class="avatar"> rnahum:</div>
<blockquote>
<p>can I load the other segmentations from the other two views into the segmentation of the third view using the segment editor module</p>
</blockquote>
</aside>
<p>Yes, you can import any segments from any segmentation into another segmentation node. To prevent losing details duting import, make sure the segmentation node where you import the segments has sufficiently high resolution (you can create a higher resolution segmentation by cropping/resampling using Crop volumes module). In 1-2 weeks <a href="https://github.com/Slicer/Slicer/pull/975">we’ll add a feature to segmentation module, which will make this resampling very easy</a>.</p>

---

## Post #11 by @rnahum (2018-07-25 20:16 UTC)

<p>Hello!<br>
I was wondering if this resampling feature has been added to the segmentation module yet?</p>

---

## Post #12 by @lassoan (2018-07-25 20:36 UTC)

<p>Yes, it is already available in nightly version of Slicer. Click on the button on the right side of <em>Master volume</em> selector in Segment editor module to open the dialog where you can view/change current resolution.</p>

---
