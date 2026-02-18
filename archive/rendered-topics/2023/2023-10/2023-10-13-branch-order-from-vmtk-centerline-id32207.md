# Branch order from vmtk-centerline

**Topic ID**: 32207
**Date**: 2023-10-13
**URL**: https://discourse.slicer.org/t/branch-order-from-vmtk-centerline/32207

---

## Post #1 by @b_gop (2023-10-13 12:57 UTC)

<p>Hi,</p>
<p>Is there any way I can get branch order information from the centerline computed by VMTK?</p>
<p>Thanks!</p>

---

## Post #2 by @chir.set (2023-10-13 17:08 UTC)

<aside class="quote no-group" data-username="b_gop" data-post="1" data-topic="32207">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/b_gop/48/67116_2.png" class="avatar"> b_gop:</div>
<blockquote>
<p>branch order information</p>
</blockquote>
</aside>
<p>The “branch order information” is hard to understand.</p>
<p>If you use the logic class of BranchClipper module from SlicerVMTK extension, you can get the number of branches from the input centerline using the ::GetNumberOfBranches() function. You can get each branch with ::GetBranch(). Perhaps these information may suit your context.</p>

---

## Post #3 by @b_gop (2023-10-13 20:36 UTC)

<p>I need the " <strong>the topological distance (number of nodes to cross) downwards to the farthest terminal branch</strong> . For example, as in the images attached below. And along with the branch order for each branch, also the associated diameter, curvature, etc.</p>
<p>I hope this makes sense. Would you know of a method to get this data?</p>
<p>Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6eb9338baae1dde0777ffc1e2f75dc64368cd151.png" data-download-href="/uploads/short-url/fNvjsi5riMWDLnQ7lJRCn0pc61b.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6eb9338baae1dde0777ffc1e2f75dc64368cd151.png" alt="image" data-base62-sha1="fNvjsi5riMWDLnQ7lJRCn0pc61b" width="690" height="465" data-dominant-color="EDEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">778×525 8.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a60ae71e61d1bc7c99d42e91cee1d5dca383370.png" alt="image" data-base62-sha1="fb3Kyktc14QAtk96RO2rvJRLf32" width="260" height="335"></p>

---

## Post #4 by @chir.set (2023-10-14 20:45 UTC)

<p>This does not entirely solve your problem, it’s rather a hint to build up a solution. I didn’t get further than exploring a bit further the too many functions offered by the VMTK libs.</p>
<p>The basic idea is to identify all parts of a centerline beyond a selected bifurcation, and annotate them in some way according to the levels in your diagram. The bifurcating parts of a branched centerline can be identified by a ‘blankingArrayName’ after due processing.</p>
<p>From vtkvmtkComputationalGeometry, you can use vtkvmtkCenterlineBranchExtractor() that produces a polydata tagged with many scalar arrays, on which is the ‘blankingArrayName’ that you pass in, typically ‘Blanking’. You can find an example in the ‘Extract centerline’ module’s implementation. Use this polydata output onwards.</p>
<p>Then exploring vtkvmtkCenterlineUtilities() in vtkvmtkComputationalGeometry is very informative. It exposes many functions, 2 of which are GetBlankedGroupsIdList() and FindAdjacentCenterlineGroupIds(). These, and some of the other functions also, may help you identify individual branches at each bifurcation. Then your code should tag them relative to a trunk as reference.</p>
<p>If you get a working solution, please share it here.</p>
<p>Regards.</p>

---
