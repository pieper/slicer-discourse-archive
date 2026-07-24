---
topic_id: 47723
title: "Measuring per-tooth displacement between serial intraoral scans - which modules?"
date: 2026-07-23
url: https://discourse.slicer.org/t/47723
last_bumped: 2026-07-23T12:31:26.534Z
---

# Measuring per-tooth displacement between serial intraoral scans - which modules?

**Topic ID**: 47723
**Date**: 2026-07-23
**URL**: https://discourse.slicer.org/t/measuring-per-tooth-displacement-between-serial-intraoral-scans-which-modules/47723

---

## Post #1 by @Alla_Belova (2026-07-23 12:31 UTC)

<p>Hi all — I’m a dentist working on a PhD metrology project and I kindly ask for your help to build an efficient protocol for measuring tooth displacement in time.</p>
<p><strong>The data:</strong> five surface meshes (STL) of the same mandibular arch, scanned intraorally at different timepoints (baseline, immediately after splinting, then 1, 3 and 6 months). The lower anterior segment (six teeth) is splinted, and I want to measure whether/how it moves over time while treating the posterior teeth as a stable reference.</p>
<p><strong>What I want to measure:</strong></p>
<ul>
<li>Rigid, whole-surface <strong>best-fit superimposition</strong> (no scaling), registered on the <em>posterior</em> teeth as the stable region.</li>
<li><strong>Per-landmark displacement</strong> for six anterior points — signed components along vestibulo-oral / mesio-distal / vertical axes (ΔX, ΔY, ΔZ) and the 3D resultant ΔR — not just a scalar surface distance.</li>
<li>Each point’s <strong>perpendicular deviation from a curve</strong> fitted through the six landmarks at baseline (landmarks: incisal-edge midpoints on the incisors, cusp tips on the canines).</li>
<li>From 15 repeat scans my method noise is ~0.08 mm, so I’m working close to that limit.</li>
</ul>
<p><strong>What I’m looking at in Slicer</strong> (and where I’d love guidance):</p>
<ul>
<li><strong>Markups</strong> for the points, and a Markups <strong>Curve</strong> for the anterior curve — is that the right way to trace and measure deviation from it?</li>
<li><strong>Model Registration / SurfaceToolbox</strong> vs. the <strong>Model-to-Model Distance</strong> extension — which gives me <em>signed per-axis</em> displacement rather than only closest-point distance?</li>
<li><strong>SlicerMorph</strong> (and <strong>ALPACA</strong>) for placing/transferring the landmarks consistently across the five timepoints — worth it here, or overkill for six points?</li>
</ul>
<p><strong>Specific questions:</strong></p>
<ol>
<li>How do I constrain the best-fit to register on the posterior sub-region while measuring the anterior segment?</li>
<li>What’s the cleanest way to get <strong>per-axis (X/Y/Z) components</strong> of each landmark’s movement between timepoints?</li>
<li>Automated landmark transfer across scans vs. manual picking — what would you recommend at this scale and precision?</li>
<li>Is there a way to automate the whole process (ex. write a code)?</li>
</ol>
<p>Screenshot of the marked reference points and the traced anterior curve below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/758e5f13b756e84c8f24961503b068fe7c2bdcaa.jpeg" data-download-href="/uploads/short-url/gLWTo20eVJjt2YLBDkqP02fyOMy.jpeg?dl=1" title="reference points_curve" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/758e5f13b756e84c8f24961503b068fe7c2bdcaa_2_689x367.jpeg" alt="reference points_curve" data-base62-sha1="gLWTo20eVJjt2YLBDkqP02fyOMy" width="689" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/758e5f13b756e84c8f24961503b068fe7c2bdcaa_2_689x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/758e5f13b756e84c8f24961503b068fe7c2bdcaa_2_1033x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/758e5f13b756e84c8f24961503b068fe7c2bdcaa.jpeg 2x" data-dominant-color="E9E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">reference points_curve</span><span class="informations">1240×661 76.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ade341cf8ab125f1beea897083b770bcc6259303.jpeg" data-download-href="/uploads/short-url/oOhuTVJBikogo1r6UJCIylClaOD.jpeg?dl=1" title="reference points" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ade341cf8ab125f1beea897083b770bcc6259303_2_689x367.jpeg" alt="reference points" data-base62-sha1="oOhuTVJBikogo1r6UJCIylClaOD" width="689" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ade341cf8ab125f1beea897083b770bcc6259303_2_689x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ade341cf8ab125f1beea897083b770bcc6259303_2_1033x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ade341cf8ab125f1beea897083b770bcc6259303.jpeg 2x" data-dominant-color="E9E7E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">reference points</span><span class="informations">1240×661 68.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Any help is appreciated. Many thanks!</p>

---
