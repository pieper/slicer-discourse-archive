# Bending 3D model

**Topic ID**: 9340
**Date**: 2019-11-30
**URL**: https://discourse.slicer.org/t/bending-3d-model/9340

---

## Post #1 by @GL1984 (2019-11-30 14:31 UTC)

<p>Hello,<br>
I was wondering if I could use one of Slicer’s extension to bend a 3D model?<br>
Essentially I would like to contour a stabilising plate to the bone model ahead of surgery. I saw that there is an osteotomy planner module somewhere that allow bone bending but for some reason it does not show up on my extension manager. If that extension is still available, could it be used to bend a model of a plate using it?</p>

---

## Post #2 by @lassoan (2019-11-30 15:19 UTC)

<p>You can warp a model by applying a thin-plate spline transform and specifying corresponding point pairs using Fiducial Registration Wizard module (provided by SlicerIGT extension).</p>
<p>However, if you want to create a perfectly fitting “bone plate” directly from your CT then it is easier to create it directly, using Segment Editor:</p>
<ul>
<li>segment the bone</li>
<li>use Hollow effect to create a shell covering the bone</li>
<li>use Scissors effect to cut to the desired shape</li>
<li>keep the side you want to keep using Islands effect (Keep selected island)</li>
<li>you can drill holes into the plate using Scissors effect, with circle shape option</li>
</ul>

---

## Post #3 by @apparrilla (2020-11-07 16:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="9340">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can warp a model by applying a thin-plate spline transform and specifying corresponding point pairs using Fiducial Registration Wizard module (provided by SlicerIGT extension).</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a>. how can I create a new  thin-plate spline transform in Slicer? I´ve triyed to do throw Python Interactor (defTransform = slicer.vtkThinPlateSplineTransform) but I can not see it on Slicer.<br>
Thanks on advance!</p>

---

## Post #4 by @lassoan (2020-11-07 16:24 UTC)

<p>You need to put VTK transform object into a vtkMRMLTransformNode as ToParent or FromParent transform if you want it to appear in the scene.</p>
<p>You can use Fiducial registration wizard module’s logic from Python to do this and synchronize the landmarks in the transform with markups fiducial nodes.</p>

---

## Post #5 by @apparrilla (2020-11-07 23:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="9340">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>and synchronize the landmarks in the transform with markups fiducial nodes.</p>
</blockquote>
</aside>
<p>I can´t understand you…</p>
<p>I did:</p>
<blockquote>
<p>DefTrans=vtk.vtkThinPlateSplineTransform()<br>
T = slicer.mrmlScene.GetFirstNodeByName(‘Transform’)<br>
T.SetAndObserveTransformFromParent(DefTrans)<br>
T.SetAndObserveTransformToParent(DefTrans)</p>
</blockquote>
<p>In Fiducial Registration Wizard:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93d65900ded1ea0b18df27e205bf6934c8975d8b.png" data-download-href="/uploads/short-url/l5PqpeF1bFSC28bxnDuKSoyF74v.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93d65900ded1ea0b18df27e205bf6934c8975d8b_2_380x500.png" alt="image" data-base62-sha1="l5PqpeF1bFSC28bxnDuKSoyF74v" width="380" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93d65900ded1ea0b18df27e205bf6934c8975d8b_2_380x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93d65900ded1ea0b18df27e205bf6934c8975d8b_2_570x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93d65900ded1ea0b18df27e205bf6934c8975d8b_2_760x1000.png 2x" data-dominant-color="30363A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">988×1300 36.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Nodes:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d0af64546a06df120da74734c2f4ad96dc52ba9.png" data-download-href="/uploads/short-url/1RnGYczWWfXLP9uWNRC8f2g8dxT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d0af64546a06df120da74734c2f4ad96dc52ba9.png" alt="image" data-base62-sha1="1RnGYczWWfXLP9uWNRC8f2g8dxT" width="517" height="70" data-dominant-color="354A5D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">985×135 7.23 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Before Wizard:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/1319d1af9b23d460ccd1ae3c5365dd89c3243d75.jpeg" data-download-href="/uploads/short-url/2IYo7BoAZrNBXuxaObZCXSDUaHP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1319d1af9b23d460ccd1ae3c5365dd89c3243d75_2_414x374.jpeg" alt="image" data-base62-sha1="2IYo7BoAZrNBXuxaObZCXSDUaHP" width="414" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1319d1af9b23d460ccd1ae3c5365dd89c3243d75_2_414x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1319d1af9b23d460ccd1ae3c5365dd89c3243d75_2_621x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1319d1af9b23d460ccd1ae3c5365dd89c3243d75_2_828x748.jpeg 2x" data-dominant-color="BDAD87"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1011×914 83.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Result:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ece9c6aced8179d6482f097a085b2e34ac1115c.jpeg" data-download-href="/uploads/short-url/26ZlupPNqhiNcQVUSdStDpXk60k.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ece9c6aced8179d6482f097a085b2e34ac1115c_2_417x375.jpeg" alt="image" data-base62-sha1="26ZlupPNqhiNcQVUSdStDpXk60k" width="417" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ece9c6aced8179d6482f097a085b2e34ac1115c_2_417x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ece9c6aced8179d6482f097a085b2e34ac1115c_2_625x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0ece9c6aced8179d6482f097a085b2e34ac1115c_2_834x750.jpeg 2x" data-dominant-color="9A99BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1137×1019 95.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I don´t know what I´m doing wrong…</p>

---

## Post #6 by @lassoan (2020-11-08 20:38 UTC)

<p>Discussion in this topic should explain how to use FiducialRegistrationWizard module from Python: <a href="https://discourse.slicer.org/t/fiducial-registration-wizard-custom-transformation-configuration/7217/2" class="inline-onebox">Fiducial registration Wizard - custom transformation configuration</a></p>

---
