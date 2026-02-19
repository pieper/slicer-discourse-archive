---
topic_id: 931
title: "Merging Two Models"
date: 2017-08-23
url: https://discourse.slicer.org/t/931
---

# Merging two models

**Topic ID**: 931
**Date**: 2017-08-23
**URL**: https://discourse.slicer.org/t/merging-two-models/931

---

## Post #1 by @jimmylarson (2017-08-23 15:45 UTC)

<p>Operating system:windows<br>
Slicer version:4.6.2<br>
Expected behavior: I am trying to merge two different models that I made in the editor module. I trying to put dots to map out where buds are on a tree trunk that I have a scan of. I first used the threshold effect to create the surface of the trunk, this was my “master volume” and then I clicked the “create new label map” under “merge volume” and used the paint brush to create map of dots. I want to have my finished model showing these two models together<br>
Actual behavior: When I go to save as an .stl, I can only save each model separately (the dots as one model, and the trunk as another). I can see the models together in the viewer, but I don’t know how to make them one who I go to save. Thanks</p>

---

## Post #2 by @lassoan (2017-08-23 15:51 UTC)

<p>I would recommend to use Segment Editor module (<a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a>)  in latest nightly version of Slicer. You can merge segments using Logical operators effect.</p>

---

## Post #3 by @jimmylarson (2017-08-23 18:10 UTC)

<p>Thank you for the reply. I’ve found the logical operator effect, but I can’t seem to figure out how to merge segments or how to make a segment. Do I need to repeat the process that I did in the regular editor to make the map and surface or can I use what I already have?</p>
<p>Thank you for your help</p>

---

## Post #4 by @cpinter (2017-08-23 18:27 UTC)

<p>Adding a segment: Click Add segment</p>
<p>Merging: See 3D printing tutorial <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_3D_Printing" class="inline-onebox">Documentation/Nightly/Training - Slicer Wiki</a><br>
Here’s the relevant figure<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a3c65f67c0515f5f5dcc85ba0709191732cf743.png" alt="image" data-base62-sha1="61DsiNwuaX3C5Spq0nQ9tiXgB8f" width="603" height="440"></p>

---

## Post #5 by @fedorov (2017-08-23 18:34 UTC)

<aside class="quote no-group quote-modified" data-username="jimmylarson" data-post="3" data-topic="931">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ecae2f/48.png" class="avatar"> jimmylarson:</div>
<blockquote>
<p>I am trying to merge two different models that I made in the editor module.<br>
I can’t seem to figure out how to […] make a segment</p>
</blockquote>
</aside>
<p>You will need to import the models first into a segmentation. Go to Segmentations module, make a new segmentation, then in the Import/export section make a selection to import the model hierarchy:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e8226e054acbb658dab2def33d8edbb4da44b5b.png" data-download-href="/uploads/short-url/i390DN69YQ594SpyrVyL5OTfwL1.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7e8226e054acbb658dab2def33d8edbb4da44b5b_2_402x500.png" alt="image" data-base62-sha1="i390DN69YQ594SpyrVyL5OTfwL1" width="402" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7e8226e054acbb658dab2def33d8edbb4da44b5b_2_402x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7e8226e054acbb658dab2def33d8edbb4da44b5b_2_603x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/7e8226e054acbb658dab2def33d8edbb4da44b5b_2_804x1000.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">888×1104 80.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> the “Import” button in the import/export section should either automatically make a new segmentation node on import, or be disabled until segmentation node is selected - agreed?</p>

---

## Post #6 by @jimmylarson (2017-08-24 15:55 UTC)

<p>Thank you for your help, that seems to have worked. My ultimate goal is to be able to input my model into a powerpoint presentation. So far, I am only familiar with saving the model as a .stl file and then converting it to a pdf to input into powerpoint. When I go to save my segmentation, the only file format options I have are .seg.nrrd or .nrrd. Do you know if either of those is an acceptable format to put into powerpoint or how I would go about doing that. Thank you</p>

---

## Post #7 by @fedorov (2017-08-24 16:09 UTC)

<p>You can use the “Export” option from the module to export your segmentation to “Models”. Those can be saved as STL.</p>

---

## Post #8 by @lassoan (2017-08-24 18:00 UTC)

<p>You can also create nice video animations (rotate your model, sweep through slices) by using Screen Capture module (in Utilities category). You can export videos that you can add into your PPT directly.</p>

---

## Post #9 by @jimmylarson (2017-08-25 13:40 UTC)

<p>Thank you for all your help, that worked. The only problem I have now is that when I open the .stl file and convert it to a pdf the whole model is in the grey scale color of the scan. Is there a way that I can keep the color of my segments from segment editor?</p>

---

## Post #10 by @lassoan (2017-08-25 13:51 UTC)

<p>STL file format has no standard way of storing colors.</p>
<p>For simple animations, you can export videos using <a href="https://www.slicer.org/wiki/Documentation/4.6/Modules/ScreenCapture">ScreenCapture module</a>.</p>
<p>If you need more sophisticated animations then you can <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_entire_scene_as_VRML">export the complete scenes (including color and opacity information)</a> and use a professional animation software, such as <a href="https://www.blender.org/">Blender</a>, to create a video.</p>

---

## Post #11 by @jimmylarson (2017-08-25 16:08 UTC)

<p>I can’t seem to get the screen capture module to take video. It’s capturing single image but not video. I’ve set up the ffmpeg.exe, still nothing though. Thanks<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ec15980120ba186e570a0804cec941a4a10d52b.jpeg" data-download-href="/uploads/short-url/mEpGMcZe6Kue3gIbT5fEYlvBIdJ.JPG?dl=1" title="IMG_2463" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9ec15980120ba186e570a0804cec941a4a10d52b_2_666x500.JPG" alt="IMG_2463" data-base62-sha1="mEpGMcZe6Kue3gIbT5fEYlvBIdJ" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9ec15980120ba186e570a0804cec941a4a10d52b_2_666x500.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9ec15980120ba186e570a0804cec941a4a10d52b_2_999x750.JPG 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/9ec15980120ba186e570a0804cec941a4a10d52b_2_1332x1000.JPG 2x" data-dominant-color="A19C93"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_2463</span><span class="informations">2015×1511 1.47 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @lassoan (2017-08-25 16:37 UTC)

<p>At “Number of images”, unclick the “single” option.</p>

---

## Post #13 by @jimmylarson (2017-08-25 17:23 UTC)

<p>That worked perfectly. Thank you</p>

---

## Post #14 by @gleman (2018-01-25 16:52 UTC)

<p>Any hints on how to do this via python?  I’m thinking of being able to accept an STL file from the user and automatically build the segmentation without any other clicks.</p>

---

## Post #15 by @lassoan (2018-01-25 18:50 UTC)

<p>Do you mean you would like to be able to load an STL file directly as a Segmentation node (avoid going to Segmentations module, creating new segmentation, and importing the model node)?</p>

---

## Post #16 by @gleman (2018-01-25 19:11 UTC)

<p>That would be great, but I’d settle for tips on how to import the model into the segmentation via python rather than going through the interface.</p>

---

## Post #17 by @lassoan (2018-01-25 19:56 UTC)

<p>I’ll implement it now, it should be really simple.</p>

---

## Post #18 by @lassoan (2018-01-25 21:58 UTC)

<p>Implementation is completed, it’ll be available in the nightly release tomorrow.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5db3d50f8517651e2ca56847ab1cfdd892f54624.png" data-download-href="/uploads/short-url/dmVH0etXFlSCo9zKWA2ZU4hkN3S.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5db3d50f8517651e2ca56847ab1cfdd892f54624_2_690x496.png" alt="image" data-base62-sha1="dmVH0etXFlSCo9zKWA2ZU4hkN3S" width="690" height="496" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5db3d50f8517651e2ca56847ab1cfdd892f54624_2_690x496.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5db3d50f8517651e2ca56847ab1cfdd892f54624.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5db3d50f8517651e2ca56847ab1cfdd892f54624.png 2x" data-dominant-color="BDBCC2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">837×602 49.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/cpinter">@cpinter</a></p>

---
