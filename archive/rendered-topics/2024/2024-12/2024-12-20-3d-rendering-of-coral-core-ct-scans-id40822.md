# 3d rendering of Coral Core CT scans

**Topic ID**: 40822
**Date**: 2024-12-20
**URL**: https://discourse.slicer.org/t/3d-rendering-of-coral-core-ct-scans/40822

---

## Post #1 by @Caleb_Prouty (2024-12-20 20:44 UTC)

<p>Hi, I have a data set of a bunch of .Tiff images from a CT scan of a Coral core. I would like to make a 3d render similar to what can be seen in here: <a href="https://www.usgs.gov/media/images/computed-tomographic-image-animation-a-coral-core" rel="noopener nofollow ugc">Computed tomographic image animation of a coral core </a></p>
<p>So far I’ve managed to load the data in and can view the slices, but no volume<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd284855b434962f405159f4e36a279292d48be1.jpeg" data-download-href="/uploads/short-url/vyrPcXhRDxz8v7aI9XenCtlH95L.jpeg?dl=1" title="Screenshot 2024-12-20 111950" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd284855b434962f405159f4e36a279292d48be1_2_690x388.jpeg" alt="Screenshot 2024-12-20 111950" data-base62-sha1="vyrPcXhRDxz8v7aI9XenCtlH95L" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd284855b434962f405159f4e36a279292d48be1_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd284855b434962f405159f4e36a279292d48be1_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd284855b434962f405159f4e36a279292d48be1_2_1380x776.jpeg 2x" data-dominant-color="7A7A7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-12-20 111950</span><span class="informations">1920×1080 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any help would be appreciated!</p>

---

## Post #2 by @pieper (2024-12-20 21:05 UTC)

<p>Should be very doable.  Did you try dragging the Shift slider?  It may be that the scalar range of your data is very different from what we typically see.  You can look in the Volume Properties section of the Volumes module.  You may need to play around with the lookup tables in the advanced section.  To make an animation like you linked look at the Animator module in SlicerMorph.</p>

---

## Post #3 by @Caleb_Prouty (2024-12-25 22:50 UTC)

<p>Hi, thanks for the response!</p>
<p>Could you elaborate on what “dragging the shift slider” means?</p>
<p>I also unfortunately did not see a “volume properties” section in the volumes module, closest was “volume information”</p>
<p>The last thing I was wondering, is SlicerMorph a separate application to 3D Slicer?</p>
<p>Thanks again for the help, this is the first time I’ve ever used this program</p>

---

## Post #4 by @mau_igna_06 (2024-12-26 00:09 UTC)

<p>Please check these out:</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html" class="inline-onebox" rel="noopener nofollow ugc">Volume rendering — 3D Slicer documentation</a></li>
</ul>
<div class="youtube-onebox lazy-video-container" data-video-id="KvhdOs9L9JA" data-video-title="Getting Started with SlicerMorph in 3D Slicer: A Guide to Landmark-Based Morphological Analysis" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=KvhdOs9L9JA" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/KvhdOs9L9JA/maxresdefault.jpg" title="Getting Started with SlicerMorph in 3D Slicer: A Guide to Landmark-Based Morphological Analysis" width="690" height="388">
  </a>
</div>

<p>HIH</p>

---

## Post #5 by @muratmaga (2024-12-26 04:29 UTC)

<aside class="quote no-group" data-username="Caleb_Prouty" data-post="3" data-topic="40822">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/caleb_prouty/48/78939_2.png" class="avatar"> Caleb_Prouty:</div>
<blockquote>
<p>is SlicerMorph a separate application to 3D Slicer?</p>
</blockquote>
</aside>
<p>SlicerMorph is an extension for 3D Slicer. It makes importing microCT data into 3D Slicer easier, as well as provides functionality to do landmark-based morphometrics analysis.</p>
<p>Official tutorials for SlicerMorph is at <a href="https://github.com/SlicerMorph/SlicerMorph" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerMorph: Extension to import microCT data and conduct 3D morphometrics in Slicer</a>.<br>
You should also get familiar with Slicer’s own documentation, where you can find answers to your question like “what is slider during in volume rendering module”.</p>
<p><a href="https://slicer.readthedocs.io" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io</a></p>

---
