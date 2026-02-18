# How to set makupline diameter to absolute?

**Topic ID**: 17738
**Date**: 2021-05-22
**URL**: https://discourse.slicer.org/t/how-to-set-makupline-diameter-to-absolute/17738

---

## Post #1 by @apparrilla (2021-05-22 23:27 UTC)

<p>Hi everyone!<br>
I need to change Line Thickness Display Property to an absolute value by script.<br>
Something like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e87c364ceb92261e63e5f56a1afde5c40466b4d.png" data-download-href="/uploads/short-url/dufKJ3YOucYlJmBG2qvr5PC21vn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e87c364ceb92261e63e5f56a1afde5c40466b4d_2_517x178.png" alt="image" data-base62-sha1="dufKJ3YOucYlJmBG2qvr5PC21vn" width="517" height="178" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e87c364ceb92261e63e5f56a1afde5c40466b4d_2_517x178.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e87c364ceb92261e63e5f56a1afde5c40466b4d_2_775x267.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e87c364ceb92261e63e5f56a1afde5c40466b4d_2_1034x356.png 2x" data-dominant-color="3D3A3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1142×395 19.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks on advance!</p>

---

## Post #2 by @jamesobutler (2021-05-23 01:28 UTC)

<p>It appears you are looking for the following method available in the vtkMRMLMarkupsDisplayNode as this would be for the markups line node display settings.</p>
<p><a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsDisplayNode.html#a5e452bb436f3b4cfbecef72518ce26a9" class="onebox" target="_blank" rel="noopener nofollow ugc">https://apidocs.slicer.org/master/classvtkMRMLMarkupsDisplayNode.html#a5e452bb436f3b4cfbecef72518ce26a9</a></p>

---

## Post #3 by @apparrilla (2021-05-23 06:26 UTC)

<p>Not exactly. SetUseGlyphScale() works like upside “Glyph Size” toggle button. I need downside “Line Thickness” toggle button. I´ve been looking fot it in vtkMRMLMarkupsDisplayNode documentation but I cannot find a proper method for it…</p>
<p>Thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a> .</p>

---

## Post #4 by @jamesobutler (2021-05-23 13:14 UTC)

<p>Which specific Markups node type are you using?</p>

---

## Post #5 by @apparrilla (2021-05-23 19:59 UTC)

<p>vtkMRMLMarkupsLineNode.<br>
Maybe I get solution: I´m using these two methods SetCurveLineSizeMode(1) and SetLineDiameter(1.0) and it works…</p>

---
