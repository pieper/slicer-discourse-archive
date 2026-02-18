# Workflow for FEM Simulation of Soft Tissue Deformation after Bimaxillary Surgery (using 3D Slicer + Open-Source Tools)

**Topic ID**: 44829
**Date**: 2025-10-20
**URL**: https://discourse.slicer.org/t/workflow-for-fem-simulation-of-soft-tissue-deformation-after-bimaxillary-surgery-using-3d-slicer-open-source-tools/44829

---

## Post #1 by @tschreiner (2025-10-20 18:04 UTC)

<p>Hi everyone,</p>
<p>I’m working on a project to <strong>simulate soft tissue deformation resulting from a bimaxillary (orthognathic) surgery</strong>.<br>
My goal is to model the <strong>soft tissue displacement and facial profile changes</strong> based on <strong>pre- and postoperative bone movements</strong>.</p>
<p>Here’s a video that illustrates what I’m trying to achieve:<br>
<img src="https://emoji.discourse-cdn.com/twitter/backhand_index_pointing_right.png?v=15" title=":backhand_index_pointing_right:" class="emoji" alt=":backhand_index_pointing_right:" loading="lazy" width="20" height="20"> <a href="https://www.youtube.com/watch?v=wqkXn2a4OGw" rel="noopener nofollow ugc">Soft Tissue Simulation after Orthognathic Surgery – Example</a></p>
<p>I’m planning to use <strong>3D Slicer</strong> for segmentation and model preparation, combined with <strong>open-source FEM tools</strong> such as <strong>Gmsh</strong>, <strong>FEBio</strong>, or <strong>CalculiX</strong> for the actual simulation.</p>
<p>I’d really appreciate any advice or shared experience on the following points:</p>
<hr>
<h3><a name="p-129335-h-1-data-preparation-in-3d-slicer-1" class="anchor" href="#p-129335-h-1-data-preparation-in-3d-slicer-1" aria-label="Heading link"></a>1. Data Preparation in 3D Slicer</h3>
<ul>
<li>Best workflow for segmenting <strong>bone and soft tissue</strong> regions (e.g., skin, mandible, maxilla).</li>
<li>Recommended export formats for meshing (<strong>STL</strong>, <strong>VTK</strong>, or direct <strong>tetrahedral volume meshes</strong>).</li>
<li>Methods for <strong>simplifying and cleaning</strong> the meshes before FEM processing (e.g., decimation, smoothing).</li>
</ul>
<hr>
<h3><a name="p-129335-h-2-meshing-and-boundary-setup-2" class="anchor" href="#p-129335-h-2-meshing-and-boundary-setup-2" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/gear.png?v=15" title=":gear:" class="emoji" alt=":gear:" loading="lazy" width="20" height="20"> 2. Meshing and Boundary Setup</h3>
<ul>
<li>Generating <strong>high-quality tetrahedral meshes</strong> (e.g. using <strong>Gmsh</strong>).</li>
<li>Defining <strong>boundary conditions</strong> based on the surgical bone movements (translation/rotation of the maxilla and mandible).</li>
<li>Assigning <strong>material properties</strong> (elastic, nonlinear, or viscoelastic) to different soft tissue layers.</li>
</ul>
<hr>
<h3><a name="p-129335-h-3-fem-simulation-tools-3" class="anchor" href="#p-129335-h-3-fem-simulation-tools-3" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/abacus.png?v=15" title=":abacus:" class="emoji" alt=":abacus:" loading="lazy" width="20" height="20"> 3. FEM Simulation Tools</h3>
<ul>
<li>Has anyone used <strong>FEBio</strong>, <strong>CalculiX</strong>, or other <strong>open-source solvers</strong> for similar soft tissue or craniofacial simulations?</li>
<li>Are there any <strong>existing scripts, Slicer extensions, or Python modules</strong> that simplify the export for such biomechanical setups?</li>
</ul>
<hr>
<p>If anyone has done something similar or can share an example <strong>workflow or reference</strong>, it would be extremely helpful.</p>
<p>Thanks a lot in advance for your time and insights!</p>

---

## Post #2 by @pieper (2025-10-20 18:33 UTC)

<p>That’s a big project, but something that can definitely be done using the tools you mentioned, at least to some level of approximation.  Each of the steps you outlines is full of difficulties with no clear best solution, so you’ll need to explore the options and also see what other people have had luck with.  Sliding layers of soft and hard tissue remain challenges and will be key in your project I suspect.</p>
<p>I suggest you also look at SOFA, and the SlicerSOFA extension.  You can find pointers to everything <a href="https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/SlicerSOFA/">here</a>.</p>

---
