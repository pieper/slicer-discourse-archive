# High quality segmentation of the orbital walls

**Topic ID**: 2345
**Date**: 2018-03-17
**URL**: https://discourse.slicer.org/t/high-quality-segmentation-of-the-orbital-walls/2345

---

## Post #1 by @Itamartz (2018-03-17 22:15 UTC)

<p>Operating system- Windows 10<br>
Slicer version- 4.8.1</p>
<p>Hello friends,</p>
<p>I would be grateful for your help in solving the following issue- I am having poor results modeling the orbital walls of the skull. After using a threshold segmentation, the orbital walls are filled with many holes.</p>
<p>Following a tip from other thread (<a href="https://discourse.slicer.org/t/model-created-from-skull-ct-looks-lacy-with-many-bony-holes/1744">link</a>), I tried to get better results using the crop volume module (Interpolated cropping + B-spline) before doing a threshold segmentation, and yet, the model is not in the required quality (see picture below).</p>
<p>Do you have ideas for a better workflow?<br>
Or there is no much to do, except post-processing the model in other program (like meshmixer)?</p>
<p>Thank you in progress,<br>
Itamar</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14177770ae2c8652058cdd040d4941f40c395258.jpeg" alt="image" data-base62-sha1="2RJPefHJ8lorFZ1VJ617qHcba0E" width="270" height="207"></p>

---

## Post #2 by @timeanddoctor (2018-03-18 00:15 UTC)

<p>From <a href="https://discourse.slicer.org/t/segmentation-of-thin-surfaces/2332/2:">https://discourse.slicer.org/t/segmentation-of-thin-surfaces/2332/2:</a></p>
<blockquote>
<p>We had very similar problem when segmenting thin orbital bone. Couple of things that helped:</p>
<p>Crop and resample your volume to make the structures that you want to segment at least 4-5 voxel wide. Otherwise all the region-growing based method will fail, as due to random noise a few voxels may be missed and your structure may break to parts.<br>
Apply filtering, which enhances thin structures. We have found that unsharp masking helped.<br>
If the structure that you need to represent is a surface then instead of a volumetric representation, you may try to reconstruct a surface from points. See this complete example3 that works in Slicer as is, See also these additional VTK examples: Poisson surface reconstruction3, comparison of 3 surface reconstruction methods that are available in VTK2. If this approach works well then let me know and I can make a segment editor effect from it.<br>
You may paint the structure manually on a couple of (non-neighbor) slices and use Fill between slices effect to create a complete segmentation out of it.</p>
</blockquote>

---

## Post #3 by @timeanddoctor (2018-03-18 00:20 UTC)

<p>I think you can crop the orbital as a single one by ROI, and then try to follow the method from Andras Lasso <a href="https://discourse.slicer.org/t/segmentation-of-thin-surfaces/2332/2">Segmentation of thin surfaces</a>.<br>
If you succeed please let me know and post some useful picture for the procedure.<br>
Thanks.</p>

---

## Post #4 by @lassoan (2018-03-18 01:15 UTC)

<p>Orbital wall segmentation is very challenging. We have developed a semi-automatic method (described in this <a href="https://qspace.library.queensu.ca/bitstream/handle/1974/15290/Ibrahim_Amani_201612_MSc.pdf?sequence=2&amp;isAllowed=y">Masters thesis</a>) in collaboration with Cari Whyne’s group at Sunnybrook, which fulfilled the clinical requirements for custom 3D-printed surgical guide design, but of course it could be still improved.</p>
<p>Meshmixer, Blender, and other modeling tools are great for modeling and mesh editing. However, a fundamental limitation of using them for “fixing” medical image segmentations is that these modeling software cannot show you the original volumetric image along with the mesh. Therefore, after you finished cleaning up the surface model, you must still read it back into Slicer (or similar medical image visualization software) to verify that the mesh is correct, and make further corrections as needed. You may repeat this process several times, until the end result is acceptable. This workflow is quite inefficient, and since you probably import images from DICOM and perform initial segmentation in Slicer anyway, it just make more sense to do all further post-processing, review, and fixing in Slicer.</p>

---

## Post #5 by @lambrosone (2018-03-18 02:15 UTC)

<p>I am a slicer newbie and have no comment on anything sophisticated with the program. However the orbital floor and walls are extremely this as is the post max sinus. I assumed that this was just from the thinness of the bones which the beam misses.</p>

---

## Post #6 by @lassoan (2018-03-18 03:07 UTC)

<p>Yes, the problem is that the bone is thin, compared to the resolution of the CT image. The beam does not “miss” the bone, but voxels that are partially filled by bone have lower intensity value than voxels that only contain bone (this is known as <em>partial volume effect</em>). Due to noise and variance of voxel intensity in the image, these lower-intensity bone voxels may not be clearly distinguishable from other tissues.</p>

---

## Post #7 by @Itamartz (2018-03-18 19:08 UTC)

<p>Thank you all!! I will try to apply and publish any usful results</p>

---
