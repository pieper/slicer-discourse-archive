# SlicerMorph extension missing in Windows preview version

**Topic ID**: 7992
**Date**: 2019-08-12
**URL**: https://discourse.slicer.org/t/slicermorph-extension-missing-in-windows-preview-version/7992

---

## Post #1 by @smrolfe (2019-08-12 20:48 UTC)

<p>Hello,<br>
The SlicerMorph extension is not available in the Preview version of the Slicer for Windows. I checked <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerMorph" rel="nofollow noopener">CDash</a> and the Linux and Mac builds show no errors but the Windows build is missing. The last successful Windows build was yesterday, 8/11.</p>
<p>Where can I look to find what might be causing this?<br>
Thanks,<br>
Sara</p>

---

## Post #2 by @smrolfe (2019-08-12 21:07 UTC)

<p>The SegmentEditorExtraEffects extension, a dependency of SlicerMorph, is also missing from the Extension Manager and <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SegmentEditorExtraEffects" rel="nofollow noopener">shows no Windows build in CDash</a>.</p>

---

## Post #3 by @Sam_Horvath (2019-08-13 13:37 UTC)

<p>Hi Sara:</p>
<p>I looked at this on the factory machine yesterday, and couldn’t find any reason that the build was skipped.  I re-triggered both builds and they were successful.  I will keep any eye on it today to see if it happens again.</p>
<p>Sam</p>

---

## Post #4 by @smrolfe (2019-08-13 16:53 UTC)

<p>Thanks <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>!</p>

---
