---
topic_id: 31635
title: "How To Make A Translucent Model Suitable For Scientific Publ"
date: 2023-09-09
url: https://discourse.slicer.org/t/31635
---

# How to make a translucent model suitable for scientific publication

**Topic ID**: 31635
**Date**: 2023-09-09
**URL**: https://discourse.slicer.org/t/how-to-make-a-translucent-model-suitable-for-scientific-publication/31635

---

## Post #1 by @pawel (2023-09-09 17:36 UTC)

<p>Hello,</p>
<p>How to make a translucent model  which I will then be able to export as a semi-transparent model.<br>
And I know the “opacity” option but after exporting the stl model this model is still opacity. I want semi-transparent model.<br>
Example figure with random article.  I would like to do similar effect.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/448b48b9089b5de6da73884d61de1cd11ce16adb.jpeg" data-download-href="/uploads/short-url/9MmSJg0XYkCDUoArgnJHeYT5L5x.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/448b48b9089b5de6da73884d61de1cd11ce16adb_2_527x500.jpeg" alt="image" data-base62-sha1="9MmSJg0XYkCDUoArgnJHeYT5L5x" width="527" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/448b48b9089b5de6da73884d61de1cd11ce16adb_2_527x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/448b48b9089b5de6da73884d61de1cd11ce16adb_2_790x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/448b48b9089b5de6da73884d61de1cd11ce16adb.jpeg 2x" data-dominant-color="E0E0E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1000×948 71.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-09-10 01:29 UTC)

<p>We usually just set the view background color to white for publications.</p>
<p>But if you want to capture a screenshot with transparent background then you can do that by copy-pasting <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#capture-3d-view-into-png-file-with-transparent-background">this script</a> into the Python console.</p>

---

## Post #3 by @pawel (2023-09-10 08:18 UTC)

<p>Thanks for the answer<br>
I understand that I cannot export a transparent model. Directly in 3D slicer,I need to take a screenshot “3d view” with translucent model skull with brain cast  and then change the background in Photoshop, etc or maybe is there a suitable tool for making a white background directly in 3D slicer?<br>
How option “opacity” is better in “Segmentations” or “Models”.</p>

---

## Post #4 by @lassoan (2023-09-10 12:38 UTC)

<aside class="quote no-group" data-username="pawel" data-post="3" data-topic="31635">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/ecae2f/48.png" class="avatar"> pawel:</div>
<blockquote>
<p>I understand that I cannot export a transparent model</p>
</blockquote>
</aside>
<p>You can actually export a transparent model, directly in Slicer, using the script that I linked above. You can copy that image over content in Word, PowerPoint, etc. and the background will be visible wherever the view content is transparent.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa2ad0c502fb59ac6cad21dded0da22f77c9255f.png" data-download-href="/uploads/short-url/zH56a8svocZKhwGhAC0MWILfg2H.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa2ad0c502fb59ac6cad21dded0da22f77c9255f_2_690x458.png" alt="image" data-base62-sha1="zH56a8svocZKhwGhAC0MWILfg2H" width="690" height="458" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa2ad0c502fb59ac6cad21dded0da22f77c9255f_2_690x458.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa2ad0c502fb59ac6cad21dded0da22f77c9255f_2_1035x687.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa2ad0c502fb59ac6cad21dded0da22f77c9255f_2_1380x916.png 2x" data-dominant-color="64666C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1544×1026 251 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can also set the view background to white if you know that you’ll show the content over white background and then you don’t need to copy-paste a script.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17710f8d56aa17f3744b12b9e6674b53aee591e2.jpeg" data-download-href="/uploads/short-url/3lnde9SvpaYBLpBAjPmBq0n9KJs.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17710f8d56aa17f3744b12b9e6674b53aee591e2_2_658x500.jpeg" alt="image" data-base62-sha1="3lnde9SvpaYBLpBAjPmBq0n9KJs" width="658" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17710f8d56aa17f3744b12b9e6674b53aee591e2_2_658x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17710f8d56aa17f3744b12b9e6674b53aee591e2.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17710f8d56aa17f3744b12b9e6674b53aee591e2.jpeg 2x" data-dominant-color="A6A9AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">934×709 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="pawel" data-post="3" data-topic="31635">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/ecae2f/48.png" class="avatar"> pawel:</div>
<blockquote>
<p>How option “opacity” is better in “Segmentations” or “Models”.</p>
</blockquote>
</aside>
<p>There is no difference, they are both equally good for making a 3D object semi-transparent.</p>

---

## Post #5 by @pawel (2023-09-10 13:53 UTC)

<p>Thank you for your answer.Your answer is very helpful:)</p>
<p>I see that also turning off the “3D cube” and “3D axis label” options will allow me to get an effect like in the attached image.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cf233cc3108673213a404f1aad915c8cfb8498d.jpeg" data-download-href="/uploads/short-url/dgeQhZnr5x6fktxBRTfiGArZ03b.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cf233cc3108673213a404f1aad915c8cfb8498d.jpeg" alt="image" data-base62-sha1="dgeQhZnr5x6fktxBRTfiGArZ03b" width="526" height="500" data-dominant-color="E0DFE3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">790×750 52.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Best,</p>

---

## Post #6 by @muratmaga (2023-09-10 15:33 UTC)

<p>Also, explore the Lights module in Sandbox extension for better control over shadows.</p>

---

## Post #7 by @pawel (2023-09-11 16:12 UTC)

<p>Thank you for answer.<br>
I understand that the only option to take a screenshot is the “3D View” is the "Annotation Screenshot  option?<br>
Is there a 3d view rendering option?<br>
Best,</p>

---

## Post #8 by @muratmaga (2023-09-11 17:28 UTC)

<p>You can use that (and simply switch to 3D layout option for 3D rendering only screenshot). Or you can follow the contents of this thread to create a high-resolution capture via little bit of python scripting:</p>
<aside class="quote quote-modified" data-post="30" data-topic="8880">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/higher-resolution-for-screen-captures-of-3d-view/8880/30">Higher resolution for screen captures of 3D view?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You made me curious, so I tried <a href="https://kitware.github.io/vtk-examples/site/Cxx/Utilities/OffScreenRendering/">offscreen rendering</a> and it basically works, although it sometimes leads to a crash when interacting with the view after rendering.  But something like the code below could be added as a feature if someone wants to play with it.  It could use more tweaks, but if it’s useful for people we could put it in the script repository for now. 
Here’s the full res 5kx5x version: 

 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e786811920cc3e684ad3f938add3e1a5cc22ce52.jpeg" data-download-href="/uploads/short-url/x2at7QZEtOgPUulGLquLePyQ0G6.jpeg?dl=1" title="image">[image]</a> 

vtk.vtkGraphicsFactory()
gf = vtk.vtkGraphicsFactory()
gf.SetOffScreenOnlyMode(1)
gf…
  </blockquote>
</aside>


---

## Post #9 by @pawel (2023-09-11 21:41 UTC)

<p>Thank you<br>
I have one more question.<br>
I made a model in 3D slicer with a semi-transparent human body model and non-transparent bone model.<br>
I have a problem because there is a strange overlap between the human body model (white model) and the bone model (red).<br>
Can this be fixed?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1b6df984e111be74da51fc0f28644b50a6d6005.jpeg" data-download-href="/uploads/short-url/n4AFZhxHQ3RhYaicGk90izsxDU1.jpeg?dl=1" title="image190" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1b6df984e111be74da51fc0f28644b50a6d6005_2_690x494.jpeg" alt="image190" data-base62-sha1="n4AFZhxHQ3RhYaicGk90izsxDU1" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1b6df984e111be74da51fc0f28644b50a6d6005_2_690x494.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1b6df984e111be74da51fc0f28644b50a6d6005_2_1035x741.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1b6df984e111be74da51fc0f28644b50a6d6005_2_1380x988.jpeg 2x" data-dominant-color="DCD4D1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image190</span><span class="informations">6151×4412 1.12 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2023-09-12 22:48 UTC)

<p>This looks like “z fighting” - almost equal surface mesh elements are rendered on top of each other.</p>
<p>Do you still display the original segmentation and the exported model? Hiding the segmentation or the model will fix the issue then.</p>
<p>Have you enabled “depth peeling” in the 3D view controller? That option is required for correct rendering of transparent surfaces.</p>

---

## Post #11 by @pawel (2023-09-13 10:52 UTC)

<p>Thanks for help.<br>
Yes,  “depth peeling” function is enabled.</p>
<p>I first exported “the human body” segmentation as a model then bone (red) segmentation exported  as a model and I see that there is no longer a problem. First I did  white model then a red  model.</p>

---

## Post #12 by @pieper (2023-09-13 18:22 UTC)

<p>To me this looks like you have a “negative” of the vertebra as part of the body model.  One option is to segment the body first (with threshold say), close any connections to the outside air and remove islands to get a homogeneous block.  Then add the vertebra segment.</p>

---
