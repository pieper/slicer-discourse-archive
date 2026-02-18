# Slice-by-slice statistics

**Topic ID**: 1099
**Date**: 2017-09-21
**URL**: https://discourse.slicer.org/t/slice-by-slice-statistics/1099

---

## Post #1 by @mschumaker (2017-09-21 19:51 UTC)

<p>Given an image volume and a segmentation, is there a way to get image statistics on individual slices along an axis? In particular, I’m looking for mean image intensities within 2D segmentations in multiple Axial views.</p>

---

## Post #2 by @Fernando (2017-09-21 19:55 UTC)

<p>Have you tried the <strong>Segment Statistics</strong> module of the latest nightly version?</p>

---

## Post #3 by @mschumaker (2017-09-21 20:12 UTC)

<p>I have, yes. However, if I create a 3D segmentation, it appears that what’s produced is a set of statistics for the full 3D segmentation, rather than individual slices along an axis. Is there a way to get (Axial) slice-by-slice statistics, without creating a separate segment for every slice?</p>

---

## Post #4 by @lassoan (2017-09-21 21:18 UTC)

<p>This is a very specialized requirement that you have to implement a simple script for. Probably the easiest is to export segmentation to labelmap volume and do compute statistics using numpy. In numpy it’s very easy to get a single slice of a volume, apply a mask, and compute mean.</p>

---

## Post #5 by @mschumaker (2017-09-21 22:46 UTC)

<p>Ok, thanks, I’ll try it that way.</p>

---

## Post #6 by @timeanddoctor (2019-12-02 12:03 UTC)

<p>Dear Professor Michael Schumaker:</p>
<p>Did you completed such a statistics?</p>

---
