# Slicer Virtual Reality extension

**Topic ID**: 15752
**Date**: 2021-01-31
**URL**: https://discourse.slicer.org/t/slicer-virtual-reality-extension/15752

---

## Post #1 by @muratmaga (2021-01-31 16:52 UTC)

<p>I finally had my hands on a oculus rift system and tried it with Slicer. I have couple questions.</p>
<ol>
<li>
<p>I used the MRhead as a Volume Rendering and interactions with it was very fluid. But I can’t seem to do anything else beyond moving/rotating/scaling or clipping through slices. Is that normal? E.g. can I do landmarking, or adjust volume rendering settings through the headset?</p>
</li>
<li>
<p>I enabled 3D rendering from a thresholded segment of MRHead. It was very slow to interact, but more importantly stuttered/flickered (I don’t know how to describe)</p>
</li>
</ol>
<p>My knowledge of VR is systems is non-existent to minimal, so guidance would be helpful. I am using the Windows preview from 1/20 and the GPU is RTX Titan.</p>

---

## Post #2 by @lassoan (2021-01-31 20:31 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="15752">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I used the MRhead as a Volume Rendering and interactions with it was very fluid. But I can’t seem to do anything else beyond moving/rotating/scaling or clipping through slices. Is that normal? E.g. can I do landmarking, or adjust volume rendering settings through the headset?</p>
</blockquote>
</aside>
<p>Yes, it is not obvious just how much you can achieve in virtual reality, because we cannot yet display regular GUI widgets (buttons, sliders, etc.) so you need to activate features in the desktop GUI. We’ll be able to show widgets after we upgrade to VTK9. Until then you can use position of any object to set any parameters anywhere with a short Python script (you add an observer to the object’s parent transform, and in the callback function update the chosen parameter, for example volume rendering transfer function; it takes just a few lines of Python code).</p>
<p>When we implemented markups placement in virtual reality, we realized that we needed to add support for multiple active markup points (desktop user can hover over a markup control point, while virtual reality user can hove over/grab two other control points), so we implemented this feature, but we ran out of time finishing the landmarking. I think a new student will start to work with <a class="mention" href="/u/cpinter">@cpinter</a> tomorrow who will work on finishing this (and maybe on the immersive widget display, too).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="15752">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I enabled 3D rendering from a thresholded segment of MRHead. It was very slow to interact, but more importantly stuttered/flickered</p>
</blockquote>
</aside>
<p>For some reason, segmentations are very slow to move (we haven’t debugged this, as we did not need it). To resolve this, right-click on the segmentation to export it to model and hide the segmentation node.</p>

---
