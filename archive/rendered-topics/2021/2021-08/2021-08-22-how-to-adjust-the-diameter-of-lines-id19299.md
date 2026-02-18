# How to adjust the diameter of lines

**Topic ID**: 19299
**Date**: 2021-08-22
**URL**: https://discourse.slicer.org/t/how-to-adjust-the-diameter-of-lines/19299

---

## Post #1 by @slicer365 (2021-08-22 14:09 UTC)

<p>How to adjust the diameter of these three kinds of lines,</p>
<p>I want to make them thicker<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f89dcebb42351053910eda88f2bdf752696a708.jpeg" data-download-href="/uploads/short-url/6MxOi7qRFZDREm7beRZzWFcuBbq.jpeg?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f89dcebb42351053910eda88f2bdf752696a708_2_402x375.jpeg" alt="捕获" data-base62-sha1="6MxOi7qRFZDREm7beRZzWFcuBbq" width="402" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f89dcebb42351053910eda88f2bdf752696a708_2_402x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2f89dcebb42351053910eda88f2bdf752696a708_2_603x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f89dcebb42351053910eda88f2bdf752696a708.jpeg 2x" data-dominant-color="77767C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">661×616 61.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<img src="https://emoji.discourse-cdn.com/twitter/smiling_face_with_three_hearts.png?v=12" title=":smiling_face_with_three_hearts:" class="emoji only-emoji" alt=":smiling_face_with_three_hearts:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @jamesobutler (2021-08-22 17:46 UTC)

<p>See the following thread which covered this topic</p>
<aside class="quote" data-post="3" data-topic="18932">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slice-intersection-thickness/18932/3">Slice Intersection Thickness</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You need to dig into how to get the slice display nodes, but in most cases this for example will set the red slice intersection thickness to 5 points: 
getNode('vtkMRMLModelDisplayNode1').SetLineWidth(5)
  </blockquote>
</aside>


---
