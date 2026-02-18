# Error after installing radiomics

**Topic ID**: 2668
**Date**: 2018-04-23
**URL**: https://discourse.slicer.org/t/error-after-installing-radiomics/2668

---

## Post #1 by @Diana (2018-04-23 15:20 UTC)

<p>Hello,</p>
<p>everytime I try to run Slicer 3D an error table shows up <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba37aa66116bb6606b3cc8be76d70669d349702f.png" alt="image" data-base62-sha1="qzm4uRjssUg7HThbNIWeGTNnqfJ" width="400" height="239"></p>
<p>it started after I installed Radiomics, which I had to do offline from a file(downloaded from <a href="https://slicer.kitware.com/midas3/download/index?items=352857" rel="noopener nofollow ugc">https://slicer.kitware.com/midas3/download/index?items=352857</a>), and everytime I run Radiomics module, Slicer crashes… can anyone help, please?</p>
<p>I have tried reinstalling Slicer for the newest version, but no change</p>

---

## Post #2 by @JoostJM (2018-04-23 15:42 UTC)

<p>It looks like Slicer tries to load a compiled module (which can be the C extensions of PyRadiomics or C code include in pyyaml package), but is unable to do so and crashes. Is there a specific reason you need to install PyRadiomics offline? Maybe there is a version mismatch, does the version of the offline file match your slicer version?</p>

---

## Post #3 by @Diana (2018-04-23 16:06 UTC)

<p>yes, the reason I can’t do it online is because Slicer has problems connecting (it does not load extensions at all or it shows a connection problem) …could this be caused from changing the proxy settings? this is the latest change I have made</p>

---

## Post #4 by @Diana (2018-04-23 16:16 UTC)

<p>I have a matching version, I turned off proxy settings so now I can install it online, but the Runtime error still shows up, now together with</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/Diana/AppData/Roaming/NA-MIC/Extensions-27158/SlicerRadiomics/lib/Slicer-4.9/qt-scripted-modules/SlicerRadiomics.py”, line 576, in _onStatus<br>
if self._cli_running:<br>
AttributeError: SlicerRadiomicsLogic instance has no attribute ‘_cli_running’</p>
<p>any ideas, please?</p>

---
