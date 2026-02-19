---
topic_id: 3109
title: "Problem With Segment Editor Paint"
date: 2018-06-07
url: https://discourse.slicer.org/t/3109
---

# Problem with segment editor paint

**Topic ID**: 3109
**Date**: 2018-06-07
**URL**: https://discourse.slicer.org/t/problem-with-segment-editor-paint/3109

---

## Post #1 by @Ash_Alarfaj (2018-06-07 12:00 UTC)

<p>Operating system:Windows<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a506de6ab74bfd650d5104a7e54f2a6e8d67c03.jpeg" data-download-href="/uploads/short-url/fauVIbG0l9lb5l7LgSEG4PZ7URl.jpg?dl=1" title="paint%20problem%20disable" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a506de6ab74bfd650d5104a7e54f2a6e8d67c03_2_690x387.jpg" alt="paint%20problem%20disable" data-base62-sha1="fauVIbG0l9lb5l7LgSEG4PZ7URl" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a506de6ab74bfd650d5104a7e54f2a6e8d67c03_2_690x387.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a506de6ab74bfd650d5104a7e54f2a6e8d67c03_2_1035x580.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a506de6ab74bfd650d5104a7e54f2a6e8d67c03.jpeg 2x" data-dominant-color="939397"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">paint%20problem%20disable</span><span class="informations">1366×768 302 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Slicer version:4.9<br>
Expected behavior: apply paint<br>
Actual behavior: doesn’t work!</p>
<p>Hi could please help me, I start segmentation by applying the threshold, then correct it by paint and eras, but now, paint doesn’t work with me, in the middle of my segmentation I went to volume rendering and I can’t undo the volume rendering so does it affect the paint?</p>

---

## Post #2 by @lassoan (2018-06-07 13:04 UTC)

<p>Volume rendering should not affect Segment editor.</p>
<p>Do you see any errors or warnings in the logs? (red icon in the lower-right corner)</p>
<p>Make sure you disabled all special options:</p>
<ul>
<li>Color smudge: off</li>
<li>Editable area: Everywhere</li>
<li>Editable intensity range: off</li>
<li>Overwrite other segments: All segments</li>
</ul>
<p>If you still have problems, try these:</p>
<ul>
<li>Save the scene, restart Slicer, and load the scene and see if you can paint.</li>
<li>If still does not work, restart Slicer and load just the saved segmentation and volume and see if you can paint.</li>
<li>Install the latest nightly build and try the two steps above.</li>
</ul>
<p>Let us know which solution worked.</p>

---

## Post #3 by @szhang (2021-02-18 19:19 UTC)

<p>Unfortunately it happens in the stable version 4.11.20200930 as well… In the middle of segment editing, the brush just cannot paint anymore…<br>
I tried to follow your instructions and restarted, but still cannot make the paint to brush in the segment editor. It didn’t work in nightly build of 20200818 either.<br>
Here are two “Warning” messages in “Log messages”<br>
QLayout::addChildLayout: layout “” already has a parent<br>
ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1</p>
<p>Greatly appreciate your help!</p>

---

## Post #4 by @lassoan (2021-02-18 19:21 UTC)

<p>Can you share the scene that demonstrates this issue (upload it somewhere and post the link here)?</p>

---

## Post #5 by @szhang (2021-02-18 19:28 UTC)

<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/s/k7tqphvvou0jvgm/2021-02-05-Scene.mrml?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/s/k7tqphvvou0jvgm/2021-02-05-Scene.mrml?dl=0" target="_blank" rel="noopener nofollow ugc">2021-02-05-Scene.mrml</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<p>
Would this work?</p>

---

## Post #6 by @lassoan (2021-02-18 19:31 UTC)

<p>Please save the scene as a bundle (.mrb) so that the actual data files are included as well.</p>

---

## Post #7 by @szhang (2021-02-18 20:29 UTC)

<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/s/1qs0d0powtk7grg/2021-02-05-Scene.mrb?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/s/1qs0d0powtk7grg/2021-02-05-Scene.mrb?dl=0" target="_blank" rel="noopener nofollow ugc">2021-02-05-Scene.mrb</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<p>
I see, please take a look at this one. Thank you.</p>

---

## Post #8 by @lassoan (2021-02-18 21:31 UTC)

<p>All I had to do to display segmentations was to go to Data module and click on the eye icon of the segmentation node.</p>
<p>However, I’ve noticed that the segmentation was shifted down by about 10cm. I’m not sure how this offset could have occurred (maybe there was a transform applied on the master volume earlier?), but I removed it by editing the segmentation header file so that its geometry matches exactly the CT’s geometry. You can download the updated scene from <a href="https://1drv.ms/u/s!Arm_AFxB9yqHxYcA91v9yZbA1681Kg?e=r4Yog1">here</a>.</p>

---

## Post #9 by @szhang (2021-02-18 22:28 UTC)

<p>Thank you, <a class="mention" href="/u/lassoan">@lassoan</a> !<br>
Now I noticed the shift, but when I was editing previous two segments they both looked fine on the master volume, until the 3rd one that I could not paint anymore…<br>
I experienced “paint brush stop working” before as well, and it seems other people had similar issue…<br>
Perhaps it was due to transformation drop-off while using segment editor?</p>

---

## Post #10 by @lassoan (2021-02-18 23:49 UTC)

<p>It is hard to tell now what caused the shift. I think we fixed all the reported errors but if you can reproduce either shifting or paint strokes not appearing with latest stable or preview release then let us know.</p>

---

## Post #11 by @Fullcalf42 (2023-05-26 18:46 UTC)

<p>Was this resolved for you?</p>
<p>I am having the same issue yesterday and today. When I try to apply paint in a segment it doesn’t leave a mark. I saved my scene as .mrb but cannot upload it here.<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e231c1b039874c31695ba70c0820f1edae61a17d.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e231c1b039874c31695ba70c0820f1edae61a17d.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e231c1b039874c31695ba70c0820f1edae61a17d.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #12 by @lassoan (2023-05-28 00:30 UTC)

<p>It’s great if you can provide a scene that reproduces the unexpected behavior. You can upload the mrb file anywhere (dropbox, onedrive, google drive, etc.) and post the link here.</p>

---

## Post #13 by @Ash_Alarfaj (2023-05-28 08:38 UTC)

<p>Hello<br>
I did not have any issues currently, I did not asked any questions from long time.<br>
Thanks</p>

---

## Post #14 by @Marcin_Wczysla (2024-04-26 21:00 UTC)

<p>Hello, I am very new to 3D slicer,  I began learning with the tools paint and thresholding, everything worked fine and then it stopped. When I try to paint it does not remain a trace, the boxes editable areas: everywhere, editable intensity range: not ticked, modify other segments: overwrite all,</p>
<p>same happens with thresholding… please help how I can solve this</p>

---

## Post #15 by @muratmaga (2024-04-27 00:18 UTC)

<p>Please start from scratch and try again. Chances are either you have change editable area settings and masking, or trying to segment something different than the master volume you have.</p>
<p>I encourage you to look this tutorial in detail if you are new to Slicer: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/Segmentation" class="inline-onebox">Tutorials/Segmentation at main · SlicerMorph/Tutorials · GitHub</a></p>

---

## Post #16 by @lassoan (2024-04-28 12:03 UTC)

<p>It would be useful to know why the Segment Editor does not work as expected. Do you see any errors or warnings in the application log? Do you have multiple segmentations in the scene, are you editing the correct one? If you could join or weekly meeting on Tuesday and show it on your computer then we can guide you in how to make it work.</p>

---

## Post #17 by @MedPhys2004 (2024-07-05 17:02 UTC)

<p>This helped me, thank you!</p>

---
