# Rendering Performance with Large number of slab slices

**Topic ID**: 8351
**Date**: 2019-09-09
**URL**: https://discourse.slicer.org/t/rendering-performance-with-large-number-of-slab-slices/8351

---

## Post #1 by @burnhamd (2019-09-09 22:01 UTC)

<p>I have a volume with 512x512,313 dimensions.</p>
<p>I have enabled reslice driver for tracking of a needle.  The reslice rendering performance is quite good when I am navigating on only once slice at a time.  However when I set the slab thickness to around 75 and have a spacing fraction of 5 I see a huge slowdown to about 1fps.  Is this normal?  I am seeing that my computer is being CPU limited.  I have a i7 with 1.9ghz speed.</p>

---

## Post #2 by @pieper (2019-09-09 22:17 UTC)

<p>Yes, I would say that sounds normal.  You might want to change to using GPU volume rendering instead (unfortunately it’s a very different pipeline so you’d probably need to change the way you do things).</p>

---

## Post #3 by @lassoan (2019-09-09 23:44 UTC)

<p>Yes, this performance is expected if you use CPU for raycasting.</p>
<p>See instructions in this post how to configure the GPU volume renderer to create projection image: <a href="https://discourse.slicer.org/t/is-it-possible-to-change-a-cbct-to-2d/7617" class="inline-onebox">Is it possible to change a cbct to 2d</a></p>
<p>If you want to limit the slab to a certain thickness then set the volume rendering clipping ROI’s Z size to the desired thickness and then apply the SlicerToRAS transform of the slice view to this ROI.</p>

---

## Post #4 by @burnhamd (2019-09-10 16:19 UTC)

<p>Thanks for the responses.  I used the 3d view and followed the steps as Iassoan linked with some tweaks for the scan I have.  It does seem to be much more responsive.</p>
<p>To set the view I set the camera focal point to the center of my volume and then I offset the camera position to a position above the focal point to get a Coronal image of the scan.  This seems to work ok.  Although the FOV isnt currently applicable to an volume since I set the distance manually.</p>
<p>Im a little confused about the last suggestion</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="8351">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you want to limit the slab to a certain thickness then set the volume rendering clipping ROI’s Z size to the desired thickness and then apply the SlicerToRAS transform of the slice view to this ROI.</p>
</blockquote>
</aside>
<p>I’m not using a slice view.  Are you suggesting that I can place a volume render in a slice view window?</p>

---

## Post #5 by @lassoan (2019-09-10 17:09 UTC)

<aside class="quote no-group" data-username="burnhamd" data-post="4" data-topic="8351">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/5fc32e/48.png" class="avatar"> burnhamd:</div>
<blockquote>
<p>I’m not using a slice view. Are you suggesting that I can place a volume render in a slice view window?</p>
</blockquote>
</aside>
<p>If the axes of the thick slab is aligned with anatomical axes then you don’t need a transform, you can just set the center and size of the ROI to define the slab.</p>
<p>If you want to show an oblique slab then you need to create a transform to position/orient your ROI node. If you use slice views, you can set this transform by copying the position/orientation of an oblique slice view.</p>

---

## Post #6 by @burnhamd (2019-09-10 18:21 UTC)

<p>Sorry for being dense <img src="https://emoji.discourse-cdn.com/twitter/laughing.png?v=9" title=":laughing:" class="emoji" alt=":laughing:"></p>
<p>I understand I need to get a transform if I want a arbitrary slice angle/oblique view.  What I dont understand is how to get a volume render to display in a slice view.  Is that what you are suggesting?</p>

---

## Post #7 by @lassoan (2019-09-11 01:01 UTC)

<aside class="quote no-group" data-username="burnhamd" data-post="6" data-topic="8351">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/5fc32e/48.png" class="avatar"> burnhamd:</div>
<blockquote>
<p>What I dont understand is how to get a volume render to display in a slice view. Is that what you are suggesting?</p>
</blockquote>
</aside>
<p>I’m not suggesting to display a volume rendered image in a slice view. If you need that then you need to implement it yourself (grab the image from the 3D view, put it into a single-slice volume, and show that volume in a slice view).</p>

---
