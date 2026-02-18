# Suggestion: Quicker scissor tool and Seed growing to split a segment in two parts

**Topic ID**: 6006
**Date**: 2019-03-04
**URL**: https://discourse.slicer.org/t/suggestion-quicker-scissor-tool-and-seed-growing-to-split-a-segment-in-two-parts/6006

---

## Post #1 by @Amine (2019-03-04 15:11 UTC)

<p>Hello, i would like to suggest two features that i found my way around but were very time consuming ( hopefully not so hard to code):</p>
<ol>
<li>
<p>Using the scissor tool to cut through a segment in 3d view (without drawing a full circle, just a line) and separate the segment into two: especially useful for isolating territories of a vascular tree. obviously this would only work if the specified cutting line is enough to split the segment into two parts. (to do this i had to localise the cutting point with shift+crosshairs then erase a slice then new segment&gt; add island, wich is very time consuming for a lot of vessel branches )</p>
</li>
<li>
<p>Adding an option based on “grow from seeds” to split a segment containing two structures into two segments containing those structures: by using two other segments as seeds, the operation taking effect only on the segment to be split and not the whole volume obviously (the workaround here was to check editable area=inside all segments, then hide the segment to be split, and run the grow from seeds with only the segments containing seeds unhidden, but still its hard since gro&lt; from seends doesent run on the entire volume but limited to the area around the seed segments, so its necessary to paint all over the segments to split and not just in the junction zone)</p>
</li>
</ol>

---

## Post #2 by @Amine (2019-03-30 03:03 UTC)

<p>As for the Second Proposition, i tought id make an illustrated description because it is really important,<br>
So the goal is to separate this threshold into vascular and Bone<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a84d28e8084be594dfa514cf90545cd74a652036.png" alt="1" data-base62-sha1="o0RwNX7xf7gGAy4NURHkEyo7B6C" width="398" height="252"></p>
<p>To do this, the method i found is to use editable=inside that layer to paint seeding regions in two new segments<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4571446cf932586115da645affe0e818d5503bf8.png" alt="2" data-base62-sha1="9UjCpnBllSMKlgtIUkPHGktXPvO" width="358" height="243"></p>
<p>Then hide the original threshold, and do a growfromseeds with editable=Inside the hidden layer, to get this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93480a6baa2d1693dd5df53eb97939e8c5b6bd73.png" data-download-href="/uploads/short-url/l0Ux9dl5NnvKMsS60zFsENX9Gev.png?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93480a6baa2d1693dd5df53eb97939e8c5b6bd73_2_690x320.png" alt="3" data-base62-sha1="l0Ux9dl5NnvKMsS60zFsENX9Gev" width="690" height="320" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93480a6baa2d1693dd5df53eb97939e8c5b6bd73_2_690x320.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93480a6baa2d1693dd5df53eb97939e8c5b6bd73_2_1035x480.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93480a6baa2d1693dd5df53eb97939e8c5b6bd73.png 2x" data-dominant-color="898A91"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1260×586 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The problem here as you see is that grow from seeds defines  cropping region limited to the boundaries of the seeds to speed up the processing so the solution was to add a new segment and use editable= everywhere to draw the boundaries of the volume as shown here<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bddcd5d18885a8be280b083639a4dd05c5f326b.png" alt="4" data-base62-sha1="6g3JTxukJT3tsYOA48NbAY9fpAT" width="366" height="262"></p>
<p>Then proceed the same way with growfromseeds and editable=inside the hidden layer to get the final result:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55c94742a40eccf55c66d1ced03525ad8cce14c2.png" data-download-href="/uploads/short-url/ceTOXkFr6oj3wOa8nTOorIUV3nI.png?dl=1" title="5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55c94742a40eccf55c66d1ced03525ad8cce14c2_2_685x500.png" alt="5" data-base62-sha1="ceTOXkFr6oj3wOa8nTOorIUV3nI" width="685" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55c94742a40eccf55c66d1ced03525ad8cce14c2_2_685x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55c94742a40eccf55c66d1ced03525ad8cce14c2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55c94742a40eccf55c66d1ced03525ad8cce14c2.png 2x" data-dominant-color="2E1E30"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5</span><span class="informations">812×592 226 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What i would suggest is either adding an option in grow from seeds module to extend the cropping zone to even the hidden layers or to a specific layer<br>
OR to make a separate module that wil take as inputs the segment to split and the two seeding segments and use grow from seeds as usual, taking the whole segment into account.</p>
<p>This is the feature i used the most and it could get way simpler,<br>
Hope this Makes any sense!</p>

---
