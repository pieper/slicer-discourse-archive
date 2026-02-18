# Using Displacement Map to Deform or Morph a Segment/Model

**Topic ID**: 18552
**Date**: 2021-07-07
**URL**: https://discourse.slicer.org/t/using-displacement-map-to-deform-or-morph-a-segment-model/18552

---

## Post #1 by @Fluvio_Lobo (2021-07-07 03:12 UTC)

<p>Hello,</p>
<p>Is it possible to use a displacement map/volume, like the output from the <strong>Model to Model Distance</strong> module, to <strong>deform</strong> or <strong>morph</strong> another segment/volume/model? Even if it just a simple approximation.</p>
<p>I am trying to simulate the stretching of the skin over the advancement of multiple skull segments.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/3759d786dc157544585f40ee83834b25f9fd2eab.png" data-download-href="/uploads/short-url/7TEKgCTFIqutemh3YGZQFpz2OUj.png?dl=1" title="model2modeldist" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/3759d786dc157544585f40ee83834b25f9fd2eab_2_292x250.png" alt="model2modeldist" data-base62-sha1="7TEKgCTFIqutemh3YGZQFpz2OUj" width="292" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/3759d786dc157544585f40ee83834b25f9fd2eab_2_292x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/3759d786dc157544585f40ee83834b25f9fd2eab_2_438x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/3759d786dc157544585f40ee83834b25f9fd2eab_2_584x500.png 2x" data-dominant-color="7D9599"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">model2modeldist</span><span class="informations">682×583 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-07-12 14:47 UTC)

<p>You can very easily warp a model using displacement field stored for each point of the mesh (see <a href="https://vtk.org/doc/nightly/html/classvtkWarpVector.html" class="inline-onebox">VTK: vtkWarpVector Class Reference</a>). However, I’m not sure if Model to Model Distance extension provides displacement vectors. Anyway, if you want to align surface models then you can probably get better results with <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#model-registration">model registration modules</a>.</p>

---

## Post #3 by @Fluvio_Lobo (2021-07-13 02:31 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I found <a href="https://discourse.slicer.org/t/merge-scalars-of-two-models/15682/3">this post</a> and I am trying to repeat the process;</p>
<p>First, I ran <strong>Model To Model Distance</strong> and created <code>D_rev2orig</code> as the “displacement model”<br>
Additionally, I have a “target” model <code>D_ST</code> which I would like to warp/deform.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69b428da699103a73f84737b3763eb520d7052b4.jpeg" data-download-href="/uploads/short-url/f567IFiJGUQ8crInKAv4DW55rrm.jpeg?dl=1" title="figure_disp_map" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/69b428da699103a73f84737b3763eb520d7052b4_2_345x182.jpeg" alt="figure_disp_map" data-base62-sha1="f567IFiJGUQ8crInKAv4DW55rrm" width="345" height="182" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/69b428da699103a73f84737b3763eb520d7052b4_2_345x182.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/69b428da699103a73f84737b3763eb520d7052b4_2_517x273.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/69b428da699103a73f84737b3763eb520d7052b4_2_690x364.jpeg 2x" data-dominant-color="280D1C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure_disp_map</span><span class="informations">1222×647 62.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe251c1a674b401d1e320c78e8b1b31288ccd34a.png" data-download-href="/uploads/short-url/AggMES7ZkY6r9hXBePffVLyxqc2.png?dl=1" title="figure_skin_model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe251c1a674b401d1e320c78e8b1b31288ccd34a_2_345x182.png" alt="figure_skin_model" data-base62-sha1="AggMES7ZkY6r9hXBePffVLyxqc2" width="345" height="182" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe251c1a674b401d1e320c78e8b1b31288ccd34a_2_345x182.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe251c1a674b401d1e320c78e8b1b31288ccd34a_2_517x273.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe251c1a674b401d1e320c78e8b1b31288ccd34a_2_690x364.png 2x" data-dominant-color="332C15"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure_skin_model</span><span class="informations">1222×647 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here is what I am doing to warp the “target” model;</p>
<pre><code class="lang-auto">dispModel = getNode("D_rev2orig")
targetModel = getNode("D_ST")

dispMesh = dispModel.GetMesh()
dispMesh.GetPointData().SetActiveVectors("PointToPointVector")

warp = vtk.vtkWarpVector()
warp.SetInputData(dispMesh)

warp.SetScaleFactor(1.0)
warp.Update()
targetModel.SetPolyDataConnection(warp.GetOutputPort())
</code></pre>
<p>This overrides the <code>D_ST</code> “target” model and generates a weird hybrid model;<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d8ddb90d0e2a4b6dc39268782e2c08dbff350bb.jpeg" data-download-href="/uploads/short-url/dlCkFGN8Ufnsmpw5zMlNprrZHRh.jpeg?dl=1" title="figure_output_warp" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d8ddb90d0e2a4b6dc39268782e2c08dbff350bb_2_345x164.jpeg" alt="figure_output_warp" data-base62-sha1="dlCkFGN8Ufnsmpw5zMlNprrZHRh" width="345" height="164" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d8ddb90d0e2a4b6dc39268782e2c08dbff350bb_2_345x164.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d8ddb90d0e2a4b6dc39268782e2c08dbff350bb_2_517x246.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d8ddb90d0e2a4b6dc39268782e2c08dbff350bb_2_690x328.jpeg 2x" data-dominant-color="260C1A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">figure_output_warp</span><span class="informations">1222×583 91.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This model has the <code>PointToPointVector</code> attribute from the displacement model <code>D_rev2orig</code>, but does not have the geometry of the “target” model. The geometry is not the same as the “displacement model” however, so maybe I am just missing something in the script above?</p>

---

## Post #4 by @lassoan (2021-07-13 03:13 UTC)

<p>I’m not sure what “PointToPointVector” vector contains, but I guess it is something like vector to the closest point. This vector field can be very noisy and discontinuous, so I would not use it to warp a surface. Instead, I would try to use one of the surface registration methods.</p>
<p>Can you write a bit more about your end goal? You wrote above that “I am trying to simulate the stretching of the skin over the advancement of multiple skull segments.”, but this is not very clear for me. Displacement of rigid bone pieces and geometric interpolation between them will not tell much about how the skin will move or stretch. For that you would probably need to run FEM analysis, for example using <a href="https://febio.org/downloads/">FEBio</a>.</p>

---

## Post #5 by @Fluvio_Lobo (2021-07-13 13:22 UTC)

<blockquote>
<p>Can you write a bit more about your end goal? You wrote above that “I am trying to simulate the stretching of the skin over the advancement of multiple skull segments.”, but this is not very clear for me.</p>
</blockquote>
<p>Of course!<br>
The model representative of the bone segments here, also carrying the <strong>Model To Model Distance</strong> data, is the result of a <strong>Fronto-Orbital Advancement</strong> <a href="https://discourse.slicer.org/t/osteotomy-planner-v2-0/18384/2">planning done using Slicer</a>. I ended-up creating two posts about this problem because I wanted to separate this final step from the entire planning discussion.</p>
<p>My goal was to use either the <strong>Bandeau Model</strong> itself or the <strong>Model To Model Distance</strong> data  to then <strong>warp</strong> or <strong>deform</strong> the skin to match the overall advancement of the bones.</p>
<blockquote>
<p>This vector field can be very noisy and discontinuous, so I would not use it to warp a surface. Instead, I would try to use one of the surface registration methods.</p>
</blockquote>
<p>I have been using registration methods to warp the model <a href="https://discourse.slicer.org/t/osteotomy-planner-v2-0/18384/9">also</a>. So far creating a warp transform from fiducial registration has given me the best results, but the result can only be improved with the addition of more landmark and with manual registration. The limit is 30 landmarks and warp transforms do not support the automatic registration.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a90c2e25f38c89eceafd3a95467c9ec8134a298e.jpeg" data-download-href="/uploads/short-url/o7sMTp3HGrUIPnlQOn7ca8SBnae.jpeg?dl=1" title="skin_overlay" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a90c2e25f38c89eceafd3a95467c9ec8134a298e_2_341x250.jpeg" alt="skin_overlay" data-base62-sha1="o7sMTp3HGrUIPnlQOn7ca8SBnae" width="341" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a90c2e25f38c89eceafd3a95467c9ec8134a298e_2_341x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a90c2e25f38c89eceafd3a95467c9ec8134a298e_2_511x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a90c2e25f38c89eceafd3a95467c9ec8134a298e_2_682x500.jpeg 2x" data-dominant-color="33462D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">skin_overlay</span><span class="informations">1222×894 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I was working on Python script that would use the vertices of the source and target models as landmarks, but the registration was falling apart. If you think this is a viable approach, I can continue to explore this… I was thinking of sorting the vertices along the AP so that vertices would match somewhat better between models. In this case I am still limited by the 30 point limit. Is this a hard limit or just a warning about # computations?</p>
<blockquote>
<p>Displacement of rigid bone pieces and geometric interpolation between them will not tell much about how the skin will move or stretch. For that you would probably need to run FEM analysis, for example using <a href="https://febio.org/downloads/" rel="noopener nofollow ugc">FEBio</a>.</p>
</blockquote>
<p>I agree. In fact, I was planning to use FEBio too. My hope was to, at the very least, get some sort of nodal displacement field that I can use in FEBio to run the simulation a little more programmatically.</p>
<p>Perhaps I can improve the warp transform and convert it to a grid transform, vector volume, or displacement volume? <img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=12" title=":thinking:" class="emoji" alt=":thinking:" loading="lazy" width="20" height="20"></p>
<p>Let me know if this is a little clearer now,</p>

---

## Post #6 by @lassoan (2021-07-13 13:50 UTC)

<p>There should be no limit on number of points for registration, just the computation will get slower. To make computation fast, you can create bspline transform from the scattered landmark points using ScatteredTransform extension.</p>
<p>The main issue with transforms is that the deformation is constrained to be smooth, but it does not mean that the deformation will be realistic (e.g., bones may be stretched).</p>

---
