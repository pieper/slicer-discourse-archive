# Angle planes issue

**Topic ID**: 13471
**Date**: 2020-09-13
**URL**: https://discourse.slicer.org/t/angle-planes-issue/13471

---

## Post #1 by @Malick (2020-09-13 16:59 UTC)

<p>Operating system: Win 10<br>
Slicer version: 4.10.2<br>
Expected behavior: Angles measurements<br>
Actual behavior: Impossible to create a new plane</p>
<p>Python error line<br>
Traceback (most recent call last):<br>
File “C:/Users/Malick/AppData/Roaming/NA-MIC/Extensions-28257/AnglePlanesExtension/lib/Slicer-4.10/qt-scripted-modules/AnglePlanes.py”, line 244, in onLandmarksChanged<br>
onSurface)<br>
File “C:/Users/Malick/AppData/Roaming/NA-MIC/Extensions-28257/AnglePlanesExtension/lib/Slicer-4.10/qt-scripted-modules/AnglePlanes.py”, line 999, in connectLandmarks<br>
PointAddedEventTag = landmarks.AddObserver(landmarks.PointAddedEvent, self.onPointAddedEvent)<br>
AttributeError: ‘vtkSlicerMarkupsModuleMRMLPython.vtkMRMLMarkupsFid’ object has no attribute ‘PointAddedEvent’</p>

---

## Post #2 by @muratmaga (2020-09-13 17:57 UTC)

<p>Planes are incorporated into the Markups module. You will be better of using the latest preview.</p>

---

## Post #3 by @Malick (2020-09-13 21:19 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="13471">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Planes are incorporated into the Markups module. You will be better of using the latest preview</p>
</blockquote>
</aside>
<p>Sorry, I am still stuck<br>
I create markups<br>
I’d like to connect them to create a new plane</p>

---

## Post #4 by @muratmaga (2020-09-13 21:36 UTC)

<p>Did you switch to Markups-&gt; Plane setting:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/984b482918a5ad788b806e5abae934ed87f812b2.png" data-download-href="/uploads/short-url/lJfRHCnSsS6zBCLQzyGIeuTRnQS.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/984b482918a5ad788b806e5abae934ed87f812b2_2_655x500.png" alt="image" data-base62-sha1="lJfRHCnSsS6zBCLQzyGIeuTRnQS" width="655" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/984b482918a5ad788b806e5abae934ed87f812b2_2_655x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/984b482918a5ad788b806e5abae934ed87f812b2_2_982x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/984b482918a5ad788b806e5abae934ed87f812b2_2_1310x1000.png 2x" data-dominant-color="A2A2AE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1704×1299 219 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You can find more details about the Markups module, including how to interactively change planes,  <a href="https://github.com/SlicerMorph/S_2020/blob/master/Day_2/Markups/Markups.md">here</a>:</p>

---

## Post #5 by @Malick (2020-09-13 21:41 UTC)

<p>No such option<br>
I use the 4.10.2 version<br>
I’ll upgrade</p>

---

## Post #6 by @Malick (2020-09-13 22:58 UTC)

<p>Great<br>
Planes created<br>
Final query please: how to calculate angles between planes (created ones and standard ones)</p>

---

## Post #7 by @anasmh101 (2024-02-13 06:15 UTC)

<p>hello, may I ask you if you managed to calculate angles between planes, I am having difficulty in this matter</p>

---
