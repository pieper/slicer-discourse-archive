---
topic_id: 1744
title: "Model Created From Skull Ct Looks Lacy With Many Bony Holes"
date: 2017-12-30
url: https://discourse.slicer.org/t/1744
---

# Model created from skull CT looks lacy with many bony holes

**Topic ID**: 1744
**Date**: 2017-12-30
**URL**: https://discourse.slicer.org/t/model-created-from-skull-ct-looks-lacy-with-many-bony-holes/1744

---

## Post #1 by @lambrosone (2017-12-30 12:41 UTC)

<p>Operating system: WIN 10<br>
Slicer version: 4.6.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Newbie to slicer. My skull ct model frequently come out lacy with many holes. Is this because of my processing inSlicer? How do I correct it to get more solid models</p>

---

## Post #2 by @lassoan (2017-12-30 15:35 UTC)

<p>Holes in the model caused by image noise. There are many factors to consider when you acquire an image: minimize radiation dose, acquisition time, image noise, voxel size, equipment cost, restraining of patient, etc.</p>
<p>If you have the option of using better imaging equipment, or increase radiation dose (for example, because you are imaging cadavers and imaging dose is not a concern) then just do that and you may get nearly perfect models by simple thresholding.</p>
<p>Alternatively, you can use more sophisticated segmentation and pre/post-processing methods. Download latest version of Slicer (at least 4.8), use Segment editor module, create initial segmentation using Threshold effect, then fill holes using Smoothing effect. If results are not satisfactory, then pre-process the input image using Crop volume module (set isotropic spacing, as shown <a href="https://youtu.be/BJoIexIvtGo?t=15s">here</a>) and maybe also try Anisotropic smoothing.</p>
<p>I would also recommend to check out segmentation tutorials on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">Slicer training page</a>.</p>

---

## Post #3 by @lambrosone (2017-12-30 19:14 UTC)

<p>Thank you very much. Does the quality of the image seen  in volume rendering have any bearing on the final result?<br>
How do I tell when thresholding is right? There is a range when the color cycles… at what point in the range is the best choice?</p>
<p>Val</p>

---

## Post #4 by @lassoan (2017-12-30 22:04 UTC)

<p>Volume rendering does not need a hard threshold, so visually volume rendering gives nicer, smoother results. If you only need to visualize bone surface then you can just use volume rendering.</p>
<p>If you need surface model (for quantification, exporting to modeling software, 3D printing, etc.) then you need to segment the volume. Threshold effect gives a real-time preview, so the best is to adjust threshold sliders so that structures that you need are highlighted and nothing else. If you use higher thresholds then image noise will result in holes (that you can later fill), while if you use lower threshold value then the surface will have extrusions (that you can later remove).</p>

---

## Post #5 by @lambrosone (2017-12-31 18:14 UTC)

<p>Thank you very much.</p>

---

## Post #6 by @lambrosone (2018-01-01 23:06 UTC)

<p>If I may ask a further question, if the laciness and holes in the bony model, especially at the infraorbital foramen,  come from  image noise, why is this noise not visible in the standard 3 axis view?</p>
<p>I suspect I have been overthreholding.</p>
<p>Thanks</p>
<p>happy new year.</p>
<p>Val</p>

---

## Post #7 by @lassoan (2018-01-01 23:32 UTC)

<p>Human vision can recognize structures in noisy images. You may not even realize the noise level (unless you increase the display contrast).</p>
<p>Note that by noise I mean all kinds of effects and artifacts that may affect CT images, such as partial volume effect (that makes thin bones appear darker), streak artifacts due to metal implants or bones, motion artifacts, etc. Strategy to deal with these depend on what exactly you need to segment and for what clinical purpose.</p>

---
