---
topic_id: 27019
title: "Cmf Extension Not Available In Mac Preview Build"
date: 2023-01-03
url: https://discourse.slicer.org/t/27019
---

# CMF extension not available in Mac preview build

**Topic ID**: 27019
**Date**: 2023-01-03
**URL**: https://discourse.slicer.org/t/cmf-extension-not-available-in-mac-preview-build/27019

---

## Post #1 by @PaoloZaffino (2023-01-03 17:00 UTC)

<p>Hi all,<br>
I just noted that, on Mac, the CMF extension is not available in the preview build.<br>
Here the CDash page:<br>
<a href="https://slicer.cdash.org/viewTest.php?onlyfailed&amp;buildid=2902908" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.cdash.org/viewTest.php?onlyfailed&amp;buildid=2902908</a></p>
<p>Best,<br>
Paolo</p>

---

## Post #2 by @jcfr (2023-01-05 21:57 UTC)

<p>While some of the tests are failing, the extension should be available this can be verified <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2023-01-03&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=site&amp;compare1=63&amp;value1=macos&amp;field2=buildname&amp;compare2=63&amp;value2=CMF">here</a> where clicking on the failing test correspond to the buildid <code>2902908</code> associated with the link you shared.</p>
<p>As mentioned in <a href="https://discourse.slicer.org/t/no-mac-extensions-for-slicer-stable/26775/6" class="inline-onebox">No mac extensions for Slicer stable? - #6 by jcfr</a>, I will make sure the extensions test are disabled for the macos extension stable builds.</p>

---

## Post #3 by @PaoloZaffino (2023-01-14 15:24 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a>, now it is possible to download the extension!</p>

---
