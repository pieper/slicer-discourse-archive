# Normalization/calibration

**Topic ID**: 1420
**Date**: 2017-11-09
**URL**: https://discourse.slicer.org/t/normalization-calibration/1420

---

## Post #1 by @Hamburgerfinger (2017-11-09 14:56 UTC)

<p>What is the best way to apply a normalization or calibration factor to an image volume?  (I.e. just multiply all voxel scalars by a constant)</p>
<p>It seems like a good place for this would be the “Volumes” node.</p>
<p>Thanks!<br>
Luke</p>

---

## Post #2 by @lassoan (2017-11-09 17:08 UTC)

<p>You can click and drag in any of the slice viewers to apply linear scaling/offset to the displayed volume.</p>

---

## Post #3 by @Hamburgerfinger (2017-11-10 16:26 UTC)

<p>But this just changes the color mapping.  I want to actually modify the values present in the dataset by scalar multiplication.</p>
<p>For instance, if the image is quantified in units of (signal)/(unit volume) and I want (signal)/(unit mass), it’s necessary to multiply by a calibration factor (inverse of the density).</p>

---

## Post #4 by @jcfr (2017-11-10 18:51 UTC)

<aside class="quote no-group" data-username="Hamburgerfinger" data-post="3" data-topic="1420">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/eb9ed0/48.png" class="avatar"> Hamburgerfinger:</div>
<blockquote>
<p>to actually modify the values present in the dataset by scalar multiplication.</p>
</blockquote>
</aside>
<p>This should be helpful: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array" class="inline-onebox">Documentation/Nightly/Developers/Python scripting - Slicer Wiki</a></p>

---

## Post #5 by @fedorov (2017-11-10 22:48 UTC)

<p>If you prefer to use the GUI for that operation, you can use ShiftScaleImageFilter from the SimpleFilters module:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a92065604dcd399cd9419fa8e9978e5280b49c04.png" alt="image" data-base62-sha1="o8a6eLVLmyj3leB4v90iadXHcri" width="488" height="474"></p>

---

## Post #6 by @Hamburgerfinger (2017-11-10 23:31 UTC)

<p>Thanks, this is exactly what I wanted!</p>
<p>Best,<br>
Luke</p>

---
