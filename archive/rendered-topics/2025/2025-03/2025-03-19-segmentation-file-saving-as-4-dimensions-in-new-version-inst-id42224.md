# Segmentation File saving as 4 dimensions in new version instead of 3

**Topic ID**: 42224
**Date**: 2025-03-19
**URL**: https://discourse.slicer.org/t/segmentation-file-saving-as-4-dimensions-in-new-version-instead-of-3/42224

---

## Post #1 by @acoggins (2025-03-19 17:21 UTC)

<p>Using the new version of slicer my segmentation files (.seg.nrrd) are saving as 4 dimensions:<br>
dimension: 4<br>
space: left-posterior-superior<br>
sizes: 2 512 512 156</p>
<p>In previous versions, my segmentation files save as 3 dimensions:<br>
dimension: 3<br>
space: left-posterior-superior<br>
sizes: 512 512 156</p>
<p>Is there a way to save the segmentation files as 3 dimensions to match my old files and codes?</p>

---

## Post #2 by @muratmaga (2025-03-19 18:12 UTC)

<p>If you allowed overlap with segments (that is a voxel can be in more than one segment), I think it is always saved as 4D format.</p>
<p>I am not seeing any difference on my end between 5.8.1 and the latest preview.</p>

---

## Post #3 by @acoggins (2025-03-19 18:30 UTC)

<p>The older version I’m using is 4.11.20200930 and the new version is 5.8.0</p>

---

## Post #4 by @pieper (2025-03-19 18:32 UTC)

<p>In the Segmentations module you can collapse the layers.</p>

---

## Post #5 by @acoggins (2025-03-19 18:47 UTC)

<p>This worked, thank you!</p>

---

## Post #6 by @muratmaga (2025-03-19 18:52 UTC)

<aside class="quote no-group" data-username="acoggins" data-post="3" data-topic="42224" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/7993a0/48.png" class="avatar"> acoggins:</div>
<blockquote>
<p>The older version I’m using is 4.11.20200930 and the new version is 5.8.0</p>
</blockquote>
</aside>
<p>keep in mind those are both not maintained. The latest stable is 5.8.1</p>

---
