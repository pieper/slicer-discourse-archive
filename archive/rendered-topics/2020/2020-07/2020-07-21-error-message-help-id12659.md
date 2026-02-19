---
topic_id: 12659
title: "Error Message Help"
date: 2020-07-21
url: https://discourse.slicer.org/t/12659
---

# Error message,help!

**Topic ID**: 12659
**Date**: 2020-07-21
**URL**: https://discourse.slicer.org/t/error-message-help/12659

---

## Post #1 by @wwx992881 (2020-07-21 13:01 UTC)

<p>Hi!<br>
when I try to Extract centerline,and I get two error message as follow?what happened?what shoule I do?Thanks!!!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c503d5275fc897eec2f8bb374624a435c1ca181.png" alt="微信图片_20200721210031" data-base62-sha1="miOoFboT5PCmR0dio2wSrJweToB" width="480" height="303"></p>

---

## Post #2 by @pieper (2020-07-21 17:35 UTC)

<p>That message means you ran out of memory.  If you search the forum there are many related threads with suggestions, such as this one:</p>
<aside class="quote quote-modified" data-post="1" data-topic="11981">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/centerline-computation-failed/11981">Centerline computation failed</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello Everyone, 
I’ve been trying to compute centerlines for <a href="https://github.com/DeepaMahm/misc/blob/master/Segmentation4.seg.nrrd" rel="nofollow noopener">this</a> geometry using VMTK extension. 
However, I couldn’t successfully obtain centerlines. Even the networkExtraction failed when I tried 
to use the stl file of the same geometry 

reader = vmtkscripts.vmtkSurfaceReader() 
reader.InputFileName = ‘input.stl’ 
reader.Execute() 
# network extraction
networkExtraction = vmtkscripts.vmtkNetworkExtraction()
networkExtraction.Surface = reader.Surface
networkExtraction.Execute()


Could someon…
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2020-07-23 02:02 UTC)

<p>You can also try the latest VMTK in latest Slicer Preview Release, as we’ve made lots of improvements recently, including reducing memory usage.</p>

---
