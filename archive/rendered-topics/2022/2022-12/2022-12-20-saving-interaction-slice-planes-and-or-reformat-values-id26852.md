# Saving interaction slice planes and/or reformat values

**Topic ID**: 26852
**Date**: 2022-12-20
**URL**: https://discourse.slicer.org/t/saving-interaction-slice-planes-and-or-reformat-values/26852

---

## Post #1 by @Thijs (2022-12-20 15:27 UTC)

<p>Hi!</p>
<p>I am struggling a bit with creating markups in resliced planes. I hope that someone here might have some insight if what I want to achieve is possible?</p>
<p>Using the interactive slice planes is great, I can use it to find a good view of the anatomy that I am interested in. When I find a good view I can place some markers or a closed curve for example. Then I adjust the interactive slice planes to find a good view of another anatomical structure which I want to annotate. The difficulty that I am having is that I cannot find a way to easily go back to the first view that I created my annotations in.</p>
<p>Would there be a way to somehow save a slice orientation and go back to it?<br>
I found the Reformat module that allows manually setting angles/normals of the planes. I’m thinking maybe it is possible to save/load these Reformat values in a file using python? Or am I maybe overlooking a simpler solution?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2022-12-20 18:03 UTC)

<p>You could try creating transforms (move the data) rather than moving the slice planes (change the view).  Transforms can be saved with the scene and you can apply them arbitrarily.</p>

---
