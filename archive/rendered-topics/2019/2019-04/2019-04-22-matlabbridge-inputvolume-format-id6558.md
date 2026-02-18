# MatlabBridge inputvolume format

**Topic ID**: 6558
**Date**: 2019-04-22
**URL**: https://discourse.slicer.org/t/matlabbridge-inputvolume-format/6558

---

## Post #1 by @Cincy (2019-04-22 18:50 UTC)

<p>Operating system:win10<br>
Slicer version:4.10.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello,<br>
I’m Cincy.emmm…I have a question about using  MatlabBridge.I want to know if I can give the File path directly as input volume,rather than through "cli_imageread."Because sometimes we need convert NRRD to Nifti,and that’s not easy.</p>
<p>Look forward to your reply !<br>
Thank you !</p>
<p>for example,like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e1f9f05aedc8d00f70c61963b737194e611ad57.png" alt="image" data-base62-sha1="20WqP7jSSgf4EruBB7oDUgVSijl" width="431" height="50"></p>

---

## Post #2 by @lassoan (2019-04-22 19:03 UTC)

<p>Yes, you can specify a wide range of file formats in the .xml file, you just have to make sure you use the corresponding file reader. However, if you use the MatlabBridge with Slicer then you can always use nrrd.</p>

---
