---
topic_id: 4958
title: "One Dicom Study Loading As Multiple"
date: 2018-12-04
url: https://discourse.slicer.org/t/4958
---

# One DICOM study loading as multiple

**Topic ID**: 4958
**Date**: 2018-12-04
**URL**: https://discourse.slicer.org/t/one-dicom-study-loading-as-multiple/4958

---

## Post #1 by @geodeltax (2018-12-04 19:23 UTC)

<p>Hi,</p>
<p>I’m trying to import a CT scan using the DICOM Browser on Slicer 4.10.0. The directory I imported with one study loaded as several studies, each with one series containing one slice.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/943387de3c5fb721468f78b3d15178217db11900.png" data-download-href="/uploads/short-url/l934jZpL5qNWynJloPN60GKcmmk.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/943387de3c5fb721468f78b3d15178217db11900_2_690x304.png" alt="Capture" data-base62-sha1="l934jZpL5qNWynJloPN60GKcmmk" width="690" height="304" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/943387de3c5fb721468f78b3d15178217db11900_2_690x304.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/943387de3c5fb721468f78b3d15178217db11900_2_1035x456.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/943387de3c5fb721468f78b3d15178217db11900_2_1380x608.png 2x" data-dominant-color="DEE8F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">1910×844 31.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It’s currently loading one image at a time rather than all the images as a stack. Is there some way I can combine all these studies back into one?</p>

---

## Post #2 by @lassoan (2018-12-04 19:28 UTC)

<p>Is this a 4D CT? It seems that the data set has been anonymized and maybe it was done incorrectly.</p>
<p>In 4D CT acquisitions, typically all frames are in the same series and you seem to have many series.</p>
<p>There is a fallback mechanism in the multi-volume DICOM importer in Slicer that can still load the data as a time sequence, but you need to select the whole study (all the series) and certain criteria must be met (number of frames and frame positions are the same for all time points; frames can be grouped based on one of the known frame grouping tags, etc.).</p>
<p>If selecting the study and loading results in loading of many individual frames then check “Advanced” section, click “Examine” to see what options are offered for loading and report back to us.</p>
<p>You can also create a volume sequence from a set of volume nodes in the scene using Sequences module in Sequences extension.</p>

---

## Post #3 by @geodeltax (2018-12-05 02:15 UTC)

<p>We were trying to anonymize our CTs using Matlab’s dicomanon function but we weren’t sure what fields we needed to keep the DICOM study intact. But all of these should be part of one 3D CT scan. Each slice can be selected in the viewer as a different series. Do you know exactly what tags we’d need to preserve the standard format?</p>
<p>In the advanced tab, there aren’t any options available after clicking “Examine”.</p>
<p>I loaded all the frames into the Sequences module but playback in the Sequences browser isn’t showing anything but the slice position rapidly ticking out of order.</p>

---

## Post #4 by @lassoan (2018-12-05 04:09 UTC)

<p>You can get definite answer from <a href="http://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.3" rel="nofollow noopener">DICOM standard Part 3</a>.</p>
<p>Instead of starting from scratch, you can start by inspecting tags present in a CT series created by a clinical scanner. You can find definition of all tags in the standard. You can safely skip all private DICOM tags.</p>

---
