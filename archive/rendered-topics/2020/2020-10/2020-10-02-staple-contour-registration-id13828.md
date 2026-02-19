---
topic_id: 13828
title: "Staple Contour Registration"
date: 2020-10-02
url: https://discourse.slicer.org/t/13828
---

# STAPLE contour registration

**Topic ID**: 13828
**Date**: 2020-10-02
**URL**: https://discourse.slicer.org/t/staple-contour-registration/13828

---

## Post #1 by @peterg1t (2020-10-02 20:12 UTC)

<p>Hi all,<br>
I’m not an experience Slicer user so maybe this has been asked before. I was wondering if something like Majority Vote or Simultaneous truth and Performance Level Estimation (STAPLE) is included in any of the packages available to the community. My problem is that I have several contours (or estimates of the same structure) and I want to obtain a single contour based on the optimal combination of the input contours. Any tips and hints are appreciated.<br>
Have a great day,</p>
<p>Pedro Martinez</p>

---

## Post #2 by @pieper (2020-10-02 21:00 UTC)

<p>It should be included in SimpleFilters, but I’m not seeing it in the current builds.  Maybe <a class="mention" href="/u/blowekamp">@blowekamp</a> knows?</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://www.slicer.org/w/img_auth.php/6/64/Favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/SimpleFilters" target="_blank" rel="noopener">slicer.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/SimpleFilters" target="_blank" rel="noopener">Documentation/4.10/Modules/SimpleFilters - Slicer Wiki</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @blowekamp (2020-10-05 14:00 UTC)

<p>This filter was removed from this module with in <a href="https://github.com/SimpleITK/SlicerSimpleFilters/commit/77eeae334bef866318ed923e786d4af508b994ac" rel="noopener nofollow ugc">this</a> commit. The linked commit message only indicate that the filter had an issue with an “Int” widget. However, this filter operates on “N” images and I don’t believe a GUI element was ever created to work with an arbitrary number of inputs. Also, I thought this might be an import algorithm with additional output statistics that might justify someone writing a custom module just for this filter.</p>

---

## Post #4 by @lassoan (2020-10-05 14:12 UTC)

<aside class="quote no-group" data-username="blowekamp" data-post="3" data-topic="13828">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/blowekamp/48/1386_2.png" class="avatar"> blowekamp:</div>
<blockquote>
<p>I don’t believe a GUI element was ever created to work with an arbitrary number of inputs</p>
</blockquote>
</aside>
<p>We could now use a subject hierarchy tree widget - the user would choose a folder that contains all the input images.</p>

---
