---
topic_id: 41463
title: "Slicerjupyter Not Found In Slicer 5 7 And 5 8"
date: 2025-02-03
url: https://discourse.slicer.org/t/41463
---

# SlicerJupyter Not Found in Slicer 5.7 and 5.8

**Topic ID**: 41463
**Date**: 2025-02-03
**URL**: https://discourse.slicer.org/t/slicerjupyter-not-found-in-slicer-5-7-and-5-8/41463

---

## Post #1 by @park (2025-02-03 14:11 UTC)

<p>Hello,</p>
<p>I noticed that <strong>SlicerJupyter</strong> is not available in both Slicer 5.7 and 5.8. Is it only compatible with Slicer 5.6? Additionally, I would like to know if there are any plans to update and support it in future versions.</p>
<p>Thank you in advance for your insights.</p>

---

## Post #2 by @muratmaga (2025-02-03 20:16 UTC)

<p>What OS are you running?<br>
For slicer stable,<br>
Cdash shows a build error on Windows platform:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.cdash.org/viewBuildError.php?buildid=3677176">
  <header class="source">
      <img src="https://slicer.cdash.org/favicon.ico" class="site-icon" width="32" height="32">

      <a href="https://slicer.cdash.org/viewBuildError.php?buildid=3677176" target="_blank" rel="noopener nofollow ugc">slicer.cdash.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.cdash.org/viewBuildError.php?buildid=3677176" target="_blank" rel="noopener nofollow ugc">CDash</a></h3>

  <p>
            CDash is an open source, web-based software testing server. CDash aggregates, analyzes, and displays the
            results of software testing processes submitted from clients located around the world. CDash is a part of a
           ...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Mac version seems OK:<br>
<a href="https://slicer.cdash.org/sites/1282?project=13&amp;currenttime=1738551600" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.cdash.org/sites/1282?project=13&amp;currenttime=1738551600</a></p>
<p>There has been some issues with Linux extensions (they don’t seem to be built).</p>

---

## Post #3 by @Matteboo (2025-02-10 15:15 UTC)

<p>Hello,</p>
<p>I have the same issue on windows 11. I can’t install SlicerJupyter on 5.8, but it is working fine on 5.6.2</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9198cf03ee05999edfdad196ce0cecb7b3c95a87.png" alt="image" data-base62-sha1="kM0CHBfqPP287uHGx11eZz2IMh9" width="398" height="86"></p>

---

## Post #4 by @Matteboo (2025-02-18 10:50 UTC)

<p>Hello, SlicerJupyter is not available in the version 5.8. Is there a timeline for when the extension will be updated to be compatible with the latest slicer version ?</p>

---

## Post #5 by @jcfr (2025-02-18 15:24 UTC)

<p>Thanks for the report <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>Looking at CDash associated with both the Stable (see <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2025-02-16&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=jupyter">here</a>) and the Preview build (see <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-02-18&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=jupyter">here</a>), the extension is packaged and available on Linux and macOS but not on Windows.</p>
<p>For example, corresponding Windows error can be reviewed <a href="https://slicer.cdash.org/viewBuildError.php?buildid=3693507">here</a></p>
<p>A dedicated issue has been created: <a href="https://github.com/Slicer/SlicerJupyter/issues/78">https://github.com/Slicer/SlicerJupyter/issues/78</a></p>
<p><a class="mention" href="/u/matteboo">@Matteboo</a>  Let us know if you would like to either work on the issue or if you would have resources to help support its resolution <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---
