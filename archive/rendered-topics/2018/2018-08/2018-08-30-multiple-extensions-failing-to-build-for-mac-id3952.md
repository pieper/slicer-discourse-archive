---
topic_id: 3952
title: "Multiple Extensions Failing To Build For Mac"
date: 2018-08-30
url: https://discourse.slicer.org/t/3952
---

# Multiple extensions failing to build for Mac

**Topic ID**: 3952
**Date**: 2018-08-30
**URL**: https://discourse.slicer.org/t/multiple-extensions-failing-to-build-for-mac/3952

---

## Post #1 by @mschumaker (2018-08-30 15:23 UTC)

<p>I’ve noticed that there are a few extensions on the CDash page for SlicerPreview that fail to build on Mac, and only on Mac. I’m wondering if these problems are related.</p>
<p>The extensions that CDash shows are not building for Mac are:</p>
<ul>
<li>
<p><a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerVirtualReality" rel="nofollow noopener">SlicerVirtualReality</a></p>
</li>
<li>
<p><a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerVMTK" rel="nofollow noopener">SlicerVMTK</a></p>
</li>
<li>
<p><a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerElastix" rel="nofollow noopener">SlicerElastix</a></p>
</li>
</ul>

---

## Post #2 by @lassoan (2018-08-30 16:22 UTC)

<p>SlicerVirtualReality: I think macOS support has not been considered. Current build errors on macOS looks trivial to fix but maybe after fixing those some real errors will come up. Do you have a working SteamVR setup on macOS?</p>
<p>SlicerElastix: Current build errors on macOS looks trivial to fix but maybe after fixing those some harder-to-fix errors will come up. I’ll try updating to latest master of Elastix and see if it fixes the problems.</p>
<p>SlicerVMTK: Looks like Python wrapping shared libraries are not found. It is probably not a trivial fix but somebody who knows Python wrapping on macOS would need to investigate.</p>

---
