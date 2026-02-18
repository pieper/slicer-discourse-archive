# Landmarking in virtual reality?

**Topic ID**: 36593
**Date**: 2024-06-04
**URL**: https://discourse.slicer.org/t/landmarking-in-virtual-reality/36593

---

## Post #1 by @Dave_Matthews (2024-06-04 18:33 UTC)

<p>Hi,</p>
<p>I’m wondering whether there are plans to add further tools to the virtual reality module? Specifically, are there any plans to add landmarking capabilities to VR?</p>
<p>Thanks!<br>
Dave</p>

---

## Post #2 by @muratmaga (2024-06-04 18:44 UTC)

<p>We (SlicerMorph) are not involved with virtual reality aspects of Slicer. So take it a with a grain of salt, I am not sure what the plans are.</p>
<p>Having said that, personally I am not convinced the virtual reality interfaces (not just in Slicer, pretty much everywhere) are sufficiently precise to do a good job for anatomical landmarking, particularly for quantitative morphology. I am having a hard time seeing mouse and keyboard (or digitization pads, pencils) being replaced for that purpose.</p>
<p>VR/AR is great of manipulation (e.g., sculpting a fossil reconstruction from fragments, possibly segmentation) and definitely for teaching and simulations. I am just not convinced it is the right tool for landmarking.</p>

---

## Post #3 by @LeidyMoraV (2024-06-04 19:01 UTC)

<p>I think some work in that direction (VR/AR) has been already done <a href="https://www.youtube.com/watch?v=KdUdFQ44h3U" rel="noopener nofollow ugc">Augmented reality guidance for burr hole placement using HoloLens - YouTube</a></p>

---

## Post #4 by @Dave_Matthews (2024-06-04 20:49 UTC)

<p>Thanks for your responses Murat and Leidy!</p>
<p>I see how it would be hard to match the precision of other methods. I thought that if it was possible, it would be fun to try it out and see how well it worked. I also thought that on complex 3D models (fish heads for both hard tissue and soft tissue contrast enhanced) the VR might make it substantially easier to place landmarks on internal bones since you have depth as an axis that can be controlled with the input device.</p>
<p>You mentioned segmentation as a use of VR. Do you know if that is currently possible in Slicer VR?</p>

---

## Post #5 by @muratmaga (2024-06-04 21:01 UTC)

<p>I do not know the latest state of virtual reality in Slicer. There is definitely some recent improvements. You can go to this page and see what’s possible currently. <a href="https://github.com/KitwareMedical/SlicerVirtualReality" class="inline-onebox">GitHub - KitwareMedical/SlicerVirtualReality: A Slicer extension that enables user to interact with a Slicer scene using virtual reality.</a></p>
<p>This is an example of interacting with segmented structures (but not necessarily segmenting them).</p>
<div class="youtube-onebox lazy-video-container" data-video-id="VzVjvnKuBAE" data-video-title="3D Slicer reconstruction of fragmented bones in virtual reality" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=VzVjvnKuBAE" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/VzVjvnKuBAE/maxresdefault.jpg" title="3D Slicer reconstruction of fragmented bones in virtual reality" width="690" height="388">
  </a>
</div>


---

## Post #6 by @lassoan (2024-06-05 12:22 UTC)

<p>Since you can work at arbitrary scale in virtual reality, position objects directly (not with clunky mouse gestures) and the controllers are very accurate, I would expect that you can place landmarks with higher accuracy and less effort than with mouse and keyboard and a 2D screen.</p>
<p>However, markup placement in AR/VR in Slicer is not yet supported. We need to inplement snapping or laser-pointer like projection to allow placing points on surfaces. PerkLab is not currently working on this but Kitware or Ebatinca might.</p>

---

## Post #7 by @muratmaga (2024-06-05 15:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="36593">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would expect that you can place landmarks with higher accuracy and less effort than with mouse and keyboard and a 2D screen</p>
</blockquote>
</aside>
<p>It is possible. But it is all about the interface. I am happy to try and shown to be wrong, when it is available. In other VR applications, even with a laser-pointer like projection, I am finding localizing to the exact spot a lot more challenging with a controller that has 6 degrees of freedom in my shaky hand compared to a mouse moving on a flat surface.</p>

---
