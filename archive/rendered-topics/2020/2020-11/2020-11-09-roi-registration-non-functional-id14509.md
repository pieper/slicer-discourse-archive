---
topic_id: 14509
title: "Roi Registration Non Functional"
date: 2020-11-09
url: https://discourse.slicer.org/t/14509
---

# ROI Registration Non-Functional

**Topic ID**: 14509
**Date**: 2020-11-09
**URL**: https://discourse.slicer.org/t/roi-registration-non-functional/14509

---

## Post #1 by @ahopf (2020-11-09 17:02 UTC)

<p>I am trying to use ROI registration (within the surface registration module) to register two .ply models based on an overlapping section of the models after fiducial registration (which gave close pre-alignment).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc196bd0308f078730d39b4285ca845fe6ceabfc.jpeg" alt="image" data-base62-sha1="t7xRQBJdFKpuafNIOkslV8PgnBW" width="336" height="404"></p>
<p>I have placed the fiducials to border the overlapping region with both the markups module and the built-in landmark functionality in the ROI registration module.</p>
<p>After placing the fiducials and setting an output transform, the module does not run to completion/register the models when I click compute (a previous attempt turned the models blue but also did not work).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4c3342378d5a5d79f52c7628afbb0e8e80059b3.png" data-download-href="/uploads/short-url/nvywG5S2C4VvZcYozNyuiTCCqD9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4c3342378d5a5d79f52c7628afbb0e8e80059b3.png" alt="image" data-base62-sha1="nvywG5S2C4VvZcYozNyuiTCCqD9" width="465" height="499" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">527×566 13.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f389f79085ad9a1bb9ffc79e5f14cc7a978dc1c2.png" data-download-href="/uploads/short-url/yKrCkY66twfTQ9g7QbvxLGLyWNs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f389f79085ad9a1bb9ffc79e5f14cc7a978dc1c2.png" alt="image" data-base62-sha1="yKrCkY66twfTQ9g7QbvxLGLyWNs" width="436" height="500" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">524×600 15.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Error log:</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/socce/AppData/Roaming/NA-MIC/Extensions-28257/CMFreg/lib/Slicer-4.10/qt-scripted-modules/SurfaceRegistration.py”, line 331, in onComputeButton<br>
self.applyROIRegistration(outputTrans)<br>
File “C:/Users/socce/AppData/Roaming/NA-MIC/Extensions-28257/CMFreg/lib/Slicer-4.10/qt-scripted-modules/SurfaceRegistration.py”, line 386, in applyROIRegistration<br>
fixedROIPolydata = self.logic.getROIPolydata(self.inputFixedLandmarksSelector.currentNode())<br>
File “C:/Users/socce/AppData/Roaming/NA-MIC/Extensions-28257/CMFreg/lib/Slicer-4.10/qt-scripted-modules/SurfaceRegistration.py”, line 673, in getROIPolydata<br>
activeLandmarkState = landmarkDescription[markupID]<br>
KeyError: ‘vtkMRMLMarkupsFiducialNode_25’</p>

---
