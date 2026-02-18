# Exporting markup plane as an stl model

**Topic ID**: 31621
**Date**: 2023-09-08
**URL**: https://discourse.slicer.org/t/exporting-markup-plane-as-an-stl-model/31621

---

## Post #1 by @mohammed_alshakhas (2023-09-08 17:46 UTC)

<p>is it possible to export a  plane as an STL model?</p>
<p>my reason is that I can fit a pLane as a guide for surgical correction in 3dslicer since I can visualize volume rendering with models. but I still need to finish my workflow in other software like Meshmixer and Freeform.</p>
<p>i could not figure out a way to export the plane as an STL.</p>

---

## Post #2 by @mau_igna_06 (2023-09-08 18:17 UTC)

<p>Hi</p>
<p>Please check:<br>
<a href="https://vtk.org/doc/nightly/html/classvtkPlaneSource.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://vtk.org/doc/nightly/html/classvtkPlaneSource.html</a><br>
And first part of this:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-segmentation-from-a-model-node" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-segmentation-from-a-model-node</a></p>
<p>Replace the sphere by the plane</p>
<p>Hope it helps</p>

---

## Post #3 by @mohammed_alshakhas (2023-09-08 18:29 UTC)

<p>unfortunately, I have no ability to code. was hoping there is a direct way from slicer</p>

---

## Post #4 by @lassoan (2023-09-08 21:14 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="1" data-topic="31621">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>I still need to finish my workflow in other software like Meshmixer and Freeform</p>
</blockquote>
</aside>
<p>What do you need to do in Meshmixer and Freeform?</p>

---

## Post #5 by @mohammed_alshakhas (2023-09-08 23:55 UTC)

<p>I do the following<br>
Models registration ( tried and failed in 3d slicer )<br>
Osteotomies ( crazy simple in meshmixer)<br>
Transformation ( which I hate doing in 3d slicer for it’s difficult control )<br>
Creation of surgical guides</p>

---

## Post #6 by @lassoan (2023-09-09 10:59 UTC)

<p>Thank you this is useful.</p>
<p>What museum registering methods have you tried?</p>
<p>Have you tried Dynamic modeler module for osteotomy?</p>
<p>By transformation you mean translating/rotating a model in 3D view by click-and-dragging arrows? How do you determine the curve position?</p>
<p>What kind of surgical guides do you create - plates, cutting guides,…? Fire what clinical procedures? Have you tried the <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner">Bone Reconstruction Planner extension</a>? There are also other extensions that allow you to create osteotomies and surgical plans and even real-time guidance during the procedure.</p>

---

## Post #7 by @mohammed_alshakhas (2023-09-09 11:24 UTC)

<p>a single osteotomy has 3 or 4 planes. That makes it so hard to do in most software except for ones designed for clinicians with presets. however, the way I do it in meshmixer is by selecting brush and then “separate” action.  which is very detailed and quick.  Actually, it is done better in Meshmixer compared to the specific clinical software I use for my cases. ( IPS case designer )</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be80c2c85666bdf6f51146a310c4d0ea148e9ac2.jpeg" data-download-href="/uploads/short-url/rbgAtkzSL9upYG0G8Je1yaFH1Z0.jpeg?dl=1" title="Screenshot 2023-09-09 at 14.22.17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be80c2c85666bdf6f51146a310c4d0ea148e9ac2_2_578x500.jpeg" alt="Screenshot 2023-09-09 at 14.22.17" data-base62-sha1="rbgAtkzSL9upYG0G8Je1yaFH1Z0" width="578" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be80c2c85666bdf6f51146a310c4d0ea148e9ac2_2_578x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be80c2c85666bdf6f51146a310c4d0ea148e9ac2_2_867x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be80c2c85666bdf6f51146a310c4d0ea148e9ac2_2_1156x1000.jpeg 2x" data-dominant-color="969592"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-09-09 at 14.22.17</span><span class="informations">1278×1104 87.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/002783f15222cbdd0212ac52666a4787a7432d5d.jpeg" data-download-href="/uploads/short-url/1mF0fHH7Fakj28Jj6jKCnGW6V7.jpeg?dl=1" title="Screenshot 2023-09-09 at 14.22.10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/002783f15222cbdd0212ac52666a4787a7432d5d_2_690x453.jpeg" alt="Screenshot 2023-09-09 at 14.22.10" data-base62-sha1="1mF0fHH7Fakj28Jj6jKCnGW6V7" width="690" height="453" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/002783f15222cbdd0212ac52666a4787a7432d5d_2_690x453.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/002783f15222cbdd0212ac52666a4787a7432d5d_2_1035x679.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/002783f15222cbdd0212ac52666a4787a7432d5d_2_1380x906.jpeg 2x" data-dominant-color="A19C96"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-09-09 at 14.22.10</span><span class="informations">1556×1022 94.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(The one done in the picture took less than 1 minute to perform osteotomy )</p>
<p>I tried using Easy Clip and Osteotomy Planner and couldn’t use them well  (Osteotomy Planner crashes 100% of the time )</p>
<p>the method I use for registration is by making the fixed segment as a magnet, then brushing the moving segment in characteristic areas. then   using the align  to target  tool ( another robust tool in mesh mixer that  I didn’t  see any other software does better )</p>
<p>for the guides, I use mostly osteotomy guides. for chin osteotomy for example. since this osteotomy is almost never symmetrical in real life, guides are very helpful.  This process requires many other tools for CAD and model editing</p>

---
