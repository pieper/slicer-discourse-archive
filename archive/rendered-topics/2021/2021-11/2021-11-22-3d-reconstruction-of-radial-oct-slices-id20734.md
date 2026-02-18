# 3D reconstruction of radial OCT slices

**Topic ID**: 20734
**Date**: 2021-11-22
**URL**: https://discourse.slicer.org/t/3d-reconstruction-of-radial-oct-slices/20734

---

## Post #1 by @Soumaya (2021-11-22 19:02 UTC)

<p>Hi everyone!</p>
<p>I’m working on radial OCT scans of the optic nerve head (eye), and the slices are rotated from each other by 15°.<br>
Since I don’t have parallel slices, I’m struggling to construct the 3D model of the optic nerve head using those rotational slices. Is there a way that I could do it in 3D Slicer?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a807de4acbf0796e1343a1bb1a4be9ce9482b501.jpeg" data-download-href="/uploads/short-url/nYt4w2I0bW5IIBBFvfpntjIRrJT.jpeg?dl=1" title="radial_oct_scans" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a807de4acbf0796e1343a1bb1a4be9ce9482b501_2_511x500.jpeg" alt="radial_oct_scans" data-base62-sha1="nYt4w2I0bW5IIBBFvfpntjIRrJT" width="511" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a807de4acbf0796e1343a1bb1a4be9ce9482b501_2_511x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a807de4acbf0796e1343a1bb1a4be9ce9482b501_2_766x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a807de4acbf0796e1343a1bb1a4be9ce9482b501_2_1022x1000.jpeg 2x" data-dominant-color="B4AAAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">radial_oct_scans</span><span class="informations">1531×1498 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2021-11-23 07:11 UTC)

<p>Yes, that should be no problem at all. You can use the code snippet provided here:</p>
<aside class="quote quote-modified" data-post="4" data-topic="14598">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segmentation-of-mitral-valve/14598/4">Segmentation of Mitral valve</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" style="--category-badge-color: #F1592A; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="11" data-drop-close="true" class="badge-category --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
  </div>
  <blockquote>
    I had a look at the data set and tried all 3 methods. 
Method C does not work because slices intersect each other and therefore cannot be interpolated using a grid transform. 
Method B somewhat worked (I had to slightly improve the DICOM importer, the update will be available in tomorrow’s Slicer Preview Release). Since the the volume is quite sparse and the leaflet visibility is not always great, segmenting the leaflets like this can be quite challenging (you need to keep browsing the slices to…
  </blockquote>
</aside>

<p>You just need to set numberOfTimePoints to 1, as I guess your data set is a simple 3D volume (not a 3D+t volume sequence).</p>

---

## Post #3 by @Soumaya (2021-11-23 20:14 UTC)

<p>Hello,</p>
<p>Thank you so much for taking the time to answer my question.<br>
Yes exactly, I only need a 3D model with no time included.<br>
I tried the code snippet you provided and made sure that I have the extensions installed.<br>
I set numberOgTimePoints to 1, but I have an error of type : AttributeError: ‘NoneType’ object has no attribute ‘GetDataNodeAtValue’. Maybe there is a None value in the “inputVolumeSequenceNode”.<br>
Would you mind explaining why does this error arise so I can fix it?</p>
<p>Thank you again.</p>

---

## Post #4 by @lassoan (2021-11-23 22:23 UTC)

<p>As a starting point, you need to create a sequence node that contains each image slice and its correct position and orientation. This is done automatically if you read your images from an MRI scanner but if you just have a bunch of TIFF files then you need to put together the sequence manually.</p>
<p>First of all, you need to set the origin, spacing, and axis directions for each image slice. The origin is the physical position of one corner of the image, spacing is the size of one pixel, and axis directions are the directions of the x, y, and z (=cross(x,y)) axes of the image, using either the Transforms module, or using SetOrigin, SetSpacing, and SetIJKToRASDirections methods of each volume node. Once all the image slices have the correct geometry, you can put them into a sequence using either Python scripting, or using Sequences module: in Edit tab, choose Sequence → Create new sequence, select each node in the “Add remove data nodes” section, and click the green arrow button until all images are added to the sequence.</p>

---

## Post #5 by @Soumaya (2021-11-29 21:01 UTC)

<p>Thank you for providing the instructions.<br>
Using Transforms, I defined the rotation angle of each slice, then I created a sequence that contains all the slices. And I got no errors this time in the code you provided, but I don’t get the 3D volume. Am I missing a step?<br>
Also, I noticed, when I apply the rotation to each slice, only the last slice’s rotation is displayed (the other slices are not rotated even though I defined their rotation angle).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c3ff29fe4a4d46cdfc0695221c3802e0fa7422f.jpeg" data-download-href="/uploads/short-url/6js0ZZy0bcgzX9Q65rNi7TY68vt.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c3ff29fe4a4d46cdfc0695221c3802e0fa7422f_2_690x399.jpeg" alt="image" data-base62-sha1="6js0ZZy0bcgzX9Q65rNi7TY68vt" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c3ff29fe4a4d46cdfc0695221c3802e0fa7422f_2_690x399.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c3ff29fe4a4d46cdfc0695221c3802e0fa7422f_2_1035x598.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c3ff29fe4a4d46cdfc0695221c3802e0fa7422f.jpeg 2x" data-dominant-color="41424C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1219×706 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2021-11-30 00:19 UTC)

<aside class="quote no-group" data-username="Soumaya" data-post="5" data-topic="20734">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/96bed5/48.png" class="avatar"> Soumaya:</div>
<blockquote>
<p>I noticed, when I apply the rotation to each slice, only the last slice’s rotation is displayed (the other slices are not rotated even though I defined their rotation angle).</p>
</blockquote>
</aside>
<p>If you want to rotate the slice view along with the image slice then you can use Volume Reslice Driver module in SlicerIGT extension.</p>
<aside class="quote no-group" data-username="Soumaya" data-post="5" data-topic="20734">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/96bed5/48.png" class="avatar"> Soumaya:</div>
<blockquote>
<p>Using Transforms, I defined the rotation angle of each slice, then I created a sequence that contains all the slices. And I got no errors this time in the code you provided, but I don’t get the 3D volume. Am I missing a step?</p>
</blockquote>
</aside>
<p>What you have above is a 3D volume. You can see that near the center of rotation the gaps between the slices are filled. However, at the output resolution you have chosen the gap between slices gets way too big as you move away from the rotation center. Therefore, there is no way to meaningfully fill those gaps from the available information.</p>
<p>You can increase the size of the filled region if you lower the output resolution, but then of course the image will contain less details (will appear more blurry). Therefore, if you want to have a larger filled region without quality loss then you need to acquire more slices. For a reasonable sized 3D region I would recommend to acquire at least 5-10x more slices.</p>

---

## Post #7 by @AlexJ (2022-09-25 16:49 UTC)

<p>Hi,</p>
<p>I’m also trying to do 3D rendering of radial OCT scans.<br>
Is it also possible to determine a volume from several tif files in 3D Slicer?</p>
<p>I have tried to understand the protocol given here: I have arranged 24 images accordingly via “Transformers” (see figure), but I cannot display all images at the same time or display them as a volume.<br>
I can only edit one image via the segment editor, not all of them.</p>
<p>I would greatly appreciate any help with these problems.<br>
Thanks in advance.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b27015c95f627a59dceb9e01377f55127186087.png" data-download-href="/uploads/short-url/hzsir6Yj0MqI0SAQ9VOKcKQbrkr.png?dl=1" title="Bildschirmfoto 2022-09-25 um 15.03.59" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b27015c95f627a59dceb9e01377f55127186087_2_690x332.png" alt="Bildschirmfoto 2022-09-25 um 15.03.59" data-base62-sha1="hzsir6Yj0MqI0SAQ9VOKcKQbrkr" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b27015c95f627a59dceb9e01377f55127186087_2_690x332.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b27015c95f627a59dceb9e01377f55127186087_2_1035x498.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b27015c95f627a59dceb9e01377f55127186087_2_1380x664.png 2x" data-dominant-color="64637B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2022-09-25 um 15.03.59</span><span class="informations">1454×700 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
