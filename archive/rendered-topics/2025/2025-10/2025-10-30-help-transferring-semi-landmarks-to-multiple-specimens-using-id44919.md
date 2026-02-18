# Help transferring semi-landmarks to multiple specimens using ALPACA

**Topic ID**: 44919
**Date**: 2025-10-30
**URL**: https://discourse.slicer.org/t/help-transferring-semi-landmarks-to-multiple-specimens-using-alpaca/44919

---

## Post #1 by @r_dientes (2025-10-30 15:05 UTC)

<p>Hi everyone,</p>
<p>I’m working with a collection of archaeological human teeth (permanent canines) and I’m trying to transfer a set of <strong>semi-landmarks</strong> from a reference model to several specimens.</p>
<p>Here’s my current workflow:</p>
<ul>
<li>
<p>I segmented each tooth from micro-CT scans (SkyScan 1272) and exported the surfaces as <code>.ply</code> files.</p>
</li>
<li>
<p>I have <strong>manual anatomical landmarks</strong> placed on every specimen (saved as <code>.fcsv</code> markup files).</p>
</li>
<li>
<p>I manually selected and exported a <strong>set of semi-landmarks</strong> from the reference tooth (also as <code>.fcsv</code>).</p>
</li>
</ul>
<p>Now I would like to <strong>transfer these semi-landmarks from the template to the other specimens</strong>.</p>
<p>I tried using <strong>ALPACA</strong>, but the semi-landmarks end up in the wrong positions (collapsed or off the surface). This is my first time using the module, and I don’t fully understand how it works. If anyone could share <strong>tutorials, papers, or videos</strong> explaining ALPACA or its correct parameter settings, that would be very helpful.</p>
<p>I also have another issue: <strong>not all my specimens are complete</strong>, so I had to <strong>impute some missing landmarks in R</strong>, and I will probably need to do the same for a few semi-landmarks.<br>
Is it possible to perform that kind of imputation directly in <strong>3D Slicer</strong>, or should it be done in R?</p>
<p>Thank you very much for your help!</p>
<p>— Renata</p>

---

## Post #2 by @muratmaga (2025-10-30 15:34 UTC)

<aside class="quote no-group" data-username="r_dientes" data-post="1" data-topic="44919">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/r_dientes/48/79849_2.png" class="avatar"> r_dientes:</div>
<blockquote>
<p>have <strong>manual anatomical landmarks</strong> placed on every specimen (saved as <code>.fcsv</code> markup files).</p>
</blockquote>
</aside>
<p>If you have manual landmarks for every specimen, and want to transfer a template of semi-landmarks, do not use ALPACA. Use <strong>ProjectSemiLMs</strong> module: <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ProjectSemiLM" class="inline-onebox" rel="noopener nofollow ugc">SlicerMorph/Docs/ProjectSemiLM at master · SlicerMorph/SlicerMorph · GitHub</a></p>

---

## Post #3 by @r_dientes (2025-10-30 20:03 UTC)

<p>Hi Murat,</p>
<p>Thank you very much for your clear answer — it really helped me understand when to use <strong>ProjectSemiLM</strong> instead of <strong>ALPACA</strong>.</p>
<p>I was able to apply the module successfully, and it worked very well overall. Only a few semi-landmarks were not perfectly projected, but I corrected those manually using the <strong>Markups</strong> module.</p>
<p>I have one additional question related to incomplete specimens. In my dataset, many teeth show slight dental wear. In those cases, I imputed the corresponding anatomical landmarks in <strong>R</strong>, but I am not sure how to properly transfer the semi-landmarks.</p>
<p>What would you recommend doing in those cases? Is there a way to impute (or estimate) the missing semi-landmarks directly in <strong>Slicer</strong>? Or would it be better to create a new template excluding some semi-landmarks and then impute them in <strong>R</strong>? The challenge is that not all specimens have the same degree of wear…</p>
<p>Lastly, could you recommend any bibliography, tutorials, or methodological papers for cases involving incomplete specimens?</p>
<p>Thank you again for your time!</p>
<p>— Renata</p>

---

## Post #4 by @muratmaga (2025-10-30 20:16 UTC)

<p>For models with missing structures, you might want to disable projection (to the surface of the model) in ProjectSemiLMs, and try.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/603d38c4436215f8f248d9d8ff5490ee83bc6109.png" data-download-href="/uploads/short-url/dJn0fWaMgEGjKwBhdtqeNVUlTtL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/603d38c4436215f8f248d9d8ff5490ee83bc6109.png" alt="image" data-base62-sha1="dJn0fWaMgEGjKwBhdtqeNVUlTtL" width="494" height="278"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">494×278 25 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If this doesn’t work out, you can try to manually create TPS warping between your reference and target landmarks using the <strong>IGT Fiducial Transform wizard</strong> in IGT extension (make sure to use the Warping transform), and then apply that to your reference semi-landmarks.</p>
<p>Some tools in R does imputation of missing landmarks, but I am not sure which one works better. A few we tried in (Morpho and geomory) didn’t come out so good.</p>

---

## Post #5 by @r_dientes (2025-10-31 18:59 UTC)

<p>Thanks again for your suggestion — I tried using the <em>Fiducial Registration Wizard</em> with the warping (TPS) transform between my reference and target landmarks, but so far I haven’t managed to get good results. The deformation applies, but the semi-landmarks end up displaced from the surface.<br>
I’m currently evaluating whether to remove the problematic landmark</p>

---

## Post #6 by @muratmaga (2025-10-31 19:35 UTC)

<p>That’s because only the control points on the TPS deformation is guaranteed to be on the model, everything else will be interpolated. So if the morphology is sufficiently different between two models, or you have sparse coverage of control points (i.e. your anatomical landmarks) transfer may result in points floating in space. That’s why we have the projection option in the PlaceSemiLMs module.</p>
<p>You can either try to increase your corresponding control points in regions where things do not line up.</p>

---

## Post #7 by @muratmaga (2025-10-31 19:53 UTC)

<aside class="quote no-group" data-username="r_dientes" data-post="5" data-topic="44919">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/r_dientes/48/79849_2.png" class="avatar"> r_dientes:</div>
<blockquote>
<p>The deformation applies, but the semi-landmarks end up displaced from the surface.</p>
</blockquote>
</aside>
<p>You can also try the SegmentRegistration to derive the warping transform and then apply that.</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/SlicerRt/SegmentRegistration?tab=readme-ov-file#segment-registration-1">
  <header class="source">

      <a href="https://github.com/SlicerRt/SegmentRegistration?tab=readme-ov-file#segment-registration-1" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/4610f5a312d1cce803a6ead98c20ef1e/SlicerRt/SegmentRegistration?tab=readme-ov-file#segment-registration-1" class="thumbnail">

  <h3><a href="https://github.com/SlicerRt/SegmentRegistration?tab=readme-ov-file#segment-registration-1" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerRt/SegmentRegistration: 3D Slicer extension for segment registration (aka...</a></h3>

    <p><span class="github-repo-description">3D Slicer extension for segment registration (aka fusion, contour propagation)</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
