---
topic_id: 5780
title: "Segments Imported As Stl Files Failing To Mask Properly"
date: 2019-02-14
url: https://discourse.slicer.org/t/5780
---

# Segments imported as stl files failing to mask properly

**Topic ID**: 5780
**Date**: 2019-02-14
**URL**: https://discourse.slicer.org/t/segments-imported-as-stl-files-failing-to-mask-properly/5780

---

## Post #1 by @miniBin (2019-02-14 14:08 UTC)

<p>Hello Slicer Community.</p>
<p>I imported an stl file and converted it to a segment as described in this forum: <a href="https://discourse.slicer.org/t/difficulty-with-editing-new-segments-imported-as-stl-files/5756" class="inline-onebox">Difficulty with editing new segments imported as stl files</a></p>
<p>However when I try to mask a transform using this segment it does not work as expected.</p>
<p>Green segment (sharp edges) to use as mask:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7d72b0a669a7b7aed663d24092e969d80c5f9eb.jpeg" alt="one" data-base62-sha1="svS0KV70yxcHGmgTatvRHOFSa7N" width="488" height="442"></p>
<p>Masking result (pixelated and blocky and not desired):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/320b692ddc0a8f87a58e8d05428f462f95f4ee3d.png" alt="two" data-base62-sha1="78IjUzuH7Lz3CqvoL3O6fg1y2Pr" width="434" height="386"></p>
<p>Help would be appreciated and thank you for your support.</p>

---

## Post #2 by @pieper (2019-02-14 14:45 UTC)

<p>Hi <a class="mention" href="/u/minibin">@miniBin</a> - The pictures help, but it’s still hard to diagnose what’s going on.  Could you post data and a short script that would allow people to reproduce the issue you are facing?  I suspect that the underlying cause is related to interpolation of transforms.</p>

---

## Post #3 by @miniBin (2019-02-14 14:53 UTC)

<p>What is the best way to transfer the data? Also I apologize but I do not know how to create the script?</p>

---

## Post #4 by @pieper (2019-02-14 15:11 UTC)

<p>You can use google drive / dropbox / onedrive etc to share the data.</p>
<p>By script I meant a python script, but if you aren’t using one, then a step-by-step description of what you are doing, what you expect to happen, and what happens instead.  (Speaking from experience, the process of creating such a script often leads to the solution, but if not then it will help us help you).</p>

---

## Post #5 by @cpinter (2019-02-14 15:25 UTC)

<p>The issue is probably still the resolution. If you do masking, then it’s not just the mask that determines the result but also the original image, which stays the same resolution regardless what you do with the segmentation.</p>
<p>I’d suggest using Crop Volumes module to resample the image as well. If you turn off interpolation for the volume in the slice view (an icon next to the volume selector in the drop-down menu of the slice view), then you will see the actual resolution.</p>

---

## Post #6 by @miniBin (2019-02-14 15:28 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>:  Thank you for your response.</p>
<p>Here is the google drive link: <a href="https://drive.google.com/drive/folders/1ZM_7Nf89sZSo_d9_NHUrV0OGbwfdmlzk?usp=sharing" rel="nofollow noopener">https://drive.google.com/drive/folders/1ZM_7Nf89sZSo_d9_NHUrV0OGbwfdmlzk?usp=sharing</a></p>
<p>I have provided all stls and transforms. Also there are two videos where I document step by step.</p>
<p>Thank you all for your continued effort and support.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a>: I tried using crop volumes earlier and the problem still occurred. I can try to turn off interpolation. Is there no way to mask out this object then?</p>

---

## Post #7 by @pieper (2019-02-19 17:59 UTC)

<p>Hi <a class="mention" href="/u/minibin">@miniBin</a> - when I go to that link I get an empty folder that says “drop files here”.  Are you sure it’s the right link?</p>
<p>Best,<br>
Steve</p>

---

## Post #8 by @miniBin (2019-02-19 22:37 UTC)

<p>My apologies, see if the link works now.</p>

---
