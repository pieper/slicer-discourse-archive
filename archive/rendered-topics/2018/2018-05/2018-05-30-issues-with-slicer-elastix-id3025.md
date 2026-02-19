---
topic_id: 3025
title: "Issues With Slicer Elastix"
date: 2018-05-30
url: https://discourse.slicer.org/t/3025
---

# Issues with Slicer Elastix

**Topic ID**: 3025
**Date**: 2018-05-30
**URL**: https://discourse.slicer.org/t/issues-with-slicer-elastix/3025

---

## Post #1 by @Sam_Horvath (2018-05-30 18:55 UTC)

<p>OS: Windows 10<br>
Slicer version 5/23 through current nightly</p>
<p>I am running into several issues with the Elastix General registration.  As far back as the 4/24 installer, I am getting this error on any registration attempt (<a href="https://issues.slicer.org/view.php?id=4568" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4568</a>):<br>
Volume registration is started in working directory: C:/Users/sam.horvath/AppData/Local/Temp/Slicer/Elastix/20180530_145144_361<br>
Register volumes…<br>
Error: global name ‘platform’ is not defined</p>
<p>Older versions are (5/23 and previous for me) are affected by this issue: <a href="https://github.com/lassoan/SlicerElastix/issues/7" rel="nofollow noopener">https://github.com/lassoan/SlicerElastix/issues/7</a></p>

---

## Post #2 by @lassoan (2018-05-30 19:43 UTC)

<p>Thanks for reporting this, the error is now fixed (see <a href="https://issues.slicer.org/view.php?id=4568">https://issues.slicer.org/view.php?id=4568</a>).</p>
<p>For extensions that are hosted on github and issue tracker is enabled, the best is to report the errors directly there (instead of the Slicer core issue tracker and/or the forum).</p>

---
