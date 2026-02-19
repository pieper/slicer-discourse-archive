---
topic_id: 20568
title: "Unable To Find Specific Revision Of 3Dslicer"
date: 2021-11-10
url: https://discourse.slicer.org/t/20568
---

# Unable to find specific revision of 3DSlicer

**Topic ID**: 20568
**Date**: 2021-11-10
**URL**: https://discourse.slicer.org/t/unable-to-find-specific-revision-of-3dslicer/20568

---

## Post #1 by @DeepaKrishnaswamy (2021-11-10 16:18 UTC)

<p>Hi,</p>
<p>I am trying to use the module mpReview ( <a href="https://github.com/SlicerProstate/mpReview/wiki/Documentation" class="inline-onebox" rel="noopener nofollow ugc">Documentation · SlicerProstate/mpReview Wiki · GitHub</a>) which requires the use of these 3DSlicer versions as listed in the link:</p>
<pre><code>macOS: http://download.slicer.org/download?os=macosx&amp;stability=any&amp;revision=28560
Linux: http://download.slicer.org/download?os=linux&amp;stability=any&amp;revision=28560
Windows: http://download.slicer.org/download?os=win&amp;stability=any&amp;revision=28560
</code></pre>
<p>It seems that no matching revisions are found.</p>
<p>Thank you,</p>
<p>Deepa</p>

---

## Post #2 by @lassoan (2021-11-10 16:46 UTC)

<p>Slicer Preview Releases, such as Slicer-4.11.x (rev 28560) are not archived indefinitely.</p>
<p>You can try using Slicer 4.11.20210226 (rev 29738) or Slicer 4.10.2 (rev 28257) instead. They can be downloaded from <a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/5f4474d0e1d8c75dfc705482">here</a>.</p>
<p>Note that most (maybe all) features are available in the latest Slicer Preview Release, without installing any extensions, by using Data module to browse images and show/hide them and Segment Editor to segment them.</p>
<p>mpReview extension was developed to make the workflow more convenient for clinicians: a person responsible for data management set up the scenes that clinicians could process it more easily. There are discussions about reviving the extension in some form - you can contact <a class="mention" href="/u/fedorov">@fedorov</a> for more details.</p>

---

## Post #3 by @fedorov (2021-11-10 16:51 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Deepa is working with me, and started looking into mpReview. <a href="https://github.com/SlicerProstate/mpReview/wiki/Documentation">The user instructions</a> we had for the users relied on a specific version of Slicer (to provide consistency and stability, and not being able to keep updating the module to track Slicer updates). I was hoping Deepa can use that “known to work” release to get started, but looks like she will also need to explore more recent versions as well.</p>

---

## Post #4 by @lassoan (2021-11-10 16:55 UTC)

<p>Sounds good. Probably you can use the latest Slicer Stable Release with the most recent version of your extension.</p>

---

## Post #5 by @fedorov (2021-11-10 17:03 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20568">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer Preview Releases, such as Slicer-4.11.x (rev 28560) are not archived indefinitely.</p>
</blockquote>
</aside>
<p>Since this came up - do we know for how long a given preview version is archived?</p>

---

## Post #6 by @lassoan (2021-11-10 17:07 UTC)

<p>The goal is to preserve preview releases until a new stable comes out, but a cleanup may have to be started if the extensions server gets full. The extensions server got replaced around September, preview releases before that might have been discarded.</p>
<p>You can always check out a Slicer version and build it and the extensions if you want to check one specific version.</p>

---
