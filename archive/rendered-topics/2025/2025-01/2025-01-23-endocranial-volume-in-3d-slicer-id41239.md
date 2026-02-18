# Endocranial volume in 3D Slicer

**Topic ID**: 41239
**Date**: 2025-01-23
**URL**: https://discourse.slicer.org/t/endocranial-volume-in-3d-slicer/41239

---

## Post #1 by @ThomasVanParys (2025-01-23 15:51 UTC)

<p>Hello,</p>
<p>I am segmenting skulls from the NDMDID PM-CT dataset.<br>
I want to measure endocranial volume, or some measure of cranial capacity/brain size. What is best or easiest way to do this from the skull models?<br>
Here is an example image (segmented using Amira Avizo, not 3DSlicer):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb181525f43f25a15a76cd769c23cbb2da93c412.jpeg" data-download-href="/uploads/short-url/qH6SN3j3w6u2n26YULVy2Lvikw2.jpeg?dl=1" title="Skull_lateral" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb181525f43f25a15a76cd769c23cbb2da93c412_2_690x493.jpeg" alt="Skull_lateral" data-base62-sha1="qH6SN3j3w6u2n26YULVy2Lvikw2" width="690" height="493" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb181525f43f25a15a76cd769c23cbb2da93c412_2_690x493.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb181525f43f25a15a76cd769c23cbb2da93c412_2_1035x739.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb181525f43f25a15a76cd769c23cbb2da93c412_2_1380x986.jpeg 2x" data-dominant-color="A4A0B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Skull_lateral</span><span class="informations">1920×1372 72 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do I need to create an endocast or segment the brain to measure the volume?</p>
<p>EDIT: I used SwissSkullStripper on head/neck thin bone CT files to retrieve a volume measurement (see segmentation statistics), is this fairly reliable?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcb51f246c96027d2030870ac9e3498bb2d13ade.png" data-download-href="/uploads/short-url/vut5SzNNoyl4CYAOOjlmZO4m1SS.png?dl=1" title="Screenshot 2025-01-23 154908" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dcb51f246c96027d2030870ac9e3498bb2d13ade_2_690x357.png" alt="Screenshot 2025-01-23 154908" data-base62-sha1="vut5SzNNoyl4CYAOOjlmZO4m1SS" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dcb51f246c96027d2030870ac9e3498bb2d13ade_2_690x357.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dcb51f246c96027d2030870ac9e3498bb2d13ade_2_1035x535.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dcb51f246c96027d2030870ac9e3498bb2d13ade_2_1380x714.png 2x" data-dominant-color="B2AFAA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-01-23 154908</span><span class="informations">1919×993 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Help is much appreciated.<br>
Tom.</p>

---

## Post #2 by @muratmaga (2025-01-23 16:31 UTC)

<p>It is very easy to do endocranial space segmentation in Slicer. You can install the SlicerMorph extension and give SegmentEndoCranium module a try. It uses another extension called WrapSurfaceSolidify, which you can also use directly. That gives you more control over the segmentation:</p>
<p>Tutorial for SegmentEndoCranium (<a href="https://slicermorph.github.io/Endocast_creation.html" class="inline-onebox" rel="noopener nofollow ugc">Cavity Segmentation: Creating Endocasts | SlicerMorph Project</a>)<br>
Tutorial for using WrapSurfaceSolidify directly: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/WaterTightModels" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/WaterTightModels at main · SlicerMorph/Tutorials · GitHub</a> (you are just going to do the largest cavity option).</p>

---

## Post #3 by @ThomasVanParys (2025-01-24 13:05 UTC)

<p>Thank you.</p>
<p>For some reason, SegmentEndocranium is not giving the results I expected:</p>
<ol>
<li>It is taking unusually long to produce</li>
<li>the endocasts themselves are failing, as they go beyond the skull, with distorted shapes.</li>
</ol>
<p>Is swill skull stripper an alternative method to use here to get some volume measure? Tom.</p>

---

## Post #4 by @muratmaga (2025-01-24 16:36 UTC)

<aside class="quote no-group" data-username="ThomasVanParys" data-post="3" data-topic="41239">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ThomasVanParys:</div>
<blockquote>
<p>For some reason, SegmentEndocranium is not giving the results I expected:</p>
</blockquote>
</aside>
<p>It is possible that your scans are very high resolution. For endocranial space segmentation (particularly to get volume of the region), you don’t need that high-resolution.<br>
It is possible that defaults are not good for your dataset. For example if your data is 0.1 mm thick 3.0mm smoothing would be 30x30x30 voxels which would indeed take long and will be unnecessary.</p>
<p>if SegmentEndoCranium didn’t work well, I suggest going straight to WrapSurfaceSolidify extension, which SegmentEndoCranium uses under the hood. It exposes more parameters</p>
<aside class="quote no-group" data-username="ThomasVanParys" data-post="3" data-topic="41239">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/7ea924/48.png" class="avatar"> ThomasVanParys:</div>
<blockquote>
<p>Is swill skull stripper an alternative method to use here to get some volume measure? Tom.</p>
</blockquote>
</aside>
<p>I mean if swill skull stripper is giving you what you want and it is faster, sure.</p>

---

## Post #5 by @philippepellerin (2025-01-26 09:57 UTC)

<p>I do a lot of endocranial volume segmentation. The slicermorph extension is not working properly , as you experienced, but the WarpSurface Solidity is perfect, very effective and quite fast. Just use those settings:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5284e51125b587ecd8d8cce5ed596d05f0cbb40b.png" data-download-href="/uploads/short-url/bLZSspb08MFvn0kFUajVyQwOtUn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5284e51125b587ecd8d8cce5ed596d05f0cbb40b_2_489x500.png" alt="image" data-base62-sha1="bLZSspb08MFvn0kFUajVyQwOtUn" width="489" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5284e51125b587ecd8d8cce5ed596d05f0cbb40b_2_489x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5284e51125b587ecd8d8cce5ed596d05f0cbb40b_2_733x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5284e51125b587ecd8d8cce5ed596d05f0cbb40b_2_978x1000.png 2x" data-dominant-color="E8E9E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1326×1354 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @ThomasVanParys (2025-01-28 15:34 UTC)

<p>Thank you.<br>
I am now using the NMDID provided ‘TRUE_BRAIN’ CT scan for each decedent, which is actually working very well in SegmentEndoCranium (I can also increase the smoothing kernel size). From there, I am getting expected endocast volume measurements in segment statistics, so thank you!<br>
Tom</p>

---
