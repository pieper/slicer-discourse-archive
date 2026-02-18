# Smoothing effect only in 1 axis

**Topic ID**: 14613
**Date**: 2020-11-15
**URL**: https://discourse.slicer.org/t/smoothing-effect-only-in-1-axis/14613

---

## Post #1 by @NoobForSlicer (2020-11-15 07:12 UTC)

<p>is it possible to have smoothing effect only affect the one axis, the one that vertically goes through slices.</p>
<p>In other words, if the resolution of a slice is good but slices were spaced a lot,  if the 2mm or 3mm smooth is applied, it affects all directions, that way resolution in the slice is sadly lost.</p>
<p>so is there an option to smooth only 1 direction?</p>
<ol>
<li>for example add extra slices between these and make a voxel through interplation<br>
Or</li>
<li>somehow manouver 3D models to be smoothen only in 1 direction</li>
</ol>
<p>?</p>

---

## Post #2 by @muratmaga (2020-11-15 07:28 UTC)

<p>If you are planning to apply this smoothing to a segmentation, and your dataset is highly anisotropic, probably you want to resample the original volume as isotropic using CropVolume before you start your segmentation. This would be equivalent to your <span class="hashtag">#1</span>.</p>
<p>If it is a scalar volume you want to smooth, then you can try SimpleFilters (e.g., gaussian or median) which let’s you specify the smoothing sigmas independently for each axis.</p>

---

## Post #3 by @NoobForSlicer (2020-11-15 08:16 UTC)

<ol>
<li>no, I do not think this would be the same. Even isotropic volume when smooth applied it would be applied between horizontal pixels in each slice.</li>
</ol>
<p>So let’s say the segmentaiton is a very sharp corner somewhere and looks beautiful when only viewed in a horizontal sice.</p>
<p>Even with isotropic voxels, smoothing will affect the horizontal edges and lines, thus result in rounding of the corners in horizonal slices as well.</p>
<ol start="2">
<li>I am not sure what is a scalar volume, I will see what this means but this is a regular nrrd file made up of many slices that’s all… just images stacked upon one another. great resolution but horrible spacing.</li>
</ol>

---

## Post #4 by @NoobForSlicer (2020-11-15 08:23 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97e305933e7321341e96fe080ceee013893b9ccf.png" data-download-href="/uploads/short-url/lFEunnKJNbWbU0DQ8pmZYvoFNlt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97e305933e7321341e96fe080ceee013893b9ccf_2_644x500.png" alt="image" data-base62-sha1="lFEunnKJNbWbU0DQ8pmZYvoFNlt" width="644" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97e305933e7321341e96fe080ceee013893b9ccf_2_644x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97e305933e7321341e96fe080ceee013893b9ccf_2_966x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/97e305933e7321341e96fe080ceee013893b9ccf_2_1288x1000.png 2x" data-dominant-color="4A4A4A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1698×1318 80.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here I tried to illustrate it.</p>
<p>Assume you have 3 images stacked upon one another.</p>
<ol>
<li>you want to avoid sharp red line but</li>
<li>you want to smoothen it to get the green line</li>
<li>however on a horizontal plane you WANT to keep the sharp blue line as is</li>
<li>and avoid having it smoothen out to be yellow line (because resolution is great 7T micrometers images and segmentation was done excellently well without errors.</li>
</ol>
<p>However because process takes long, slices were few and huge spacing</p>

---

## Post #5 by @NoobForSlicer (2020-12-05 05:32 UTC)

<p>hello PLease?! Help, I tried to apply median smartfilter so scalar volumes.</p>
<p>There are no gilters with these names gaussian or median<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c21631a971d70bec4d3eb3eb94acfe312ff4664.png" data-download-href="/uploads/short-url/8zWb9c3uYWpxJ51pshvPHRtkHwE.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c21631a971d70bec4d3eb3eb94acfe312ff4664.png" alt="image" data-base62-sha1="8zWb9c3uYWpxJ51pshvPHRtkHwE" width="690" height="457" data-dominant-color="EBEFF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1076×713 28.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>there are other similar named filters such as binarymedian something.</p>
<p>Which exactly filter to choose?<br>
How to select axis in which to apply it?</p>

---

## Post #6 by @NoobForSlicer (2020-12-05 05:41 UTC)

<p>Also Muratmaga, how will cropping volume solve anything?</p>
<p>There is no way to tell the slicer to create extra slicers and interpolate them only in 1 axis.</p>
<p>Here all I see is spaxin 1x.</p>
<p>Further more how would cropping create interpolated new slices which interpolate ONLY in one axis and not other two?</p>

---

## Post #7 by @NoobForSlicer (2020-12-05 05:44 UTC)

<p>in order to check isotropic spacing it forces me to use “interpolated cropping” which then affects all directions with interpolation.</p>

---

## Post #8 by @NoobForSlicer (2020-12-05 05:45 UTC)

<p>that is exactly what I am trying to avoid since images are perfectly clear and beautiful in horizontal plane. No need to interpolate them.</p>

---

## Post #9 by @NoobForSlicer (2020-12-05 05:52 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e4c5d2ad339a609ca8aa4bf13bb4ba0b1530b47.png" data-download-href="/uploads/short-url/fJK86vpQ0mRlKED3CYrDThL2zUH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e4c5d2ad339a609ca8aa4bf13bb4ba0b1530b47_2_690x350.png" alt="image" data-base62-sha1="fJK86vpQ0mRlKED3CYrDThL2zUH" width="690" height="350" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e4c5d2ad339a609ca8aa4bf13bb4ba0b1530b47_2_690x350.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e4c5d2ad339a609ca8aa4bf13bb4ba0b1530b47.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e4c5d2ad339a609ca8aa4bf13bb4ba0b1530b47.png 2x" data-dominant-color="CECFC8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">882×448 48 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I mean look what it does to the horizontal images which were fine and okay. It creates opacity low many images horizontal images. This is actually a horrible solution to what I am proposing. IT completely ruins the detail and effects that were contained in high resolution horizontal images.</p>
<p>Crop Volume isotropic demands interpolation and that interpolation makes no distinction what it is interpolating or in which axis. It simply interpolates everything thus ruining the detail of horizontal images.</p>

---

## Post #10 by @NoobForSlicer (2020-12-05 05:56 UTC)

<p>The proposal is simple:</p>
<p>Do not affect horizontal shapes of the OBJ, preserve all details of each pixel in the horizontal images, simply smoothen out the object vertically in 1 axis.</p>
<p>The SmartFilters you said do not exist. Those are the only three smartfilters with name median in them:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/8385997152f12f6b61140147d95f43c31c2da2cc.png" alt="image" data-base62-sha1="iLuMBFfwBBxzJ8Ww92fWKOcS0ag" width="491" height="236"></p>
<p>and here are the filters that have gaussian name in them:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acd46b4b272bdfb3a870cc8ce1a2e6abab524258.png" data-download-href="/uploads/short-url/oEVej5JbIrvZeMuYhCInLi8Gpfy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/acd46b4b272bdfb3a870cc8ce1a2e6abab524258.png" alt="image" data-base62-sha1="oEVej5JbIrvZeMuYhCInLi8Gpfy" width="690" height="364" data-dominant-color="D9DFE3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">725×383 16.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Filters with simple name median or gaussian do not exist.</p>
<p>Please Muratmaga clarify if you can and have time?</p>
<p>What exactly could I do now? Is this even possible?</p>

---

## Post #11 by @muratmaga (2020-12-05 06:27 UTC)

<p>If you type median to the search box in the <code>SimpleFilters</code>, you should see the filters: BinaryMedianFilter is the first one shown, but the drop down should list the others. Same for Gaussian too.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce2fd8cbe5dc1c14e64d3a3cf3e354426f6ec19b.png" data-download-href="/uploads/short-url/tq0RXAn8tpsazGhCQWmfvffDsgP.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce2fd8cbe5dc1c14e64d3a3cf3e354426f6ec19b_2_332x250.png" alt="image" data-base62-sha1="tq0RXAn8tpsazGhCQWmfvffDsgP" width="332" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce2fd8cbe5dc1c14e64d3a3cf3e354426f6ec19b_2_332x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce2fd8cbe5dc1c14e64d3a3cf3e354426f6ec19b_2_498x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce2fd8cbe5dc1c14e64d3a3cf3e354426f6ec19b_2_664x500.png 2x" data-dominant-color="404548"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1137×855 75.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You probably should have done the crop volume with interpolation and isotropic spacing prior to starting the segmentation. If you only want to resample in the Z direction, ResampleScalarVolume can give you what you want. (just leave x and y values as 0,0 and enter whatever spacing you want for Z).</p>
<p>Rest of what you are trying to achieve is not clear to me.</p>

---

## Post #12 by @NoobForSlicer (2020-12-05 06:30 UTC)

<p>sir thank you very much. I have found similar methods in 3ds max to affect only one axis but this is much better I can tell because it is right away in slicer.</p>
<p>I did not want to bother you so I was researching on my own trying to do it but failed with many times over. Now I will try these two methods Hopefully see which one works. There is also one more student he was given similar tasks for 2 weeks and he has same issue. I hope this works</p>
<p>Thank you sir so much for replying</p>

---

## Post #13 by @lassoan (2020-12-05 06:35 UTC)

<p>If your image is highly anisotropic then it means that you won’t be able to fully utilize the high resolution information within the image slice, because you just miss so much information between the slices.</p>
<p>You can find more information here: <a href="https://discourse.slicer.org/t/how-can-i-import-in-the-same-volume-3-dicom-files-of-the-same-volume/8695/2" class="inline-onebox">How can I import in the same volume 3 DICOM files of the same volume - #2 by lassoan</a></p>
<p>If your goal is not to reproduce the missing information (which is impossible), and it is OK to have sharp edges along two axes, while smooth interpolation along the third one, then you can use morphological interpolation to fill in the gaps. To achieve this, resample the input volume to be isotropic as <a class="mention" href="/u/muratmaga">@muratmaga</a> suggested above, but then only segment at the middle of the original slices. To do that, you can choose your original sparse volume as background volume and use Scissors effect to fill a thin slice (Operation: Fill inside; Slice cut: symmetric 0.1mm or whatever the resolution along the high-resolution axis). You will end up with thin slices with large gaps between them. When you are finished with your segmentation, use Fill between slices effect to fill in the gaps.</p>
<p>Before “Fill between slices”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f4d19896b45398c00b549f0c28e9751662bf788.jpeg" data-download-href="/uploads/short-url/6KrCQxf8MsJZiv2Y5rUQ91ZzM3S.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f4d19896b45398c00b549f0c28e9751662bf788_2_479x500.jpeg" alt="image" data-base62-sha1="6KrCQxf8MsJZiv2Y5rUQ91ZzM3S" width="479" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f4d19896b45398c00b549f0c28e9751662bf788_2_479x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f4d19896b45398c00b549f0c28e9751662bf788_2_718x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f4d19896b45398c00b549f0c28e9751662bf788_2_958x1000.jpeg 2x" data-dominant-color="303134"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1166×1217 193 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After “Fill between slices”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0cea3c5ab6815a00e0cb436a885bee58b0f7a9e.jpeg" data-download-href="/uploads/short-url/tNc2jVSQ2FmNCNhSq8evieJoBMq.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0cea3c5ab6815a00e0cb436a885bee58b0f7a9e_2_477x500.jpeg" alt="image" data-base62-sha1="tNc2jVSQ2FmNCNhSq8evieJoBMq" width="477" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0cea3c5ab6815a00e0cb436a885bee58b0f7a9e_2_477x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0cea3c5ab6815a00e0cb436a885bee58b0f7a9e_2_715x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0cea3c5ab6815a00e0cb436a885bee58b0f7a9e_2_954x1000.jpeg 2x" data-dominant-color="313336"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1168×1224 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #14 by @NoobForSlicer (2020-12-05 06:42 UTC)

<p>this exactly describes what I want and you have properly understood what I mean.</p>
<p>Aim to “recover” information between slices if of course impossible</p>
<p>The aim was only to smoothen the transition so that it doesn’t look so ugly.</p>
<p>The problem is that images are loaded from a sequence with white background. They are enumerated and then the automatic script segments them with treshold since they all have copletely white background. This way thousands of images are processed.</p>
<p>The threshold would simply segment everything right?<br>
I would not be able to tell threshold function in the script “segment every third slice or every 4th slice”.</p>
<p>But yes, this properly describes what I mean or what I tried to express and what you did is exactly that what you demonstrated is exactly what I meant.</p>

---

## Post #15 by @lassoan (2020-12-05 07:02 UTC)

<aside class="quote no-group" data-username="NoobForSlicer" data-post="14" data-topic="14613">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/noobforslicer/48/10900_2.png" class="avatar"> NoobForSlicer:</div>
<blockquote>
<p>I would not be able to tell threshold function in the script “segment every third slice or every 4th slice”.</p>
</blockquote>
</aside>
<p>You could then insert blank slices between your segmented slices to create the desired input volume (with gaps between thin slices).</p>

---

## Post #16 by @NoobForSlicer (2020-12-05 16:27 UTC)

<p>hello Lassoan, I have done this and yes results are nice <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
