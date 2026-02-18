# Segmentation / corner detection of grid intersection points in 3D image

**Topic ID**: 33361
**Date**: 2023-12-12
**URL**: https://discourse.slicer.org/t/segmentation-corner-detection-of-grid-intersection-points-in-3d-image/33361

---

## Post #1 by @G_Tom (2023-12-12 15:50 UTC)

<p>Hello,<br>
I have a 3D volume of a grid. I would like to detect the intersection points. I know if  it was a 2D image, I can run Corner Detection algorithm.<br>
however, in 3D what will be the equivalent, best approach ? the volume is shown below.</p>
<p>What I have tried is to threshold the image using segmentation editor and then use the segmentation module but the result is not ideal as can be seen in the second image below.</p>
<p>I am glad to hear any other suggestions.</p>
<p>Thanks</p>
<p>Image 1<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4752e208d52ed89a4f40f7902421828b8d728d1.jpeg" data-download-href="/uploads/short-url/pKp07WLUj7lnTK2TxlESaiklbQR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4752e208d52ed89a4f40f7902421828b8d728d1_2_689x397.jpeg" alt="image" data-base62-sha1="pKp07WLUj7lnTK2TxlESaiklbQR" width="689" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4752e208d52ed89a4f40f7902421828b8d728d1_2_689x397.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4752e208d52ed89a4f40f7902421828b8d728d1_2_1033x595.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4752e208d52ed89a4f40f7902421828b8d728d1.jpeg 2x" data-dominant-color="4A4A56"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1374×792 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Image 2<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3855527d973487ea93686c926073221b9a52bde5.jpeg" data-download-href="/uploads/short-url/82lxvd49dgYr1G1dcRlWEuEgnWZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3855527d973487ea93686c926073221b9a52bde5_2_690x285.jpeg" alt="image" data-base62-sha1="82lxvd49dgYr1G1dcRlWEuEgnWZ" width="690" height="285" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3855527d973487ea93686c926073221b9a52bde5_2_690x285.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3855527d973487ea93686c926073221b9a52bde5_2_1035x427.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/3855527d973487ea93686c926073221b9a52bde5_2_1380x570.jpeg 2x" data-dominant-color="717279"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1909×790 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks</p>
<p>GT</p>

---

## Post #2 by @G_Tom (2023-12-12 15:57 UTC)

<p>I should add that volume rendering shows a nice visualization of the intersection points but how do I obtain those points ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3a302a5aed2f1d6c2ab171494699c4dd6de6f6e.jpeg" data-download-href="/uploads/short-url/wtLDisRHuikYoIqBqsmPN7DohaK.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3a302a5aed2f1d6c2ab171494699c4dd6de6f6e.jpeg" alt="image" data-base62-sha1="wtLDisRHuikYoIqBqsmPN7DohaK" width="615" height="500" data-dominant-color="887D94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">738×600 50.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @mikebind (2023-12-12 17:48 UTC)

<p>It looks like thresholding did a pretty reasonable job of picking out intersection regions.  You could continue that approach by using the Islands effect to split each separate clump of voxels into separate segments, and then Segment Statistics module to automatically find the centroid of each segment.  Lastly, if you wanted to visualize those points in a uniform way, you could create a Markups Point List with control points at all the segment centroids.  A simple python script could automate these steps for you if it is something you would be doing regularly.</p>
<p>However, if your goal is just to visualize a regular grid of points in 3D, it seems like it would be easier to just calculate them (e.g. using numpy) and then display.  What is your ultimate goal?<br>
There might be other ways to achieve it.</p>

---

## Post #4 by @G_Tom (2023-12-12 19:33 UTC)

<p>Hello Mikebind,<br>
Thanks for your response. So this is a CT image of a grid phantom. I want to compare grid intersection points from the image to those of a 3d model of the phantom.<br>
Yes, the thresholding and segmentation approach is what I am working on now. Although, I am not sure how to improve the thresholding and wondered if there is a better approach.<br>
Are there some filters to apply before the thresholding to improve the result ?</p>
<p>Thanks</p>

---

## Post #5 by @mikebind (2023-12-12 20:48 UTC)

<p>You could try a Gaussian blur.  I would expect those intersection points to remain local peaks in even a pretty strongly blurred image, so maybe you would find a thresholded version of a blurred image to be of satisfactory quality.  Are you attempting to find the center point of each intersection?  You could find the voxel coordinates of the highest voxel value in each region after blurring.  That would be somewhat robust to the problem of needing a non-uniform threshold, if the different sizes of islands is what is troubling you about the segmentation you have or might get after blurring and thresholding.</p>

---

## Post #6 by @G_Tom (2023-12-12 22:35 UTC)

<p>Hi, thanks for your reply. Yes my end goal is I want to find the center point of  each intersection point.<br>
The gaussian smoothing is fine but the thresholding is not always constant.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc609cc68753812b293042f85b3740f4f95c2ed7.jpeg" data-download-href="/uploads/short-url/qSsKQoxjraYeCCBZNBajnBfV1oX.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc609cc68753812b293042f85b3740f4f95c2ed7_2_690x427.jpeg" alt="image" data-base62-sha1="qSsKQoxjraYeCCBZNBajnBfV1oX" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc609cc68753812b293042f85b3740f4f95c2ed7_2_690x427.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc609cc68753812b293042f85b3740f4f95c2ed7_2_1035x640.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc609cc68753812b293042f85b3740f4f95c2ed7.jpeg 2x" data-dominant-color="4C4C58"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1272×788 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
But the result is still not ideal due to non uniform intensity across the image. You can see some areas where the intersection points are joined.<br>
At this rate I wonder if I should have  a different approach ? 3D Hough lines then  find intersection of the lines ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55752ea7b515db61a3267fef3bfbd21acaf40a46.jpeg" data-download-href="/uploads/short-url/cbZE6gZ7DvPhJWj0OoaJzNJmKCq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55752ea7b515db61a3267fef3bfbd21acaf40a46_2_690x285.jpeg" alt="image" data-base62-sha1="cbZE6gZ7DvPhJWj0OoaJzNJmKCq" width="690" height="285" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55752ea7b515db61a3267fef3bfbd21acaf40a46_2_690x285.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55752ea7b515db61a3267fef3bfbd21acaf40a46_2_1035x427.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55752ea7b515db61a3267fef3bfbd21acaf40a46_2_1380x570.jpeg 2x" data-dominant-color="7B7D83"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1915×793 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is there a 3D Hough lines implementation ? Do you know ?<br>
Thanks</p>

---
