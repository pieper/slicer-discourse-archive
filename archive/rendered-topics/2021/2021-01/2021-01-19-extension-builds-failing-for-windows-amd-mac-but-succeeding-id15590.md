---
topic_id: 15590
title: "Extension Builds Failing For Windows Amd Mac But Succeeding"
date: 2021-01-19
url: https://discourse.slicer.org/t/15590
---

# Extension builds failing for Windows amd mac, but succeeding for linux

**Topic ID**: 15590
**Date**: 2021-01-19
**URL**: https://discourse.slicer.org/t/extension-builds-failing-for-windows-amd-mac-but-succeeding-for-linux/15590

---

## Post #1 by @Alex_Vergara (2021-01-19 12:41 UTC)

<p>In <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;begin=2020-12-25&amp;end=2021-01-08&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Opendose" rel="noopener nofollow ugc">Dash board</a> I can see my entension is building successfully in Linux (my main OS). However I have detected that it is failing for Windows and mac since december 25, 2020. I have not made any significant changes to it and since it is running fine on Linux I wonder what it is happening here?</p>

---

## Post #2 by @jamesobutler (2021-01-19 13:08 UTC)

<p>Using the link that you provided it shows Windows builds succeeding. Here is the link to the one started on January 17th <a href="http://slicer.cdash.org/build/2123703" class="inline-onebox" rel="noopener nofollow ugc">SlicerPreview : Build Summary</a>.</p>
<p>For macOS here’s a successful one on January 5th <a href="http://slicer.cdash.org/build/2113098" class="inline-onebox" rel="noopener nofollow ugc">SlicerPreview : Build Summary</a>.</p>
<p>There is probably not an issue with the extension itself. If it simply doesn’t show a report then the factory build machine had an error such as Slicer not building successfully or timing out. I haven’t seen anything that indicates your extension has been consistently failing to build though. Are there specific recent cdash pages for Windows and macOS showing it failed?</p>

---

## Post #3 by @Alex_Vergara (2021-01-19 19:33 UTC)

<p>Not failed but just not being built, <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;begin=2021-01-01&amp;end=2021-01-19&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Opendose" rel="noopener nofollow ugc">see this</a></p>

---

## Post #4 by @lassoan (2021-01-19 19:47 UTC)

<p>This is probably due to the macOS test timeout issue: <a href="https://github.com/Slicer/Slicer/issues/5391" class="inline-onebox">Dashboard test timeouts on macOS · Issue #5391 · Slicer/Slicer · GitHub</a>, which happens on the factory since Jan 7, but I could not reproduce it locally. <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> is investigating the problem.</p>

---

## Post #5 by @Alex_Vergara (2021-01-22 09:37 UTC)

<p>Ok everything is <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2021-01-21&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Opendose" rel="noopener nofollow ugc">back online now</a>, except the macos build that was timed out after 10 minutes.</p>

---
