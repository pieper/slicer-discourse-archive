---
topic_id: 40141
title: "Binary Labelmap Creation Is There A Systematic Way To Select"
date: 2024-11-12
url: https://discourse.slicer.org/t/40141
---

# Binary Labelmap Creation - Is there a systematic way to select optimal segment conversion parameters to reduce artefacting?

**Topic ID**: 40141
**Date**: 2024-11-12
**URL**: https://discourse.slicer.org/t/binary-labelmap-creation-is-there-a-systematic-way-to-select-optimal-segment-conversion-parameters-to-reduce-artefacting/40141

---

## Post #1 by @LRAnti (2024-11-12 02:50 UTC)

<p>Hello,</p>
<p>I work with a lot of different dcm RTSTRUCT datasets, and often end up with weird artefacts after conversion of planar contours to a binary labelmap, such as holes, aliasing and interpolation errors creating planar artefacts where there may be a significant change in cross section between contours (sometimes, but not always).<br>
This is what these artefacts tend to look like:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc3e246725bdae92ebef5a9f19e725d3d426f41e.png" data-download-href="/uploads/short-url/t8OxFmzcC8RZxKEPAracrKX7ypg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc3e246725bdae92ebef5a9f19e725d3d426f41e.png" alt="image" data-base62-sha1="t8OxFmzcC8RZxKEPAracrKX7ypg" width="359" height="247"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">359×247 50.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I can usually get a decent result by changing a couple of conversion parameters in the “Advanced Create” dialogue such as the spacing (voxel size) and the oversampling factor - there seems to be an optimal spacing that gets rid of artefacts and minimises aliasing while preserving detail. However I can only find this through trial and error currently.</p>
<p>Does anyone know of a way to select the best conversion parameters based on features of the dataset (maybe like contour spacing, contour resolution, overall size of the segment, or something else)?</p>
<p>Or does anyone have any links to technical resources that might help me to get a deeper understanding of the geometric/algorithmic procedure that is at play here?</p>
<p>Any help would be much appreciated!</p>
<p>Thanks,<br>
Lauren</p>

---

## Post #2 by @cpinter (2024-11-12 13:13 UTC)

<p>First of all, I think it is important to understand the way segmentations are handled in Slicer. Please see this page<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html</a><br>
The figure about conversion shows exactly the RT use case, where you have a set of planar contours for each structure. By default Slicer converts these planar contours to closed surface models (see paper: Sunderland, K., Woo, B., Pinter, C., &amp; Fichtinger, G. (2015, March). Reconstruction of surfaces from planar contours through contour interpolation. In <em>Medical Imaging 2015: Image-Guided Procedures, Robotic Interventions, and Modeling</em> (Vol. 9415, pp. 435-442). SPIE.), which are then voxelized. Once you start editing the segments, the binary labelmap becomes the source representation, and closed surface is created directly from that.</p>
<p>In the advance create dialog that you already found, you can define an alternate route from planar contours, which is via ribbons. It is more robust, but less accurate (no out-of-slice changes for each slice, so the slice thickness seriously limits the reconstructed details).</p>
<p>To me the artifacts you show seem like instances where the binary labelmap contains a connecting point between parts of the structure, which the algorithm wants to triangulate (with the included smoothing), and this is the result. Unfortunately in this single low-resolution screenshot there is not much to see.</p>
<p>Overall I think your approach to increase resolution via oversampling is a good way to go if your data allows this increased memory and performance demand. Every application is very different, so I think you’ll need to find an overall reasonable oversampling factor, and use that.</p>
<p>Maybe if you give us more information we can give you better answers.</p>

---

## Post #3 by @LRAnti (2024-12-05 03:10 UTC)

<p>Hi Csaba,</p>
<p>Thank you for that it was very helpful! I think the issue was a correspondence problem because it was primarily showing up with datasets with larger contour spacing and for thin layer segments. This was solved using the ribbon pathway when the spacing is above a certain threshold.</p>
<p>I have noticed though that sometimes increasing the oversampling results in what looks like aliasing - but in the xy plane (as opposed to staircasing in z). Is there any point in the conversion that interpolates between points on the contour as well as between contours? Are there any resources that you know of that might help me learn more about this?</p>
<p>When I was inspecting the contour points themselves I noticed that in some cases they are very unevenly spaced. I have considered reconstructing the contours by fitting a spline to the points in the RTSTRUCT dataset and then sampling that at regular spacing along the curve, creating a new dataset and then putting it into 3Dslicer to convert. Do you know if this approach is likely to affect the result?</p>
<p>Thank you again - I learnt a lot of useful info from the links you provided!</p>

---

## Post #4 by @cpinter (2024-12-05 14:25 UTC)

<p>Out-of-plane interpolation is solved by the conversion I was talking about above. If you visualize the ribbons in 3D you’ll understand why there is no “interpolation” using those. I recommend using the default Slicer options for loading legacy RTSTRUCT files.</p>
<p>It is extremely hard to answer questions when the information provided is so little.</p>

---

## Post #5 by @LRAnti (2024-12-09 08:29 UTC)

<p>Yes, as I said, I tried the ribbon pathway and it worked well. I’m not sure what you mean by “the information you provided is so little”, my question was a general one but perhaps I didn’t explain it very well. I am looking for some more background information - (such as how 3Dslicer puts planar contours together from an RTSTRUCT dataset, as it was my understanding that RTSTRUCT just contains ordered points and doesn’t contain any edges or curves etc). Very broadly, I’m interested in gaining a better understanding of how changing conversion parameters in 3dslicer leads to different output. At this stage I’m not looking for answers on specific cases, I mainly just wanted to know if you had any more suggestions of background reading because I found the papers you mentioned in your previous reply to be very helpful.</p>

---

## Post #6 by @cpinter (2024-12-09 09:48 UTC)

<aside class="quote no-group" data-username="LRAnti" data-post="5" data-topic="40141">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lranti/48/78502_2.png" class="avatar"> LRAnti:</div>
<blockquote>
<p>how 3Dslicer puts planar contours together from an RTSTRUCT dataset, as it was my understanding that RTSTRUCT just contains ordered points and doesn’t contain any edges or curves etc</p>
</blockquote>
</aside>
<p>The algorithm is explained in detail in the paper I referred to above (Sunderland et al., 2015).</p>
<aside class="quote no-group" data-username="LRAnti" data-post="5" data-topic="40141">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lranti/48/78502_2.png" class="avatar"> LRAnti:</div>
<blockquote>
<p>how changing conversion parameters in 3dslicer leads to different output</p>
</blockquote>
</aside>
<p>The representations and conversions can be generally explored and optimized in the Segmentations module (not Segment Editor). You’ll see the representations a below the segments and the display options. This is what you see for RTSTRUCT:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f476d8c4e52e3fc60562f3b4f5a81887f71427d.png" data-download-href="/uploads/short-url/mJ2WZfKa08xDFj6M5c5XgbHICyV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f476d8c4e52e3fc60562f3b4f5a81887f71427d.png" alt="image" data-base62-sha1="mJ2WZfKa08xDFj6M5c5XgbHICyV" width="366" height="121"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">366×121 3.73 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you click Update you’ll be able to choose the conversion path and change the parameters that are exposed:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcf4012e21dfb8bf6573c968e343ec3984882b98.png" data-download-href="/uploads/short-url/A5J6ctqLewOHUCencIumDjYoQTm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcf4012e21dfb8bf6573c968e343ec3984882b98.png" alt="image" data-base62-sha1="A5J6ctqLewOHUCencIumDjYoQTm" width="511" height="447"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">511×447 10.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This particular converter (planar contours to closed surface) has two conversion parameters. You can get more information about them in the tooltip if you hover their names. The default slice thickness parameter is typically not used, it is a fallback value when the quality of the dataset is low (you’ll get an error in the log about this if it happens).</p>
<aside class="quote no-group" data-username="LRAnti" data-post="5" data-topic="40141">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lranti/48/78502_2.png" class="avatar"> LRAnti:</div>
<blockquote>
<p>I’m not sure what you mean by “the information you provided is so little”</p>
</blockquote>
</aside>
<p>I meant that we can help better if you explain your use case and what is bothering you exactly and what you want to achieve.</p>

---
