---
topic_id: 11293
title: "New Module For Measuring Cross Section Area Of Segments"
date: 2020-04-24
url: https://discourse.slicer.org/t/11293
---

# New module for measuring cross-section area of segments

**Topic ID**: 11293
**Date**: 2020-04-24
**URL**: https://discourse.slicer.org/t/new-module-for-measuring-cross-section-area-of-segments/11293

---

## Post #1 by @lassoan (2020-04-24 15:45 UTC)

<p>A new module - “Segment cross-section area” - has been added to Slicer. It can compute cross-sectional area of segmented structures along a chosen axis direction. Results are available both as a table and can be shown in a plot, too. Short demo video:</p>
<div class="lazyYT" data-youtube-id="G8wZl9mLWtU" data-youtube-title="Cross-sectional area computation in segmented image" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>For now, the module is available by installing “Sandbox” extension in the extension manager in a recent 3D Slicer Preview Release.</p>
<p>If you have any comments and suggestions then please post it here.</p>

---

## Post #2 by @Vito (2020-05-17 10:16 UTC)

<p>Hello Professor Lasso, I want to calculate the cross-sectional area of the area of interest, how can I calculate</p>

---

## Post #3 by @lassoan (2020-05-17 14:11 UTC)

<p>Follow the steps that are shown in the video above and let us know if you encounter any problems.</p>

---

## Post #5 by @S_Jo (2020-08-12 04:45 UTC)

<p>I have tried the method following instructions, but I do not get area.  I get positions, not even sure what this means.  Your instruction video also shows volume (cm^3), not area (cm^2).  Is this an error? Or do I need to divide by slice thickness?  Is there a way to convert when I am not exactly sure of slice thickness (varies by scanners in real life patients)? Also, how is this different from segment statistics?</p>

---

## Post #6 by @muratmaga (2020-08-12 05:41 UTC)

<p>Please watch the whole video, the table you want is at the end. The initial table is the output from segment statistics which reports volumes (so in cm3).</p>
<p>CA of segments reports cross-sectional area in a slice-by-slice manner. Positions you refer to can be  the slice number (but see below). And the other value is the cross-sectional area.</p>
<p>If you want to get a more in-depth understanding of what the module does, I suggest experimenting with the module more. For example, segment a structure of interest in one slice. Then run the CA module and I think you will find it fairly easy to interpret results (every other slice apart from your segmentation will have 0s, and you will a single spike in the plot). The only confusion you may have is that volume axis is referred as row, column and slice (as oppose to axial, sagittal, or coronal, or X, Y or Z). But if you do the exercise I suggest, you will quickly find out which one corresponds to your segmentation plane.</p>

---

## Post #7 by @S_Jo (2020-08-13 01:42 UTC)

<p>Thank you for the reply.  Now I understand. I was very confused on the position column.  I need to scroll down to the correct slice number to see my measurement.   Are the units in mm2 if I used DICOM files?</p>

---

## Post #8 by @muratmaga (2020-08-13 01:59 UTC)

<p>Default units in Slicer is mm. So I reported values should in mm2. But again, when in doubt, the best thing is to test with something know. For example, you can segment a 10mm radius circle (with the paint tool) and be certain about what units its being reported at…</p>

---

## Post #9 by @S_Jo (2020-08-13 02:21 UTC)

<p>Thank you for the suggestion!</p>

---

## Post #10 by @lassoan (2020-08-13 14:02 UTC)

<p>Also note that in the table you get RAS position of the center of the slicing plane. Anatomical orientations (axial, sagittal, coronal) are not used because cross-section axes are not aligned with anatomical planes but with volume axes (which may or may not coincide with anatomical directions).</p>

---

## Post #11 by @Juan (2020-09-02 22:40 UTC)

<p>Good afternoon,</p>
<p>I want to calculate area and volume´s segments with 3D slice. I have installed Sandbox extension with the extension manager but I still can see the “segment cross-section area” in the Quantification part in modules.</p>
<p>How could I fix it?</p>
<p>Many thanks in advance.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7de206e79b7c973c7b9696702f36470b2015154.jpeg" alt="Screen Shot 2020-09-02 at 18.37.20" data-base62-sha1="x5ccoquxbVxCpQO2RZHvHkYOKzO" width="682" height="280"></p>

---

## Post #12 by @lassoan (2020-09-02 22:42 UTC)

<p>It is available for recent Slicer Preview Releases.</p>

---

## Post #13 by @Juan (2020-09-03 13:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="11293">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>recent Slicer Preview Releases.</p>
</blockquote>
</aside>
<p>Thank you for your response.</p>
<p>I tried with 4.11.10 version and it is not available this module.</p>

---

## Post #14 by @lassoan (2020-09-03 13:50 UTC)

<p>You can follow these steps:</p>
<ul>
<li>Install latest Slicer Preview Release (if you do it between 12am-11am EST then you can <a href="https://download.slicer.org/?offset=-1">download the release created the day before</a>, to make sure that all extension builds are completed).</li>
<li>Install Sandbox extension (you may need to choose Examples category to see it)</li>
<li>Wait for the “Restart” button to become active and click it to restart the application</li>
<li>Find “Segment cross-section area module” using the module finder</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf8424d87c66944addc40b648eae054f61a6d34d.png" data-download-href="/uploads/short-url/rkejsH546rXBnB1TOYqC4QNFY0l.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf8424d87c66944addc40b648eae054f61a6d34d_2_690x412.png" alt="image" data-base62-sha1="rkejsH546rXBnB1TOYqC4QNFY0l" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf8424d87c66944addc40b648eae054f61a6d34d_2_690x412.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf8424d87c66944addc40b648eae054f61a6d34d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf8424d87c66944addc40b648eae054f61a6d34d.png 2x" data-dominant-color="5F6264"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">936×559 41.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @Hamid (2021-06-28 21:42 UTC)

<p>I am working with Slicer 4.11.20200930 but there is not Sandbox in extension?!!</p>

---

## Post #16 by @lassoan (2021-06-28 21:44 UTC)

<p>You can find it in the “Examples” category. However, you need to use at least the latest stable release (currently Slicer 4.11.20210226).</p>

---

## Post #17 by @Hamid (2021-06-28 21:48 UTC)

<p>Thank you so much.<br>
1-Where is the “Example” category?<br>
2- I want to get the cross section area of a cannula tube which is not  circle? does it work for me?</p>

---

## Post #18 by @Hamid (2021-06-28 21:57 UTC)

<p>Many thanks Lassoan. Found it</p>

---

## Post #19 by @Hamid (2021-06-28 22:05 UTC)

<p>I get the plot. What is the slice index in the plot? How can I find the desired cross section area of my volume? is there any connection between the plot and views?</p>

---

## Post #20 by @lassoan (2021-06-28 22:33 UTC)

<p>The cross-sectional area works for any cross-section shape.</p>
<p>Slice index is the voxel index of the selected “Volume” node (). You can get physical (RAS coordinate system, unit in mm) coordinates of the cross-sections in the “Position” column of the table.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a078fed24d3d837c45172e1dcf49cb2efff5beec.png" data-download-href="/uploads/short-url/mTBCR5ivDb3RlV0N7wvWsTkTODa.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a078fed24d3d837c45172e1dcf49cb2efff5beec_2_246x500.png" alt="image" data-base62-sha1="mTBCR5ivDb3RlV0N7wvWsTkTODa" width="246" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a078fed24d3d837c45172e1dcf49cb2efff5beec_2_246x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a078fed24d3d837c45172e1dcf49cb2efff5beec_2_369x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a078fed24d3d837c45172e1dcf49cb2efff5beec_2_492x1000.png 2x" data-dominant-color="F1EEE7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">660×1337 52.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #21 by @sarah11pete (2021-10-22 19:11 UTC)

<p>Hello - I would also like to determine the cross-sectional area of the region I identified using Segment Editor.  I can’t find the Sandbox extension - has it been renamed?</p>
<p>Thanks!</p>

---

## Post #22 by @lassoan (2021-10-23 15:36 UTC)

<p>It has not been renamed. It might have been a temporary issue with the extension manager server. Try again now. I would recommend to use the latest Slicer Preview Release.</p>
<p>You may also find useful the much more advanced <a href="https://github.com/jmhuie/Slicer-SegmentGeometry#segment-geometry">SegmentGeometry extension</a>.</p>
<p>If you need to measure diameter of long thin structures (such as blood vessels or nerves) along a curved trajectory then you can use Cross-section analysis module in <a href="https://github.com/vmtk/SlicerExtension-VMTK">SlicerVMTK extension</a>.</p>

---

## Post #23 by @lassoan (2021-12-01 18:56 UTC)

<p>A post was merged into an existing topic: <a href="/t/change-shell-thickness/15081/6">Change shell thickness</a></p>

---

## Post #24 by @AmandineG (2023-02-01 10:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="11293">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It can compute cross-sectional area of segmented structures along a chosen axis direction</p>
</blockquote>
</aside>
<p>Hi!</p>
<p>I tried your method after tilting my axial line in the axis of the intervertebral disc, but in the Segment Cross-Section Area tool table, it actually corresponds to several slices.<br>
However, in the sagittal image, we can see that the “stairs” of slices in my axial view overlap. The area of my surface of interest cannot therefore correspond to the sum of the 2 slices composing it.</p>
<p>For example, if we take the last column of the table which corresponds to the surface of the L2L3 intervertebral disc, it is composed of slices number 99 and 100 because of the tilt. But as these 2 slices overlap on the sagittal section (see image and red circle), my surface cannot be equal to 1138.47+1025.41, it will be overestimated because of the overlap.</p>
<p>How can I get an exact surface of my chosen axial slice after tilting?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c55c9e07ea73260a6a26610acb11799180c6495.jpeg" data-download-href="/uploads/short-url/hJV0sVhCTnQn3x15Q9TVY777TbT.jpeg?dl=1" title="Capture d’écran 2023-02-01 à 11.17.06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c55c9e07ea73260a6a26610acb11799180c6495_2_690x431.jpeg" alt="Capture d’écran 2023-02-01 à 11.17.06" data-base62-sha1="hJV0sVhCTnQn3x15Q9TVY777TbT" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c55c9e07ea73260a6a26610acb11799180c6495_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c55c9e07ea73260a6a26610acb11799180c6495_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c55c9e07ea73260a6a26610acb11799180c6495_2_1380x862.jpeg 2x" data-dominant-color="A6A7A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2023-02-01 à 11.17.06</span><span class="informations">1440×900 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks</p>

---

## Post #25 by @chir.set (2023-02-01 12:03 UTC)

<aside class="quote no-group" data-username="AmandineG" data-post="24" data-topic="11293">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/8edcca/48.png" class="avatar"> AmandineG:</div>
<blockquote>
<p>after tilting</p>
</blockquote>
</aside>
<p>You might consider “<a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/StenosisMeasurement2D.md" rel="noopener nofollow ugc">Stenosis measurement: 2D</a>” module in SlicerVMTK. It is designed for a specific context, but can calculate the surface area of any segment cut at an arbitrary location and orientation. However, the segment must not be one single slice thick. You might paint the whole intervertebral disk, reslice and follow the instructions. Hope it helps.</p>

---

## Post #26 by @chir.set (2023-02-02 08:44 UTC)

<aside class="quote no-group" data-username="AmandineG" data-post="24" data-topic="11293">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/8edcca/48.png" class="avatar"> AmandineG:</div>
<blockquote>
<p>get an exact surface</p>
</blockquote>
</aside>
<p>A quicker solution would be drawing a ‘Closed curve’ and get the surface area in the Markups module’s widget. Slice orientation is not an issue here. You may even generate the enclosed model using ‘Baffle planner’ in SlicerHeart extension.</p>

---

## Post #27 by @lassoan (2023-02-02 09:45 UTC)

<aside class="quote no-group" data-username="AmandineG" data-post="24" data-topic="11293">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/8edcca/48.png" class="avatar"> AmandineG:</div>
<blockquote>
<p>I tried your method after tilting my axial line in the axis of the intervertebral disc, but in the Segment Cross-Section Area tool table, it actually corresponds to several slices.</p>
</blockquote>
</aside>
<p>This module requires complete segmentation on at least one non-oblique slice. In the screenshot above you have only segmented half of the structure on 2 slices, so you are not getting correct results.</p>
<p>Both suggestions of <a class="mention" href="/u/chir.set">@chir.set</a> are excellent. Summarizing your options:</p>
<ul>
<li>If you need cross-section of the disc in <strong>one or more axial slice(s)</strong> then you can segment the slice(s) completely and use the “Segment Cross-Section Area” module.</li>
<li>If you need cross-section in <strong>oblique slices</strong> then you can segment several consecutive slices (so that the complete intersection of the disc and the cutting plane is segmented) and use Cross-section analysis or Stenosis measurement modules in VMTK extension.</li>
<li>If you only need to measure cross-section area in a <strong>single slice</strong> (either axial oblique) then you can use a closed curve (enable area measurement in Measurements section).</li>
</ul>

---

## Post #28 by @AmandineG (2023-02-08 17:49 UTC)

<p>Thank you all for your suggestions! It worked well with Stenosis measurement modules in VMTK extension.</p>

---

## Post #29 by @AmandineG (2023-02-09 17:26 UTC)

<p>Hi,</p>
<p>I was able to apply your method on my MRI to obtain the area of a homogeneous surface.<br>
But is it possible to apply this method to a heterogeneous surface (total muscle separated into fat and muscle)?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf9b3e5477a5a801012a424019ea754e325834fd.jpeg" data-download-href="/uploads/short-url/tCzrwIWqtHTHkAGsx1ojfypjsrb.jpeg?dl=1" title="Capture d’écran 2023-02-09 à 17.42.45" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf9b3e5477a5a801012a424019ea754e325834fd_2_517x323.jpeg" alt="Capture d’écran 2023-02-09 à 17.42.45" data-base62-sha1="tCzrwIWqtHTHkAGsx1ojfypjsrb" width="517" height="323" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf9b3e5477a5a801012a424019ea754e325834fd_2_517x323.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf9b3e5477a5a801012a424019ea754e325834fd_2_775x484.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf9b3e5477a5a801012a424019ea754e325834fd_2_1034x646.jpeg 2x" data-dominant-color="ABA9AB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2023-02-09 à 17.42.45</span><span class="informations">1440×900 265 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I tried several ways and the results are not identical (despite an identical threshold) because the heterogeneous surface is made of several separate pixel islands.</p>
<p>Initially, I had obtained my surface value via another technique.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d986e01410c30baa5e954ef3e4cb6316dd3daf2.png" data-download-href="/uploads/short-url/b4rllJN8FcLLRthNoUuqArHdy26.png?dl=1" title="ValeursCSAMFDWhiteDIVL2L3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d986e01410c30baa5e954ef3e4cb6316dd3daf2_2_517x323.png" alt="ValeursCSAMFDWhiteDIVL2L3" data-base62-sha1="b4rllJN8FcLLRthNoUuqArHdy26" width="517" height="323" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d986e01410c30baa5e954ef3e4cb6316dd3daf2_2_517x323.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d986e01410c30baa5e954ef3e4cb6316dd3daf2_2_775x484.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d986e01410c30baa5e954ef3e4cb6316dd3daf2_2_1034x646.png 2x" data-dominant-color="7D7E84"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ValeursCSAMFDWhiteDIVL2L3</span><span class="informations">1440×900 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bec3d17a32069ea65f3b293511c8e48e7e659769.png" data-download-href="/uploads/short-url/rdAg07pGI233Syql1V75RkTp81z.png?dl=1" title="ValeursCSAMFGWhiteDIVL2L3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bec3d17a32069ea65f3b293511c8e48e7e659769_2_517x323.png" alt="ValeursCSAMFGWhiteDIVL2L3" data-base62-sha1="rdAg07pGI233Syql1V75RkTp81z" width="517" height="323" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bec3d17a32069ea65f3b293511c8e48e7e659769_2_517x323.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bec3d17a32069ea65f3b293511c8e48e7e659769_2_775x484.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bec3d17a32069ea65f3b293511c8e48e7e659769_2_1034x646.png 2x" data-dominant-color="7E7F86"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ValeursCSAMFGWhiteDIVL2L3</span><span class="informations">1440×900 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>With your technique, if I check or uncheck “limited to cloest islands”, it gives me even more values.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2da4e57f2056aa42b4575c0d4e45244ddfd71da8.jpeg" data-download-href="/uploads/short-url/6vMM3Z1WFm9rGREoE7Pi1GRg8Mo.jpeg?dl=1" title="Capture d’écran 2023-02-09 à 17.36.10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2da4e57f2056aa42b4575c0d4e45244ddfd71da8_2_517x323.jpeg" alt="Capture d’écran 2023-02-09 à 17.36.10" data-base62-sha1="6vMM3Z1WFm9rGREoE7Pi1GRg8Mo" width="517" height="323" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2da4e57f2056aa42b4575c0d4e45244ddfd71da8_2_517x323.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2da4e57f2056aa42b4575c0d4e45244ddfd71da8_2_775x484.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2da4e57f2056aa42b4575c0d4e45244ddfd71da8_2_1034x646.jpeg 2x" data-dominant-color="B0AEAF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2023-02-09 à 17.36.10</span><span class="informations">1440×900 252 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I can’t find a reliable method that will allow me to obtain the area of fat in the total muscle.</p>
<p>Thanks</p>

---

## Post #30 by @lassoan (2023-02-09 17:32 UTC)

<p>If the object you quantify is not a single solid shape then “Segment Cross-Section Area” module may be a better choice, because stenosis analysis extracts and quantifies a single branch (the one that is closest to the centerline curve).</p>

---

## Post #31 by @AmandineG (2023-02-09 18:09 UTC)

<p>Yes but “Segment Cross-Section Area” module doesn’t work with the fiducial node allowing me to keep a modified axis.</p>
<p>If I eliminate the confounding factors around the volume I am interested in, i.e. if I isolate the fat muscle volume with the “Mask volume” tool and study it separately, would it work better? Or would the islands still be a problem?</p>

---

## Post #32 by @chir.set (2023-02-09 18:23 UTC)

<p>You have many lines because “Apply to all segments” is checked. (Please note it refers to visible segments).</p>
<p>If you uncheck “Limit to closest island(s)”, you should be able to get a section as below for each segment (only one is shown here for clarity).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5042d5e2b024faf304ac5644054496327f75c43b.png" alt="11293_0" data-base62-sha1="bs1oiTKWLZmMgoJ8sl5PIWdPa2v" width="624" height="424"></p>
<p>Is it what you are expecting ? Can you share the segmentation node only for more real troubleshooting ?</p>
<p>As <a class="mention" href="/u/lassoan">@lassoan</a> said, and as I mentioned above, this module is designed for a specific context. Nevertheless, it should he helpful for you, as far as I understand.</p>
<p>What is fat and what is muscle in your pictures ? Do you want sections of muscle without fat and fat without muscle ?</p>

---

## Post #33 by @AmandineG (2023-02-13 16:49 UTC)

<p>“You have many lines because “Apply to all segments” is checked”<br>
Yes, it’s intentional.</p>
<p>“If you uncheck “Limit to closest island(s)”, you should be able to get a section as below for each segment (only one is shown here for clarity).”<br>
When I uncheck “Limit to closest island(s)”, the given area varies according to the location of my fiducial node, for the same axial plane I have chosen.</p>
<p>I want to know the area of the green surface on this image for example, according to an axis that I have chosen (fiducial node), and that would take into account all the pixels islands (including isolated ones).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c638a1f1e068568e78df7457e0400c0ba5638d4b.png" alt="Capture d’écran 2023-01-31 à 14.57.45 copie" data-base62-sha1="shxSbnBpt8ZJHkXWuALdXXy21GH" width="441" height="306"></p>
<p>In your image, the green areas are all connected, none is isolated.</p>
<p>“What is fat and what is muscle in your pictures ?”<br>
In the first image of my previous post, red and brown correspond to fat, yellow and blue to muscle.</p>
<p>“Do you want sections of muscle without fat and fat without muscle?”<br>
I especially want to be able to calculate the area of fat and the area of muscle separately in a chosen axial plane, whether they are visualized together or separately on my model (on the image here, only the fat is visualized).</p>
<p>Thanks</p>

---

## Post #34 by @chir.set (2023-02-13 18:05 UTC)

<aside class="quote no-group" data-username="AmandineG" data-post="33" data-topic="11293">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/8edcca/48.png" class="avatar"> AmandineG:</div>
<blockquote>
<p>the given area varies according to the location of my fiducial node, for the same axial plane I have chosen</p>
</blockquote>
</aside>
<p>If you move the Fiducial point in the selected slice view with the same slice orientation, the result should not change.</p>
<p>If you move the Fiducial point in another slice view or in the 3D view, the result will be different.</p>
<p>If you change the selected slice view’s orientation, the result will change also.</p>
<p>The cutting plane corresponding to the selected slice view’s orientation. The plane is constructed at the Fiducial point’s coordinates.</p>
<p>As a helper, the selected slice view’s orientation is memorised with the fiducial point the first time you click on it. This allows to restore the orientation when you click on it again. It is very helpful when working with diseased blood vessels with more than 1 control point.</p>
<p>The location of the Fiducial point is not memorised, it does not makes sense.</p>
<p>To reset the memorised orientation, choose More/Reset control point orientation and click on the Fiducial point again.</p>
<p>A connected or disconnected segment is the same if you uncheck ‘Limit to closest islands’. It does make a difference if this option is checked.</p>

---

## Post #35 by @AmandineG (2023-02-15 09:49 UTC)

<p>Thank you very much for your help!<br>
It seems to work this time</p>

---

## Post #36 by @Caner_Ozturk (2023-06-17 16:05 UTC)

<p>Hi. I need help for a issue I’m experiencing abou this module.<br>
I am using segment cross section area tool to measure muscle mass volume at L3 vertebra corpus level. Sometimes the result shows zero. I couldn’t figure out why.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33a8a473feff1805417a9cc3f2124a7dcdf3ae59.jpeg" data-download-href="/uploads/short-url/7mZFgMSoek5RIzFFpOnjpvGYudr.jpeg?dl=1" title="ssoru" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33a8a473feff1805417a9cc3f2124a7dcdf3ae59_2_690x219.jpeg" alt="ssoru" data-base62-sha1="7mZFgMSoek5RIzFFpOnjpvGYudr" width="690" height="219" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33a8a473feff1805417a9cc3f2124a7dcdf3ae59_2_690x219.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33a8a473feff1805417a9cc3f2124a7dcdf3ae59_2_1035x328.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33a8a473feff1805417a9cc3f2124a7dcdf3ae59_2_1380x438.jpeg 2x" data-dominant-color="474844"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ssoru</span><span class="informations">2549×812 263 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #37 by @lassoan (2023-06-18 12:32 UTC)

<p>Do you see any error in the application log?<br>
Can you share anonymized data or instructions to reproduce the issue using openly available data (such as images in the Sample data module)?</p>

---

## Post #38 by @Frederico_Lisboa_Nog (2023-06-18 19:50 UTC)

<p>Please,<br>
Where is the video?</p>

---

## Post #39 by @muratmaga (2023-06-19 00:08 UTC)

<div class="youtube-onebox lazy-video-container" data-video-id="fBaTM5utQC0" data-video-title="3D Slicer - Segment Geometry Demo" data-video-start-time="0" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=fBaTM5utQC0" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/fBaTM5utQC0/maxresdefault.jpg" title="3D Slicer - Segment Geometry Demo" width="" height="">
  </a>
</div>

<div class="youtube-onebox lazy-video-container" data-video-id="fI5xFT7_81I" data-video-title="3D Slicer - Segment Geometry Cat Jaw Demo" data-video-start-time="0" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=fI5xFT7_81I" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/fI5xFT7_81I/maxresdefault.jpg" title="3D Slicer - Segment Geometry Cat Jaw Demo" width="" height="">
  </a>
</div>


---
