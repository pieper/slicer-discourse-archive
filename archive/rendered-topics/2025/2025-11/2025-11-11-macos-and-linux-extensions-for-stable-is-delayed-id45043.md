# MacOS and Linux extensions for stable is delayed?

**Topic ID**: 45043
**Date**: 2025-11-11
**URL**: https://discourse.slicer.org/t/macos-and-linux-extensions-for-stable-is-delayed/45043

---

## Post #1 by @muratmaga (2025-11-11 18:29 UTC)

<p>Hi folks,</p>
<p>Current extension catalog for stable for MacOS and Linux is not updated with build from today. Windows is up to date. Cdash does not show any MacOS builds.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.cdash.org/index.php?project=SlicerStable">
  <header class="source">
      <img src="https://slicer.cdash.org/favicon.ico" class="site-icon" alt="" width="32" height="32">

      <a href="https://slicer.cdash.org/index.php?project=SlicerStable" target="_blank" rel="noopener nofollow ugc">slicer.cdash.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.cdash.org/index.php?project=SlicerStable" target="_blank" rel="noopener nofollow ugc">SlicerStable</a></h3>

  <p>
            CDash is an open source, web-based software testing server. CDash aggregates, analyzes, and displays the
            results of software testing processes submitted from clients located around the world. CDash is a part of a
           ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Are they still being build?</p>

---

## Post #2 by @Sam_Horvath (2025-11-11 18:31 UTC)

<p>We are in the process of fixing some things with the extensions, will get the linux/macOS stable build going again soon.</p>

---

## Post #3 by @Sam_Horvath (2025-11-11 18:40 UTC)

<p>Linux is fixed and coming up now</p>

---

## Post #4 by @Sam_Horvath (2025-11-11 18:45 UTC)

<p>macOS extensions coming up now</p>

---

## Post #5 by @muratmaga (2025-11-12 16:56 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>
<p>Any idea why SlicerMorph MacOS extension not showing on the stable dashboard?</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.cdash.org/index.php?project=SlicerStable&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=slicermorph">
  <header class="source">
      <img src="https://slicer.cdash.org/favicon.ico" class="site-icon" alt="" width="32" height="32">

      <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=slicermorph" target="_blank" rel="noopener nofollow ugc">slicer.cdash.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=slicermorph" target="_blank" rel="noopener nofollow ugc">SlicerStable</a></h3>

  <p>
            CDash is an open source, web-based software testing server. CDash aggregates, analyzes, and displays the
            results of software testing processes submitted from clients located around the world. CDash is a part of a
           ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @Sam_Horvath (2025-11-12 17:24 UTC)

<p>We are having some connectivity issues with the macOS machine, and it looks like it rebooted overnight.  I an rerunning the stable extensions index</p>

---

## Post #7 by @Sam_Horvath (2025-11-12 19:15 UTC)

<p>SlicerMorph should now be available</p>

---

## Post #8 by @ruffsl (2025-11-17 22:36 UTC)

<aside class="quote no-group" data-username="Sam_Horvath" data-post="3" data-topic="45043" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<p>Linux is fixed and coming up now</p>
</blockquote>
</aside>
<p>Looking at the build failure for <code>SlicerIGT</code> extension for Linux:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.cdash.org/builds/3996957">
  <header class="source">
      <img src="https://slicer.cdash.org/favicon.ico" class="site-icon" alt="" width="32" height="32">

      <a href="https://slicer.cdash.org/builds/3996957" target="_blank" rel="noopener nofollow ugc">slicer.cdash.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.cdash.org/builds/3996957" target="_blank" rel="noopener nofollow ugc">SlicerStable - Build Summary</a></h3>

  <p>
            CDash is an open source, web-based software testing server. CDash aggregates, analyzes, and displays the
            results of software testing processes submitted from clients located around the world. CDash is a part of a
           ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Was the Qt setup/install for docker CI pipeline updated again as well?</p>
<pre><code class="lang-auto">/.../SlicerIGT/FiducialRegistrationWizard/Widgets/qSlicerTransformPreviewWidget.h:29:10: fatal error: ui_qSlicerTransformPreviewWidget.h: No such file or directory
</code></pre>

---
