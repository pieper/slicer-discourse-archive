---
topic_id: 48250
title: "New modules for generation CFD-simulation-ready meshes"
date: 2026-09-23
url: https://discourse.slicer.org/t/48250
last_bumped: 2026-09-24T14:03:18.235Z
---

# New modules for generation CFD-simulation-ready meshes

**Topic ID**: 48250
**Date**: 2026-09-23
**URL**: https://discourse.slicer.org/t/new-modules-for-generation-cfd-simulation-ready-meshes/48250

---

## Post #1 by @lassoan (2026-09-23 15:41 UTC)

<p>I’m happy to share that we have completed development of a set of modules to generate CFD-simulation-ready mesh from image segmentation.</p>
<p>The work has been largely based on the <a href="https://vmtk.github.io/">VMTK</a> toolkit, exposing its existing features and extending it with new ones. It was a joint effort between the <a href="https://slicerheart.org/">SlicerHeart</a> group at Children’s Hospital of Philadelphia (PI: Matthew A. Jolley) and <a href="https://simvascular.github.io/">SimVascular</a> group at Stanford (PI: Alison Marsden), with Andras Lasso and Aaron Brown as main contributors.</p>
<p>Demo video of the main features:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="NfmVDswPphY" data-video-title="Image Segmentation to Simulation-Ready Mesh SlicerHeart Workflow" data-video-start-time="" data-video-list-id="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=NfmVDswPphY" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/NfmVDswPphY/maxresdefault.jpg" title="Image Segmentation to Simulation-Ready Mesh SlicerHeart Workflow" width="690" height="388">
  </a>
</div>
<p><em><a href="https://youtu.be/NfmVDswPphY">(Click here to see the video on YouTube)</a></em></p>
<p>The workflow consists of three modules - one of them is completely new and one completely reworked. Each module can run fully automatically, but also offers many customization options:</p>
<ul>
<li><strong>Extract centerline:</strong> needed for convenient definition of vessel branches and clipping plane orientations - <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/ExtractCenterline.md">documentation</a></li>
<li><strong>Clip vessel:</strong> clip the segmentation to the relevant region - <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/ClipVessel.md">documentation</a>
<ul>
<li>cut off branches: automatic endpoint detection and clipping position/orientation recommendation, can be adjusted for each point</li>
<li>flow extensions: optional, absolute or relative to radius, can be set globally and adjusted individually for each branch</li>
<li>capping: straight or smooth, optionally uniform distribution (automatic resolution to match wall or manually specified)</li>
<li>labeling: boundaries and cap faces are labeled using point and cell data, they are propagated to the final volumetric mesh</li>
</ul>
</li>
<li><strong>CFD mesh generator:</strong> generate tetrahedral mesh from surface mesh - <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/Docs/CfdMeshGenerator.md">documentation</a>
<ul>
<li>uniform remeshing: optional, can be enabled separately for the wall and caps</li>
<li>capping: optional, if input did not contain caps it can add them</li>
<li>boundary layer refinement: optional, adds layers of prism elements at the wall, can be turned off separately for the caps</li>
<li>automatic labeling of boundary surfaces: based on labels in the input surface mesh</li>
<li>regional isotropic refinement supported by all but not yet exposed on the user interface</li>
<li>it provides 3 meshing engines: all the module features are available for all three meshers, all the inputs and outputs are converted automatically to match the data format used by each mesher
<ul>
<li>TetGen: fast but its free license is extremely restrictive (AGPL), therefore most uses require paid commercial license</li>
<li>NetGen: slightly slower but completely free (LGPL weak copyleft license allows free commercial use without sharing own source code)</li>
<li>fTetWild: slow, but free and does not require good quality input mesh (MPL2.0 weak copyleft license allows free commercial use without sharing own source code)</li>
</ul>
</li>
</ul>
</li>
<li><strong>SimVascular Mesh Prep</strong> is a new module in the SimVascular extension that converts a volume mesh from CFD Mesh Generator into a <code>mesh-complete</code> folder that can be read by the <a href="https://github.com/SimVascular/svMultiPhysics">svMultiPhysics solver</a>. That folder holds the volume mesh plus one surface file per inlet, outlet and wall, which the solver’s boundary conditions attach to. The module works together with Clip Vessel in the VMTK extension to automatically pass clip point names on to corresponding cap surfaces. The names are carried through CFD Mesh Generator, so a clipped model arrives with every cap already named after its clip point, and renaming a clip point renames the cap. You can also name any face, or rename one, by hovering over it and clicking it in the 3D view. For each face the module shows its area, equivalent diameter and flatness. Export mesh-complete writes the  mesh-complete folder that is ready for an svMultiPhysics simulation run from the terminal. Setting up and running simulations from Slicer’s GUI is under active development as part of the ongoing SimVascular-to-Slicer port. - <a href="https://github.com/SimVascular/SlicerSimVascular/blob/main/Docs/SimVascularMeshPrep.md">documentation</a></li>
</ul>
<p>Notes:</p>
<ul>
<li>All these modules are available via the VMTK and SimVascular extensions for the latest Slicer Stable Release (currently Slicer-5.12.4) and very latest Slicer Preview Release.</li>
<li>The modules can be used in sequence or independently. For example, if you already have the clipped surface mesh then you can go straight to the CFD mesh generator module.</li>
<li>Slicer uses mm-g-s unit system. For exchanging simulation input or output meshes that use a different system (such as CGS), you can use the “Import/Export simulation model” module in SlicerHeart extension - <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImportExportSimulationModel.md">documentation</a></li>
<li>The modules work with all automatic and manual segmentation modules in 3D Slicer and various mesh processing modules, such as stent deployment simulator in <a href="https://github.com/SimVascular/SlicerSimVascular#simvascular-extension-for-3d-slicer">SimVascular Slicer extension</a>.</li>
</ul>
<p>Extracted centerline:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef59f2e90d85509f60e0966f4b6e2e317729b639.jpeg" data-download-href="/uploads/short-url/y9oPsw7KcFXSO1vO0PnsQiUMLQB.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef59f2e90d85509f60e0966f4b6e2e317729b639_2_690x388.jpeg" alt="image" data-base62-sha1="y9oPsw7KcFXSO1vO0PnsQiUMLQB" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef59f2e90d85509f60e0966f4b6e2e317729b639_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef59f2e90d85509f60e0966f4b6e2e317729b639_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef59f2e90d85509f60e0966f4b6e2e317729b639_2_1380x776.jpeg 2x" data-dominant-color="ACABCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Clip, cap, and extend vessel branches:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26984dea4f2eb50295065331ba9a8495d694e2c9.jpeg" data-download-href="/uploads/short-url/5vqsaVAsbF3PBhuz5vZ37E2bZwd.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26984dea4f2eb50295065331ba9a8495d694e2c9_2_690x388.jpeg" alt="image" data-base62-sha1="5vqsaVAsbF3PBhuz5vZ37E2bZwd" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26984dea4f2eb50295065331ba9a8495d694e2c9_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26984dea4f2eb50295065331ba9a8495d694e2c9_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26984dea4f2eb50295065331ba9a8495d694e2c9_2_1380x776.jpeg 2x" data-dominant-color="A4A5C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 229 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Generated volumetric mesh with thin boundary layer elements:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/443cf23f7c65782fd35ada20a1e7cb61708e1845.jpeg" data-download-href="/uploads/short-url/9JF2Mc6gut8xDPTeEis5SMZ9gix.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/443cf23f7c65782fd35ada20a1e7cb61708e1845_2_690x388.jpeg" alt="image" data-base62-sha1="9JF2Mc6gut8xDPTeEis5SMZ9gix" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/443cf23f7c65782fd35ada20a1e7cb61708e1845_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/443cf23f7c65782fd35ada20a1e7cb61708e1845_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/443cf23f7c65782fd35ada20a1e7cb61708e1845_2_1380x776.jpeg 2x" data-dominant-color="B9879E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 363 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Mesh preparation for SimVascular svMultiPhysics:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29420d8b65f33edf9a9de92574b68823cd8415c2.jpeg" data-download-href="/uploads/short-url/5SZ5PiRWqCRcDf54mXa8SImxkpc.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29420d8b65f33edf9a9de92574b68823cd8415c2_2_690x444.jpeg" alt="image" data-base62-sha1="5SZ5PiRWqCRcDf54mXa8SImxkpc" width="690" height="444" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29420d8b65f33edf9a9de92574b68823cd8415c2_2_690x444.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29420d8b65f33edf9a9de92574b68823cd8415c2_2_1035x666.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29420d8b65f33edf9a9de92574b68823cd8415c2_2_1380x888.jpeg 2x" data-dominant-color="C5C5DC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1621×1045 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any feedback and suggestions are welcome.</p>

---

## Post #2 by @Esteban_Barreiro (2026-09-24 14:03 UTC)

<p>Congratulations for all the team. Great work!!!</p>
<p>is good to know that VMTK still alive and pumping! Thanks for sharing.</p>

---
