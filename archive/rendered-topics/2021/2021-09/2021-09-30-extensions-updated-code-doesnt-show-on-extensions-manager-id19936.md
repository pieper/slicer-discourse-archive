---
topic_id: 19936
title: "Extensions Updated Code Doesnt Show On Extensions Manager"
date: 2021-09-30
url: https://discourse.slicer.org/t/19936
---

# Extension's updated code doesn't show on Extensions Manager

**Topic ID**: 19936
**Date**: 2021-09-30
**URL**: https://discourse.slicer.org/t/extensions-updated-code-doesnt-show-on-extensions-manager/19936

---

## Post #1 by @mau_igna_06 (2021-09-30 13:56 UTC)

<p>Hi. I updated the BoneReconstructionPlanner extension main branch (i.e. <a href="https://github.com/Slicer/ExtensionsIndex/blob/4.11/BoneReconstructionPlanner.s4ext" rel="noopener nofollow ugc">extensionsIndex’s observed branch</a>) on last Tuesday as you can see <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/commits/main" rel="noopener nofollow ugc">here</a> but I downloaded today BoneReconstructionPlanner on Slicer Stable release and the extension hasn’t updated, actually last update appears to be <a href="https://slicer-packages.kitware.com/#item/60ae2856ae4540bf6a89dde2" rel="noopener nofollow ugc">June 30th</a>.</p>
<p>Why did the extension not rebuild? Shouldn’t it have rebuild yesterday or today?</p>

---

## Post #2 by @lassoan (2021-09-30 15:50 UTC)

<p>The extension is built from the latest git revision for both the Slicer Stable Release and the Slicer Preview Release:</p>
<ul>
<li>
<a href="https://slicer.cdash.org/index.php?project=Slicer4&amp;date=2021-09-30&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=bonereconstruction">Stable dashboard</a>:  latest git hash is eb64f2d or f775c6f → up-to-date</li>
<li>
<a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2021-09-30&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=bonereconstruction">Preview dashboard</a>:  latest git hash is eb64f2d or f775c6f → up-to-date</li>
</ul>
<p>However, these builds are not uploaded to the Extensions Server:</p>
<ul>
<li><strong><a href="https://slicer-packages.kitware.com/#search/results?query=29738_BoneReconstructionPlanner&amp;mode=prefix">Stable packages</a>: latest git hash is a7f80c0 → outdated!</strong></li>
<li>
<a href="https://slicer-packages.kitware.com/#search/results?query=30275_BoneReconstructionPlanner&amp;mode=prefix">Preview packages</a>: latest git hash is eb64f2d or f775c6f → up-to-date</li>
</ul>
<p><a class="mention" href="/u/jcfr">@jcfr</a> is this a known issue?</p>

---

## Post #3 by @jcfr (2021-09-30 16:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="19936">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>is this a known issue?</p>
</blockquote>
</aside>
<p>This should now be fixed:</p>
<ul>
<li>Relevant build-system updates have been backported to the <a href="https://github.com/Slicer/Slicer/commits/v4.11">v4.11</a> branch</li>
<li>Local checkout associated with the latest stable release on the factories have been manually updated.</li>
</ul>
<p>For reference, while latest updates have been backported to the <code>v4.11</code> branch, they are currently under review for integration in master in <a href="https://github.com/Slicer/Slicer/pull/5922">PR-5922</a></p>

---
