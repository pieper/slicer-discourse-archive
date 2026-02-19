---
topic_id: 43644
title: "Population Analysis Output"
date: 2025-07-08
url: https://discourse.slicer.org/t/43644
---

# Population Analysis Output

**Topic ID**: 43644
**Date**: 2025-07-08
**URL**: https://discourse.slicer.org/t/population-analysis-output/43644

---

## Post #1 by @anasmh101 (2025-07-08 09:25 UTC)

<p>Hello everyone,</p>
<p>I’m currently working on a project that involves analyzing bone apposition and resorption in mandibular condyles by comparing pre-treatment and post-treatment CBCT scans.</p>
<p>Here’s what I’ve done so far:</p>
<ol>
<li>
<p>I performed rigid alignment for the pre- and post-treatment condyle segmentations.</p>
</li>
<li>
<p>I ran SPHARM-PDM on all segmented models (pre and post).</p>
</li>
<li>
<p>Using population analysis module I created a CSV file to define the pre- and post-treatment groups then clicked the <strong>“Process and Export”</strong> button.</p>
</li>
</ol>
<p>However, the output in the 3D viewer shows a dark, unrecognizable model with no clear shape as shown in screenshot</p>
<p>Did I miss something in the workflow or setup? I’d really appreciate any guidance or suggestions on what might be going wrong.<br>
Thanks in advance!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fef91da78f53e8052188af45d2b1fab17c7fa33.jpeg" data-download-href="/uploads/short-url/97Bm69l33fiD7yOlI5E5rsGKjJh.jpeg?dl=1" title="Population Analysis" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fef91da78f53e8052188af45d2b1fab17c7fa33_2_690x431.jpeg" alt="Population Analysis" data-base62-sha1="97Bm69l33fiD7yOlI5E5rsGKjJh" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fef91da78f53e8052188af45d2b1fab17c7fa33_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fef91da78f53e8052188af45d2b1fab17c7fa33_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fef91da78f53e8052188af45d2b1fab17c7fa33_2_1380x862.jpeg 2x" data-dominant-color="878E95"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Population Analysis</span><span class="informations">1920×1200 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @styner (2025-07-10 07:55 UTC)

<p>Hi Anash<br>
The dark color of the average model shown in the screenshot might be an issue of surface normal flipping. If you use the “models” module, you should be able to select that surface and under 3D Display → Visible Sides, it should say “All”. If not please, switch to All.<br>
Some quick questions<br>
After step 2, did the model surfaces look fine? Did you double check the correspondence in Shape Population Viewer to see that there are no flipped correspondences?<br>
Best<br>
Martin</p>

---

## Post #3 by @anasmh101 (2025-07-10 14:24 UTC)

<p>Hi Martin,</p>
<p>Thanks again for your help!</p>
<p>I checked the correspondences in Shape Population Viewer as shown in the screenshot, and it seems there <strong>is</strong> an issue with the correspondence.</p>
<p>May I ask how I can solve this?</p>
<p>Just to add some context — I’m using the <code>.vtk</code> files named <code>surf_SPHARM_ellalign.vtk</code>.</p>
<p>Best regards,<br>
Anas<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a8d7479151a70bc461a16762eaea74f581a55bc.jpeg" data-download-href="/uploads/short-url/m3eAYiaRnonZVTz9ulrCdhMX6qg.jpeg?dl=1" title="Correspondence" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a8d7479151a70bc461a16762eaea74f581a55bc_2_690x431.jpeg" alt="Correspondence" data-base62-sha1="m3eAYiaRnonZVTz9ulrCdhMX6qg" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a8d7479151a70bc461a16762eaea74f581a55bc_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a8d7479151a70bc461a16762eaea74f581a55bc_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a8d7479151a70bc461a16762eaea74f581a55bc_2_1380x862.jpeg 2x" data-dominant-color="645772"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Correspondence</span><span class="informations">1920×1200 285 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @styner (2025-07-10 14:49 UTC)

<p>Thanks Anas<br>
To solve the issue with the correspondence, let’s first outline what the issue is:</p>
<ol>
<li>Is the correspondence issue mainly a flip (or multiple flips) along one of the main axes, e.g. front-back flip, top-bottom flip, left-right flip? If so, then those flips can be added manually to the SPHARM-PDM generation module  (SPHARM-PDM has issues with correspondence if the shape of structure is not elongated and more spherical in a first order approximation, this seems to be the case here)</li>
</ol>
<ol start="2">
<li>If the correspondence issue is more complex, e.g. the correspondence is off by a 30 degree rotation of the phi or theta visualization, then at least 3 fiducials/landmarks on all objects will be needed as input the Correspondence Improvement module</li>
</ol>
<p>hope this helps<br>
Martin</p>

---

## Post #5 by @anasmh101 (2025-07-10 17:52 UTC)

<p>Hi Martin,</p>
<p>Thanks a lot again for your continued support</p>
<p>I’ve re-run the SPHARM-PDM process using landmarks to improve the correspondence. Each fiducial file matches the name of its respective condyle, and the landmarks have consistent names and sequences across all models.</p>
<p>Unfortunately, the correspondence issue still persists.</p>
<p>Just to clarify: I processed all pre- and post-treatment condyle segmentations together in a single batch. Since you mentioned that the flip can be manually controlled during SPHARM-PDM generation, I’m now considering running SPHARM-PDM for each <strong>pre/post pair individually</strong> so I can better control the flipping.</p>
<p>If I do it that way, would I still be able to perform <strong>population analysis and PCA</strong> later on using the full set of 50 models?</p>
<p>If not, how can I control the flipping when processing all 25 pre- and 25 post-treatment segmentations together? Specifically, how do I determine the correct <strong>starting point (axis: X, Y, or Z)</strong> to fix the flipping and end up with consistently aligned models?</p>
<p>Thanks again for your help — your guidance is really appreciated!</p>
<p>Best,<br>
Anas</p>

---
