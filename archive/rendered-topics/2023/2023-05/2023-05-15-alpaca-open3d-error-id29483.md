# ALPACA open3d error

**Topic ID**: 29483
**Date**: 2023-05-15
**URL**: https://discourse.slicer.org/t/alpaca-open3d-error/29483

---

## Post #1 by @seanchoi0519 (2023-05-15 23:57 UTC)

<p>Hello,</p>
<p>Is ALPACA no longer compatible with open3d v 0.10.0? only 0.14.1 + onwards?<br>
Is there any way I can still make it work with v0.10.0?</p>
<p>I noticed the registration capability slowed down significantly since the update.<br>
Thanks,</p>

---

## Post #2 by @muratmaga (2023-05-16 00:33 UTC)

<p>Unfortunately open3d never worked consistently well for us, causing many different problems especially in cross-platform. We have reimplemented the functionality in open3d as part of the ITK, and a new alpaca module called alpaca_preview is available in latest SlicerMorph. See this thread on how to enable it.</p>
<aside class="quote quote-modified" data-post="3" data-topic="28906">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/increasing-alpaca-non-rigid-alignment/28906/3">Increasing ALPACA Non-Rigid Alignment</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    How many points are you left with during the pointcloud conversion? (ALPACA should report the number of points). If it is too few, that might be the problem. 

Try changing both alpha and beta values together. Increasing CPD iterations will probably be useful as well. 
Finally, the current ALPACA module will be deprecated soon, and we will switch to an ITK based implementation (instead of open3d we are currently using). Make sure you start using, it is already available with SlicerMorph (it is …
  </blockquote>
</aside>

<p>Going forward, this ITK based ALPACA will be default and we will stop using open3d. Our test how shown that ITK based implementation is in fact gives us slightly better results.</p>
<p>I suggest you start using the ITK-ALPACA (alpaca_preview) as well.</p>

---
