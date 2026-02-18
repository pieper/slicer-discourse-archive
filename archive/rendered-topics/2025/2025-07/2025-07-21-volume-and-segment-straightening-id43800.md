# Volume and segment straightening

**Topic ID**: 43800
**Date**: 2025-07-21
**URL**: https://discourse.slicer.org/t/volume-and-segment-straightening/43800

---

## Post #1 by @sulli419 (2025-07-21 19:51 UTC)

<p>Hello, I have a segmented volume of the spine, similar to the video below. I want to get the center points and straighten all the segments and the volume in one fell swoop. What is the best way to do this?</p>
<p>I see a workflow in the 2nd video that uses “extract centerline” but I cannot figure out how to get this extension. I see from old notes that it might be in VMTK but I no longer see this as a downloadable extension in the Slicer “install extensions” menu (I have the latest version). Perhaps there is a newer and better way to go about this?</p>
<p>I could see one problem in straightening multiple spinal segments is that it would introduce overlap. Any methods/approaches that would deal with this might be ideal.</p>
<p>Thanks!</p>
<p>spine segments</p>
<p><img src="https://img.youtube.com/vi/wMMi0QIrCvc/maxresdefault.jpg" alt="" title="Semi-automatic vertebra segmentation on CT" role="presentation" width="690" height="388"></p>
<p><a href="https://www.youtube.com/watch?v=wMMi0QIrCvc" rel="noopener nofollow ugc">Semi-automatic vertebra segmentation on CT</a></p>
<p>vessel straightening</p>
<p><img src="https://img.youtube.com/vi/yi07mjr3JeU/maxresdefault.jpg" alt="" title="New vessel branch extraction module for 3D Slicer" role="presentation" width="690" height="388"></p>
<p><a href="https://www.youtube.com/watch?v=yi07mjr3JeU" rel="noopener nofollow ugc">New vessel branch extraction module for 3D Slicer</a></p>

---

## Post #2 by @chir.set (2025-07-21 20:09 UTC)

<aside class="quote no-group" data-username="sulli419" data-post="1" data-topic="43800">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>I no longer see this as a downloadable extension in the Slicer “install extensions” menu (I have the latest version).</p>
</blockquote>
</aside>
<p>If you are using SlicerPreview, the SlicerVMTK extension is broken since months. You may use SlicerVMTK with SlicerStable.</p>

---

## Post #3 by @sulli419 (2025-07-21 23:35 UTC)

<p>Thanks.  I installed the most recent stable version of slicer and indeed found VMTK.  Some of the menu items look different from the video I shared (earlier version).  For example, where is curved planar reformat?</p>
<p>This is what my menu looks like:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9eba5feec0d2e0e7ffbcc9d3cbd70e6fc948662.png" data-download-href="/uploads/short-url/zETLoWYpeoY48KQHuh9uKaTKF22.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9eba5feec0d2e0e7ffbcc9d3cbd70e6fc948662.png" alt="image" data-base62-sha1="zETLoWYpeoY48KQHuh9uKaTKF22" width="604" height="480"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">604×480 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @chir.set (2025-07-22 07:08 UTC)

<aside class="quote no-group" data-username="sulli419" data-post="3" data-topic="43800">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sulli419/48/78859_2.png" class="avatar"> sulli419:</div>
<blockquote>
<p>where is curved planar reformat?</p>
</blockquote>
</aside>
<p>It’s in the <code>Sandbox</code> extension.</p>

---

## Post #5 by @sulli419 (2025-07-22 19:51 UTC)

<p>great that worked.  thanks.  I’m now able to very crudely straighten a volume following the video I posted.  Although the centerpoints do not seem to truly be the center of the segment I used for creating it, and I do not see a way to straighten my segmentations, in addition to the volume (2nd part of my initial question (fyi this was not attempted in the video)).</p>

---
