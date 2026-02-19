---
topic_id: 16353
title: "Updating An Extension Using The Python Console"
date: 2021-03-04
url: https://discourse.slicer.org/t/16353
---

# Updating an extension using the python console

**Topic ID**: 16353
**Date**: 2021-03-04
**URL**: https://discourse.slicer.org/t/updating-an-extension-using-the-python-console/16353

---

## Post #1 by @athanell (2021-03-04 09:18 UTC)

<p>Operating system: Win 10<br>
Slicer version: 4.13.0-2021-02-17 r29718 / 5ca36fd</p>
<p>Hello,<br>
I am trying to update the <a href="https://github.com/lassoan/SlicerDICOMwebBrowser" rel="noopener nofollow ugc">SlicerDICOMwebBrowser</a> to it’s latest commit.<br>
I followed the directions of<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#Updating_installed_extensions" rel="noopener nofollow ugc">Update extension through the extension manager</a> but I still didn’t get the latest commit.<br>
Is there a way or some documentation on how to update a slicer extension to it’s latest commit through the python console?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2021-03-04 13:57 UTC)

<p>Extensions are updated once a day, which is during the night in EST. In Europe, this is during the day, in the morning, so you can expect to get the new extension versions by afternoon.</p>
<p>You can check status on the dasboard: <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2021-03-04&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=DICOMweb">preview</a>, <a href="https://slicer.cdash.org/index.php?project=Slicer4&amp;date=2021-03-04&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=DICOMweb">stable</a></p>

---
