# Hollow tool - thickness

**Topic ID**: 16648
**Date**: 2021-03-19
**URL**: https://discourse.slicer.org/t/hollow-tool-thickness/16648

---

## Post #1 by @Larissa_C (2021-03-19 16:28 UTC)

<p>Operating system: Windowns 10 / 64 bit<br>
Slicer version: 4.11</p>
<p>I am building bolus for use in radiotherapy.<br>
I used three steps:<br>
1º Segmentation of a patient’s outer surface.<br>
2º Cut the area of interest (this area represents the bolus)<br>
3º Addition of the thickness with the Hollow tool (medium surface). The problem is that I add a thickness, but when I do the measurement, the thickness does not match.</p>
<p>Obs: I tried to use the “external and internal surface”, but the object becomes hollow. The object to be printed cannot contain air, so “medium surface” was the one that worked.</p>
<p>I need the exact thickness of 5mm. Can anybody help me? Thanks!</p>

---

## Post #2 by @lassoan (2021-03-19 18:33 UTC)

<aside class="quote no-group" data-username="Larissa_C" data-post="1" data-topic="16648">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/b5a626/48.png" class="avatar"> Larissa_C:</div>
<blockquote>
<p>Addition of the thickness with the Hollow tool (medium surface). The problem is that I add a thickness, but when I do the measurement, the thickness does not match.</p>
</blockquote>
</aside>
<p>You want to be able to place the printed bolus on the skin, so you need to use the segmented surface as inside surface (not as medial surface).</p>
<p>You set the requested thickness. The actual thickness is limited by the resolution of the volume and it is displayed below the requested thickness:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0eb5ac1773d9bddec14e0197cd1444304fee8c48.png" data-download-href="/uploads/short-url/267ULndsdV8Xfbopz0XcJLSOYli.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0eb5ac1773d9bddec14e0197cd1444304fee8c48.png" alt="image" data-base62-sha1="267ULndsdV8Xfbopz0XcJLSOYli" width="690" height="285" data-dominant-color="353534"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1049×434 16.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You have several options to address this:</p>
<ul>
<li>You can either crop and resample the volume to have finer resolution using Crop volume module (before segmenting).</li>
<li>Export the skin surface to a model (surface mesh), clip the model (using Dynamic Modeler module or Surface Clip or Easy Clip extensions, or within about a week there will be a very convenient option for this, because you will be able to use a markups ROI for clipping in Dynamic Modeler), and then use Hollow tool in Dynamic modeler to give an exact thickness to the model. Hollow tool in Dynamic modeler linearly extrudes the model in surface normal direction, so in presence of small sharp features it can create self-intersecting mesh, which the 3D printing software may complain about. In case this happens, you can either apply slight smoothing to the segmentation before exporting to model; or fix up the final mesh in the printing software (or use Option A).</li>
</ul>

---

## Post #3 by @Larissa_C (2021-03-30 21:53 UTC)

<p>So for my specific case (image), should I use 5.6 to be 5 mm thick? After creating the shell, I must delete (image) the segmentation using island tool, right?</p>
<blockquote>
<p><img alt="" width="20" height="20" src="https://avatars.discourse-cdn.com/v4/letter/l/b5a626/40.png">Larissa_C:</p>
<p>Addition of the thickness with the Hollow tool (medium surface). The problem is that I add a thickness, but when I do the measurement, the thickness does not match.</p>
</blockquote>
<p>You want to be able to place the printed bolus on the skin, so you need to use the segmented surface as inside surface (not as medial surface).</p>
<p>You set the requested thickness. The actual thickness is limited by the resolution of the volume and it is displayed below the requested thickness:</p>
<p>You have several options to address this:</p>
<ul>
<li>You can either crop and resample the volume to have finer resolution using Crop volume module (before segmenting).</li>
<li>Export the skin surface to a model (surface mesh), clip the model (using Dynamic Modeler module or Surface Clip or Easy Clip extensions, or within about a week there will be a very convenient option for this, because you will be able to use a markups ROI for clipping in Dynamic Modeler), and then use Hollow tool in Dynamic modeler to give an exact thickness to the model. Hollow tool in Dynamic modeler linearly extrudes the model in surface normal direction, so in presence of small sharp features it can create self-intersecting mesh, which the 3D printing software may complain about. In case this happens, you can either apply slight smoothing to the segmentation before exporting to model; or fix up the final mesh in the printing software (or use Option A).</li>
</ul>
<p>–<br>
<em>Previous Replies</em><br>
Operating system: Windowns 10 / 64 bit<br>
Slicer version: 4.11</p>
<p>I am building bolus for use in radiotherapy.<br>
I used three steps:<br>
1º Segmentation of a patient’s outer surface.<br>
2º Cut the area of interest (this area represents the bolus)<br>
3º Addition of the thickness with the Hollow tool (medium surface). The problem is that I add a thickness, but when I do the measurement, the thickness does not match.</p>
<p>Obs: I tried to use the “external and internal surface”, but the object becomes hollow. The object to be printed cannot contain air, so “medium surface” was the one that worked.</p>
<p>I need the exact thickness of 5mm. Can anybody help me? Thanks!</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2627b4292bafa7b584744f13386b362c636ff556.png" alt="Espessura_5 mm.png" data-base62-sha1="5rxcWxatGVG1iShsfYJe2Am90do" width="526" height="251"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/548a3c8db9d90c7c93b332f7328365a7d1c746fd.png" data-download-href="/uploads/short-url/c3ShenlhkyipsnNQuFYTLxJECzX.png?dl=1" title="Seg+shell.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/548a3c8db9d90c7c93b332f7328365a7d1c746fd_2_690x413.png" alt="Seg+shell.png" data-base62-sha1="c3ShenlhkyipsnNQuFYTLxJECzX" width="690" height="413" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/548a3c8db9d90c7c93b332f7328365a7d1c746fd_2_690x413.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/548a3c8db9d90c7c93b332f7328365a7d1c746fd.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/548a3c8db9d90c7c93b332f7328365a7d1c746fd.png 2x" data-dominant-color="BABABA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Seg+shell.png</span><span class="informations">769×461 24.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @mau_igna_06 (2021-03-31 12:26 UTC)

<p>One option is to do a hollow with 5mm (inside surface) of all the skin then cut with the scissors the wanted area. Then export that segment to a model and save it as .stl and is ready to print</p>

---

## Post #5 by @slicer365 (2021-03-31 13:58 UTC)

<p>Adjust the threshold until the entire head is completely wrapped, then select the Hollow tool. Note that if the sinuses are not wrapped, you need to do it manually, then use Hollow, and then use scissors to cut</p>

---

## Post #6 by @Larissa_C (2021-05-03 12:24 UTC)

<p>It worked. Thank you!!!</p>

---
