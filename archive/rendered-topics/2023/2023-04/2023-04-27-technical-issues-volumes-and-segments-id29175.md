---
topic_id: 29175
title: "Technical Issues Volumes And Segments"
date: 2023-04-27
url: https://discourse.slicer.org/t/29175
---

# Technical issues volumes and segments

**Topic ID**: 29175
**Date**: 2023-04-27
**URL**: https://discourse.slicer.org/t/technical-issues-volumes-and-segments/29175

---

## Post #1 by @Ennio_Russo_Clarisci (2023-04-27 15:12 UTC)

<p>Hi everybody,</p>
<p>I am a new Slicer user with no competence in Python scripting. I am carrying out a project that aims to measure bone densities (in terms of Hounsfield) from concentric cylindrical sections. To this aim, a series of concentric hollow tubes was built in FreeCad and imported in Slicer. The tubes were created calculating inner and outer radius so that the tube volume was constant irrespective of the distance from the center. Therefore, the thickness of the more external tube is progressively lower than the inner tube. For each distance, 10 replicate tubes are available.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a7db5ccb84e26a8b0858593af5eeb19d8374175.png" alt="Cylinder" data-base62-sha1="8lr1C8GYMx4qmoQlOnhRIjr9h2J" width="172" height="167"></p>
<p>After importing the bone volume in Slicer, the respective segment was obtained. Each tube (.stl) was imported in Slicer as Segmentation. The tubes have specific coordinates that guarantee an a priori defined overlapping with the bone segment. To obtain the actual bone region overlapping with the tube, the bone segment and the tube have been intersected and the statistics was calculated.</p>
<p>Since the results from Slicer were somehow unexpected, some technical trials were performed. Firstly, it was checked if the volume of the tube exported from FreeCad was preserved in Slicer. To this purpose, the tubes were imported in Slicer as Segments. To calculate their volume, the option “Specify Geometry” from the “Segment Editor” Module was selected and the respective volume was created. Subsequently, the statistics was calculated. Here is the output obtained from Slicer for the tubes of a specific distance. Also, the volume is compared to the expected value from FreeCad (also confirmed through hand calculation).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/9867811b044b5c76504f7767bb37447c823bbfe2.png" alt="Tabella 1" data-base62-sha1="lKekC5aRrMxKlpildXupkR6Q64O" width="479" height="287"></p>
<p><strong>A first question is: why does Slicer calculate tube volumes differently than another software and in a different way according to the site? What am I doing wrong?</strong></p>
<p>After these results, a further technical check was made. In FreeCad, two cubes and two cylinders with a specified volume were created. One cube had the exact half of the volume of the first cube and the same was true for tubes. These shapes (.stl) were imported in Slicer as Segment. The volume was obtained with function “Specify Geometry” as described before.</p>
<p>At first, the volume was calculated for each geometric shape separately.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d923c963917a0254e9149352fbf51996288b2343.png" alt="Tabella 2" data-base62-sha1="uYUhAumkDkvQi5Q2vwLDglXtwgX" width="429" height="81"></p>
<p>While the cube/2 is the exact half of the cube as expected, the volume of the tube/2 is not the half of the tube: 23.4487/2=11.72435. The discrepancy from the expected value is about 0.11%.<br>
Volume was then calculated after intersecting the cube in cube/2 and the tube in tube/2. Therefore, the expected volumes were the cube/2 and the tube/2. Here are the results.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3ab72141fb8cc43327fd81e9fd19ef1758c9c6b2.png" alt="Tabella 3" data-base62-sha1="8nq2VSyjtAXHFainKRtxl1DYSf8" width="403" height="99"></p>
<p>Volumes appear definitely not the expected ones.</p>
<p><strong>From these results the following questions:</strong></p>
<p><strong>Why is the volume of the tube/2 not completely the half of the tube as expected? Why does the tube behave differently from the cube? Is there a bias in the results from Slicer depending on the shapes considered?</strong></p>
<p><strong>Why do I obtain such different results after intersecting the segments? Could this operation affect my results also during the experimental phase?</strong></p>
<p>One last unclear point arose when working on the volumes and segment that I should analyze for my experiment.<br>
Here is an example output collected after intersecting the tube with the bone volume of interest.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/630732702a1ea54a6a85c986c4253552bcb364b5.png" data-download-href="/uploads/short-url/e82GJ0jOa25z2XdZ8ZIBRVTeonz.png?dl=1" title="segments" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/630732702a1ea54a6a85c986c4253552bcb364b5_2_477x500.png" alt="segments" data-base62-sha1="e82GJ0jOa25z2XdZ8ZIBRVTeonz" width="477" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/630732702a1ea54a6a85c986c4253552bcb364b5_2_477x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/630732702a1ea54a6a85c986c4253552bcb364b5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/630732702a1ea54a6a85c986c4253552bcb364b5.png 2x" data-dominant-color="D5D7E9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segments</span><span class="informations">657×688 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The red segment is the tube and the green segment is the bone intersected with the tube. The statistics is as follows.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf8d38339a4e7d173cecb7380ba3ac309d31125c.png" alt="Statistics1" data-base62-sha1="rkxL0YHTA6R2Soz6hP27w3oiwIA" width="647" height="73"></p>
<p>In this case, the two rows are identical, indicating that the intersected segments are exactly the same. However, this holds not true for all the sites measured considering a specific tube. For example, at the measurement site 7, the intersection shows segments that do not perfectly overlap and thus show different statistics.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf4d5eb3664c0419ac4632c5e91574edb169183f.png" alt="Segment and statistics" data-base62-sha1="tzSBf1tV7gDGtWQcYIFMtjFnaCH" width="666" height="267"></p>
<p><strong>The question now is:</strong></p>
<ul>
<li><strong>Why do the two segments not intersect perfectly in this occasion? The procedure was the same followed for other sites, but the result was different.</strong></li>
<li><strong>Is it expected that the intersection process retrieves two identical segments?</strong></li>
<li><strong>Also, it is not clear to me what the statistics value refer to, why do I observe multiple columns with volume values that differ one from the other?</strong></li>
</ul>
<p>I thank you in advance for any suggestion that you may want to share.</p>
<p>Best</p>
<p>Ennio</p>

---

## Post #2 by @pieper (2023-04-27 17:51 UTC)

<p>Sorry for not taking the time to digest your full set of questions, but on the first point about cubes and tubes having different volumes, I believe you can explain this as the difference because your cad program probably works on curved surfaces but then you exported triangulated surface (stl) that are just a piecewise linear approximation of a tube, but an exact description of the cube.</p>
<p>Similarly for your second set of questions you may be seeing issues related to discretization when going from surface models to volumes.</p>

---

## Post #3 by @Ennio_Russo_Clarisci (2023-04-28 08:04 UTC)

<p>Dear Dr. Pieper,</p>
<p>thank you for your kind and brisk reply. I see your point and this would justify the discrepancy of 0.11% when measuring the tube/2 volume.</p>
<p>Do you have by chance the possibility to help me with the last point about the weird intersection of the two segments?</p>
<p>Thank you very much<br>
Best<br>
Ennio</p>

---

## Post #4 by @pieper (2023-04-28 13:11 UTC)

<p>Hi Ennio -  I see you gave a lot of description and maybe there’s enough there to figure out what’s going on but I don’t really have time to dig in right now.  Perhaps someone else will be able to look through it and offer suggestions.  Best of luck.</p>

---

## Post #5 by @tsehrhardt (2023-04-29 00:49 UTC)

<p>Have you tried exporting your bone models out of Slicer and performing your intersections and calculations with another software using the tubes you made to see how the results compare?</p>

---

## Post #6 by @Ennio_Russo_Clarisci (2023-05-03 08:40 UTC)

<p>Thank you for suggestion. I thought about this other approach, but I did not put it into practice yet. Do you have any piece of software to recommend?</p>

---

## Post #7 by @tsehrhardt (2023-05-03 19:06 UTC)

<p>You can try Meshlab. It’s free and has lots of tools for mesh comparisons.</p>

---
