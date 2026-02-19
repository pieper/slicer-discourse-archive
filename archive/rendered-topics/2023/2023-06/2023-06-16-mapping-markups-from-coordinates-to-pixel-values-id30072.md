---
topic_id: 30072
title: "Mapping Markups From Coordinates To Pixel Values"
date: 2023-06-16
url: https://discourse.slicer.org/t/30072
---

# Mapping markups from coordinates to pixel values

**Topic ID**: 30072
**Date**: 2023-06-16
**URL**: https://discourse.slicer.org/t/mapping-markups-from-coordinates-to-pixel-values/30072

---

## Post #1 by @jawbra (2023-06-16 14:47 UTC)

<p>Hello dear 3D slicer community,</p>
<p>We have annotated a dataset of CT scans using markups in 3D slicer, we have used boxes, fiducials and planes. I have written a python script that would map the coordinate values from the patient coordinate space to pixel space, since we need this for downstream tasks. I have had some success, but also experienced that, there is sometimes an offset by one or two pixels, which is especially a problem regarding the z axis (we are using axial view, so the box is either too hight or too low, compared to the annotations in 3D slicer). I noticed that 3D slicer itself is doing this transformation (since it is displaying both the coordinates and the pixel values in the data probe window in the lower left corner, see attached screenshot). My questions are as follows:</p>
<p>Is there a way to extract the exact transformation equation that 3D slicer is using to be able to display pixel values? It seems to be doing it anyway, so the information must be somewhere right?</p>
<p>Secondly, might there be an easier way of achieving what I want? I basically would like to extract every markup as a nifti file .</p>
<p>Sorry, if this question has come up before, I browsed this forum and did not find anything helpful ragarding this problem so far.</p>
<p>Many thanks,</p>
<p>Johannes<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b8b761897c66fdcc2e417dad366f75b20deed00.png" data-download-href="/uploads/short-url/d3Qf94re7iwrqxZ0PjQjR1PogzS.png?dl=1" title="Bildschirmfoto 2023-06-16 um 16.41.41" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b8b761897c66fdcc2e417dad366f75b20deed00_2_690x260.png" alt="Bildschirmfoto 2023-06-16 um 16.41.41" data-base62-sha1="d3Qf94re7iwrqxZ0PjQjR1PogzS" width="690" height="260" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b8b761897c66fdcc2e417dad366f75b20deed00_2_690x260.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b8b761897c66fdcc2e417dad366f75b20deed00.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b8b761897c66fdcc2e417dad366f75b20deed00.png 2x" data-dominant-color="EAEAEA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto 2023-06-16 um 16.41.41</span><span class="informations">936×354 32.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-06-17 16:56 UTC)

<p>You can have a look at the <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DataProbe/DataProbe.py#L255-L257">source code of the Data Probe module</a> to see how the calculations are done and there should also be good examples in the script repository.</p>

---
