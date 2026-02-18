# PET/CT "Could not load: ... as a Scalar Volume"

**Topic ID**: 12660
**Date**: 2020-07-21
**URL**: https://discourse.slicer.org/t/pet-ct-could-not-load-as-a-scalar-volume/12660

---

## Post #1 by @jcaruso884 (2020-07-21 15:21 UTC)

<p>I’m having problems loading my PET/CT data. Any ideas on how to fix this issue? Any tips are appreciated!<br>
<a href="https://drive.google.com/drive/folders/1T0mYrI5O0IVnnwpj6UTGUMtb1XlR3obs?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/drive/folders/1T0mYrI5O0IVnnwpj6UTGUMtb1XlR3obs?usp=sharing</a></p>
<p>Operating system: macOS High Sierra<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Warnings detected during load.  Examine data in Advanced mode for details.  Load anyway?</p>
<p>Could not load: 5303: MPR fusion WB coronal as a Scalar Volume</p>

---

## Post #2 by @lassoan (2020-07-23 01:47 UTC)

<p>The data set at the link is not accessible (I’ve requested access).</p>

---

## Post #3 by @Chris_Rorden (2020-07-23 17:10 UTC)

<p>These look like valid DICOMs, but are unusual and Slicer might not be the ideal tool for these.</p>
<ol>
<li>Unusual transfer syntax 1.2.840.10008.1.2.4.91 JPEG 2000 (potentially lossy) Image Compression. This may confound some readers, I would suggest raw storage as DICOM does not require readers to support this format (gdcm and dcmtk can convert). These were created by Osirix, and it can be set to save data as raw.</li>
<li>Unusual Instance Numbers (0020,0013): [ 27 32 33 147 153 184 190 218 219 224 225 230 231 345 351 379 386 392 423 437]. Again, this is legal, as DICOM does not require sequential or even unique values. However, this often suggests files are missing.</li>
<li>Uneven spacing between slices. Distance from the first slice is [0 4.88281 5.85931 117.188 123.047 153.32 159.18 186.523 187.5 192.383 193.359 198.242 199.219 310.547 316.406 343.75 350.586 356.445 386.719 400.391]. Again, this is legal but might suggest some slices are lost, and frustrates tools that expect equal slice spacing.</li>
<li>This fusion image uses RGB with 8-bits per channel. Again, this is legal, but does limit utility. 24-bit RGB allows just 256 unique gray levels, and therefore less dynamic range than 12-bit (4096 grays) or 16-bit (65536 grays) data. Further, since there are 3 channels, it is not scalar. Slicer is really optimized for scalar (single channel) data. Consider a CT image with a single channel reporting Hounsfield units in the range -1000…1000. The relative brightness between voxels is explicit. In contrast, consider two Red/Green/Blue voxels, one with values 255/0/0 (Red) and the other with 0/0/255 (Blue). The red voxel is brighter to the human eye (as it is more sensitive to red) while the blue voxel is hotter if the units is a Kelvin color scale. With an RGB image, the colors are “baked in”, which will limit the utility of Slicer.</li>
</ol>
<p>The dcm2niix module for Slicer should convert these for you. It can interpolate from the 20 slices to create 40 evenly spaced slices, which might be useful.</p>

---

## Post #4 by @lassoan (2020-07-23 20:45 UTC)

<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> thanks a lot for the analysis. Based on what you describe, it seems that the data set is just some secondary capture (essentially screenshots) and not the original clinical image.</p>
<p>Recent Slicer versions can fill in the space of missing slices and you can convert color image to grayscale but the proper thing to do would be to use the original images that come out of the scanner.</p>

---

## Post #5 by @jcaruso884 (2020-07-24 12:56 UTC)

<p>Thank you! I appreciate the time and help. I will try the dcm2niix module in hopes that will work!</p>

---
