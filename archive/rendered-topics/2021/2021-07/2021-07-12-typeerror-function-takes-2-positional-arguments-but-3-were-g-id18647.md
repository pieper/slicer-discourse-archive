# TypeError: Function takes 2 positional arguments but 3 were given

**Topic ID**: 18647
**Date**: 2021-07-12
**URL**: https://discourse.slicer.org/t/typeerror-function-takes-2-positional-arguments-but-3-were-given/18647

---

## Post #1 by @Ahmet_Yildiz (2021-07-12 17:12 UTC)

<p>I have been modifying a code to measure angle between Markup lines. It worked just fine in Slicer’s Python terminal. However, as soon as i moved on to create a module the following error pops up:</p>
<p>TypeError: ShowAngle() takes 2 positional arguments but 3 were given.</p>
<p>When i run the module on slicer it gives the angle correctly however, when i start moving the markup line to observe the angle changing i get the previous error.<br>
I am assuming the error is in addObserver function but i am not quite sure about it,</p>
<p>I am using QT Designer for GUI, i am posting a snap shot of the main function.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1259c9ba7a5ab0c7927c44956ef92903a103aa8.png" data-download-href="/uploads/short-url/yphEuPmxWlMIDj87YhG2LArdXWE.png?dl=1" title="image (5)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1259c9ba7a5ab0c7927c44956ef92903a103aa8.png" alt="image (5)" data-base62-sha1="yphEuPmxWlMIDj87YhG2LArdXWE" width="364" height="500" data-dominant-color="F9F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image (5)</span><span class="informations">589×809 9.74 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea35e56a558326d5dda194a99afb8f3805234fe9.png" data-download-href="/uploads/short-url/xpVcp2niJ3U8ZlldaSM4N101PRL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea35e56a558326d5dda194a99afb8f3805234fe9.png" alt="image" data-base62-sha1="xpVcp2niJ3U8ZlldaSM4N101PRL" width="676" height="500" data-dominant-color="424342"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1081×799 39.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51ceb4437d128d7dee4d88a17cb4ea185abb41d1.png" data-download-href="/uploads/short-url/bFHxh8luO16g4ijKA7X8U6lYcgh.png?dl=1" title="image (6)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51ceb4437d128d7dee4d88a17cb4ea185abb41d1.png" alt="image (6)" data-base62-sha1="bFHxh8luO16g4ijKA7X8U6lYcgh" width="618" height="500" data-dominant-color="464745"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image (6)</span><span class="informations">844×682 20.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you so much,</p>

---

## Post #2 by @lassoan (2021-07-12 17:42 UTC)

<p>Callback functions of VTK observers are required to take 2 arguments (<code>caller</code> and <code>eventId</code>). If the callback function is a member of a class then it requires an additional <code>self</code> argument as first argument, so you need a total of 3 arguments.</p>
<p>Note that in current Slicer versions you can use “angle” markup to measure a simple angle.</p>

---

## Post #3 by @Ahmet_Yildiz (2021-07-13 11:48 UTC)

<p>Thank you so much Dr. Lasso for your quick reply,<br>
May i ask about the ruler Markup? It seems that it is only visible at the Sagittal plane of the MRI and also on the 3D section bit not for two other planes. I am aware of Markup line as a valid option but for the code i am working on i found measuring angle in real-time between rulers is easier and also better visualized in both the planes and 3D. Is there is a solution for this?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/819a8f29a5653c6d8e8a9d0414b9154bf554d5ba.jpeg" data-download-href="/uploads/short-url/iuwJAwNzOj8NDA7lWBpfmuBF29Y.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/819a8f29a5653c6d8e8a9d0414b9154bf554d5ba_2_690x222.jpeg" alt="image" data-base62-sha1="iuwJAwNzOj8NDA7lWBpfmuBF29Y" width="690" height="222" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/819a8f29a5653c6d8e8a9d0414b9154bf554d5ba_2_690x222.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/819a8f29a5653c6d8e8a9d0414b9154bf554d5ba_2_1035x333.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/819a8f29a5653c6d8e8a9d0414b9154bf554d5ba.jpeg 2x" data-dominant-color="21201E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1294×418 86.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also about the Measurements module <a href="https://www.slicer.org/wiki/Modules:Measurements-Documentation-3.6" class="inline-onebox" rel="noopener nofollow ugc">Modules:Measurements-Documentation-3.6 - Slicer Wiki</a>, it seems no longer supported for Slicer 4, is it the case?</p>
<p>Thank you again so much.</p>

---

## Post #4 by @lassoan (2021-07-13 12:40 UTC)

<p>Annotations module has several limitations and issues that will not be fixed anymore, it is not compatible with the new event management model that is needed to support new features (such as right-click menu, measurements in virtual reality, etc) and the entire module will be removed. We only keep the Annotations module around so that developers that started off when markups module did not exist have time to update their modules.</p>
<p>We are constantly improving markups, so if you don’t like anything about them then we can fix those. Just let us know what you would like to change. It helps if you attach a screenshot.</p>

---

## Post #5 by @jamesobutler (2021-07-13 12:48 UTC)

<p><a class="mention" href="/u/ahmet_yildiz">@Ahmet_Yildiz</a> Have you tried the Markups module “Angle” object instead of trying to manually determine angle using two lines? Do you not like the look of the “Angle” object?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/708a1bc789a1ef626558ffe17e7face66e27f900.jpeg" data-download-href="/uploads/short-url/g3zn76qa9ICQsipUFKr6O3iUfy8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/708a1bc789a1ef626558ffe17e7face66e27f900_2_690x373.jpeg" alt="image" data-base62-sha1="g3zn76qa9ICQsipUFKr6O3iUfy8" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/708a1bc789a1ef626558ffe17e7face66e27f900_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/708a1bc789a1ef626558ffe17e7face66e27f900_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/708a1bc789a1ef626558ffe17e7face66e27f900_2_1380x746.jpeg 2x" data-dominant-color="8B8B92"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 258 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @Ahmet_Yildiz (2021-07-13 12:48 UTC)

<p>Thank you again Dr. Lasso,<br>
My issue is refining the code written by you to measure angle between rulers in real-time <a href="https://gist.github.com/lassoan/9bf334743871e400f7e3b3745b312b14" class="inline-onebox" rel="noopener nofollow ugc">3D Slicer scripted module for measuring angle between rulers · GitHub</a>,<br>
I tried multiple times for the code to switch from ruler to markup line by changing<br>
self.rulerNodeClass = ‘vtkMRMLAnnotationRulerNode’<br>
To<br>
self.rulerNodeClass = ‘vtkMRMLMarkupsLineNode’</p>
<p>And a wave of errors show up, mainly<br>
AttributeError: ‘vtkSlicerMarkupsModuleMRMLPython.vtkMRMLMarkupsLin’ object has no attribute ‘GetNthNodeByClass’<br>
and some others.</p>
<p>What exactly should be modified for the script to switch from measuring angle between rulers to markup lines?</p>

---

## Post #7 by @Ahmet_Yildiz (2021-07-13 12:52 UTC)

<p>Thank you for your reply <a class="mention" href="/u/jamesobutler">@jamesobutler</a>,<br>
The markupline/ruler will move with respect to needle tracked by optical tracker, that’s why i added addObserver function.<br>
Not sure if the angle can be attached to the tool tip and measure “error” between current tool trajectory and a predefined desired trajectory.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3b8dfe7004c81da77dce0ec13756e01ae55f4d1.jpeg" alt="image" data-base62-sha1="pDTyFLQZaqzIs1j7H2qZVRBzAZz" width="612" height="390"></p>

---

## Post #8 by @jamesobutler (2021-07-13 12:56 UTC)

<p>A vtkMRMLMarkupsAngleNode has 3 control points so if you have observers that are already moving endpoints of some line objects you could instead tell it to update the position of the angle node control points instead.</p>

---

## Post #9 by @Ahmet_Yildiz (2021-07-13 13:03 UTC)

<p>I am not sure i am following here,<br>
Is it possible for one control point from vtkMRMLMarkupsAngleNode  to be fixed on top of created needle/imported needle CAD model and another point on the target (tumor) and a third on current trajectory and measures the angle difference in real time? If yes, how is this exactly possible?</p>
<p>Thank you so much <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>

---

## Post #10 by @lassoan (2021-07-13 13:22 UTC)

<aside class="quote no-group" data-username="Ahmet_Yildiz" data-post="6" data-topic="18647">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/90ced4/48.png" class="avatar"> Ahmet_Yildiz:</div>
<blockquote>
<p>AttributeError: ‘vtkSlicerMarkupsModuleMRMLPython.vtkMRMLMarkupsLin’ object has no attribute ‘GetNthNodeByClass’</p>
</blockquote>
</aside>
<p>This is because you are calling <code>markupsNode.GetNthNodeByClass(...)</code>, while the correct would be <code>slicer.mrmlScene.GetNthNodeByClass(...)</code>. It is not related to using annotations or markups.</p>
<aside class="quote no-group" data-username="Ahmet_Yildiz" data-post="6" data-topic="18647">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/90ced4/48.png" class="avatar"> Ahmet_Yildiz:</div>
<blockquote>
<p>What exactly should be modified for the script to switch from measuring angle between rulers to markup lines?</p>
</blockquote>
</aside>
<p>There is a complete example in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-angle-between-two-markup-lines">script repository</a>.</p>

---

## Post #11 by @Ahmet_Yildiz (2021-07-13 13:30 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> Again thank you for your time,<br>
It seems it’s not possible to “attach” one control point from (markup line/ruler/angle) to a moving needle and observe the angle changing with respect to another fixed markup line/ruler,</p>
<p>As soon as i move the markup line/ruler in transform hierarchy in Data module to the transform where the needle exist “StylusToReference” so they can move at the same rate; the markup line/ruler disappears,</p>
<p>I am wondering how to measure distance/angle between needle (stylus) and target (Tumor) in real time to facilitate navigation. This is my ultimate goal, sorry about this but any idea?</p>

---

## Post #12 by @lassoan (2021-07-13 14:03 UTC)

<p>A transform is always attached to a node, but you can add an observer to a transform and update selected points in the callback function.</p>
<aside class="quote no-group" data-username="Ahmet_Yildiz" data-post="11" data-topic="18647">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/90ced4/48.png" class="avatar"> Ahmet_Yildiz:</div>
<blockquote>
<p>I am wondering how to measure distance/angle between needle (stylus) and target (Tumor) in real time to facilitate navigation. This is my ultimate goal, sorry about this but any idea?</p>
</blockquote>
</aside>
<p>Breach warning module in <a href="https://github.com/SlicerIGT/SlicerIGT">SlicerIGT extension</a> is developed exactly for this purpose (for example, it is used extensively for navigated breast tumor resection).</p>

---
