# How to export distances between anatomical landmarks

**Topic ID**: 23489
**Date**: 2022-05-19
**URL**: https://discourse.slicer.org/t/how-to-export-distances-between-anatomical-landmarks/23489

---

## Post #1 by @MrMarkus (2022-05-19 13:47 UTC)

<p>Operating system:win10<br>
Slicer version: r29738</p>
<p><strong>Dear slicerMorph user,</strong></p>
<p>I am wondering if there is a way to export the dimensions between anatomical<br>
landmarks.</p>
<p><em>General worklfow in slicerMorph</em></p>
<ul>
<li>List item data acquisition</li>
<li>List item model generation</li>
<li>List item generate landmarks</li>
<li>List item populate landmarks across samples</li>
</ul>
<p>And at this step it would be great if there would be an option to export for each sample<br>
the dimensions between the established landmarks. In that way one would have the possibility<br>
to obtain information about dimension/length/width/… of e.g. skull, mandible…<br>
in addition to procrustes analysis and PCA;<br>
This would enable  “intuitive” information, as a first step, like: skull A large than skull B,… instead of<br>
shape variation across PC1…</p>
<p><strong>Is there a way to retrieve such an information and implement batch export of the resulting dimensions between the landmarks?</strong></p>
<p>Best,<br>
Markus</p>

---

## Post #2 by @muratmaga (2022-05-19 14:38 UTC)

<p>In Markups module, you can highlight any two points (markups) in the control list and then right click to obtain the distance between them.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea7b9897a50ac8fe94a1d66cc67ca9c84b993683.png" data-download-href="/uploads/short-url/xskwWOPoGqkUEwf6PoUhW9aVEtB.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea7b9897a50ac8fe94a1d66cc67ca9c84b993683_2_345x216.png" alt="image" data-base62-sha1="xskwWOPoGqkUEwf6PoUhW9aVEtB" width="345" height="216" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea7b9897a50ac8fe94a1d66cc67ca9c84b993683_2_345x216.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea7b9897a50ac8fe94a1d66cc67ca9c84b993683_2_517x324.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea7b9897a50ac8fe94a1d66cc67ca9c84b993683_2_690x432.png 2x" data-dominant-color="DEE2E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1098×688 39.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Beyond that it is hard to generalize what you asked, because it all depends on how you measure the skull width/length (which landmarks, what order). You can develop that as a simple python script for your data. Let us know if you need examples.</p>
<p>Also simple distance measures are rarely useful by themselves. Because if a skull is larger or wider than the others, it usually will be observable. Ratios of those linear measurements can be more informative about the shape differences as it will indicate proportional changes.</p>

---

## Post #3 by @MrMarkus (2022-05-19 16:14 UTC)

<p>Thanks for the feedback.</p>
<p>Following example:</p>
<ul>
<li>List item estimate / categorize cases of “Brachycephalie”</li>
<li>List item Brachycephalie could be defined as ratio: width/lenght</li>
</ul>
<p>Now assume that the following 9 anatomical landmarks were established accross the cohort,<br>
(ref.: <a href="https://getahead.la.psu.edu/landmarks/viewer/?id=Adult_Mouse_Skull" class="inline-onebox" rel="noopener nofollow ugc">Viewer – Richtsmeier Laboratory</a>)</p>
<ol>
<li>Center of alveolar ridge over maxillary incisor, left side</li>
<li>Center of alveolar ridge over maxillary incisor, right side</li>
<li>Anterior-most point at intersection of premaxillae and nasal bones, left side</li>
<li>Anterior-most point at intersection of premaxillae and nasal bones, right side</li>
<li>Intersection of parietal, temporal and interparietal bones, left side</li>
<li>Intersection of parietal, temporal and interparietal bones,right side</li>
<li>Bregma: intersection of frontal bones and parietal bones at midline</li>
<li>Intersection of parietal bones with anterior aspect of interparietal bone at midline</li>
<li>Intersection of interparietal bones with squamous portion of occipital bone at midline</li>
</ol>
<p>If I am not mistaken 36 distances between these 9  points can be measured.</p>
<p>Workflow:</p>
<ul>
<li>
<p>List item set the 9 landmarks</p>
</li>
<li>
<p>List item use ALPACA workflow to transfer these 9 landmarks to the samples of interest</p>
</li>
<li>
<p>List item once the individual transformations are established (ALPACA strength) export for each sample the 36 distances for the applied 9 landmarks</p>
</li>
<li>
<p>List item use additional software to load the distances of the samples and perform computation/analysis/visualization (e.g. box plot / mean+/-sdt. of specific distance … ect.)</p>
</li>
</ul>
<p>Would this be feasible?</p>

---

## Post #4 by @muratmaga (2022-05-19 19:56 UTC)

<p>I would approach this differently and focus only automating the measurement and displaying results (the last item on your list). Everything else (eg ALPACA) is pretty streamlined and automatic anyways (only takes about 10 clicks or so once you define you templates and points).</p>
<p>Estimating pairwise distances from point list is straightforward, and so is converting them ratios and even plotting them. Check the sample script repository on how to read and work with Markups <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html?highlight=script#markups" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>
<p>and these are plotting examples. <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html?highlight=script#plots" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>

---

## Post #5 by @MrMarkus (2022-05-30 12:46 UTC)

<p>Hi,</p>
<p>one result of ALPACA pipeline are the resulting transformed landmarks; these results are stored as *.fcsv; currently these results/transformed coordinates are used to obtain the distances between each landmark coordinate.<br>
For this step additional software is used which loads the *.fcsv file and computes the distances between all landmarks.</p>
<p>This approach works fine and not additinal scripting in slicerMorph is required.</p>

---

## Post #6 by @muratmaga (2022-05-30 20:44 UTC)

<aside class="quote no-group" data-username="MrMarkus" data-post="5" data-topic="23489">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> MrMarkus:</div>
<blockquote>
<p>This approach works fine and not additinal scripting in slicerMorph is required.</p>
</blockquote>
</aside>
<p>Yes, if you are going to do pairwise distance calculation outside of Slicer, you don’t need to do any scripting with Slicer. Everything else to that point is pretty straighforward, and detailed in our tutorials.</p>

---
