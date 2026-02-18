# Midpoint of an Open Curve

**Topic ID**: 13766
**Date**: 2020-09-30
**URL**: https://discourse.slicer.org/t/midpoint-of-an-open-curve/13766

---

## Post #1 by @NiinaIn3D (2020-09-30 06:57 UTC)

<p>Hi there, is there a way to determine a midpoint of an Open curve created in Markups? I.e. midpoint of the length, not centreline.</p>
<p>Or if not with Open curve, possibly for a curve model created using Curve Maker?</p>
<p>Many thanks!</p>

---

## Post #2 by @timeanddoctor (2020-09-30 09:19 UTC)

<p>you can resample the curve to 101 points and the 50th is the midpoint.</p>

---

## Post #3 by @NiinaIn3D (2020-10-01 00:01 UTC)

<p>What a beautiful simple solution, thanks. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #4 by @lassoan (2021-08-08 14:02 UTC)

<p>Alternatively (if you don’t want to resample the line but you are comfortable with writing a line of Python code) then you can get the curve length, and then get the coordinate of point along the line at half length.</p>

---
