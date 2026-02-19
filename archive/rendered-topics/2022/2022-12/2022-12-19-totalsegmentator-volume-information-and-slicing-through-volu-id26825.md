---
topic_id: 26825
title: "Totalsegmentator Volume Information And Slicing Through Volu"
date: 2022-12-19
url: https://discourse.slicer.org/t/26825
---

# Totalsegmentator - volume information and slicing through volumes?

**Topic ID**: 26825
**Date**: 2022-12-19
**URL**: https://discourse.slicer.org/t/totalsegmentator-volume-information-and-slicing-through-volumes/26825

---

## Post #1 by @a.mohseni (2022-12-19 16:09 UTC)

<p>Operating system: Windows 11 Pro<br>
Slicer version: 5.2.1</p>
<p>Hello,</p>
<p>So I have been using the 3DSlicer and Totalsegmentator extension recently for the segmentation of the abdominal organs in a CT-abdomen scan, but I have the following questions:</p>
<p>-After automatically segmenting the liver, the liver is displayed in 3D-space, but is this just a surface mark-up or is there also information on the inside? So in other words is the liver volumetrically segmentated? Is there any data on the contents of the liver that can be used?</p>
<p>-I tried using the volume rendering function and selected a region of interest inside the 3 different views of the CT, which also displayed itself on the 3D model of the liver. Is there a way to slice through the liver so to speak, to see the parenchyma on the inside?</p>
<p>So what our research group wants to achieve is the following: Segmenting liver organs and their injuries → the injuries are mostly on the inside of the liver parenchyma so we would like to see the inside of the liver aswell or atleast slice through the liver in 3D space if possible → then we would export this segmentation for further annotation of the injuries.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2022-12-19 16:13 UTC)

<aside class="quote no-group" data-username="a.mohseni" data-post="1" data-topic="26825">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f1d935/48.png" class="avatar"> a.mohseni:</div>
<blockquote>
<p>After automatically segmenting the liver, the liver is displayed in 3D-space, but is this just a surface mark-up or is there also information on the inside?</p>
</blockquote>
</aside>
<p>It is not just a surface markup, segments are real, solid, 3D objects.</p>
<aside class="quote no-group" data-username="a.mohseni" data-post="1" data-topic="26825">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f1d935/48.png" class="avatar"> a.mohseni:</div>
<blockquote>
<p>So in other words is the liver volumetrically segmentated?</p>
</blockquote>
</aside>
<p>Yes.</p>
<aside class="quote no-group" data-username="a.mohseni" data-post="1" data-topic="26825">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f1d935/48.png" class="avatar"> a.mohseni:</div>
<blockquote>
<p>Is there any data on the contents of the liver that can be used?</p>
</blockquote>
</aside>
<p>You can use segments in many different ways. You can get each segment as a 3D numpy array, as a surface mesh, as a volumetric mesh, compute volume, surface, bounding box, shape and intensity statistics, etc., all by 1-2 clicks. <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">This page</a> is a good starting point and feell free to ask more questions here.</p>
<aside class="quote no-group" data-username="a.mohseni" data-post="1" data-topic="26825">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f1d935/48.png" class="avatar"> a.mohseni:</div>
<blockquote>
<p>So what our research group wants to achieve is the following: Segmenting liver organs and their injuries → the injuries are mostly on the inside of the liver parenchyma so we would like to see the inside of the liver aswell or atleast slice through the liver in 3D space if possible → then we would export this segmentation for further annotation of the injuries.</p>
</blockquote>
</aside>
<p>This should be no problem at all. You can move he camera inside the liver or export the segment to a model and use clip feature of Models module or clip the mesh using Dynamic modeler module.</p>

---

## Post #3 by @rbumm (2022-12-19 16:17 UTC)

<p>That should be possible.</p>
<p>The TotalSegmentator liver is segmented in 3D space and you could use this segmentation in the Segment Editor to → Mask Volume and just show the damaged liver parenchyma.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a753c894912e6e40411fe8c1055b89653283e7f.png" alt="image" data-base62-sha1="8l8S18Ertg6L2qy82ZlnJgsU1rN" width="343" height="451"></p>
<p>You could then “volume render” the masked volume.</p>

---

## Post #4 by @a.mohseni (2022-12-19 16:31 UTC)

<p>Thanks for the elaborate and fast answers, much appreciated!</p>
<p>So I’m reading documentation right now for how to slice through the liver. I tried to export the liver as a model and clip through it as one of our injuries is located in the medial part of the liver (vascular injury) and these can not be seen on the outside. That region would be my ROI which then would be exported as a mesh file. Are there any instructions or guides on how to do this more explicitly?</p>
<p>What would be the best format for my use case, voumetric mesh or 3D numpy array?</p>

---

## Post #5 by @a.mohseni (2022-12-19 16:51 UTC)

<p>And another question i had, is this possible in combination with Totalsegmentator or would I have to use separate extensions or workflows?</p>

---

## Post #6 by @rbumm (2022-12-19 17:08 UTC)

<p>A very quick take on this: Run TotalSegmentator on the low-resolution CTAAbdomen demo dataset, then “Mask volume”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a002bc1b44271353b50e59c1cc58e895b2cfd278.png" data-download-href="/uploads/short-url/mPwfMqJvdoVmM8kTaDqUUM3neME.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a002bc1b44271353b50e59c1cc58e895b2cfd278_2_690x290.png" alt="image" data-base62-sha1="mPwfMqJvdoVmM8kTaDqUUM3neME" width="690" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a002bc1b44271353b50e59c1cc58e895b2cfd278_2_690x290.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a002bc1b44271353b50e59c1cc58e895b2cfd278_2_1035x435.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a002bc1b44271353b50e59c1cc58e895b2cfd278_2_1380x580.png 2x" data-dominant-color="77757B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1906×802 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>then use volume rendering of the cropped volume to get an overview of the vascular structures (quite poor in this example due to low resolution, missing contrast medium and limited laptop GPU). You may need to add a bit of liver segmentation volume manually to the central part of the liver to add vessels in the hepatic ligament.</p>
<p></p><div class="video-placeholder-container" data-video-src="/404" data-orig-src="upload://6ijgJicDmPFNA1Y6ugBwdNrHVuK.mp4">
  </div><p></p>

---

## Post #7 by @a.mohseni (2022-12-19 17:42 UTC)

<p>I followed the steps you described and I got to the part where I could use the “Shift” option, but for me it only functions as a binary tool, either it shows the whole liver or it blacks out the whole screen. Is there another solution for this?</p>
<p>I’m using Contrast-enhanced CT-abdomen scans with a slice thickness of 1.0 mm, the active bleeding (or other vascular injury) is mostly in the parenchyma so this view you are showing in the video would be ideal, but could I also use another preset?</p>
<p>And how could I export the segment of the liver that contains the vascular injury? So basically I want to isolate the injury so it could be annotated in another application.</p>

---

## Post #8 by @rbumm (2022-12-19 18:28 UTC)

<p>This is really a bit hidden:</p>
<p>Please use these sliders in the “Advanced” → “Scalar Opacity Mapping”, put them closer together:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/399845da918ecb17666c07d8f1b3fa275d330269.png" alt="image" data-base62-sha1="8dvss7bgWDuQ1MlwsnYAlNXzJNv" width="379" height="471"></p>
<p>to make the “Shift” slider less responsive.<br>
Of course, you could try other presets from all of those available.</p>

---

## Post #9 by @rbumm (2022-12-19 18:34 UTC)

<aside class="quote no-group" data-username="a.mohseni" data-post="7" data-topic="26825">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f1d935/48.png" class="avatar"> a.mohseni:</div>
<blockquote>
<p>And how could I export the segment of the liver that contains the vascular injury?</p>
</blockquote>
</aside>
<p>This technique is volume rendering only - not a “real” vessel or structure segmentation that you could export into a 3D viewer or 3D postprocessing.</p>

---

## Post #10 by @lassoan (2022-12-19 18:43 UTC)

<aside class="quote no-group" data-username="a.mohseni" data-post="7" data-topic="26825">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f1d935/48.png" class="avatar"> a.mohseni:</div>
<blockquote>
<p>And how could I export the segment of the liver that contains the vascular injury? So basically I want to isolate the injury so it could be annotated in another application.</p>
</blockquote>
</aside>
<p>It might be simpler to do everything at one place and do all the additional annotation, analysis, quantification in Slicer, too. If you tell us a bit more details about what you want to do then we can suggest solutions for those in Slicer. There are of course various ways for exporting the data, too.</p>

---

## Post #11 by @a.mohseni (2022-12-20 16:26 UTC)

<p>So what we want to achieve is the following:<br>
After loading a DICOM file (Contrast Enhanced CT-Abdomen in our case) we would like to visualize the liver. The totalsegmentator does this adequately, but then we would like to “slice” through the visualized liver as if it were a CT-scan in axial/coronal/saggital view.</p>
<p>Vascular injuries will mostly be on the inside of the liver tissue, so we need to see the inside of the liver to annotate or if you will mark it with some kind of marking/annotation tool. This would then hopefully create a 3-dimensional marked region inside of the liver. We already know where the injury is on the CT-scan and we can pinpoint it using the markers to align all 3 views. So it would be great if that place (marked as ROI perhaps) would be shown in the 3D view or if we could navigate to it. We would then want to export that as mesh-data or voxel-based data.</p>
<p>I hope this makes our use case a bit more clear</p>

---

## Post #12 by @a.mohseni (2022-12-20 21:45 UTC)

<p>So right now I’ve managed to slice through the 3D model and annotate a 3-dimensional region of the liver (a cube now shows in the 3D view), how can i export these coordinates or annotated data?</p>

---

## Post #13 by @lassoan (2022-12-20 23:53 UTC)

<aside class="quote no-group" data-username="a.mohseni" data-post="11" data-topic="26825">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f1d935/48.png" class="avatar"> a.mohseni:</div>
<blockquote>
<p>The totalsegmentator does this adequately, but then we would like to “slice” through the visualized liver as if it were a CT-scan in axial/coronal/saggital view</p>
</blockquote>
</aside>
<p>This is the default behavior. Let us know if you don’t see the the segmentation and the input image in the slice views or you have trouble navigating the slices.</p>
<aside class="quote no-group" data-username="a.mohseni" data-post="11" data-topic="26825">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f1d935/48.png" class="avatar"> a.mohseni:</div>
<blockquote>
<p>Vascular injuries will mostly be on the inside of the liver tissue, so we need to see the inside of the liver to annotate or if you will mark it with some kind of marking/annotation tool.</p>
</blockquote>
</aside>
<p>In Slicer we call this process <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">image segmentation</a> and we have a very powerful, dedicated module for this, the Segment Editor. It has many manual and semi-automatic tools that you can use to mark vessels, lesions, etc. Segmented regions are automatically, immediately displayed in all slice views and also in the 3D view.</p>
<aside class="quote no-group" data-username="a.mohseni" data-post="11" data-topic="26825">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f1d935/48.png" class="avatar"> a.mohseni:</div>
<blockquote>
<p>it would be great if that place (marked as ROI perhaps) would be shown in the 3D view or if we could navigate to it. We would then want to export that as mesh-data or voxel-based data.</p>
</blockquote>
</aside>
<p>You can do all these. We developed segmentation modules for exactly these purposes. If the documentation and tutorials are not clear enough then you can post specific questions on this forum anytime.</p>
<aside class="quote no-group" data-username="a.mohseni" data-post="12" data-topic="26825">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f1d935/48.png" class="avatar"> a.mohseni:</div>
<blockquote>
<p>a cube now shows in the 3D view</p>
</blockquote>
</aside>
<p>If you have trouble making volume rendering to show useful information by following <a class="mention" href="/u/rbumm">@rbumm</a>’s excellent advices above, then you may just give up on that and hide the volume rendering, by going to Data module, right-clicking on the eye icon in the row of the input volume node, and uncheck <code>Show in 3D views as volume rendering</code> checkbox.</p>

---

## Post #14 by @a.mohseni (2022-12-21 12:21 UTC)

<p>Thanks for all the helpful answers, it helped me out a lot. Now if I want to export this information (the ROI i pointed out using a 3D box) in mesh format or any other format, how do i do that? I skimmed through the documentation you linked but I couldn’t find it. I will try to look into it later today.</p>

---

## Post #15 by @lassoan (2022-12-21 13:01 UTC)

<p>See instructions for exporting segmentation to mesh or image files <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-model-surface-mesh-file">here</a>.</p>
<p>What kind of analysis would you like to perform on the segmentations?</p>
<p>Slicer has hundreds of analysis tools and a full Python environment that allows using any Python packages or custom Python scripts, so most likely you can conveniently perform the analysis you need and display the result in Slicer.</p>

---
