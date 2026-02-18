# Segmentation Fast Marching effect does not work

**Topic ID**: 21647
**Date**: 2022-01-26
**URL**: https://discourse.slicer.org/t/segmentation-fast-marching-effect-does-not-work/21647

---

## Post #1 by @javipeina (2022-01-26 23:56 UTC)

<p>Operating system: Mac OS 10.15.7<br>
Slicer version:4.11.20210226 r29738 / 7a593c8<br>
Expected behavior: Segmentation effect fast marching grow a region in contrasted aorta<br>
Actual behavior: does nothing at all<br>
I have done everything I’m suppose to do (add new segment, select it, paint in some spots inside the contrasted aorta, 1% maximum volume, iizialyse). Nothing happens, it remains the same or even erase the painted spots. Please help me, I don’t know how to do it. I have tried even this Thresold effect, but it’s the same, t doesn’t even seems to be a precess inside the computer when I clic Inizialise button. Thanks.</p>

---

## Post #2 by @lassoan (2022-01-27 01:11 UTC)

<p>Can you paint in the aorta using the Paint effect? If not then make sure that:</p>
<ul>
<li>segment and the segmentation are visible in the current view</li>
<li>“Masking” settings are correct (you can set them to defaults: editable area → everywhere, editable intensity range → turned off,  modify other segments → overwrite all)</li>
<li>segmentation bounds are chosen correctly (see <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">here</a>)</li>
</ul>
<p>If none of these helps then you could share the scene file with us (save your scene as a .mrb file, upload to dropbox/onedrive/etc. and post the link here) and we can investigate. Make sure no patient information is included.</p>

---

## Post #3 by @rbumm (2022-01-27 10:47 UTC)

<p>Maybe this link helps  - including how to segment the aorta in 30 s:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="yi07mjr3JeU" data-video-title="New vessel branch extraction module for 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=yi07mjr3JeU" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/yi07mjr3JeU/maxresdefault.jpg" title="New vessel branch extraction module for 3D Slicer" width="" height="">
  </a>
</div>

<p>If you get this working, “Fast Marching” should be possible too.</p>

---

## Post #4 by @susk (2022-02-03 12:13 UTC)

<p>I have the exact same problem. Operating system Windows 11 Pro, Slicer version 4.11.20210226 r29738 / 7a593c8</p>
<p>I am trying to follow the 3D Slicer segmentation recipe ‘Aorta segmentation (fast, using Fast marching)’, so I loaded the sample data CTACardio and followed the steps in the recipe by creating a new segment, then painting a few strokes inside the aorta. Then I select the Fast Marching effect, set the Maximum Volume to 1%, and press Initialize. For a few seconds ‘Running Fast Marching’ is visible in the lower left corner of the window. After that, the few strokes I painted in the aorta have slightly changed position and size/shape, but the Segment Volume slider stays greyed out, so I cannot change the volume of the segmentation as should be possible according to the recipe.</p>

---

## Post #5 by @chir.set (2022-02-03 16:55 UTC)

<p>Have you a compelling need for ‘Fast marching’ ?</p>
<p>If not, you can try ‘Local threshold’ and ‘Flood filling’. Experiment with all options, segmenting an aorta is usually a simple task.</p>

---

## Post #6 by @mikebind (2022-02-03 21:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="21647">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<ul>
<li>segment and the segmentation are visible in the current view</li>
<li>“Masking” settings are correct (you can set them to defaults: editable area → everywhere, editable intensity range → turned off, modify other segments → overwrite all)</li>
<li>segmentation bounds are chosen correctly (see <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">here </a>)</li>
</ul>
</blockquote>
</aside>
<p>These are the most common confusions. Make sure that painting works first as <a class="mention" href="/u/lassoan">@lassoan</a> suggests.</p>

---

## Post #7 by @susk (2022-02-07 13:23 UTC)

<p>Thank you for your replies!<br>
<a class="mention" href="/u/chir.set">@chir.set</a>, I do not need to use fast marching per se, I was just getting familiar with the different ways to segment vessels with 3D slicer and following the tutorials/recipes. <a class="mention" href="/u/mikebind">@mikebind</a>, I can paint in the aorta and all the settings are as <a class="mention" href="/u/lassoan">@lassoan</a> suggests.</p>
<p>The problem seems to be solved by installing the preview release of Slicer, 4.13.0. Now the Fast Marching algorithm works as described in the recipe with the sample data set CTACardio.</p>

---
