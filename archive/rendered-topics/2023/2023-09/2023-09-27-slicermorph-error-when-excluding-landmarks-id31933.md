# Slicermorph: error when excluding landmarks

**Topic ID**: 31933
**Date**: 2023-09-27
**URL**: https://discourse.slicer.org/t/slicermorph-error-when-excluding-landmarks/31933

---

## Post #1 by @Ale (2023-09-27 13:55 UTC)

<p>Hi all, I’m using Slicermorph for GM analyses. The GPA runs fine using all landmarks, but when trying to exclude one landmark e.g. 12, from analysis nothing happens. Python console shows me this error:</p>
<p>AttributeError: ‘int’ object has no attribute ‘shape’</p>
<p>Thanks in advance,</p>
<p>Ale</p>

---

## Post #2 by @smrolfe (2023-09-28 17:55 UTC)

<p>Hi <a class="mention" href="/u/ale">@Ale</a></p>
<p>I have not been able to replicate this behavior, can you let me know what version of Slicer you are using and if you have the most recent version of SlicerMorph?</p>
<p>If both are up to date, are you able to share some data I can use to generate this error?</p>

---

## Post #3 by @smrolfe (2023-09-28 18:31 UTC)

<p>The error you are seeing is different, but may be related to: <a href="https://github.com/SlicerMorph/SlicerMorph/issues/276" class="inline-onebox" rel="noopener nofollow ugc">GPA - Exclude LM error · Issue #276 · SlicerMorph/SlicerMorph · GitHub</a></p>
<p>I’ve updated our repo and the fix should be available from the Slicer Extensions Manager tomorrow. Please let us know if this corrects your issue.</p>

---

## Post #4 by @Ale (2023-10-03 11:06 UTC)

<p>Hi Sara, thank you. Now works just fine!<br>
Cheers,</p>
<p>Ale</p>

---
