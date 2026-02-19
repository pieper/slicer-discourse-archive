---
topic_id: 2524
title: "Minc2 Reader And Ras Coordinate System"
date: 2018-04-05
url: https://discourse.slicer.org/t/2524
---

# MINC2 Reader and RAS coordinate system

**Topic ID**: 2524
**Date**: 2018-04-05
**URL**: https://discourse.slicer.org/t/minc2-reader-and-ras-coordinate-system/2524

---

## Post #1 by @hgueziri (2018-04-05 20:34 UTC)

<p>Slicer 4.9.0-2017-11-29 r26666<br>
Linux Mint 18.2 64-bit</p>
<p>Hello all,</p>
<p>It is a very helpful feature to be able to read/write MINC2 files directly in slicer. However, I noticed an unexpected behavior when loading MINC2 files: the image is oriented in a wrong direction.</p>
<ul>
<li>First, when loading the image using ITK, the image is loaded properly, with an identity direction matrix.</li>
<li>Then, when loading the image using slicer, the volume direction matrix is rotated 180° around IS axis. As far as I know, MINC2 format uses the RAS orientation convention, which makes me believe that slicer considers the default orientation of minc files as LPI (not sure?) and re-orients the image to RAS.</li>
<li>I converted the image to a NIfTI file, then slicer reads it properly (volume direction has identity matrix)</li>
</ul>
<p>My questions are:</p>
<ul>
<li>am I missing something about the image orientations?</li>
<li>is it possible to turn off the automatic re-orientation to RAS in slicer?</li>
<li>is it a bug of slicer misinterpreting the MINC2 orientation?</li>
</ul>
<p>Thanks</p>

---

## Post #2 by @lassoan (2018-04-06 00:37 UTC)

<p>In all commonly used image file formats (nrrd, metaimage, nifti, etc), coordinate system (LPS, RAS, …) is specified in the file header. Does MINC2 files have this information in its header or MINC2 is hardcoded to always use RAS?</p>

---

## Post #3 by @hgueziri (2018-04-06 15:11 UTC)

<p>Hi Andras,</p>
<p>The MINC2 “world” coordinate system is always supposed to be in RAS. However, the x,y,z image coordinates can be stored in different order on the disk, the order is specified in the header’s tag</p>
<p><code>image:dimorder = "zspace,yspace,xspace" ;</code></p>
<p>I wonder if this is handled by the ITK reader filter.</p>

---

## Post #4 by @lassoan (2018-04-06 15:16 UTC)

<p>I’ve checked Slicer source code and MINC file loading is handled completely by ITK. We use whatever orientation ITK provides. While we could add workarounds at Slicer level, if you find any errors then best would be to report and fix in ITK. See ITK’s MINC image reader implementation here: <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/master/Modules/IO/MINC/src/itkMINCImageIO.cxx">https://github.com/InsightSoftwareConsortium/ITK/blob/master/Modules/IO/MINC/src/itkMINCImageIO.cxx</a></p>

---

## Post #5 by @hgueziri (2018-04-11 18:04 UTC)

<p>ITK loads MINC files in the correct orientation, i.e., RAS. I believe slicer is assuming by default that the image is in LPI and re-orient the images. Is it possible to have slicer leaving the orientation as loaded by ITK?</p>

---

## Post #6 by @lassoan (2018-04-12 19:42 UTC)

<aside class="quote no-group" data-username="hgueziri" data-post="5" data-topic="2524">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/a587f6/48.png" class="avatar"> hgueziri:</div>
<blockquote>
<p>ITK loads MINC files in the correct orientation, i.e., RAS</p>
</blockquote>
</aside>
<p>In general, ITK loads all images as LPS. If it loads MINC files as RAS then it may be an error. We can easily compensate for this inconsistency in Slicer but this would be better clarified with maintainer of MINC IO in ITK.</p>
<p><a class="mention" href="/u/thewtex">@thewtex</a> do you know if MINC reader behavior is intentional?</p>

---

## Post #7 by @thewtex (2018-04-12 20:13 UTC)

<p>Yes <a class="mention" href="/u/lassoan">@lassoan</a> is right – if the MINC reader is loading the image in RAS instead of LPS, then it is not intentional and it signals a bug.</p>

---

## Post #8 by @thewtex (2018-04-12 20:16 UTC)

<p>It sounds like the <code>itk::Image</code> <code>Direction</code> should account for RAS -&gt; LPS.</p>

---
