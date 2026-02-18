# Airway segmentation

**Topic ID**: 8940
**Date**: 2019-10-29
**URL**: https://discourse.slicer.org/t/airway-segmentation/8940

---

## Post #1 by @Kedar_Hibare (2019-10-29 12:09 UTC)

<p>Hi, I am new to 3D slicer and I am learning by trial and error airway segmentation so that I can design airway prosthesis (airway stents). I wish to 3D print the same after doing so. I haven’t been able to master it with accuracy. Any help with video links / ppts would be appreciated to do (airway segmentation) this as accurately as possible. Thank you in advance<br>
Regards<br>
KrH</p>

---

## Post #2 by @timeanddoctor (2019-10-29 13:42 UTC)

<p>Did you segment the airway and smoothing it from the DICOMs?</p>

---

## Post #3 by @Kedar_Hibare (2019-10-30 07:33 UTC)

<p>I have gone through tutorials and my workflow so far:</p>
<ol>
<li>Crop and identify ROI</li>
<li>Segment Editor and create 2 segments one trachea and other</li>
<li>Use paint and grow seed tools and create 3D</li>
</ol>
<p>I am yet to learn to make it hollow and print it…</p>
<p>My plan is to use it to redesign tracheas with stenosis / tumors and be able to see if we could predict the end of procedure / prosthesis insertions like stents accurately to the anatomy</p>
<p>Can any of you help me with more steps to be able to do this better?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc2831cbabc577a39cafc9af5271987e52d75a8e.jpeg" data-download-href="/uploads/short-url/zYGrd8HIb7bvQ543RTj3R19Me2G.jpeg?dl=1" title="46%20AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc2831cbabc577a39cafc9af5271987e52d75a8e_2_420x500.jpeg" alt="46%20AM" data-base62-sha1="zYGrd8HIb7bvQ543RTj3R19Me2G" width="420" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc2831cbabc577a39cafc9af5271987e52d75a8e_2_420x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc2831cbabc577a39cafc9af5271987e52d75a8e_2_630x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc2831cbabc577a39cafc9af5271987e52d75a8e_2_840x1000.jpeg 2x" data-dominant-color="424242"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">46%20AM</span><span class="informations">1214×1442 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Regards<br>
KrH</p>

---

## Post #4 by @Leon (2019-10-31 12:05 UTC)

<p>Your segmentation looks nice!</p>
<p>You say that your plan is to make it hollow.</p>
<ul>
<li>First export it as a STL, which is hollow by itself because it’s only the surface.</li>
<li>Import the STL into a 3D-modeler (I use Blender).</li>
<li>Cut of the ends and than you’re left with a hollow construct.</li>
<li>Use a modifier (in Blender choose ‘Solidify’) and give the STL some thickness and you’re done.</li>
<li>Export as a STL for printing.</li>
</ul>

---

## Post #5 by @Alice (2020-08-03 08:19 UTC)

<p>Are you using the airway segmentation function?<br>
If I use THE 3D SLicer with integrated CIP, the error will not be reported. If I use the ordinary 3D SLicer and then load CIP, the error will not be reported. However, the 3D image cannot be displayed and further calculation cannot be carried out</p>

---
