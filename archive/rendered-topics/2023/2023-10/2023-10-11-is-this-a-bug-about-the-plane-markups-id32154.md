# Is this a bug about the Plane Markups？

**Topic ID**: 32154
**Date**: 2023-10-11
**URL**: https://discourse.slicer.org/t/is-this-a-bug-about-the-plane-markups/32154

---

## Post #1 by @slicer365 (2023-10-11 09:29 UTC)

<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8165f9a1fa50b903b681fad9ac3cffa04c7d77b5.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8165f9a1fa50b903b681fad9ac3cffa04c7d77b5.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/8165f9a1fa50b903b681fad9ac3cffa04c7d77b5.mp4</a>
    </video>
  </div><br>
I put a plane in the 2D view, but the center of the plane does not adjust as the plane changes.<br>
This should be the same as ROI, which can be adjusted at any time.<br>
How to modify the code?<p></p>

---

## Post #2 by @muratmaga (2023-10-11 16:30 UTC)

<p>I am guessing you are using the default point and normal plane creation mode. If you want to interact with the planes in a manner similar to ROI, you probably want to use the <code>three points</code> option.</p>

---

## Post #3 by @Fokatu (2023-12-09 18:38 UTC)

<p>I have the same question.<br>
<a class="mention" href="/u/muratmaga">@muratmaga</a> , how to use <code>three points</code> option to create plane.</p>

---

## Post #4 by @muratmaga (2023-12-09 22:15 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html</a><br>
See the plane markup</p>

---
