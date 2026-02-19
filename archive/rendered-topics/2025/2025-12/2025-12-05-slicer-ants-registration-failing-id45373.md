---
topic_id: 45373
title: "Slicer Ants Registration Failing"
date: 2025-12-05
url: https://discourse.slicer.org/t/45373
---

# Slicer ANTs Registration Failing

**Topic ID**: 45373
**Date**: 2025-12-05
**URL**: https://discourse.slicer.org/t/slicer-ants-registration-failing/45373

---

## Post #1 by @ThomasVanParys (2025-12-05 09:56 UTC)

<p>Hello! I have tried to register two nrrd. volumes in ‘G:\Kikopey_project\ANTs_Volumes’<br>
But I have come across this issue, and don’t fully undertsnad how to resolve it:</p>
<pre><code class="lang-auto">Python 3.12.10 (main, Nov 10 2025, 02:47:38) [MSC v.1942 64 bit (AMD64)] on win32
&gt;&gt;&gt; 
[VTK] antsRegistrationCLI standard error:
[VTK]  file C:/Users/ImagingLab/AppData/Local/Temp/Slicer/BDBII_vtkMRMLScalarVolumeNodeB.nrrd does not exist . 
[VTK]  file C:/Users/ImagingLab/AppData/Local/Temp/Slicer/BDBII_vtkMRMLScalarVolumeNodeC.nrrd does not exist . 
[VTK] antsRegistrationCLI terminated with a fault
[Qt] QPixmap::scaled: Pixmap is a null pixmap
</code></pre>
<p>Any help would be much appreciated. This is on Slicer 5.10.0.</p>
<p>UPDATE: Do not have both ANTs Resgirstration and SlicerANTsOy plug-ins installed, as it will obscure the template, group-wise, and pair-wise tab options.</p>

---

## Post #2 by @dzenanz (2025-12-08 20:23 UTC)

<p>I guess that problem was resolved by <a href="https://github.com/SlicerMorph/SlicerANTsPy/commit/8b1ce30c81d3e4b44bd96af8adfbdd9aae39abc3" class="inline-onebox" rel="noopener nofollow ugc">Rename antsRegistrationLib to ANTsPyRegistrationLib to avoid conflict… · SlicerMorph/SlicerANTsPy@8b1ce30 · GitHub</a></p>

---

## Post #3 by @ThomasVanParys (2025-12-08 20:25 UTC)

<p>Thank you, I have managed to make it work - And I ended up using SlicerANTsPy in the end.</p>

---
