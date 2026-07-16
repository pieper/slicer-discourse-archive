---
topic_id: 47540
title: "Slicer 5.12: Summary, Highlights, and Changelog"
date: 2026-07-10
url: https://discourse.slicer.org/t/47540
last_bumped: 2026-07-16T01:36:38.552Z
---

# Slicer 5.12: Summary, Highlights, and Changelog

**Topic ID**: 47540
**Date**: 2026-07-10
**URL**: https://discourse.slicer.org/t/slicer-5-12-summary-highlights-and-changelog/47540

---

## Post #1 by @ebrahim (2026-07-10 12:01 UTC)

<ul>
<li><a href="#heading--summary">Summary</a></li>
<li><a href="#heading--highlights">Highlights</a></li>
<li><a href="#heading--changelog-5-12-0">Changelog: 5.12.0</a></li>
</ul>
<h2 id="heading--summary">Summary</h2>
<p>Slicer 5.12 is the next stable release after Slicer 5.10. The release focuses on Qt 6 build support, a redesigned DICOM browser for larger databases, native support for additional DICOM object types, improved volume and segmentation display controls, better markups and transform visualization, a new Python dependency management API for scripted modules and extensions, and updated extension catalog metadata.</p>
<h2 id="heading--highlights">Highlights</h2>
<h3 id="heading--dicom-browser-and-dicom-object-support">DICOM browser and DICOM object support</h3>
<p>The Visual DICOM Browser was refactored for large DICOM databases, adding a dockable side panel, tab/list modes, configurable thumbnails, improved query/retrieve job tracking, and refreshed documentation (<a href="https://github.com/Slicer/Slicer/pull/8866">PR-8866</a>, <a href="https://github.com/Slicer/Slicer/pull/9070">PR-9070</a>). DICOM SEG, Parametric Map, TID 1500 Structured Report, and M3D object plugins were moved into Slicer core, reducing the need for separate extension installs for these common object types (<a href="https://github.com/Slicer/Slicer/pull/9114">PR-9114</a>).</p>
<div>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c579c0ae7ca3619ae1b11ed477cbeaf85e396b04.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b28c4ebfe8a654094c6f165ebf8b1731d04279d6.jpeg" data-video-base62-sha1="saWULokooptf9PB47Bbz30CCPUU.mp4">
  </div><br>
<em>Visual DICOM Browser improvements for large DICOM databases.</em><p></p>
</div>
<h3 id="heading--rendering-color-mapping-and-visualization">Rendering, color mapping, and visualization</h3>
<p>Volume rendering now supports volumes under non-linear transforms (<a href="https://github.com/Slicer/Slicer/pull/8929">PR-8929</a>). Scalar volume display supports logarithmic color mapping, with color legend and volume-rendering synchronization updates (<a href="https://github.com/Slicer/Slicer/pull/9016">PR-9016</a>). Segmentation display now exposes material controls such as interpolation, ambient, diffuse, specular, metallic, and roughness properties in the GUI (<a href="https://github.com/Slicer/Slicer/pull/8782">PR-8782</a>).</p>
<div>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e98050f3ce5243db3f7eecb8290e2ccec4890ff3.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e679c51d12ef576296eb376f2cf569d59692ff3a.jpeg" data-video-base62-sha1="xjEalmF5ruIjH7g8sgay0IKLeMP.mp4">
  </div><br>
<em>Logarithmic color mapping.</em><p></p>
</div>
<h3 id="heading--markups-transforms-and-modeling-tools">Markups, transforms, and modeling tools</h3>
<p>Curve and line markups can show configurable directional arrow glyphs in slice and 3D views (<a href="https://github.com/Slicer/Slicer/pull/9066">PR-9066</a>). Transform visualization gained editable 2D glyph thickness, arrow tip length, and circle glyph resolution controls (<a href="https://github.com/Slicer/Slicer/pull/8931">PR-8931</a>, <a href="https://github.com/Slicer/Slicer/pull/8934">PR-8934</a>). Dynamic Modeler Extrude and Revolve tools now accept more markup input types and include several geometry fixes (<a href="https://github.com/Slicer/Slicer/pull/8816">PR-8816</a>).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9ca8dd3ba8473ba321df8b9c9a2b7c799d1579af.jpeg" data-download-href="/uploads/short-url/mlSh44eo4vlSISx1H2ROxjjFcjt.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ca8dd3ba8473ba321df8b9c9a2b7c799d1579af_2_690x155.jpeg" alt="image" data-base62-sha1="mlSh44eo4vlSISx1H2ROxjjFcjt" width="690" height="155" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ca8dd3ba8473ba321df8b9c9a2b7c799d1579af_2_690x155.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ca8dd3ba8473ba321df8b9c9a2b7c799d1579af_2_1035x232.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ca8dd3ba8473ba321df8b9c9a2b7c799d1579af_2_1380x310.jpeg 2x" data-dominant-color="8F8B9E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×433 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3 id="heading--clearer-visibility-state-in-subject-hierarchy">Clearer visibility state in Subject Hierarchy</h3>
<p>Subject Hierarchy now gives clearer feedback when an item is hidden because one of its parent folders is hidden. Child items keep their own visibility setting, but their eye icons are grayed out when parent visibility makes them effectively invisible, reducing confusion in complex scenes with nested folders (<a href="https://github.com/Slicer/Slicer/pull/9195">PR-9195</a>).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/259f385568308f368f7c2ae0973230c28bb67306.gif" alt="visibility" data-base62-sha1="5mONdm8lfBDhJTzw7Mbtdd1P7OS" width="690" height="456" class="animated"></p>
<h3 id="heading--python-package-management-for-modules-and-extensions">Python package management for modules and extensions</h3>
<p>A new <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer.packaging"><code>slicer.packaging</code></a> module provides a standard API for extension and scripted-module dependency handling. It can load <code>requirements.txt</code> or <code>pyproject.toml</code> dependencies, check installed packages without launching pip, install packages with progress feedback, and prompt for restart when updated packages are already imported. Existing <code>slicer.util.pip_install</code> and <code>slicer.util.pip_uninstall</code> calls remain available as compatibility wrappers (<a href="https://github.com/Slicer/Slicer/pull/9010">PR-9010</a>).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9e372df086c99c3a720589043d5420ab994f3b8.png" data-download-href="/uploads/short-url/oeTZWF6cIwOFLMx3gMUSZ3YStOU.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9e372df086c99c3a720589043d5420ab994f3b8.png" alt="image" data-base62-sha1="oeTZWF6cIwOFLMx3gMUSZ3YStOU" width="390" height="213"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">520×285 38.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3 id="heading--qt-6-build-support">Qt 6 build support</h3>
<p>Slicer can now be built against Qt 6, while preserving Qt 5.15 compatibility. This work includes the main Qt 6 enablement, follow-up compatibility fixes, packaging/startup fixes, and support work for Qt 6.8, 6.10, and 6.11 builds (<a href="https://github.com/Slicer/Slicer/pull/8893">PR-8893</a>, <a href="https://github.com/Slicer/Slicer/pull/8868">PR-8868</a>, <a href="https://github.com/Slicer/Slicer/pull/8874">PR-8874</a>, <a href="https://github.com/Slicer/Slicer/pull/8919">PR-8919</a>, <a href="https://github.com/Slicer/Slicer/pull/8935">PR-8935</a>, <a href="https://github.com/Slicer/Slicer/pull/8937">PR-8937</a>, <a href="https://github.com/Slicer/Slicer/pull/8956">PR-8956</a>, <a href="https://github.com/Slicer/Slicer/pull/9212">PR-9212</a>).</p>
<h3 id="heading--extensions">Extensions</h3>
<p>The 5.12 extension catalog adds 22 extensions since Slicer 5.10.0. Extension metadata now supports tier, DICOM support rules, recommendations, and keywords to improve discoverability and future DICOM workflow suggestions (<a href="https://github.com/Slicer/Slicer/pull/9040">PR-9040</a>, <a href="https://github.com/Slicer/Slicer/pull/9057">PR-9057</a>).</p>
<h2 id="heading--changelog-5-12-0">Changelog: 5.12.0</h2>
<h3 id="heading--core">Core</h3>
<h4 id="heading--rendering-and-display">Rendering and display</h4>
<ul>
<li>Allow volume rendering of non-linearly transformed volumes (<a href="https://github.com/Slicer/Slicer/pull/8929">PR-8929</a>).</li>
<li>Add logarithmic scalar volume color mapping and synchronize logarithmic display with color legends and volume rendering (<a href="https://github.com/Slicer/Slicer/pull/9016">PR-9016</a>).</li>
<li>Reduce volume-rendering control point count during volume-display synchronization (<a href="https://github.com/Slicer/Slicer/pull/9016">PR-9016</a>).</li>
<li>Expose segmentation material properties in the Segmentations module GUI (<a href="https://github.com/Slicer/Slicer/pull/8782">PR-8782</a>).</li>
<li>Optimize 3D segmentation display for linearly transformed segmentations by using a GPU transform path (<a href="https://github.com/Slicer/Slicer/pull/9031">PR-9031</a>).</li>
<li>Fix loss of volume-rendering opacity transfer-function points (<a href="https://github.com/Slicer/Slicer/pull/9186">PR-9186</a>).</li>
<li>Fix incorrect synchronization of 2D colormap settings to the rendering colormap (<a href="https://github.com/Slicer/Slicer/pull/9250">PR-9250</a>).</li>
<li>Fix log10 display of inverted color tables (<a href="https://github.com/Slicer/Slicer/pull/8884">PR-8884</a>).</li>
<li>Fix effective range computation in the volume property node widget (<a href="https://github.com/Slicer/Slicer/pull/9080">PR-9080</a>).</li>
<li>Fix crash when selecting active scalars for several model nodes at once (<a href="https://github.com/Slicer/Slicer/pull/9169">PR-9169</a>).</li>
<li>Disable default VTK render-window keyboard shortcuts (<a href="https://github.com/Slicer/Slicer/pull/9194">PR-9194</a>).</li>
<li>Fix View Controller crash with virtual reality views and update VTK with virtual-reality fixes (<a href="https://github.com/Slicer/Slicer/pull/8900">PR-8900</a>, <a href="https://github.com/Slicer/Slicer/pull/8984">PR-8984</a>).</li>
<li>Add Meta AR video passthrough support (<a href="https://github.com/Slicer/Slicer/pull/9249">PR-9249</a>).</li>
</ul>
<h4 id="heading--dicom">DICOM</h4>
<ul>
<li>Refactor the Visual DICOM Browser UI for large databases, with dockable side-panel mode, tab/list modes, thumbnail controls, query/retrieve job tracking, and updated documentation (<a href="https://github.com/Slicer/Slicer/pull/8866">PR-8866</a>).</li>
<li>Add refresh functionality to the Visual DICOM Browser (<a href="https://github.com/Slicer/Slicer/pull/9070">PR-9070</a>).</li>
<li>Improve DICOM import performance in Qt 6 builds, including thumbnail and detailed-logging behavior (<a href="https://github.com/Slicer/Slicer/pull/8982">PR-8982</a>).</li>
<li>Add DICOM SEG, Parametric Map, TID 1500 SR, and M3D plugins to Slicer core (<a href="https://github.com/Slicer/Slicer/pull/9114">PR-9114</a>).</li>
<li>Add integration tests for DICOM SEG, TID 1500 SR, and M3D plugin loading (<a href="https://github.com/Slicer/Slicer/pull/9114">PR-9114</a>).</li>
<li>Improve dcmqi binary lookup for package-bundled executables (<a href="https://github.com/Slicer/Slicer/pull/9136">PR-9136</a>).</li>
<li>Pin transitive dependencies in <code>python-dicom-requirements</code> (<a href="https://github.com/Slicer/Slicer/pull/9132">PR-9132</a>).</li>
<li>Add JPEG2000 and Zlib support to DCMTK builds (<a href="https://github.com/Slicer/Slicer/pull/9099">PR-9099</a>, <a href="https://github.com/Slicer/Slicer/pull/9107">PR-9107</a>).</li>
<li>Fix DICOM Labelmap SEG segment metadata off-by-one behavior (<a href="https://github.com/Slicer/Slicer/pull/9163">PR-9163</a>).</li>
<li>Fix crash exporting a DICOM series with no local files (<a href="https://github.com/Slicer/Slicer/pull/9251">PR-9251</a>).</li>
<li>Fix DICOM thumbnail-size label typo (<a href="https://github.com/Slicer/Slicer/pull/8964">PR-8964</a>).</li>
</ul>
<h4 id="heading--segmentations-and-modeling">Segmentations and modeling</h4>
<ul>
<li>Expose material properties in the Segmentation module display controls (<a href="https://github.com/Slicer/Slicer/pull/8782">PR-8782</a>).</li>
<li>Scroll to newly added segments in Segment Editor (<a href="https://github.com/Slicer/Slicer/pull/9042">PR-9042</a>).</li>
<li>Fix missing closed-surface segment statistics when a segmentation node is transformed (<a href="https://github.com/Slicer/Slicer/pull/8854">PR-8854</a>).</li>
<li>Fix crash in <code>ExportSegmentsToColorTableNode</code> (<a href="https://github.com/Slicer/Slicer/pull/8942">PR-8942</a>).</li>
<li>Fix invalid segment iterator in <code>vtkSegmentation::ReorderSegments</code> (<a href="https://github.com/Slicer/Slicer/pull/8981">PR-8981</a>).</li>
<li>Guard null segmentation nodes in <code>qMRMLSegmentEditorWidget</code> (<a href="https://github.com/Slicer/Slicer/pull/9134">PR-9134</a>).</li>
<li>Fix duplicate opacity slider for segments in subject hierarchy (<a href="https://github.com/Slicer/Slicer/pull/9243">PR-9243</a>).</li>
<li>Fix crash after using Fill Between Slices and closing the application (<a href="https://github.com/Slicer/Slicer/pull/8998">PR-8998</a>).</li>
<li>Improve Dynamic Modeler Extrude and Revolve tools, including support for additional markup input types (<a href="https://github.com/Slicer/Slicer/pull/8816">PR-8816</a>).</li>
<li>Remove orphan points from Dynamic Modeler ROI and plane cut tools (<a href="https://github.com/Slicer/Slicer/pull/8971">PR-8971</a>).</li>
<li>Fix copy-paste error in oversampling fuzzy membership function (<a href="https://github.com/Slicer/Slicer/pull/9045">PR-9045</a>).</li>
</ul>
<h4 id="heading--markups-and-transforms">Markups and transforms</h4>
<ul>
<li>Add directional arrow glyphs to line and curve markups in 2D and 3D views (<a href="https://github.com/Slicer/Slicer/pull/9066">PR-9066</a>).</li>
<li>Add position status column to <code>qSlicerSimpleMarkupsWidget</code> (<a href="https://github.com/Slicer/Slicer/pull/8955">PR-8955</a>).</li>
<li>Add a view-node flag to disable Markups occlusion checking (<a href="https://github.com/Slicer/Slicer/pull/8979">PR-8979</a>).</li>
<li>Keep markup placement preview visible when slice views move or zoom (<a href="https://github.com/Slicer/Slicer/pull/9189">PR-9189</a>).</li>
<li>Fix unwanted markup measurements (<a href="https://github.com/Slicer/Slicer/pull/9216">PR-9216</a>).</li>
<li>Hide 3D angle line when fewer than two points are available (<a href="https://github.com/Slicer/Slicer/pull/9215">PR-9215</a>).</li>
<li>Fix markup control point coordinates not updating in the table (<a href="https://github.com/Slicer/Slicer/pull/9047">PR-9047</a>).</li>
<li>Fix last-used control point number not resetting when a list is reset (<a href="https://github.com/Slicer/Slicer/pull/8970">PR-8970</a>).</li>
<li>Deprecate the FCSV file format (<a href="https://github.com/Slicer/Slicer/pull/9192">PR-9192</a>).</li>
<li>Support 2D transforms by converting them to 3D during reading (<a href="https://github.com/Slicer/Slicer/pull/8842">PR-8842</a>).</li>
<li>Add support for 2D special cases of <code>MatrixOffsetTransform</code> (<a href="https://github.com/Slicer/Slicer/pull/9204">PR-9204</a>).</li>
<li>Add editable transform visualization controls for 2D glyph thickness, arrow tip length, and circle glyph resolution (<a href="https://github.com/Slicer/Slicer/pull/8931">PR-8931</a>, <a href="https://github.com/Slicer/Slicer/pull/8934">PR-8934</a>).</li>
<li>Add “Flip normal” action to plane nodes (<a href="https://github.com/Slicer/Slicer/pull/8794">PR-8794</a>).</li>
<li>Improve transform reading precision and ITK/VTK transform conversion cleanup (<a href="https://github.com/Slicer/Slicer/pull/8917">PR-8917</a>).</li>
</ul>
<h4 id="heading--application-and-ui">Application and UI</h4>
<ul>
<li>Add application icons for Linux and set the Windows application icon on <code>SlicerApp-Real.exe</code> (<a href="https://github.com/Slicer/Slicer/pull/9196">PR-9196</a>, <a href="https://github.com/Slicer/Slicer/pull/8987">PR-8987</a>).</li>
<li>Add automatic file-cache trimming at application startup (<a href="https://github.com/Slicer/Slicer/pull/9115">PR-9115</a>).</li>
<li>Fix CacheManager startup warning (<a href="https://github.com/Slicer/Slicer/pull/9159">PR-9159</a>).</li>
<li>Improve labels and tooltips in the Scene Views dialog (<a href="https://github.com/Slicer/Slicer/pull/9006">PR-9006</a>).</li>
<li>Fix inability to create multiple scene views (<a href="https://github.com/Slicer/Slicer/pull/9059">PR-9059</a>).</li>
<li>Fix capture toolbar location at startup (<a href="https://github.com/Slicer/Slicer/pull/8936">PR-8936</a>).</li>
<li>Separate SampleData category name and title, and fix SampleData module behavior (<a href="https://github.com/Slicer/Slicer/pull/9096">PR-9096</a>, <a href="https://github.com/Slicer/Slicer/pull/9150">PR-9150</a>).</li>
<li>Fix Extension Wizard module creation (<a href="https://github.com/Slicer/Slicer/pull/9178">PR-9178</a>).</li>
<li>Fix table copy/paste failure when the system clipboard is unavailable (<a href="https://github.com/Slicer/Slicer/pull/9025">PR-9025</a>).</li>
<li>Fix crash loading a table with unsupported schema column type (<a href="https://github.com/Slicer/Slicer/pull/9238">PR-9238</a>).</li>
<li>Fix <code>GetFileNameWithoutExtension()</code> failing when called with no arguments (<a href="https://github.com/Slicer/Slicer/pull/9152">PR-9152</a>).</li>
<li>Fix Qt 6 data dialog description shift-change behavior (<a href="https://github.com/Slicer/Slicer/pull/8978">PR-8978</a>).</li>
<li>Fix Python errors when the application path contains special characters (<a href="https://github.com/Slicer/Slicer/pull/9032">PR-9032</a>).</li>
</ul>
<h4 id="heading--subject-hierarchy">Subject hierarchy</h4>
<ul>
<li>Gray out visibility icons for subject hierarchy items under hidden parents (<a href="https://github.com/Slicer/Slicer/pull/9195">PR-9195</a>).</li>
<li>Show folder opacity before the visibility toggle (<a href="https://github.com/Slicer/Slicer/pull/9200">PR-9200</a>).</li>
<li>Fix clicking the visibility icon changing item selection (<a href="https://github.com/Slicer/Slicer/pull/9198">PR-9198</a>).</li>
<li>Reset view action metadata when opening the subject hierarchy widget context menu (<a href="https://github.com/Slicer/Slicer/pull/9205">PR-9205</a>).</li>
<li>Fix qMRMLNodeComboBox <code>nodeAddedByUser</code> being emitted twice (<a href="https://github.com/Slicer/Slicer/pull/9158">PR-9158</a>).</li>
<li>Fix crash when setting no display in a subject hierarchy combobox with no scene (<a href="https://github.com/Slicer/Slicer/pull/8853">PR-8853</a>).</li>
</ul>
<h4 id="heading--scripting-and-python">Scripting and Python</h4>
<ul>
<li>Add <code>slicer.packaging</code> for loading requirements, checking packages, installing dependencies with progress, and prompting for restarts after imported-package updates (<a href="https://github.com/Slicer/Slicer/pull/9010">PR-9010</a>).</li>
<li>Keep <code>slicer.util.pip_install</code> and <code>slicer.util.pip_uninstall</code> as compatibility wrappers over <code>slicer.packaging</code> (<a href="https://github.com/Slicer/Slicer/pull/9010">PR-9010</a>).</li>
<li>Add <code>slicer.packaging</code> usage to the scripted module template (<a href="https://github.com/Slicer/Slicer/pull/9010">PR-9010</a>).</li>
<li>Restore <code>slicer.util._executePythonModule</code> and Python console imports (<a href="https://github.com/Slicer/Slicer/pull/9141">PR-9141</a>, <a href="https://github.com/Slicer/Slicer/pull/9220">PR-9220</a>).</li>
<li>Improve translation support and fix translation-related errors (<a href="https://github.com/Slicer/Slicer/pull/9104">PR-9104</a>).</li>
<li>Fix VTK observer leak in <code>parameterNodeWrapper</code> GUI connection handling (<a href="https://github.com/Slicer/Slicer/pull/9063">PR-9063</a>).</li>
<li>Add <code>Base/Python/slicer/tests/test_slicer_packaging.py</code> and focused compatibility tests for <code>slicer.util</code> pip wrappers (<a href="https://github.com/Slicer/Slicer/pull/9010">PR-9010</a>).</li>
</ul>
<h4 id="heading--io-mrml-and-api">IO, MRML, and API</h4>
<ul>
<li>Fix private storable node saving (<a href="https://github.com/Slicer/Slicer/pull/9236">PR-9236</a>).</li>
<li>Fix mention of SWIG required external project and update <code>PushVolumeToSlicer</code> to use deep copy (<a href="https://github.com/Slicer/Slicer/pull/8930">PR-8930</a>).</li>
<li>Fix operator precedence in time-unit display coefficients (<a href="https://github.com/Slicer/Slicer/pull/9046">PR-9046</a>).</li>
<li>Get image data extent using accessors instead of direct member access (<a href="https://github.com/Slicer/Slicer/pull/8925">PR-8925</a>).</li>
<li>Replace deprecated <code>AddActor2D</code>/<code>RemoveActor2D</code> usage (<a href="https://github.com/Slicer/Slicer/pull/8944">PR-8944</a>).</li>
<li>Fix correct <code>vtkErrorMacro</code> message return (<a href="https://github.com/Slicer/Slicer/pull/8997">PR-8997</a>).</li>
<li>Add missing <code>Superclass::setup()</code> calls in 13 module widgets (<a href="https://github.com/Slicer/Slicer/pull/9044">PR-9044</a>).</li>
</ul>
<h4 id="heading--installation-and-packaging">Installation and packaging</h4>
<ul>
<li>Fix ignored installer branding text (<a href="https://github.com/Slicer/Slicer/pull/8858">PR-8858</a>).</li>
<li>Update CTKAppLauncher from 0.1.33 to 0.1.34 (<a href="https://github.com/Slicer/Slicer/pull/9033">PR-9033</a>).</li>
<li>Fix Qt 6 packaging and startup issues (<a href="https://github.com/Slicer/Slicer/pull/8937">PR-8937</a>).</li>
<li>Fix missing OpenJPEG shared library in packages, including macOS package handling (<a href="https://github.com/Slicer/Slicer/pull/9227">PR-9227</a>, <a href="https://github.com/Slicer/Slicer/pull/9228">PR-9228</a>).</li>
<li>Update Slicer CA certificate bundle (<a href="https://github.com/Slicer/Slicer/pull/9102">PR-9102</a>, <a href="https://github.com/Slicer/Slicer/pull/9111">PR-9111</a>, <a href="https://github.com/Slicer/Slicer/pull/9237">PR-9237</a>).</li>
</ul>
<h4 id="heading--documentation">Documentation</h4>
<ul>
<li>Revise Visual Studio installation instructions for Windows (<a href="https://github.com/Slicer/Slicer/pull/8851">PR-8851</a>).</li>
<li>Update supported operating system versions (<a href="https://github.com/Slicer/Slicer/pull/8933">PR-8933</a>).</li>
<li>Add macOS Apple Silicon Qt 6 build recipe and Qt 6 Linux build instructions (<a href="https://github.com/Slicer/Slicer/pull/9011">PR-9011</a>, <a href="https://github.com/Slicer/Slicer/pull/9084">PR-9084</a>).</li>
<li>Clarify inconsistencies between documentation and code (<a href="https://github.com/Slicer/Slicer/pull/9008">PR-9008</a>).</li>
<li>Document <code>slicer.packaging</code> in the developer guide (<a href="https://github.com/Slicer/Slicer/pull/9010">PR-9010</a>).</li>
<li>Fix image segmentation guide spelling error (<a href="https://github.com/Slicer/Slicer/pull/9098">PR-9098</a>).</li>
<li>Fix typo in MRML overview documentation (<a href="https://github.com/Slicer/Slicer/pull/9116">PR-9116</a>).</li>
<li>Fix elongation and flatness definitions in Segment Statistics documentation (<a href="https://github.com/Slicer/Slicer/pull/9177">PR-9177</a>).</li>
<li>Do not show “Edit on GitHub” links for special documentation pages (<a href="https://github.com/Slicer/Slicer/pull/9188">PR-9188</a>).</li>
<li>Update issue templates for patch and release processes (<a href="https://github.com/Slicer/Slicer/pull/8838">PR-8838</a>).</li>
<li>Add recent funding and product information to About documentation (<a href="https://github.com/Slicer/Slicer/pull/8894">PR-8894</a>, <a href="https://github.com/Slicer/Slicer/pull/8899">PR-8899</a>, <a href="https://github.com/Slicer/Slicer/pull/8913">PR-8913</a>, <a href="https://github.com/Slicer/Slicer/pull/9168">PR-9168</a>).</li>
</ul>
<h3 id="heading--infrastructure">Infrastructure</h3>
<h4 id="heading--qt-6-and-platform-support">Qt 6 and platform support</h4>
<ul>
<li>Add Qt 6 support (<a href="https://github.com/Slicer/Slicer/pull/8893">PR-8893</a>).</li>
<li>Add follow-up Qt 6 preparation, compatibility, test, packaging, and startup fixes (<a href="https://github.com/Slicer/Slicer/pull/8868">PR-8868</a>, <a href="https://github.com/Slicer/Slicer/pull/8874">PR-8874</a>, <a href="https://github.com/Slicer/Slicer/pull/8919">PR-8919</a>, <a href="https://github.com/Slicer/Slicer/pull/8935">PR-8935</a>, <a href="https://github.com/Slicer/Slicer/pull/8937">PR-8937</a>, <a href="https://github.com/Slicer/Slicer/pull/8956">PR-8956</a>).</li>
<li>Support building with Qt 6.8, Qt 6.10, and Qt 6.11-related dependency updates (<a href="https://github.com/Slicer/Slicer/pull/8956">PR-8956</a>, <a href="https://github.com/Slicer/Slicer/pull/8938">PR-8938</a>, <a href="https://github.com/Slicer/Slicer/pull/9212">PR-9212</a>).</li>
<li>Allow <code>Slicer_USE_QtTesting=ON</code> with Qt 6 builds (<a href="https://github.com/Slicer/Slicer/pull/9138">PR-9138</a>).</li>
<li>Enforce Qt 5.15 minimum and remove support for older Qt versions (<a href="https://github.com/Slicer/Slicer/pull/8949">PR-8949</a>, <a href="https://github.com/Slicer/Slicer/pull/8977">PR-8977</a>).</li>
<li>Remove support for building against VTK &lt;= 9.3 and add support for VTK 9.6 builds (<a href="https://github.com/Slicer/Slicer/pull/8972">PR-8972</a>, <a href="https://github.com/Slicer/Slicer/pull/8928">PR-8928</a>).</li>
<li>Disable touch events on macOS Qt 6 to fix stuck 3D rotation (<a href="https://github.com/Slicer/Slicer/pull/9069">PR-9069</a>).</li>
<li>Update minimum required <code>CMAKE_OSX_DEPLOYMENT_TARGET</code> to 14.0 (<a href="https://github.com/Slicer/Slicer/pull/8850">PR-8850</a>).</li>
<li>Add MSVC compatibility checks and improve <code>FindVcvars</code> support for old toolsets in newer Visual Studio versions (<a href="https://github.com/Slicer/Slicer/pull/9221">PR-9221</a>, <a href="https://github.com/Slicer/Slicer/pull/9206">PR-9206</a>).</li>
</ul>
<h4 id="heading--build-system">Build system</h4>
<ul>
<li>Raise minimum CMake version floor to 3.28 and remove dead version-conditional code (<a href="https://github.com/Slicer/Slicer/pull/9210">PR-9210</a>).</li>
<li>Enable CMake CMP0071 NEW behavior for extension builds (<a href="https://github.com/Slicer/Slicer/pull/8845">PR-8845</a>).</li>
<li>Prefer declaring CMake minimum and maximum required versions as variables (<a href="https://github.com/Slicer/Slicer/pull/8375">PR-8375</a>).</li>
<li>Add option for IDImageIO support in CMake configuration (<a href="https://github.com/Slicer/Slicer/pull/9023">PR-9023</a>).</li>
<li>Make Teem a private dependency (<a href="https://github.com/Slicer/Slicer/pull/9030">PR-9030</a>).</li>
<li>Unify generated <code>Export.h</code> usage in Base and MRML libraries (<a href="https://github.com/Slicer/Slicer/pull/9036">PR-9036</a>).</li>
<li>Remove unused SimpleITK shared-build option and switch SimpleITK to pre-built wheels (<a href="https://github.com/Slicer/Slicer/pull/8932">PR-8932</a>, <a href="https://github.com/Slicer/Slicer/pull/8923">PR-8923</a>).</li>
<li>Build oneTBB from source, update to 2022.3.0, and fix TBB install discovery on Linux (<a href="https://github.com/Slicer/Slicer/pull/8945">PR-8945</a>, <a href="https://github.com/Slicer/Slicer/pull/8951">PR-8951</a>).</li>
<li>Disable Brotli support in cURL configuration and fix static cURL link failures (<a href="https://github.com/Slicer/Slicer/pull/9007">PR-9007</a>, <a href="https://github.com/Slicer/Slicer/pull/9095">PR-9095</a>).</li>
<li>Update Slicer certificate creation to use a non-archived Mozilla repository (<a href="https://github.com/Slicer/Slicer/pull/8973">PR-8973</a>).</li>
</ul>
<h4 id="heading--dependencies">Dependencies</h4>
<ul>
<li>Update ITK to 5.4.5 and 5.4.6 (<a href="https://github.com/Slicer/Slicer/pull/8862">PR-8862</a>, <a href="https://github.com/Slicer/Slicer/pull/9125">PR-9125</a>).</li>
<li>Update VTK to 9.6.1 and 9.6.2 (<a href="https://github.com/Slicer/Slicer/pull/9087">PR-9087</a>, <a href="https://github.com/Slicer/Slicer/pull/9166">PR-9166</a>).</li>
<li>Update CTK for Qt 6, PythonQt, and latest upstream fixes (<a href="https://github.com/Slicer/Slicer/pull/8901">PR-8901</a>, <a href="https://github.com/Slicer/Slicer/pull/8938">PR-8938</a>, <a href="https://github.com/Slicer/Slicer/pull/8940">PR-8940</a>, <a href="https://github.com/Slicer/Slicer/pull/9097">PR-9097</a>, <a href="https://github.com/Slicer/Slicer/pull/9128">PR-9128</a>, <a href="https://github.com/Slicer/Slicer/pull/9202">PR-9202</a>, <a href="https://github.com/Slicer/Slicer/pull/9212">PR-9212</a>).</li>
<li>Update DCMTK to 3.7.0 series and include binary SEG/JPEG2000-related fixes (<a href="https://github.com/Slicer/Slicer/pull/8946">PR-8946</a>, <a href="https://github.com/Slicer/Slicer/pull/8948">PR-8948</a>, <a href="https://github.com/Slicer/Slicer/pull/8988">PR-8988</a>).</li>
<li>Update BRAINSTools from 2024-11-09 to 2025-11-10 (<a href="https://github.com/Slicer/Slicer/pull/8860">PR-8860</a>).</li>
<li>Update LibFFI to a 3.5.2-based version and fix LibFFI build errors (<a href="https://github.com/Slicer/Slicer/pull/8939">PR-8939</a>, <a href="https://github.com/Slicer/Slicer/pull/8943">PR-8943</a>).</li>
<li>Update cURL to 8.17.0 (<a href="https://github.com/Slicer/Slicer/pull/8959">PR-8959</a>).</li>
<li>Switch XZ to the official project repository and update to v5.8.2 (<a href="https://github.com/Slicer/Slicer/pull/8958">PR-8958</a>).</li>
<li>Switch sqlite-amalgamation to a maintained repository, update SQLite to 3.51.2, and fix sqlite linker failure (<a href="https://github.com/Slicer/Slicer/pull/8965">PR-8965</a>, <a href="https://github.com/Slicer/Slicer/pull/8969">PR-8969</a>).</li>
<li>Update Python packages and docs dependencies, including urllib3 security-related updates (<a href="https://github.com/Slicer/Slicer/pull/8844">PR-8844</a>, <a href="https://github.com/Slicer/Slicer/pull/9161">PR-9161</a>, <a href="https://github.com/Slicer/Slicer/pull/8966">PR-8966</a>, <a href="https://github.com/Slicer/Slicer/pull/8968">PR-8968</a>, <a href="https://github.com/Slicer/Slicer/pull/9222">PR-9222</a>).</li>
<li>Add missing <code>itkImageRegionIteratorWithIndex.h</code> includes (<a href="https://github.com/Slicer/Slicer/pull/9219">PR-9219</a>).</li>
<li>Disable ITKv4 legacy classes and re-enable specific legacy transform classes needed for compatibility (<a href="https://github.com/Slicer/Slicer/pull/8898">PR-8898</a>, <a href="https://github.com/Slicer/Slicer/pull/8911">PR-8911</a>).</li>
</ul>
<h4 id="heading--extensions-and-custom-applications">Extensions and custom applications</h4>
<ul>
<li>Add extension metadata fields for tier, DICOM support rule, recommended extensions, and keywords (<a href="https://github.com/Slicer/Slicer/pull/9040">PR-9040</a>).</li>
<li>Add JSON schema support for extension <code>dicom_support_rule</code> metadata (<a href="https://github.com/Slicer/Slicer/pull/9057">PR-9057</a>).</li>
<li>Fix failing extension description tests (<a href="https://github.com/Slicer/Slicer/pull/9112">PR-9112</a>).</li>
<li>Add unique startup RC files for custom applications and a <code>Slicer_USE_SLICERRC</code> build option to disable startup RC scripts (<a href="https://github.com/Slicer/Slicer/pull/9240">PR-9240</a>).</li>
<li>Fix test behavior when the extension manager is disabled (<a href="https://github.com/Slicer/Slicer/pull/8888">PR-8888</a>).</li>
</ul>
<h4 id="heading--continuous-integration-and-testing">Continuous integration and testing</h4>
<ul>
<li>Add and update tests for Qt 6, DICOM plugins, <code>slicer.packaging</code>, transform storage, and module behavior (<a href="https://github.com/Slicer/Slicer/pull/8919">PR-8919</a>, <a href="https://github.com/Slicer/Slicer/pull/9114">PR-9114</a>, <a href="https://github.com/Slicer/Slicer/pull/9010">PR-9010</a>, <a href="https://github.com/Slicer/Slicer/pull/8842">PR-8842</a>, <a href="https://github.com/Slicer/Slicer/pull/9242">PR-9242</a>).</li>
<li>Fix multiple QtTesting, AtlasTests, and module-specific test failures (<a href="https://github.com/Slicer/Slicer/pull/9162">PR-9162</a>, <a href="https://github.com/Slicer/Slicer/pull/9235">PR-9235</a>, <a href="https://github.com/Slicer/Slicer/pull/9241">PR-9241</a>, <a href="https://github.com/Slicer/Slicer/pull/9242">PR-9242</a>).</li>
<li>Update pre-commit hooks and address lint/codespell/type cleanup ([multiple commits in <code>v5.10.0..v5.12.0</code>]).</li>
</ul>
<h4 id="heading--style">Style</h4>
<ul>
<li>Fix multiple typing errors (<a href="https://github.com/Slicer/Slicer/pull/8996">PR-8996</a>).</li>
<li>Fix codespell errors (<a href="https://github.com/Slicer/Slicer/pull/9061">PR-9061</a>).</li>
<li>Fix typos in the CreateDICOMSeries GUI (<a href="https://github.com/Slicer/Slicer/pull/9103">PR-9103</a>).</li>
</ul>
<h3 id="heading--extensions-1">Extensions</h3>
<p>Listed below are extension catalog changes added to the 5.12 extension index branch since the Slicer 5.10.0 release cutoff.</p>
<h4 id="heading--new">New</h4>
<ul>
<li><a href="https://github.com/niyaziacer/SlicerAAL3BrainLabeling">AAL3BrainLabeling</a>: AAL3 atlas-based morphometric analysis pipeline for 3D Slicer using Elastix.
<ul>
<li>Category: Neuroimaging</li>
<li>Tier: 1</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc7b896247206aed02e944b9e564b03f05637e2d.jpeg" data-download-href="/uploads/short-url/qTorjjBEFBLJwHI83DQE1i2xa7X.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc7b896247206aed02e944b9e564b03f05637e2d.jpeg" alt="image" data-base62-sha1="qTorjjBEFBLJwHI83DQE1i2xa7X" width="128" height="128"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">256×256 24.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://github.com/benzwick/SlicerAdaptiveBrush.git">AdaptiveBrush</a>: Adaptive brush segment editor effect that segments based on image intensity similarity, stopping at edges and boundaries.
<ul>
<li>Category: Segmentation</li>
<li>Tier: 1</li>
</ul>
</li>
<li><a href="https://github.com/ImagingDataCommons/SlicerCrossSegmentationExplorer">CrossSegmentationExplorer</a>: Tools for the visual inspection and comparison of multiple segmentations on the same volume.
<ul>
<li>Category: Segmentation</li>
<li>Tier: 1</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89d66ed98a17a2015f12a34756be853d63399c4e.jpeg" data-download-href="/uploads/short-url/jFmPI5sly2zCBbIETdR5vZiQV1c.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89d66ed98a17a2015f12a34756be853d63399c4e_2_128x128.jpeg" alt="image" data-base62-sha1="jFmPI5sly2zCBbIETdR5vZiQV1c" width="128" height="128" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89d66ed98a17a2015f12a34756be853d63399c4e_2_128x128.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89d66ed98a17a2015f12a34756be853d63399c4e_2_192x192.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89d66ed98a17a2015f12a34756be853d63399c4e_2_256x256.jpeg 2x" data-dominant-color="D6D6D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1828×1828 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://gitlab.in2p3.fr/iftim/public-projects/SlicerDelineateLiverRT.git">DelineateLiverRT</a>: Clinical decision-support extension for nuclear medicine supporting liver tumor treatment workflows with SPECT/CT and PET/CT imaging. Provides three integrated modules: automatic AI-based liver and tumor segmentation (SegModule), multimodal image registration (RecModule), and patient-specific dosimetry computation using LDM/VDK physical models (DosiModule).
<ul>
<li>Category: Nuclear Medicine</li>
<li>Tier: 1</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70f58fbbba70cc6d0eb661b72c829ce79f4bbcbe.png" data-download-href="/uploads/short-url/g7hAyLcZu33o5COpF1DKPF7nBZc.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70f58fbbba70cc6d0eb661b72c829ce79f4bbcbe.png" alt="image" data-base62-sha1="g7hAyLcZu33o5COpF1DKPF7nBZc" width="128" height="128"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">128×128 11 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://github.com/DeepReasoningAI/SlicerDRAISegmentation.git">DRAISegmentation</a>: AI-powered segmentation for Spine/Pelvis (CT) and Aorta–Iliac–Femoral Arteries (CTA). For Spine/Pelvis CT, we generate individual segmentation masks for each vertebra, as well as the pelvis and sacrum; for CTA, we segment all traceable arteries below the aortic arch. Moreover, we can separate metal. Upload CT volumes to the DRAI cloud and receive high-quality, multi-label masks directly in 3D Slicer within minutes. Built to handle complex cases—including bypass grafts, occuled arteries, extreme scoliosis, metal implants, and challenging pathology—with reliable accuracy. All data is securely processed and deleted immediately after inference. Questions? Contact <a href="mailto:support@deepreasoningai.com">support@deepreasoningai.com</a>.
<ul>
<li>Category: Segmentation</li>
<li>Tier: 1</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6cd1dfa15ac45e63315f8d8ec6833f7e0f1981f.jpeg" data-download-href="/uploads/short-url/smG01VS6ep2CRToZ7Ullaz58Fwb.jpeg?dl=1" title="image.jpg"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6cd1dfa15ac45e63315f8d8ec6833f7e0f1981f_2_256x62.jpeg" data-base62-sha1="smG01VS6ep2CRToZ7Ullaz58Fwb" width="256" height="62" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6cd1dfa15ac45e63315f8d8ec6833f7e0f1981f_2_256x62.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6cd1dfa15ac45e63315f8d8ec6833f7e0f1981f_2_384x93.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6cd1dfa15ac45e63315f8d8ec6833f7e0f1981f_2_512x124.jpeg 2x" data-dominant-color="BEC3D3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">1920×466 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://github.com/cuneytozdemir/SlicerFootSegmentation.git">FootSegmentation</a>: AI-powered automatic 3D foot segmentation using deep learning
<ul>
<li>Category: Segmentation</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/8593fd8710cbb2ca7cb340dbdab3cd0f4add20b2.jpeg" data-download-href="/uploads/short-url/j3Gzqwkj3hQqcwKG0Z0vSgGFmx4.jpeg?dl=1" title="image.jpg"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/8593fd8710cbb2ca7cb340dbdab3cd0f4add20b2_2_128x91.jpeg" data-base62-sha1="j3Gzqwkj3hQqcwKG0Z0vSgGFmx4" width="128" height="91" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/8593fd8710cbb2ca7cb340dbdab3cd0f4add20b2_2_128x91.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/8593fd8710cbb2ca7cb340dbdab3cd0f4add20b2_2_192x136.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/8593fd8710cbb2ca7cb340dbdab3cd0f4add20b2_2_256x182.jpeg 2x" data-dominant-color="8BB6D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">714×509 60.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://github.com/vboussot/SlicerImpactReg">ImpactReg</a>: Slicer IMPACT-Reg is a 3D Slicer module dedicated to multimodal medical image registration. It integrates the IMPACT deep semantic similarity metric within the Elastix registration engine and exposes predefined registration presets through a simple graphical interface.
<ul>
<li>Category: Registration</li>
<li>Tier: 3</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a8ac4006936778e6694136fc08960ee087829e8.jpeg" data-download-href="/uploads/short-url/jLBc5fTAWyhj7CKLwpONyWma5sY.jpeg?dl=1" title="ImpactReg logo"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a8ac4006936778e6694136fc08960ee087829e8_2_128x128.jpeg" data-base62-sha1="jLBc5fTAWyhj7CKLwpONyWma5sY" alt="ImpactReg logo" width="128" height="128" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a8ac4006936778e6694136fc08960ee087829e8_2_128x128.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a8ac4006936778e6694136fc08960ee087829e8_2_192x192.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a8ac4006936778e6694136fc08960ee087829e8_2_256x256.jpeg 2x" data-dominant-color="C3BEBC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ImpactReg logo</span><span class="informations">1024×1024 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://github.com/vboussot/SlicerImpactSynth">ImpactSynth</a>: Deep learning-based synthetic CT generation, sCT segmentation, and quality assurance tools powered by KonfAI IMPACT-Synth models.
<ul>
<li>Category: Image Synthesis</li>
<li>Tier: 3</li>
</ul>
</li>
<li><a href="https://github.com/Atakanisik/SlicerIVIMFit.git">IVIMFitSlicer</a>: Advanced IVIM Analysis tool with ROI-based fitting
<ul>
<li>Category: Diffusion</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bc28e8bd7cf033a67576c626d6bcf6b0c653a8e.png" data-download-href="/uploads/short-url/d5KhIULxW0p6PAQjR3x3MRgjYT4.png?dl=1" title="IVIMFitSlicer logo"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bc28e8bd7cf033a67576c626d6bcf6b0c653a8e.png" data-base62-sha1="d5KhIULxW0p6PAQjR3x3MRgjYT4" alt="IVIMFitSlicer logo" width="128" height="128"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IVIMFitSlicer logo</span><span class="informations">128×128 4.46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://github.com/vboussot/SlicerKonfAI">KonfAI</a>: An extension enabling fast and configurable deep learning inference in 3D Slicer using KonfAI models from the Hugging Face repository.
<ul>
<li>Category: Pipelines</li>
<li>Tier: 3</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad70b337464cbacb9fb04646b9b51a12300fb162.jpeg" data-download-href="/uploads/short-url/oKk3N5uLQA6qWujq6MkGVrrnKbE.jpeg?dl=1" title="KonfAI logo"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad70b337464cbacb9fb04646b9b51a12300fb162_2_128x64.jpeg" data-base62-sha1="oKk3N5uLQA6qWujq6MkGVrrnKbE" alt="KonfAI logo" width="128" height="64" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad70b337464cbacb9fb04646b9b51a12300fb162_2_128x64.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad70b337464cbacb9fb04646b9b51a12300fb162_2_192x96.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad70b337464cbacb9fb04646b9b51a12300fb162_2_256x128.jpeg 2x" data-dominant-color="243237"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">KonfAI logo</span><span class="informations">1024×512 49.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://github.com/benzwick/SlicerMouseMaster.git">MouseMaster</a>: Advanced mouse button customization for multi-button mice with preset management and context-sensitive bindings.
<ul>
<li>Category: Utilities</li>
</ul>
</li>
<li><a href="https://github.com/MuscleMap/SlicerMuscleMap">MuscleMap</a>: A 3D Slicer extension to the MuscleMap whole-body segmentation model.
<ul>
<li>Category: Segmentation</li>
<li>Tier: 1</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f8f34f36770728a3e11406ab7cb98d21e4ad4a6.jpeg" data-download-href="/uploads/short-url/icrsouzfcFZ3aGYxVCYjz2HA0NU.jpeg?dl=1" title="MuscleMap logo"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f8f34f36770728a3e11406ab7cb98d21e4ad4a6_2_128x115.jpeg" data-base62-sha1="icrsouzfcFZ3aGYxVCYjz2HA0NU" alt="MuscleMap logo" width="128" height="115" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f8f34f36770728a3e11406ab7cb98d21e4ad4a6_2_128x115.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f8f34f36770728a3e11406ab7cb98d21e4ad4a6_2_192x172.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f8f34f36770728a3e11406ab7cb98d21e4ad4a6_2_256x230.jpeg 2x" data-dominant-color="191A16"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MuscleMap logo</span><span class="informations">1458×1316 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://github.com/niyaziacer/SlicerOpenMAPT1Auto.git">OpenMAPT1Auto</a>: Automated brain MRI parcellation into 280 anatomical regions using OpenMAP-T1 deep learning model. NON-COMMERCIAL USE ONLY.
<ul>
<li>Category: Segmentation</li>
<li>Tier: 1</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9411f0de6b11394f73c491bdcdcfdbbe225261a9.png" data-download-href="/uploads/short-url/l7T6r3POYdpKmERPm4VZRYh4Lbj.png?dl=1" title="OpenMAPT1Auto logo"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9411f0de6b11394f73c491bdcdcfdbbe225261a9.png" data-base62-sha1="l7T6r3POYdpKmERPm4VZRYh4Lbj" alt="OpenMAPT1Auto logo" width="128" height="128"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">OpenMAPT1Auto logo</span><span class="informations">128×128 495 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://github.com/radiuma-com/SlicerPySERA">PySERA</a>: PySERA radiomics extraction library integrated into 3D Slicer.
<ul>
<li>Category: Analysis</li>
<li>Tier: 1</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81372c6914a7cc133caa840a5802312cff2d2f35.png" data-download-href="/uploads/short-url/ir5NK7no1IOgH5wb0TbCGJLJ2nP.png?dl=1" title="PySERA logo"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81372c6914a7cc133caa840a5802312cff2d2f35_2_128x157.png" data-base62-sha1="ir5NK7no1IOgH5wb0TbCGJLJ2nP" alt="PySERA logo" width="128" height="157" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81372c6914a7cc133caa840a5802312cff2d2f35_2_128x157.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81372c6914a7cc133caa840a5802312cff2d2f35_2_192x235.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81372c6914a7cc133caa840a5802312cff2d2f35_2_256x314.png 2x" data-dominant-color="DCE2EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PySERA logo</span><span class="informations">1094×1345 70.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://github.com/LuisParedesOcampo/SlicerRadReirradiation">RadReirradiation</a>: A clinical tool for Reirradiation analysis, EQD2 dose calculation, and integrated DVH metrics.
<ul>
<li>Category: Radiotherapy</li>
<li>Tier: 1</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/467ceef70a74a560e987cb255387070d395941a1.png" data-download-href="/uploads/short-url/a3z5GdG6lRA2vIVQELEftf1AkXT.png?dl=1" title="RadReirradiation logo"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/467ceef70a74a560e987cb255387070d395941a1.png" data-base62-sha1="a3z5GdG6lRA2vIVQELEftf1AkXT" alt="RadReirradiation logo" width="128" height="128"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">RadReirradiation logo</span><span class="informations">128×128 20.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://github.com/liukuan5625/SlicerScapularMorphology">ScapularMorphology</a>: Scapular Morphology for glenoid segmentation and landmarks location.
<ul>
<li>Category: Segmentation</li>
<li>Tier: 1</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76f9a5bfa60c81d159036607375aa9a992563fb8.jpeg" data-download-href="/uploads/short-url/gYvcWjLzYkoghJ9wGbl6qJNfeRO.jpeg?dl=1" title="ScapularMorphology logo"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76f9a5bfa60c81d159036607375aa9a992563fb8_2_128x128.jpeg" data-base62-sha1="gYvcWjLzYkoghJ9wGbl6qJNfeRO" alt="ScapularMorphology logo" width="128" height="128" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76f9a5bfa60c81d159036607375aa9a992563fb8_2_128x128.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76f9a5bfa60c81d159036607375aa9a992563fb8_2_192x192.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76f9a5bfa60c81d159036607375aa9a992563fb8_2_256x256.jpeg 2x" data-dominant-color="C1BFBF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ScapularMorphology logo</span><span class="informations">667×669 80 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://github.com/EpiReC-ISARG/SlicerSEEGContactDetector">SEEGContactDetector</a>: SEEG Contact Detector is a extension for automatic localization of stereoelectroencephalography electrode contact centers from post-implantation CT data. The module uses a model-based approach that respects electrode geometry and accounts for bending, twisting, and partial contact visibility. It supports optional MRI-based brain masking, manual correction tools, and interactive visualization for efficient clinical review.
<ul>
<li>Category: IGT</li>
<li>Tier: 3</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fcc19d6679a6269fbc0034d10a7dee91e0816de.png" data-download-href="/uploads/short-url/kw5ySenDAs5vkIhfHsHWDKxVYzI.png?dl=1" title="image.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fcc19d6679a6269fbc0034d10a7dee91e0816de.png" data-base62-sha1="kw5ySenDAs5vkIhfHsHWDKxVYzI" width="128" height="128"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">128×128 4.48 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://github.com/esheo-skia/Slicer-SegTemplateEditor.git">SegTemplateEditor</a>: Extension for creating and managing reusable segmentation templates with predefined segment names and colors
<ul>
<li>Category: Segmentation</li>
<li>Tier: 1</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c252f275b9cb9e02364fd255c29cd7ac1e83eaba.jpeg" data-download-href="/uploads/short-url/rJ4lf3TOz1rNvXDffHUrphcqrrQ.jpeg?dl=1" title="SegTemplateEditor logo"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c252f275b9cb9e02364fd255c29cd7ac1e83eaba_2_128x128.jpeg" data-base62-sha1="rJ4lf3TOz1rNvXDffHUrphcqrrQ" alt="SegTemplateEditor logo" width="128" height="128" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c252f275b9cb9e02364fd255c29cd7ac1e83eaba_2_128x128.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c252f275b9cb9e02364fd255c29cd7ac1e83eaba_2_192x192.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c252f275b9cb9e02364fd255c29cd7ac1e83eaba_2_256x256.jpeg 2x" data-dominant-color="E8E9E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SegTemplateEditor logo</span><span class="informations">1024×1024 57.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://github.com/SimVascular/SlicerSimVascular">SimVascular</a>: SimVascular extensions developed by Marsden lab members and associates for 3D Slicer.
<ul>
<li>Category: Simulation</li>
<li>Tier: 3</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6ef9f3766b4f837133228d390e32912e66f6421.png" data-download-href="/uploads/short-url/zeuQpAGZIrysrBygjcmkoZ4pIaJ.png?dl=1" title="SimVascular logo"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6ef9f3766b4f837133228d390e32912e66f6421.png" data-base62-sha1="zeuQpAGZIrysrBygjcmkoZ4pIaJ" alt="SimVascular logo" width="128" height="128"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SimVascular logo</span><span class="informations">285×285 66.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://github.com/wallematthias/SlicerTimelapsedHRpQCT">TimelapsedHRpQCTSlicer</a>: HR-pQCT toolbox for 3D Slicer with longitudinal timelapsed analysis, motion scoring, Scanco AIM I/O, and contouring/segmentation workflow modules.
<ul>
<li>Category: Quantification</li>
<li>Tier: 1</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af45c0ec5d4677d5a9c08f4ee9ba010d84ec5930.jpeg" data-download-href="/uploads/short-url/p0x0enIvYfU7CUdYq79IQoaafaU.jpeg?dl=1" title="TimelapsedHRpQCTSlicer logo"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af45c0ec5d4677d5a9c08f4ee9ba010d84ec5930_2_128x123.jpeg" data-base62-sha1="p0x0enIvYfU7CUdYq79IQoaafaU" alt="TimelapsedHRpQCTSlicer logo" width="128" height="123" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af45c0ec5d4677d5a9c08f4ee9ba010d84ec5930_2_128x123.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af45c0ec5d4677d5a9c08f4ee9ba010d84ec5930_2_192x184.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af45c0ec5d4677d5a9c08f4ee9ba010d84ec5930_2_256x246.jpeg 2x" data-dominant-color="AD9D94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">TimelapsedHRpQCTSlicer logo</span><span class="informations">740×712 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://github.com/niyaziacer/SlicerVolBrain.git">volbrain</a>: 3D Slicer extension for comprehensive brain structure volume calculation and 3D visualization from volBrain segmentation outputs. Supports 108+ cortical regions, tissue classification, lobes, and macrostructures.
<ul>
<li>Category: Quantification</li>
<li>Tier: 1</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fb00a3c3729559b7788763ff700954d703d3588.jpeg" data-download-href="/uploads/short-url/95pfa5cX9Tpsdf7G9lmNB7VWtXG.jpeg?dl=1" title="volbrain logo"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fb00a3c3729559b7788763ff700954d703d3588.jpeg" data-base62-sha1="95pfa5cX9Tpsdf7G9lmNB7VWtXG" alt="volbrain logo" width="128" height="103"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volbrain logo</span><span class="informations">423×342 76.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li><a href="https://github.com/lassoan/SlicerVoxTell">VoxTell</a>: VoxTell lets users segment 3D medical scans in 3D Slicer using plain-language prompts (for example, liver or right kidney).
<ul>
<li>Category: Segmentation</li>
<li>Tier: 5</li>
<li><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5099de47780c428fa1277eece092e2c03d5c252.png" data-download-href="/uploads/short-url/uoCiUyjEprFthHDtLobK3RSkrx8.png?dl=1" title="VoxTell logo"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5099de47780c428fa1277eece092e2c03d5c252.png" data-base62-sha1="uoCiUyjEprFthHDtLobK3RSkrx8" alt="VoxTell logo" width="128" height="128"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">VoxTell logo</span><span class="informations">256×256 43.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
</ul>
<h4 id="heading--renamed">Renamed</h4>
<ul>
<li><a href="https://github.com/OpenwaterHealth/SlicerOpenLIFU.git">OpenLIFU</a>: A 3D Slicer extension for Openwater’s OpenLIFU (Low Intensity Focused Ultrasound) research platform. Licensed under AGPL (a strong copyleft license that may impose restrictions on combined works).
<ul>
<li>Renamed from: SlicerOpenLIFU</li>
</ul>
</li>
</ul>
<h4 id="heading--updated">Updated</h4>
<ul>
<li><a href="https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools.git">AutomatedDentalTools</a>: This extension will allow clinicians to perform automatic CBCT scan segmentation as well as automatic lamndmark identification in CBCT and IOS using machine learning tools.
<ul>
<li>Update: category metadata updated.</li>
</ul>
</li>
<li><a href="https://github.com/SoniaPujolLab/SlicerLanguagePacks">LanguagePacks</a>: Extension for deploying language packs and editing translations.
<ul>
<li>Update: repository URL updated.</li>
</ul>
</li>
<li><a href="https://github.com/MHubAI/SlicerMHubRunner">MHubRunner</a>: MHub Runner is a 3D Slicer plugin that seamlessly integrates Deep Learning models from the Medical Hub repository (MHub) into 3D Slicer.
<ul>
<li>Update: repository URL updated.</li>
</ul>
</li>
<li><a href="https://github.com/QIICR/Slicer-PETDICOMExtension.git">PETDICOMExtension</a>: The PET DICOM Extension provides tools to import PET Standardized Uptake Value images from DICOM into Slicer.
<ul>
<li>Update: DICOM support rule and metadata schema updated.</li>
</ul>
</li>
<li><a href="https://github.com/QIICR/QuantitativeReporting.git">QuantitativeReporting</a>: Segmentation-based measurements with DICOM-based import and export of the results.
<ul>
<li>Update: dependencies, DICOM support rule, and metadata schema updated.</li>
</ul>
</li>
<li><a href="https://github.com/SlicerDMRI/SlicerDMRI.git">SlicerDMRI</a>: SlicerDMRI provides tools to load diffusion MRI image data, perform tractography, and quantify results.
<ul>
<li>Update: DICOM support rule and metadata schema updated.</li>
</ul>
</li>
<li><a href="https://github.com/SlicerHeart/SlicerHeart.git">SlicerHeart</a>: Modules for cardiac analysis and intervention planning and guidance
<ul>
<li>Update: DICOM support rule and metadata schema updated.</li>
</ul>
</li>
<li><a href="https://github.com/SlicerMorph/SlicerMorph.git">SlicerMorph</a>: This extension enables retrieval, visualization, measurement and annotation of high-resolution specimen data from volumetric scans (CTs and MRs) or 3D surface scans.
<ul>
<li>Update: revision updated.</li>
</ul>
</li>
<li><a href="https://github.com/SlicerRt/SlicerRT.git">SlicerRT</a>: Toolkit for radiation therapy research. Features include DICOM-RT import/export, dose volume histogram, dose accumulation, external beam planning (TPS), structure comparison, isodose line/surface generation, etc.
<ul>
<li>Update: DICOM support rule and metadata schema updated.</li>
</ul>
</li>
<li><a href="https://github.com/SoniaPujolLab/SlicerTutorialMaker.git">TutorialMaker</a>: The Tutorial Maker is currently in an experimental development phase. It provides a framework for generating 3D Slicer tutorials that can be translated into multiple languages.
<ul>
<li>Update: category metadata and repository URL updated.</li>
</ul>
</li>
</ul>
<h4 id="heading--removed">Removed</h4>
<ul>
<li><a href="https://github.com/QIICR/dcmqi.git">DCMQI</a>
<ul>
<li>Category: DICOM</li>
<li>Tier: 5</li>
</ul>
</li>
<li><a href="https://github.com/QIICR/PETLiverUptakeMeasurement">PETLiverUptakeMeasurement</a>
<ul>
<li>Category: Quantification</li>
<li>Tier: 3</li>
</ul>
</li>
</ul>

---

## Post #2 by @ebrahim (2026-07-10 12:01 UTC)

<h1><a name="p-134813-changelog-5121-1" class="anchor" href="#p-134813-changelog-5121-1" aria-label="Heading link"></a>Changelog: 5.12.1</h1>
<h2 id="heading--core">Core</h2>
<h3 id="heading--fixes">Fixes</h3>
<ul>
<li>Disable the <code>pip_install</code> progress UI when called outside the main thread, allowing blocking package installation to proceed safely (<a href="https://github.com/Slicer/Slicer/pull/9273">PR-9273</a>)</li>
</ul>
<h2 id="heading--infrastructure">Infrastructure</h2>
<h3 id="heading--dependencies">Dependencies</h3>
<ul>
<li>Update DCMTKcs so OpenJPEG is linked privately on macOS, fixing extension packages that failed to load because they unnecessarily referenced <code>libopenjp2</code> (<a href="https://github.com/Slicer/Slicer/pull/9263">PR-9263</a>)</li>
</ul>

---

## Post #3 by @Juergen (2026-07-10 19:22 UTC)

<p><a class="mention" href="/u/ebrahim">@ebrahim</a> Great news, I would like to try some of these updated tools.</p>
<p>I entirely rely on SlicerJupyter and I hoped that SlicerJupyter would get resurrected also for the Windows OS at some point so that I can use more updated Slicer tools, too. Any chance this might happen some time soon?</p>
<p>Thanks, Juergen</p>

---

## Post #4 by @ebrahim (2026-07-10 19:43 UTC)

<p><a class="mention" href="/u/juergen">@Juergen</a> I think the last activity is still <a href="https://github.com/Slicer/SlicerJupyter/pull/79">the linux fix</a>, which I hope works but I have not tested it for a while. Working on Windows is not convenient for me so no promises, but if I get a chance to take a look and attempt a fix I will take a look. I also would like it work.</p>
<p>You may be happy to hear also that the long term aspirations for many Slicer developers, post slicer 6.0 probably, is to move towards making it easier and easier to call upon Slicer as a tool from Python rather than calling upon Python as a tool from Slicer (“the great inversion” as we’ve been calling it).</p>

---

## Post #5 by @Juergen (2026-07-10 19:53 UTC)

<p>Love the Great Inversion! Appreciate your help.</p>

---

## Post #6 by @muratmaga (2026-07-10 20:10 UTC)

<p>Isn’t the dynamic library issue on MacOS supposed to be solved with the patch release? I am still seeing the same error with 5.12.1:</p>
<p>[Qt] Error(s):</p>
<p>[Qt] Cannot load library /Applications/Slicer.app/Contents/Extensions-34624/MarkupsToModel/lib/Slicer-5.12/qt-loadable-modules/libqSlicerMarkupsToModelModule.dylib: (dlopen(/Applications/Slicer.app/Contents/Extensions-34624/MarkupsToModel/lib/Slicer-5.12/qt-loadable-modules/libqSlicerMarkupsToModelModule.dylib, 0x0085): Library not loaded: libopenjp2.7.dylib</p>
<p>[Qt] Referenced from: &lt;8AB6103B-BD3F-3B06-B823-E5A294A0BE71&gt; /Applications/Slicer.app/Contents/Extensions-34624/MarkupsToModel/lib/Slicer-5.12/libdcmjp2kcs.20.dylib</p>
<p>[Qt] Reason: tried: ‘libopenjp2.7.dylib’ (relative path not allowed in hardened program), ‘/System/Volumes/Preboot/Cryptexes/OSlibopenjp2.7.dylib’ (no such file), ‘libopenjp2.7.dylib’ (relative path not allowed in hardened program))</p>
<p>[Qt] Error(s):</p>
<p>[Qt] Cannot load library /Applications/Slicer.app/Contents/Extensions-34624/SurfaceMarkup/lib/Slicer-5.12/qt-loadable-modules/libqSlicerGridSurfaceMarkupsModule.dylib: (dlopen(/Applications/Slicer.app/Contents/Extensions-34624/SurfaceMarkup/lib/Slicer-5.12/qt-loadable-modules/libqSlicerGridSurfaceMarkupsModule.dylib, 0x0085): Library not loaded: libopenjp2.7.dylib</p>
<p>[Qt] Referenced from: &lt;8AB6103B-BD3F-3B06-B823-E5A294A0BE71&gt; /Applications/Slicer.app/Contents/Extensions-34624/SurfaceMarkup/lib/Slicer-5.12/libdcmjp2kcs.20.dylib</p>
<p>[Qt] Reason: tried: ‘libopenjp2.7.dylib’ (relative path not allowed in hardened program), ‘/System/Volumes/Preboot/Cryptexes/OSlibopenjp2.7.dylib’ (no such file), ‘libopenjp2.7.dylib’ (relative path not allowed in hardened program))</p>
<p>dlopen(/Applications/Slicer.app/Contents/Extensions-34624/Sandbox/lib/Slicer-5.12/qt-loadable-modules/vtkSlicerCombineModelsModuleLogicPython.so, 0x0002): Library not loaded: libopenjp2.7.dylib</p>
<p>Referenced from: &lt;8AB6103B-BD3F-3B06-B823-E5A294A0BE71&gt; /Applications/Slicer.app/Contents/Extensions-34624/Sandbox/lib/Slicer-5.12/libdcmjp2kcs.20.dylib</p>
<p>Reason: tried: ‘libopenjp2.7.dylib’ (relative path not allowed in hardened program), ‘/System/Volumes/Preboot/Cryptexes/OSlibopenjp2.7.dylib’ (no such file), ‘libopenjp2.7.dylib’ (relative path not allowed in hardened program)</p>
<p>[Qt] libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space</p>
<p>[Qt] libpng warning: iCCP: known incorrect sRGB profile</p>
<p>dlopen(/Applications/Slicer.app/Contents/Extensions-34624/SegmentEditorExtraEffects/lib/Slicer-5.12/qt-loadable-modules/vtkSlicerSegmentEditorFastMarchingModuleLogicPython.so, 0x0002): Library not loaded: libopenjp2.7.dylib</p>
<p>Referenced from: &lt;8AB6103B-BD3F-3B06-B823-E5A294A0BE71&gt; /Applications/Slicer.app/Contents/Extensions-34624/SegmentEditorExtraEffects/lib/Slicer-5.12/libdcmjp2kcs.20.dylib</p>
<p>Reason: tried: ‘libopenjp2.7.dylib’ (relative path not allowed in hardened program), ‘/System/Volumes/Preboot/Cryptexes/OSlibopenjp2.7.dylib’ (no such file), ‘libopenjp2.7.dylib’ (relative path not allowed in hardened program)</p>

---

## Post #7 by @ebrahim (2026-07-16 01:36 UTC)

<h1><a name="p-134932-changelog-5122-1" class="anchor" href="#p-134932-changelog-5122-1" aria-label="Heading link"></a>Changelog: 5.12.2</h1>
<ul>
<li>Clean rebuild of 5.12.1, no other changes.</li>
</ul>

---
