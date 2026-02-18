# Slicer 5.8: Summary, Highlights, and Changelog

**Topic ID**: 41988
**Date**: 2025-03-07
**URL**: https://discourse.slicer.org/t/slicer-5-8-summary-highlights-and-changelog/41988

---

## Post #1 by @jcfr (2025-03-07 18:40 UTC)

<h1><a name="p-123145-table-of-content-1" class="anchor" href="#p-123145-table-of-content-1" aria-label="Heading link"></a>Table of content</h1>
<ul>
<li><a href="#heading--summary">Summary</a></li>
<li><a href="https://discourse.slicer.org/t/slicer-5-8-summary-highlights-and-changelog/41988/2">Detailed Changlog 5.8.0</a></li>
<li><a href="https://discourse.slicer.org/t/slicer-5-8-summary-highlights-and-changelog/41988/3">Detailed Changlog 5.8.1</a></li>
</ul>
<h1><a name="p-123145-summary-2" class="anchor" href="#p-123145-summary-2" aria-label="Heading link"></a>Summary</h1>
<p>The community of 3D Slicer developers is proud to announce that version 5.8 is <a href="http://download.slicer.org/">now available for download</a>. This release includes new <a href="https://discourse.slicer.org/t/new-feature-interactive-transformation-adjustable-center-of-rotation/36974">interactive transformations</a>, <a href="https://discourse.slicer.org/t/new-feature-generalized-clipping/41994">generalized clipping</a>, <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#ambient-shadows">adjustable ambient shadows</a>, a <a href="https://discourse.slicer.org/t/new-feature-visual-dicom-browser/33874">visual DICOM browser</a>, a <a href="https://training.slicer.org/">revamped training portal</a>, and over <a href="https://discourse.slicer.org/t/slicer-5-8-summary-highlights-and-changelog/41988/2#heading--new">20 new extensions</a> that further expand Slicer’s capabilities. It also includes enhancements across core modules, as well as numerous performance and usability improvements.</p>
<p>3D Slicer 5.8 builds on the success of earlier versions that have had over 1.8 million downloads of the core application and 8 million downloads of extensions during the last decade.</p>
<p>The development of 3D Slicer—including its numerous modules, extensions, datasets, pull requests, patches, issues reports, suggestions—is made possible by users, developers, contributors and commercial partners around the world. 3D Slicer is based on a stack of open-source software and we are working constantly on updating the underlying packages. This development is funded by various grants and agencies. For more details, please see the 3D Slicer <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#acknowledgments">Acknowledgments</a> page.</p>
<p>Feel free to share your insights on <a href="https://discourse.slicer.org/">Discourse</a> and explore how to contribute to the project (please, read our <a href="https://slicer.readthedocs.io/en/latest/developer_guide/contributing.html">contributing guidelines</a>). If you need help using Slicer, want to report a problem, request a feature, or share how Slicer has contributed to your work, visit our <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html">Get Help</a> section.</p>
<p><a href="https://www.slicer.org/">slicer.org</a> serves as the central hub for the application, training materials, and the development community, offering a series of tutorials and data sets through the <a href="https://slicer.readthedocs.io/en/5.8/user_guide/getting_started.html#tutorials">Slicer Tutorials</a> page.</p>
<p><em>Please note that Slicer continues to be a research package and is not intended for clinical use (clinical users must obtain the necessary ethics or regulatory approvals).</em></p>
<p><em>The <code>5.8.0</code> version was released on January 23rd, 2025, under the tag <a href="https://github.com/Slicer/Slicer/tree/v5.8.0">v5.8.0</a>. Subsequently, the <code>5.8.1</code> followed on March 2nd, 2025, tagged at <a href="https://github.com/Slicer/Slicer/tree/v5.8.1">v5.8.1</a>. For information on prior releases, please see the <a href="https://github.com/Slicer/Slicer/wiki/Release-Details">Release Details</a> page.</em></p>
<h1><a name="p-123145-highlights-3" class="anchor" href="#p-123145-highlights-3" aria-label="Heading link"></a>Highlights</h1>
<ul>
<li>
<p>Introduce <a href="https://discourse.slicer.org/t/new-feature-interactive-transformation-adjustable-center-of-rotation/36974"><strong>Interactive transformations with adjustable center of rotation:</strong></a> Add the ability for any node to be translated, rotated, or scaled using interactive handles in both slice and 3D views. Editing operations can be constrained to specific axes, and the center of rotation can be freely chosen. Visualization options for interaction handle widgets can be customized to display only relevant handles/axes in each view. This updated interaction handle pipeline is also integrated with Markups, providing the same improved visualization for both Transforms and Markups.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th style="text-align:center"></th>
<th style="text-align:center">Before</th>
<th style="text-align:center">After</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center"><strong>Transforms</strong></td>
<td style="text-align:center"><img src="https://hackmd.io/_uploads/B1OP3HDj1e.png" alt="image" width="503" height="500"></td>
<td style="text-align:center"><img src="https://hackmd.io/_uploads/B1MKhBvoJe.png" alt="image" width="503" height="500"></td>
</tr>
<tr>
<td style="text-align:center"><strong>Markups</strong></td>
<td style="text-align:center"><img src="https://hackmd.io/_uploads/rJKqhBPjJl.png" alt="image" width="503" height="500"></td>
<td style="text-align:center"><img src="https://hackmd.io/_uploads/H173hBDoJx.png" alt="image" width="503" height="500"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>Allow adjusting ambient shadow intensity:</strong> Add shift and scale <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#ambient-shadows">sliders in the 3D view controller</a> to linearly modify ambient shadows. This makes it possible to darken ambient shadows (by increasing scale) without dimming the entire 3D scene (by increasing shift).</p>
<div class="md-table">
<table>
<thead>
<tr>
<th style="text-align:center"><img src="https://hackmd.io/_uploads/ryIm2SPj1e.png" alt="image" width="690" height="238"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">Shadow of the rib cast on the kidney behind it.<br><strong>Left</strong> - no shadows. | <strong>Center</strong> - default shadows (100%/0%). | <strong>Right</strong> - strong shadows (200%/20%)<br></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>Add Visual DICOM browser</strong>: Provide a <a href="https://discourse.slicer.org/t/new-feature-visual-dicom-browser/33874">new user interface</a> for quick viewing and retrieval of patient images stored on remote DICOM servers. The new browser focuses on clinical workflows that involve all images of a single patient rather than multi-patient management.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th style="text-align:center"><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f88bb3a966b466304744e7e8a23a63067f3f5a7e.png" data-download-href="/uploads/short-url/zsJIMVnPVCUwTBzwM37eg4Y1mNg.png?dl=1" title=""><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f88bb3a966b466304744e7e8a23a63067f3f5a7e_2_616x500.png" alt="" role="presentation" width="616" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f88bb3a966b466304744e7e8a23a63067f3f5a7e_2_616x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f88bb3a966b466304744e7e8a23a63067f3f5a7e_2_924x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f88bb3a966b466304744e7e8a23a63067f3f5a7e_2_1232x1000.png 2x" data-dominant-color="BCBDBE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">1577×1280 353 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">Visual DICOM Browser</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://discourse.slicer.org/t/new-feature-generalized-clipping/41994"><strong>Add clipping options to models, segmentation, and volume rendering:</strong></a> Introduce a new <code>vtkMRMLClipNode</code> class that specifies the combination of implicit functions used for clipping. Nodes such as <code>vtkMRMLMarkupsPlaneNode</code>, <code>vtkMRMLMarkupsROINode</code>, <code>vtkMRMLSliceNode</code>, <code>vtkMRMLModelNode</code>, or additional <code>vtkMRMLClipNode</code>s may be referenced from the <code>vtkMRMLClipNode</code>. Each provides a <code>GetImplicitFunctionWorld()</code> method that returns a <code>vtkImplicitFunction</code> to apply clipping operations to other nodes.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th style="text-align:center"><img src="https://hackmd.io/_uploads/Hy-3iBvsJe.png" alt="image" width="474" height="500"></th>
<th style="text-align:center"><img src="https://hackmd.io/_uploads/rkZxhSDiJl.png" alt="image" width="456" height="238"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center">Node clipping of model, segmentation and volume rendering</td>
<td style="text-align:center">Clipping node widget</td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><strong>New Training Portal</strong>: Launch a training portal at <a href="https://training.slicer.org">training.slicer.org</a>, which replaces the historical MediaWiki-based approach with a modern static site generator (Jekyll) and modular tutorials. Each tutorial can live in its own GitHub repository for easier creation, revision control, and release-asset management. Future work will automate tasks such as translation and test execution.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th style="text-align:center"><img src="https://hackmd.io/_uploads/HyWWTSvskl.png" alt="image" width="528" height="500"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center"><a href="https://training.slicer.org">3D Slicer Training Compendium</a></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p>Introduce over <a href="https://discourse.slicer.org/t/slicer-5-8-summary-highlights-and-changelog/41988/2#heading--new"><strong>20 new extensions</strong></a> that integrate advanced AI-based segmentation, collaborative segmentation workflows, 3D simulation frameworks, comprehensive morphological analysis, specialized diffusion pipelines, streamlined tutorial creation, and more.</p>
</li>
</ul>

---

## Post #2 by @jcfr (2025-03-07 18:40 UTC)

<h1><a name="p-123146-changelog-580-1" class="anchor" href="#p-123146-changelog-580-1" aria-label="Heading link"></a>Changelog: 5.8.0</h1>
<ul>
<li><a href="#heading--core">Core</a>
<ul>
<li><a href="#heading--rendering-display">Rendering &amp; display</a></li>
<li><a href="#heading--io">IO</a></li>
<li><a href="#heading--performances">Performances</a></li>
<li><a href="#heading--fixes">Fixes</a></li>
<li><a href="#heading--application">Application</a></li>
<li><a href="#heading--extension">Extension</a></li>
<li><a href="#heading--cli">CLI</a></li>
<li><a href="#heading--scripting">Scripting</a></li>
<li><a href="#heading--internationalization-localization">Internationalization/Localization</a></li>
<li><a href="#heading--installation">Installation</a></li>
<li><a href="#heading--mrml">MRML</a></li>
<li><a href="#heading--api-updates">API Updates</a></li>
<li><a href="#heading--telemetry-support">Telemetry Support</a></li>
<li><a href="#heading--documentation">Documentation</a></li>
</ul>
</li>
<li><a href="#heading--improved-modules">Improved Modules</a>
<ul>
<li><a href="#heading--data">Data</a></li>
<li><a href="#heading--dicom">DICOM</a></li>
<li><a href="#heading--endoscopy">Endoscopy</a></li>
<li><a href="#heading--markups">Markups</a></li>
<li><a href="#heading--models">Models</a></li>
<li><a href="#heading--reformat">Reformat</a></li>
<li><a href="#heading--sampledata">SampleData</a></li>
<li><a href="#heading--segmentations">Segmentations</a></li>
<li><a href="#heading--segment-statistics">Segment Statistics</a></li>
<li><a href="#heading--sequences">Sequences</a></li>
<li><a href="#heading--subject-hierarchy">Subject Hierarchy</a></li>
<li><a href="#heading--texts">Texts</a></li>
<li><a href="#heading--terminologies">Terminologies</a></li>
<li><a href="#heading--transforms">Transforms</a></li>
<li><a href="#heading--volume-rendering">Volume Rendering</a></li>
<li><a href="#heading--webserver">WebServer</a></li>
</ul>
</li>
<li><a href="#heading--infrastructure">Infrastructure</a>
<ul>
<li><a href="#heading--packaging">Packaging</a></li>
<li><a href="#heading--testing">Testing</a></li>
<li><a href="#heading--continuous-integration-ci">Continuous integration (CI)</a></li>
<li><a href="#heading--build-system">Build system</a></li>
<li><a href="#heading--platform-support">Platform support</a></li>
<li><a href="#heading--dependencies">Dependencies</a></li>
<li><a href="#heading--custom-slicer-application-support">Custom Slicer application support</a></li>
</ul>
</li>
<li><a href="#heading--extensions">Extensions</a>
<ul>
<li><a href="#heading--new">New</a></li>
<li><a href="#heading--updated">Updated</a></li>
<li><a href="#heading--removed">Removed</a></li>
</ul>
</li>
</ul>
<h2 id="heading--core">Core</h2>
<h3 id="heading--rendering-display">Rendering &amp; display</h3>
<ul>
<li>Add clipping options to models, segmentation, and volume rendering (<a href="https://github.com/Slicer/Slicer/pull/7996">PR-7996</a>, <a href="https://github.com/Slicer/Slicer/pull/8087">PR-8087</a>)</li>
<li>Allow disabling layer blend clipping to background in slice views (<a href="https://github.com/Slicer/Slicer/pull/7886">PR-7886</a>)</li>
<li>Add option to display shadows in 3D views (<a href="https://github.com/Slicer/Slicer/pull/7515">PR-7515</a>)</li>
<li>Allow setting ambient shadows intensity (<a href="https://github.com/Slicer/Slicer/pull/7822">PR-7822</a>)</li>
<li>Disable shadows in 3D views by default (<a href="https://github.com/Slicer/Slicer/pull/7583">PR-7583</a>)</li>
<li>Add option to display slice edges in 3D view (<a href="https://github.com/Slicer/Slicer/pull/8008">PR-8008</a>)</li>
<li>Re-enable display of interaction handles in VR (<a href="https://github.com/Slicer/Slicer/pull/7630">PR-7630</a>)</li>
<li>Allow reslicing of 32-bit integer images (<a href="https://github.com/Slicer/Slicer/pull/7292">PR-7292</a>)</li>
<li>Fix backface color on Slice nodes in 3D views (<a href="https://github.com/Slicer/Slicer/pull/8056">PR-8056</a>)</li>
<li>Standardize fit slice to volume behavior (<a href="https://github.com/Slicer/Slicer/pull/8063">PR-8063</a>, <a href="https://github.com/Slicer/Slicer/pull/8076">PR-8076</a>)</li>
<li>Fix fit slice view if no background volume is selected (<a href="https://github.com/Slicer/Slicer/pull/7986">PR-7986</a>)</li>
<li>Fix interaction handle enable/disable not working in views (<a href="https://github.com/Slicer/Slicer/pull/8068">PR-8068</a>)</li>
<li>Fix slice view “More Options” opening by default (<a href="https://github.com/Slicer/Slicer/pull/8096">PR-8096</a>)</li>
<li>Ensure background SeriesTime corner annotation is displayed (<a href="https://github.com/Slicer/Slicer/pull/8122">PR-8122</a>)</li>
</ul>
<h3 id="heading--io">IO</h3>
<ul>
<li>Show more details about scene changes on close or exit (<a href="https://github.com/Slicer/Slicer/pull/8000">PR-8000</a>)</li>
<li>Improve <code>vtkMRMLVolumeArchetypeStorageNode</code> for left-handed volumes (<a href="https://github.com/Slicer/Slicer/pull/7627">PR-7627</a>)</li>
<li>Improve ultrasound reading (<a href="https://github.com/Slicer/Slicer/pull/7649">PR-7649</a>)</li>
<li>Improve automatic detection of NIFTI displacement field transform files (<a href="https://github.com/Slicer/Slicer/pull/7967">PR-7967</a>)</li>
<li>Show warning if data loss occurs when saving to TIFF (<a href="https://github.com/Slicer/Slicer/pull/7655">PR-7655</a>)</li>
<li>Allow aliases for NRRD “type” header in postNRRD (<a href="https://github.com/Slicer/Slicer/pull/7664">PR-7664</a>)</li>
<li>Log more information when NRRD reading fails (<a href="https://github.com/Slicer/Slicer/pull/7700">PR-7700</a>)</li>
<li>Improve automatic detection of segmentation files (<a href="https://github.com/Slicer/Slicer/pull/7967">PR-7967</a>)</li>
<li>Reduce bundle temp directory length when saving scene MRB (<a href="https://github.com/Slicer/Slicer/pull/7899">PR-7899</a>)</li>
<li>Make minor fixes from 5D NRRD IO development (<a href="https://github.com/Slicer/Slicer/pull/7880">PR-7880</a>)</li>
<li>Fix reading of images that have a left-handed IJK coordinate system (<a href="https://github.com/Slicer/Slicer/pull/7746">PR-7746</a>)</li>
<li>Fix saving of NRRD files with certain filenames (<a href="https://github.com/Slicer/Slicer/pull/7616">PR-7616</a>)</li>
<li>Make automatic detection of segmentation files more robust (<a href="https://github.com/Slicer/Slicer/pull/7738">PR-7738</a>)</li>
<li>Make segmentation .seg.nrrd file reading more robust (<a href="https://github.com/Slicer/Slicer/pull/7738">PR-7738</a>)</li>
<li>Fix export of VTK unstructured grid (<a href="https://github.com/Slicer/Slicer/pull/7760">PR-7760</a>)</li>
<li>Fix reading of volume property (<code>.vp</code>) file (<a href="https://github.com/Slicer/Slicer/pull/7772">PR-7772</a>)</li>
<li>Fix tensor image reading (<a href="https://github.com/Slicer/Slicer/pull/7773">PR-7773</a>)</li>
<li>Fix saving with long node names (<a href="https://github.com/Slicer/Slicer/pull/8028">PR-8028</a>)</li>
<li>Fix loading and saving <code>.mrb</code> files with trailing space in filename (<a href="https://github.com/Slicer/Slicer/pull/8134">PR-8134</a>)</li>
</ul>
<h3 id="heading--performances">Performances</h3>
<ul>
<li>Update ITK to suppress irrelevant TIFF warnings (<a href="https://github.com/Slicer/Slicer/pull/8016">PR-8016</a>)</li>
</ul>
<h3 id="heading--fixes">Fixes</h3>
<ul>
<li>Do not show warning popup on exit if camera node is changed (<a href="https://github.com/Slicer/Slicer/pull/8000">PR-8000</a>)</li>
<li>Re-introduce logging of unparsed arguments (to log file only) (<a href="https://github.com/Slicer/Slicer/pull/7943">PR-7943</a>)</li>
<li>Fix crash when module category name matches a module name (<a href="https://github.com/Slicer/Slicer/pull/7524">PR-7524</a>)</li>
<li>Fix Model DM crash when adding display node (<a href="https://github.com/Slicer/Slicer/pull/8131">PR-8131</a>)</li>
<li>Fix crash when hovering over interaction handles after scene load (<a href="https://github.com/Slicer/Slicer/pull/8067">PR-8067</a>)</li>
<li>Suppress “Populating font family aliases” warning on macOS (<a href="https://github.com/Slicer/Slicer/pull/8159">PR-8159</a>)</li>
<li>Remove unneeded display of ignored command line arguments (<a href="https://github.com/Slicer/Slicer/pull/7941">PR-7941</a>)</li>
<li>Remove “Active” prefix from some node selection comboboxes (<a href="https://github.com/Slicer/Slicer/pull/7985">PR-7985</a>)</li>
</ul>
<h3 id="heading--application">Application</h3>
<ul>
<li>Display instantiated module name in splash screen (<a href="https://github.com/Slicer/Slicer/pull/7454">PR-7454</a>)</li>
<li>Allow dragging of splash window (<a href="https://github.com/Slicer/Slicer/pull/7527">PR-7527</a>)</li>
<li>Support dragging of the splash window just after clicking on it (<a href="https://github.com/Slicer/Slicer/pull/7532">PR-7532</a>)</li>
<li>Update <code>Slicer.crt</code> CA bundle (<a href="https://github.com/Slicer/Slicer/pull/7575">PR-7575</a>, <a href="https://github.com/Slicer/Slicer/pull/7781">PR-7781</a>, <a href="https://github.com/Slicer/Slicer/pull/7916">PR-7916</a>, <a href="https://github.com/Slicer/Slicer/pull/8054">PR-8054</a>)</li>
</ul>
<h3 id="heading--extension">Extension</h3>
<ul>
<li>Support specifying contributor extension metadata with newlines (<a href="https://github.com/Slicer/Slicer/pull/7720">PR-7720</a>)</li>
<li>Switch extension index entry format from <code>.s4ext</code> to <code>.json</code> (<a href="https://github.com/Slicer/Slicer/pull/7709">PR-7709</a>)</li>
<li>Simplify Slicer version check in extensions (<a href="https://github.com/Slicer/Slicer/pull/7954">PR-7954</a>)</li>
<li>Add “tier” property to extensions catalog schema (<a href="https://github.com/Slicer/Slicer/pull/8066">PR-8066</a>)</li>
<li>Simplify extension manager build system (<a href="https://github.com/Slicer/Slicer/pull/7644">PR-7644</a>)</li>
<li>Fix loading of modules that depend on another extension (<a href="https://github.com/Slicer/Slicer/pull/7580">PR-7580</a>)</li>
<li>Fix extension schema ID (<a href="https://github.com/Slicer/Slicer/pull/7710">PR-7710</a>)</li>
</ul>
<h3 id="heading--cli">CLI</h3>
<ul>
<li>Disable compression for CLI output files (<a href="https://github.com/Slicer/Slicer/pull/7885">PR-7885</a>)</li>
<li>Report missing <code>longflag</code> in module description XML (<a href="https://github.com/Slicer/Slicer/pull/7779">PR-7779</a>)</li>
<li>Restore support for writing CLI output as <code>.fcsv</code> files (<a href="https://github.com/Slicer/Slicer/pull/7971">PR-7971</a>)</li>
</ul>
<h3 id="heading--scripting">Scripting</h3>
<ul>
<li>Add parameter node GUI wrappings for certain CTK and other classes (<a href="https://github.com/Slicer/Slicer/pull/7918">PR-7918</a>)</li>
<li>Add methods for <code>runTest</code> upgrade (<a href="https://github.com/Slicer/Slicer/pull/7444">PR-7444</a>)</li>
<li>Fix support for registering <code>parameterNodeWrapper</code> plugins (<a href="https://github.com/Slicer/Slicer/pull/7480">PR-7480</a>)</li>
<li>Fix meta-object system registration of <code>qSlicerIO::fileType</code> return type (<a href="https://github.com/Slicer/Slicer/pull/7552">PR-7552</a>)</li>
<li>Support checking if IO registration from Python occurs with no registered IOs (<a href="https://github.com/Slicer/Slicer/pull/7553">PR-7553</a>)</li>
<li>Fix module reload of modules without <code>reloadTestMenuButton</code> (<a href="https://github.com/Slicer/Slicer/pull/8116">PR-8116</a>)</li>
<li>Fix <code>QComboBoxToEnumConnector</code> to avoid resetting default (<a href="https://github.com/Slicer/Slicer/pull/8116">PR-8116</a>)</li>
</ul>
<h3 id="heading--internationalization-localization">Internationalization/Localization</h3>
<ul>
<li>Make translations in Python scripts more robust (<a href="https://github.com/Slicer/Slicer/pull/7611">PR-7611</a>)</li>
<li>Add translation for <code>VolumeDisplayPresets.json</code> (<a href="https://github.com/Slicer/Slicer/pull/7651">PR-7651</a>)</li>
<li>Only translate Python strings when necessary (<a href="https://github.com/Slicer/Slicer/pull/7813">PR-7813</a>)</li>
<li>Make more strings translatable (<a href="https://github.com/Slicer/Slicer/pull/7309">PR-7309</a>)</li>
<li>Fix translation in <code>qMRMLThreeDViewCntrollerWidget</code> (<a href="https://github.com/Slicer/Slicer/pull/7526">PR-7526</a>)</li>
<li>Mark translatable strings in Markups module (<a href="https://github.com/Slicer/Slicer/pull/7620">PR-7620</a>)</li>
<li>Mark translatable strings in ExtensionWizard module (<a href="https://github.com/Slicer/Slicer/pull/7698">PR-7698</a>)</li>
<li>Fix translation handle flickering when holding ALT; <strong>update</strong> Transforms module documentation to include interaction info (<a href="https://github.com/Slicer/Slicer/pull/7663">PR-7663</a>)</li>
<li>Fix translation of Python modules (<a href="https://github.com/Slicer/Slicer/pull/7909">PR-7909</a>)</li>
<li>Mark translatable strings in Reformat, Texts, and Transforms modules (<a href="https://github.com/Slicer/Slicer/pull/7817">PR-7817</a>)</li>
</ul>
<h3 id="heading--installation">Installation</h3>
<ul>
<li>Remove <code>DMRIInstall</code> module (<a href="https://github.com/Slicer/Slicer/pull/7662">PR-7662</a>)</li>
</ul>
<h3 id="heading--mrml">MRML</h3>
<ul>
<li>Improve handling of invalid input in <code>MRMLViewInteractorStyle</code> classes (<a href="https://github.com/Slicer/Slicer/pull/7497">PR-7497</a>)</li>
<li>Register nodes in <code>MRMLScene</code> constructor deterministically (<a href="https://github.com/Slicer/Slicer/pull/8156">PR-8156</a>)</li>
<li>Check if a node is present in the scene before adding it (<a href="https://github.com/Slicer/Slicer/pull/8029">PR-8029</a>)</li>
<li>Fix incorrect <code>vtkMRMLSliceDisplayNode</code> XML attribute name (<a href="https://github.com/Slicer/Slicer/pull/8081">PR-8081</a>)</li>
<li>Fix folder display override for model nodes (<a href="https://github.com/Slicer/Slicer/pull/8083">PR-8083</a>)</li>
<li>Ensure MRB loading correctly reports loaded nodes (<a href="https://github.com/Slicer/Slicer/pull/8135">PR-8135</a>)</li>
<li>Fix issue with adding a new node after rename cancellation (<a href="https://github.com/Slicer/Slicer/pull/7598">PR-7598</a>)</li>
<li>Fix <code>GetStorableNodesModifiedSinceRead</code> for short text nodes (<a href="https://github.com/Slicer/Slicer/pull/8000">PR-8000</a>)</li>
<li>Fix <code>vtkMRMLTextStorageNode::WriteDataInternal</code> not throwing error (<a href="https://github.com/Slicer/Slicer/pull/8025">PR-8025</a>)</li>
<li>Fix creation of extra volume property storage nodes (<a href="https://github.com/Slicer/Slicer/pull/8029">PR-8029</a>)</li>
<li>Prevent making volume storage nodes modified after file save (<a href="https://github.com/Slicer/Slicer/pull/8029">PR-8029</a>)</li>
</ul>
<h3 id="heading--api-updates">API Updates</h3>
<ul>
<li>Add API to access SSAO rendering pass in 3D views (<a href="https://github.com/Slicer/Slicer/pull/7616">PR-7616</a>)</li>
<li>Improve <code>vtkMRMLLayoutNode</code> API (<a href="https://github.com/Slicer/Slicer/pull/7616">PR-7616</a>)</li>
<li>Migrate <code>vtkSingleton</code> to <code>vtkAddon</code> (<a href="https://github.com/Slicer/Slicer/pull/7849">PR-7849</a>)</li>
</ul>
<h3 id="heading--telemetry-support">Telemetry Support</h3>
<ul>
<li>Add API to log software usage events (<a href="https://github.com/Slicer/Slicer/pull/7855">PR-7855</a>)</li>
</ul>
<h3 id="heading--documentation">Documentation</h3>
<ul>
<li>Switch highlighted social network to LinkedIn (<a href="https://github.com/Slicer/Slicer/pull/8023">PR-8023</a>)</li>
<li>Improve docstring of <code>vtkMRMLViewInteractorStyle</code> processing functions (<a href="https://github.com/Slicer/Slicer/pull/7498">PR-7498</a>)</li>
<li>Update installation and building instructions for ArchLinux (<a href="https://github.com/Slicer/Slicer/pull/7521">PR-7521</a>)</li>
<li>Update list of supported formats for Quantitative Reporting extension (<a href="https://github.com/Slicer/Slicer/pull/7557">PR-7557</a>)</li>
<li>Fix comment format, update variable names, and add missing closing bracket in script repository (<a href="https://github.com/Slicer/Slicer/pull/7615">PR-7615</a>)</li>
<li>Update <code>FastModelAlign</code> <code>registration.md</code> (<a href="https://github.com/Slicer/Slicer/pull/7669">PR-7669</a>)</li>
<li>Add Ubuntu 22.04 build instructions (<a href="https://github.com/Slicer/Slicer/pull/7689">PR-7689</a>)</li>
<li>Reorganize Ubuntu console example of required dev tools (<a href="https://github.com/Slicer/Slicer/pull/7692">PR-7692</a>)</li>
<li>Encourage trying preview release before reporting bugs (<a href="https://github.com/Slicer/Slicer/pull/7686">PR-7686</a>)</li>
<li>Update <code>gui.md</code> with an example of displaying a node in only some views (<a href="https://github.com/Slicer/Slicer/pull/7708">PR-7708</a>)</li>
<li>Improve segmentation DICOM export documentation (<a href="https://github.com/Slicer/Slicer/pull/7761">PR-7761</a>)</li>
<li>Match updated interface in <code>SlicerSurfaceToolbox Dynamic Modeler</code> (<a href="https://github.com/Slicer/Slicer/pull/7766">PR-7766</a>)</li>
<li>Clarify meaning of negative and positive sides of plane (<a href="https://github.com/Slicer/Slicer/pull/7769">PR-7769</a>)</li>
<li>Add documentation for 3D view <code>CTRL + Left-click + drag</code> (<a href="https://github.com/Slicer/Slicer/pull/7774">PR-7774</a>)</li>
<li>Update example of DICOM query/retrieve (<a href="https://github.com/Slicer/Slicer/pull/7802">PR-7802</a>)</li>
<li>Add plane creation example to <code>markups.md</code> (<a href="https://github.com/Slicer/Slicer/pull/7804">PR-7804</a>)</li>
<li>Add Python example for extracting a slice from a volume (<a href="https://github.com/Slicer/Slicer/pull/7808">PR-7808</a>)</li>
<li>Update Linux documentation (<a href="https://github.com/Slicer/Slicer/pull/7798">PR-7798</a>)</li>
<li>Add notes to <code>SECURITY.md</code> (<a href="https://github.com/Slicer/Slicer/pull/7818">PR-7818</a>)</li>
<li>Add notes on segment cross-sectional area measurement (<a href="https://github.com/Slicer/Slicer/pull/7863">PR-7863</a>)</li>
<li>Add script to query/retrieve DICOM with <code>ctkDICOMScheduler</code> (<a href="https://github.com/Slicer/Slicer/pull/7912">PR-7912</a>)</li>
<li>Add <code>scriptedregistration.md</code> with an example rigid registration (<a href="https://github.com/Slicer/Slicer/pull/7926">PR-7926</a>)</li>
<li>Remove outdated example and link to slicerio documentation (<a href="https://github.com/Slicer/Slicer/pull/7920">PR-7920</a>)</li>
<li>Improve <code>slicer.util.pip_install</code> documentation (<a href="https://github.com/Slicer/Slicer/pull/7959">PR-7959</a>)</li>
<li>Add example to compute distance of points from a plane (<a href="https://github.com/Slicer/Slicer/pull/7973">PR-7973</a>)</li>
<li>Update recommended screen resolution in documentation (<a href="https://github.com/Slicer/Slicer/pull/8010">PR-8010</a>)</li>
<li>Clarify doc of <code>vtkMRMLMarkupsROINode::GetObjectToWorldMatrix</code> (<a href="https://github.com/Slicer/Slicer/pull/8034">PR-8034</a>)</li>
<li>Clarify Qt 5.15.2 Windows binary install instructions (<a href="https://github.com/Slicer/Slicer/pull/8082">PR-8082</a>)</li>
<li>Update <code>dicom.md</code> (<a href="https://github.com/Slicer/Slicer/pull/8088">PR-8088</a>)</li>
<li>Fix “Edit on GitHub” link not appearing on ReadTheDocs (<a href="https://github.com/Slicer/Slicer/pull/8107">PR-8107</a>)</li>
<li>Set GitHub repository information for documentation generation (<a href="https://github.com/Slicer/Slicer/pull/8116">PR-8116</a>, <a href="https://github.com/Slicer/Slicer/pull/8108">PR-8108</a>)</li>
<li>Improve <code>slicer.util.getNode</code> documentation (<a href="https://github.com/Slicer/Slicer/pull/8116">PR-8116</a>)</li>
<li>Update links to tutorials (<a href="https://github.com/Slicer/Slicer/pull/7910">PR-7910</a>)</li>
</ul>
<h2 id="heading--improved-modules">Improved Modules</h2>
<h3 id="heading--data">Data</h3>
<ul>
<li>Improve appearance of node information section in Data module (<a href="https://github.com/Slicer/Slicer/pull/7578">PR-7578</a>)</li>
</ul>
<h3 id="heading--dicom">DICOM</h3>
<ul>
<li>Add <a href="https://discourse.slicer.org/t/new-feature-visual-dicom-browser/33874">visual DICOM browser</a> (<a href="https://github.com/Slicer/Slicer/pull/7525">PR-7525</a>, <a href="https://github.com/Slicer/Slicer/pull/7912">PR-7912</a>, <a href="https://github.com/Slicer/Slicer/pull/7676">PR-7676</a>, <a href="https://github.com/Slicer/Slicer/pull/7650">PR-7650</a>, <a href="https://github.com/Slicer/Slicer/pull/7811">PR-7811</a>, <a href="https://github.com/Slicer/Slicer/pull/7751">PR-7751</a>)</li>
<li>Add DICOM support for Multi-frame Grayscale Byte Secondary Capture Image (<a href="https://github.com/Slicer/Slicer/pull/7566">PR-7566</a>)</li>
<li>Add DICOM patcher rule to fix compressed ultrasound discolorization (<a href="https://github.com/Slicer/Slicer/pull/7656">PR-7656</a>)</li>
<li>Make characterset modifier DICOM patcher rule stronger (<a href="https://github.com/Slicer/Slicer/pull/7683">PR-7683</a>)</li>
<li>Add <code>loadSuccess</code> flag to loadable Qt and VTK DICOM classes (<a href="https://github.com/Slicer/Slicer/pull/8139">PR-8139</a>)</li>
<li>Fix context change at runtime in DICOM module (<a href="https://github.com/Slicer/Slicer/pull/7358">PR-7358</a>)</li>
<li>Fix error string format in <code>DICOMScalarVolumePlugin</code> and <code>ImportItkSnapLabel</code> (<a href="https://github.com/Slicer/Slicer/pull/7484">PR-7484</a>)</li>
<li>Prevent DICOM Browser popups on initial module entry (<a href="https://github.com/Slicer/Slicer/pull/7811">PR-7811</a>)</li>
<li>Force loading images from DICOM using right-handed coordinate system (<a href="https://github.com/Slicer/Slicer/pull/7858">PR-7858</a>)</li>
<li>Fix reading of multiple window/level presets in <code>DICOMScalarVolumePlugin</code> (<a href="https://github.com/Slicer/Slicer/pull/7922">PR-7922</a>)</li>
<li>Skip disabled plugins when loading DICOM by scripting (<a href="https://github.com/Slicer/Slicer/pull/7935">PR-7935</a>)</li>
<li>Fix regression for scans with negative spacing in DICOM (<a href="https://github.com/Slicer/Slicer/pull/7987">PR-7987</a>)</li>
<li>Fix hanging progress popup in DICOM browser (<a href="https://github.com/Slicer/Slicer/pull/8062">PR-8062</a>)</li>
<li>Add loadable warning in case of loading failure (<a href="https://github.com/Slicer/Slicer/pull/7163">PR-7163</a>)</li>
</ul>
<h3 id="heading--endoscopy">Endoscopy</h3>
<ul>
<li>Use “Use this curve” instead of “Create flythrough path” for the button text (<a href="https://github.com/Slicer/Slicer/pull/7435">PR-7435</a>)</li>
<li>Simplify Endoscopy API related to quaternion (<a href="https://github.com/Slicer/Slicer/pull/7431">PR-7431</a>)</li>
<li>Improve Endoscopy module UI self-discovery (<a href="https://github.com/Slicer/Slicer/pull/7436">PR-7436</a>)</li>
<li>Fix rebuild of Endoscopy flythrough when modifying the input curve (<a href="https://github.com/Slicer/Slicer/pull/7433">PR-7433</a>)</li>
<li>Recompute <code>EndoscopyLogic</code> fields immediately instead of lazily (<a href="https://github.com/Slicer/Slicer/pull/7437">PR-7437</a>)</li>
</ul>
<h3 id="heading--markups">Markups</h3>
<ul>
<li>Fix crash in <code>vtkPointLocator</code> when markups curve polydata is empty (<a href="https://github.com/Slicer/Slicer/pull/7732">PR-7732</a>)</li>
<li>Fix issue preventing interaction with Markups curves (<a href="https://github.com/Slicer/Slicer/pull/8021">PR-8021</a>)</li>
<li>Fix incorrect plane interaction scale handles initialization (<a href="https://github.com/Slicer/Slicer/pull/8031">PR-8031</a>)</li>
<li>Hide angle markups when the line does not intersect with the slice (<a href="https://github.com/Slicer/Slicer/pull/7832">PR-7832</a>)</li>
<li>Add API to change screen scale factor (<a href="https://github.com/Slicer/Slicer/pull/7740">PR-7740</a>)</li>
<li>Skip creation of markups interaction widget in VR windows (<a href="https://github.com/Slicer/Slicer/pull/7612">PR-7612</a>)</li>
<li>Add <code>Point(Start/End)InteractionEvent</code> for Markups interaction handles (<a href="https://github.com/Slicer/Slicer/pull/8117">PR-8117</a>)</li>
<li>Fix crash in Markups widget when closing a scene (<a href="https://github.com/Slicer/Slicer/pull/7628">PR-7628</a>)</li>
<li>Fix markups handle scale not updating (<a href="https://github.com/Slicer/Slicer/pull/7675">PR-7675</a>)</li>
<li>Fix crash when deleting multiple markups in subject hierarchy (<a href="https://github.com/Slicer/Slicer/pull/7736">PR-7736</a>)</li>
<li>Fix warning messages when creating markups with no display nodes (<a href="https://github.com/Slicer/Slicer/pull/7747">PR-7747</a>)</li>
<li>Fix unnecessary confirmation popup after hovering over markups (<a href="https://github.com/Slicer/Slicer/pull/8000">PR-8000</a>)</li>
<li>Fix markups interaction handles not respecting visibility options (<a href="https://github.com/Slicer/Slicer/pull/7868">PR-7868</a>)</li>
<li>Fix reading of markup point position from integer values (<a href="https://github.com/Slicer/Slicer/pull/7928">PR-7928</a>)</li>
<li>Fix copying of markup measurements (<a href="https://github.com/Slicer/Slicer/pull/8012">PR-8012</a>)</li>
<li>Fix missing Markups ROI fill in some views (<a href="https://github.com/Slicer/Slicer/pull/8019">PR-8019</a>)</li>
<li>Remove explicit dependency of <code>MarkupsROINode</code> on JSON storage node (<a href="https://github.com/Slicer/Slicer/pull/8152">PR-8152</a>)</li>
</ul>
<h3 id="heading--models">Models</h3>
<ul>
<li>Fix warnings when <code>vtkMRMLModelNode</code> has no mesh data (<a href="https://github.com/Slicer/Slicer/pull/7750">PR-7750</a>)</li>
</ul>
<h3 id="heading--reformat">Reformat</h3>
<ul>
<li>Fix incorrect tooltip for “Rotate to Volume Reformat” button (<a href="https://github.com/Slicer/Slicer/pull/7787">PR-7787</a>)</li>
<li>Fix failing <code>vtkMRMLCameraDisplayableManagerTest</code> (<a href="https://github.com/Slicer/Slicer/pull/7853">PR-7853</a>)</li>
</ul>
<h3 id="heading--sampledata">SampleData</h3>
<ul>
<li>Add option to download sample data from a custom URL (<a href="https://github.com/Slicer/Slicer/pull/8133">PR-8133</a>)</li>
<li>Use specified filename as node name in <code>SampleDataLogic.downloadFromSource</code> (<a href="https://github.com/Slicer/Slicer/pull/8163">PR-8163</a>)</li>
<li>Do not require file type in sample data specification (<a href="https://github.com/Slicer/Slicer/pull/7479">PR-7479</a>)</li>
<li>Fix error handling in <code>slicer.util.downloadFile</code> (<a href="https://github.com/Slicer/Slicer/pull/7473">PR-7473</a>)</li>
</ul>
<h3 id="heading--segmentations">Segmentations</h3>
<ul>
<li>Add <code>RemoveUnusedDisplayProperties</code> to <code>vtkMRMLSegmentationDisplayNode</code> (<a href="https://github.com/Slicer/Slicer/pull/7784">PR-7784</a>)</li>
<li>Generate unique segment IDs using a random identifier (<a href="https://github.com/Slicer/Slicer/pull/7836">PR-7836</a>)</li>
<li>Introduce setting for using standard terminology in segments table (<a href="https://github.com/Slicer/Slicer/pull/8011">PR-8011</a>)</li>
<li>Allow hiding parts of the Segment Editor widget (<a href="https://github.com/Slicer/Slicer/pull/8116">PR-8116</a>)</li>
<li>Allow disabling histogram (2D views) interactions of <code>ThresholdEffect</code> (<a href="https://github.com/Slicer/Slicer/pull/7695">PR-7695</a>)</li>
<li>Simplify paint/erase diameter options for a more concise UI (<a href="https://github.com/Slicer/Slicer/pull/7278">PR-7278</a>)</li>
<li>Add <code>SegmentationGeometryLogic</code> API to set reference image geometry (<a href="https://github.com/Slicer/Slicer/pull/7607">PR-7607</a>)</li>
<li>Make <code>SegmentsTableView</code> functions available from Python (<a href="https://github.com/Slicer/Slicer/pull/7829">PR-7829</a>)</li>
<li>Change log level in Islands effect (<a href="https://github.com/Slicer/Slicer/pull/7848">PR-7848</a>)</li>
<li>Allow one draw effect point without preventing use in other slice offsets (<a href="https://github.com/Slicer/Slicer/pull/6997">PR-6997</a>)</li>
<li>Fix smoothing effect for all visible segments (<a href="https://github.com/Slicer/Slicer/pull/7483">PR-7483</a>)</li>
<li>Fix Mask volume effect node selector (<a href="https://github.com/Slicer/Slicer/pull/7478">PR-7478</a>)</li>
<li>Fix segment disappearing when sharing Segment Editor node between widgets (<a href="https://github.com/Slicer/Slicer/pull/7577">PR-7577</a>)</li>
<li>Fix loading of an empty segmentation (<a href="https://github.com/Slicer/Slicer/pull/7609">PR-7609</a>)</li>
<li>Fix issues caused by invalid Segmentation binary labelmap scalar types (<a href="https://github.com/Slicer/Slicer/pull/7605">PR-7605</a>)</li>
<li>Fix “Show 3D” button staying disabled (<a href="https://github.com/Slicer/Slicer/pull/7962">PR-7962</a>)</li>
<li>Fix visibility column in segment list (<a href="https://github.com/Slicer/Slicer/pull/8048">PR-8048</a>)</li>
<li>Fix segments not visible after thresholding (<a href="https://github.com/Slicer/Slicer/pull/8060">PR-8060</a>)</li>
<li>Fix name editing in Segment Editor (<a href="https://github.com/Slicer/Slicer/pull/8071">PR-8071</a>)</li>
<li>Fix output volume node selector in Mask Volume effect (<a href="https://github.com/Slicer/Slicer/pull/7939">PR-7939</a>)</li>
</ul>
<h3 id="heading--segment-statistics">Segment Statistics</h3>
<ul>
<li>Add percentiles computation to Segment Statistics scalar volume plugin (<a href="https://github.com/Slicer/Slicer/pull/8037">PR-8037</a>)</li>
</ul>
<h3 id="heading--sequences">Sequences</h3>
<ul>
<li>Recognize sequences generated by dcm2niix (<a href="https://github.com/Slicer/Slicer/pull/7871">PR-7871</a>)</li>
<li>Fix empty candidate node list in Sequences module (<a href="https://github.com/Slicer/Slicer/pull/7506">PR-7506</a>)</li>
<li>Increase minimum size of Sequences intensity plot (<a href="https://github.com/Slicer/Slicer/pull/7871">PR-7871</a>)</li>
<li>Fix saving of labelmap volume sequences (<a href="https://github.com/Slicer/Slicer/pull/7946">PR-7946</a>)</li>
<li>Make <code>qMRMLSequenceBrowserPlayWidget</code> shortcuts accessible from Python (<a href="https://github.com/Slicer/Slicer/pull/7715">PR-7715</a>)</li>
<li>Ensure selected item number in Sequence browser remains valid (<a href="https://github.com/Slicer/Slicer/pull/7458">PR-7458</a>)</li>
<li>Fix deletion of the last time point in a sequence (<a href="https://github.com/Slicer/Slicer/pull/7559">PR-7559</a>)</li>
<li>Fix warning when browsing a transform node sequence (<a href="https://github.com/Slicer/Slicer/pull/8116">PR-8116</a>)</li>
</ul>
<h3 id="heading--subject-hierarchy">Subject Hierarchy</h3>
<ul>
<li>Improve SubjectHierarchy API for UIDs (<a href="https://github.com/Slicer/Slicer/pull/7616">PR-7616</a>)</li>
<li>Fix loading of <code>SubjectHierarchyPlugin</code>s at startup (<a href="https://github.com/Slicer/Slicer/pull/7477">PR-7477</a>)</li>
<li>Add SH options to control transform interaction handle type visibility (<a href="https://github.com/Slicer/Slicer/pull/7673">PR-7673</a>)</li>
<li>Fix subject hierarchy consolidation after loading a scene (<a href="https://github.com/Slicer/Slicer/pull/7616">PR-7616</a>)</li>
<li>Do not deselect items in <code>SHTree::setCurrentItems</code> before reselecting them (<a href="https://github.com/Slicer/Slicer/pull/7452">PR-7452</a>)</li>
<li>Fix subject hierarchy help button tooltip appearance in dark mode (<a href="https://github.com/Slicer/Slicer/pull/7906">PR-7906</a>)</li>
</ul>
<h3 id="heading--texts">Texts</h3>
<ul>
<li>Allow <code>vtkMRMLTextStorageNode</code> to store any text files (<a href="https://github.com/Slicer/Slicer/pull/7961">PR-7961</a>)</li>
</ul>
<h3 id="heading--terminologies">Terminologies</h3>
<ul>
<li>Improve terminology selector (<a href="https://github.com/Slicer/Slicer/pull/7691">PR-7691</a>)</li>
<li>Improve terminology selector speed (<a href="https://github.com/Slicer/Slicer/pull/7714">PR-7714</a>)</li>
<li>Make terminology code finding more robust (<a href="https://github.com/Slicer/Slicer/pull/8003">PR-8003</a>)</li>
<li>Add API for finding terminology from codes (<a href="https://github.com/Slicer/Slicer/pull/7735">PR-7735</a>)</li>
<li>Add methods for comparing terminologies (<a href="https://github.com/Slicer/Slicer/pull/7809">PR-7809</a>)</li>
<li>Improve terminology category selection (<a href="https://github.com/Slicer/Slicer/pull/7976">PR-7976</a>)</li>
<li>Add Python-wrappable methods for accessing anatomical regions (<a href="https://github.com/Slicer/Slicer/pull/7687">PR-7687</a>)</li>
<li>Fix condition for customization in <code>qSlicerTerminologyItemDelegate</code> (<a href="https://github.com/Slicer/Slicer/pull/8059">PR-8059</a>)</li>
</ul>
<h3 id="heading--transforms">Transforms</h3>
<ul>
<li>Add interaction handle visualization for linear transform nodes (<a href="https://github.com/Slicer/Slicer/pull/7562">PR-7562</a>, <a href="https://github.com/Slicer/Slicer/pull/7590">PR-7590</a>)</li>
<li>Improve interaction options in Transforms SH plugin and module widget (<a href="https://github.com/Slicer/Slicer/pull/7599">PR-7599</a>)</li>
<li>Add finer control of 2D interaction handle axis display (<a href="https://github.com/Slicer/Slicer/pull/7586">PR-7586</a>)</li>
<li>Add “jump to handle” action for interaction handles (<a href="https://github.com/Slicer/Slicer/pull/7595">PR-7595</a>)</li>
<li>Add “cancel” action for interaction handles (<a href="https://github.com/Slicer/Slicer/pull/7600">PR-7600</a>)</li>
<li>Add transform plugin in subject hierarchy tree view (<a href="https://github.com/Slicer/Slicer/pull/7997">PR-7997</a>)</li>
<li>Fix issue saving transform with a non-origin center of transformation (<a href="https://github.com/Slicer/Slicer/pull/7878">PR-7878</a>)</li>
<li>Fix editing of transform component values in spinbox (<a href="https://github.com/Slicer/Slicer/pull/7942">PR-7942</a>)</li>
<li>Resolve interaction handles rendering issues (<a href="https://github.com/Slicer/Slicer/pull/7903">PR-7903</a>)</li>
</ul>
<h3 id="heading--volume-rendering">Volume Rendering</h3>
<ul>
<li>Make volume rendering preset registration more robust (<a href="https://github.com/Slicer/Slicer/pull/7610">PR-7610</a>)</li>
<li>Fix volume rendering property always marked as modified (<a href="https://github.com/Slicer/Slicer/pull/8029">PR-8029</a>)</li>
</ul>
<h3 id="heading--webserver">WebServer</h3>
<ul>
<li>Control the amount of console output from the Python web proxy (<a href="https://github.com/Slicer/Slicer/pull/7950">PR-7950</a>)</li>
<li>Add WebServer example scripts (<a href="https://github.com/Slicer/Slicer/pull/7841">PR-7841</a>)</li>
<li>Fix WebServer script repository formatting (<a href="https://github.com/Slicer/Slicer/pull/7843">PR-7843</a>)</li>
<li>Update HTTPS support and add WebXR demo as transform controller (<a href="https://github.com/Slicer/Slicer/pull/7568">PR-7568</a>)</li>
<li>Support returning results when executing Python from <code>qSlicerWebWidget</code> (<a href="https://github.com/Slicer/Slicer/pull/7624">PR-7624</a>)</li>
<li>Add missing OPTIONS request handler when CORS is enabled (<a href="https://github.com/Slicer/Slicer/pull/7998">PR-7998</a>)</li>
</ul>
<h2 id="heading--infrastructure">Infrastructure</h2>
<h3 id="heading--packaging">Packaging</h3>
<ul>
<li>Ensure packaging of the latest <code>d3dcompiler_47.dll</code> for <code>SlicerVirtualReality</code> (<a href="https://github.com/Slicer/Slicer/pull/7571">PR-7571</a>)</li>
<li>Ensure launcher scripts installed from wheels remain accessible (<a href="https://github.com/Slicer/Slicer/pull/7587">PR-7587</a>)</li>
<li>Include runtime libraries to ensure compatibility in <code>SlicerExecutionModel</code> (<a href="https://github.com/Slicer/Slicer/pull/8149">PR-8149</a>)</li>
</ul>
<h3 id="heading--testing">Testing</h3>
<ul>
<li>Fix <code>vtkMRMLCameraDisplayableManagerTest1.mrml</code> (<a href="https://github.com/Slicer/Slicer/pull/7517">PR-7517</a>)</li>
<li>Fix <code>vtkMRMLTransformStorageNodeTest1</code> in debug mode (<a href="https://github.com/Slicer/Slicer/pull/8029">PR-8029</a>)</li>
<li>Fix <code>py_SlicerRestoreSceneViewCrashIssue3445</code> test in debug mode (<a href="https://github.com/Slicer/Slicer/pull/8029">PR-8029</a>)</li>
<li>Fix <code>qSlicerExtensionsManagerModelTest</code> (<a href="https://github.com/Slicer/Slicer/pull/7584">PR-7584</a>)</li>
<li>Fix <code>vtkMRMLVolumeArchetypeStorageNodeTest1.cxx</code> (<a href="https://github.com/Slicer/Slicer/pull/7734">PR-7734</a>)</li>
<li>Fix <code>MRMLDisplayableManagerCxxTests</code> (<a href="https://github.com/Slicer/Slicer/pull/7734">PR-7734</a>)</li>
<li>Fix SampleData tests to align with revised file loading behavior (<a href="https://github.com/Slicer/Slicer/pull/8162">PR-8162</a>)</li>
<li>Fix self-tests by explicitly setting file loading parameters (<a href="https://github.com/Slicer/Slicer/pull/8164">PR-8164</a>)</li>
</ul>
<h3 id="heading--continuous-integration-ci">Continuous integration (CI)</h3>
<ul>
<li>Add GitHub workflow for keeping pre-commit configuration up to date (<a href="https://github.com/Slicer/Slicer/pull/7636">PR-7636</a>)</li>
<li>Add GitHub workflow to update the <code>nightly-main</code> branch daily (<a href="https://github.com/Slicer/Slicer/pull/7953">PR-7953</a>)</li>
<li>Skip “CI (Build)” workflow if only SuperBuild changes on <code>nightly-main</code> (<a href="https://github.com/Slicer/Slicer/pull/7945">PR-7945</a>)</li>
<li>Speed up doxygen generation by enabling parallel build (<a href="https://github.com/Slicer/Slicer/pull/8138">PR-8138</a>)</li>
<li>Add GitHub workflow to trigger Doxygen build and publish (<a href="https://github.com/Slicer/Slicer/pull/8144">PR-8144</a>)</li>
<li>Fix GitHub workflow for daily updates to <code>nightly-main</code> branch (<a href="https://github.com/Slicer/Slicer/pull/7955">PR-7955</a>)</li>
<li>Fix GitHub workflow authentication for “Update Preview Branch” (<a href="https://github.com/Slicer/Slicer/pull/7965">PR-7965</a>)</li>
<li>Update <code>.gitignore</code> to ensure changes to <code>.github</code> files are reported (<a href="https://github.com/Slicer/Slicer/pull/7635">PR-7635</a>)</li>
<li>Add support for codespell 2.3.0 and fix identified typos (<a href="https://github.com/Slicer/Slicer/pull/7762">PR-7762</a>)</li>
<li>Add support for codespell 2.4.0 and fix identified typos (<a href="https://github.com/Slicer/Slicer/pull/8158">PR-8158</a>)</li>
<li>Fix source files and <strong>update</strong> pre-commit setting to run additional hooks (<a href="https://github.com/Slicer/Slicer/pull/7647">PR-7647</a>)</li>
<li>Update “commit-message” workflow to use dedicated GitHub action (<a href="https://github.com/Slicer/Slicer/pull/7925">PR-7925</a>)</li>
<li>Fix manual trigger of Doxygen build/publish through GitHub UI (<a href="https://github.com/Slicer/Slicer/pull/8146">PR-8146</a>)</li>
<li>Fix pull request description generated by pre-commit-autoupdate workflow (<a href="https://github.com/Slicer/Slicer/pull/7688">PR-7688</a>)</li>
<li>Fix workflow file link in pre-commit-autoupdate workflow (<a href="https://github.com/Slicer/Slicer/pull/7690">PR-7690</a>)</li>
<li>Fix version extraction in pre-commit-autoupdate workflow (<a href="https://github.com/Slicer/Slicer/pull/7755">PR-7755</a>)</li>
</ul>
<h3 id="heading--build-system">Build system</h3>
<ul>
<li>Update acceptable VS2022 MSVC version for TBB install (<a href="https://github.com/Slicer/Slicer/pull/7833">PR-7833</a>)</li>
<li>Remove obsolete WebKit-specific integration code from <code>qSlicerWebWidget</code> (<a href="https://github.com/Slicer/Slicer/pull/7625">PR-7625</a>)</li>
<li>Drop support for MSVC toolset v141 (Visual Studio 2017) (<a href="https://github.com/Slicer/Slicer/pull/7989">PR-7989</a>)</li>
<li>Enable OpenSSL support in DCMTK build (<a href="https://github.com/Slicer/Slicer/pull/8106">PR-8106</a>)</li>
<li>Fix generation of additional launcher settings for list-based settings (<a href="https://github.com/Slicer/Slicer/pull/7485">PR-7485</a>)</li>
<li>Re-generate additional launcher settings if they are updated (<a href="https://github.com/Slicer/Slicer/pull/7486">PR-7486</a>)</li>
<li>Ensure full path ID for macOS libraries installed for fixup (<a href="https://github.com/Slicer/Slicer/pull/7537">PR-7537</a>)</li>
<li>Prefer clearing <code>CMAKE_INSTALL_NAME_TOOL</code> on a per-project basis (<a href="https://github.com/Slicer/Slicer/pull/7540">PR-7540</a>)</li>
<li>Fix ITK’s threading-related method name deprecation warnings (<a href="https://github.com/Slicer/Slicer/pull/7400">PR-7400</a>)</li>
<li>Fix extension build to ensure build dependency directories are passed (<a href="https://github.com/Slicer/Slicer/pull/7712">PR-7712</a>)</li>
<li>Remove redundant call in <code>vtkITKMorphologicalContourInterpolator</code> (<a href="https://github.com/Slicer/Slicer/pull/7723">PR-7723</a>)</li>
<li>Resolve deprecated warning in MRML testing macro for <code>std::string</code> (<a href="https://github.com/Slicer/Slicer/pull/8041">PR-8041</a>)</li>
<li>Replace <code>vtkStdString</code> with <code>std::string</code> (<a href="https://github.com/Slicer/Slicer/pull/8042">PR-8042</a>)</li>
</ul>
<h3 id="heading--platform-support">Platform support</h3>
<ul>
<li>Add support for configuring <code>_manylinux</code> module (<a href="https://github.com/Slicer/Slicer/pull/8168">PR-8168</a>)</li>
<li>Update minimum required <code>CMAKE_OSX_DEPLOYMENT_TARGET</code> to 13.0 (<a href="https://github.com/Slicer/Slicer/pull/7990">PR-7990</a>)</li>
<li>Fix fatal error not reported for MSVC + TBB compatibility (<a href="https://github.com/Slicer/Slicer/pull/7834">PR-7834</a>)</li>
</ul>
<h3 id="heading--dependencies">Dependencies</h3>
<p><strong>CTK:</strong></p>
<ul>
<li>Update CTK DICOM Database version from <code>0.7.0</code> to <code>0.8.0</code> (<a href="https://github.com/Slicer/Slicer/pull/7472">PR-7472</a>)</li>
<li>Update CTK (<a href="https://github.com/Slicer/Slicer/pull/7544">PR-7544</a>, <a href="https://github.com/Slicer/Slicer/pull/7558">PR-7558</a>, <a href="https://github.com/Slicer/Slicer/pull/7964">PR-7964</a>)</li>
<li>Add <code>removePatient/Series/Study</code> signals to DICOM database (<a href="https://github.com/Slicer/Slicer/pull/7549">PR-7549</a>)</li>
<li>Backport PythonQt fixes &amp; restore script compilation to <code>.pyc</code> (<a href="https://github.com/Slicer/Slicer/pull/7561">PR-7561</a>)</li>
<li>Fix Qt designer crash at startup (<a href="https://github.com/Slicer/Slicer/pull/7585">PR-7585</a>)</li>
</ul>
<p><strong>DCMTK:</strong></p>
<ul>
<li>Update DCMTK from <code>3.6.6</code> to <code>3.6.8</code> (<a href="https://github.com/Slicer/Slicer/pull/8018">PR-8018</a>)</li>
<li>Backport fixes for CVE-2022-2119 and CVE-2022-2120 (<a href="https://github.com/Slicer/Slicer/pull/8017">PR-8017</a>)</li>
</ul>
<p><strong>ITK:</strong></p>
<ul>
<li>Update ITK to <code>5.4.0</code> (<a href="https://github.com/Slicer/Slicer/pull/7771">PR-7771</a>)</li>
<li>Fix HDF5 symbol clash when importing ITK wheel (<a href="https://github.com/Slicer/Slicer/pull/7838">PR-7838</a>)</li>
</ul>
<p><strong>libarchive:</strong></p>
<ul>
<li>Fix libarchive build error with Clang 16 (<a href="https://github.com/Slicer/Slicer/pull/8097">PR-8097</a>)</li>
</ul>
<p><strong>VTK:</strong></p>
<ul>
<li>Backport selected Rendering, OpenVR, and OpenXR patches (<a href="https://github.com/Slicer/Slicer/pull/7487">PR-7487</a>)</li>
<li>Backport VR, OpenVR, and OpenXR improvements (<a href="https://github.com/Slicer/Slicer/pull/7514">PR-7514</a>, <a href="https://github.com/Slicer/Slicer/pull/7516">PR-7516</a>)</li>
<li>Backport OpenXR-SDK improvements for streamlined integration (<a href="https://github.com/Slicer/Slicer/pull/7529">PR-7529</a>)</li>
<li>Backport support for <code>Holographic.Remoting.OpenXr &gt;= 2.9.3</code> (<a href="https://github.com/Slicer/Slicer/pull/7534">PR-7534</a>)</li>
<li>Backport fix for OpenVR gesture recognition (<a href="https://github.com/Slicer/Slicer/pull/7503">PR-7503</a>)</li>
<li>Backport <code>vtkSSAOPass</code> fixes (<a href="https://github.com/Slicer/Slicer/pull/7554">PR-7554</a>)</li>
<li>Backport <code>vtkSSAOPass</code> intensity adjustment feature (<a href="https://github.com/Slicer/Slicer/pull/7820">PR-7820</a>)</li>
<li>Fix preprocessor expression in <code>vtkOpenGLRenderWindow</code> (<a href="https://github.com/Slicer/Slicer/pull/7505">PR-7505</a>)</li>
<li>Backport deprecation macro update (<a href="https://github.com/Slicer/Slicer/pull/7508">PR-7508</a>)</li>
</ul>
<p><strong>Other Dependencies:</strong></p>
<ul>
<li>Update <code>FindVcvars</code> for future MSVC versions (<a href="https://github.com/Slicer/Slicer/pull/7815">PR-7815</a>)</li>
<li>Update <code>LandmarkRegistration</code> in <code>SuperBuild.cmake</code> (<a href="https://github.com/Slicer/Slicer/pull/7977">PR-7977</a>)</li>
<li>Update Python packages to latest (<a href="https://github.com/Slicer/Slicer/pull/7597">PR-7597</a>, <a href="https://github.com/Slicer/Slicer/pull/7776">PR-7776</a>)</li>
<li>Update <code>SimpleITK</code> to fix missing use of custom namespace (<a href="https://github.com/Slicer/Slicer/pull/7812">PR-7812</a>)</li>
<li>Update <code>SlicerSurfaceToolbox</code> to include dynamic modeler extrude tool (<a href="https://github.com/Slicer/Slicer/pull/8145">PR-8145</a>)</li>
</ul>
<h3 id="heading--custom-slicer-application-support">Custom Slicer application support</h3>
<h4><a name="p-123146-slicer-application-2" class="anchor" href="#p-123146-slicer-application-2" aria-label="Heading link"></a>Slicer Application</h4>
<ul>
<li>Improve and <strong>customize</strong> URI argument handling for custom applications (<a href="https://github.com/Slicer/Slicer/pull/7938">PR-7938</a>)</li>
<li>Support customizing interaction widget event translation (<a href="https://github.com/Slicer/Slicer/pull/8101">PR-8101</a>)</li>
<li>Fix <code>sitkUtils</code> without <code>MRMLIDImageIO</code> (<a href="https://github.com/Slicer/Slicer/pull/7940">PR-7940</a>)</li>
</ul>
<h4><a name="p-123146-build-system-3" class="anchor" href="#p-123146-build-system-3" aria-label="Heading link"></a>Build-System</h4>
<ul>
<li>Support reuse of “commit-message” GitHub workflow (<a href="https://github.com/Slicer/Slicer/pull/7898">PR-7898</a>)</li>
<li>Update “pre-commit” workflow to support reuse from private projects (<a href="https://github.com/Slicer/Slicer/pull/7900">PR-7900</a>)</li>
<li>Fix collision of main project source dir with extension of same name (<a href="https://github.com/Slicer/Slicer/pull/7724">PR-7724</a>)</li>
</ul>
<h2 id="heading--extensions">Extensions</h2>
<p><em>Listed below are extensions added, removed or updated since the 5.6 release.</em></p>
<p>The Slicer <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html">extensions manager</a> enables Slicer users to install more than 190 extensions written and contributed by their peers from around the world.</p>
<h3 id="heading--new">New</h3>
<ul>
<li>
<p><a href="https://github.com/supervisely-ecosystem/SlicerConnectToSupervisely">ConnectToSupervisely</a>: Extension designed to organize and manage the work of labeling teams on the Supervisely computer vision platform.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><img src="https://github.com/supervisely-ecosystem/SlicerConnectToSupervisely/raw/master/Images/icon_png_128x128.png" alt="" role="presentation" width="128" height="128"></th>
<th><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef55f9fb1b94c025e6e04c40d85d277c9c15e6ac.jpeg" data-download-href="/uploads/short-url/y9gjN3oAZu8vAb5xNrYdCIFKoMc.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef55f9fb1b94c025e6e04c40d85d277c9c15e6ac_2_660x500.jpeg" alt="image" data-base62-sha1="y9gjN3oAZu8vAb5xNrYdCIFKoMc" width="660" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef55f9fb1b94c025e6e04c40d85d277c9c15e6ac_2_660x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef55f9fb1b94c025e6e04c40d85d277c9c15e6ac_2_990x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef55f9fb1b94c025e6e04c40d85d277c9c15e6ac_2_1320x1000.jpeg 2x" data-dominant-color="7B7579"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1562×1183 432 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/LOAMRI/Slicer-DTI-ALPS">DTI-ALPS</a>: Calculate the diffusion tensor image analysis along the perivascular space</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><img src="https://github.com/LOAMRI/Slicer-DTI-ALPS/raw/main/DTI_ALPS.png" alt="" role="presentation" width="128" height="128"></th>
<th><img src="https://github.com/LOAMRI/Slicer-DTI-ALPS/raw/main/docs/assets/DTI-ALPS-NMO-patients.png" alt="" role="presentation" width="690" height="255"></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/dmolony3/SlicerFractionalMyocardialMass">FractionalMyocardialMass</a>: Computation of fractional myocardial mass (FMM) and myocardial mass at risk (MMAR).</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><img src="https://raw.githubusercontent.com/dmolony3/SlicerFractionalMyocardialMass/main/FMM.png" alt="" role="presentation" width="128" height="128"></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/ciroraggio/SlicerImageAugmenter">ImageAugmenter</a> is a MONAI- and PyTorch-based medical image augmentation tool for 3D Slicer. Inspired by the <a href="https://github.com/ciroraggio/AugmentedDataLoader">AugmentedDataLoader</a>, it applies a range of transformations to each image, expanding the training dataset for deep learning models with minimal coding effort.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e2dc7b4ca97f320304fb5e18463f60c4a1b8e85.jpeg" data-download-href="/uploads/short-url/6Aw2UTavYnLFmSzXFmbvPTp5upT.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e2dc7b4ca97f320304fb5e18463f60c4a1b8e85_2_250x250.jpeg" alt="image" data-base62-sha1="6Aw2UTavYnLFmSzXFmbvPTp5upT" width="250" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e2dc7b4ca97f320304fb5e18463f60c4a1b8e85_2_250x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e2dc7b4ca97f320304fb5e18463f60c4a1b8e85_2_375x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e2dc7b4ca97f320304fb5e18463f60c4a1b8e85_2_500x500.jpeg 2x" data-dominant-color="AAAAAF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">800×800 98.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><a href="https://github.com/CSIM-Toolkits/Slicer-LesionSimulatorExtension">LesionSimulator</a>: Provides a toolkit for Multiple Sclerosis lesion simulation in multimodal MRI images, such as T1, T2, T2-FLAIR and DTI scalar maps.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><img src="https://github.com/CSIM-Toolkits/Slicer-LesionSimulatorExtension/raw/main/LesionSimulator.png" alt="" role="presentation" width="128" height="128"></th>
<th><img src="https://github.com/CSIM-Toolkits/Slicer-LesionSimulatorExtension/raw/main/docs/assets/3DLesionsOverlay.png" alt="" role="presentation" width="552" height="500"></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/CSIM-Toolkits/LesionSpotlightExtension">LesionSpotlight</a>: Provides modern T2-FLAIR MRI segmentation and enhancement methods that highlight abnormal white matter voxels, enabling increased contrast and segmentation of hyperintense Multiple Sclerosis lesions.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><img src="https://github.com/CSIM-Toolkits/Slicer-LesionSpotlightExtension/raw/main/LesionSpotlight.png" alt="" role="presentation" width="128" height="128"></th>
<th><img src="https://github.com/CSIM-Toolkits/Slicer-LesionSpotlightExtension/raw/main/docs/assets/T2FLAIR_patient_lesionLabel_AFT.png" alt="" role="presentation" width="417" height="500"></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/jamzad/SlicerMassVision">MassVision</a>: End-to-end AI solution for Mass Spectrometry Imaging (MSI) data, enabling targeted and non-targeted visualization, histopathology-driven co-localization, dataset curation with spatial and spectral guidance, multi-slide data alignment and denoising, AI model training and validation, and whole-slide AI deployment.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c36e1e087fd45fee5ad8f2715ce15b6e854d608.jpeg" data-download-href="/uploads/short-url/6j8ANCEfrNxooQow1DYA5DjboLe.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c36e1e087fd45fee5ad8f2715ce15b6e854d608_2_434x500.jpeg" alt="image" data-base62-sha1="6j8ANCEfrNxooQow1DYA5DjboLe" width="434" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c36e1e087fd45fee5ad8f2715ce15b6e854d608_2_434x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c36e1e087fd45fee5ad8f2715ce15b6e854d608_2_651x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c36e1e087fd45fee5ad8f2715ce15b6e854d608_2_868x1000.jpeg 2x" data-dominant-color="A3989D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1346×1550 208 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></th>
<th><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/079d7418d38bec7ecfe9d85bdea0d9259975c361.jpeg" data-download-href="/uploads/short-url/15mGsDwstO9AGgQudyQpIF6Fq6d.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/079d7418d38bec7ecfe9d85bdea0d9259975c361_2_690x309.jpeg" alt="image" data-base62-sha1="15mGsDwstO9AGgQudyQpIF6Fq6d" width="690" height="309" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/079d7418d38bec7ecfe9d85bdea0d9259975c361_2_690x309.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/079d7418d38bec7ecfe9d85bdea0d9259975c361_2_1035x463.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/079d7418d38bec7ecfe9d85bdea0d9259975c361_2_1380x618.jpeg 2x" data-dominant-color="40393D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×717 87.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/pieper/SlicerMorphoDepot">MorphoDepot</a>: use GitHub infrastructure to manage multi-person segmentation projects.</p>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7b4cbca8c959e1202af2e9a152ade130523c7ff.png" data-download-href="/uploads/short-url/uMe0C7AjAjZD0fff48vHgnu5Lsz.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7b4cbca8c959e1202af2e9a152ade130523c7ff_2_300x300.png" alt="image" data-base62-sha1="uMe0C7AjAjZD0fff48vHgnu5Lsz" width="300" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7b4cbca8c959e1202af2e9a152ade130523c7ff_2_300x300.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7b4cbca8c959e1202af2e9a152ade130523c7ff_2_450x450.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7b4cbca8c959e1202af2e9a152ade130523c7ff.png 2x" data-dominant-color="94908A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">512×512 42.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li><a href="https://github.com/WashUMusculoskeletalCore/Slicer-MusculoskeletalAnalysis">MusculoskeletalAnalysis</a>: Analyzes 3D musculoskeletal images and generates reports.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cfa3998092c4639bb0a6e30c7ac3515a7d90a67.png" data-download-href="/uploads/short-url/dgw1YjDOmCBzcdXnmX8q6QJp4Cr.png?dl=1" title="MusculoskeletalAnalysis-modified"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cfa3998092c4639bb0a6e30c7ac3515a7d90a67_2_250x250.png" alt="MusculoskeletalAnalysis-modified" data-base62-sha1="dgw1YjDOmCBzcdXnmX8q6QJp4Cr" width="250" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cfa3998092c4639bb0a6e30c7ac3515a7d90a67_2_250x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cfa3998092c4639bb0a6e30c7ac3515a7d90a67_2_375x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cfa3998092c4639bb0a6e30c7ac3515a7d90a67_2_500x500.png 2x" data-dominant-color="CCE6F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MusculoskeletalAnalysis-modified</span><span class="informations">800×800 304 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>
<p><a href="https://discourse.slicer.org/t/photogrammetry-extension-is-released/41891">Photogrammetry</a>: Preprocess (mask) large collections of photographs which then can be processed to construct 3D models with texture.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0ccf566ed801eaae4057dd176c32e84312c1717.png" data-download-href="/uploads/short-url/w4G4EUFBjTqjoFiLcNjNszEnbNB.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ccf566ed801eaae4057dd176c32e84312c1717_2_250x250.png" alt="image" data-base62-sha1="w4G4EUFBjTqjoFiLcNjNszEnbNB" width="250" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ccf566ed801eaae4057dd176c32e84312c1717_2_250x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ccf566ed801eaae4057dd176c32e84312c1717_2_375x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e0ccf566ed801eaae4057dd176c32e84312c1717_2_500x500.png 2x" data-dominant-color="858481"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">512×512 62.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><a href="https://github.com/SlicerMorph/SlicerEditor">ScriptEditor</a>: A script editor. It allows auto complete, text highlighting and saving of the python scripts as text nodes into the scene. To execute a code, highlight in the editor, hit copy and then manually paste it into the python console.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><img src="https://github.com/SlicerMorph/SlicerScriptEditor/raw/main/ScriptEditor.png" alt="" role="presentation" width="690" height="388"></th>
<th><img src="https://github.com/SlicerMorph/SlicerScriptEditor/raw/main/screenshot.png" alt="" role="presentation" width="459" height="489"></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/cpinter/SlicerSegmentationVerification">SegmentationVerification</a>: Enables quick review and verification of AI segmentation results by inspecting each segment (mask or label).</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><img src="https://raw.githubusercontent.com/cpinter/SlicerSegmentationVerification/main/SegmentationVerification.png" alt="" role="presentation" width="500" height="500"></th>
<th><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/288bb4c5dfd8906253815208544146f7ff1460ef.jpeg" data-download-href="/uploads/short-url/5MGpUdLzKzeXidoNvgKdN7QxhDx.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/288bb4c5dfd8906253815208544146f7ff1460ef_2_690x388.jpeg" alt="image" data-base62-sha1="5MGpUdLzKzeXidoNvgKdN7QxhDx" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/288bb4c5dfd8906253815208544146f7ff1460ef_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/288bb4c5dfd8906253815208544146f7ff1460ef_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/288bb4c5dfd8906253815208544146f7ff1460ef_2_1380x776.jpeg 2x" data-dominant-color="9D9998"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/mazurowski-lab/SlicerSegmentHumanBody">SegmentHumanBody</a>: Integrate the SegmentAnyBone developed by Mazurowski Lab.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dcaf05e1838a0c699a899551a8925ca2a624663.png" data-download-href="/uploads/short-url/1Y106QkRUIJSSju1UWfsvfz6pO3.png?dl=1" title="SegmentHumanBody-modified"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0dcaf05e1838a0c699a899551a8925ca2a624663.png" alt="SegmentHumanBody-modified" data-base62-sha1="1Y106QkRUIJSSju1UWfsvfz6pO3" width="203" height="203"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SegmentHumanBody-modified</span><span class="informations">271×271 16.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><a href="https://github.com/laboratory-for-translational-medicine/SlicerCineTrack">SlicerCineTrack</a>: Visual verification of target tracking results. The extension enables target tracking visualization by replaying cine 2D images and overlays the outline of the Region of interest (ROI) using a displacement data file.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th style="text-align:center"><img src="https://raw.githubusercontent.com/slicercinetrack/slicercinetrack.github.io/main/resources/SlicerCineTrack_logo.png" alt="" role="presentation" width="100" height="100"></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/CSIM-Toolkits/SlicerDiffusionComplexityMap">SlicerDiffusionComplexityMap</a>: Image processing technique using the principle of diffusion distribution evaluation regarding the LMC complexity measure</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><img src="https://github.com/CSIM-Toolkits/SlicerDiffusionComplexityMap/raw/main/DiffusionComplexityMap.png" alt="" role="presentation" width="128" height="128"></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/mprires/SlicerMOOSE">SlicerMOOSE</a>: MOOSE (Multi-organ objective segmentation) is a data-centric AI solution that generates multilabel organ segmentations to facilitate systemic TB whole-person research.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><img src="https://github.com/mprires/SlicerMOOSE/raw/main/Images/SlicerMOOSE_Screenshot1.png" alt="" role="presentation" width="690" height="460"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/neuropacs/SlicerNeuropacs">SlicerNeuropacs</a>: Receive and analyze diffusion MRI data from patients aged 40 years and older presenting with Parkinson’s disease (PD) symptoms.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><img src="https://github.com/neuropacs/SlicerNeuropacs/raw/main/NeuropacsSlicerExtension.png" alt="" role="presentation" width="64" height="64"></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/Slicer/SlicerSOFA">SlicerSOFA</a>: Integrate mechanical simulations with 3D Slicer. This extension integrates the <a href="https://sofa-framework.org">SOFA Framework</a> in 3D Slicer to facilitate the development and execution of mechanical simulations involving 3D meshes, medical-image volumes and interaction with <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html">3D Slicer markups</a>. Currently, the extension enables the use of the SOFA API in python and provides its own SlicerSOFA API (optional) to set up a simulation and transfer data between 3D Slicer objects and SOFA objects</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><img src="https://raw.githubusercontent.com/RafaelPalomar/SlicerSOFA/main/slicer-sofa-logo.png" alt="" role="presentation" width="500" height="500"></th>
<th><img src="https://github.com/Slicer/SlicerSOFA/raw/main/Screenshots/SoftTissueSimulationScreenshot_1.png" alt="" role="presentation" width="690" height="405"></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/SlicerDMRI/SlicerTractParcellation">SlicerTractParcellation</a>: Automatic parcellation of white matter tractography using <a href="https://whitematteranalysis.readthedocs.io/en/latest/index.html">White matter analysis (WMA)</a> method and <a href="https://dmri.slicer.org/atlases/">O’Donnell Research Group (ORG) atlas</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9f5229c048f015c2f44c6db90d7a5a41779f0e0.jpeg" data-download-href="/uploads/short-url/qx3wY5OLka6cdzW5wz4sWzK46EU.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9f5229c048f015c2f44c6db90d7a5a41779f0e0_2_306x250.jpeg" alt="image" data-base62-sha1="qx3wY5OLka6cdzW5wz4sWzK46EU" width="306" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9f5229c048f015c2f44c6db90d7a5a41779f0e0_2_306x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9f5229c048f015c2f44c6db90d7a5a41779f0e0_2_459x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9f5229c048f015c2f44c6db90d7a5a41779f0e0_2_612x500.jpeg 2x" data-dominant-color="C8C5C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1016×828 202 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><a href="https://github.com/SlicerLatinAmerica/SlicerTutorialMaker">TutorialMaker</a>: Streamline the creation of 3D Slicer tutorials in multiple languages.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><img src="https://github.com/SlicerLatinAmerica/SlicerTutorialMaker/raw/main/TutorialMaker.png" alt="" role="presentation" width="256" height="256"></th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/SlicerUltrasound/SlicerUltrasound">Ultrasound</a>:  Provide modules to process ultrasound video data.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><img src="https://github.com/SlicerUltrasound/SlicerUltrasound/blob/main/Ultrasound.png?raw=true" alt="" role="presentation" width="126" height="126"></th>
<th><img src="https://github.com/SlicerUltrasound/SlicerUltrasound/raw/main/Screenshots/2024-04-14_AnonymizeUltrasound.png" alt="" role="presentation" width="690" height="388"></th>
</tr>
</thead>
<tbody>
<tr>
<td><img src="https://github.com/SlicerUltrasound/SlicerUltrasound/raw/main/Screenshots/2024-04-14_MmodeAnalysis.png" alt="" role="presentation" width="690" height="448"></td>
<td><img src="https://github.com/SlicerUltrasound/SlicerUltrasound/raw/main/Screenshots/TimeSeriesAnnotation_2024-06-27.png" alt="" role="presentation" width="690" height="413"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/uncbiag/SlicerUniGradICON">UniGradICON</a>: A Foundation Model for Medical Image Registration. The extension provides a Slicer interface for the model, allowing users to perform image registration tasks using the models.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><img src="https://github.com/uncbiag/SlicerUniGradICON/raw/main/screenshots/knee_example.png" alt="" role="presentation" width="690" height="338"></td>
<td><img src="https://github.com/uncbiag/SlicerUniGradICON/raw/main/screenshots/brain_example.png" alt="" role="presentation" width="690" height="338"></td>
</tr>
</tbody>
</table>
</div></li>
</ul>
<h3 id="heading--updated">Updated</h3>
<p>All the existing extensions have been maintained and updated to account for API and build environment changes.</p>
<h3 id="heading--removed">Removed</h3>
<p>Between Slicer 5.6 and Slicer 5.8, the extensions <code>iGyne</code> and <code>SlicerOpenCV</code> were removed.</p>
<p>List of archived extensions is documented at <a href="https://github.com/Slicer/ExtensionsIndex/blob/main/ARCHIVE/README.md">Slicer/ExtensionsIndex/ARCHIVE/README.md</a>.</p>

---

## Post #3 by @jcfr (2025-03-07 18:40 UTC)

<h1><a name="p-123147-changelog-581-1" class="anchor" href="#p-123147-changelog-581-1" aria-label="Heading link"></a>Changelog: 5.8.1</h1>
<ul>
<li><a href="#heading--core">Core</a>
<ul>
<li><a href="#heading--improvements">Improvements</a></li>
<li><a href="#heading--fixes">Fixes</a></li>
<li><a href="#heading--documentation">Documentation</a></li>
</ul>
</li>
<li><a href="#heading--infrastructure">Infrastructure</a>
<ul>
<li><a href="#heading--packaging">Packaging</a></li>
<li><a href="#heading--continuous-integration-ci">Continuous Integration (CI)</a></li>
<li><a href="#heading--dependencies">Dependencies</a></li>
</ul>
</li>
</ul>
<h2 id="heading--core">Core</h2>
<h3 id="heading--improvements">Improvements</h3>
<ul>
<li>Make maximum file length configurable (<a href="https://github.com/Slicer/Slicer/pull/8283">PR-8283</a>)</li>
<li>Update Slicer.crt CA bundle (<a href="https://github.com/Slicer/Slicer/pull/8269">PR-8269</a>)</li>
</ul>
<h3 id="heading--fixes">Fixes</h3>
<ul>
<li>Prevent loading DWMRI volumes as sequences (<a href="https://github.com/Slicer/Slicer/pull/8274">PR-8274</a>)</li>
<li>Fix crash in SystemTools::RemoveADirectory (<a href="https://github.com/Slicer/Slicer/pull/8275">PR-8275</a>)</li>
<li>Fix scene loading warning message (<a href="https://github.com/Slicer/Slicer/pull/8272">PR-8272</a>)</li>
<li>Prevent additional error message in DICOMReaders.py (<a href="https://github.com/Slicer/Slicer/pull/8271">PR-8271</a>)</li>
<li>Fix saving to .mrb files with long node names (<a href="https://github.com/Slicer/Slicer/pull/8270">PR-8270</a>)</li>
<li>Fix typo in “Grow From Seeds” help text (<a href="https://github.com/Slicer/Slicer/pull/8261">PR-8261</a>)</li>
</ul>
<h3 id="heading--documentation">Documentation</h3>
<ul>
<li>Dynamically generate links to Slicer Doxygen based on ReadTheDocs version (<a href="https://github.com/Slicer/Slicer/pull/8263">PR-8263</a>)</li>
<li>Fix links to Slicer Doxygen in the developer guide (<a href="https://github.com/Slicer/Slicer/pull/8262">PR-8262</a>)</li>
<li>Fix various broken documentation links in the developer guide (<a href="https://github.com/Slicer/Slicer/pull/8264">PR-8264</a>)</li>
<li>Update Transforms module API documentation to add missing Doxygen links (<a href="https://github.com/Slicer/Slicer/pull/8266">PR-8266</a>)</li>
<li>Add documentation for the Help menu (<a href="https://github.com/Slicer/Slicer/pull/8276">PR-8276</a>)</li>
</ul>
<h2 id="heading--infrastructure">Infrastructure</h2>
<h3 id="heading--packaging">Packaging</h3>
<ul>
<li>Improve NSIS Windows installer with application branding (<a href="https://github.com/Slicer/Slicer/pull/8268">PR-8268</a>)</li>
</ul>
<h3 id="heading--continuous-integration-ci">Continuous Integration (CI)</h3>
<ul>
<li>Update GitHub CI workflow to be release specific (<a href="https://github.com/Slicer/Slicer/pull/8259">PR-8259</a>)</li>
</ul>
<h3 id="heading--dependencies">Dependencies</h3>
<ul>
<li>Update VTK backporting fix to support building on Linux with clang (<a href="https://github.com/Slicer/Slicer/pull/8265">PR-8265</a>)</li>
<li>Update vtkAddon (<a href="https://github.com/Slicer/Slicer/pull/8273">PR-8273</a>)</li>
<li>Update BRAINSTools from 2024-05-31 to 2024-11-09 and include macOS build fix (<a href="https://github.com/Slicer/Slicer/pull/8267">PR-8267</a>)</li>
<li>Update python-cmake-buildsystem anticipating a Python version update (<a href="https://github.com/Slicer/Slicer/pull/8260">PR-8260</a>)</li>
</ul>

---

## Post #4 by @Lohi (2025-03-08 00:23 UTC)

<p>fantastic upgrade!<br>
the contributions of many people have resulted in rather significant enhancements.<br>
I’m hoping that there will be more help for people trying to negotiate the steep ladder “learning curve”, so that more of us can better use the software for the most difficult diagnosis and treatments…</p>

---
