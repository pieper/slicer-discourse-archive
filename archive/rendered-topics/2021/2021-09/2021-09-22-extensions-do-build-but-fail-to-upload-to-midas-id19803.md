---
topic_id: 19803
title: "Extensions Do Build But Fail To Upload To Midas"
date: 2021-09-22
url: https://discourse.slicer.org/t/19803
---

# Extensions do build but fail to upload to midas

**Topic ID**: 19803
**Date**: 2021-09-22
**URL**: https://discourse.slicer.org/t/extensions-do-build-but-fail-to-upload-to-midas/19803

---

## Post #1 by @Alex_Vergara (2021-09-22 08:32 UTC)

<p>Something weird is being happening lately, my extension is succesfully built but not uploaded to midas, see <a href="https://slicer.cdash.org/viewBuildError.php?type=1&amp;buildid=2408172" class="inline-onebox" rel="noopener nofollow ugc">CDash</a></p>
<p>Is this a fake report? Since I can see the extension still available. Perhaps an old version that did not launch any warning to me, but certeinly wrong</p>

---

## Post #2 by @lassoan (2021-09-22 19:14 UTC)

<p>Midas does not exist anymore. To fix the error, you would need to update the server address and get write permission to the new server, but probably what you want is to package without upload.</p>

---

## Post #3 by @jcfr (2021-09-22 22:30 UTC)

<p>Following <a href="https://github.com/Slicer/Slicer/commit/43cc41a6b7e18a347b2d722a087e3ff5ff7d39c6#diff-20a23c67898af08340ce4cbe61157f25b882c52abf33e9814d378dec09fefabb">43cc41a6b</a>, the upload to midas only reports warnings in case of failure. Shortly we will update <code>SlicerExtensionPackageAndUploadTarget.cmake</code> to completely remove midas support.</p>

---

## Post #4 by @Alex_Vergara (2021-09-23 06:31 UTC)

<p>Then how do I shall proceed? Is there something I shall change in my extension?</p>

---

## Post #5 by @Alex_Vergara (2021-09-23 06:36 UTC)

<p>I want to know if this issue affects the package version that is installed inside Slicer or not.</p>

---

## Post #6 by @lassoan (2021-09-23 12:56 UTC)

<p>Normally you just test packaging of your extension locally (and let factory machines build and upload the official packages to the extensions server). Why would you like to upload packages?</p>

---

## Post #7 by @Alex_Vergara (2021-09-23 13:10 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="3" data-topic="19803">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>SlicerExtensionPackageAndUploadTarget.cmake</p>
</blockquote>
</aside>
<p>Apparently this file forces extensions to try to upload the packages to midas, is there a way to disable this behaviour?</p>

---

## Post #8 by @Alex_Vergara (2021-09-23 13:11 UTC)

<p>I won’t. It is just the factory machines that tried this. I don’t know how to tell them to disable this</p>

---

## Post #9 by @lassoan (2021-09-23 13:31 UTC)

<p>Your extension is successfully uploaded to the <a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/614ab807342a877cb3c65229">new extensions server</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca2675a83224895bb2614dbc9937e0cc1bde57ff.png" data-download-href="/uploads/short-url/sQiQB0T2aUEioudnzwGwmT2qxav.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca2675a83224895bb2614dbc9937e0cc1bde57ff_2_690x231.png" alt="image" data-base62-sha1="sQiQB0T2aUEioudnzwGwmT2qxav" width="690" height="231" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca2675a83224895bb2614dbc9937e0cc1bde57ff_2_690x231.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca2675a83224895bb2614dbc9937e0cc1bde57ff_2_1035x346.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca2675a83224895bb2614dbc9937e0cc1bde57ff_2_1380x462.png 2x" data-dominant-color="E1E2E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1578×529 73.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Today the download links work on the <a href="https://slicer.cdash.org/index.php?project=SlicerPreview">dashboard</a>, too (the small yellow boxes are there).</p>
<p>You can ignore any remaining Midas upload warnings/errors - <a class="mention" href="/u/jcfr">@jcfr</a> will take care of them.</p>

---
