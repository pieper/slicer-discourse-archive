---
topic_id: 48950
title: "Idea for a new extension: 3D organoid analysis in Slicer"
date: 2026-11-18
url: https://discourse.slicer.org/t/48950
last_bumped: 2026-11-18T20:29:50.529Z
---

# Idea for a new extension: 3D organoid analysis in Slicer

**Topic ID**: 48950
**Date**: 2026-11-18
**URL**: https://discourse.slicer.org/t/idea-for-a-new-extension-3d-organoid-analysis-in-slicer/48950

---

## Post #1 by @Roya_Khajavi (2026-11-18 04:02 UTC)

<p>Hi all,</p>
<p>I’d like to suggest an extension that I think fills a real gap, in case it interests a developer, student or lab looking for a project.</p>
<p><strong>The gap:</strong> Organoids are lab-grown 3D mini-tissues used widely in cancer research, drug screening and developmental biology. More and more of them are imaged in true 3D and over time with light-sheet and confocal microscopy. Most organoid analysis tools today focus on 2D brightfield images (OrganoID, OrgaQuant, napari plugins). The main 3D tool I know of is the Fiji plugin Deforming Mesh 3D (Smith et al., Biophysical Journal 2023). As far as I can tell, Slicer has no organoid workflow, even though it already has most of the building blocks:</p>
<ul>
<li>Volumetric segmentation (Segment Editor, nnInteractive, MONAI Label)</li>
<li>Shape statistics and radiomics</li>
<li>Sequences for time-lapse data</li>
<li>Mesh/model handling for 3D surfaces</li>
</ul>
<p><strong>What a first version could do:</strong></p>
<ul>
<li>Import 3D microscopy stacks (OME-TIFF / Zarr) with correct voxel spacing</li>
<li>Segment whole organoids and/or individual cells using existing AI tools</li>
<li>Report per-organoid measurements: volume, surface area, sphericity, lumen size, and cell counts</li>
<li>Track growth over time</li>
<li>Import existing segmentation meshes (e.g. from DM3D) for comparison and further analysis</li>
</ul>
<p><strong>Ready-to-use public data with ground truth:</strong> Zenodo record 7544194 (CC BY 4.0) contains 3D time-lapse light-sheet images of mouse mammary organoids, plus cell segmentation meshes and trained models from the paper above. That makes it a good test and validation set from day one. Zenodo 4419984 (pancreatic and bile-duct cancer organoids, light-sheet) is another option.</p>
<p><strong>Why it could be a good project:</strong></p>
<ul>
<li>Well scoped for NA-MIC Project Week or a student or summer project</li>
<li>A clear publication opportunity (e.g. a tools/software paper)</li>
<li>Would bring Slicer to the growing organoid and microscopy community</li>
</ul>
<p><strong>How I can help:</strong> I’m not in a position to lead development, but I have a background in medical-imaging AI and segmentation. I’m happy to help with testing, feedback, finding datasets, and connecting with potential users.</p>
<p>Is anyone already working on something similar, or interested in picking this up? Do the core developers think it’s a good fit for Project Week?</p>
<p>Thanks!<br>
Roya</p>

---

## Post #2 by @muratmaga (2026-11-18 04:34 UTC)

<p>I think this would be a good project for PW, and I think it will be easier to implement than you think, particularly with the new ome-zarr extension it is now very straightforward to import ome-zarr into Slicer.</p>
<p>There is no AI model trained on organoid, but generic prompt-based segmentation via NNInteractive should get you there. Everything else is already available in Slicer (surface/volume calculations, reporting etc).</p>
<p>I am not sure about the extension angle, but it is more a putting together an end to end workflow, which should be easy (or at least easier) with the help of LLM and slicer-skill (<a href="https://github.com/pieper/slicer-skill" class="inline-onebox" rel="noopener nofollow ugc">GitHub - pieper/slicer-skill: SKILLS.md style information for slicer programing and usage · GitHub</a>)</p>

---

## Post #3 by @Roya_Khajavi (2026-11-18 05:26 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="48950">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/83011_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>g else is already available in Slicer (surface/volume calculations, reporting etc).</p>
<p>I am not sure about the extension angle, but it is more a putting together an end to end workflow, which should be easy (or at least easier) with the help of LLM and slicer-skill ( <a href="https://github.com/pieper/slicer-skill" class="inline-onebox" rel="noopener nofollow ugc">GitHub - pieper/slicer-skill: SKILLS.md style information for slicer programing and usage · GitHub</a> )</p>
</blockquote>
</aside>
<p>Thanks, Murat, that’s really helpful and encouraging! Framing it as an end-to-end workflow (OME-Zarr import → nnInteractive segmentation → existing measurement and reporting tools) rather than a new extension makes a lot of sense and lowers the bar quite a bit.</p>
<p>If anyone is looking for a Project Week project and finds this interesting, please feel free to pick it up. The public datasets above should be a good starting point.</p>

---

## Post #4 by @muratmaga (2026-11-18 06:28 UTC)

<p>I am not sure if there are developers who are looking additional project. Most likely, they might give a hand when you need it, but almost everyone is busy with their own project. As such, I highly encourage you to attend and do this yourself. Most success stories happen when stakeholders and people who need the tools drive (or help it to drive) their development.</p>

---

## Post #5 by @Roya_Khajavi (2026-11-18 06:44 UTC)

<p>Thanks, Murat; that’s fair and very helpful advice. I’ll take this on and work toward a prototype workflow you mentioned, to bring it to an upcoming Project Week. I’ll post updates here as it progresses, and I may reach out with questions along the way.</p>

---

## Post #6 by @curtislisle (2026-11-18 20:11 UTC)

<p>Dear Roya,</p>
<p>I am interested in your application.  I plan to be imaging organoids in a few months and am experienced in 3D Slicer.  I’d be interested in helping / collaborating as you develop this workflow for processing organoid imagery in Slicer.  Unfortunately, I don’t plan to attend Project Week this January either, but I am in the Slicer community and would be willing to participate on your project.  I can be reached by email directly at <a href="mailto:clisle@knowledgevis.com">clisle@knowledgevis.com</a></p>
<p>Curtis Lisle</p>
<p>Principal AI/ML Engineer, NIAID</p>

---

## Post #7 by @Roya_Khajavi (2026-11-18 20:28 UTC)

<p>(post deleted by author)</p>

---

## Post #8 by @Roya_Khajavi (2026-11-18 20:29 UTC)

<p>Thank you, Curtis, that’s wonderful! I’d be very glad to collaborate. I’ll follow up with you by email to coordinate next steps, and we’ll share progress here and on the Project Week page (<a href="https://github.com/NA-MIC/ProjectWeek/issues/1826" class="inline-onebox" rel="noopener nofollow ugc">Project: 3D Organoid Analysis Workflow in Slicer · Issue #1826 · NA-MIC/ProjectWeek · GitHub</a>).</p>

---
