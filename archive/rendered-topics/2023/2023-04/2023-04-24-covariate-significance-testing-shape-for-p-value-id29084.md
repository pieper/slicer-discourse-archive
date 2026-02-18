# Covariate Significance Testing - shape for p-value?

**Topic ID**: 29084
**Date**: 2023-04-24
**URL**: https://discourse.slicer.org/t/covariate-significance-testing-shape-for-p-value/29084

---

## Post #1 by @Yuyoung (2023-04-24 08:15 UTC)

<p>Hello everyone,</p>
<p>I am currently using version 4.0.1 - 2023-02-08 of SlicerSALT to check out the morphological changes in the human pubic symphyseal surface as a result of aging. Specifically, I am now analyzing four age groups: 20s, 40s, 60s, and 80s.</p>
<p>My main question concerns the Covariate Significance Testing Module. I have reviewed the <a href="https://docs.google.com/presentation/d/1i8kAbBCAswffkwVwBqFe14MT1OtVyUcd4AWxqVKOwjI/present?slide=id.p1" rel="noopener nofollow ugc">tutorial</a> on the <a href="https://salt.slicer.org/documentation/" rel="noopener nofollow ugc">SlicerSALT documentation</a> and some talks made on community, but still <strong>having some trouble comprehending what input file should I use for Shape for p-values</strong>.</p>
<p>Here are the steps I took, prior to Covariate Significance Testing Module:</p>
<blockquote>
<ol>
<li>
<p>Processed the output files of SPHARM-PDM, specifically the <strong>pp_surf_SPHARM_ellalign.vtk</strong> files, using the Procrustes Registration module.</p>
</li>
<li>
<p>Used <strong>Population Analysis Module</strong> to extract the mean model for each age group with the output files from step 1.</p>
</li>
<li>
<p>Used the <strong>Model to Model Distance Module</strong> to extract a vtk file that visualizes the changes between two age groups.<br>
e.g. To observe the changes between the 20s and 40s, I set the 20s mean as the source and the 40s mean as the target, and set the distance as corresponding point_to_point. Below is the result of 20s to 40s Model to Model (viewed on Paraview)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc6dccca2cd4c8300a9c34cfefd9f026187006e5.png" data-download-href="/uploads/short-url/qSV0Bzl1IFnfF608IEETG4XaTSl.png?dl=1" title="20To40_mtm" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc6dccca2cd4c8300a9c34cfefd9f026187006e5_2_263x500.png" alt="20To40_mtm" data-base62-sha1="qSV0Bzl1IFnfF608IEETG4XaTSl" width="263" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc6dccca2cd4c8300a9c34cfefd9f026187006e5_2_263x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc6dccca2cd4c8300a9c34cfefd9f026187006e5_2_394x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc6dccca2cd4c8300a9c34cfefd9f026187006e5.png 2x" data-dominant-color="596969"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20To40_mtm</span><span class="informations">403×764 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
</blockquote>
<p>I then used the <strong>Covariate Significance Testing Module</strong> to determine whether the vector data shown in the model to model vtk file were statistically significant.</p>
<p>The input and output for my Covariate Significance Testing on the 20s and 40s groups are as follows:</p>
<blockquote>
<p><em>Input:</em></p>
<ul>
<li><strong>Select CSV files:</strong> a CSV file with two columns. The first column contains path-to-vtk files for the 20s and 40s, and the second column contains an index for each age group (0 for 20s and 1 for 40s).</li>
<li><strong>Select shape for p-value:</strong> I consider it as a template model that can display p-values. So, I thought in order to see the change from 20s to 40s, I should use the mean model of the 20s.</li>
</ul>
<p><em>Output:</em><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd211bc15599fdfc6ec55dfbf35fc307b85292ce.png" data-download-href="/uploads/short-url/vycseFzoODBzhSlhw9JwXVD36rQ.png?dl=1" title="20To40-side" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd211bc15599fdfc6ec55dfbf35fc307b85292ce_2_505x500.png" alt="20To40-side" data-base62-sha1="vycseFzoODBzhSlhw9JwXVD36rQ" width="505" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd211bc15599fdfc6ec55dfbf35fc307b85292ce_2_505x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd211bc15599fdfc6ec55dfbf35fc307b85292ce.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd211bc15599fdfc6ec55dfbf35fc307b85292ce.png 2x" data-dominant-color="555F70"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20To40-side</span><span class="informations">526×520 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
(L) the model-to-model VTK, (R) result of the covariate significance testing (Paraview)<br>
I think the change pattern is quite consistent with each other.</p>
</blockquote>
<p>FINALLY the questions are:</p>
<blockquote>
<ol>
<li>
<p><em><strong>What exactly is the “shape for p-value”?</strong></em> I’ve understood it as a template to display the p-value result.</p>
</li>
<li>
<p>To see the desired result, age-related changes, <em><strong>is it correct to import a younger age group’s mean model in “shape for p-value”</strong></em>?</p>
</li>
<li>
<p>I also had an experiment importing 40s mean models to “shape for p-value” while using the same CSV file as before (right image). However, <em><strong>the result was not similar</strong></em> to when I used a 20s mean model (left image). <em><strong>Can you explain to me why this had happened?</strong></em><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/925c210871c06c63739019f77f5dcfe65cd9e4ef.png" data-download-href="/uploads/short-url/kSL5XV08ytiRtvsaYDw9xkCZQTl.png?dl=1" title="20to40mean-side" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/925c210871c06c63739019f77f5dcfe65cd9e4ef_2_690x420.png" alt="20to40mean-side" data-base62-sha1="kSL5XV08ytiRtvsaYDw9xkCZQTl" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/925c210871c06c63739019f77f5dcfe65cd9e4ef_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/925c210871c06c63739019f77f5dcfe65cd9e4ef.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/925c210871c06c63739019f77f5dcfe65cd9e4ef.png 2x" data-dominant-color="555775"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20to40mean-side</span><span class="informations">820×500 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
</blockquote>
<p>If there is anything I misunderstood or any mistake I made during the process, any advice or guide in the right direction will be much appreciated.</p>
<p>Best regards,</p>
<p>Yuyoung</p>

---

## Post #2 by @anasmh101 (2025-07-08 03:21 UTC)

<aside class="quote no-group" data-username="Yuyoung" data-post="1" data-topic="29084">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/eada6e/48.png" class="avatar"> Yuyoung:</div>
<blockquote>
<p>Used <strong>Population Analysis Module</strong> to extract the mean model for each age group with the output files from step 1.</p>
</blockquote>
</aside>
<p>Hello may I ask you , how did you extract the mean model for each group ? can you please explain the steps ?</p>

---
