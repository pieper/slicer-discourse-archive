---
topic_id: 9246
title: "Extension Q3Dc Slicer 4 11 Macos Catalina"
date: 2019-11-21
url: https://discourse.slicer.org/t/9246
---

# Extension Q3DC Slicer 4.11. macOS Catalina

**Topic ID**: 9246
**Date**: 2019-11-21
**URL**: https://discourse.slicer.org/t/extension-q3dc-slicer-4-11-macos-catalina/9246

---

## Post #1 by @Fuessinger (2019-11-21 12:39 UTC)

<p>Hey,<br>
I have installed the extension Q3DC in the extension manager, but if I search the module, I cannot find it. Where is the mistake?<br>
Thank you<br>
Best regards</p>
<p>Marc Anton</p>

---

## Post #2 by @lassoan (2019-11-21 13:57 UTC)

<p>Is any error logged? (menu: Help / Report a bug)<br>
Does it work in latest stable release (currently Slicer-4.10.2)?</p>

---

## Post #3 by @Fuessinger (2019-11-21 19:41 UTC)

<p>Hey Andras,<br>
perfect help!! I switched back to the stable release. Now it works. Thanks for your help.<br>
Best regards</p>
<p>Marc Anton</p>

---

## Post #4 by @jamesobutler (2019-11-21 23:33 UTC)

<p>Based on the failing tests for the extension (see <a href="http://slicer.cdash.org/testDetails.php?test=9584870&amp;build=1753583" rel="nofollow noopener">here</a> for example) it looks like Q3DC hasn’t been updated to be Python3 compatible for Slicer 4.11</p>

---

## Post #5 by @lassoan (2019-11-22 04:14 UTC)

<p>There is a <a href="https://github.com/DCBIA-OrthoLab/Q3DCExtension/pull/16">pull request</a> that fixes the issue but the maintainer of the repository has not merged it. I’ll ask the maintainer again and if there is no response then we can fork the repository and fix it there.</p>

---

## Post #6 by @lassoan (2019-11-22 14:29 UTC)

<p>The pull request is merged now, so from tomorrow Q3DC should be avaialble for Slicer preview releases, too.</p>

---
