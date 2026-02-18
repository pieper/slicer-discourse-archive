# Problems installing pyradiomics via pip install

**Topic ID**: 32879
**Date**: 2023-11-17
**URL**: https://discourse.slicer.org/t/problems-installing-pyradiomics-via-pip-install/32879

---

## Post #1 by @Magnus (2023-11-17 16:09 UTC)

<p>Hello,</p>
<p>I want to batch process a number radiomic extractions. Since I believe there is no way to do that through 3D Slicer, I tried to install pyradiomics. I’ve tried with the suggested python-versions as well as newer, but get different error messages depending on the python-version.</p>
<p>" Getting requirements to build wheel … error<br>
error: subprocess-exited-with-error" with the latest python version 3.12.</p>
<p>Any suggestions what I’m doing wrong?</p>
<p>Best regards<br>
Magnus</p>

---

## Post #2 by @pieper (2023-11-17 17:03 UTC)

<p>I would suggest just using the version of python that comes with slicer and the pyradiomics you get with SlicerRadiomics.</p>

---

## Post #3 by @Magnus (2023-11-18 08:55 UTC)

<p>Thank you for the suggestion,</p>
<p>However, I’m having a hard time localizing the pyradiomics python file. I searched for “radiomics.py” or “pyradiomics.py” in my slicer folder, and didn’t find the files, which made it hard to use the command line to batch process my files. Are they installed in other locations?</p>
<p>Best regards</p>
<p>Magnus</p>

---

## Post #4 by @pieper (2023-11-18 15:03 UTC)

<p>If you install the SlicerRadiomics extension you get the python package too.</p>
<p>On linux everything is in:</p>
<p>/home/exouser/Downloads/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/SlicerRadiomics</p>
<p>In the Slicer python console you can do <code>import radiomics</code></p>

---

## Post #5 by @Magnus (2023-11-18 19:23 UTC)

<p>Now I feel rather stupid. Have been using 3D Slicer for quite some time, but never really noticed the little icon with two snakes up in the toolbar…</p>
<p>Thank you.</p>
<p>Best regards</p>
<p>Magnus</p>

---
