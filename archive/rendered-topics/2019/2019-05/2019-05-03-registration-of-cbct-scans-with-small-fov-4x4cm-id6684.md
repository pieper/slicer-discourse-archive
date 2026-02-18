# Registration of CBCT scans with small FOV (4x4cm)

**Topic ID**: 6684
**Date**: 2019-05-03
**URL**: https://discourse.slicer.org/t/registration-of-cbct-scans-with-small-fov-4x4cm/6684

---

## Post #1 by @sfglio (2019-05-03 06:32 UTC)

<p>Operating system: MacOS 10.14.4<br>
Slicer version: 4.11.0<br>
Expected behavior: Registration of two scans (with/without dental implant)<br>
Actual behavior: I loaded the dicom files and tried General Registration (BRAINS) using RIGID and AFFINE, RIGID and BSpline and Slicer Linear Transform.<br>
As fixed image: scan without the implant<br>
As moving image: scan with implant</p>
<p>As I cannot verify the registration in Module General Registration (BRAINS) I loaded the “registered” and the scan without implant in Landmark registration and there they were never superimposing accurately. Beside, I want to use the substract scalar vol module for what I need the perfect registration of different scans.</p>
<p>Here is an example of two scans I want to match:<br>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1VgTvA5XxiQ_ySkrPYUrzn0V2LhtTI4qK/view?usp=drive_open" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
    


<h3><a href="https://drive.google.com/file/d/1VgTvA5XxiQ_ySkrPYUrzn0V2LhtTI4qK/view?usp=drive_open" target="_blank" rel="nofollow noopener">Screenshot.png</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #2 by @lassoan (2019-05-03 18:31 UTC)

<p>Since bones are rigid, always use rigid registration. Crop the image so that it only contains regions that are rigidly connected (keep only the lower jaw or upper jaw in the image never both). Use masking to prevent the implant from throwing off the registration (masked regions are ignored in the registration). Try SlicerElastix extension as well.</p>
<p>Automatic image-based registration should work well for this simple registration problem, but if you want to do manual registration, then you can try “Fiducial registration wizard” module (in SlicerIGT extension).</p>
<p>Subtracting registered volumes is indeed a good way of visually checking registration (make sure you harden the transform before you subtract). You can also use “Compare Volumes” module - if you set one volume as foreground and the other as background and enable “Layer reveal cursor” option then you can quickly compare volumes by moving the mouse in slice viewers. For quantitative measurements, you can mark corresponding anatomical points using markups and get RMS error from “Fiducial registration wizard” module.</p>

---
