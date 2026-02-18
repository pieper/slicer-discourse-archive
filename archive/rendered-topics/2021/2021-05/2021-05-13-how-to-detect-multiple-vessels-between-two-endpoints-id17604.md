# How to detect multiple vessels between two endpoints

**Topic ID**: 17604
**Date**: 2021-05-13
**URL**: https://discourse.slicer.org/t/how-to-detect-multiple-vessels-between-two-endpoints/17604

---

## Post #1 by @perecanals (2021-05-13 10:55 UTC)

<p>Hi,</p>
<p>In the images I usually analyze, it is common to get vascular structures that have more than one path between endpoints (vessels that originate at one point and converge afterwards). As I understand it, the centerline model extracted by VMTK only detects the shortest path between two endpoints, which causes the longer path (a different vascular segments) to be excluded from the centerline model. However, the network model does include the missing vessel, but I would like to have it in the centerline model as centerlines look much smoother and better than the network model. Any ideas on how to do that?</p>
<p>I attach a couple of images of an example case. The left vertebral artery is missing in the centerline model (first image). The Voronoi diagram inside the vessel and the network model look good, though (second image).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bffe400ad8febd0c671916d70f124495f900ffa.jpeg" data-download-href="/uploads/short-url/6heM0K7tIxhdnKmEjLV1GRHHCQi.jpeg?dl=1" title="img1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2bffe400ad8febd0c671916d70f124495f900ffa_2_295x374.jpeg" alt="img1" data-base62-sha1="6heM0K7tIxhdnKmEjLV1GRHHCQi" width="295" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2bffe400ad8febd0c671916d70f124495f900ffa_2_295x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2bffe400ad8febd0c671916d70f124495f900ffa_2_442x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2bffe400ad8febd0c671916d70f124495f900ffa_2_590x748.jpeg 2x" data-dominant-color="939AC5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">img1</span><span class="informations">1252×1588 226 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/240acf7ae9e6f0ce732ee459fea4f63c9bae5527.jpeg" data-download-href="/uploads/short-url/58QlIoHG5PUtb7CPJKWT80yd7bF.jpeg?dl=1" title="img2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/240acf7ae9e6f0ce732ee459fea4f63c9bae5527_2_269x374.jpeg" alt="img2" data-base62-sha1="58QlIoHG5PUtb7CPJKWT80yd7bF" width="269" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/240acf7ae9e6f0ce732ee459fea4f63c9bae5527_2_269x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/240acf7ae9e6f0ce732ee459fea4f63c9bae5527_2_403x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/240acf7ae9e6f0ce732ee459fea4f63c9bae5527_2_538x748.jpeg 2x" data-dominant-color="9297BF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">img2</span><span class="informations">1252×1742 319 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2021-05-13 14:19 UTC)

<p>“Network extraction” method performs geometric analysis and extracts a graph (with circles, etc). Limitation is that vessel shape at branching points is not anatomically meaningful.</p>
<p>“Centerline tree extraction” can extract vessel trees. It provides more anatomically realistic centerline shape at branching points, but for this you need to select one or more “inflow” endpoints, and each other (“outflow”) endpoint will be connected to the closest inflow point. To extract circles, you either need to make a small cut in the circle (in the input model) or add more endpoints in the circle and then patch up the small disconnect in a post-processing step.</p>
<p>See more information in the <a href="https://github.com/vmtk/SlicerExtension-VMTK#installation">VMTK extension documentation</a>.</p>

---
