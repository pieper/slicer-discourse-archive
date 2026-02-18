# Import file dicom in Python Pyradiomics

**Topic ID**: 24197
**Date**: 2022-07-06
**URL**: https://discourse.slicer.org/t/import-file-dicom-in-python-pyradiomics/24197

---

## Post #1 by @Van_Tran_Sang_Huynh (2022-07-06 08:25 UTC)

<p>Hello,<br>
I want to import 1 patient CT dicom image file (about 100+ images) into python pyrradiomics for feature extraction. How can I use the code? hope the helping.<br>
Thank.<br>
Sang</p>

---

## Post #2 by @pieper (2022-07-06 13:40 UTC)

<p>You can script that, like in these examples, then use pyradiomics/SlicerRadiomics.<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#dicom" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#dicom</a></p>

---

## Post #3 by @Van_Tran_Sang_Huynh (2022-07-07 12:38 UTC)

<p>I am getting error when using this code on Python 3.6.4, I am importing CT data for feature extraction using the Python Pyradiomics library package. Is there any way to use it?<br>
The purpose I need to import a patient’s CT DICOM data file into Python and extract features using the Pyradiomics library package.<br>
Hope for a help.<br>
Thank.<br>
Sang</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53b51c73bafdfaa245cf38269afd7d4b696c4be5.png" data-download-href="/uploads/short-url/bWvEQIRjzCFyCgaYXF5clAP0RJX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53b51c73bafdfaa245cf38269afd7d4b696c4be5_2_690x388.png" alt="image" data-base62-sha1="bWvEQIRjzCFyCgaYXF5clAP0RJX" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53b51c73bafdfaa245cf38269afd7d4b696c4be5_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53b51c73bafdfaa245cf38269afd7d4b696c4be5_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53b51c73bafdfaa245cf38269afd7d4b696c4be5_2_1380x776.png 2x" data-dominant-color="DCDBDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 383 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pieper (2022-07-07 19:45 UTC)

<p>Pyradiomics in native python does not support dicom directly (not all sets of dicom files will map to a volumetric image) instead it needs a nrrd or nifti of a volume.  The Slicer example code I linked only works in Slicer’s python, so you can use that to determine the right volume data from your CT dicom files.  Then you can use pyradomics.</p>

---
