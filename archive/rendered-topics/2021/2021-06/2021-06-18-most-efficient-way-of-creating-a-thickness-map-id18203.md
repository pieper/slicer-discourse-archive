---
topic_id: 18203
title: "Most Efficient Way Of Creating A Thickness Map"
date: 2021-06-18
url: https://discourse.slicer.org/t/18203
---

# Most Efficient Way of Creating a Thickness Map

**Topic ID**: 18203
**Date**: 2021-06-18
**URL**: https://discourse.slicer.org/t/most-efficient-way-of-creating-a-thickness-map/18203

---

## Post #1 by @Fluvio_Lobo (2021-06-18 12:45 UTC)

<p>Hello,</p>
<p>I have been working on various CMF workflows recently and, in most, our team wants to be capable of generating a thickness map.</p>
<p>My current approach is very simple;</p>
<ol>
<li>Segment the bony tissue</li>
<li>Hollow the segment</li>
<li>Crop/isolate the region of interest (mostly using scissors)</li>
<li>Separate Outer and Inner surfaces by treating them as islands</li>
<li>Convert Outer and Inner segments into models</li>
<li>Use the <strong>Model-to-Model-Distance</strong> module to create a distance or thickness map</li>
<li>Visualize distance map using the <strong>Shape-Population-Viewer module</strong>*<br>
*Note that I have to account for the thickness of the segments themselves</li>
</ol>
<p>In a simple bone harvesting workflow, this process works nicely<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a75ddab9cf7abd2b6ec975d70b11b3b752611b9c.png" data-download-href="/uploads/short-url/nSAOORPE5UcLpYK07BRhwS9hPJy.png?dl=1" title="superior_view_thickness_mapping" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a75ddab9cf7abd2b6ec975d70b11b3b752611b9c_2_345x375.png" alt="superior_view_thickness_mapping" data-base62-sha1="nSAOORPE5UcLpYK07BRhwS9hPJy" width="345" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a75ddab9cf7abd2b6ec975d70b11b3b752611b9c_2_345x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a75ddab9cf7abd2b6ec975d70b11b3b752611b9c_2_517x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a75ddab9cf7abd2b6ec975d70b11b3b752611b9c.png 2x" data-dominant-color="9E87A4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">superior_view_thickness_mapping</span><span class="informations">659×715 357 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>On a cranioplasty workflow, where I am trying to create a thickness map around the bone defect, the process gets a little complicated. Specifically when the edges of the defect reach areas of the ear and nose, where the skull features internal hollow features. In this case;</p>
<ol>
<li>Segment the bony tissue</li>
<li>Fill internal features/holes/cavities*</li>
<li>Hollow the segment</li>
<li>Crop/isolate the region of interest (mostly using scissors) —&gt; this applies to everything beyond the inner edges of the skull defect</li>
<li>Use a dilated version of the Baffle, created to fix the defect, to crop the inner edges of the bone defect</li>
<li>Separate Outer and Inner surfaces by treating them as islands</li>
<li>Convert Outer and Inner segments into models</li>
<li>Use the <strong>Model-to-Model-Distance</strong> module to create a distance or thickness map</li>
<li>Visualize distance map using the <strong>Shape-Population-Viewer module</strong>**</li>
</ol>
<p>*I would prefer not doing this and rather cut-out the entire area, otherwise I am calculating an inaccurate thickness<br>
**To use the Baffle planner I needed Slicer 4.13 but the Shape-Population-Viewer is not available in this version?</p>
<p>Here are some pictures of the process;</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4db7a73dd8349140a271261b0fc46af52c137a5f.jpeg" data-download-href="/uploads/short-url/b5weUMwciviLJbzQU3iSy261iuX.jpeg?dl=1" title="skull.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4db7a73dd8349140a271261b0fc46af52c137a5f_2_256x250.jpeg" alt="skull.PNG" data-base62-sha1="b5weUMwciviLJbzQU3iSy261iuX" width="256" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4db7a73dd8349140a271261b0fc46af52c137a5f_2_256x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4db7a73dd8349140a271261b0fc46af52c137a5f_2_384x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4db7a73dd8349140a271261b0fc46af52c137a5f_2_512x500.jpeg 2x" data-dominant-color="5A5036"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">skull.PNG</span><span class="informations">833×811 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81c76d4d0bd19f0c5231bdea4b22828eba868b0b.png" data-download-href="/uploads/short-url/iw4Rz6PTUBQG8bPqLqMhzLCZAzF.png?dl=1" title="innerouter" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81c76d4d0bd19f0c5231bdea4b22828eba868b0b_2_402x375.png" alt="innerouter" data-base62-sha1="iw4Rz6PTUBQG8bPqLqMhzLCZAzF" width="402" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81c76d4d0bd19f0c5231bdea4b22828eba868b0b_2_402x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81c76d4d0bd19f0c5231bdea4b22828eba868b0b_2_603x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81c76d4d0bd19f0c5231bdea4b22828eba868b0b.png 2x" data-dominant-color="0B1109"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">innerouter</span><span class="informations">753×701 77.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa4cb95caf4b13f575a77fc994f1e84cc7cd7f8b.png" data-download-href="/uploads/short-url/oixy8gVsgCeSiD7zeCVEdQS7idR.png?dl=1" title="ringmap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa4cb95caf4b13f575a77fc994f1e84cc7cd7f8b_2_386x375.png" alt="ringmap" data-base62-sha1="oixy8gVsgCeSiD7zeCVEdQS7idR" width="386" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa4cb95caf4b13f575a77fc994f1e84cc7cd7f8b_2_386x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa4cb95caf4b13f575a77fc994f1e84cc7cd7f8b_2_579x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa4cb95caf4b13f575a77fc994f1e84cc7cd7f8b_2_772x750.png 2x" data-dominant-color="575039"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ringmap</span><span class="informations">804×780 368 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2eb3067e40739c433f0a8b57d6820428e3db1d0.png" data-download-href="/uploads/short-url/u5S9RwxaQ3XYz4ADMHrtGorDxZe.png?dl=1" title="baffle" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2eb3067e40739c433f0a8b57d6820428e3db1d0_2_268x250.png" alt="baffle" data-base62-sha1="u5S9RwxaQ3XYz4ADMHrtGorDxZe" width="268" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2eb3067e40739c433f0a8b57d6820428e3db1d0_2_268x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2eb3067e40739c433f0a8b57d6820428e3db1d0_2_402x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2eb3067e40739c433f0a8b57d6820428e3db1d0_2_536x500.png 2x" data-dominant-color="356131"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">baffle</span><span class="informations">825×767 294 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My questions are;<br>
<strong>Is there a more elegant way of doing this?</strong><br>
<strong>Are there compatibility issues with the Shape-Population-Viewer in 4.13?</strong></p>
<p><em>PS: I have tried the <a href="https://github.com/Auditory-Biophysics-Lab/SlicerBoneThicknessMappingExtension" rel="noopener nofollow ugc">Thickness-Mapping</a> module with little success, but I am willing to retry if it is the most appropriate method</em></p>

---

## Post #2 by @lassoan (2021-06-18 20:16 UTC)

<p>Thickness-Mapping module should work well if you want to measure thickness along a certain axis.</p>
<p>Otherwise, I would recommend using the workflow described here:</p>
<aside class="quote quote-modified" data-post="2" data-topic="2735">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-analyze-the-thickness-of-the-model/2735/2">How to analyze the thickness of the model</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    “Thickness” is not a very well defined term for models (surface meshes), but for shell-like meshes it is probably not too difficult to estimate it robustly and accurately. 
Potential approaches: 
A. Extract medial surface and estimate thickness as 2x of distance from medial surface. There are various ways of computing these in Slicer. One possible workflow: 

Compute medial surface using Simple Filters module - BinaryThinningImageFilter.
Compute distance map using Simple Filters module - Daniels…
  </blockquote>
</aside>

<p>You need to use a segmentation that contains the entire skull bone (not just the thin cortical surfaces but the internal cancellous bone as well).</p>
<p>You don’t need to use Shape Population Viewer to see the color overlay, just go to Models module and click “Visible” checkbox in Display / Scalars section (and select distance as active scalar, if it has not been selected already).</p>

---

## Post #3 by @Fluvio_Lobo (2021-06-24 02:37 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Thank you for the solution!<br>
Here is a summary of the process, my results, and some follow-up questions.</p>
<ol>
<li>
<p>Generated a <strong>label-map</strong> from the <strong>segmentation</strong> of the skull<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2eeda73eada46ccec24e01afca17ea90bc004f44.png" data-download-href="/uploads/short-url/6H98h7UOaPlzjkMKgn11iAQLP0M.png?dl=1" title="labelmap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2eeda73eada46ccec24e01afca17ea90bc004f44_2_345x186.png" alt="labelmap" data-base62-sha1="6H98h7UOaPlzjkMKgn11iAQLP0M" width="345" height="186" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2eeda73eada46ccec24e01afca17ea90bc004f44_2_345x186.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2eeda73eada46ccec24e01afca17ea90bc004f44_2_517x279.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2eeda73eada46ccec24e01afca17ea90bc004f44_2_690x372.png 2x" data-dominant-color="2F2E2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">labelmap</span><span class="informations">1920×1040 344 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Created a <strong>medial surface</strong> from the <strong>label-map</strong> using the <strong>BinaryThinningImageFilter</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03d08622fde47519de63247dc5f64d349ce8fadc.png" data-download-href="/uploads/short-url/xKbXJHoRWPQGUY5CUZa8hFDllW.png?dl=1" title="medialsurface" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03d08622fde47519de63247dc5f64d349ce8fadc_2_345x186.png" alt="medialsurface" data-base62-sha1="xKbXJHoRWPQGUY5CUZa8hFDllW" width="345" height="186" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03d08622fde47519de63247dc5f64d349ce8fadc_2_345x186.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03d08622fde47519de63247dc5f64d349ce8fadc_2_517x279.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03d08622fde47519de63247dc5f64d349ce8fadc_2_690x372.png 2x" data-dominant-color="252422"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">medialsurface</span><span class="informations">1920×1040 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Created a <strong>distance map</strong> from the <strong>medial surface</strong> using the <strong>DanielssonDistanceMapImageFilter</strong> with <em>Input is Binary = Yes</em> and <em>Use Image Spacing=Yes</em><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0ff06df5dc06b843427242840b7d8fc16731bfec.jpeg" data-download-href="/uploads/short-url/2h0hm972mV9heyv8fqQYaD9mQ6E.jpeg?dl=1" title="distancemap.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ff06df5dc06b843427242840b7d8fc16731bfec_2_345x186.jpeg" alt="distancemap.PNG" data-base62-sha1="2h0hm972mV9heyv8fqQYaD9mQ6E" width="345" height="186" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ff06df5dc06b843427242840b7d8fc16731bfec_2_345x186.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ff06df5dc06b843427242840b7d8fc16731bfec_2_517x279.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ff06df5dc06b843427242840b7d8fc16731bfec_2_690x372.jpeg 2x" data-dominant-color="2E2D2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">distancemap.PNG</span><span class="informations">1920×1040 249 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Created a <strong>thickness/displacement model</strong> with the <strong>distance map</strong> using the <strong>Probe Volume with Model</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1919bd041b597b22496ae8c1d74a5b172c179c6.jpeg" data-download-href="/uploads/short-url/pkQtAXg89ZjNdYzGqBvAXGRnWrY.jpeg?dl=1" title="dispmodel.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b1919bd041b597b22496ae8c1d74a5b172c179c6_2_345x186.jpeg" alt="dispmodel.PNG" data-base62-sha1="pkQtAXg89ZjNdYzGqBvAXGRnWrY" width="345" height="186" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b1919bd041b597b22496ae8c1d74a5b172c179c6_2_345x186.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b1919bd041b597b22496ae8c1d74a5b172c179c6_2_517x279.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b1919bd041b597b22496ae8c1d74a5b172c179c6_2_690x372.jpeg 2x" data-dominant-color="26262C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dispmodel.PNG</span><span class="informations">1920×1040 347 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Finally, I can visualize the data using model properties<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e13c03fada5a253032089c9582b0b122e38793a6.jpeg" data-download-href="/uploads/short-url/w8w0Q9eqlXYnfeUOqFCIvVxNB7U.jpeg?dl=1" title="prop.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e13c03fada5a253032089c9582b0b122e38793a6_2_345x186.jpeg" alt="prop.PNG" data-base62-sha1="w8w0Q9eqlXYnfeUOqFCIvVxNB7U" width="345" height="186" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e13c03fada5a253032089c9582b0b122e38793a6_2_345x186.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e13c03fada5a253032089c9582b0b122e38793a6_2_517x279.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e13c03fada5a253032089c9582b0b122e38793a6_2_690x372.jpeg 2x" data-dominant-color="25262C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">prop.PNG</span><span class="informations">1920×1040 380 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>Remaining questions;</p>
<ol>
<li>
<p>I originally tried making the <strong>label-map</strong> from the model using the <strong>Model to LabelMap</strong> extension, but just a right click on the segment seems easier… is this the correct approach?</p>
</li>
<li>
<p>How do you plot/show/display a <strong>color table/bar</strong> next to the 3D model?</p>
</li>
</ol>

---

## Post #4 by @pieper (2021-06-24 18:25 UTC)

<p>That’s looking quite nice <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=14" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="3" data-topic="18203">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p>I originally tried making the <strong>label-map</strong> from the model using the <strong>Model to LabelMap</strong> extension, but just a right click on the segment seems easier… is this the correct approach?</p>
</blockquote>
</aside>
<p>Yes, that is a good way.</p>
<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="3" data-topic="18203">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p>How do you plot/show/display a <strong>color table/bar</strong> next to the 3D model?</p>
</blockquote>
</aside>
<p>There’s a Color Scalar Bar option in the Colors module.</p>

---

## Post #5 by @jdellorfano (2021-11-29 01:33 UTC)

<p>I am working on a similar problem in the heart. In this test case I simply segmented the endocardium and the epicardium and used the model to model distance to create a thickness map. In practice, this may identify areas of scar tissue on the heart. I made an artificial infarct in this test data and the results seem to be good. I am very new to 3D Slicer and am wondering if there is a better way to do this such as described in this thread. I did not have luck reproducing this with my dataset but I think I am happy with the results of the model to model distance. Any suggestions?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d61309d65af8d6c7003f6b0b0abfd8aa78e44d21.jpeg" data-download-href="/uploads/short-url/uxMY2dhdKhBDBFtcEhBEzO8SWNb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d61309d65af8d6c7003f6b0b0abfd8aa78e44d21_2_610x500.jpeg" alt="image" data-base62-sha1="uxMY2dhdKhBDBFtcEhBEzO8SWNb" width="610" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d61309d65af8d6c7003f6b0b0abfd8aa78e44d21_2_610x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d61309d65af8d6c7003f6b0b0abfd8aa78e44d21_2_915x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d61309d65af8d6c7003f6b0b0abfd8aa78e44d21_2_1220x1000.jpeg 2x" data-dominant-color="827FBB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1247×1021 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @Fluvio_Lobo (2021-11-29 04:35 UTC)

<p>Joseph,</p>
<p>Cool application!<br>
Instead of making two models and using model-to-model distance, try replicating <a href="https://discourse.slicer.org/t/most-efficient-way-of-creating-a-thickness-map/18203/3">the solution to the post</a>.</p>
<p>Keep in mind that the <strong>BinaryThinningImageFilter</strong> will take a very long time to complete and the loading bar does not seem to be working. I have been using his process for a cranioplasty implant, which should be a pretty simple part to compute, and it took 13 minutes!!!</p>
<p>Here are some suggestions for your model;</p>
<ol>
<li>Ensure there are no holes between the endocardium and epicardium</li>
<li>Don’t use the entire model, perhaps cut the area of the infarct and some of the surrounding tissue (to start)</li>
</ol>
<p>As always, let everyone know how it went!</p>

---

## Post #7 by @Fluvio_Lobo (2022-01-18 04:44 UTC)

<p>In case anyone is still using <strong>medial surfaces</strong> for thickness measurement and calculation, I have been working on a consolidated workflow to <strong>measure the thickness of cranioplasty implants</strong>;</p>
<p>Starting with a <strong>model</strong> of the implant (or any input surface mesh for that matter), the <strong>ThicknessMapping</strong> function (below) will complete all of the steps discussed previously, with the addition of some display settings:</p>
<p>For this input model;<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fba39ddadd624d5b0f8741f4f4f30621a591437.png" data-download-href="/uploads/short-url/6OdqznDJBMm2Ob9HmZFnORqw1tJ.png?dl=1" title="input_model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fba39ddadd624d5b0f8741f4f4f30621a591437_2_690x373.png" alt="input_model" data-base62-sha1="6OdqznDJBMm2Ob9HmZFnORqw1tJ" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fba39ddadd624d5b0f8741f4f4f30621a591437_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fba39ddadd624d5b0f8741f4f4f30621a591437_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fba39ddadd624d5b0f8741f4f4f30621a591437_2_1380x746.png 2x" data-dominant-color="303020"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">input_model</span><span class="informations">1920×1040 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The following <strong>medial thickness map</strong> is generated;<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed1af232a656995193ef93f98d94bd270312aca0.jpeg" data-download-href="/uploads/short-url/xPwTjGxyivApctx3IzSBYyanYHu.jpeg?dl=1" title="medial_thickness_map.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed1af232a656995193ef93f98d94bd270312aca0_2_690x373.jpeg" alt="medial_thickness_map.PNG" data-base62-sha1="xPwTjGxyivApctx3IzSBYyanYHu" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed1af232a656995193ef93f98d94bd270312aca0_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed1af232a656995193ef93f98d94bd270312aca0_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ed1af232a656995193ef93f98d94bd270312aca0_2_1380x746.jpeg 2x" data-dominant-color="352B39"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">medial_thickness_map.PNG</span><span class="informations">1920×1040 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/870cfbc610fd91dd8e7f304f2d33fa152af56574.png" data-download-href="/uploads/short-url/jgIh54b0sgh9MatcYJqHWNSY980.png?dl=1" title="medial_thickness_map_fourviews" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/870cfbc610fd91dd8e7f304f2d33fa152af56574_2_690x373.png" alt="medial_thickness_map_fourviews" data-base62-sha1="jgIh54b0sgh9MatcYJqHWNSY980" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/870cfbc610fd91dd8e7f304f2d33fa152af56574_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/870cfbc610fd91dd8e7f304f2d33fa152af56574_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/7/870cfbc610fd91dd8e7f304f2d33fa152af56574_2_1380x746.png 2x" data-dominant-color="221F23"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">medial_thickness_map_fourviews</span><span class="informations">1920×1040 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The program generates a <strong>blank voxel volume</strong> around the <strong>model</strong>, instead of using the original volume from the reconstruction. This reduces the number of voxels to be processed to calculate the <strong>medial surface</strong>. For standard 3.0 mm Head CTs I was originally <strong>waiting for about 10-13 minutes</strong> for the <strong>BinaryThinningImageFilter</strong> to complete. For this model shown here, the entire program takes about 1-2 mins <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=12" title=":grin:" class="emoji" alt=":grin:" loading="lazy" width="20" height="20"></p>
<p>Here is the program, written as a python function. Feel free to use and please give feedback!!!</p>
<pre><code class="lang-auto">def ThicknessMapping(self):
        '''
            Thickness Mapping
                Generates and display the thickness of a model throughout its surface.
                The thickness map is calculated using a combination of ITK Filters available to Slicer in python

            References
            [1] How to run a CLI module from Python (https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html?highlight=CLI#how-to-run-a-cli-module-from-python)
            [2] Running an ITK filter in Python using SimpleITK (https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#running-an-itk-filter-in-python-using-simpleitk)
            [3] Create custom color map and display color legend (https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-custom-color-map-and-display-color-legend)
        '''
        # Flags
        verbose                 = True

        # UI Inputs
        thicknessMapInputModel  = slicer.mrmlScene.GetNodeByID( self._parameterNode.GetNodeReferenceID("ThicknessMapInputModel") )

        # Process
        ## Creating Function Directory 
        shNode                  = slicer.mrmlScene.GetSubjectHierarchyNode()
        folder                  = shNode.CreateFolderItem(shNode.GetSceneItemID(), "Thickness Mapping")

        ## Get Model Centroid and Bounding Box
        inputAssemblyBounds, assemblyBoundingBoxCentroid            = self.logic.getBoundingBoxCentroid( thicknessMapInputModel.GetName(), True )

        ## Generate a Blank,  Bounding Volume
        masterVolumeNodeName                                        = "{}_volume".format( thicknessMapInputModel.GetName() )
        N                                                           = 2.0
        imageSpacing                                                = [1/N,1/N,1/N]
        imageSize                                                   = [int(np.round(inputAssemblyBounds[1]-inputAssemblyBounds[0])*1.10*N),
                                                                        int(np.round(inputAssemblyBounds[3]-inputAssemblyBounds[2])*1.10*N), 
                                                                        int(np.round(inputAssemblyBounds[5]-inputAssemblyBounds[4])*1.10*N)]
        voxelType                                                   = vtk.VTK_UNSIGNED_CHAR
        imageOrigin                                                 = [(assemblyBoundingBoxCentroid[0]-imageSize[0]/(2*N)), 
                                                                    (assemblyBoundingBoxCentroid[1]-imageSize[1]/(2*N)), 
                                                                    (assemblyBoundingBoxCentroid[2]-imageSize[2]/(2*N))]
        
        imageDirections                                             = [[1,0,0], [0,1,0], [0,0,1]]
        fillVoxelValue                                              = 0
        imageData                                                   = vtk.vtkImageData()
        imageData.SetDimensions(imageSize)
        imageData.AllocateScalars(voxelType, 1)
        imageData.GetPointData().GetScalars().Fill(fillVoxelValue)
        masterVolumeNode                                            = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", masterVolumeNodeName)
        masterVolumeNode.SetOrigin(imageOrigin)
        masterVolumeNode.SetSpacing(imageSpacing)
        masterVolumeNode.SetIJKToRASDirections(imageDirections)
        masterVolumeNode.SetAndObserveImageData(imageData)
        masterVolumeNode.CreateDefaultDisplayNodes()
        masterVolumeNode.CreateDefaultStorageNode()

        shNode.SetItemParent( shNode.GetItemByDataNode(masterVolumeNode), folder )

        # Status
        if (verbose):
            print( "Generated Blank, Bounding Volume..." )

        ## Generate a LabelMap using the Input Model and the Blank Bounding Volume
        modelLabelMapParams                                         = {}
        modelLabelMapParams["InputVolume"]                          = masterVolumeNode
        modelLabelMapParams["surface"]                              = thicknessMapInputModel
        modelLabelMapNode                                           = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode","{}_labelmap".format( thicknessMapInputModel.GetName() ))
        modelLabelMapParams["OutputVolume"]                         = modelLabelMapNode
        modelToLabelMap                                             = slicer.modules.modeltolabelmap

        cliNode = slicer.cli.runSync(modelToLabelMap, None, modelLabelMapParams)

        if cliNode.GetStatus() &amp; cliNode.ErrorsMask:
            errorText = cliNode.GetErrorText()
            slicer.mrmlScene.RemoveNode(cliNode)
            raise ValueError("CLI execution failed: " + errorText)
        slicer.mrmlScene.RemoveNode(cliNode)

        shNode.SetItemParent( shNode.GetItemByDataNode(modelLabelMapNode), folder )
        shNode.SetItemParent( shNode.GetItemByDataNode(cliNode), folder )

        # Status
        if (verbose):
            print( "Generated LabelMap from Model..." )

        ## Generating Medial Surface
        inputImage                                                  = sitkUtils.PullVolumeFromSlicer( modelLabelMapNode )
        filter                                                      = sitk.BinaryThinningImageFilter()
        outputImage                                                 = filter.Execute( inputImage )
        medialSurfaceVolumeNode                                     = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", "{}_medial_surface".format( thicknessMapInputModel.GetName() ))
        sitkUtils.PushVolumeToSlicer(outputImage, medialSurfaceVolumeNode)

        shNode.SetItemParent( shNode.GetItemByDataNode(medialSurfaceVolumeNode), folder )

        # Status
        if (verbose):
            print( "Generated Medial Surface from LabelMap..." )
        
        ## Generating Distance Map
        inputImage                                                  = sitkUtils.PullVolumeFromSlicer( medialSurfaceVolumeNode )
        filter                                                      = sitk.DanielssonDistanceMapImageFilter()
        filter.UseImageSpacingOn()
        filter.InputIsBinaryOn()
        outputImage                                                 = filter.Execute( inputImage )
        distanceMapVolumeNode                                       = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", "{}_distance_map".format( thicknessMapInputModel.GetName() ))
        sitkUtils.PushVolumeToSlicer(outputImage, distanceMapVolumeNode)

        shNode.SetItemParent( shNode.GetItemByDataNode(distanceMapVolumeNode), folder )

        # Status
        if (verbose):
            print( "Generated Distance Map from Medial Surface..." )

        ## Probe Volume with Model
        probeVolumeWithModelParams                                  = {}
        probeVolumeWithModelParams["InputVolume"]                   = distanceMapVolumeNode
        probeVolumeWithModelParams["InputModel"]                    = thicknessMapInputModel
        thicknessMapNode                                            = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelNode","{}_thickness_map".format( thicknessMapInputModel.GetName() ))
        probeVolumeWithModelParams["OutputModel"]                   = thicknessMapNode
        probeVolumeWithModel                                        = slicer.modules.probevolumewithmodel

        cliNode = slicer.cli.runSync(probeVolumeWithModel, None, probeVolumeWithModelParams)

        if cliNode.GetStatus() &amp; cliNode.ErrorsMask:
            errorText = cliNode.GetErrorText()
            slicer.mrmlScene.RemoveNode(cliNode)
            raise ValueError("CLI execution failed: " + errorText)
        slicer.mrmlScene.RemoveNode(cliNode)

        thicknessMapInputModel.GetDisplayNode().SetVisibility(False)

        shNode.SetItemParent( shNode.GetItemByDataNode(thicknessMapNode), folder )
        shNode.SetItemParent( shNode.GetItemByDataNode(cliNode), folder )

        # Status
        if (verbose):
            print( "Generated Thickness Map from Distance Map and Input Model..." )
        
        ## Updating Display Settings, Colormap Labeling
        # First, we set the medial surface volume on the background
        slicer.util.setSliceViewerLayers( background = medialSurfaceVolumeNode, foreground = None, label = None )
        # Here we ensure the thickness model is shwon intersecting all planes
        thicknessMapNode.GetDisplayNode().SetSliceIntersectionVisibility(True)
        thicknessMapNode.GetDisplayNode().SetSliceIntersectionThickness(3)
        # And finally we plot the colormap;
        # To generate the colormap, we need to extract the scalar range associated with the model
        scalars                                                     = vtk_to_numpy( thicknessMapNode.GetPolyData().GetPointData().GetScalars() )
        maxThickness                                                = np.max( scalars )
        minThickness                                                = np.min( scalars )
        avgThickness                                                = np.mean( scalars )

        colorTableTitle                                             = "Medial Thickness (mm)"
        labelFormat                                                 = "%4.1f mm"
        colorTableRange                                             = maxThickness
        # Create color node
        colorNode = slicer.mrmlScene.CreateNodeByClass("vtkMRMLProceduralColorNode")
        colorNode.UnRegister(None)  # to prevent memory leaks
        colorNode.SetName(slicer.mrmlScene.GenerateUniqueName("MedialThicknessMap"))
        colorNode.SetAttribute("Category", "MedialThicknessModule")
        # The color node is a procedural color node, which is saved using a storage node.
        # Hidden nodes are not saved if they use a storage node, therefore
        # the color node must be visible.
        colorNode.SetHideFromEditors(False)
        slicer.mrmlScene.AddNode(colorNode)
        # Specify colormap
        colorMap = colorNode.GetColorTransferFunction()
        colorMap.RemoveAllPoints()
        colorMap.AddRGBPoint(0.0, 0.66, 0.0, 1.0)
        colorMap.AddRGBPoint(0.5, 1.0, 0.0, 1.0)
        colorMap.AddRGBPoint(1.0, 1.0, 0.33, 1.0)
        colorMap.AddRGBPoint(1.5, 1.0, 1.0, 1.0)
        colorMap.AddRGBPoint(2.0, 0.33, 1.0, 1.0)
        colorMap.AddRGBPoint(2.0, 0.0, 1.0, 1.0)
        colorMap.AddRGBPoint(maxThickness, 0.0, 0.66, 1.0)
        # Display color legend
        thicknessMapNode.GetDisplayNode().SetAndObserveColorNodeID(colorNode.GetID())
        colorLegendDisplayNode = slicer.modules.colors.logic().AddDefaultColorLegendDisplayNode(thicknessMapNode)
        colorLegendDisplayNode.SetTitleText(colorTableTitle)
        colorLegendDisplayNode.SetLabelFormat(labelFormat)
        

        # Status
        if (verbose):
            print( "Thickness Mapping Completed...!" )
</code></pre>

---

## Post #8 by @Bor_Antolic (2022-12-08 13:36 UTC)

<p>Hi!<br>
I just started working on this problem - how to get thickness map from cardiac CT in order to visualize scar. Did you manage to find a reproducible workflow?<br>
Thanks!</p>

---

## Post #9 by @DANIELE_COSSELLU (2024-08-01 16:21 UTC)

<p>Hi. I am trying to use this function (Slicer 5.6.2) but I get the error<br>
“AttributeError: ‘MRMLCorePython.vtkMRMLModelNode’  object has no attribute ‘_parameterNode’.”<br>
I used this example code<br>
def createModelFromVolume(inputVolumeNode):<br>
“”“Create surface mesh from volume node using CLI module”“”</p>
<p>parameters = {}<br>
parameters[“InputVolume”] = inputVolumeNode<br>
outputModelNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLModelNode”)<br>
parameters[“OutputGeometry”] = outputModelNode</p>
<p>grayMaker = slicer.modules.grayscalemodelmaker<br>
cliNode = slicer.cli.runSync(grayMaker, None, parameters)</p>
<p>if cliNode.GetStatus() &amp; cliNode.ErrorsMask:</p>
<pre><code>errorText = cliNode.GetErrorText()
slicer.mrmlScene.RemoveNode(cliNode)
raise ValueError("CLI execution failed: " + errorText)
</code></pre>
<p>slicer.mrmlScene.RemoveNode(cliNode)<br>
return outputModelNode<br>
from <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html" class="inline-onebox" rel="noopener nofollow ugc">Python FAQ — 3D Slicer documentation</a> to create the model.<br>
Anyone can help me understand how to go forward?</p>
<p>Thanks, Daniele.</p>

---
