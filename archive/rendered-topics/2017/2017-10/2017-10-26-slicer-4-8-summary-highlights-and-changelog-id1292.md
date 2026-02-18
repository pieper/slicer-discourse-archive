# Slicer 4.8: Summary, Highlights and Changelog

**Topic ID**: 1292
**Date**: 2017-10-26
**URL**: https://discourse.slicer.org/t/slicer-4-8-summary-highlights-and-changelog/1292

---

## Post #1 by @jcfr (2017-10-26 21:05 UTC)

<h1>Table of Contents</h1>
<ul>
<li><a href="#heading--summary">Summary</a></li>
<li><a href="#heading--highlights">Highlights</a></li>
<li>
<a href="#heading--changelog">Changelog</a>
<ul>
<li><a href="#heading--core">Core</a></li>
<li><a href="#heading--io">IO</a></li>
<li><a href="#heading--api-updates-and-python-scripting">API updates and Python Scripting</a></li>
<li><a href="#heading--build-system-continuous-integration-software-process-release-process">Build System, Continuous Integration, Software Process, Release Process</a></li>
<li>
<a href="#heading--modules">Modules</a>
<ul>
<li><a href="#heading--segmentations">Segmentations</a></li>
<li><a href="#heading--volumes">Volumes</a></li>
<li><a href="#heading--sceneviews">SceneViews</a></li>
<li><a href="#heading--dicom">DICOM</a></li>
<li><a href="#heading--cropvolume">CropVolume</a></li>
<li><a href="#heading--endoscope">Endoscope</a></li>
<li><a href="#heading--openigtlink">OpenIGTLink</a></li>
<li><a href="#heading--tables">Tables</a></li>
<li><a href="#heading--surfacetoolbox">SurfaceToolbox</a></li>
<li><a href="#heading--transform">Transform</a></li>
<li><a href="#heading--sampledata">SampleData</a></li>
<li><a href="#heading--data">Data</a></li>
<li><a href="#heading--volumerendering">VolumeRendering</a></li>
<li><a href="#heading--terminology-new-module">Terminology (New module)</a></li>
<li><a href="#heading--screencapture">ScreenCapture</a></li>
</ul>
</li>
<li>
<a href="#heading--extensions">Extensions</a>
<ul>
<li><a href="#heading--new">New</a></li>
<li><a href="#heading--improved">Improved</a></li>
</ul>
</li>
</ul>
</li>
</ul>

<h1 id="heading--summary">Summary</h1>
<p>The community of 3D Slicer developers is proud to announce that version 4.8 is <a href="http://download.slicer.org/">now available for download</a>. This version introduces close to 1,000 feature enhancements and bug fixes for better performance and stability. It includes more than 15 new-and-improved core modules and dozens of updated extensions.</p>
<p>The development of 3D Slicer—including its numerous modules, extensions, datasets, pull requests, patches, issues reports, suggestions—is made possible by users, developers, contributors and commercial partners around the world. This development is funded by various grants and agencies. For more details, please see the 3D Slicer <a href="https://www.slicer.org/wiki/Documentation/%7B%7Bdocumentation/version%7D%7D/Acknowledgments">Acknowledgments</a> page.</p>
<p><a href="https://www.slicer.org">slicer.org</a> is the portal to the application, training materials, and the development community.</p>
<p>The <a href="https://www.slicer.org/wiki/Documentation/4.8/Training">Slicer Training</a> page provides a series of tutorials and data sets for training in the use of Slicer.</p>
<p><em>Please note that Slicer continues to be a research package and is not intended for clinical use. Testing of functionality is an ongoing activity with high priority, however, some features of Slicer are not fully tested.</em></p>
<h1 id="heading--highlights">Highlights
</h1><p>Slicer 4.8 highlights are:</p>
<ul>
<li>
<p>Simpler <a href="https://wiki.slicer.org/slicerWiki/index.php/Documentation/4.8/Modules/Data">Data</a> module integrating the Subject Hierarchy.</p>
</li>
<li>
<p><a href="https://wiki.slicer.org/slicerWiki/index.php/Documentation/4.8/Modules/Segmentations">Segmentations</a> module improvements including addition of new effects like Grow from seeds, Fill between slices, Surface cut, Mask Volume, Watershed, Fast marching and Flood Filling.</p>
</li>
<li>
<p>Improvements to slice viewers including better <a href="https://wiki.slicer.org/slicerWiki/index.php/Documentation/4.8/SlicerApplication/MainApplicationGUI#Crosshair_Options">crosshair usability</a> and support for slice model projection.</p>
</li>
<li>
<p>Support for <a href="https://blog.kitware.com/3d-slicer-adds-volumetric-mesh-support/">Volumetric Meshes</a>.</p>
</li>
<li>
<p><a href="https://wiki.slicer.org/slicerWiki/index.php/Documentation/4.8/Modules/DICOM">DICOM</a> support improvements including supports for definition of semantic meanings and faster imports.</p>
</li>
<li>
<p><a href="https://wiki.slicer.org/slicerWiki/index.php/Documentation/4.8/Modules/Transforms">Transforms</a> module improvements including support for interactively updating transform in the 3D view and visualization of displacements of individual points.</p>
</li>
<li>
<p>Support for <a href="https://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Developers/Plots">fast and interactive plotting</a> using VTK Charts.</p>
</li>
<li>
<p>More than 15 new and improved core modules.</p>
</li>
<li>
<p>Dozens of new and improved extensions.</p>
</li>
<li>
<p>Transition from mailing list to <a href="https://discourse.slicer.org/">Slicer discourse forum</a>.</p>
</li>
</ul>
<h1 id="heading--changelog">Changelog</h1>
<h2 id="heading--core">Core</h2>
<ul>
<li>
<p>Features:</p>
<ul>
<li>
<p>Add volumetric mesh support in vtkMRMLModelNode.</p>
<ul>
<li>
<p><a href="https://blog.kitware.com/3d-slicer-adds-volumetric-mesh-support/">https://blog.kitware.com/3d-slicer-adds-volumetric-mesh-support/</a></p>
</li>
<li>
<p><a href="https://www.researchgate.net/project/3D-Slicer/update/5893511c934940fcce426a70">https://www.researchgate.net/project/3D-Slicer/update/5893511c934940fcce426a70</a></p>
</li>
<li>
<p>Add straight vs whole cell clipping option for meshes.</p>
</li>
</ul>
</li>
<li>
<p>Interactive plotting</p>
<ul>
<li>
<p>Allows plotting directly from Table node contents, faster plotting, and interactive plot manipulation. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots</a>.</p>
</li>
<li>
<p>The features is already usable but further significant improvements are expected in nightly builds.</p>
</li>
</ul>
</li>
<li>
<p>Crosshair</p>
<ul>
<li>
<p>Improve crosshair usability adding display in 3D view.</p>
</li>
<li>
<p>Add centered slice jump crosshair behavior.</p>
</li>
<li>
<p>Crosshair position is only synchronized between view in the same ViewGroup</p>
</li>
</ul>
</li>
<li>
<p>Models</p>
<ul>
<li>
<p>Add option to display model projected to slice (not just display intersection).</p>
</li>
<li>
<p>Add distance-based coloring option to model slice projection display. (different color based on which side of the slice the model is and how far)</p>
</li>
</ul>
</li>
<li>
<p>Colors:</p>
<ul>
<li>Adding support for “diverging colormap” and perceptually uniform colormaps.</li>
</ul>
</li>
<li>
<p>Change default DTI glyph type to line which is faster &amp; clearer for normal use.</p>
</li>
<li>
<p>Slice viewer</p>
<ul>
<li>
<p>Add slice view zoom in/out using Ctrl+MouseWheel.</p>
</li>
<li>
<p>Add opacity setting for 2D slice intersections.</p>
</li>
<li>
<p>Slice intersection is only shown for slice views in the same ViewGroup</p>
</li>
<li>
<p>Improve slice viewer WW/WL and adjustment: if mouse is moved too far into one direction WW/WL values only follow it until they are still in the volume’s range (therefore it is easier to restore the values to a valid range).</p>
</li>
<li>
<p>Auto-select background/foreground volume for W/L change in slice viewer: adjust the WW/WL of the volume visible in the clicked position (if both foreground and background volume is visible then adjust foreground volume’s). Makes it easier to change W/L of the intended volume (no need to swap foreground/background volume, less chance of accidentally modifying another volume)</p>
</li>
</ul>
</li>
<li>
<p>Command Line Module</p>
<ul>
<li>Added CLI output display to module widget: Error are shown automatically in the module GUI, user can slick on expand button (next to the status message) to see detailed log of the execution.</li>
</ul>
</li>
</ul>
</li>
<li>
<p>Fixes / Performances:</p>
<ul>
<li>
<p>Increase overall robustness of the application: Fix heap corruption errors, fix memory leaks, fix MRML node circular references, improve error checking (e.g catch ITK exceptions when unable to read images).</p>
</li>
<li>
<p>Slice viewer:</p>
<ul>
<li>
<p>Improve slice browsing speed when slice annotations shown.</p>
</li>
<li>
<p>Fix incorrect scaling of Dash2D and Cross2D markups.</p>
</li>
<li>
<p>Fix slice spacing computation: When a slice axis is not aligned with a volume axis then slice spacing is computed using elliptical interpolation.</p>
</li>
<li>
<p>Fix slice bounds for volumes not RAS aligned</p>
</li>
<li>
<p>Snap slice views to slice center after rotate to volume plane.</p>
</li>
<li>
<p>Center view button now update clipping planes.</p>
</li>
<li>
<p>Fix handling of annotation 2D coordinates by adding 1 pixel offset in ConvertDeviceToXYZ().</p>
</li>
<li>
<p>Fix setting of slice viewer offset.</p>
</li>
</ul>
</li>
<li>
<p>Colors:</p>
<ul>
<li>Fixed color table editing.</li>
</ul>
</li>
<li>
<p>3D viewer:</p>
<ul>
<li>
<p>Fix picking of markups in 3D view.</p>
</li>
<li>
<p>Exclude crosshair from 3D field of view computation.</p>
</li>
</ul>
</li>
<li>
<p>Reformat:</p>
<ul>
<li>Improve robustness of auto-rotate slice to camera normal.</li>
</ul>
</li>
<li>
<p>Extension Manager:</p>
<ul>
<li>Fix extension manager crash with dark theme.</li>
</ul>
</li>
<li>
<p>DataProbe:</p>
<ul>
<li>Fix DataProbe when slicer starts up with a chart in the layout.</li>
</ul>
</li>
<li>
<p>Environment management:</p>
<ul>
<li>Application environment is now consistently managed across all platforms by reading associated settings from human-readable configuration file. It internally relies on CTKAppLauncher. See <a href="https://github.com/commontk/AppLauncher">https://github.com/commontk/AppLauncher</a>.</li>
</ul>
</li>
<li>
<p>Settings:</p>
<ul>
<li>Remember last selected Additional module path in settings.</li>
</ul>
</li>
<li>
<p>ExtensionWizard:</p>
<ul>
<li>
<p>Support extension without project in toplevel CMakeLists.</p>
</li>
<li>
<p>Support layout with main CMakeLists in subdirectory.</p>
</li>
<li>
<p>Faster “–contribute” avoiding iterate over all user repos.</p>
</li>
<li>
<p>Reject improper module name when adding module.</p>
</li>
<li>
<p>Templates:</p>
<ul>
<li>
<p>Add scripted segment editor effect template</p>
</li>
<li>
<p>Add ScriptedEditorEffect to SlicerGenerateExtensionTemplates target.</p>
</li>
<li>
<p>Add ScriptedSegmentEditorEffect to SlicerGenerateExtensionTemplates target.</p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<h2 id="heading--io">IO</h2>
<ul>
<li>
<p>Features</p>
<ul>
<li>
<p>Support added for read/write of MINC image files.</p>
</li>
<li>
<p>Support loading of regular 4D NRRD file as segmentation.</p>
</li>
<li>
<p>Write coordinate system to model files.</p>
</li>
<li>
<p>Add OBJ file save option for model nodes.</p>
</li>
<li>
<p>Add option to disable automatic opacities when loading segmentation form file.</p>
</li>
<li>
<p>Add option to load terminology json files from GUI.</p>
</li>
<li>
<p>Add show option to Add data dialog for volume loading.</p>
</li>
<li>
<p>Made Add data dialog more keyboard-friendly.</p>
</li>
</ul>
</li>
<li>
<p>Performances:</p>
<ul>
<li>Speed up volume loading by reading scalar range from headerfile.</li>
</ul>
</li>
<li>
<p>Fixes:</p>
<ul>
<li>
<p>Fix NRRD reader for large images.</p>
</li>
<li>
<p>Fix loading of RGB volumes.</p>
</li>
<li>
<p>Fix saving of FreeSurfer model nodes with overlay.</p>
</li>
<li>
<p>Fix loading of FreeSurfer overlays with custom extensions.</p>
</li>
<li>
<p>Fix scene save with images loaded from command-line.</p>
</li>
<li>
<p>More robust DICOM file reading with Add data.</p>
</li>
</ul>
</li>
</ul>
<h2 id="heading--api-updates-and-python-scripting">API updates and Python Scripting</h2>
<ul>
<li>
<p>Features:</p>
<ul>
<li>
<p>Python console</p>
<ul>
<li>
<p>Improve Python console completion:</p>
<ul>
<li>Avoid creation of intermediate variables by evaluating functions.</li>
</ul>
</li>
<li>
<p>Print separator in Python console when a module is reloaded.</p>
</li>
</ul>
</li>
<li>
<p>Add projection option to model slice display:</p>
<ul>
<li>
<p>Models consisting of thin structures (such as catheters, coils, stents), can clearly be visible in slice views, as their intersection with the slice is now the complete object instead of just a few points or small circles.</p>
</li>
<li>
<p>User interface is not yet added for this feature (it would require more experimentation to see how it is the best to expose this option), but can be activated from the Python console for a model node: <code>slicer.util.getNode('MyModel').GetDisplayNode().SetSliceDisplayModeToProjection()</code></p>
</li>
</ul>
</li>
<li>
<p>Settings:</p>
<ul>
<li>Support use of <code>ctkSettings</code> from python.</li>
</ul>
</li>
<li>
<p><code>slicer.util python module</code>:</p>
<ul>
<li>
<p>Add <code>slicer.util.loadUI</code>: Allow to create a widget from a .ui file.</p>
</li>
<li>
<p>Add <code>slicer.util.findChild</code>: Allow quick access to a particular widget by name.</p>
</li>
<li>
<p>Add <code>slicer.util.setSliceViewerLayers</code>: Allow to update all slice views.</p>
</li>
<li>
<p>Add <code>slicer.util.clickAndDrag</code>: Send synthetic mouse events to the specified widget. Useful to write self-tests.</p>
</li>
<li>
<p>Add more numpy array conversions to <code>slicer.util</code> (<code>arrayFromVolume</code>, <code>arrayFromModelPoints</code>, <code>updateVolumeFromArray</code>).</p>
</li>
</ul>
</li>
<li>
<p>Scripted module:</p>
<ul>
<li>
<p>Expose <code>enter()</code> and <code>exit()</code> methods.</p>
</li>
<li>
<p>Add support for <code>cleanup()</code> method.</p>
</li>
<li>
<p>Add Edit button to Reload&amp;test area.</p>
</li>
</ul>
</li>
<li>
<p><code>Slicerrc.py</code></p>
<ul>
<li>
<p>Ensure function defined in <code>.slicerrc.py</code> are available in console.</p>
</li>
<li>
<p>Made slicer startup script more discoverable: Show slicerrc file location in application settings and add a button to open it. If the file does not exist then a default file is created.</p>
</li>
</ul>
</li>
<li>
<p>Python packages</p>
<ul>
<li>
<p>Add couchdb.</p>
</li>
<li>
<p>Add wheel, pip and associated dependencies.</p>
</li>
</ul>
</li>
<li>
<p>DataProbe:</p>
<ul>
<li>Facilitate integration in custom view.</li>
</ul>
</li>
</ul>
</li>
<li>
<p>API updates and fixes:</p>
<ul>
<li>
<p>Markups: Add easy access to node selector in <code>qSlicerSimpleMarkupsWidget</code>.</p>
</li>
<li>
<p>Tables: Add tables logic method for finding layout with table.</p>
</li>
<li>
<p>Application</p>
<ul>
<li>
<p>SlicerApplication: Introduce <code>startupCompleted()</code> signal.</p>
</li>
<li>
<p>SlicerCoreApplication: Introduces <code>isUsingLauncher()</code> function.</p>
</li>
<li>
<p>Environment management: Add support for <code>startupEnvironment()</code>: It allows to get the environment as it was before starting Slicer.</p>
</li>
</ul>
</li>
<li>
<p>Allow disabling slice view interactions</p>
</li>
<li>
<p>Extend <code>vtkTeem</code> API to expose labels and units found in NRRD files.</p>
</li>
<li>
<p>Add orientation normalization utilities to <code>vtkAddon</code>.</p>
</li>
<li>
<p>SimpleITK: More robust API for the <code>sitkUtils</code> python module provided by Slicer.</p>
</li>
<li>
<p>Fix issue with <code>qMRMLNodeComboBox</code> when removing an attribute filter.</p>
</li>
<li>
<p>Add optional checkable column in <code>qMRMLColorModel</code>.</p>
</li>
<li>
<p>Add <code>vtkMRMLSliceLogic::SetForegroundWindowLevel</code>.</p>
</li>
<li>
<p>Segmentations:</p>
<ul>
<li>
<p>Add convenience function in <code>vtkSegmentation</code> to get segment by name.</p>
</li>
<li>
<p>Allow restricting Segment editor to certain views:</p>
<ul>
<li>
<p>Previously, Segment Editor allowed editing in all views, even where the Segmentation node was not displayed. Now editing is only allowed in view nodes where the Segmentation node is displayable.</p>
</li>
<li>
<p>It is now also possible to disable automatic display of the master volume node when switching between segmentation nodes or master volumes. This allows more refined control of segment editor when it is embedded into another module.</p>
</li>
</ul>
</li>
<li>
<p>Set <code>autoShowMasterVolumeNode</code> property of qMRMLSegmentEditorWidget to false to prevent automatic showing of master volume.</p>
</li>
</ul>
</li>
<li>
<p>Transform:</p>
<ul>
<li>
<p>Add <code>GetNodeBounds</code> to return untransformed bounds of node.</p>
</li>
<li>
<p>Add static method to get all nodes transformed by a transform node.</p>
</li>
<li>
<p>Fix <code>vtkOrientedImageData::GetExtent</code>.</p>
</li>
</ul>
</li>
<li>
<p>Volumes:</p>
<ul>
<li>Add <code>vtkSlicerVolumesLogic::CloneVolumeGeneric</code> cloning any volume.</li>
</ul>
</li>
<li>
<p>CLI</p>
<ul>
<li>
<p>Set CLI widget objectName based on parameter name</p>
</li>
<li>
<p>Add <code>AllowInMemoryTransfer</code> CLI setting</p>
</li>
</ul>
</li>
<li>
<p>Functions wrapped in python:</p>
<ul>
<li>
<p><code>qSlicerTerminologyNavigatorWidget::recommendedColorFromTerminology</code>.</p>
</li>
<li>
<p><code>vtkMRMLNode::GetAttributeNames</code>.</p>
</li>
<li>
<p>Made segment labelmap export available from Python.</p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<h2 id="heading--build-system-continuous-integration-software-process-release-process">Build System, Continuous Integration, Software Process, Release Process</h2>
<ul>
<li>
<p>Continuous Integration (CI) and Dashboards:</p>
<ul>
<li>
<p>Do not clean directory for continuous dashboard builds, make continuous build more configurable.</p>
</li>
<li>
<p>Use ExternalData_OBJECT_STORES from environment as default</p>
</li>
</ul>
</li>
<li>
<p>Slicer Build System:</p>
<ul>
<li>
<p>Update build system to support building against VTK8, Qt5 with C++11 enabled.</p>
</li>
<li>
<p>Add support for VS2015.</p>
</li>
<li>
<p>Improve support for parallel build and installation of python packages fixing race condition.</p>
</li>
<li>
<p>Introduce SlicerPatch.cmake allowing to apply patch only once. Also add FindPatch CMake module.</p>
</li>
<li>
<p>Packaging:</p>
<ul>
<li>
<p>Fix extension packaging setting CMAKE_MACOSX_RPATH to 0 (see <a href="https://github.com/Slicer/Slicer/commit/f332fc2">Slicer/Slicer@f332fc2</a>).</p>
</li>
<li>
<p>Fix list of Qt plugins to install on macOS.</p>
</li>
</ul>
</li>
<li>
<p>Support custom GIT tag and repository URL for all Slicer external projects.</p>
</li>
<li>
<p>Check required python package availability when building against system python.</p>
</li>
<li>
<p>Add external project step allowing to keep track of project version: This generate a project description file named ‘version-.txt’ containing one line of the form ’ '.</p>
</li>
</ul>
</li>
<li>
<p>Release process:</p>
<ul>
<li>
<p>Add python cli automating versioning of Slicer wiki documentation.</p>
</li>
<li>
<p>release/midasdata: Re-use destination folder if it already exists</p>
</li>
</ul>
</li>
<li>
<p>Testing</p>
<ul>
<li>ScriptedModuleDiscoveryTest: Skip test using test output on windows (see <a href="https://github.com/Slicer/Slicer/commit/3a553f6">Slicer/Slicer@3a553f6</a>).</li>
</ul>
</li>
<li>
<p>Extension build system:</p>
<ul>
<li>
<p>Report extension source checkout error.</p>
</li>
<li>
<p>Update SlicerConfig to include path to Git and Svn. Allow to build extension simply passing -DSlicer_DIR.</p>
</li>
<li>
<p>Generate (Extension)Config.cmake: Allow an extension import targets from another extension.</p>
</li>
<li>
<p>Add PYTHON_SITE_PACKAGES_SUBDIR to launcher settings (see <a href="https://github.com/Slicer/Slicer/commit/7b5ee46">Slicer/Slicer@7b5ee46</a>).</p>
</li>
<li>
<p>Add Slicer_THIRDPARTY_* vars to launcher settings (see <a href="https://github.com/Slicer/Slicer/commit/58275e6">Slicer/Slicer@58275e6</a>).</p>
</li>
<li>
<p>Introduce PYTHON_STDLIB_SUBDIR and PYTHON_SITE_PACKAGES_SUBDIR CMake vars (see <a href="https://github.com/Slicer/Slicer/commit/bc95187">Slicer/Slicer@bc95187</a>).</p>
</li>
</ul>
</li>
</ul>
<h2 id="heading--modules">Modules</h2>
<h3 id="heading--segmentations">Segmentations</h3>
<ul>
<li>
<p>New effects:</p>
<ul>
<li>
<p>Grow from seeds: Creates a complete segmentation from a few seeds, painted by the user inside each structure. Seeds can be interactively modified and updated segmentation is displayed within seconds. It is a greatly improved version of “Fast growcut” effect found in earlier Slicer versions.</p>
</li>
<li>
<p>Fill between slices: it is not necessary to contour on all slices, user can skip slices and this effect fills the missing contours by interpolation (previously was partly available in Smoothing effect).</p>
</li>
<li>
<p>Scissors effect: cut depth on slice view can be restricted (to behind or in front of the current slice, or around the current slice). Details:<a href="https://www.researchgate.net/deref/https%3A%2F%2Fdiscourse.slicer.org%2Ft%2Fscissors-on-range-of-slices%2F360"> </a><a href="https://discourse.slicer.org/t/scissors-on-range-of-slices/360">https://discourse.slicer.org/t/scissors-on-range-of-slices/360</a></p>
</li>
<li>
<p>Surface cut (in SegmentEditorExtraEffects extension): is for creating segments by clicking at the boundary of a structure on a few image slices. Similar to VolumeClip extension’s Clip volume with model module.</p>
</li>
<li>
<p>Mask volume (in SegmentEditorExtraEffects extension): is for quick blanking of areas of volumes for volume rendering, registration mask generation, etc. Details: <a href="https://discourse.slicer.org/t/new-segment-editor-effects-mask-volume-and-surface-cut/699/2">https://discourse.slicer.org/t/new-segment-editor-effects-mask-volume-and-surface-cut/699/2</a></p>
</li>
<li>
<p>Watershed (in SegmentEditorExtraEffects extension): similar to grow from seeds. Advantage: smoothness of the segments can be enforced. Disadvantage: much slower. Details: <a href="https://discourse.slicer.org/t/watershed-fast-marching-and-flood-filling-effects-in-segment-editor/104">https://discourse.slicer.org/t/watershed-fast-marching-and-flood-filling-effects-in-segment-editor/104</a></p>
</li>
<li>
<p>Fast marching (in SegmentEditorExtraEffects extension): expands the current segment to regions with similar intensity. Improved version of FastMarching effect in earlier Slicer versions. Details: <a href="https://discourse.slicer.org/t/watershed-fast-marching-and-flood-filling-effects-in-segment-editor/104">https://discourse.slicer.org/t/watershed-fast-marching-and-flood-filling-effects-in-segment-editor/104</a></p>
</li>
<li>
<p>Flood filling (in SegmentEditorExtraEffects extension): clicking in the image adds points around the click position to the current segment. Intensity tolerance is adjustable. Neighborhood size parameter can be used to prevent leakage. Details: <a href="https://discourse.slicer.org/t/watershed-fast-marching-and-flood-filling-effects-in-segment-editor/104">https://discourse.slicer.org/t/watershed-fast-marching-and-flood-filling-effects-in-segment-editor/104</a></p>
</li>
</ul>
</li>
<li>
<p>Segment statistics module (in Quantification category): Surfaces and volumes of segmented structures can be directly computed from Segmentation nodes (there is no need to export to model or labelmap nodes anymore).</p>
<ul>
<li>
<p>Results are stored in a table, which can be saved as csv file or copied to Excel for analysis. Demo: <a href="https://youtu.be/fM_rxfDTRi0">https://youtu.be/fM_rxfDTRi0</a></p>
</li>
<li>
<p>Developers can add custom plugins that can compute additional metrics and statistics</p>
</li>
<li>
<p>Uses units and standard terminologies to create measurements that can be exported in standard DICOM format (see Quantitative Reporting extension)</p>
</li>
</ul>
</li>
<li>
<p>Segment content can be described using standard DICOM terminology. The information is used for creating quantitative reports using Segment Statistics module. Terminology information is included when Segmentation is loaded from DICOM segmentation object (see Quantitative Reporting extension).</p>
</li>
<li>
<p>Support fractional labelmaps</p>
<ul>
<li>
<p>New non-binary labelmap representation in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations">segmentations infrastructure</a>: conversion from/to closed surface</p>
</li>
<li>
<p>Useful for representing partial voxel occupancy (finer structure details in the same amount of memory), or probabilistic maps (multi-atlas segmentations)</p>
</li>
<li>
<p>Two visualization types: 1) Threshold-based hard edges for partial voxel representation, 2) Opacity-based for probabilistic representation. See Figures 3.6 and 3.7 in <a href="http://qspace.library.queensu.ca/bitstream/handle/1974/22677/Sunderland_Kyle_R_201709_MSC.pdf">K. Sunderland’s MSc thesis</a></p>
</li>
<li>
<p>Updated Segment Editor effects to support fractional labelmaps if it is the master representation of the edited segmentation</p>
</li>
</ul>
</li>
<li>
<p>Additional improvements</p>
<ul>
<li>
<p>Reference geometry can be specified for labelmap export: it allows the merged labelmap geometry to exactly match the geometry of the input (or any other) volume.</p>
</li>
<li>
<p>Paint brush size can be fixed in screen coordinates. This way when the user zooms in the view, the brush absolute size decreases, allowing editing of finer details.</p>
</li>
<li>
<p>New shortcuts for many actions: see details in <a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html#keyboard-shortcuts">documentation</a>.</p>
</li>
<li>
<p>Simplified user interface, made it easier to switch between Segmentations and Segment editor modules</p>
</li>
<li>
<p>Add ‘Crop to reference image geometry’ segmentation conversion option to allow clipping of large imported models on import.</p>
</li>
</ul>
</li>
<li>
<p>Performance and Fixes</p>
<ul>
<li>
<p>Improve support of transformed segments.</p>
</li>
<li>
<p>Improve performance when show/hide segment.</p>
</li>
<li>
<p>Improve segment editor initialization speed.</p>
</li>
<li>
<p>Reduce memory footprint and improve performance of effects.</p>
</li>
<li>
<p>Fix display of labelmaps exported from segmentation.</p>
</li>
<li>
<p>Fix segment opacity auto calculation.</p>
</li>
<li>
<p>Fix segmentation controller slice view widget.</p>
</li>
<li>
<p>Deactivate segment editor effect if markups placement mode is activated.</p>
</li>
<li>
<p>Do not reset slice FOV on layout switch in Segment editor.</p>
</li>
<li>
<p>Fix bounds computation in vtkMRMLVolumeNode and vtkMRMLSegmentationNode: When volume or segmentation was empty sometimes non-empty bounds were returned.</p>
</li>
<li>
<p>Fix background volume switch on Segment Editor module entering: As a side effect of hiding labelmap layer, the last propagated background volume got re-displayed.</p>
</li>
</ul>
</li>
<li>
<p>API / Developer</p>
<ul>
<li>
<p>Improve segment editor widget API.</p>
</li>
<li>
<p>Fix loading of segment editor effects from extensions.</p>
</li>
<li>
<p>Made segment editor effects list customizable.</p>
</li>
<li>
<p>Allow exporting segments to transformed labelmap node.</p>
</li>
<li>
<p>Always export to models under the same transforms as segmentation.</p>
</li>
<li>
<p>Deterministically order segments and support a segment index.</p>
</li>
<li>
<p>Add option to hide segments from segments table.</p>
</li>
</ul>
</li>
</ul>
<h3 id="heading--volumes">Volumes</h3>
<ul>
<li>
<p>Features:</p>
<ul>
<li>
<p>Add labelmap-&gt;scalar conversion.</p>
</li>
<li>
<p>Add lock window/level button.</p>
</li>
<li>
<p>Apply bimodal analysis to float and long volumes for auto-W/L.</p>
</li>
</ul>
</li>
</ul>
<h3 id="heading--sceneviews">SceneViews</h3>
<ul>
<li>Fix scene view thumbnail display.</li>
</ul>
<h3 id="heading--dicom">DICOM</h3>
<ul>
<li>
<p>Features / Fixes / Performances:</p>
<ul>
<li>
<p>Speedup DICOM import by factor x10.</p>
</li>
<li>
<p>Improved robustness of DICOM image loading: user can now choose between GDCM and DCMTK toolkits.</p>
</li>
<li>
<p>Support selecting a subset of DICOM directories.</p>
</li>
<li>
<p>Add more rules to DICOM patcher module.</p>
</li>
<li>
<p>Add advisor for dicom extensions: After an import to the DICOM database the contents are checked against a pre-configured file that suggests possible extensions.</p>
</li>
<li>
<p>Add option to disable DICOM reference check.</p>
</li>
<li>
<p>Add saving of DICOM scalar volume voxel quantity&amp;unit in volume node.</p>
</li>
<li>
<p>Ensure precache tags are configured with or without mainwindow.</p>
</li>
<li>
<p>Fix slow display of DICOM metadata widget.</p>
</li>
<li>
<p>Fix loading of DICOM series using quasi-matching filename.</p>
</li>
<li>
<p>Update window/level presets in Volumes based on DICOM metadata.</p>
</li>
</ul>
</li>
<li>
<p>API</p>
<ul>
<li>Add function to easily load lists of series by UID without having to manually create a dicomWidget object.</li>
</ul>
</li>
</ul>
<h3 id="heading--cropvolume">CropVolume</h3>
<p>Crop Volume module is an essential pre-processing tool for segmentation. Either for reducing size of large volumes (cropping/downsampling) or allowing better segmentation of structures that are comparable to the voxel size (cropping/upsampling)</p>
<ul>
<li>
<p>Features / Fixes:</p>
<ul>
<li>
<p>Fill value is now configurable.</p>
</li>
<li>
<p>Interpolated cropping allows linear transforms of any volumes or ROIs, input volume can even be non-linearly transformed:</p>
<ul>
<li>Cropping of transformed or non-axis aligned volumes and ROIs was very limited (input volume was not allowed to be transformed, non-linear transforms were not allowed).</li>
</ul>
</li>
<li>
<p>No output volume was selectable (this was unlike all other modules in Slicer and it often lead to creating several unneeded output volumes when experimenting with cropping parameters) -Nnow output volume can be specified (if not specified then it is created automatically)</p>
</li>
<li>
<p>When there is any inconsistency, an error message is displayed and Apply button is disabled; the user can either resolve inconsistencies by selecting different nodes, changing transforms, or clicking the Fix button to automatically resolve all inconsistencies by changing/aligning transforms:</p>
<ul>
<li>If inconsistency was found (e.g., misaligned ROI and input volume for voxel-based cropping) then a popup was displayed and users’ node selections were reverted, which often disrupted user’s workflow (for example, it was not possible to switch input volume and then switch to corresponding ROI because after switching input volume there was a temporary inconsistency that the module wanted to resolve immediately).</li>
</ul>
</li>
<li>
<p>A ROI auto-fit button is available:</p>
<ul>
<li>It was tedious to initialize ROI to include the entire volume (e.g., when the goal was to decrease resolution or crop only on one side).</li>
</ul>
</li>
<li>
<p>In the Volume information section users can immediately see what the size and resolution of the cropped volume will be:</p>
<ul>
<li>Meaning of “Input spacing scaling constant” parameter was not clear (is it an absolute spacing value or a factor relative to current spacing; what value increases/decreases the resolution) and it was often difficult to predict how large the cropped output volume will be without actually performing the cropping.</li>
</ul>
</li>
<li>
<p>Axes between input and output volumes are now correctly matched:</p>
<ul>
<li>Spacing was not computed correctly for volumes where the order of axes were permuted (for example in MRHead sample).</li>
</ul>
</li>
</ul>
</li>
<li>
<p>Performances:</p>
<ul>
<li>Avoid unnecessary images creation: Cropping of large volumes required lots of memory (voxel-based cropping created extra unnecessary temporary vtkImageData objects; interpolated cropping created an unnecessary reference volume, instead of just specifying output volume geometry using CLI arguments).</li>
</ul>
</li>
</ul>
<h3 id="heading--endoscope">Endoscope</h3>
<ul>
<li>
<p>Features</p>
<ul>
<li>Add endoscope orientation computation: It is now possible to show a tool (not just a fiducial point) or reslice the volume using VolumeResliceDriver at the endoscope tip position.</li>
</ul>
</li>
</ul>
<h3 id="heading--openigtlink">OpenIGTLink</h3>
<ul>
<li>
<p>Features</p>
<ul>
<li>Add support for processing RGB image.</li>
</ul>
</li>
<li>
<p>Fixes</p>
<ul>
<li>
<p>Fix crash when sending node via OpenIGTLink.</p>
</li>
<li>
<p>Fix command handling.</p>
</li>
</ul>
</li>
<li>
<p>Use cases</p>
<ul>
<li>3D object tracking using your webcam and 2D barcodes: You can now move objects in 3D Slicer by printing and sticking 2D barcodes to objects and putting them in front of your web camera. There are more serious applications, in surgical training, simulation, and potentially even in some clinical procedures. - <a href="https://discourse.slicer.org/t/webcam-based-marker-tracking-is-available-in-slicer-now/565/3">https://discourse.slicer.org/t/webcam-based-marker-tracking-is-available-in-slicer-now/565/3</a>
</li>
</ul>
</li>
</ul>
<h3 id="heading--tables">Tables</h3>
<ul>
<li>Table column properties: customize table properties (description, data type, unit, etc). It is used for customizing appearance and behavior and can be used by modules to associate any kind of metadata with a table column. Column properties are stored in a schema file (csv format). Details:<a href="https://www.researchgate.net/deref/https%3A%2F%2Fdiscourse.slicer.org%2Ft%2Ftable-columns-customization%2F436"> </a><a href="https://discourse.slicer.org/t/table-columns-customization/436">https://discourse.slicer.org/t/table-columns-customization/436</a>
</li>
</ul>
<h3 id="heading--surfacetoolbox">SurfaceToolbox</h3>
<ul>
<li>
<p>Features:</p>
<ul>
<li>Add mirror and normals auto-orientation</li>
</ul>
</li>
</ul>
<h3 id="heading--transform">Transform</h3>
<ul>
<li>
<p>Features</p>
<ul>
<li>
<p>Add support for interactively updating transform in the 3D view.</p>
</li>
<li>
<p>Transforms module in 3D Slicer now allows visualization of displacements of individual points. This can be used for exploring and visualizing registration results or displaying where planned target points move. See a short demo video here: <a href="https://youtu.be/CTLcYrtmoNo">https://youtu.be/CTLcYrtmoNo</a></p>
</li>
</ul>
</li>
<li>
<p>Fixes</p>
<ul>
<li>
<p>Convert empty VTK transform to identity ITK transform.</p>
</li>
<li>
<p>Prevent ITK from crashing after reading TPS transform.</p>
</li>
<li>
<p>Fix ITK transform conversion crash.</p>
</li>
<li>
<p>Fix warping of markup fiducial labels.</p>
</li>
<li>
<p>Reset transform sliders when switching between transforms.</p>
</li>
<li>
<p>Fix ResampleDTIVolume to work with composite transforms.</p>
</li>
<li>
<p>Fix transform rotation spinbox in Transforms module.</p>
</li>
<li>
<p>Fix annotation ROI transform hardening.</p>
</li>
<li>
<p>Do not report error messages when testing if NRRD is tensor file.</p>
</li>
</ul>
</li>
</ul>
<h3 id="heading--sampledata">SampleData</h3>
<ul>
<li>
<p>Features:</p>
<ul>
<li>
<p>Display thumbnails in SampleData module.</p>
</li>
<li>
<p>Make it easier to register custom sample data.</p>
</li>
<li>
<p>Improve name of Panoramix dataset and acknowledge “Osirix DICOM image library”.</p>
</li>
</ul>
</li>
</ul>
<h3 id="heading--data">Data</h3>
<p>The Data module acts as a central data-organizing point in Slicer.</p>
<ul>
<li>
<p>Integrate Subject Hierarchy module into Data module.</p>
</li>
<li>
<p>Provide three views:</p>
<ul>
<li>
<p>Subject hierarchy view</p>
<ul>
<li>
<p>Overview all loaded data objects in the same place, types indicated by icons.</p>
</li>
<li>
<p>Organize data in folders or patient/subject trees.</p>
</li>
<li>
<p>Visualize and bulk-handle lots of data nodes loaded from disk.</p>
</li>
<li>
<p>Easy show/hide of branches of displayable data.</p>
</li>
<li>
<p>Transform whole study (any branch).</p>
</li>
<li>
<p>Export DICOM data (edit DICOM tags).</p>
</li>
<li>
<p>Lots of type-specific functionality offered by the plugins.</p>
</li>
</ul>
</li>
<li>
<p>Transform hierarchy view</p>
<ul>
<li>Manage transformation chains/hierarchies.</li>
</ul>
</li>
<li>
<p>All nodes view</p>
<ul>
<li>Developer tool for debugging problems.</li>
</ul>
</li>
<li>
<p>Removed the Displayable view (Subject hierarchy can do the same and much more).</p>
</li>
</ul>
</li>
</ul>
<h3 id="heading--volumerendering">VolumeRendering</h3>
<ul>
<li>
<p>Features:</p>
<ul>
<li>
<p>Support ROI clipping in arbitrary direction.</p>
</li>
<li>
<p>Allow finer volume rendering offset adjustment.</p>
</li>
<li>
<p>Enable setting GPU memory larger than 4GB.</p>
</li>
</ul>
</li>
</ul>
<h3 id="heading--terminology-new-module">Terminology (New module)</h3>
<p>This new module supports definition of semantic meanings of structures represented in Slicer using terminologies from DICOM, SNOMED, and related standards. The new module includes widgets for easily finding meaningful terms and associating them with colors.  This is built on concepts from the older Colors module and is designed to support DICOM SEG objects:</p>
<ul>
<li>
<p>Add Generic Anatomy Colors.</p>
</li>
<li>
<p>Add option to load custom anatomical contexts for terminologies.</p>
</li>
<li>
<p>Use new vtkCodedEntry class as base class for terminology containers.</p>
</li>
<li>
<p>Add support for DICOMSegmentationPlugin from Quantitative Reporting extension by adding capability to load anatomical context from DICOM SEG descriptor.</p>
</li>
</ul>
<h3 id="heading--screencapture">ScreenCapture</h3>
<ul>
<li>
<p>Features:</p>
<ul>
<li>
<p>Add support for capturing a single image of the current state.</p>
</li>
<li>
<p>Add option for capturing all views.</p>
</li>
<li>
<p>Add setting for configuring the rotation axis.</p>
</li>
<li>
<p>Capturing can now be cancelled.</p>
</li>
</ul>
</li>
<li>
<p>Fixes:</p>
<ul>
<li>Hide all 3D view controller bars in “Capture all views” mode.</li>
</ul>
</li>
</ul>
<h2 id="heading--extensions">Extensions</h2>
<h3 id="heading--new">New</h3>
<ul>
<li>
<p>BoneTextureExtension: presents texture quantification algorithms that provide a statistical description of the local texture of a 2D, 3D or N-D image.  The N-Dimensional texture maps are generated with a high performance algorithm andmulti-threaded implementation in the <a href="https://itk.org/">Insight Toolkit (ITK)</a>. These algorithms are used to characterize subchondral bone texture in <a href="https://en.wikipedia.org/wiki/Temporomandibular_joint">temporomandibular joint</a> (TMJ) <a href="http://www.arthritis.org/about-arthritis/types/osteoarthritis/">osteoarthritis</a> (OA). Bone is well characterized by these filters due to the rich textures present in the trabecular bone (low density bone). See <a href="https://blog.kitware.com/fast-n-dimensional-texture-feature-maps/">https://blog.kitware.com/fast-n-dimensional-texture-feature-maps/</a></p>
</li>
<li>
<p>SegmentEditorExtraEffects: Experimental effects for Segment Editor in 3D Slicer.</p>
</li>
<li>
<p>Sequence registration: This extension registers a sequence of volumes (3D+t a.k.a. 4D image data) to a selected volume. Processing results is a transform sequence (3D displacement field changing in time) and motion-compensated volume sequence. The transform sequence can be used for deforming point targets or structures. Applications include motion-compensation for volume comparison and analysis of organ motion.</p>
</li>
<li>
<p>SlicerElastix: This extension makes available Elastix medical image registration toolkit (<a href="http://elastix.isi.uu.nl/">http://elastix.isi.uu.nl/</a>) available in Slicer.</p>
</li>
<li>
<p>SlicerITKUltrasound: This extension provides ultrasound image scan conversion of B-mode and next-generation ultrasound imaging modalities. Interfaces are built off the <a href="https://github.com/KitwareMedical/ITKUltrasound/">ITKUltrasound</a> library. The modules available in this extension are useful for both 2D and 3D image generation for traditional B-mode imaging, but also next-generation ultrasound image modalities like ultrasound spectroscopy, acoustic radiation force imaging (ARFI), acoustic radiation force shear wave imaging (ARFI-SWEI), and others. See <a href="https://blog.kitware.com/3d-slicer-resamples-ultrasound-images/">https://blog.kitware.com/3d-slicer-resamples-ultrasound-images/</a></p>
</li>
<li>
<p>Radiomics: This extension provides the interface to the pyradiomics library (<a href="http://pyradiomics.readthedocs.io/en/latest/">http://pyradiomics.readthedocs.io/en/latest/</a>) that can be used to calculate over 1500 radiomics features from an image region defined by a segmentation.</p>
</li>
</ul>
<h3 id="heading--improved">Improved</h3>
<ul>
<li>
<p>SlicerRT</p>
<ul>
<li>
<p>Stable release of External Beam Planning module</p>
</li>
<li>
<p>Fractional labelmap support</p>
</li>
<li>
<p>New Room’s Eye View module</p>
</li>
<li>
<p>Fix bug where Hausdorff Distance 95% and Avg Dist were computed incorrectly</p>
</li>
<li>
<p>Improve dose visualization using isodose color table</p>
</li>
<li>
<p>Improve DVH layouts</p>
</li>
<li>
<p>DICOM improvements</p>
</li>
</ul>
</li>
<li>
<p>VMTK</p>
</li>
<li>
<p>DCMQI</p>
</li>
<li>
<p>QuantitativeReporting</p>
</li>
<li>
<p>SliceTracker</p>
</li>
<li>
<p>SlicerDMRI</p>
<ul>
<li>
<p>More fiber measurement statistics</p>
</li>
<li>
<p>Improved UKFTractography masking</p>
</li>
<li>
<p>UKFTractography included with SlicerDMRI</p>
</li>
<li>
<p>Improved NIfTI support in DWIConvert (thanks BRAINS team)</p>
</li>
<li>
<p>Improved integration with new Data module (thanks <a class="mention" href="/u/cpinter">@cpinter</a>)</p>
</li>
</ul>
</li>
</ul>

---
