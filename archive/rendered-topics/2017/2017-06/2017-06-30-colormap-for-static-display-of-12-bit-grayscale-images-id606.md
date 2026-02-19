---
topic_id: 606
title: "Colormap For Static Display Of 12 Bit Grayscale Images"
date: 2017-06-30
url: https://discourse.slicer.org/t/606
---

# Colormap for static display of 12 bit grayscale images

**Topic ID**: 606
**Date**: 2017-06-30
**URL**: https://discourse.slicer.org/t/colormap-for-static-display-of-12-bit-grayscale-images/606

---

## Post #1 by @jondo (2017-06-30 14:14 UTC)

<p>In order to look at 12 bit grayscale images on a 24 bit RGB display, one has to interactively change the rendering brightness to see all areas.</p>
<p>There are “perceptionally uniform” color maps [1] that could be used to render such images statically. This would be useful in situations without interactivity, like reports or papers. Is there a way to use such a color map instead?</p>
<p>[1]  like “viridis”, the new <a href="http://matplotlib.org/users/dflt_style_changes.html#colormap" rel="nofollow noopener">default colormap of Matplotlib 2.0</a></p>

---

## Post #2 by @lassoan (2017-06-30 21:51 UTC)

<p>Switch to latest nightly. It is stable, contains lots of fixes, and already contains these colormaps (Inferno, Magma, Plasma, Viridis).</p>

---

## Post #3 by @jondo (2017-07-03 11:38 UTC)

<p>Ah - as a newbie I only just found out about the Color module!</p>
<p>I am currently on version 4.7.0-2017-06-22, which already has Viridis in there. How do I use it for displaying a CT volume?</p>

---

## Post #4 by @lassoan (2017-07-03 20:34 UTC)

<p>To adjust color mapping, go to <code>Volumes</code> module and select a <code>Lookup table</code>.</p>

---
