# How to change the background with a picture in 3d window?

**Topic ID**: 1628
**Date**: 2017-12-10
**URL**: https://discourse.slicer.org/t/how-to-change-the-background-with-a-picture-in-3d-window/1628

---

## Post #1 by @timeanddoctor (2017-12-10 14:19 UTC)

<p>Operating system:win 7<br>
Slicer version:4.8<br>
Expected behavior:<br>
Actual behavior:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89d4d459b187b6b56cb92d4f27ede18dafa886f8.jpeg" data-download-href="/uploads/short-url/jFjoHYUmVsQfMALUv3sJA6qss8o.jpg?dl=1" title="2017-12-10_215129" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/89d4d459b187b6b56cb92d4f27ede18dafa886f8_2_612x500.jpg" alt="2017-12-10_215129" data-base62-sha1="jFjoHYUmVsQfMALUv3sJA6qss8o" width="612" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/89d4d459b187b6b56cb92d4f27ede18dafa886f8_2_612x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89d4d459b187b6b56cb92d4f27ede18dafa886f8.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89d4d459b187b6b56cb92d4f27ede18dafa886f8.jpeg 2x" data-dominant-color="494745"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2017-12-10_215129</span><span class="informations">795×649 55.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2017-12-10 14:59 UTC)

<p>You can load an image and show it in a slice plane. For easy positioning of the image, install SlicerIGT extension and use Volume Reslicile Driver module (apply a transform to the image and use the image as driver for a slice view in transverse mode).</p>

---

## Post #3 by @doc-xie (2017-12-11 08:54 UTC)

<p>About the background of the 3D view,how to change the color or replace the background with a picture?</p>

---

## Post #4 by @lassoan (2017-12-11 16:46 UTC)

<aside class="quote no-group" data-username="doc-xie" data-post="3" data-topic="1628" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/c77e96/48.png" class="avatar"> doc-xie:</div>
<blockquote>
<p>About the background of the 3D view,how to change the color or replace the background with a picture?</p>
</blockquote>
</aside>
<p>See my answers above.</p>
<p>If you are thinking about changing the background color so that you can remove that color and replace it with an image, then there is a much simpler way: you can save the view content with transparent background. See “Capture 3D view into PNG file with transparent background” example in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture">script repository</a>.</p>

---

## Post #5 by @doc-xie (2017-12-12 13:40 UTC)

<p>Thanks a lot!<br>
Maybe I have not show my thought definitely. The color of the background in the 3D view include light blue,white and black,if I want to change the color to red or repalce it with another picture  arbitriraly,what can i do without any familiarity with Python .<br>
Best wishes!<br>
doc-xie</p>

---

## Post #6 by @lassoan (2017-12-12 15:28 UTC)

<p>You can change the background to red using this code snippet:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_3D_view_background_color" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_3D_view_background_color</a></p>

---

## Post #7 by @doc-xie (2017-12-14 07:44 UTC)

<p>Thanks，I got it like this!<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7d6d254c3cb5fb4b41fadeafaa4d5e56d81d044.jpeg" data-download-href="/uploads/short-url/qejD4IE3fzrL2q4XCgtOARtu3oE.jpg?dl=1" title="无标题" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7d6d254c3cb5fb4b41fadeafaa4d5e56d81d044_2_690x373.jpg" alt="无标题" data-base62-sha1="qejD4IE3fzrL2q4XCgtOARtu3oE" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7d6d254c3cb5fb4b41fadeafaa4d5e56d81d044_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7d6d254c3cb5fb4b41fadeafaa4d5e56d81d044_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7d6d254c3cb5fb4b41fadeafaa4d5e56d81d044.jpeg 2x" data-dominant-color="D47C7D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题</span><span class="informations">1340×726 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @timeanddoctor (2020-02-06 10:47 UTC)

<p>I changed the background to Red, however,it return when click the 3d tool . Can I keep the changing?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92390342611fbc0598a6ad49b610a9bf3949bc58.gif" data-download-href="/uploads/short-url/kRxRjsb28RGB5aaXPY5VfOXGLy0.gif?dl=1" title="d" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92390342611fbc0598a6ad49b610a9bf3949bc58_2_690x489.gif" alt="d" data-base62-sha1="kRxRjsb28RGB5aaXPY5VfOXGLy0" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/92390342611fbc0598a6ad49b610a9bf3949bc58_2_690x489.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92390342611fbc0598a6ad49b610a9bf3949bc58.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92390342611fbc0598a6ad49b610a9bf3949bc58.gif 2x" data-dominant-color="C2191A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">d</span><span class="informations">763×541 27.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @lassoan (2020-02-06 16:54 UTC)

<p>The example in the script repository was only intended for temporary change of the background color. For changing it persistently, use SetBackgroundColor methods of the view node - see the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_3D_view_background_color">updated example in script repository</a>.</p>

---
