# Importing a 3DSlicer body model into Unreal game engine

**Topic ID**: 9183
**Date**: 2019-11-17
**URL**: https://discourse.slicer.org/t/importing-a-3dslicer-body-model-into-unreal-game-engine/9183

---

## Post #1 by @jtle (2019-11-17 22:50 UTC)

<p>Is it possible to create a model of a body with all the underlying organs, etc and then import the model into Unreal game engine for further interaction between user and the simulation? And how would the importation be done? This is meant to be done in Virtual Reality, so ideally the user will wear the headset, see a body and be able to interact with it, and the interactions and consequences are programmed in Unreal. I know there’s an extension SlicerVR, but do not think it’s sophisticated enough to handle too much interaction between the model and the user?</p>

---

## Post #2 by @pieper (2019-11-18 13:18 UTC)

<p>Hi -</p>
<p>You can export models in various formats for use with other systems like Unity.  Lately there’s some work with <a href="https://discourse.slicer.org/t/transferring-models-using-gltf-2-0/7064">glTF</a>, but other formats should work too.</p>
<aside class="quote no-group" data-username="jtle" data-post="1" data-topic="9183">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/4491bb/48.png" class="avatar"> jtle:</div>
<blockquote>
<p>I know there’s an extension SlicerVR, but do not think it’s sophisticated enough to handle too much interaction between the model and the user?</p>
</blockquote>
</aside>
<p>A lot depends on what you are trying to accomplish.  SlicerVR allows you to directly interact with Slicer functionality so things like segmentation, transforms, and volume rendering are all native.  Plus Slicer is fully open source so it’s possible to program anything you need.  But of course it’s newer and has a smaller developer base so it’s not as polished as something like Unity.</p>

---

## Post #3 by @lassoan (2019-11-18 14:37 UTC)

<p>In general, it makes sense to use SlicerVirtualReality if you implement a medical image viewing/analysis application, while game engine is more suitable if you implement a game-like application.</p>
<p>See these slides from this <a href="http://perk.cs.queensu.ca/contents/enhance-medical-software-applications-immersive-virtual-reality-experience">recent SlicerVirtualReality presentation</a>:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f84b591ac09796977c9064a5e726654b87addffe.png" data-download-href="/uploads/short-url/zqvQoM5tzeB14KwfzrbdJ7xODZY.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f84b591ac09796977c9064a5e726654b87addffe_2_690x386.png" alt="image" data-base62-sha1="zqvQoM5tzeB14KwfzrbdJ7xODZY" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f84b591ac09796977c9064a5e726654b87addffe_2_690x386.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f84b591ac09796977c9064a5e726654b87addffe_2_1035x579.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f84b591ac09796977c9064a5e726654b87addffe_2_1380x772.png 2x" data-dominant-color="F6F0ED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2254×1264 300 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8fcbd93da736dc8c190f8d42542b838946a72aa.png" data-download-href="/uploads/short-url/xf6gziGFm52SCB5YcFMzNbIFRsS.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8fcbd93da736dc8c190f8d42542b838946a72aa_2_690x386.png" alt="image" data-base62-sha1="xf6gziGFm52SCB5YcFMzNbIFRsS" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8fcbd93da736dc8c190f8d42542b838946a72aa_2_690x386.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8fcbd93da736dc8c190f8d42542b838946a72aa_2_1035x579.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e8fcbd93da736dc8c190f8d42542b838946a72aa_2_1380x772.png 2x" data-dominant-color="EDECEC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2246×1259 329 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
