---
topic_id: 48950
title: "Idea for a new extension: 3D organoid analysis in Slicer"
date: 2026-11-18
url: https://discourse.slicer.org/t/48950
last_bumped: 2026-11-26T02:53:07.338Z
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

## Post #8 by @Roya_Khajavi (2026-11-18 20:29 UTC)

<p>Thank you, Curtis, that’s wonderful! I’d be very glad to collaborate. I’ll follow up with you by email to coordinate next steps, and we’ll share progress here and on the Project Week page (<a href="https://github.com/NA-MIC/ProjectWeek/issues/1826" class="inline-onebox" rel="noopener nofollow ugc">Project: 3D Organoid Analysis Workflow in Slicer · Issue #1826 · NA-MIC/ProjectWeek · GitHub</a>).</p>

---

## Post #9 by @qiang1900 (2026-11-25 12:37 UTC)

<p>hi, Roya, I did a research and wonder those existing extensions/plugins may already covered some/most of the gap in Slicer, or could use some them as integration partners instead of re-inventing ourself. Worth to take a look first, then either adjust the proposed project scope or have a off the shelf solution from those:</p>
<ul>
<li><strong>OrganoidTracker:</strong> specifically addresses 3D cell tracking, lineage reconstruction and manual correction, with error estimates that help prioritize review. This is a potential integration partner, not something to rebuild casually. <a href="https://organoidtracker.org/" rel="noopener nofollow ugc">Project (https://organoidtracker.org/)</a></li>
<li><strong>3DCellScope:</strong> performs multilevel analysis of nuclei, cells and whole organoids, including morphological and topological measurements. It directly overlaps much of the proposed functionality. <a href="https://github.com/quantacell/3DcellScope" rel="noopener nofollow ugc">Repository (https://github.com/quantacell/3DcellScope)</a>, <a href="https://www.nature.com/articles/s41592-025-02685-4" rel="noopener nofollow ugc">2025 paper (https://www.nature.com/articles/s41592-025-02685-4)</a></li>
<li><strong>Tapenade:</strong> provides 3D organoid preprocessing, nuclei analysis and spatial quantification through Python and napari interfaces. The characterization of napari as primarily 2D misses this work. <a href="https://github.com/GuignardLab/tapenade" rel="noopener nofollow ugc">Repository (https://github.com/GuignardLab/tapenade)</a></li>
<li><strong>SlicerOMEZarr:</strong> already imports multiscale images, labels, channels and time sequences, with memory-budgeted resolution selection and region refinement. Evaluate and reuse it before proposing another Zarr reader. Its documented capabilities still need verification on the chosen datasets. <a href="https://github.com/fideus-labs/SlicerOMEZarr" rel="noopener nofollow ugc">Repository (https://github.com/fideus-labs/SlicerOMEZarr)</a></li>
</ul>
<p>Cheers</p>
<p>Qiang</p>

---

## Post #10 by @Roya_Khajavi (2026-11-25 17:40 UTC)

<aside class="quote no-group" data-username="qiang1900" data-post="9" data-topic="48950">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/q/f19dbf/48.png" class="avatar"> qiang1900:</div>
<blockquote>
<p>hi, Roya, I did a research and wonder those existing extensions/plugins may already covered some/most of the gap in Slicer, or could use some them as integration partners instead of re-inventing ourself. Worth to take a look first, then either adjust the proposed project scope or have a off the shelf solution from those:</p>
<ul>
<li><strong>OrganoidTracker:</strong> specifically addresses 3D cell tracking, lineage reconstruction and manual correction, with error estimates that help prioritize review. This is a potential integration partner, not something to rebuild casually. <a href="https://organoidtracker.org/" rel="noopener nofollow ugc">Project (https://organoidtracker.org/)</a></li>
<li><strong>3DCellScope:</strong> performs multilevel analysis of nuclei, cells and whole organoids, including morphological and topological measurements. It directly overlaps much of the proposed functionality. <a href="https://github.com/quantacell/3DcellScope" rel="noopener nofollow ugc">Repository (https://github.com/quantacell/3DcellScope)</a>, <a href="https://www.nature.com/articles/s41592-025-02685-4" rel="noopener nofollow ugc">2025 paper (https://www.nature.com/articles/s41592-025-02685-4)</a></li>
<li><strong>Tapenade:</strong> provides 3D organoid preprocessing, nuclei analysis and spatial quantification through Python and napari interfaces. The characterization of napari as primarily 2D misses this work. <a href="https://github.com/GuignardLab/tapenade" rel="noopener nofollow ugc">Repository (https://github.com/GuignardLab/tapenade)</a></li>
<li><strong>SlicerOMEZarr:</strong> already imports multiscale images, labels, channels and time sequences, with memory-budgeted resolution selection and region refinement. Evaluate and reuse it before proposing another Zarr reader. Its documented capabilities still need verification on the chosen datasets. <a href="https://github.com/fideus-labs/SlicerOMEZarr" rel="noopener nofollow ugc">Repository (https://github.com/fideus-labs/SlicerOMEZarr)</a></li>
</ul>
<p>Cheers</p>
</blockquote>
</aside>
<hr>
<p>Hi Qiang,</p>
<p>Thank you for taking the time to look into this. It’s really useful, and a fair correction on napari; I undersold Tapenade and the 3D work there.</p>
<p>I agree the goal shouldn’t be to rebuild what already exists, so I’ll adjust the scope. For import, we’ll use SlicerOMEZarr rather than writing a new reader, as Murat also suggested, and test it on the Zenodo light-sheet datasets to confirm it handles their time series and voxel spacing correctly. The focus will be on what Slicer adds: an interactive end-to-end workflow that brings together nnInteractive segmentation, 3D and time-lapse visualization with Sequences, and shape and radiomics measurements, rather than duplicating standalone pipelines.</p>
<p>I also looked more closely at the tools you mentioned, and they fit in naturally as partners. Tapenade is a pip-installable Python library, so we can try calling its preprocessing and StarDist3D nuclei segmentation directly from Slicer’s Python environment and load the resulting label maps as segmentations. OrganoidTracker stores its tracks as JSON (.aut files) and exports TrackMate XML and Cell Tracking Challenge formats, so a lightweight importer could bring its tracks and lineages into Slicer as time-varying markups alongside the image sequence. 3DCellScope we’ll use as a reference point, comparing its organoid-level measurements with ours on the same dataset.</p>
<p>I’ll update the Project Week page (<a href="https://github.com/NA-MIC/ProjectWeek/issues/1826" class="inline-onebox" rel="noopener nofollow ugc">Project: 3D Organoid Analysis Workflow in Slicer · Issue #1826 · NA-MIC/ProjectWeek · GitHub</a>) to reflect this. You clearly know this space well, and it would be great to have you on the project. Curtis Lisle has also offered to help, so please feel free to join us at whatever level suits you.</p>
<p>Thanks again,<br>
Roya</p>

---

## Post #11 by @qiang1900 (2026-11-26 02:53 UTC)

<p>hi <a class="mention" href="/u/roya_khajavi">@Roya_Khajavi</a> ,</p>
<p>Nice to hear from you. I can dig into Tapenade, OrganoidTracker, and SlicerOMEZarr deeper to see would they fit well into the 3D organoid project or not, by running those on my end.</p>
<p>One question, do you currently have a lab machine which is planned for the eventual Slicer integration?</p>
<p>Second, do you have a plan on where to host the project’s code repo, and other relevant questions like Slicer maintainer, test operator, repo owner and data permissions? I recommend a new, standalone public GitHub repository controlled either by you or a neutral Slicer-community organization. If those not yet determined for now, may bring those for discussion in this group chat and on the ProjectWeek site.</p>
<p>Lastly, you can send an invite to my github acct <a href="https://github.com/qmandev" rel="noopener nofollow ugc">qmandev</a> so I can join ProjectWee’s project.</p>
<p>Have a wonderful Thanks Giving!</p>
<p>Qiang</p>

---
