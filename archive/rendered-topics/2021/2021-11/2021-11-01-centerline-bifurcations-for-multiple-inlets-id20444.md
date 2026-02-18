# Centerline bifurcations for multiple inlets

**Topic ID**: 20444
**Date**: 2021-11-01
**URL**: https://discourse.slicer.org/t/centerline-bifurcations-for-multiple-inlets/20444

---

## Post #1 by @som1197 (2021-11-01 21:41 UTC)

<p>Hello,</p>
<p>I had some issues with the blanking array which is not generated correctly when multiple inlet branches are present. Consider the following example:</p>
<p>I have 2 inputs coming from the left and right vertebral arteries (LVA and RVA). The vmtk script using pyepad gives the following output and fails to generate/combine all centerlines correctly.<br>
Reference: <a href="http://www.vmtk.org/tutorials/Centerlines.html" class="inline-onebox" rel="noopener nofollow ugc">Computing Centerlines | vmtk - the Vascular Modelling Toolkit</a><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8597fe0144dd3c468aee3bebdea697a401b586d.png" alt="image" data-base62-sha1="qiPBAWssq15BC9dPuYwTEFQKdgF" width="267" height="384"></p>
<p>When I use 3D slicer, I tried different variations as shown in the figure to combine all the centerline vtk files into one object. But every time, I have 2 source points defined for a single Centerline model object, the output changes and just one centerline curve gets saved instead.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab93adeefd90f1a102380d2b20abd64471b5ac8c.png" data-download-href="/uploads/short-url/otQ32YFxRjhPzQuTm23OS9sJKO0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab93adeefd90f1a102380d2b20abd64471b5ac8c_2_376x499.png" alt="image" data-base62-sha1="otQ32YFxRjhPzQuTm23OS9sJKO0" width="376" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab93adeefd90f1a102380d2b20abd64471b5ac8c_2_376x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab93adeefd90f1a102380d2b20abd64471b5ac8c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab93adeefd90f1a102380d2b20abd64471b5ac8c.png 2x" data-dominant-color="EDF0EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">516×686 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So I used just 1 source point and multiple target points as shown below. In that case, the centerlines do get assembled into 1 vtk object but the blanking regions are not correctly produced at the bifurcation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3ab3b81b0b8ab7660e2a301011112fd65d431f5d.jpeg" data-download-href="/uploads/short-url/8niJRQVEAdXhkIZXwEKyFUu6VLD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ab3b81b0b8ab7660e2a301011112fd65d431f5d_2_689x360.jpeg" alt="image" data-base62-sha1="8niJRQVEAdXhkIZXwEKyFUu6VLD" width="689" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ab3b81b0b8ab7660e2a301011112fd65d431f5d_2_689x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ab3b81b0b8ab7660e2a301011112fd65d431f5d_2_1033x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3ab3b81b0b8ab7660e2a301011112fd65d431f5d.jpeg 2x" data-dominant-color="F2F3F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1231×643 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As the last alternative I combined the 2 vtk files using <a href="https://vtk.org/doc/nightly/html/classvtkAppendPolyData.html" class="inline-onebox" rel="noopener nofollow ugc">VTK: vtkAppendPolyData Class Reference</a> and tried to extract the branches using <a href="https://github.com/vmtk/vmtk/blob/master/vmtkScripts/vmtkbranchextractor.py" class="inline-onebox" rel="noopener nofollow ugc">vmtk/vmtkScripts/vmtkbranchextractor.py at master · vmtk/vmtk · GitHub</a>, but it failed to generate the blanking arrays where the 2 parent vessels (LVA and RVA) met.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd7add8f4c4e58e29167944bd859e0e7be61145c.jpeg" data-download-href="/uploads/short-url/vBiL3FI8Ab7IXY9eGG7qraYfzJy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dd7add8f4c4e58e29167944bd859e0e7be61145c_2_342x500.jpeg" alt="image" data-base62-sha1="vBiL3FI8Ab7IXY9eGG7qraYfzJy" width="342" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/dd7add8f4c4e58e29167944bd859e0e7be61145c_2_342x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd7add8f4c4e58e29167944bd859e0e7be61145c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd7add8f4c4e58e29167944bd859e0e7be61145c.jpeg 2x" data-dominant-color="EFF0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">484×707 74.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Does the vmtk centerline code need to be modified for generating the parent child relationships correctly when multiple parent vessels are present at the bifurcation?</p>
<p>Thank you.</p>

---

## Post #2 by @kayarre (2021-11-04 21:12 UTC)

<p>What is the overall goal you are trying to achieve?</p>

---

## Post #3 by @lassoan (2021-11-05 00:10 UTC)

<p>Centerline extraction must know the blood flow direction in each section of the vessel network, therefore your network must have a forest topology (one or more trees). When we used VMTK to model cardiac PDA then we performed two centerline extractions (with switching up some inflow/outflow points) and then merge the two trees by cutting both trees in the middle of the PDA and connecting the two endpoints.</p>

---

## Post #4 by @som1197 (2021-11-05 14:23 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a> ,</p>
<p>Can you explain what you mean to say by a figure possibly? Do you mean that for vasculatures having multiple inlets, the centerline trees should be extracted considering every inlet separately and then merging all of them?<br>
Annotating this figure might help.<br>
References<br>
<strong>Xiong, J., Sun, Q., Qian, Y., Hu, L., Tong, Z., Liu, J., &amp; Liu, J. (2021). Effects of patent ductus arteriosus on the hemodynamics of modified Blalock-Taussig shunt based on patient-specific simulation. <em>Frontiers in Physiology</em> , <em>12</em> , 707128.</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee7d1fcfa61305c6c792eb3a843dcaa3569613a5.jpeg" data-download-href="/uploads/short-url/y1LImeHAtvN16ShkYME0htZxgB7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee7d1fcfa61305c6c792eb3a843dcaa3569613a5_2_690x335.jpeg" alt="image" data-base62-sha1="y1LImeHAtvN16ShkYME0htZxgB7" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee7d1fcfa61305c6c792eb3a843dcaa3569613a5_2_690x335.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee7d1fcfa61305c6c792eb3a843dcaa3569613a5_2_1035x502.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee7d1fcfa61305c6c792eb3a843dcaa3569613a5.jpeg 2x" data-dominant-color="D5C0C0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1093×531 95.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8799a3225afbb338fdaecb3370785826299aede.jpeg" data-download-href="/uploads/short-url/sBu1BsOnXRALU1STUMcn000FgPc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8799a3225afbb338fdaecb3370785826299aede_2_666x500.jpeg" alt="image" data-base62-sha1="sBu1BsOnXRALU1STUMcn000FgPc" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c8799a3225afbb338fdaecb3370785826299aede_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8799a3225afbb338fdaecb3370785826299aede.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8799a3225afbb338fdaecb3370785826299aede.jpeg 2x" data-dominant-color="EDDDDF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">761×571 61.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In my case I have 2 vertebral arteries (parent arteries) merging into the basilar. I need to quantify the parent child relationship properly to quantify the overall loss due to bifurcations correctly. I am referring to this publication, but here parts of the vasculature having just a single inlet have been used for analysis.<br>
<strong>Chnafa, C., Valen-Sendstad, K., Brina, O., Pereira, V. M., &amp; Steinman, D. A. (2017). Improved reduced-order modelling of cerebrovascular flow distribution by accounting for arterial bifurcation pressure drops. Journal of Biomechanics, 51, 83–88.</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/9781c17806bb9d8629b9b95b13bf56fa45f4e9a3.jpeg" data-download-href="/uploads/short-url/lCi66l7VyYZBdpbkBEQXtfIptT5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9781c17806bb9d8629b9b95b13bf56fa45f4e9a3_2_690x245.jpeg" alt="image" data-base62-sha1="lCi66l7VyYZBdpbkBEQXtfIptT5" width="690" height="245" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9781c17806bb9d8629b9b95b13bf56fa45f4e9a3_2_690x245.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9781c17806bb9d8629b9b95b13bf56fa45f4e9a3_2_1035x367.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/9781c17806bb9d8629b9b95b13bf56fa45f4e9a3.jpeg 2x" data-dominant-color="F0F0F0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1045×372 55.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks</p>

---

## Post #5 by @som1197 (2021-11-05 14:24 UTC)

<aside class="quote quote-modified" data-post="4" data-topic="20444">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/som1197/48/14945_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/centerline-bifurcations-for-multiple-inlets/20444/4">Centerline bifurcations for multiple inlets</a> <a class="badge-category__wrapper " href="/c/community/vmtk/28"><span data-category-id="28" style="--category-badge-color: #E45735; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #F7941D;" data-parent-category-id="12" data-drop-close="true" class="badge-category --has-parent" title="This is the new home of the VMTK community (moved from VMTK Google Groups)"><span class="badge-category__name">VMTK</span></span></a>
  </div>
  <blockquote>
    Hello <a class="mention" href="/u/lassoan">@lassoan</a> , 
Can you explain what you mean to say by a figure possibly? Do you mean that for vasculatures having multiple inlets, the centerline trees should be extracted considering every inlet separately and then merging all of them? 
Annotating this figure might help. 
References 
Xiong, J., Sun, Q., Qian, Y., Hu, L., Tong, Z., Liu, J., &amp; Liu, J. (2021). Effects of patent ductus arteriosus on the hemodynamics of modified Blalock-Taussig shunt based on patient-specific simulation. Frontie…
  </blockquote>
</aside>


---

## Post #6 by @som1197 (2021-11-05 14:27 UTC)

<p>A modification in the vmtk code might be required?</p>
<p><a href="http://www.vmtk.org/tutorials/BranchSplitting.html" class="onebox" target="_blank" rel="noopener nofollow ugc">http://www.vmtk.org/tutorials/BranchSplitting.html</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f936d98bfc87bad0e86e753967b7b586c2dd6640.png" data-download-href="/uploads/short-url/zyEp7TwiwtB2CrRnGlSCVk7BFeM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f936d98bfc87bad0e86e753967b7b586c2dd6640.png" alt="image" data-base62-sha1="zyEp7TwiwtB2CrRnGlSCVk7BFeM" width="690" height="168" data-dominant-color="F6F695"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1278×313 23 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2021-11-05 15:10 UTC)

<p>Yes, we did what is described in the VMTK documentation: temporarily break the network to have trees and then merged the result:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39bff055f09da1c24cf7e8eec38c79eac371a365.png" data-download-href="/uploads/short-url/8eSrscXy9hRKPAU2EfCcuTrXFhH.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39bff055f09da1c24cf7e8eec38c79eac371a365_2_690x322.png" alt="image" data-base62-sha1="8eSrscXy9hRKPAU2EfCcuTrXFhH" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/39bff055f09da1c24cf7e8eec38c79eac371a365_2_690x322.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39bff055f09da1c24cf7e8eec38c79eac371a365.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39bff055f09da1c24cf7e8eec38c79eac371a365.png 2x" data-dominant-color="EBE0DE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1000×468 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @som1197 (2021-11-08 18:49 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thank you for the suggestion!<br>
I used that to generate separate centerline trees starting from the inlet and connecting the outlets separately, but still I lose the blanking part near the bifurcations, after merging the 2 trees.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/390eec127244226de6948b25b878d8af348918b9.jpeg" data-download-href="/uploads/short-url/88LbytzodbLAdL2NejzLtGvyJrr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/390eec127244226de6948b25b878d8af348918b9_2_690x323.jpeg" alt="image" data-base62-sha1="88LbytzodbLAdL2NejzLtGvyJrr" width="690" height="323" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/390eec127244226de6948b25b878d8af348918b9_2_690x323.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/390eec127244226de6948b25b878d8af348918b9_2_1035x484.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/390eec127244226de6948b25b878d8af348918b9.jpeg 2x" data-dominant-color="565555"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1107×519 99.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The same thing happens even when I try to merge these centerlines.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53bf4d0bd3af9460cd0d0f647f252ff663d02621.jpeg" data-download-href="/uploads/short-url/bWRupm8oKqMx3oWXWHJXSXGtlqF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53bf4d0bd3af9460cd0d0f647f252ff663d02621_2_576x500.jpeg" alt="image" data-base62-sha1="bWRupm8oKqMx3oWXWHJXSXGtlqF" width="576" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/53bf4d0bd3af9460cd0d0f647f252ff663d02621_2_576x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53bf4d0bd3af9460cd0d0f647f252ff663d02621.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53bf4d0bd3af9460cd0d0f647f252ff663d02621.jpeg 2x" data-dominant-color="3E3A3A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">736×638 83.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here, they use a method to encapsulate separate masks for the bifurcations by merging the centerlines based on <strong>vmtkcenterlinemerge</strong>: <a href="http://www.vmtk.org/vmtkscripts/vmtkcenterlinemerge.html" class="inline-onebox" rel="noopener nofollow ugc">vmtk - the Vascular Modelling Toolkit</a><br>
<a href="https://pubmed.ncbi.nlm.nih.gov/31397083/" class="inline-onebox" rel="noopener nofollow ugc">Impact of baseline coronary flow and its distribution on fractional flow reserve prediction - PubMed</a></p>
<p>Thanks</p>

---

## Post #9 by @lassoan (2021-11-08 19:06 UTC)

<aside class="quote no-group" data-username="som1197" data-post="8" data-topic="20444">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/som1197/48/14945_2.png" class="avatar"> som1197:</div>
<blockquote>
<p>I used that to generate separate centerline trees starting from the inlet and connecting the outlets separately, but still I lose the blanking part near the bifurcations, after merging the 2 trees.</p>
</blockquote>
</aside>
<p>We only needed the geometry and radius values (tom compute angles and curvatures) and not used the bifurcation reference system.</p>

---

## Post #10 by @som1197 (2021-11-08 19:15 UTC)

<p>Yes, sure I will need the 1D curvature to build a reduced order model. I shall probably use the aforementioned reference to isolate the bifurcation regions.</p>
<p>Thanks</p>

---

## Post #11 by @som1197 (2021-11-08 22:40 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a> , <a class="mention" href="/u/lantiga">@lantiga</a> ,</p>
<p>What modifications need to be done in the underlying vmtk code to take into account multiple inlets converging into a single daughter artery or for generating a forest of centerlines with the correct set of blanked regions?</p>
<p>Is there a way to generate centerlines considering multiple inlets for a fully connected Circle Of Willis? Even if I generate separate centerline trees for all inlets, the common portions (communicating arteries) should share a daughter branch between both the centerline trees. This does not happen using vmtk. It would be great if we can obtain the correct set of bifurcation vectors and bifurcation reference systems considering the blood flow direction in the patient specific centerline trees.</p>
<p>Thanks</p>

---
