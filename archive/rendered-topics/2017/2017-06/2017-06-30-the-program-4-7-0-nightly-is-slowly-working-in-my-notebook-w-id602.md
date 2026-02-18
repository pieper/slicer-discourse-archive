# The program (4.7.0 nightly) is slowly working in my notebook. What sould I do?

**Topic ID**: 602
**Date**: 2017-06-30
**URL**: https://discourse.slicer.org/t/the-program-4-7-0-nightly-is-slowly-working-in-my-notebook-what-sould-i-do/602

---

## Post #1 by @vetyasin (2017-06-30 08:22 UTC)

<p>Hi.<br>
My operating system: Windows Ultimate 7 64 bit, 2.66-2.93 (Turbo) Ghz, 256 Gb SSD, i5, 6 Gb RAM.</p>
<p>The program is slowly working or freezing in processes of volume rendering, 3D model imaging etc.</p>
<p>What sould I do ?</p>
<p>Best,</p>

---

## Post #2 by @cpinter (2017-06-30 08:51 UTC)

<p>If you have a dedicated graphics card in your laptop, then changing the Rendering option in Volume Rendering to VTK GPU Ray Casting will make it much faster.</p>

---

## Post #3 by @lassoan (2017-07-01 00:11 UTC)

<p>While there are a few computationally intensive operations that may take time, in general Slicer can quickly process and visualize common data sets on average hardware.</p>
<p>If you need more helpful answers we need more information from you. What kind of data you load, how large, what do you do with it, what operations are slow?</p>

---
