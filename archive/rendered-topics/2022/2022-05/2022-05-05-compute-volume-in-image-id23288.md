# Compute volume in image

**Topic ID**: 23288
**Date**: 2022-05-05
**URL**: https://discourse.slicer.org/t/compute-volume-in-image/23288

---

## Post #1 by @Qazi (2022-05-05 15:28 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
I have converted my dataset from 16bit to 8 bit and then used the data to calculate volume but the values (for volume) I get are quite unrealistic rather very far from being realistic. Like I expect values of ~50microlitres whereas I get 50000ml. My other colleague tried on unaltered dataset from same project and she got the values in the right range. Problem for me is that it will be a lot  of work to go back and keeping the 16bit size from the raw data since I processed the raw data (scaled down) to take it to give me 3D image. I was wondering if reducing the bit size would impact on the quantification (segment statistics) in 3D slicer? If so, Is there a way to get the segment (heart ventricle) in its true shape so I get its correct quantification measurements (ventricular volume in my case) without going back to raw data?<br>
Many thanks,<br>
Qazi</p>

---

## Post #2 by @lassoan (2022-05-05 16:32 UTC)

<p>Bit depth (storing an image on 8 or 16 bits) does not affect physical size or volume.</p>
<p>Have you segmented the structure that you want to measure the volume of?<br>
Have you or your colleague has changed units settings in application settings?<br>
Where your input image comes from? Is it a human cardiac CT, MRI, or US?<br>
Why are you considering converting your data set from 16 to 8 bits per voxel?</p>

---

## Post #3 by @Qazi (2022-05-05 16:55 UTC)

<p>Yes I segmented the volume.<br>
My collegaue and I didnt change any unit settings.<br>
My input images are axial sections datastack, just like CT scan but from episcopic microscope (after each 2 micron section, camera takes an image). Being quite bif data and heavy on Mac as well as osirix, we scale it down.</p>

---

## Post #4 by @lassoan (2022-05-05 17:18 UTC)

<p>Most likely by rescaling the image in OsiriX you ended up with a file that has undefined or incorrect pixel spacing. You can fix that when you load that into Slicer or after you loaded it into Slicer, but it is better to avoid creating such corrupted file.</p>
<p>For example, you can load the original image into Slicer and use <code>Crop volume</code> module to crop and resample the image. It will have correct spacing. If you load a TIFF/JPG/PNG stack then you can use <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks">ImageStacks module of SlicerMorph extension</a> to reduce file size during import.</p>

---
