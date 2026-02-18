# Volumetric mesh from CT file?

**Topic ID**: 21611
**Date**: 2022-01-25
**URL**: https://discourse.slicer.org/t/volumetric-mesh-from-ct-file/21611

---

## Post #1 by @Vasko (2022-01-25 01:46 UTC)

<p>Hello,</p>
<p>I’ve recently discovered the 3D Slicer and it’s possibilities. I’m beginning to work on project for analysis of occlusal stress distribution in cantilever dental bridges. Our starting point is CT file of the jaws with teeth and from 3D slicer we need volumetric mesh which would be implemented in the FE software for the analysis.<br>
I saw that 3D Slicer has extension (Segment Mesher) which could generate the required volumetric mesh. But, so far I’ve information that it works only with MR files? If this is right what are your suggestions for my future work?</p>

---

## Post #2 by @DIV (2022-01-25 11:29 UTC)

<p>Hello, Vasko.<br>
I have not been using the <a href="https://discourse.slicer.org/t/volumetric-mesh-from-ct-file/21611">Segment Mesher</a>, but I expect that it should work perfectly with CT data.  The reason is that the Segment Mesher will be applied to a <code>Segment</code>.<br>
<em>3D Slicer</em> is capable of creating <code>Segment</code>s from CT scan data, MRI scan data, PET scan data, and many other types of image data.</p>
<p>AFAIK, the Segment Mesher tutorial just happens to use MRI data to provide one example.</p>
<p>On the other hand, there may also be other (alternative) workflows that you can also consider, such as exporting the <code>Segment</code> (geometry) from <em>3D Slicer</em>, and then meshing it in your own FE software?</p>
<p>—DIV</p>

---

## Post #3 by @Vasko (2022-02-01 21:51 UTC)

<p>Hello DIV,</p>
<p>thank You for the reply. Can You tell me more about the alternative way You mentioned: “exporting the <code>Segment</code> (geometry) from <em>3D Slicer</em> , and then meshing it in your own FE software”</p>
<p>What kind of data can I export in order to be able to create 3D FE model? Maybe You can point some tutorial where I can read more about it?</p>

---

## Post #4 by @DIV (2022-02-02 05:52 UTC)

<p>Hello, Vasko.<br>
I think you can get some guidance from the online documentation.  In particular the documentation about <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-model-surface-mesh-file" rel="noopener nofollow ugc">Segmentation</a> mentions the core ability to export segments in <code>STL</code> and/or <code>OBJ</code> format.<br>
You can find various <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" rel="noopener nofollow ugc">segmentation tutorials for <em>3D Slicer</em></a> online too.</p>
<p>As for the later step of importing it into FE software, others who’ve tried that workflow may have more detailed recommendations.</p>
<p>—DIV</p>

---

## Post #5 by @Vasko (2022-05-13 14:59 UTC)

<p>Hi DIV,</p>
<p>can You tell me why the Segment Mesher is not appearing in the Segmentation drop menu? As You can see I’ve previously installed it through the Extension Manager, also I’ve restarted the 3d Slicer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9cd9df5a6d8dd6f3f3a0fd3d3735ebcdc4bbca51.png" data-download-href="/uploads/short-url/mnzh391KSPlyJt7KLBK2hGPbo0p.png?dl=1" title="segmentmesher" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cd9df5a6d8dd6f3f3a0fd3d3735ebcdc4bbca51_2_649x500.png" alt="segmentmesher" data-base62-sha1="mnzh391KSPlyJt7KLBK2hGPbo0p" width="649" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cd9df5a6d8dd6f3f3a0fd3d3735ebcdc4bbca51_2_649x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cd9df5a6d8dd6f3f3a0fd3d3735ebcdc4bbca51_2_973x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9cd9df5a6d8dd6f3f3a0fd3d3735ebcdc4bbca51_2_1298x1000.png 2x" data-dominant-color="CBCBD6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentmesher</span><span class="informations">1366×1052 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank You for he reply,<br>
Vasko</p>

---

## Post #6 by @DIV (2022-05-15 15:08 UTC)

<p>Hello, Vasko.</p>
<p>A few points…</p>
<ul>
<li>
<p>Consider updating to the <strong>latest version</strong> of <em>3D Slicer</em>.</p>
</li>
<li>
<p>Ensure that you’ve <strong>restarted</strong> the application after installing that extension.</p>
</li>
<li>
<p>The drop-down menu you mentioned is not specifically a drop-down “Segmentation menu”, rather it is a drop-down <em>Module</em> menu, and it is possible that extensions might appear in some <strong>sub-menu</strong> there.  [<em>The only reason that “Segmentations” appears at the top of your list is that you must have clicked to use that particular Module most recently.</em>]<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25542059be405a810d3cebdf7c6403e11ba5e2b2.png" data-download-href="/uploads/short-url/5kdUbTQvHYzy5xLEiNUhks5JvOO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25542059be405a810d3cebdf7c6403e11ba5e2b2_2_450x500.png" alt="image" data-base62-sha1="5kdUbTQvHYzy5xLEiNUhks5JvOO" width="450" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25542059be405a810d3cebdf7c6403e11ba5e2b2_2_450x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25542059be405a810d3cebdf7c6403e11ba5e2b2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25542059be405a810d3cebdf7c6403e11ba5e2b2.png 2x" data-dominant-color="D9DBE9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">632×701 53 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Have you tried clicking the “<strong>Find module</strong>” search button [magnifying glass icon] immediately to the left of that drop-down <em>Module</em> menu?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/adfb55c08e4bb0578dca025f82996af51ce22e9b.png" alt="image" data-base62-sha1="oP75h22FWpwlsbPLgXj7A7dfSAj" width="676" height="445"></p>
</li>
</ul>
<p>I have installed the extension, and can access it by following the above steps.</p>
<p>—DIV</p>

---

## Post #7 by @Vasko (2022-07-08 23:58 UTC)

<p>Hi DIV,</p>
<p>thank You for your support with the past replies. Recently I was practicing conversion of STL file (surface mesh) to appropriate ASCII file for my FE-Software.<br>
Now I’m back to the volumetric mesh again. I was following the procedure from GitHub, and I was trying to implement it on a CT scan of a teeth. I want to make volumetric mesh for one specific tooth. Unfortunately I have problem with displaying the results.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91810d11796185fd208a203af08c3b3da23f46c3.jpeg" data-download-href="/uploads/short-url/kLbISkcpfXmc5jhdVp6Un1RRy83.jpeg?dl=1" title="display" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91810d11796185fd208a203af08c3b3da23f46c3_2_623x500.jpeg" alt="display" data-base62-sha1="kLbISkcpfXmc5jhdVp6Un1RRy83" width="623" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91810d11796185fd208a203af08c3b3da23f46c3_2_623x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91810d11796185fd208a203af08c3b3da23f46c3_2_934x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91810d11796185fd208a203af08c3b3da23f46c3_2_1246x1000.jpeg 2x" data-dominant-color="C2C1C3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">display</span><span class="informations">1862×1494 227 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I’ll be very thankful if You can help me with some hints to sort this out.</p>
<p>Best regards,<br>
Vasko</p>

---
