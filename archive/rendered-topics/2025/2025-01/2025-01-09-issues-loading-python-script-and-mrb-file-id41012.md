# Issues loading Python script and .mrb file

**Topic ID**: 41012
**Date**: 2025-01-09
**URL**: https://discourse.slicer.org/t/issues-loading-python-script-and-mrb-file/41012

---

## Post #1 by @Symon (2025-01-09 09:46 UTC)

<p>Hi,</p>
<p>I’m new to 3D Slicer and I have somme issues with it.<br>
I have DICOM files that I load to 3D Slicer (no problem there). These are CT-Scan Dynamic with 247 images (7.8Go for the DICOM file).</p>
<p>I saved my work in a “.mrb” file, but when I want to load it, I have black screens : my CT just disappear, nothing to see…<br>
I think the file do not save completely because it is too big… What do you think ?<br>
When I load the file, this appear in the consol :</p>
<p>[VTK] [nrrd] nrrdRead: trouble<br>
[VTK] [nrrd] _nrrdRead: trouble reading NRRD file<br>
[VTK] [nrrd] _nrrdFormatNRRD_read:<br>
[VTK] [nrrd] _nrrdEncodingGzip_read: expected 8287944704 bytes but received 1611130266</p>
<p>Another issue I do have it’s using a Python script that “Threshold” all my images (I do not want to do it manually 247 times…). When I put the program in the consol, 3D Slicer is running, but bugged and shut off itself in about 2minutes… The script already exists and have worked well on other CT-Scan Dynamic (with just 68 images), so I do not understand what the issue…</p>
<p>If someone can help me and have any solution…</p>
<p>Thanks in advance<br>
Symon</p>

---

## Post #2 by @pieper (2025-01-09 16:24 UTC)

<p>The mrb file is just a .zip, so if you change the extension you can look at it with any tool.  Probably it got truncated or there was file corruptioin.</p>
<p>Regarding your other issue, if you have a reproducible example script that illustrates the issue someone might be able to give specific suggestions.</p>

---
