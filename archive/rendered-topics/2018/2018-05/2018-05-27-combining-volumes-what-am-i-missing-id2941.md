# Combining volumes - what am I missing?

**Topic ID**: 2941
**Date**: 2018-05-27
**URL**: https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941

---

## Post #1 by @mttctr (2018-05-27 13:10 UTC)

<p>Operating system: Mac - High Sierra<br>
Slicer version: 4.8.1<br>
Expected behavior: One perfect, high resolution volume<br>
Actual behavior: Three volumes, each one being high resolution in only one plane (sagittal, coronal, transverse)</p>
<p>I have been using 3D Slicer for many months and I’m slowly learning the ropes. I am using it to produce anatomical boney models, and have probably created between 10-15 models.</p>
<p>After loading CT scans from their DICOM folder I always get several volumes, often with the precursor ‘ax’, ‘sag’, ‘cor’. Individually these volumes have great resolution in the plane they are named after, but poor voxel resolution in the other two planes. Obviously I can load different volumes into each plane to view them all together, but when I start a label map I seem to be committed at that point to one volume, and so the label map resolution is affected in two of the planes.</p>
<p>Is it possible to recreate one high resolution volume from the three ‘ax’, ‘sag’, ‘cor’ volumes or is this something the Radiology department would have to do for me when they create the DICOM folder?</p>
<p>Help would be much appreciated.</p>
<p>Kind regards</p>
<p>Matt Carter</p>

---

## Post #2 by @lassoan (2018-05-27 19:17 UTC)

<p>In general, these multiple low-resolution acquisitions are not well suited for any 3D processing, so the best would be to acquire proper 3D volume, with as isotropic spacing (cubic voxel shape) as possible.</p>
<p>You may try to find toolkits that can create an isotropic super-resolution image from multiple low-resolution sweeps, but this is a difficult image reconstruction problem, so there are no standard solutions. Have a look at this post <a href="https://discourse.slicer.org/t/import-volume-by-projections/2871/6?u=lassoan">Import volume by projections</a> for info on a toolkit that might be usable.</p>
<p>You may also try to use your volumes for segmentation one by one (since you can swap the master volume any time): Create a high-resolution isotropic volume from any of the input volumes, using Crop volume module. Then create a segmentation node using this isotropic volume as master volume. After this you can switch between master volumes - the segmentation node’s internal binary labelmap representation will remain high-resolution and isotropic. For example, you can segment the structure of interest based on one image, then switch master volume and make adjustments in the segmentation as needed. Unfortunately, this is a manual, iterative process.</p>

---

## Post #4 by @kopachini (2019-12-04 17:22 UTC)

<p>Hi Matt,<br>
your problem is that these sequences aren’t isovoxel… they are acquired only in one plane (coronal), thus only coronal plane is sharp with good spatial resolution and the other two are “pixelized” (not a good description, but you get it).<br>
What you need is that sequences you want to perform segmentation from must be isovoxel (3D)… tell your surgeon to ask radiology technician or radiologist to add isovoxel sequence in the next study. Most of them have -iso or -space adjective in their name (I have the best experience with postcontrast T1 iso or iso T2 sequences).<br>
Or do what Andrass wrote <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #5 by @lassoan (2021-01-18 23:59 UTC)

<p>See a related discussion here: <a href="https://discourse.itk.org/t/mri-isotropic-volume-reconstruction-from-2d-slices/3764/5" class="inline-onebox">MRI isotropic volume reconstruction from 2D slices - Beginner Questions - ITK</a>. NiftyMIC is recommended there, which is readily usable for fetal MRI image reconstruction and may be adaptable to other kind of images.</p>

---

## Post #6 by @lassoan (2021-03-18 18:33 UTC)

<p>Suggestion from <a class="mention" href="/u/pieper">@pieper</a>:</p>
<blockquote>
<p>A colleague suggested this work and the SMORE technique from Jerry Prince’s group at JHU.  I don’t know if there’s an implementation available.</p>
<p><a href="https://arxiv.org/pdf/1802.09431.pdf">https://arxiv.org/pdf/1802.09431.pdf</a></p>
<p><a href="http://www.cs.jhu.edu/cista/455/Lectures/Segmentation-2%20%28Rev%20D%29.pdf">http://www.cs.jhu.edu/cista/455/Lectures/Segmentation-2%20(Rev%20D).pdf</a></p>
</blockquote>

---

## Post #7 by @pieper (2021-03-18 18:35 UTC)

<p>I know one of the authors and if someone would like to make an extension I could see if there is code available.</p>

---

## Post #8 by @lassoan (2021-03-18 18:40 UTC)

<p>Results from SMORE technique looks very impressive, it would be great if we could try it. It can only use a single image stack as input, which is not ideal, but it should be a significant improvement over standard bspline interpolation.</p>

---

## Post #9 by @pieper (2021-03-19 13:54 UTC)

<p>The folks at JHU were able to send me more info and a link to the singularity image.  It’s GPL licensed (may even be patented) but it should be possible to run it on your data.  I’m sure they would appreciate citations and any feedback.</p>
<p><a href="http://iacl.ece.jhu.edu/index.php?title=ISMORE" class="onebox" target="_blank" rel="noopener">http://iacl.ece.jhu.edu/index.php?title=ISMORE</a></p>

---

## Post #10 by @timeanddoctor (2021-03-21 12:27 UTC)

<p>Can we use it in 3d slicer?</p>

---

## Post #11 by @pieper (2021-03-21 13:52 UTC)

<p>Probably you can use it stand alone outside of Slicer and then import the results.  If it looks promising someone could wrap it as an extension (making sure to flag the license and potential IP issues).</p>

---

## Post #12 by @Dimitrios_Rallios (2022-11-21 19:52 UTC)

<p>I go the link as well but ,apart from downloading it, I can not do much with it. I am just a medical student. Do you have any clue how to run the program? Do I need to install it somehow??</p>
<p>Thanks for taking the time to explain and suggest solutions.</p>
<p>Best Regards,<br>
Dimitrios Rallios</p>

---

## Post #13 by @pieper (2022-11-21 19:56 UTC)

<p>You should contact the authors for instructions.</p>

---
