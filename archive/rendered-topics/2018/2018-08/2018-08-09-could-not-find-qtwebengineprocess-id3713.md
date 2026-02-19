---
topic_id: 3713
title: "Could Not Find Qtwebengineprocess"
date: 2018-08-09
url: https://discourse.slicer.org/t/3713
---

# Could not find QtWebEngineProcess

**Topic ID**: 3713
**Date**: 2018-08-09
**URL**: https://discourse.slicer.org/t/could-not-find-qtwebengineprocess/3713

---

## Post #1 by @darekdev (2018-08-09 07:33 UTC)

<p>I would like to build Slicer with Qt5 and VTK9 and 10 minutes ago the compile process was completed but I can’t run Extension Manager because of error:  Could not find QtWebEngineProcess.<br>
But that file exist in:<br>
/home/software/medical/slicer4.9/Slicer-Build-Support/qt/5.11.0/gcc_64/libexec/QtWebEngineProcess</p>
<p>I only do this to check if the SlicerJupyter module works. Doens’t work in my current build (4.9 from May, Qt4, VTK 7) after installation can’t find JupyterKernel module. This is very important to me, because at my institute we conduct research that perfectly fits into Slicer. And I need compiled version, because I write modules and slicelets.</p>
<p>Regards</p>

---

## Post #2 by @lassoan (2018-08-09 08:26 UTC)

<p>If you build Slicer then you have to build all the extensions that you need, too, so for now you can ignore the extension manager error.</p>
<p>SlicerJupyter extension nightly build fails with some uuid library issue (<a href="http://slicer.cdash.org/viewBuildError.php?buildid=1344742">http://slicer.cdash.org/viewBuildError.php?buildid=1344742</a>), maybe you could give it a try to fix it.</p>

---

## Post #3 by @darekdev (2018-08-09 09:30 UTC)

<p>OK thank you. Then I need to compile modules and extensions for instance SlicerJupyter and manually add it to Slicer, yes? Is QtWebEngineProcess only need to Extension Manager?</p>

---

## Post #4 by @lassoan (2018-08-09 11:03 UTC)

<p>Yes, exactly.</p>
<p>You can find extension source code repository URLs in the ExtensionsIndex: <a href="https://github.com/Slicer/ExtensionsIndex">https://github.com/Slicer/ExtensionsIndex</a></p>

---

## Post #5 by @darekdev (2018-08-13 10:27 UTC)

<p>Works like a charm!<br>
Ubuntu 16.04 on Docker.</p>
<p>I have installed two libraries:<br>
sudo apt-get install libicu-dev<br>
sudo apt-get install uuid-dev</p>
<p>I know that is a way that I should add this libraries to compile time only but I have created environment on Docker.</p>
<p>It’s amazing. We will save a lot of time on scientific work.<br>
Thank you Kitware!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b96f7bae2a0b829aa5682aaffb92cda4bfe401a4.jpeg" data-download-href="/uploads/short-url/qsrbnueADqgZBEVDuuSSNB4eNTu.jpeg?dl=1" title="SlicerJupyter" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b96f7bae2a0b829aa5682aaffb92cda4bfe401a4_2_690x388.jpeg" alt="SlicerJupyter" data-base62-sha1="qsrbnueADqgZBEVDuuSSNB4eNTu" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b96f7bae2a0b829aa5682aaffb92cda4bfe401a4_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b96f7bae2a0b829aa5682aaffb92cda4bfe401a4_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b96f7bae2a0b829aa5682aaffb92cda4bfe401a4_2_1380x776.jpeg 2x" data-dominant-color="B9B8B6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerJupyter</span><span class="informations">1920×1080 269 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Edit: autocompletion/hints doesn’t work here. I don’t know if it works for someone?</p>

---

## Post #6 by @lassoan (2018-08-18 07:52 UTC)

<p>A post was split to a new topic: <a href="/t/error-running-pip-install/3822">Error running pip install</a></p>

---

## Post #7 by @lassoan (2018-08-18 07:50 UTC)

<aside class="quote no-group" data-username="darekdev" data-post="5" data-topic="3713">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/e5b9ba/48.png" class="avatar"> darekdev:</div>
<blockquote>
<p>Edit: autocompletion/hints doesn’t work here. I don’t know if it works for someone?</p>
</blockquote>
</aside>
<p>We are working out some remaining issues with auto-compleiton. It should be available within a few days.</p>

---
