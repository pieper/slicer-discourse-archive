---
topic_id: 18367
title: "3Dview Model Animation Fade In Fade Out"
date: 2021-06-28
url: https://discourse.slicer.org/t/18367
---

# 3DView Model Animation (Fade-in, Fade-out)

**Topic ID**: 18367
**Date**: 2021-06-28
**URL**: https://discourse.slicer.org/t/3dview-model-animation-fade-in-fade-out/18367

---

## Post #1 by @seanchoi0519 (2021-06-28 07:07 UTC)

<p>I have 2 models that are aligned. I would like to visually show them using an animation that fades-in the source model, while simultaneously fading out the target-model, say within a 1-second timeframe, then do vice-versa. This way, the difference between the 2 models can be readily visualized.</p>
<p>How can I achieve this programatically?</p>
<p>I know that I can alter the opacity using the following piece of code:<br>
model1.GetDisplayNode().SetOpacity(0)<br>
model2.GetDisplayNode().SetOpacity(1)</p>
<p>but I would like to animate the fade-in and fade-out process within a specified timeframe for a specified duration.</p>

---

## Post #2 by @pieper (2021-06-28 12:16 UTC)

<p>You can set up a little animation loop using QTimer, something like <a href="https://github.com/Slicer/LandmarkRegistration/blob/master/RegistrationLib/Visualization.py#L146-L161">this</a>.</p>

---

## Post #3 by @lassoan (2021-06-28 13:08 UTC)

<p>It would be great if you could post here a video of the result that you get.</p>
<p>Usually we compare models in slice views (showing slice intersections with different colors) and/or by coloring the surfaces by distance (computed by ModelToModelDistance extension).</p>

---

## Post #4 by @seanchoi0519 (2021-06-28 13:10 UTC)

<p>Yes, will do Prof Andras. I think the colour map is great - however because it is a 2D representation it may be limited in its visual representation. I thought the fade-in and fade-out would be good to show the visualization in 3D. I will post the video in a moment.</p>

---

## Post #5 by @seanchoi0519 (2021-06-28 13:14 UTC)

<p>Video here (wireframe representation). Let me know what you guys think.</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1Yvmh4EAfU23K5nSycF7xJM7Kvp14TuF3/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1Yvmh4EAfU23K5nSycF7xJM7Kvp14TuF3/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
    
<div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://lh3.googleusercontent.com/vf6PT72kEHx9tGM0GH5pALHwojS8l-RwRKelbevUTacq9loa-PN5sDFQ4cQRKBXNxl0=w1200-h630-p" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://drive.google.com/file/d/1Yvmh4EAfU23K5nSycF7xJM7Kvp14TuF3/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">screen_recording.mov (video)</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Any way I can slow down the fade-in and fade-out? I’m happy with everything else.</p>

---

## Post #6 by @lassoan (2021-06-28 13:56 UTC)

<p>You can change the timer interval and/or the opacity change step size to make the fading slower/faster.</p>

---
