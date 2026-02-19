---
topic_id: 4640
title: "I Cannot Find Fastgrowcut Extension In Latest Version 4 11"
date: 2018-11-05
url: https://discourse.slicer.org/t/4640
---

# I cannot find fastgrowcut extension in latest version 4.11.

**Topic ID**: 4640
**Date**: 2018-11-05
**URL**: https://discourse.slicer.org/t/i-cannot-find-fastgrowcut-extension-in-latest-version-4-11/4640

---

## Post #1 by @Chen_Bangbin (2018-11-05 15:38 UTC)

<p>I just installed latest 3d slicer version 4.11, but cannot find fastgrocut extension.<br>
Is ‘‘fastgrowcut’’ extension deleted from the latest version?<br>
I am using mac version.<br>
Thank you for your help!</p>

---

## Post #2 by @Sam_Horvath (2018-11-05 16:01 UTC)

<p>The extension is still present in the index, but is currently failing to build on all platforms.</p>
<p>It appears to have been broken when a legacy function was removed from ITK:<br>
<code>error: ‘class itk::TimeProbe’ has no member named ‘GetMeanTime’</code></p>

---

## Post #3 by @lassoan (2018-11-05 16:44 UTC)

<p>The old fastgrowcut extension has been completely reworked, hugely improved in performance, robustness, and usability, and the result has been made available in Segment editor module as “<a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html#grow-from-seeds-grow-from-seeds">Grow from seeds</a>” effect. You can find several tutorials about how to use it on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">training page</a>.</p>

---
