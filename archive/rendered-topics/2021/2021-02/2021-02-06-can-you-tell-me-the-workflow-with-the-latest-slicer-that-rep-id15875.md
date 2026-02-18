# Can you tell me the workflow with the latest Slicer that reproduces what I am used to in 4.9.0

**Topic ID**: 15875
**Date**: 2021-02-06
**URL**: https://discourse.slicer.org/t/can-you-tell-me-the-workflow-with-the-latest-slicer-that-reproduces-what-i-am-used-to-in-4-9-0/15875

---

## Post #1 by @TudorSlicer (2021-02-06 17:47 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.9.0</p>
<p>I am familiar with using Slicer to take a CT of a limb to make an .stl file of a single bone for printing<br>
My work flow using the old version of slicer was basically<br>
Load Dicom/Volume Rendering/All modules - Crop Volume/Threshold Effect/Island effect/Make model<br>
In the latest version I cannot see how to crop and go beyond that step.  Is there an idiot’s guide for the later version</p>
<p>I have a second question.   When I make a model of the scaphoid (using the older version) the scaphoid is holy.   Is there a way to fill in the holes?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2021-02-06 18:38 UTC)

<p>It should be basically the same workflow.  The Crop Volume module is the same but now you can use the Segment Editor’s Threshold and Island effects.  You can click the Show 3D button and then in the Segmentations module you can export directly to STL.  To fill holes you probably want the <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">Wrap Solidify</a> extension.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22c58a1260c66e32dfaeab9444f8327c3398204a.jpeg" data-download-href="/uploads/short-url/4XBswzhgt5eqjJlQqXxIIolS7zk.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22c58a1260c66e32dfaeab9444f8327c3398204a_2_661x500.jpeg" alt="image" data-base62-sha1="4XBswzhgt5eqjJlQqXxIIolS7zk" width="661" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/22c58a1260c66e32dfaeab9444f8327c3398204a_2_661x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22c58a1260c66e32dfaeab9444f8327c3398204a.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22c58a1260c66e32dfaeab9444f8327c3398204a.jpeg 2x" data-dominant-color="F5F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">791×598 76.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @TudorSlicer (2021-02-08 15:32 UTC)

<p>Thanks for the reply.  I start with Volume Rendering and reduce the selection to the area that I want.  However then I cannot find the list of modules that includes Crop<br>
What I see is<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1db29a71e42a41ede35212685f55d8dc80299b3.png" data-download-href="/uploads/short-url/pno46tOBXPlNaYWArnRsgTAux35.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1db29a71e42a41ede35212685f55d8dc80299b3_2_354x500.png" alt="image" data-base62-sha1="pno46tOBXPlNaYWArnRsgTAux35" width="354" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1db29a71e42a41ede35212685f55d8dc80299b3_2_354x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1db29a71e42a41ede35212685f55d8dc80299b3_2_531x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b1db29a71e42a41ede35212685f55d8dc80299b3_2_708x1000.png 2x" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">837×1179 28.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I am sorry for being dim but where is the list of all the modules???<br>
This is how they appear in the older version<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83972a63f05f3ee2dc75ac660b142d07754bb815.png" data-download-href="/uploads/short-url/iM6q0cfL4f0wpBmtp8rLybZOLel.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83972a63f05f3ee2dc75ac660b142d07754bb815_2_651x500.png" alt="image" data-base62-sha1="iM6q0cfL4f0wpBmtp8rLybZOLel" width="651" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83972a63f05f3ee2dc75ac660b142d07754bb815_2_651x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83972a63f05f3ee2dc75ac660b142d07754bb815_2_976x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83972a63f05f3ee2dc75ac660b142d07754bb815_2_1302x1000.png 2x" data-dominant-color="F6F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1545×1185 80.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2021-02-08 15:59 UTC)

<p>That view of all modules is deprecated. Use the search function to obtain the list of modules:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70530dec30e78e3b3ce1b02d482842a5207f07e3.png" alt="image" data-base62-sha1="g1Fq23xM6HKADqr58ay7bIUgoQH" width="616" height="410"></p>

---

## Post #5 by @TudorSlicer (2021-02-09 10:52 UTC)

<p>Great,   Now found the Crop Module<br>
I would like to install the SurfaceWrap  extension.  I have found it in Github but would like to avoid the pain of the manual install.  I cannot find it listed in Extension Manager.   Should it be there?<br>
Thanks</p>

---

## Post #6 by @pieper (2021-02-09 14:29 UTC)

<p>Yes, it’s in the extension manager for the current release.  Should also be there for the nightly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9181b1626aaa62f27d461ad8cf255f7c547e3233.jpeg" data-download-href="/uploads/short-url/kLd68vPJKFyUtvHVRoPL6d7r48X.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9181b1626aaa62f27d461ad8cf255f7c547e3233_2_690x384.jpeg" alt="image" data-base62-sha1="kLd68vPJKFyUtvHVRoPL6d7r48X" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9181b1626aaa62f27d461ad8cf255f7c547e3233_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9181b1626aaa62f27d461ad8cf255f7c547e3233.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9181b1626aaa62f27d461ad8cf255f7c547e3233.jpeg 2x" data-dominant-color="E2E4E5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">909×506 88.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
