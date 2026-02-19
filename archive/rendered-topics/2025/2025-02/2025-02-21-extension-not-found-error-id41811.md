---
topic_id: 41811
title: "Extension Not Found Error"
date: 2025-02-21
url: https://discourse.slicer.org/t/41811
---

# Extension not found error

**Topic ID**: 41811
**Date**: 2025-02-21
**URL**: https://discourse.slicer.org/t/extension-not-found-error/41811

---

## Post #1 by @muratmaga (2025-02-21 18:36 UTC)

<p>On the latest stable on Linux, I am getting this error for Photogrammetry extension:</p>
<p><code>Download of extension failed, could not find an extension with id = 67b7462ed33fe21b38cc2287</code></p>
<p>Dashboard seems it is as built:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.cdash.org/builds/3697784">
  <header class="source">
      <img src="https://slicer.cdash.org/favicon.ico" class="site-icon" width="32" height="32">

      <a href="https://slicer.cdash.org/builds/3697784" target="_blank" rel="noopener nofollow ugc">slicer.cdash.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.cdash.org/builds/3697784" target="_blank" rel="noopener nofollow ugc">Build Summary</a></h3>

  <p>
            CDash is an open source, web-based software testing server. CDash aggregates, analyzes, and displays the
            results of software testing processes submitted from clients located around the world. CDash is a part of a
           ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> any idea why this might be the case.</p>

---

## Post #2 by @jamesobutler (2025-02-21 23:29 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="41811">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Download of extension failed, could not find an extension with id</p>
</blockquote>
</aside>
<p>I’m not sure. Do other extensions on the Linux platform download successfully? Are you on a corporate system with actively running ZScaler?</p>

---

## Post #3 by @muratmaga (2025-02-22 00:48 UTC)

<p>No, I am trying on the JS2, no restrictions. Preview doesn’t seem to be affected. Weird.</p>

---

## Post #4 by @muratmaga (2025-02-22 03:46 UTC)

<p>And yes, other extensions on Linux stable are available and install fine.</p>

---

## Post #5 by @muratmaga (2025-02-23 00:28 UTC)

<p>Whatever it was, it seems resolved today.</p>

---

## Post #6 by @jamesobutler (2025-02-23 00:50 UTC)

<p>The oddness and inconsistency is likely the existing known instability of the factory Linux build machine.</p>
<aside class="quote quote-modified" data-post="3" data-topic="41357">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/no-extensions-are-being-built-for-linux-stable-5-8/41357/3">No extensions are being built for Linux stable (5.8)</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Reviewing CDash, we can confirm that yesterday extensions were built for both: 

Stable:

CDash: <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2025-02-02&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex" rel="noopener nofollow ugc">https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2025-02-02&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex</a>
Extensions: <a href="https://extensions.slicer.org/catalog/All/33216/linux" rel="noopener nofollow ugc">https://extensions.slicer.org/catalog/All/33216/linux</a>


Preview (aka Nightly):

CDash: <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-02-02&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex" rel="noopener nofollow ugc">https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-02-02&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex</a>
Extensions: <a href="https://extensions.slicer.org/catalog/All/33455/linux" rel="noopener nofollow ugc">https://e…</a>
  </blockquote>
</aside>


---
