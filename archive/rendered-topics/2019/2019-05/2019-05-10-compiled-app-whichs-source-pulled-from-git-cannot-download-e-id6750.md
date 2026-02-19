---
topic_id: 6750
title: "Compiled App Whichs Source Pulled From Git Cannot Download E"
date: 2019-05-10
url: https://discourse.slicer.org/t/6750
---

# Compiled App whichs source pulled from git cannot download extension due to reversion not match.

**Topic ID**: 6750
**Date**: 2019-05-10
**URL**: https://discourse.slicer.org/t/compiled-app-whichs-source-pulled-from-git-cannot-download-extension-due-to-reversion-not-match/6750

---

## Post #1 by @Cyberobot (2019-05-10 06:50 UTC)

<p>Problem report for Slicer 4.11.0-2019-05-01 win-amd64: [please describe expected and actual behavior]<br>
I compiled the Slicer reversion of “28202” which was pulled from github, and it’s reversion became “aae6a8c”, so that I can’t download extension from Extensions Manager online. The message from Extensions Manager says as below:<br>
“No extensions found for win:64-bit, revision: ‘aae6a8c’. Please try a different combination”<br>
After that I installed a SlicerVR extension, and it works well.<br>
Then I modified the string “aae6a8c” to “28202” from file “vtkSlicerVersionConfigure.h” which was generated in project “SlicerConfigureVersionHeader”. As a result, I can download extension successfully while I can’t installed a SlicerVR extension(either compiled or downloaded) , there was something wrong with it as following.<br>
[FATAL][Qt] 09.05.2019 21:33:33 [] (unknown:0) - ASSERT failure in QList::at: “index out of range”, file D:\Qt5.9.2\5.9.2\msvc2017_64\include\QtCore/qlist.h, line 541<br>
Looking forward to fixing this bug as soon!</p>

---

## Post #2 by @jcfr (2019-05-10 06:54 UTC)

<aside class="quote no-group" data-username="Cyberobot" data-post="1" data-topic="6750">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/b2d939/48.png" class="avatar"> Cyberobot:</div>
<blockquote>
<p>No extensions found for win:64-bit, revision: ‘aae6a8c’.</p>
</blockquote>
</aside>
<p>Two approaches:</p>
<ul>
<li>
<p>To make the build system grabs the expected SVN revision, you have to use git-svn as described here. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#CHECKOUT_slicer_source_files" class="inline-onebox">Documentation/Nightly/Developers/Build Instructions - Slicer Wiki</a></p>
</li>
<li>
<p>Or configure Slicer setting option <code>Slicer_WC_REVISION</code> to the value <code>28202</code></p>
</li>
</ul>

---

## Post #3 by @lassoan (2019-05-10 12:48 UTC)

<aside class="quote no-group quote-modified" data-username="Cyberobot" data-post="1" data-topic="6750">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/b2d939/48.png" class="avatar"> Cyberobot:</div>
<blockquote>
<p>[FATAL][Qt] 09.05.2019 21:33:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ASSERT failure in QList::at: “index out of range”, file D:\Qt5.9.2\5.9.2\msvc2017_64\include\QtCore/qlist.h, line 541</p>
</blockquote>
</aside>
<p>This indicates potential ABI incompatibility. In general, if you build Slicer, you must also build all extensions yourself. This is easy to do, as extensions require the exact same build environment as Slicer. You can bundle all extension you need into your custom-built Slicer and disable the extension manager.</p>

---
