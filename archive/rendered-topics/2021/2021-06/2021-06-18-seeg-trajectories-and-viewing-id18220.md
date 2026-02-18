# sEEG trajectories and viewing

**Topic ID**: 18220
**Date**: 2021-06-18
**URL**: https://discourse.slicer.org/t/seeg-trajectories-and-viewing/18220

---

## Post #1 by @mubafz (2021-06-18 19:11 UTC)

<p>Hi,</p>
<p>I am a new clinican user to 3dSlicer and it looks great. Is there a way to quickly construct electrode trajectories based on DIXI parameters from post-implant CT/MRI co-ordinates. As well is there a way to view slices orthogonal along the trajectory of a particular electrode apart from the standard coronal, axial and sagital views? The SEEG assistant paper looks abit complicated and doesnt give a detailed step wise guide.</p>
<p>Thank you for any assistance.</p>
<p>Regards</p>

---

## Post #2 by @lassoan (2021-06-18 21:05 UTC)

<p>Yes, you can easily create straight or curved trajectories from CT/MRI coordinates (e.g., from a csv file) and reslice the volume along that axis (for example, using SlicerVMTK extension’s Cross-section analysis module).</p>

---

## Post #3 by @mubafz (2021-06-18 23:41 UTC)

<p>Thanks Andras. Its there a link to explain the csv format/importation process?</p>

---

## Post #4 by @lassoan (2021-06-19 01:01 UTC)

<p>File formats for markups are described here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html" class="inline-onebox">Markups — 3D Slicer documentation</a></p>
<p>I would recommend to use the .json file format, because that allows you to specify markup type (points, curve, etc.) and all display properties. But if you store and process your data in Excel then you can save as .csv or .tsv file that you can read into Slicer as a table and import into a markups node.</p>

---

## Post #5 by @mubafz (2021-06-19 16:12 UTC)

<p>Thank you very much for your help. Will test it out.</p>

---

## Post #6 by @mubafz (2021-06-24 14:23 UTC)

<p>Hi Andras,</p>
<p>I managed to import coordinates as markup points and its looking really good.</p>
<p>I want to ask if there is a quick way to centre a markup just by typing in the name of the desired markup point (maybe via some code in pythoninteractor or a filter somewhere). Lets say I have 200 points corresponding with stereo contacts. I want to go to a certain markup for example A5. Is there any quick shortcut way apart from scrolling through the control point table (it shows only around 6 markups at one time) and we have to scroll through to find one I want and click that row? It would be great if there is a filter or a brief code to do that.</p>
<p>sEEG reading is dynamic when we review the iEEG we want to refer back to the MRI alot of times for corresponding contacts.<br>
Thanks for any help.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0b72756d5725dd735788acd41ca8cf5879c6632.png" data-download-href="/uploads/short-url/tMnIyZ8ymRiAPWUnbauaME8R6WS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0b72756d5725dd735788acd41ca8cf5879c6632_2_690x382.png" alt="image" data-base62-sha1="tMnIyZ8ymRiAPWUnbauaME8R6WS" width="690" height="382" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0b72756d5725dd735788acd41ca8cf5879c6632_2_690x382.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0b72756d5725dd735788acd41ca8cf5879c6632.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0b72756d5725dd735788acd41ca8cf5879c6632.png 2x" data-dominant-color="F7F6F9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">926×513 29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2021-06-24 18:29 UTC)

<p>You could write a Python script that fills in a <a href="https://doc.qt.io/qt-5/qtablewidget.html">QTableWidget</a> with the point names and add a filter text box. You can use the study list in DICOMwebBrowser extension as an example (see <a href="https://github.com/lassoan/SlicerDICOMwebBrowser/blob/main/DICOMwebBrowser/DICOMwebBrowser.py">source code</a>).</p>
<p>Filter&amp;search will be generally useful, so we’ll implement this in Markups module, but we are still in the process of integrating a large markups module feature pack, so we will not be able to get to it for a couple of weeks. If you have some C++ programming experience then you can take on this task and make it available earlier.</p>

---

## Post #8 by @mubafz (2021-06-27 01:04 UTC)

<p>Hi Andras,</p>
<p>Thanks for your quick reply. Unfortunately I dont have much programming background so will wait for the feature pack upgrade.</p>
<p>I will read up on Qtablewidget in the meantime.</p>
<p>Regards<br>
M</p>

---
