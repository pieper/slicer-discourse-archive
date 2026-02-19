---
topic_id: 5663
title: "Plotting 2D Line Segments"
date: 2019-02-06
url: https://discourse.slicer.org/t/5663
---

# Plotting 2D line segments

**Topic ID**: 5663
**Date**: 2019-02-06
**URL**: https://discourse.slicer.org/t/plotting-2d-line-segments/5663

---

## Post #1 by @smrolfe (2019-02-06 20:10 UTC)

<p>Hello,<br>
We need to plot a series of line segments in 2D. The number of line segments is variable and can be large, so using a node to represent each line segment is not practical. This is not currently supported in Slicer or VTK plots. There are standard functions available in R and MATLAB to create line segment plots from pairs of endpoints that could be used as a model for this function.</p>
<p>We’ve started a <a href="https://www.slicer.org/wiki/Documentation/Labs/Plotting2DLineSegments" rel="nofollow noopener">lab page</a> for this topic and have included an example using the R function segments. We’d appreciate feedback and ideas.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2019-02-06 20:52 UTC)

<p>We already have such plots! It may be not obvious, but 3D view is actually a very sophisticated 3D plot. We can plot displacements defined by transforms. You can choose to show displacement only at markup positions:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be84d6f320f74595ccbdfea36cbac47347bc2e59.png" data-download-href="/uploads/short-url/rbpkh3lCnAYRi5hb4AWbZaIyaoN.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be84d6f320f74595ccbdfea36cbac47347bc2e59_2_690x367.png" alt="image" data-base62-sha1="rbpkh3lCnAYRi5hb4AWbZaIyaoN" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be84d6f320f74595ccbdfea36cbac47347bc2e59_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be84d6f320f74595ccbdfea36cbac47347bc2e59_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/be84d6f320f74595ccbdfea36cbac47347bc2e59_2_1380x734.png 2x" data-dominant-color="63626A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1953×1040 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We just need a bit fancier axis actors. The current axis actor is always just a centered horizontal line, but there are several 2D and 3D box axes to choose from in VTK.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01db2e86cafb27faab794c91e4d66f5ab0d3b1ee.png" data-download-href="/uploads/short-url/gq4tvkuz76FfUY6CDDxVQqfjWK.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01db2e86cafb27faab794c91e4d66f5ab0d3b1ee_2_690x420.png" alt="image" data-base62-sha1="gq4tvkuz76FfUY6CDDxVQqfjWK" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01db2e86cafb27faab794c91e4d66f5ab0d3b1ee_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01db2e86cafb27faab794c91e4d66f5ab0d3b1ee.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01db2e86cafb27faab794c91e4d66f5ab0d3b1ee.png 2x" data-dominant-color="AA8FBE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">754×460 19.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The same view looks like a plot if you change the background to white and show a nicer axis actor, see for example in ParaView:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c3fcf7cca91ed1a60048cd3f1f3ae4e6a6fc84f.png" data-download-href="/uploads/short-url/frChmYiyw4CBWlBQ5gqumJ7gcCr.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c3fcf7cca91ed1a60048cd3f1f3ae4e6a6fc84f_2_690x376.png" alt="image" data-base62-sha1="frChmYiyw4CBWlBQ5gqumJ7gcCr" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c3fcf7cca91ed1a60048cd3f1f3ae4e6a6fc84f_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c3fcf7cca91ed1a60048cd3f1f3ae4e6a6fc84f_2_1035x564.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6c3fcf7cca91ed1a60048cd3f1f3ae4e6a6fc84f_2_1380x752.png 2x" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1922×1049 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @muratmaga (2019-02-06 21:31 UTC)

<p>Hi Andras,<br>
Yes, we do use the 3D. But for various reasons, we need to be able to their 2D plane projections using the Plot infrastructure. That’s where got stuck.</p>

---

## Post #4 by @lassoan (2019-02-06 21:45 UTC)

<p>Transform displacement in 2D views is already projected to 2D. See slice views in the first screenshot above.</p>

---

## Post #5 by @smrolfe (2019-02-06 23:08 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, this approach should work for us!</p>
<p>I have one more question on setting up the view. I need to get the 3D vectors projected onto a single plane, which it looks like you’ve done in the red slice view. My slice view looks like a cross section. Can you tell me if there is an option to set this? I recall seeing a projection setting in the models module, but don’t see something similar in the transform module.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6937b91c688e67fa98cb59eff25f09e0c3a9ed57.png" alt="image" data-base62-sha1="f0Nwh3wptxQIuXLdrwPsbfamwkL" width="408" height="463"></p>

---

## Post #6 by @muratmaga (2019-02-07 17:45 UTC)

<p>I did a fiducial registration of these two sets. When I visualize it, either I get this if I choose the entire region<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77605a017a9f4795cee80eb73c52ad58698f2410.png" alt="image" data-base62-sha1="h23fA0oxobeL4ohWJ3HXNFWYbao" width="540" height="440"></p>
<p>or this if I choose the moving set under transform visualization options</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5246d3dda79529f83e36103c8487673e2ee5fd6.png" alt="image" data-base62-sha1="nyUPf9tARwI4zomPoE12UcJspoO" width="393" height="408"></p>

---

## Post #7 by @lassoan (2019-02-07 19:06 UTC)

<p>If you use a thin-plate spline transform then you should see the arrows connecting each pair of corresponding fiducials.</p>
<p>Note Fiducial registration wizard determines “Transform <em>from</em> parent” transform from the landmarks and “Transform to parent” transform is computed on-the-fly. If the displacement field is irregular then the inverse may not be accurate and you may get something like the image above. To make sure the arrows show the exact displacements defined by the fiducial point pairs, go to Transforms module, flip To/From fiducial list and click “Invert” after computing the transformation in Fiducial registration wizard (then “Transform <em>to</em> parent” displacement is visualized, which does not require inversion).</p>
<p>Regular field, transform to parent (accurate):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84f0f498d13c2545308c9428985987e859a052c1.png" data-download-href="/uploads/short-url/iY3gMTy51ONX6c3dPNQyhaP4UbD.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84f0f498d13c2545308c9428985987e859a052c1_2_690x373.png" alt="image" data-base62-sha1="iY3gMTy51ONX6c3dPNQyhaP4UbD" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84f0f498d13c2545308c9428985987e859a052c1_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84f0f498d13c2545308c9428985987e859a052c1_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84f0f498d13c2545308c9428985987e859a052c1_2_1380x746.png 2x" data-dominant-color="474644"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 81.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Irregular field, transform to parent (some inaccuracies):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/4548118ed9911f4a3bd21191ef62af5b0053572b.png" data-download-href="/uploads/short-url/9STlNUBbNodcpfgeio8AtUwqzOj.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4548118ed9911f4a3bd21191ef62af5b0053572b_2_690x373.png" alt="image" data-base62-sha1="9STlNUBbNodcpfgeio8AtUwqzOj" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4548118ed9911f4a3bd21191ef62af5b0053572b_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4548118ed9911f4a3bd21191ef62af5b0053572b_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/4548118ed9911f4a3bd21191ef62af5b0053572b_2_1380x746.png 2x" data-dominant-color="474644"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 80.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Irregular field, transform from parent (accurate):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c72dbf8397312e123faa2c351a52895f2157aeba.png" data-download-href="/uploads/short-url/sq11WZpaE3jBlh51GKOQbicrxEu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c72dbf8397312e123faa2c351a52895f2157aeba_2_690x373.png" alt="image" data-base62-sha1="sq11WZpaE3jBlh51GKOQbicrxEu" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c72dbf8397312e123faa2c351a52895f2157aeba_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c72dbf8397312e123faa2c351a52895f2157aeba_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c72dbf8397312e123faa2c351a52895f2157aeba_2_1380x746.png 2x" data-dominant-color="474644"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 81.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
