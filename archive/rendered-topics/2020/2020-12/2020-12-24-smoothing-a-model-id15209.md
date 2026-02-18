# Smoothing a model

**Topic ID**: 15209
**Date**: 2020-12-24
**URL**: https://discourse.slicer.org/t/smoothing-a-model/15209

---

## Post #1 by @treecrotch (2020-12-24 03:59 UTC)

<p>Hi. I’m sorry if this is asked often…</p>
<p>I started a basic segmentation of a femur from an MRI<br>
Here is a picture:<br>
                    <a href="https://i.ibb.co/qWy8N0b/femur.jpg" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://i.ibb.co/qWy8N0b/femur.jpg" width="690" height="490">
          </a>

</p>
<p>How do you smooth it and get rid of those largely stair stepped sides?</p>

---

## Post #2 by @lassoan (2020-12-24 04:00 UTC)

<p>This is because voxels are not cubic but stick-shaped. You can fix the issue by cropping and resampling the volume before starting the segmentation using Crop volume module, with isotropic spacing option enabled.</p>

---

## Post #3 by @treecrotch (2020-12-29 17:21 UTC)

<p>Thank you, sorry for my delay in response.<br>
I just tried a sample test with this.</p>
<p>Am I understanding correctly that what this is doing, is creating more “source” images by interpolating between the original images.</p>
<p>And I am then to manually segment this new, larger number set of images, which creates a finer set of segmentation / finer model. Is that correct?</p>
<p>Is there a way to take the first model I posted, with rougher segment spacing, and interpolate those segments from the model creating a smoothing effect on it?</p>

---

## Post #4 by @lassoan (2020-12-29 17:43 UTC)

<p>Yes, sure. You can change the segment geometry to have isotropic spacing by using “Specify geometry” button in <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html">Segment Editor module</a>.</p>

---

## Post #5 by @treecrotch (2020-12-29 18:34 UTC)

<p>Using the same model listed above, I selected Specify geometry, isotopic spacing. but i end up with almost the same result of largely stepped slices unfortunately</p>

---

## Post #6 by @lassoan (2020-12-29 18:59 UTC)

<p>When you specify a new geometry, the original content of the segmentation is preserved, but you can represent smaller details. If you want to make the segment smoother then you can use smoothing effect. It will smooth out details along each axis, so you might get slightly better results if you restart the segmentation from scratch, using this finer geometry.</p>

---

## Post #7 by @treecrotch (2020-12-29 19:45 UTC)

<p>thanks. that almost worked.</p>
<p>I tried to reapply smoothing after selecting specify new geometry and yes, it did seem better.<br>
This is a pic with one click of a circle smoothing brush, and its not a terrible result.</p>
<p>pic:<br>
                    <a href="https://i.ibb.co/99dfjcy/green.jpg" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://i.ibb.co/99dfjcy/green.jpg" width="514" height="500">
          </a>

</p>
<p>However any attempt to use the brush on the rest of it, or apply smoothing to the model without a brush. The whole software just freezes up and reports using 100% of all 12 cores on the pc, resulting in a crash/ force close</p>
<p>This only seems to happen after doing the specify geometry.</p>
<p>sounds like I might have to just start over with your original suggestion, using the crop volume module, which if I’m understanding this correctly, is starting with a better spacing from the beginning.</p>

---

## Post #8 by @lassoan (2020-12-29 20:18 UTC)

<p>What operating system and how much RAM do you have? If you save the segmentation and load it does everything work fine?</p>

---

## Post #9 by @treecrotch (2020-12-29 21:15 UTC)

<p>Actually no, i see now that it doesn’t seem to save and load properly.</p>
<p>I have the original posted project saved as as .mrb file.<br>
It loads fine.</p>
<p>If I apply the “segmentation geometry” and then save it (also as a .mrb)  when it loads the model is blank</p>
<p>ill try to play around with that a bit.</p>
<p>Heres some pc specs:</p>
<p>Windows 10<br>
Version 20H2 (OS Build 19042.685)</p>
<p>32GB DDR4 RAM</p>
<p>NVIDIA GeForce RTX 2060 super</p>
<p>AMD Ryzen 9 3900x</p>
<p>Slicer version 4.13.0-2020-12-22<br>
(I think i downloaded a beta version when trying to get a smoothing brush)</p>

---

## Post #10 by @treecrotch (2020-12-29 22:19 UTC)

<p>specify new geometry &gt; oversampling value was 1. I had experimented with 1 and above.</p>
<p>Until now I set it to 0.5 and i’m getting some ability to smooth without crash. I’m still not very good at the program so my results are a bit bad, but getting there.</p>

---

## Post #11 by @lassoan (2020-12-29 22:24 UTC)

<p>What is the resulting “Dimensions” values in the Segmentation geometry window?</p>

---

## Post #12 by @treecrotch (2020-12-29 22:37 UTC)

<p>Here is the saved model as I load it, the box shape is probably a bit weird?<br>
                    <a href="https://i.ibb.co/GFStXGS/box.jpg" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://i.ibb.co/GFStXGS/box.jpg" width="690" height="384">
          </a>

</p>
<p>Here are the dimensions inside the segmentation geometry window before and after choosing isotropic spacing.</p>
<p>                    <a href="https://i.ibb.co/WWS9v9m/a.jpg" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://i.ibb.co/WWS9v9m/a.jpg" width="690" height="435">
          </a>

</p>
<p>                    <a href="https://i.ibb.co/TK0981s/b.jpg" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://i.ibb.co/TK0981s/b.jpg" width="690" height="435">
          </a>

</p>
<p>          <a href="https://i.ibb.co/wM4QWPx/c.jpg" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://i.ibb.co/wM4QWPx/c.jpg" width="690" height="435">
          </a>
</p>

---

## Post #13 by @lassoan (2020-12-30 05:29 UTC)

<p>Something is wrong with this volume’s physical size:<br>
343 x 0.29mm = 99mm<br>
512 * 3mm = 1536mm<br>
31 * 0.29mm = 9mm</p>
<p>153cm height is way too big, and 9mm depth seems too small. If you can share the original dataset then we can investigate further.</p>
<p>I would recommend to restart the segmentation from scratch on a volume that you cropped&amp;resampled with Crop volume module.</p>

---

## Post #14 by @treecrotch (2021-01-02 02:20 UTC)

<p>I’m super new at this and just learning the very basics.<br>
I appreciate all the help so far, if you don’t have the time to keep holding my hand through it i completely understand.</p>
<p>That said if you want to take a look, and tell me if something is odd about my dicom files.<br>
Here is the link:</p>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1STY3dAhbxEAZwiGVmRBP2DqKgJ0JLGyO/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1STY3dAhbxEAZwiGVmRBP2DqKgJ0JLGyO/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1STY3dAhbxEAZwiGVmRBP2DqKgJ0JLGyO/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">DICOM.zip</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>It loads up a few sets of images, I was segmenting these 2:<br>
PD GAD AXIAL<br>
PD GAD SAG</p>
<p>I tried to anonymize it with dicom library website but the new files still had the name in it.</p>
<p>So here is the full original, with name (my name)<br>
Just don’t post it publicly if you don’t mind…not really a big deal though.</p>

---

## Post #15 by @sfat (2023-12-18 03:47 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> When i use totalsegmentator on any dicom I get stepped outputs as well, and i can’t figure out the right pre-processing setting in segmentation geometry. The example below is from the sample dataset provided by 3dslicer where I applied totalsegmentators without any modification to any settings and it really looks super low res. Any suggestions ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9241ae6a4f48d8718b8afd865d32329eebb1b47.jpeg" data-download-href="/uploads/short-url/xgsBx8KVCc7ytRmKZ2oOYYSz2Ll.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9241ae6a4f48d8718b8afd865d32329eebb1b47_2_690x407.jpeg" alt="image" data-base62-sha1="xgsBx8KVCc7ytRmKZ2oOYYSz2Ll" width="690" height="407" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9241ae6a4f48d8718b8afd865d32329eebb1b47_2_690x407.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9241ae6a4f48d8718b8afd865d32329eebb1b47_2_1035x610.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9241ae6a4f48d8718b8afd865d32329eebb1b47_2_1380x814.jpeg 2x" data-dominant-color="7B6A61"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1392×823 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @lassoan (2023-12-18 04:34 UTC)

<p>This looks pretty good to me. You can disable  fast mode (if you have not done it already) and you could slightly shrink the segments and use them as seeds for Grow from seeds effect to add more details. However, for most use cases it is not necessary to have smaller labelmap voxels. What is your use case? What details would you like to see with finer resolution, for what purpose?</p>

---

## Post #17 by @sfat (2023-12-18 04:42 UTC)

<p>I need to get the aorta for CFD modelling, and the stepped effect messes up with my model. when I smooth the results, it shrinks the segmentation which seems to make the results unreliable</p>

---

## Post #18 by @lassoan (2023-12-18 05:05 UTC)

<p>Have you used fast mode? That already gives about 2x higher resolution along each axis.</p>
<p>You can also increase “smoothing factor” for closed surface representation generation (using the drop-down menu of the “Show 3D” button), which should make the surface smoother without affecting the aorta diameter.</p>
<p>If that smoothness is not sufficient then you can create an aorta seed (by shrinking the aorta segment a little bit) and background segment (by inverting the aorta segment and shrink it) and use those as inputs for Grow from seeds. If the results are good then you can automate all the steps by a little Python scripting.</p>
<p>Only “Gaussian smoothing” method of the Smoothing effect is expected to shrink segments, but all the other methods should generally keep sizes unchanged.</p>
<p>Note that if you re-grow or smooth the segment, it won’t be able to make the segmentation’s resolution any finer. Before you grow from seeds or apply smoothing, you can increase the resolution of the segmentation as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">here</a>.</p>

---

## Post #19 by @sfat (2023-12-18 05:38 UTC)

<p>Thanks a lot !!! Very useful breakdown !!! I will play around with segment editor resolution option first, but I think I’m going to end up going down the shrink and regrow method</p>

---

## Post #20 by @sfat (2023-12-18 05:47 UTC)

<p>silly question … but what’s the best way/tool to shrink for this purpose ?</p>

---

## Post #21 by @lassoan (2023-12-18 05:48 UTC)

<aside class="quote no-group" data-username="sfat" data-post="20" data-topic="15209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sfat/48/66469_2.png" class="avatar"> sfat:</div>
<blockquote>
<p>what’s the best way/tool to shrink for this purpose ?</p>
</blockquote>
</aside>
<p>You can use the Margin effect for shrinking and Logical operators effect for inverting the segment.</p>

---

## Post #22 by @Killmaro (2024-06-30 17:00 UTC)

<p>Hello</p>
<p>Could you specify the type of filter (median, Gaussian, etc.) used for smoothing 3D rendering after segmentation ? This information does not appear in Slicer.</p>
<p>Regards</p>

---
