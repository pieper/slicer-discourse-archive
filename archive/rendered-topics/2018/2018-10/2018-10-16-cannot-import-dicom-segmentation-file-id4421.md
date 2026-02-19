---
topic_id: 4421
title: "Cannot Import Dicom Segmentation File"
date: 2018-10-16
url: https://discourse.slicer.org/t/4421
---

# Cannot import DICOM segmentation file

**Topic ID**: 4421
**Date**: 2018-10-16
**URL**: https://discourse.slicer.org/t/cannot-import-dicom-segmentation-file/4421

---

## Post #1 by @mayaslicer (2018-10-16 23:36 UTC)

<p>Operating system: Linux<br>
Slicer version: Slicer-4.9.0-2018-09-26-linux-amd64<br>
Expected behavior: Load segmentation file without error, and display it<br>
Actual behavior: After loading all the slices without error, the last one, containing the manual segmentation gives error.</p>
<p>Newbie explanation follows:</p>
<p>It first reads hundreds of MR[…].dcm (edited for privacy) files.<br>
The last good message off the command line is:<br>
“Volume” Reader has successfully read the file “[…]MR[…].dcm”[…]</p>
<p>Immediately followed bu the first error line:<br>
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open […] RS[…].dcm. ITK exception info: error in unknown:  Could not create IO object for reading file […]RS[…].dcm</p>
<p>It obviously does not recognize the segmentation file.</p>
<p>The file is read fine by the first freeware viewer I tried: Aliza.</p>
<p>The Linux “file” command recognizes the RS[…].dcm as “DICOM medical imaging data”.</p>
<p>Questions:</p>
<ol>
<li>
<p>Are there DICOM formats 3DSlicer does not understand?</p>
</li>
<li>
<p>Maybe I should have loaded a particular module?</p>
</li>
<li>
<p>How do I find out which DICOM subformat my RS.dcm file is?</p>
</li>
<li>
<p>Pointers to the right documentation?</p>
</li>
</ol>
<p>Thanks, I hope I don’t have to write an import module!</p>

---

## Post #2 by @lassoan (2018-10-16 23:38 UTC)

<p>‘RS’ probably refers to DICOM RT structure set object. You need to install SlicerRT extension to be able to load DICOM RT information objects.</p>

---

## Post #3 by @mayaslicer (2018-10-17 00:31 UTC)

<p>I already have both SlicerRT and SlicerRadiomics installed.</p>
<p>New info: Aliza reports RT as RTSTRUCT, and “series” as “Contouring” (which I called “segmentation”). May be useful to identify the right module, if any.</p>
<p>BTW, should I edit the OP with the new info or just leave it here in the comments?</p>

---

## Post #4 by @lassoan (2018-10-17 01:10 UTC)

<p>RTSTRUCT can be imported by SlicerRT extension. It has been tested on hundreds of data sets. Could you share the files that you have trouble importing? (make sure it is anonymized)</p>

---

## Post #5 by @mayaslicer (2018-10-17 12:19 UTC)

<p>Ok, anonymized it within Aliza. It’s 12578 bytes and I called it RS…dcm.<br>
How do I share it on this forum?</p>

---

## Post #6 by @mayaslicer (2018-10-17 13:33 UTC)

<p>Also, I get the same error with the RS contour files in the Planning Data directory of the WC2015_Gel_Slicelet_Dataset I downloaded from <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerRT#Tutorials" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerRT#Tutorials</a></p>
<p>Does this confirm that there is something wrong with Slicer-4.9.0-2018-09-26-linux-amd64?</p>

---

## Post #7 by @cpinter (2018-10-17 15:12 UTC)

<p>Are you sure the SlicerRT extension is installed properly? Do you see a Radiotherapy category in the module list? Do you see DicomRtImportExportPlugin in the DICOM browser if you check Advanced?</p>
<p>In the meantime I’ll try to load the tutorial dataset.</p>

---

## Post #8 by @mayaslicer (2018-10-17 20:27 UTC)

<ol>
<li>Yes, the Radiotherapy category is listed.</li>
<li>Yes, the DicomRtImportExportPlugin shows up in the DICOM browser.</li>
</ol>

---

## Post #9 by @Mihail_Isakov (2018-10-18 01:54 UTC)

<p>I’ve tested Planning Data directory of the WC2015_Gel_Slicelet_Dataset from the above post and it worked<br>
with Slicer (current nightly build). In DICOM Browser clicked import, clicked at the study and “Examine”, clicked “Load”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c4b9987458c60b3ecf21610dabd5fc6d54398e3.jpeg" data-download-href="/uploads/short-url/8BoCqOWe9yS1fqsItYbDy8pjiUj.jpeg?dl=1" title="scr1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c4b9987458c60b3ecf21610dabd5fc6d54398e3_2_645x500.jpeg" alt="scr1" data-base62-sha1="8BoCqOWe9yS1fqsItYbDy8pjiUj" width="645" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c4b9987458c60b3ecf21610dabd5fc6d54398e3_2_645x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3c4b9987458c60b3ecf21610dabd5fc6d54398e3_2_967x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c4b9987458c60b3ecf21610dabd5fc6d54398e3.jpeg 2x" data-dominant-color="DCE7EE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">scr1</span><span class="informations">1244×963 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13245638e29feb91e5bb71dd8df6ffbe1b76685f.jpeg" data-download-href="/uploads/short-url/2JkVeITJGW137ULGOoxek1FNg51.jpeg?dl=1" title="Screenshot%20at%202018-10-18%2003-46-57" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/13245638e29feb91e5bb71dd8df6ffbe1b76685f_2_690x379.jpeg" alt="Screenshot%20at%202018-10-18%2003-46-57" data-base62-sha1="2JkVeITJGW137ULGOoxek1FNg51" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/13245638e29feb91e5bb71dd8df6ffbe1b76685f_2_690x379.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/13245638e29feb91e5bb71dd8df6ffbe1b76685f_2_1035x568.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/13245638e29feb91e5bb71dd8df6ffbe1b76685f_2_1380x758.jpeg 2x" data-dominant-color="AAB5AE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20at%202018-10-18%2003-46-57</span><span class="informations">1724×948 324 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
