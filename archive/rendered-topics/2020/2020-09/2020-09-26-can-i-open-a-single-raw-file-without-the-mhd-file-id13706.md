# Can I open a single .raw file without the .mhd file? 

**Topic ID**: 13706
**Date**: 2020-09-26
**URL**: https://discourse.slicer.org/t/can-i-open-a-single-raw-file-without-the-mhd-file/13706

---

## Post #1 by @kevin.x (2020-09-26 04:04 UTC)

<p>Hi all, I got some labeled medical images in .raw format. Can I open a single .raw file without the .mhd file using 3D Slicer? And if not, is there any tool to convert the .raw file to .nii file?<br>
Much appreciated!</p>

---

## Post #2 by @lassoan (2020-09-26 04:07 UTC)

<p>Yes, you can open a raw file with Slicer. Of course the application still needs to know how to interpret that raw file, so you need to specify this data in a separate text header file (for example, a .nhdr file). You can conveniently generate such a header file using <a href="https://github.com/acetylsalicyl/SlicerRawImageGuess#slicerrawimageguess">RawImageGuess extension</a>.</p>

---

## Post #3 by @kevin.x (2020-09-28 01:10 UTC)

<p>Thank you Iassoan, it works! I read the information from the original image and then used “RawImageGuess” to generate the header for the .raw file which is the labelled image.<br>
It confused me initially as I can’t find the “RawImageGuess” module in my 3D Slicer for mac, and I finally found it in the Windows version. Is it possible to install this module in the 3D Slicer for mac?</p>
<p>Much appreciated!</p>

---

## Post #4 by @lassoan (2020-09-28 01:37 UTC)

<p>RawImageGuess extension is available for Mac, too, but probably only for Slicer-4.11. Which Slicer version did you install?</p>

---

## Post #5 by @kevin.x (2020-09-28 01:45 UTC)

<p>I installed V4.10.2，the stable version I think. I will update it to the latest version. Thanks!</p>

---
