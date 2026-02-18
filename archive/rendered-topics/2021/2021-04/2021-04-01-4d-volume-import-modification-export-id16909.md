# 4D volume import-modification-export

**Topic ID**: 16909
**Date**: 2021-04-01
**URL**: https://discourse.slicer.org/t/4d-volume-import-modification-export/16909

---

## Post #1 by @Kalman (2021-04-01 17:00 UTC)

<p>Hi, I’m interested in whether there is a possibility to import and modify 4D fMRI nifti files in the Slicer?</p>
<p>A bit more explanation about the question: we are working with multivolume datasets, where one file contains several scans (<a href="https://www.dropbox.com/s/l87rq40crjbyxp9/fMRI_raw_4D.nii?dl=0" rel="noopener nofollow ugc">I attach a file as an example</a>). I would like to make different rigid and non-linear transformations with the volume, modify scalar type etc. After having the result I would like to export it in a way that all the sub-volumes are modified accordingly (similar to that one image volume where I made the changes), and the saved single nifti file still have a multivolume property.</p>
<p>Thank you for you help!</p>
<p>Operating system: Windows 10, 64-bit<br>
Slicer version:4.11.20210226 (stable release)</p>

---

## Post #2 by @lassoan (2021-04-14 05:44 UTC)

<p>Using the GUI you can only save 4D volume sequences in nrrd format, but you can <code>pip_install('nibabel')</code> and concatenate the 3D volumes and write them as 4D using a few lines of Python script in Slicer’s Python console.</p>
<p>If you need to do this often then you can write a small IO plugin in Python that offers this option in the GUI (here is an <a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py">example</a>).</p>

---

## Post #3 by @Kalman (2021-04-14 06:43 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>: Thank you for your answer!</p>

---
