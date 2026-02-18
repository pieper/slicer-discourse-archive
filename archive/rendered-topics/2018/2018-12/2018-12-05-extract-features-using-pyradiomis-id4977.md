# Extract features using pyRadiomis

**Topic ID**: 4977
**Date**: 2018-12-05
**URL**: https://discourse.slicer.org/t/extract-features-using-pyradiomis/4977

---

## Post #1 by @camelia (2018-12-05 19:23 UTC)

<p>Hello everyone !</p>
<p>I’m trying to use pyRadiomics to extract features on a brain tumor  from DICOM images in Python.<br>
pyRadiomics doesn’t accept dicom as an input.</p>
<p>I’m using SimpleITK to read the dcm images  but I can’t do the features extraction when I use the “execute” function from featureextractor, because I need the maskFilePath(label map)</p>
<p>Does someone succeed to extract the features from dicom images using pyRadiomics ?</p>
<p>Thanks a lot in advance !<br>
Camelia</p>

---

## Post #2 by @pieper (2018-12-06 14:38 UTC)

<p>Hi <a class="mention" href="/u/camelia">@camelia</a> -</p>
<p>Once you have the dicom data loaded in Slicer or in SimpleITK you can save to any itk-compatible format and load in PyRadiomics.</p>
<p>PyRadiomics specific questions can go to the google group:<br>
<a href="https://groups.google.com/forum/#!forum/pyradiomics" rel="nofollow noopener">https://groups.google.com/forum/#!forum/pyradiomics</a></p>
<p>Best,<br>
Steve</p>

---
