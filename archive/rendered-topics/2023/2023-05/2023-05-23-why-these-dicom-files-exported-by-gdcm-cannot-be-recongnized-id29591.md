# Why these dicom files exported by gdcm cannot be recongnized correctly by 3d slicer?

**Topic ID**: 29591
**Date**: 2023-05-23
**URL**: https://discourse.slicer.org/t/why-these-dicom-files-exported-by-gdcm-cannot-be-recongnized-correctly-by-3d-slicer/29591

---

## Post #1 by @Shannon_Chow (2023-05-23 00:59 UTC)

<p>I exported multiple slices of the same series (and the same study) using <a href="https://gdcm.sourceforge.net/" rel="noopener nofollow ugc">GDCM</a> in C++. The data is attached <a href="https://drive.google.com/file/d/13xKxE014ZmDDnCrZGY8DfQ6mZDjhZaJ3/view?usp=share_link" rel="noopener nofollow ugc">here</a>.<br>
But it seems that 3D Slicer cannot recognize these files correctly:</p>
<ol>
<li>Each dcm file was recognized as a volume<br>
<a href="https://i.stack.imgur.com/wb0kF.png" rel="noopener nofollow ugc">image</a>
</li>
<li>After import, nothing is displayed in Slicer.</li>
</ol>
<p>I think I’ve filled some inappropriate content into some important dicom Tags. But there are hundreds of tags, how to find which one[s] is[are] inappropriate? How to make these dicom files compatible with Slicer?</p>

---

## Post #2 by @pearsonm (2023-05-23 01:35 UTC)

<p>One problem is that there is no windowing information. Both WindowWidth and WindowCenter are 0 and you should also have SmallestImagePixelValue and LargestImagePixelValue. There may be other issues as well.</p>

---

## Post #3 by @Shannon_Chow (2023-05-23 06:53 UTC)

<p>Thx for your reply. I’ve added all your mentioned tags but still unresolved.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc5adcdbf347360c2226b6b642d95812c2a1a8a7.png" alt="image" data-base62-sha1="qSgr5CYBBnG6w23lQTipuRxMcv5" width="379" height="269"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de1f13143c0762959a539fa8cc35e76825ed92cd.png" alt="image" data-base62-sha1="vGYzFtXBZsD5wxkyLNqzqTLAsH3" width="516" height="103"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2fa034868d61a819cd5daa2e051a2697bf8b675.png" alt="image" data-base62-sha1="pxiDFaWOQwMHhbjvoN8H7sLpm0R" width="457" height="103"></p>

---

## Post #4 by @pearsonm (2023-05-23 07:51 UTC)

<p>I can load the study (with errors) on my local build of Slicer. Try using a nightly build.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c5802aca4a978164f8fed4ba68ac1bd5317ed59.png" data-download-href="/uploads/short-url/mj52UieFe2EvFSLrMY05epcK2h3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c5802aca4a978164f8fed4ba68ac1bd5317ed59_2_633x499.png" alt="image" data-base62-sha1="mj52UieFe2EvFSLrMY05epcK2h3" width="633" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c5802aca4a978164f8fed4ba68ac1bd5317ed59_2_633x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c5802aca4a978164f8fed4ba68ac1bd5317ed59_2_949x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c5802aca4a978164f8fed4ba68ac1bd5317ed59_2_1266x998.png 2x" data-dominant-color="9E9EAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1455×1148 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @Shannon_Chow (2023-05-24 01:08 UTC)

<p>I got the following errors with version 4.10.0 r27501.<br>
Is there any information of which tag was filled wrong value or missed?</p>
<pre><code class="lang-auto">Python 2.7.13 (default, Oct 18 2018, 22:10:33) [MSC v.1900 64 bit (AMD64)] on win32
&gt;&gt;&gt; 
Traceback (most recent call last):
  File "C:\Program Files\Slicer 4.10.0\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 737, in getLoadablesFromFileLists
    loadablesByPlugin[plugin] = plugin.examine(fileLists)
  File "C:/Program Files/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 106, in examine
    loadables += self.examineFiles(files)
  File "C:/Program Files/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 493, in examineFiles
    mvNodes = self.initMultiVolumes(subseriesLists[key])
  File "C:/Program Files/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 789, in initMultiVolumes
    tagValue = self.tm2ms(tagValueStr) # convert to ms
  File "C:/Program Files/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 756, in tm2ms
    raise IOError("Invalid DICOM time string: "+tm+" (failed to parse HHMMSS)")
IOError: Invalid DICOM time string: 14:47:47 (failed to parse HHMMSS)
Warning: Plugin failed: MultiVolumeImporterPlugin

See python console for error message.
DICOM Plugin failed: Invalid DICOM time string: 14:47:47 (failed to parse HHMMSS)
Warning in DICOM plugin Scalar Volume when examining loadable Series Number: Unnamed Series: Reference image in series does not contain geometry information. Please use caution.

Loading with imageIOName: GDCM
Could not read scalar volume using GDCM approach.  Error is: FileFormatError
Loading with imageIOName: DCMTK
Could not read scalar volume using DCMTK approach.  Error is: FileFormatError

Could not load: Series Number: Unnamed Series as a Scalar Volume
</code></pre>

---

## Post #6 by @Shannon_Chow (2023-05-24 01:09 UTC)

<p>How to modify my dicom files to fix the errors?</p>

---

## Post #7 by @pearsonm (2023-05-24 02:12 UTC)

<p>To fix the immediate problem, time fields need to be in the format “HHMMSS.FFFFFF” so 14:47:47 needs to be changed to 144747.000000 (see the TM field at <a href="https://dicom.nema.org/dicom/2013/output/chtml/part05/sect_6.2.html" rel="noopener nofollow ugc">https://dicom.nema.org/dicom/2013/output/chtml/part05/sect_6.2.html</a>)<br>
In your original file this is the field AcquisitionTime.</p>
<p>You should also upgrade your Slicer if possible as 5.x is better able to handle non-compliant DICOM files.</p>

---

## Post #8 by @Shannon_Chow (2023-05-26 01:19 UTC)

<p>Changing time format did not solve the problem. But I can load my dcm files after upgrade Slicer to 5.3.0. Great Thx!</p>

---
