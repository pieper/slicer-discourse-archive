# Translate an input data (such as CT) in CLI module

**Topic ID**: 14192
**Date**: 2020-10-21
**URL**: https://discourse.slicer.org/t/translate-an-input-data-such-as-ct-in-cli-module/14192

---

## Post #1 by @aseman (2020-10-21 19:44 UTC)

<p>Slicer version: 4.10.1<br>
Hi 3D Slicer experts and all</p>
<p>Some modules, such as Gaussian Blur Image Filter, have parameter set that, when I set the parameters ( for example sigma=1, input volume: CT image), the command is shown in the log file, And it can be run in the command line. I want to do this, in the command line for the Transforms module, too.<br>
Now, I have some questions :<br>
1-  Are modules like Gaussian Blur Image Filter, CLI module?</p>
<p>2- Is it possible to transform a CT image inside CLI module, And can I shift it in L-R, A-P, and S-I with a certain value that gets it as an argument?</p>
<p>3- In the Gaussian Blur image filter module, this Gaussian function gets Sigma isotropically.  Can I give σx, σy, and σz non-isotropically?</p>
<p>4- In the IO panel, we can specify different Sigma values separately. Is it possible to define various values for Sigma in the command line?<br>
Thanks a lot</p>

---

## Post #2 by @lassoan (2020-10-21 20:31 UTC)

<p>You can do all these using CLI modules. However, image blurring and resampling are are all single-line operations in Python packages such as ITK or SimpleITK. Instead of running several executables, it is simpler to write a short Python script that uses ITK/SimpleITK directly.</p>

---
