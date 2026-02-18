# Unable to do 3D rendering from a sequence of tiff images

**Topic ID**: 1345
**Date**: 2017-11-01
**URL**: https://discourse.slicer.org/t/unable-to-do-3d-rendering-from-a-sequence-of-tiff-images/1345

---

## Post #1 by @Dadep (2017-11-01 12:46 UTC)

<p>Operating system: linux ubuntu16 64bits<br>
Slicer version: 4.8.0<br>
Expected behavior: load and render volume from 20 slices (gray scale) tiff images file<br>
Actual behavior: able to load file, appear in the Red windows only, no volume rendering.</p>

---

## Post #2 by @jcfr (2017-11-01 12:50 UTC)

<p>Hi,</p>
<p>Could you confirm that you followed these steps to load the data:</p>
<ul>
<li>Click on “Add Data”</li>
<li>Select one of the image</li>
<li>Click “Option” -&gt; Uncheck  “Single File”</li>
</ul>
<p>and load.</p>
<p>We want to make sure all images have been loaded into one “volume”.</p>
<p>Also, what do you you mean by “volume rendering” ? Did you go to:</p>
<ul>
<li>VolumeRendering module</li>
<li>Selected the corresponding volume node (of not already selected)</li>
<li>Selected CPU or CPU technique</li>
<li>Clicked on the <strong>eye icon</strong>
</li>
</ul>

---

## Post #3 by @lassoan (2017-11-01 12:52 UTC)

<p>See also this FAQ: <a href="https://www.slicer.org/wiki/Documentation/4.6/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F">https://www.slicer.org/wiki/Documentation/4.6/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F</a></p>

---

## Post #4 by @Dadep (2017-11-01 13:17 UTC)

<p>Thanks a lot it work !!<br>
The problem was that I was using the volume rendering module…<br>
thx again !</p>

---

## Post #5 by @Alessia_Longoni (2022-01-26 23:32 UTC)

<p>Hi!<br>
I am a new user of 3D slicer and I have exactly the same problem. I am trying to upload a series of slices in .tiff format. I can see my stack in the red section but in the yellow and green I have only a thin line. I don’t really understand what I need to change based on the other explanation in this post. Could you please help me?</p>
<p>Thanks!</p>

---

## Post #6 by @muratmaga (2022-01-27 00:26 UTC)

<p>EIther the slice spacing is wrong in one dimension, or instead of sequence of files you have loaded a single tiff file.</p>
<p>Either way, your life would be easier if you use ImageStacks module within SlicerMorph extension. You can specify correct voxel spacing during the import time, make sure there are as many slices as you expect to see etc…</p>
<p><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks#readme" class="inline-onebox" rel="noopener nofollow ugc">SlicerMorph/Docs/ImageStacks at master · SlicerMorph/SlicerMorph · GitHub</a></p>

---
