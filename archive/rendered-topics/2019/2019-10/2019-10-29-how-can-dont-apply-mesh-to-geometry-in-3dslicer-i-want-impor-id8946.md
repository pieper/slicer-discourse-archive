---
topic_id: 8946
title: "How Can Dont Apply Mesh To Geometry In 3Dslicer I Want Impor"
date: 2019-10-29
url: https://discourse.slicer.org/t/8946
---

# How can dont apply mesh to geometry in 3Dslicer , i want import my software without mesh

**Topic ID**: 8946
**Date**: 2019-10-29
**URL**: https://discourse.slicer.org/t/how-can-dont-apply-mesh-to-geometry-in-3dslicer-i-want-import-my-software-without-mesh/8946

---

## Post #1 by @adele1371 (2019-10-29 17:59 UTC)

<p>How can dont apply mesh to geometry in 3Dslicer , i want import my software without mesh .</p>

---

## Post #2 by @lassoan (2019-10-29 18:24 UTC)

<p>What is your input data and what would you like to get as a result?</p>

---

## Post #3 by @adele1371 (2019-10-29 19:29 UTC)

<p>The format file is  STL . And i want segment brain to (wm-GM-csf and skull)  then import my software . But I don’t want the result of 3Dslicer  produce mesh. I just want to get the 3D model . Is it impossibe?? Or is there any software that produce segment file  with STL format  that produce segment file from brain that result nothing mesh? just 3d model</p>

---

## Post #4 by @pieper (2019-10-29 19:48 UTC)

<p>Hi <a class="mention" href="/u/adele1371">@adele1371</a> - to help us help you, can you clarify what you mean by 3d model without a mesh?  Maybe you want a rasterized labelmap image?  Also, are you starting with an STL file?  Or are you starting with a medical image, like an MRI or CT?</p>

---

## Post #5 by @adele1371 (2019-10-29 19:55 UTC)

<p>Hello mr pieper .thanks . Start file to 3d slicer is MRI picture . Export file is 3d model of segmentation brain . Final files is 4 stl file (wm-gm-csf-skull) that i can import into my software</p>

---

## Post #6 by @pieper (2019-10-29 20:10 UTC)

<p>Ah, okay, yes, makes more sense now.  For MRI brain segmentation you may want to use a specialized tool <a href="https://surfer.nmr.mgh.harvard.edu/">like freesurfer</a>.  You could then use Slicer to view the results and export to STL.  Or you can do the segmentation natively in Slicer using the segment editor, but brains are tricky to segment manually (it all depends on how accurate you need the result to be).</p>

---

## Post #7 by @adele1371 (2019-10-30 07:23 UTC)

<p>I can’t install  free surfer. Is there an online site for free surfer  that  give segments files.or is impossible for you that sent me ?</p>

---

## Post #8 by @pieper (2019-10-30 11:50 UTC)

<aside class="quote no-group" data-username="adele1371" data-post="7" data-topic="8946">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ea5d25/48.png" class="avatar"> adele1371:</div>
<blockquote>
<p>I can’t install free surfer</p>
</blockquote>
</aside>
<p>Why not?  It’s free <a href="https://surfer.nmr.mgh.harvard.edu/fswiki/DownloadAndInstall" class="inline-onebox">DownloadAndInstall - Free Surfer Wiki</a></p>
<p>If you don’t have linux you could install it virtually with <a href="https://www.virtualbox.org/">https://www.virtualbox.org/</a></p>

---

## Post #9 by @adele1371 (2019-10-30 13:38 UTC)

<p>Thank you mr pieper . So 3DSlicer can not produce 3d model without mesh right??</p>

---

## Post #10 by @pieper (2019-10-30 13:49 UTC)

<aside class="quote no-group" data-username="adele1371" data-post="9" data-topic="8946">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ea5d25/48.png" class="avatar"> adele1371:</div>
<blockquote>
<p>3d model without mesh</p>
</blockquote>
</aside>
<p>Sorry, it’s still not clear to me what you mean by this phrase.</p>

---

## Post #11 by @lassoan (2019-10-30 15:27 UTC)

<aside class="quote no-group" data-username="adele1371" data-post="9" data-topic="8946">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ea5d25/48.png" class="avatar"> adele1371:</div>
<blockquote>
<p>So 3DSlicer can not produce 3d model without mesh right??</p>
</blockquote>
</aside>
<p>In medical image computing, 3D model, surface mesh, and STL file usually refer to the same thing, so if you have 3D model then it means you have mesh.</p>
<p>If you have trouble installing freesurfer then you can create models from MRI images using Slicer with some more manual work as <a class="mention" href="/u/pieper">@pieper</a> suggested above. You can remove skull using SwissSkullStripper extension and get other parts by using Segment Editor module. See tutorials at <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">Slicer training page</a>.</p>

---
