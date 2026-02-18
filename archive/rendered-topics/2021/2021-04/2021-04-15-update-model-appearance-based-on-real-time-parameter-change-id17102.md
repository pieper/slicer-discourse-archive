# Update model appearance based on real-time parameter change

**Topic ID**: 17102
**Date**: 2021-04-15
**URL**: https://discourse.slicer.org/t/update-model-appearance-based-on-real-time-parameter-change/17102

---

## Post #1 by @szhang (2021-04-15 12:15 UTC)

<p>Hello, in order to have appearance changes (e.g. color, transparency etc) on a model, in accordance to parameter changes in real-time, do I have to create a new vtkMRMLDynamicModelerNode which copies the model I meant to change? Any help or pointer is appreciated!</p>

---

## Post #2 by @lassoan (2021-04-15 13:34 UTC)

<p>It depends on what exactly you want to do.</p>
<p>We implemented the <a href="https://github.com/SlicerIGT/SlicerIGT/#breach-warning">Breach Warning module in SlicerIGT extension</a> to change color of a model and make a warning sound when a tool gets too close to a designated model node. You may be able to use this module as is or make adjustments.</p>
<p>You can also very easily add an observer to any nodes (transform nodes, images, etc.) and make any changes to any nodes in the callback function. This is used for example for constructing tumor model during navigated surgeries based on real-time mass-spectrometry data.</p>

---

## Post #3 by @szhang (2021-04-15 14:15 UTC)

<p>Thank you, <a class="mention" href="/u/lassoan">@lassoan</a><br>
I looked into the Breach Warning case, it looks too complicated for me to implement now.<br>
For the second suggestion, could you point to any good example script to refer to?</p>
<p>Thanks again!</p>

---

## Post #4 by @lassoan (2021-04-15 16:21 UTC)

<p>There are lots of examples for commonly needed operations in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>.</p>
<p>What would you like to achieve? What “parameter changes” you would like to observe and what appearance you would like to change in response?</p>

---
