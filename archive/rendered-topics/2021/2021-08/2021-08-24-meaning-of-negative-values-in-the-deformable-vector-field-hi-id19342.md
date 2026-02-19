---
topic_id: 19342
title: "Meaning Of Negative Values In The Deformable Vector Field Hi"
date: 2021-08-24
url: https://discourse.slicer.org/t/19342
---

# Meaning of negative values in the Deformable Vector Field histogram

**Topic ID**: 19342
**Date**: 2021-08-24
**URL**: https://discourse.slicer.org/t/meaning-of-negative-values-in-the-deformable-vector-field-histogram/19342

---

## Post #1 by @toyama (2021-08-24 15:48 UTC)

<p>We are trying to get the histogram of each contour of the DVF to see how it changes before and after the DIR.<br>
So, I created a DVF using the transform module and got the histogram of each countour of its VectorField.<br>
However, the result contained negative values.<br>
I thought the DVF was the square root of the sum of squares of the x-, y-, and z-axes, so it has positive values, and I don’t know why the DVF shows negative values in the histogram.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac7bc145a2bdcb635e6c3503ff175927bdc21bdc.png" alt="image" data-base62-sha1="oBRgEWkeMz0BNXgk1oPtz38qJU8" width="674" height="449"></p>

---

## Post #2 by @pieper (2021-08-24 22:55 UTC)

<p>It sounds like this is related to a previous discussion linked below.  Just to be sure we are all talking about the same things can you explain the exact steps that led to this graph?  It seems like we never quite reached a conclusion in the previous discussion.  Maybe we should just disable or fix whatever leads to the creation of this graph.</p>
<p><a href="https://discourse.slicer.org/t/negative-values-in-dvf-histogram/">https://discourse.slicer.org/t/negative-values-in-dvf-histogram/</a></p>

---
