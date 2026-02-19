---
topic_id: 16302
title: "Video Recording Of Segmentation 3D Rendering"
date: 2021-03-02
url: https://discourse.slicer.org/t/16302
---

# Video recording of segmentation / 3D rendering

**Topic ID**: 16302
**Date**: 2021-03-02
**URL**: https://discourse.slicer.org/t/video-recording-of-segmentation-3d-rendering/16302

---

## Post #1 by @mohammed_alshakhas (2021-03-02 05:47 UTC)

<p>i would love if instead of only taking screen shot , that id be able to video record in swirling and rotation .</p>
<p>i do that with screen recording using quick time , having that integrated would be great</p>

---

## Post #2 by @muratmaga (2021-03-02 06:05 UTC)

<p>You can do that with the screen capture module or with <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/Animator">Animator (if you install SlicerMorph extension)</a>.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="oGtvTOhIFtA" data-video-title="SlicerAnimator" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=oGtvTOhIFtA" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/oGtvTOhIFtA/maxresdefault.jpg" title="SlicerAnimator" width="" height="">
  </a>
</div>


---

## Post #3 by @mohammed_alshakhas (2021-03-02 08:08 UTC)

<p>Do you have a good tutorial for animator , it looks very exciting</p>

---

## Post #4 by @muratmaga (2021-03-02 15:25 UTC)

<p>If you scroll down in the help page above, you will see the tutorial link.</p>

---

## Post #5 by @rbumm (2021-03-03 18:19 UTC)

<p>Edited: If you are looking for something “inbuilt” - I usually use Slicers “Screen Capture” function - produces excellent videos</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/710adcd1cf160d7eefe2ac45fc0305c5f036e917.png" data-download-href="/uploads/short-url/g81e53RPGopHAtxQ2VA4B386OJV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/710adcd1cf160d7eefe2ac45fc0305c5f036e917.png" alt="image" data-base62-sha1="g81e53RPGopHAtxQ2VA4B386OJV" width="455" height="500" data-dominant-color="F0F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">522×573 20.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @muratmaga (2021-03-03 19:14 UTC)

<aside class="quote no-group quote-modified" data-username="rbumm" data-post="5" data-topic="16302">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Slicers “screen recorder” function</p>
</blockquote>
</aside>
<p>Minor correction. Module’s name is <code>Screen Capture</code></p>

---

## Post #7 by @mohammed_alshakhas (2021-03-11 07:19 UTC)

<p>is it possible to use segments instead of volume property for the animator ?</p>

---

## Post #8 by @muratmaga (2021-03-11 16:40 UTC)

<p>You can use segments, however you might as well use the core <code>Screen Capture</code> module since Volume Rendering or the  ROI actions will not applicable to segments.</p>

---

## Post #9 by @mohammed_alshakhas (2021-03-12 05:58 UTC)

<p>It would be great if the effect is applicable to segments instead of only volume .</p>

---

## Post #10 by @lassoan (2021-03-14 17:13 UTC)

<p>What do you mean? What animations would you like to create?</p>
<p>Note that unlike volume rendering, segmentation can be exported to OBJ file that can be animated in very sophisticated ways in Blender or other 3D modeling and animation software.</p>
<p>Another option is to adjust Animator module to also modify segmentation display properties. It is just a Python scripted module, so all you need is a text editor to modify it (you can find path to the script in Module finder - Ctrl + F).</p>

---
