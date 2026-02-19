---
topic_id: 24553
title: "What Is The Corresponding Matrix To The Transformation Rotat"
date: 2022-07-29
url: https://discourse.slicer.org/t/24553
---

# What is the corresponding matrix to the transformation/rotation I need?

**Topic ID**: 24553
**Date**: 2022-07-29
**URL**: https://discourse.slicer.org/t/what-is-the-corresponding-matrix-to-the-transformation-rotation-i-need/24553

---

## Post #1 by @jsalas424 (2022-07-29 02:08 UTC)

<p>I have the following x, y, z coordinates:</p>
<pre><code class="lang-auto">-X      Z       Y
-16.215 126.065 12.236
-16.149 125.708 14.237
-16.843 125.851 13.707
... ... ...
</code></pre>
<p>Corresponding to matrix:</p>
<pre><code class="lang-auto">1.00    0.00    0.00    0.00
0.00    1.00    0.00    0.00
0.00    0.00    1.00    0.00
</code></pre>
<p>I need to transform them back to:</p>
<pre><code class="lang-auto">X       Y       Z
16.215  12.236  126.065
16.149  14.237  125.708
16.843  13.707  125.851
... ... ...
</code></pre>
<p>and find the corresponding matrix.</p>

---

## Post #2 by @mikebind (2022-07-29 17:41 UTC)

<p>I think what you are asking is for a matrix which takes a three element vector and transforms it to another three element vector where the output vector has as its first element the negative of the first element of the input vector, has as its second element the third element of the input vector, and has as its third element the second element of the input vector.  That matrix is just</p>
<pre><code class="lang-auto"> -1 0 0
  0 0 1
  0 1 0
</code></pre>

---

## Post #3 by @jsalas424 (2022-07-29 18:11 UTC)

<p>This is it, thanks for the help!</p>
<p>This corresponds to a +180* posterior/anterior rotation then a +90* left/right rotation.</p>

---
