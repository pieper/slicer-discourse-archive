---
topic_id: 33198
title: "Dce Time Series Recognised As Scalar Volume"
date: 2023-12-04
url: https://discourse.slicer.org/t/33198
---

# DCE time series recognised as Scalar volume

**Topic ID**: 33198
**Date**: 2023-12-04
**URL**: https://discourse.slicer.org/t/dce-time-series-recognised-as-scalar-volume/33198

---

## Post #1 by @winter (2023-12-04 12:32 UTC)

<p>Operating system: Windows 10 Enterprise 64 bit<br>
Slicer version:5.6.0<br>
Expected behavior: load multiframe time series DCE data as multiframe object<br>
Actual behavior: recognised as scalar volume</p>
<p>Dear Communinty,</p>
<p>I want to analyse data coming from a time serie of images from a DCE experiment.<br>
The serie contains time serie of images throughout 9 minutes of imagin time in 3 image layers. When I load the DICOM data into 3DSlicer, the experiment is not recognised as multiframe object but as scalar volume (The images are then arranged firstly in the order of time and secondly in order of Frames). This is why it won’t be recognised in the  MultiVolumeExplorer as an input multivolume.</p>
<p>Can someone help me solving the issue?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2024-07-31 11:33 UTC)

<p>This 4D DICOM image is saved in enhanced multi-frame MRI format, which is not supported by Slicer’s 4D DICOM importer. However, you can use <a href="https://github.com/rordenlab/dcm2niix">dcm2niix</a> to create a 4D NRRD file that Slicer can load:</p>
<pre data-code-wrap="txt"><code class="lang-txt">dcm2niix -e y -z y path/to/dicomfiles
</code></pre>
<p>When you drag-and-drop the .nhdr file into Slicer and the “Add data” window appears, choose <code>Sequence</code> in <code>Description</code> column.</p>
<p>You can then replay the time sequence using the sequence toolbar and display time-intensity plot using Sequences module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33efc149659cad74fc93b4b7a8436bf73140c151.png" data-download-href="/uploads/short-url/7ps1tmsx5paxYSVgvzwlxqX1Ylz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33efc149659cad74fc93b4b7a8436bf73140c151_2_690x406.png" alt="image" data-base62-sha1="7ps1tmsx5paxYSVgvzwlxqX1Ylz" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33efc149659cad74fc93b4b7a8436bf73140c151_2_690x406.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33efc149659cad74fc93b4b7a8436bf73140c151_2_1035x609.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33efc149659cad74fc93b4b7a8436bf73140c151_2_1380x812.png 2x" data-dominant-color="514F52"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2314×1363 451 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @winter (2024-08-02 09:16 UTC)

<p>Dear Andras,<br>
I am unfamiliar with dcm2niix. Can you please tell me more detailed how to install it (if needed), where I have to type “dcm2niix -e y -z y path/to/dicomfiles” in? Thank you.</p>

---

## Post #4 by @lassoan (2024-08-02 09:23 UTC)

<p>If you wait a couple of days then a <a href="https://github.com/rordenlab/dcm2niix/pull/843">fix</a> in dcm2niix will be integrated that will make Slicer be able to load DCE-MRI sequences from DICOM without typing commands.</p>
<p>If you dont want to wait then you can download dcm2niix and run the command I provided above in the terminal window of the operating system.</p>

---

## Post #5 by @winter (2025-02-04 09:39 UTC)

<p>Dear Andras!</p>
<p>I tried to open the DCE dataset in Slicer 5.8.0 by using “Diffusion-weighted DICOM Import (DCM2niixGUI)” plugin. This opens the dataset but it seems to contain only 1 timepoint. If I go to sequences, it still does not recognizes any sequence.<br>
What do I wrong? Can you help me please?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb507776b1a5ab641bcf96660522896a439adf76.png" data-download-href="/uploads/short-url/xzGBtXBkHBnz3MoWztk4k0pF7FA.png?dl=1" title="DCE" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb507776b1a5ab641bcf96660522896a439adf76_2_690x373.png" alt="DCE" data-base62-sha1="xzGBtXBkHBnz3MoWztk4k0pF7FA" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb507776b1a5ab641bcf96660522896a439adf76_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb507776b1a5ab641bcf96660522896a439adf76_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb507776b1a5ab641bcf96660522896a439adf76_2_1380x746.png 2x" data-dominant-color="8B8B8F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DCE</span><span class="informations">1917×1039 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
