# Centerline Extraction on Bronchoscopy

**Topic ID**: 28900
**Date**: 2023-04-14
**URL**: https://discourse.slicer.org/t/centerline-extraction-on-bronchoscopy/28900

---

## Post #1 by @Komal (2023-04-14 05:36 UTC)

<p>Hi,<br>
Please can you help me to get centerline extraction on bronchoscopy using python ,VMTK and which algorithm I need to use .Please send me the source code of the same.</p>

---

## Post #2 by @lassoan (2023-04-15 03:20 UTC)

<p>You first need to segment the airways and then you can use VMTK extension to extract the centerline. You can find tutorials on YouTube and source code on Github (<a href="https://github.com/Slicer/Slicer" class="inline-onebox">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a>, <a href="https://github.com/vmtk/SlicerExtension-VMTK" class="inline-onebox">GitHub - vmtk/SlicerExtension-VMTK</a>).</p>

---

## Post #3 by @Komal (2023-04-17 07:21 UTC)

<p>Hi,<br>
Thank you<br>
Actually I want simple code like which consist STL file airway tree and algorithm  to extract centerline. I am getting like this output ,please can you help me.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51275f7a80c9ec949fc9f8b557286c8c8f2ac298.png" data-download-href="/uploads/short-url/bzV1WhpHsN6WOlhdvmDFcdofMgg.png?dl=1" title="airwayoutput" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51275f7a80c9ec949fc9f8b557286c8c8f2ac298_2_690x368.png" alt="airwayoutput" data-base62-sha1="bzV1WhpHsN6WOlhdvmDFcdofMgg" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51275f7a80c9ec949fc9f8b557286c8c8f2ac298_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51275f7a80c9ec949fc9f8b557286c8c8f2ac298_2_1035x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/51275f7a80c9ec949fc9f8b557286c8c8f2ac298_2_1380x736.png 2x" data-dominant-color="24243C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">airwayoutput</span><span class="informations">1600×855 74.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @rbumm (2023-04-17 12:17 UTC)

<p>You’ll need to generate an airway segmentation similar to the one that you showed in your image. You can use the Lung CT Segmenter (part of Lung CT Analyzer extension) for that in connection with a thin sliced lung CT tissue kernel. Then you should hollow the structure with 3D Slicers Segment Editor and follow <a class="mention" href="/u/lassoan">@lassoan</a>’s advice/link in the above post.</p>

---

## Post #5 by @lassoan (2023-04-17 13:01 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="4" data-topic="28900">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Then you should hollow the structure with 3D Slicers Segment Editor</p>
</blockquote>
</aside>
<p>Clarification: for centerline extraction you need a segment that contains the airway lumen. If you hollow the airways (for visualization, 3D printing, etc.) then do it after the centerline extraction or keep a copy of the lumen segment.</p>

---

## Post #6 by @rbumm (2023-04-17 13:15 UTC)

<p>That is a very important point, thanks for the clarification. It even spins some ideas for pulmonary vessels, which I thought must be hollowed for VMTK.</p>

---

## Post #7 by @Komal (2023-04-21 05:57 UTC)

<p>Ok Thank you,<br>
I installed vmtk in visual studio code. I want to build  vmtk in visual studio 2019 professional,<br>
how can I do ? please help .</p>

---

## Post #8 by @lassoan (2023-04-21 21:24 UTC)

<p>All the tools are built and made conveniently available as Slicer extensions that you can use in either Python or C++.</p>
<p>If you want to build the underlying libraries yourself and implement and application that integrates all the tools then it is a lot of work and you have to do it all yourself. But to give some help with getting started:</p>
<ul>
<li>VMTK can compute the centerline from airways segmentation. You can configure and build VMTK using CMake. There are no prerequisites or any special configuration options, everything just works with default settings.</li>
<li>For segmenting the airways you can use semi-automatic methods in Slicer or CIP or you can try various neural network based automatic segmentation tools.</li>
</ul>

---
