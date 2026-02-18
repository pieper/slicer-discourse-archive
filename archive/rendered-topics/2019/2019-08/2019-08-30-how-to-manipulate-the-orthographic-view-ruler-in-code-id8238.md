# How to manipulate the orthographic view ruler in code

**Topic ID**: 8238
**Date**: 2019-08-30
**URL**: https://discourse.slicer.org/t/how-to-manipulate-the-orthographic-view-ruler-in-code/8238

---

## Post #1 by @rat01 (2019-08-30 12:41 UTC)

<p>How can I access this ruler in python? I’m trying to do things such as toggle its visibility and change its color and thickness. I know how to do all of these things from the pin menu, but I’d like to be able to control these with a script.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/149d3c7f2ea3766f15f587c9d0bfb1245ca72754.png" data-download-href="/uploads/short-url/2Wmqs5p2ca9Lea6CbnohR7ZvOII.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/149d3c7f2ea3766f15f587c9d0bfb1245ca72754.png" alt="image" data-base62-sha1="2Wmqs5p2ca9Lea6CbnohR7ZvOII" width="690" height="466" data-dominant-color="A1A1D3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">696×471 12.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2019-08-30 12:59 UTC)

<p>Like most everything in Slicer, this is managed by a MRML node that you access via the scene.  In this case it’s the <a href="https://apidocs.slicer.org/master/classvtkMRMLAbstractViewNode.html" rel="nofollow noopener">view node</a>.  You can get the view node from the threeDView via the layout manager.  Is that enough to get you going?</p>

---

## Post #3 by @rat01 (2019-08-30 14:30 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/star_struck.png?v=9" title=":star_struck:" class="emoji" alt=":star_struck:"> Yes it is. Thanks for the help.</p>

---
