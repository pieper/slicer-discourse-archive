# Regarding import

**Topic ID**: 3962
**Date**: 2018-08-31
**URL**: https://discourse.slicer.org/t/regarding-import/3962

---

## Post #1 by @tomas (2018-08-31 19:38 UTC)

<p>Operating system: windows 10 64 bit<br>
Slicer version: 4.9 nightly<br>
Expected behavior: import .mat file<br>
Actual behavior: doesn’t import</p>
<p>Hi folks,</p>
<p>I have some Ultrasound volume data (video data) saved as .mat files with voxel data type uint8 and respected position in other .mat file; what is the best way to import them into 3D slicer for processing? I convert video data (datavideo_ultrasound) to Dicom images, but I could not import position info to DICOM images.  Could you please suggest me some solutions?</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2018-08-31 19:47 UTC)

<p>You can write the volume into a NRRD file using <a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver">nrrdwrite.m</a> and load that very easily into Slicer (and many other medical image computing software).</p>

---

## Post #3 by @tomas (2018-09-01 22:45 UTC)

<p>It is working properly for one 2d image to load in Slicer. But for 3d image it is not working. I have one ultrasound video (.mat) file. where I generated 278 2d images using the for loop below. therefore I used ‘cat’ for generating 3d image.  Then I used nrrdwrite to get nrrd file. but this 3d nrrd is showing nothing in slicer. I have positions of each 2d image, which is Commented in the code. It might work, if I can use position of 2d images for generating nrrd file. Is it possible to use the positions in nrrdwrite?</p>
<p>Thank you very much.</p>
<p>clc<br>
for i=1:278<br>
eval(sprintf(‘A%d = datavideo(:,:,1,i);’, i));<br>
% eval(sprintf(‘position%d = new_psonda(:,:,i);’, i));<br>
end</p>
<p>v1=cat(3,A1,A2,A3,A4,A5,A6,A7,A8,A9,A10);<br>
img.pixelData = v1;<br>
nrrdwrite(‘v1’, img);</p>

---

## Post #4 by @lassoan (2018-09-01 23:20 UTC)

<p>Is this a color image?</p>
<p>Please copy here the complete error message.</p>

---

## Post #5 by @tomas (2018-09-02 01:33 UTC)

<p>No, it is grayscale image.</p>
<p>I find the error, I didn’t put .nrrd in the file name. Now it is working fine. Thank you very much.</p>
<p>nrrdwrite(‘v1.nrrd’, img);</p>

---
