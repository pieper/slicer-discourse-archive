# Elastix displacement vector field output

**Topic ID**: 8339
**Date**: 2019-09-09
**URL**: https://discourse.slicer.org/t/elastix-displacement-vector-field-output/8339

---

## Post #1 by @labixin (2019-09-09 01:49 UTC)

<p>Operating system: Win7<br>
Slicer version: 4.11.0-2019-08-13 r28438</p>
<p>Hi all,</p>
<p>I am registering two ct images using SlicerElastix (Preset-generic (all)). Now I want to get the displacement field merely indicating bspline transform. Can I just subtract the linear part and how to accomplish this using python interactor? Besides, I would like to get the displacement of specific points in moving image. Could I invert displacement field and save it to nrrd file? I have looked through the <a href="https://discourse.slicer.org/t/using-the-invert-displacement-field-function/4768/3">discussion thread</a> but still have no idea how to do that.</p>
<p>Hope for some advice! Your help is highly appreciated!!</p>
<p>Crayon</p>

---

## Post #2 by @lassoan (2020-04-04 20:56 UTC)

<aside class="quote no-group" data-username="labixin" data-post="1" data-topic="8339">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>Can I just subtract the linear part and how to accomplish this using python interactor?</p>
</blockquote>
</aside>
<p>You can “Split” button in Transforms module (or call <code>Split</code> method of the transform node) to split a composite transform to its components.</p>
<aside class="quote no-group" data-username="labixin" data-post="1" data-topic="8339">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>Besides, I would like to get the displacement of specific points in moving image.</p>
</blockquote>
</aside>
<p>You can set all your input points in a vtkMRMLMarkupsFiducialNode, apply the transform, and get the transformed point coordinates using <code>GetNthControlPointPositionWorld</code>. There are also convenience functions in <code>slicer.util</code> to get/set point positions in Python from numpy arrays.</p>
<aside class="quote no-group" data-username="labixin" data-post="1" data-topic="8339">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>Could I invert displacement field and save it to nrrd file?</p>
</blockquote>
</aside>
<p>You can invert a transform by clicking “Invert” click (or call <code>Inverse</code> method of the transform node) and export it to displacement field using “Convert” section of Transforms module (or from Python, using transforms module logic).</p>

---
