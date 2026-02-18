# Slicer 5.6: Summary, Highlights, and Changelog

**Topic ID**: 33140
**Date**: 2023-11-30
**URL**: https://discourse.slicer.org/t/slicer-5-6-summary-highlights-and-changelog/33140

---

## Post #1 by @jcfr (2023-11-30 08:50 UTC)

<h1><a name="p-104026-table-of-content-1" class="anchor" href="#p-104026-table-of-content-1" aria-label="Heading link"></a>Table of content</h1>
<ul>
<li><a href="#heading--summary">Summary</a></li>
<li><a href="#heading--highlights">Highlights</a></li>
<li><a href="https://discourse.slicer.org/t/slicer-5-6-summary-highlights-and-changelog/33140/2">Detailed Changelog</a></li>
</ul>
<h1 id="heading--summary">Summary</h1>
<p>The community of 3D Slicer developers is proud to announce that version 5.6 is<a href="http://download.slicer.org/"> now available for download</a>. This release includes support for 3D Segmentation rendering speedup, interactive thick slab reconstruction (TSR), enhanced Endoscopy flythrough and improved support for DICOM regularization transform hardening. It also includes enhancements across core modules and introduces over 5 new extensions, each bringing additional features and improvements.</p>
<p>3D Slicer 5.6 builds on the success of earlier versions that have had over 1.4 million downloads of the core application and 6.8 million downloads of extensions during the last decade.</p>
<p>The development of 3D Slicer—including its numerous modules, extensions, datasets, pull requests, patches, issues reports, suggestions—is made possible by users, developers, contributors and commercial partners around the world. 3D Slicer is based on a stack of open-source software and we are working constantly on updating the underlying packages. This development is funded by various grants and agencies. For more details, please see the 3D Slicer <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#acknowledgments">Acknowledgments</a> page.</p>
<p>Feel free to share your insights on <a href="https://discourse.slicer.org/">Discourse</a> and explore our <a href="https://slicer.readthedocs.io/en/latest/developer_guide/contributing.html">contributing guidelines</a>. If you need help using Slicer, want to report a problem, request a feature, or share how Slicer has contributed to your work, visit our <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html">Get Help</a> section.</p>
<p><a href="https://www.slicer.org/">slicer.org</a> serves as the central hub for the application, training materials, and the development community, offering a series of tutorials and data sets through the <a href="https://slicer.readthedocs.io/en/5.6/user_guide/getting_started.html#tutorials">Slicer Tutorials</a> page.</p>
<p><em>Please note that Slicer continues to be a research package and is not intended for clinical use (clinical users must obtain the necessary ethics or regulatory approvals).</em></p>
<h1 id="heading--highlights">Highlights</h1>
<ul>
<li>
<p><strong>New Extensions:</strong> <a href="#New">10+ new and improved extensions</a>, including several AI segmentation tools, such as <a href="https://discourse.slicer.org/t/new-extension-fully-automatic-whole-body-ct-segmentation-in-2-minutes-using-totalsegmentator/26710">fully automatic segmentation of 100+ structures in CT images</a> in less than 2-minutes <a href="https://discourse.slicer.org/t/totalsegmentator-v2/32470">using TotalSegmentator v2</a>, improved <a href="https://discourse.slicer.org/t/new-colorize-volume-module/32254">volume rendering of RGBA image volume</a>, tools for liver intervention planning, review and annotation of multi-parametric imaging datasets, and support for exploring and accessing imaging data available from the NCI Imaging Data Commons.</p>
</li>
<li>
<p><strong>3D Segmentation Rendering speedup:</strong> The <a href="https://discourse.slicer.org/t/new-surface-model-generation-method-surfacenets/32430"><em>Surface Nets</em> algorithm provides a ~7x speedup to the generation of surface models</a> from segmentations compared to the default <em>Flying Edges</em> method.</p>
</li>
<li>
<p><strong>Interactive Thick Slab Reconstruction (TSR):</strong> It can now be <a href="https://discourse.slicer.org/t/new-feature-thick-slab-reconstruction-from-slice-controllers-and-views/32432">enabled and modified from the slice controllers and slice views</a>.</p>
</li>
<li>
<p><strong>Enhanced Endoscopy Flythrough:</strong> Support flying through a path along <a href="https://discourse.slicer.org/t/update-to-endoscopy-flythrough/33055">with adjusting and saving camera at specific position</a>.</p>
</li>
<li>
<p><strong>Simplified Image Capture:</strong> <a href="https://github.com/Slicer/Slicer/pull/7272">Simplified single-image capture in ScreenCapture module</a>.</p>
</li>
<li>
<p><strong>Transform Hardening Support in DICOM Scalar plugin:</strong> Identified sub-series (each loaded as independent volume node) <a href="https://discourse.slicer.org/t/new-feature-support-regularization-transform-hardening-in-dicom-scalar-plugin/32772">now support being grouped by orientation with hardening of the regularization transform hardening</a>. This can be enabled in the DICOM settings by selecting <em>harden regularization transform</em> instead of the default <em>apply regularization transform</em>.</p>
</li>
<li>
<p><strong>Security Enhancement:</strong> Added <a href="https://github.com/Slicer/Slicer/security/policy">security policy</a> describing how to report security vulnerabilities along with details about the preferred languages, supported versions and scope.</p>
</li>
</ul>
<p><em>This version was released on November 27th, 2023, and the associated git tag is <a href="https://github.com/Slicer/Slicer/tree/v5.6.0">v5.6.0</a>. Information about previous releases can be found on the <a href="https://github.com/Slicer/Slicer/wiki/Release-Details">Release Details</a> page.</em></p>
<div class="md-table">
<table>
<thead>
<tr>
<th><img src="https://github.com/Slicer/Slicer/assets/219043/c98dd3e0-6f47-40dc-a0a9-99dcd1fbc95e" alt="image" width="500" height="500"></th>
<th><img src="https://github.com/Slicer/Slicer/assets/219043/3fe81f00-05e7-447e-811b-e0040cf4c5a4" alt="image" width="500" height="500"></th>
<th><img src="https://github.com/Slicer/Slicer/assets/219043/3aa60706-fe48-47b2-8019-f44d81de2af0" alt="" role="presentation" width="500" height="500"></th>
</tr>
</thead>
<tbody>
<tr>
<td>Volume rendered RGBA volume created using the <a href="https://github.com/PerkLab/SlicerSandbox">Colorize Volume</a> module and a fully segmented rattlesnake are copied from <a href="https://discourse.slicer.org/t/new-colorize-volume-module/32254">this post</a>.</td>
<td>SlicerLiver is an extension for the medical research software 3D Slicer providing tools for analysis, quantification and therapy planning for hepatic interventions.</td>
<td>The SlicerExtraMarkups extension adds the <code>Label</code> and <code>Shape</code> markups nodes for respectively drawing  an arrow with a text label, or a pre-defined primitive shapes (circle, cone…).</td>
</tr>
</tbody>
</table>
</div>

---

## Post #2 by @jcfr (2023-11-30 08:51 UTC)

<h1 id="heading--changelog">Changelog</h1>
<ul>
<li><a href="#heading--core">Core</a>
<ul>
<li><a href="#heading--rendering-display">Rendering &amp; Display</a></li>
<li><a href="#heading--performance">Performance</a></li>
<li><a href="#heading--ui-ux">UI/UX</a></li>
<li><a href="#heading--events">Events</a></li>
<li><a href="#heading--io">IO</a></li>
<li><a href="#heading--scripting">Scripting </a></li>
<li><a href="#heading--internationalization-localization">Internationalization/Localization</a></li>
<li><a href="#heading--developer-documentation">Developer Documentation</a></li>
</ul>
</li>
<li><a href="#heading--improved-modules">Improved Modules</a>
<ul>
<li><a href="#heading--dicom">DICOM</a></li>
<li><a href="#heading--comparevolumes">CompareVolumes</a></li>
<li><a href="#heading--endoscopy">Endoscopy</a></li>
<li><a href="#heading--extensionwizard">ExtensionWizard</a></li>
<li><a href="#heading--fiducial-registration-module">Fiducial Registration module</a></li>
<li><a href="#heading--markups">Markups</a></li>
<li><a href="#heading--screencapture">ScreenCapture</a></li>
<li><a href="#heading--sequences">Sequences</a></li>
<li><a href="#heading--segmentation">Segmentation</a></li>
<li><a href="#heading--subject-hierarchy">Subject Hierarchy</a></li>
<li><a href="#heading--webserver">WebServer</a></li>
</ul>
</li>
<li><a href="#heading--infrastructure">Infrastructure</a>
<ul>
<li><a href="#heading--security">Security</a></li>
<li><a href="#heading--continuous-integration-ci">Continuous Integration (CI)</a></li>
<li><a href="#heading--packaging">Packaging</a></li>
<li><a href="#heading--build-system">Build-System</a></li>
<li><a href="#heading--dependencies">Dependencies</a></li>
<li><a href="#heading--openxr-support">OpenXR support</a></li>
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
<h3 id="heading--rendering-display">Rendering &amp; Display</h3>
<ul>
<li>Update Intersection Widget to Display Slab Thickness (<a href="https://github.com/Slicer/Slicer/pull/7093">PR-7093</a>, <a href="https://github.com/Slicer/Slicer/pull/7252">PR-7252</a>)</li>
<li>Allow display RGBA volume values in DataProbe (<a href="https://github.com/Slicer/Slicer/pull/7265">PR-7265</a>)</li>
</ul>
<h3 id="heading--performance">Performance</h3>
<ul>
<li>Support 3D rendering of segmentation using Surface Nets (<a href="https://github.com/Slicer/Slicer/pull/7224">PR-7224</a>)</li>
<li>Enable TBB as the default VTK SMP implementation on all platforms (<a href="https://github.com/Slicer/Slicer/pull/7295">PR-7295</a>)</li>
</ul>
<h3 id="heading--ui-ux">UI/UX</h3>
<ul>
<li>Remove fixed-size buttons in the view controller for better restyling (<a href="https://github.com/Slicer/Slicer/pull/7219">PR-7219</a>)</li>
<li>Improve the readability of error lists in <code>Help -&gt; Report bugs and request enhancements</code> by using a table (<a href="https://github.com/Slicer/Slicer/pull/7225">PR-7225</a>, <a href="https://github.com/Slicer/Slicer/pull/7237">PR-7237</a>)</li>
<li>Support restoring SliceViewAnnotations enabled state (<a href="https://github.com/Slicer/Slicer/pull/7176">PR-7176</a>)</li>
<li>Fix difficult-to-see slice offset text in Slicer dark mode (<a href="https://github.com/Slicer/Slicer/pull/7234">PR-7234</a>)</li>
</ul>
<h3 id="heading--events">Events</h3>
<ul>
<li>Improve Event Delegation in <code>qMRMLThreeDView</code> and <code>qMRMLSliceView</code> (<a href="https://github.com/Slicer/Slicer/pull/7311">PR-7311</a>)
<ul>
<li>This effort led to the creation and integration of +10 pull requests implementing subsequent refactoring.</li>
<li>This enhancement allows for the association of specialized interactor styles, such as <code>vtkOpenXRInteractorStyle</code> or <code>vtkOpenVRInteractorStyle</code>, with the render window while still maintaining MRML-specific event delegation.</li>
</ul>
</li>
<li>Ensure remaining application events are processed before exiting (<a href="https://github.com/Slicer/Slicer/pull/7300">PR-7300</a>)</li>
</ul>
<h3 id="heading--io">IO</h3>
<ul>
<li>Remove FreeSurfer file extensions from qSlicerModelsReader (<a href="https://github.com/Slicer/Slicer/pull/7336">PR-7336</a>)</li>
</ul>
<h3 id="heading--scripting">Scripting </h3>
<ul>
<li>Add support for <code>qMRMLSliderWidget</code> in parameterNodeWrapper GUI connector (<a href="https://github.com/Slicer/Slicer/pull/7263">PR-7263</a>)</li>
<li>Improve scripted class readability by renaming <code>setPythonSource</code> parameter and associated internal variable (<a href="https://github.com/Slicer/Slicer/pull/7352">PR-7352</a>)</li>
<li>Fix VTK-based object creation in <code>PythonSlicer</code> regardless of import order (<a href="https://github.com/Slicer/Slicer/pull/7402">PR-7402</a>)</li>
<li>Fix incorrect enter/exit called after scripted module reload (<a href="https://github.com/Slicer/Slicer/pull/7351">PR-7351</a>)</li>
<li>Fix parameter node wrapper observers not being removed (<a href="https://github.com/Slicer/Slicer/pull/7306">PR-7306</a>)</li>
</ul>
<h3 id="heading--internationalization-localization">Internationalization/Localization</h3>
<ul>
<li>Make the translation update script more robust (<a href="https://github.com/Slicer/Slicer/pull/7273">PR-7273</a>)</li>
<li>Make text in the MRML library translatable (<a href="https://github.com/Slicer/Slicer/pull/7210">PR-7210</a>)</li>
<li>Make Segment Editor effect names translatable (<a href="https://github.com/Slicer/Slicer/pull/7254">PR-7254</a>)</li>
<li>Make +10 more modules translatable (<a href="https://github.com/Slicer/Slicer/pull/7243">PR-7243</a>)</li>
</ul>
<h3 id="heading--developer-documentation">Developer Documentation</h3>
<ul>
<li>Simplify the bug report template (<a href="https://github.com/Slicer/Slicer/pull/7329">PR-7329</a>)</li>
<li>Improve the documentation of obsolete filtering API in SH proxy model (<a href="https://github.com/Slicer/Slicer/pull/7314">PR-7314</a>)</li>
<li>Clarify steps for installing Qt in windows build instructions (<a href="https://github.com/Slicer/Slicer/pull/7389">PR-7389</a>)</li>
<li>Add instructions for setting up the development environment on Ubuntu 23.04 (<a href="https://github.com/Slicer/Slicer/pull/7371">PR-7371</a>)</li>
<li>Eliminate obsolete Doxygen grouping (<a href="https://github.com/Slicer/Slicer/pull/7421">PR-7421</a>)</li>
</ul>
<h2 id="heading--improved-modules">Improved Modules</h2>
<h3 id="heading--dicom">DICOM</h3>
<ul>
<li>Support regularization transform hardening in DICOM Scalar plugin (<a href="https://github.com/Slicer/Slicer/pull/7362">PR-7362</a>)</li>
<li>Make DICOM variable spacing warning more informative (<a href="https://github.com/Slicer/Slicer/pull/7339">PR-7339</a>)</li>
<li>Update <code>DICOMUtils.loadPatient()</code> API to handle messages and progressCallback (<a href="https://github.com/Slicer/Slicer/pull/7330">PR-7330</a>)</li>
<li>Expose authentication parameters for DICOMweb networking (<a href="https://github.com/Slicer/Slicer/pull/7260">PR-7260</a>)</li>
<li>Ensure <code>DICOMCommand.start()</code> returns process output (<a href="https://github.com/Slicer/Slicer/pull/7299">PR-7299</a>)</li>
<li>Update CTK to adjust the size of the delete DICOM object dialog (<a href="https://github.com/Slicer/Slicer/pull/7317">PR-7317</a>)</li>
<li>Fix crashes in subject hierarchy and DICOM reading (<a href="https://github.com/Slicer/Slicer/pull/72">PR-72</a>)</li>
<li>Fix DICOMUtils <code>getSortedImageFiles</code> return value if the input file list is empty (<a href="https://github.com/Slicer/Slicer/pull/7384">PR-7384</a>)</li>
<li>Fix DICOM loading error reporting issue (<a href="https://github.com/Slicer/Slicer/pull/7263">PR-7263</a>)</li>
</ul>
<h3 id="heading--comparevolumes">CompareVolumes</h3>
<ul>
<li>Add docs for CompareVolumes module (<a href="https://github.com/Slicer/Slicer/pull/7152">PR-7152</a>)</li>
<li>Fix developer mode issue with tooltip button (<a href="https://github.com/Slicer/Slicer/pull/7183">PR-7183</a>)</li>
</ul>
<h3 id="heading--endoscopy">Endoscopy</h3>
<ul>
<li>Endoscopy fly through with user’s camera transforms (<a href="https://github.com/Slicer/Slicer/pull/7165">PR-7165</a>)</li>
<li>Endoscopy Module simplification (<a href="https://github.com/Slicer/Slicer/pull/7428">PR-7428</a>)</li>
</ul>
<h3 id="heading--extensionwizard">ExtensionWizard</h3>
<ul>
<li>Fix ExtensionWizard error message reporting when drag-and-dropping script (<a href="https://github.com/Slicer/Slicer/pull/7353">PR-7353</a>)</li>
</ul>
<h3 id="heading--fiducial-registration-module">Fiducial Registration module</h3>
<ul>
<li>Fix Fiducial Registration module rigid transform changing scale (<a href="https://github.com/Slicer/Slicer/pull/7255">PR-7255</a>)</li>
</ul>
<h3 id="heading--markups">Markups</h3>
<ul>
<li>Clarify markup renaming behavior (<a href="https://github.com/Slicer/Slicer/pull/7259">PR-7259</a>)</li>
<li>Remove the use of deprecated GetNumberOfMarkups in vtkMRMLMarkupsPlaneNode (<a href="https://github.com/Slicer/Slicer/pull/7395">PR-7395</a>)</li>
</ul>
<h3 id="heading--screencapture">ScreenCapture</h3>
<ul>
<li>Simplify single-image capture in ScreenCapture module (<a href="https://github.com/Slicer/Slicer/pull/7272">PR-7272</a>)</li>
</ul>
<h3 id="heading--sequences">Sequences</h3>
<ul>
<li>Make the sequence item creating strategy configurable (<a href="https://github.com/Slicer/Slicer/pull/7404">PR-7404</a>)</li>
<li><code>AddSynchronizedSequenceNodeID</code> caused the browser to stop operating correctly (<a href="https://github.com/Slicer/Slicer/pull/7331">PR-7331</a>)</li>
<li>Fix nodes not getting removed in <code>vtkMRMLSequenceNode::SetDataNodeAtValue</code> (<a href="https://github.com/Slicer/Slicer/pull/7335">PR-7335</a>)</li>
</ul>
<h3 id="heading--segmentation">Segmentation</h3>
<ul>
<li>Show segment ID in the tooltip for segments in subject hierarchy (<a href="https://github.com/Slicer/Slicer/pull/7229">PR-7229</a>)</li>
<li>Make Grow from seeds effect input requirements more clear (<a href="https://github.com/Slicer/Slicer/pull/7326">PR-7326</a>)</li>
<li>Add a setting for the overwrite mode masking option of the segment editor-set (<a href="https://github.com/Slicer/Slicer/pull/7131">PR-7131</a>) and <a href="https://github.com/Slicer/Slicer/pull/7265">PR-7265</a></li>
<li>Improve performance when removing segmentation from SH tree (<a href="https://github.com/Slicer/Slicer/pull/7253">PR-7253</a>)</li>
<li>Fix closed surface disappearing when the segment is removed (<a href="https://github.com/Slicer/Slicer/pull/7226">PR-7226</a>)</li>
<li>Fix “Show 3D” button not updating during undo/redo (<a href="https://github.com/Slicer/Slicer/pull/7248">PR-7248</a>)</li>
<li>Fix Segment Editor screen reader compatibility (<a href="https://github.com/Slicer/Slicer/pull/7263">PR-7263</a>)</li>
<li>Resolve del method override issue in AutoComplete segment editor effect (<a href="https://github.com/Slicer/Slicer/pull/7393">PR-7393</a>)</li>
</ul>
<h3 id="heading--subject-hierarchy">Subject Hierarchy</h3>
<ul>
<li>Empty folder SH visibility (<a href="https://github.com/Slicer/Slicer/pull/7214">PR-7214</a>)</li>
</ul>
<h3 id="heading--webserver">WebServer</h3>
<ul>
<li>Formalize <code>WebServer</code> request handler interface (<a href="https://github.com/Slicer/Slicer/pull/7350">PR-7350</a>)</li>
</ul>
<h2 id="heading--infrastructure">Infrastructure</h2>
<h3 id="heading--security">Security</h3>
<ul>
<li>Add security policy document (<a href="https://github.com/Slicer/Slicer/pull/7199">PR-7199</a>)</li>
<li>Update Security document to clarify “bug bounty” scope (<a href="https://github.com/Slicer/Slicer/pull/7223">PR-7223</a>)</li>
<li>Add build CI badge to <code>README</code> (<a href="https://github.com/Slicer/Slicer/pull/7221">PR-7221</a>)</li>
<li>Add OSSF scorecard action to quantify open-source health (<a href="https://github.com/Slicer/Slicer/pull/7197">PR-7197</a>)</li>
<li>Update OSSF scorecard workflow to support running Branch-Protection check (<a href="https://github.com/Slicer/Slicer/pull/7207">PR-7207</a>)</li>
<li>Restrict workflow permissions to “read” for the content scope (<a href="https://github.com/Slicer/Slicer/pull/7200">PR-7200</a>)</li>
</ul>
<h3 id="heading--continuous-integration-ci">Continuous Integration (CI)</h3>
<ul>
<li>Transition Python linting from flake8 to ruff (<a href="https://github.com/Slicer/Slicer/pull/7338">PR-7338</a>)</li>
<li>Disambiguate CI workflow names adding “(Build)” and “(Lint)” suffix (<a href="https://github.com/Slicer/Slicer/pull/7202">PR-7202</a>)</li>
<li>Fix “ci” GitHub workflow ensuring Slicer package is uploaded (<a href="https://github.com/Slicer/Slicer/pull/7249">PR-7249</a>)</li>
<li>Update GitHub workflow to remove deprecated use of “::set-output” (<a href="https://github.com/Slicer/Slicer/pull/7359">PR-7359</a>)</li>
</ul>
<h3 id="heading--packaging">Packaging</h3>
<ul>
<li>Use main project version for macOS short version string in the bundle (<a href="https://github.com/Slicer/Slicer/pull/7271">PR-7271</a>)</li>
</ul>
<h3 id="heading--build-system">Build-System</h3>
<ul>
<li>Ensure revision of type CommitCount is always recomputed based on offset (<a href="https://github.com/Slicer/Slicer/pull/7180">PR-7180</a>)</li>
<li>Fix extension packaging on macOS accounting for synthetic firmlink (<a href="https://github.com/Slicer/Slicer/pull/7181">PR-7181</a>)</li>
<li>Expand <code>&lt;CMAKE_CFG_INTDIR&gt;</code> in extension additional launcher settings (<a href="https://github.com/Slicer/Slicer/pull/7191">PR-7191</a>)</li>
<li>Fix extensions build ensuring build-type is set (<a href="https://github.com/Slicer/Slicer/pull/7247">PR-7247</a>)</li>
<li>Remove the use of deprecated <code>${CMAKE_CFG_INTDIR}</code> variable (<a href="https://github.com/Slicer/Slicer/pull/7240">PR-7240</a>)</li>
</ul>
<h3 id="heading--dependencies">Dependencies</h3>
<ul>
<li>Update SimpleITK from 2.2.0rc2 to 2.2.1 to support <strong>TotalSegmentator v2</strong> (<a href="https://github.com/Slicer/Slicer/pull/7427">PR-7427</a>)</li>
<li>Update VTK and vtkAddon for <strong>ColorizeVolume</strong> module in the Sandbox extension (<a href="https://github.com/Slicer/Slicer/pull/7305">PR-7305</a>)</li>
<li>Update VTK to fix RGBA volume rendering (<a href="https://github.com/Slicer/Slicer/pull/7274">PR-7274</a>)</li>
<li>Update VTK to remove unnecessary messages in vtkTransformPolyDataFilter (<a href="https://github.com/Slicer/Slicer/pull/7227">PR-7227</a>)</li>
<li>Update VTK to fix the segfault when enabling volume rendering (<a href="https://github.com/Slicer/Slicer/pull/7286">PR-7286</a>)</li>
<li>Update Python packages to the latest (<a href="https://github.com/Slicer/Slicer/pull/7285">PR-7285</a>)</li>
<li>Update vtkAddon to fix vtkImageLabelDilate3D build on a recent compiler (<a href="https://github.com/Slicer/Slicer/pull/7307">PR-7307</a>)</li>
</ul>
<h3 id="heading--openxr-support">OpenXR support</h3>
<ul>
<li>Update VTK to support the distribution of OpenXRRemoting in the extension (<a href="https://github.com/Slicer/Slicer/pull/7190">PR-7190</a>)</li>
<li>Update VTK to backport OpenXR error handling improvements (<a href="https://github.com/Slicer/Slicer/pull/7193">PR-7193</a>)</li>
<li>Update VTK backporting RenderingVR and RenderingOpenXR fixes (<a href="https://github.com/Slicer/Slicer/pull/7195">PR-7195</a>)</li>
</ul>
<h2 id="heading--extensions">Extensions</h2>
<p><em>Listed below are extensions added, removed or updated since the 5.4 release.</em></p>
<p>The Slicer <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html">extensions manager</a> enables Slicer users to install more than 175 extensions written and contributed by their peers from around the world.</p>
<h3 id="heading--new">New</h3>
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
<td><a href="https://github.com/PerkLab/SlicerSandbox">Colorize Volume</a></td>
<td>Create RGBA volume for volume rendering based of an input volume and a segmentation. Screenshots below representing a fully segmented rattlesnake are copied from <a href="https://discourse.slicer.org/t/new-colorize-volume-module/32254">this post</a>.</td>
</tr>
<tr>
<td><img src="https://github.com/PerkLab/SlicerSandbox/blob/master/Sandbox_Logo_128.png?raw=true" alt="" role="presentation" width="" height=""></td>
<td><img src="https://github.com/Slicer/Slicer/assets/219043/c98dd3e0-6f47-40dc-a0a9-99dcd1fbc95e" alt="" role="presentation" width="" height=""></td>
</tr>
</tbody>
</table>
</div><div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/ImagingDataCommons/SlicerIDCBrowser.git">IDCBrowser</a></td>
<td>Explore and access imaging data available from the <a href="https://imaging.datacommons.cancer.gov">National Cancer Institute Imaging Data Commons</a></td>
</tr>
<tr>
<td><img src="https://github.com/ImagingDataCommons/SlicerIDCBrowser/blob/c9519809522aaac59bb65fb558b1197cf05c3e72/IDCBrowser/Resources/Icons/IDCBrowser.png?raw=true" alt="" role="presentation" width="" height=""></td>
<td><img src="https://github.com/ImagingDataCommons/SlicerIDCBrowser/blob/main/IDCBrowser/Resources/Screenshot/screenshot.png?raw=true" alt="" role="presentation" width="" height=""></td>
</tr>
</tbody>
</table>
</div><div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/SlicerProstate/mpReview.git">mpReview</a></td>
<td>Facilitate review and annotation (segmentation) of multi-parametric imaging datasets.</td>
</tr>
<tr>
<td><img src="https://raw.githubusercontent.com/SlicerProstate/mpReview/master/Resources/Icons/mpReview.png" alt="" role="presentation" width="" height=""></td>
<td><img src="https://github.com/SlicerProstate/mpReview/raw/master/Resources/Icons/mpReview_screenshot.PNG?raw=true" alt="" role="presentation" width="" height=""></td>
</tr>
</tbody>
</table>
</div><div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://gitlab.com/chir-set/SlicerExtraMarkups.git">ExtraMarkups</a></td>
<td>Add the <code>Label</code> and <code>Shape</code> markups nodes for respectively drawing  an arrow with a text label, or a pre-defined primitive shapes (circle, cone…).</td>
</tr>
<tr>
<td><img src="https://gitlab.com/chir-set/SlicerExtraMarkups/-/raw/main/ExtraMarkups.png?ref_type=heads" alt="" role="presentation" width="" height=""></td>
<td><img src="https://github.com/Slicer/Slicer/assets/219043/3aa60706-fe48-47b2-8019-f44d81de2af0" alt="" role="presentation" width="" height=""></td>
</tr>
</tbody>
</table>
</div><div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/MHubAI/SlicerMRunner">MHubRunner</a></td>
<td>Integrates Deep Learning models from the Medical Hub repository (MHub) into 3D Slicer.</td>
</tr>
<tr>
<td><img src="https://github.com/MHubAI/SlicerMRunner/blob/main/SlicerMHubRunner.png?raw=true" alt="" role="presentation" width="" height=""></td>
<td><img src="https://mhub.ai/slicer/image01.png" alt="" role="presentation" width="" height=""></td>
</tr>
</tbody>
</table>
</div><div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/ALive-research/Slicer-Liver">SlicerLiver</a></td>
<td>Provide tools for analysis, quantification and therapy planning for hepatic interventions.</td>
</tr>
<tr>
<td><img src="https://raw.githubusercontent.com/ALive-research/Slicer-Liver/master/SlicerLiver.png" alt="" role="presentation" width="" height=""></td>
<td><img src="https://github.com/Slicer/Slicer/assets/219043/3fe81f00-05e7-447e-811b-e0040cf4c5a4" alt="" role="presentation" width="" height=""></td>
</tr>
</tbody>
</table>
</div><h3 id="heading--updated">Updated</h3>
<p>All the existing extensions have been maintained and updated to account for API and build environment changes.</p>
<ul>
<li>
<p><strong>TotalSegmentator</strong>: <a href="https://discourse.slicer.org/t/totalsegmentator-v2/32470">Now compatible with TotalSegmentator v2</a>.</p>
</li>
<li>
<p><strong>Slicer Pipeline</strong>: Now supports <a href="https://discourse.slicer.org/t/update-to-slicer-pipelines/31797">passing any number of parameters and nodes through any number of stages and include these values in the result set</a>.</p>
</li>
</ul>
<h3 id="heading--removed">Removed</h3>
<p>Between Slicer 5.4 and Slicer 5.6, no extensions were removed.</p>
<p>List of archived extensions is documented at <a href="https://github.com/Slicer/ExtensionsIndex/blob/main/ARCHIVE/README.md">Slicer/ExtensionsIndex/ARCHIVE/README.md</a></p>

---
