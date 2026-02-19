---
topic_id: 44832
title: "Binary Is Missing From The Extension Package"
date: 2025-10-20
url: https://discourse.slicer.org/t/44832
---

# Binary is missing from the extension package

**Topic ID**: 44832
**Date**: 2025-10-20
**URL**: https://discourse.slicer.org/t/binary-is-missing-from-the-extension-package/44832

---

## Post #1 by @fedorov (2025-10-20 21:41 UTC)

<p>We have a situation where one (and only one!) of the binaries that are build as part of the dcmqi extension is missing, only on Mac. For example, see this build: <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-10-17&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=dcmqi" class="inline-onebox">SlicerPreview</a> . There are no build errors, but <code>segimage2itkimage</code> CLI binary is not in the package. I don’t recall seeing this before. This worked fine, and there were no changes to the source code in many months. I asked <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> to help with this, but maybe someone seen similar issues? Corresponding issue is here: <a href="https://github.com/QIICR/dcmqi/issues/519" class="inline-onebox">`segimage2itkimage` binary is missing in Slicer extension package · Issue #519 · QIICR/dcmqi · GitHub</a>.</p>

---

## Post #2 by @DeepaKrishnaswamy (2025-10-21 16:32 UTC)

<p>Hi,</p>
<p>This turned out to be a problem with mistakenly identifying <code>segimage2itkimage</code> as a cybersecurity threat.</p>

---

## Post #3 by @jcfr (2025-10-21 18:42 UTC)

<aside class="quote no-group" data-username="DeepaKrishnaswamy" data-post="2" data-topic="44832">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/deepakrishnaswamy/48/8913_2.png" class="avatar"> DeepaKrishnaswamy:</div>
<blockquote>
<p>This turned out to be a problem with mistakenly identifying <code>segimage2itkimage</code> as a cybersecurity threat.</p>
</blockquote>
</aside>
<p>Well done identifying the <em>root</em> cause <img src="https://emoji.discourse-cdn.com/twitter/100.png?v=14" title=":100:" class="emoji" alt=":100:" loading="lazy" width="20" height="20"></p>
<p>After analyzing the executable through <code>virustotal</code>, it is likely a false positive. See <a href="https://github.com/QIICR/dcmqi/issues/519#issuecomment-3428763957">here</a> for details.</p>

---
