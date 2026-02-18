# Remove intesection lines in specific 2D view

**Topic ID**: 36430
**Date**: 2024-05-28
**URL**: https://discourse.slicer.org/t/remove-intesection-lines-in-specific-2d-view/36430

---

## Post #1 by @park (2024-05-28 11:20 UTC)

<p>Hi all,</p>
<p>I posted a question last time but did not get solution, so I’m posting it again.</p>
<p>I created four 2D slice views looks like the video below.<br>
<strong>Among these, I only want to display the intersection view in the axial window.</strong></p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af4c4d6513e518d871ed9652d527b774a8f976bb.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba2b4b33518942a010496c80ca91fc55d9eda924.png">
  </div><p></p>
<p>To achieve this, I tried changing the visibility to 0 or modifying the LinkedControl as shown below, but I observed that the intersection line reappeared when I moved the slice.</p>
<ol>
<li>
<p><code>sliceDisplayNode.SetIntersectingSlicesVisibility(0)</code></p>
</li>
<li>
<p><code>sliceCompositeNode.SetLinkedControl(False)</code></p>
</li>
</ol>
<p>Additionally, I performed SlabReconstruction on the leftmost panoramic view, but the line corresponding to the slab appeared, which interferes with the visualization.</p>
<p>Therefore, my questions are as follows:</p>
<ul>
<li>
<p>How can I display the intersection line only in the axial view?</p>
</li>
<li>
<p>How can I remove the lines related to the slab?<br>
(When I enable slab reconstruction with <code>sliceNode.SetSlabReconstructionEnabled(True)</code>, the line is generated, and I couldn’t find a way to turn it off.)</p>
</li>
</ul>
<hr>
<ul>
<li>In addition, How can I change the thickness of the intersection line?<br>
(<code>sliceDisplayNode.SetIntersectingSlicesLineThicknessMode(2)</code> does not work.)</li>
</ul>

---

## Post #2 by @cpinter (2024-05-28 13:14 UTC)

<p>A post was merged into an existing topic: <a href="/t/show-slice-intersection-line-only-in-specific-view/36275">Show slice intersection line only in specific view</a></p>

---

## Post #3 by @cpinter (2024-05-28 13:14 UTC)



---
