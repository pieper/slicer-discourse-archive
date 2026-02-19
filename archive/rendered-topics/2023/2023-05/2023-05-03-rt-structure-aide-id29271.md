---
topic_id: 29271
title: "Rt Structure Aide"
date: 2023-05-03
url: https://discourse.slicer.org/t/29271
---

# Rt structure aide

**Topic ID**: 29271
**Date**: 2023-05-03
**URL**: https://discourse.slicer.org/t/rt-structure-aide/29271

---

## Post #1 by @Assia_Benhamla (2023-05-03 15:32 UTC)

<p>Bjr<br>
j’ai des contours en format Dicom réalisé sur des images SPECT, maintenant je veux utiliser ces segments sur des images TEP/CT  afin de calculer la concentration radioactives de chaque segment, je n’arrive pas à réaliser ça<br>
pouvez vous m’aider  svp!</p>

---

## Post #2 by @gcsharp (2023-05-03 20:56 UTC)

<p>Hi,  You will need to install the SlicerRT extension to load the RTSTRUCT.  I suspect that you could use the segment statistics module to calculate the average activity from the PET image, but have never tried that myself.</p>

---

## Post #3 by @Assia_Benhamla (2023-05-04 09:40 UTC)

<p>hi<br>
The RT structure is already in place, the statistics don’t work, I have a table with the segment names as results only<br>
I exported RT structure to labelmap, I got SUV values with pet SUV computation as result, however, the stats to predict volumes and other parameters still don’t work<br>
thanks</p>

---

## Post #4 by @gcsharp (2023-05-08 13:56 UTC)

<p>Hi Assia,  Unfortunately I also was not successful.  It seems the segment statistics does not provide average intensity within a segment.  You might need to write a python script.</p>

---

## Post #6 by @cpinter (2023-05-11 10:52 UTC)

<p>Please use the English language in the forums for better understanding for the community. If you do not speak the language feel free to use Google Translate or any other similar service (as I suppose Greg did with your French message). Thank you!</p>

---

## Post #7 by @cpinter (2023-05-11 10:54 UTC)

<p>I believe it does, assuming that average and mean are the same. Here is a very recent output from the Segment Statistics module<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc9633e6dd0b30b5f2f87b6be613ba0948208837.png" data-download-href="/uploads/short-url/tbRd8opeI9oZ88V21IM8JKpKh5t.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc9633e6dd0b30b5f2f87b6be613ba0948208837.png" alt="image" data-base62-sha1="tbRd8opeI9oZ88V21IM8JKpKh5t" width="690" height="86" data-dominant-color="E5E4E4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">833×105 12.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @gcsharp (2023-05-11 14:31 UTC)

<p>I only get 4 columns: Segment, Surface Area, Volume (mm), Volume (cm).  This is on linux.  I tried 5.2.2 and 5.3.0, same result.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c5d9cb1bb459e9c984d0b89dbbb507da0ccd2cb.png" data-download-href="/uploads/short-url/k1JplyDEmRHQaDtpQdrH3M3z8OT.png?dl=1" title="2023-05-11_10-30" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c5d9cb1bb459e9c984d0b89dbbb507da0ccd2cb_2_690x413.png" alt="2023-05-11_10-30" data-base62-sha1="k1JplyDEmRHQaDtpQdrH3M3z8OT" width="690" height="413" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c5d9cb1bb459e9c984d0b89dbbb507da0ccd2cb_2_690x413.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c5d9cb1bb459e9c984d0b89dbbb507da0ccd2cb_2_1035x619.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c5d9cb1bb459e9c984d0b89dbbb507da0ccd2cb.png 2x" data-dominant-color="C2C3C1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-05-11_10-30</span><span class="informations">1211×725 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @cpinter (2023-05-11 14:35 UTC)

<p>Interesting. It seems that you only get the statistics from the Labelmap Statistics plugin, and although all the metrics of the Scalar Volume Statistics plugin are enabled as you show in the screenshot, they are not computed. Is there any error in the console or the log? I’ll try this on Linux too when I work on that computer.</p>

---

## Post #10 by @gcsharp (2023-05-11 14:40 UTC)

<p>Error log completely empty when computing statistics.  There were some warnings/errors on the structure import, but it seems to have loaded.</p>
<pre><code class="lang-auto">Warning: In /work/Preview/S-0-E-b/SlicerRT/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx, line 1258
vtkPlanarContourToClosedSurfaceConversionRule (0x116841d0): GetSpacingBetweenLines: Contour spacing is not consistent.


Warning: In /work/Preview/S-0-E-b/SlicerRT/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx, line 1258
vtkPlanarContourToClosedSurfaceConversionRule (0x116841d0): GetSpacingBetweenLines: Contour spacing is not consistent.


Warning: In /work/Preview/S-0-E-b/SlicerRT/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx, line 1258
vtkPlanarContourToClosedSurfaceConversionRule (0x116841d0): GetSpacingBetweenLines: Contour spacing is not consistent.


Warning: In /work/Preview/S-0-E-b/SlicerRT/DicomRtImportExport/ConversionRules/vtkPlanarContourToClosedSurfaceConversionRule.cxx, line 1258
vtkPlanarContourToClosedSurfaceConversionRule (0x116841d0): GetSpacingBetweenLines: Contour spacing is not consistent.


No input data


No input data


No input data


No input data


No input data


No input data


No input data


No input data


No input data


No input data


No input data


No input data


No input data


No input data


No input data


No input data


No input data


No input data


</code></pre>

---

## Post #11 by @cpinter (2023-05-11 14:55 UTC)

<p>Yes these seem “normal”. Thanks!</p>

---

## Post #12 by @Assia_Benhamla (2023-05-11 15:08 UTC)

<p>I solved the problem by creating  binarylabelmap in SEGMENTATION and doing an alignment between CT’s images</p>

---
