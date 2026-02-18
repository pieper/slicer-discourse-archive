# Slicer 5.4: Summary and Changelog

**Topic ID**: 40136
**Date**: 2024-11-11
**URL**: https://discourse.slicer.org/t/slicer-5-4-summary-and-changelog/40136

---

## Post #1 by @jcfr (2024-11-11 23:23 UTC)

<h1><a name="p-119341-table-of-content-1" class="anchor" href="#p-119341-table-of-content-1" aria-label="Heading link"></a>Table of content</h1>
<ul>
<li><a href="#heading--summary">Summary</a></li>
<li><a href="https://discourse.slicer.org/t/slicer-5-4-summary-and-changelog/40136/2">Detailed Changlog</a></li>
</ul>
<h1 id="heading--summary">Summary</h1>
<p>The community of 3D Slicer developers is pleased to share the announcement of version 5.4, originally released last year.</p>
<p>3D Slicer 5.4 built on the success of previous versions, which have collectively seen over 1.4 million downloads of the core application and 6.8 million downloads of extensions over the past decade</p>
<p>The development of 3D Slicer—including its numerous modules, extensions, datasets, pull requests, patches, issues reports, suggestions—is made possible by users, developers, contributors and commercial partners around the world. 3D Slicer is based on a stack of open-source software and we are working constantly on updating the underlying packages. This development is funded by various grants and agencies. For more details, please see the 3D Slicer <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#acknowledgments">Acknowledgments</a> page.</p>
<p>Feel free to share your insights on <a href="https://discourse.slicer.org/">Discourse</a> and explore our <a href="https://slicer.readthedocs.io/en/latest/developer_guide/contributing.html">contributing guidelines</a>. If you need help using Slicer, want to report a problem, request a feature, or share how Slicer has contributed to your work, visit our <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html">Get Help</a> section.</p>
<p><a href="https://www.slicer.org/">slicer.org</a> serves as the central hub for the application, training materials, and the development community, offering a series of tutorials and data sets through the <a href="https://slicer.readthedocs.io/en/5.4/user_guide/getting_started.html#tutorials">Slicer Tutorials</a> page.</p>
<p><em>Please note that Slicer continues to be a research package and is not intended for clinical use (clinical users must obtain the necessary ethics or regulatory approvals).</em></p>
<p><em>This version was released on August 19th, 2023, and the associated git tag is <a href="https://github.com/Slicer/Slicer/tree/v5.4.0">v5.4.0</a>. Information about previous releases can be found on the <a href="https://github.com/Slicer/Slicer/wiki/Release-Details">Release Details</a> page.</em></p>

---

## Post #2 by @jcfr (2024-11-11 23:23 UTC)

<h1 id="heading--changelog">Changelog</h1>
<ul>
<li><a href="#heading--core">Core</a>
<ul>
<li><a href="#heading--rendering-display">Rendering &amp; Display</a></li>
<li><a href="#heading--application">Application</a></li>
<li><a href="#heading--io">IO</a></li>
<li><a href="#heading--extension">Extension</a></li>
<li><a href="#heading--scripting">Scripting</a></li>
<li><a href="#heading--internationalization-localization">Internationalization/Localization</a></li>
</ul>
</li>
<li><a href="#heading--improved-modules">Improved Modules</a>
<ul>
<li><a href="#heading--dicom">DICOM</a></li>
<li><a href="#heading--markups">Markups</a></li>
<li><a href="#heading--models">Models</a></li>
<li><a href="#heading--sample-data">Sample Data</a></li>
<li><a href="#heading--sequences">Sequences</a></li>
<li><a href="#heading--segmentation">Segmentation</a></li>
<li><a href="#heading--subject-hierarchy">Subject Hierarchy</a></li>
<li><a href="#heading--surfacetoolbox">SurfaceToolbox</a></li>
<li><a href="#heading--tables">Tables</a></li>
<li><a href="#heading--terminologies">Terminologies</a></li>
<li><a href="#heading--volume-rendering">Volume Rendering</a></li>
<li><a href="#heading--webserver">WebServer</a></li>
</ul>
</li>
<li><a href="#heading--removed-modules">Removed Modules</a></li>
<li><a href="#heading--infrastructure">Infrastructure</a>
<ul>
<li><a href="#heading--packaging">Packaging</a></li>
<li><a href="#heading--testing">Testing</a></li>
<li><a href="#heading--continuous-integration-ci">Continuous Integration (CI)</a></li>
<li><a href="#heading--build-system">Build-System</a></li>
<li><a href="#heading--dependencies">Dependencies</a></li>
<li><a href="#heading--documentation">Documentation</a></li>
</ul>
</li>
</ul>
<h2 id="heading--core">Core</h2>
<h3 id="heading--rendering-display">Rendering &amp; Display</h3>
<ul>
<li>Implement multi-monitor layout (<a href="https://github.com/Slicer/Slicer/pull/6776">PR-6776</a>)</li>
<li>Add option for displaying vertical slice controller (<a href="https://github.com/Slicer/Slicer/pull/6712">PR-6712</a>)</li>
<li>Enable “Pickable” segment display property to allow disabling point picking (<a href="https://github.com/Slicer/Slicer/pull/6984">PR-6984</a>)</li>
<li>Introduce fractional addition to Add/Subtract Slice Compositing pipeline (<a href="https://github.com/Slicer/Slicer/pull/7002">PR-7002</a>)</li>
<li>Add flip and rotate buttons to Reformat module (<a href="https://github.com/Slicer/Slicer/pull/7078">PR-7078</a>)</li>
<li>Update Slicer Controller with Thick Slab Reconstruction option (<a href="https://github.com/Slicer/Slicer/pull/7021">PR-7021</a>)</li>
<li>Initialize global pause render state for newly created views (<a href="https://github.com/Slicer/Slicer/pull/6947">PR-6947</a>)</li>
<li>Display slab reconstruction thickness in slice view corner (<a href="https://github.com/Slicer/Slicer/pull/7177">PR-7177</a>)</li>
<li>Use column name as plot title when unspecified (<a href="https://github.com/Slicer/Slicer/pull/6682">PR-6682</a>)</li>
<li>Improve Volumes module display options and fix related issues (<a href="https://github.com/Slicer/Slicer/pull/6758">PR-6758</a>)</li>
<li>Add “Refocus camera” action to view context menu (<a href="https://github.com/Slicer/Slicer/pull/6916">PR-6916</a>)</li>
<li>Add alternative shortcut for view pan-zoom-rotate (<a href="https://github.com/Slicer/Slicer/pull/6916">PR-6916</a>)</li>
<li>Update crosshair cursor position on 3D view mouse move events (<a href="https://github.com/Slicer/Slicer/pull/6937">PR-6937</a>)</li>
<li>Fix issue allowing more than one rotation slider to be non-zero (<a href="https://github.com/Slicer/Slicer/pull/6759">PR-6759</a>)</li>
<li>Fix computation of offset direction label in slice view controller (<a href="https://github.com/Slicer/Slicer/pull/6781">PR-6781</a>)</li>
<li>Fix warning when changing window/level with mouse mode (<a href="https://github.com/Slicer/Slicer/pull/6897">PR-6897</a>)</li>
<li>Fix inability to change foreground volume window level with mouse mode (<a href="https://github.com/Slicer/Slicer/pull/6924">PR-6924</a>)</li>
<li>Fix dynamic update of transform visualization (<a href="https://github.com/Slicer/Slicer/pull/6956">PR-6956</a>)</li>
<li>Fix interaction handle visibility when changing displayed slice (<a href="https://github.com/Slicer/Slicer/pull/6992">PR-6992</a>)</li>
<li>Fix inability to change foreground W/L with mouse mode (<a href="https://github.com/Slicer/Slicer/pull/6996">PR-6996</a>)</li>
<li>Fix small shift in slice image in 3D views (<a href="https://github.com/Slicer/Slicer/pull/6959">MR-6959</a>)</li>
<li>Fix “Restore view layout” action in view context menu (<a href="https://github.com/Slicer/Slicer/pull/7097">PR-7097</a>)</li>
<li>Fix potential segfault during initialization of <code>qMRMLSliceWidget</code> (<a href="https://github.com/Slicer/Slicer/pull/7115">PR-7115</a>)</li>
<li>Fix color legend visibility on non-standard slice views (<a href="https://github.com/Slicer/Slicer/pull/6836">PR-6836</a>)</li>
<li>Fix display issues with “Model,” “plane markups,” and “segmentation closed surface” slice intersections (<a href="https://github.com/Slicer/Slicer/pull/7102">PR-7102</a>)</li>
</ul>
<h3 id="heading--application">Application</h3>
<ul>
<li>Enlarge error report box (<a href="https://github.com/Slicer/Slicer/pull/6769">PR-6769</a>)</li>
<li>Make ctk ErrorLogWidget dockable (<a href="https://github.com/Slicer/Slicer/pull/7059">PR-7059</a>)</li>
<li>Avoid superfluous error message (<a href="https://github.com/Slicer/Slicer/pull/6952">PR-6952</a>)</li>
<li>Enable saving and restoring SliceViewAnnotations display level (<a href="https://github.com/Slicer/Slicer/pull/7175">PR-7175</a>)</li>
<li>Re-export selected PNGs to fix “libpng warning: iCCP: CRC error” (<a href="https://github.com/Slicer/Slicer/pull/6807">PR-6807</a>)</li>
<li>Improve rendering of SaveDataDialog checkboxes in Dark Mode (<a href="https://github.com/Slicer/Slicer/pull/7098">PR-7098</a>)</li>
<li>Enhance Python scripted module detection for drag-and-drop (<a href="https://github.com/Slicer/Slicer/pull/6959">MR-6959</a>)</li>
<li>Synchronize DataProbe UI initialization and “Restore Defaults” action (<a href="https://github.com/Slicer/Slicer/pull/7174">PR-7174</a>)</li>
<li>Improve module finder filtering (<a href="https://github.com/Slicer/Slicer/pull/6844">PR-6844</a>)</li>
<li>Support import type annotation from Slicer during module load (<a href="https://github.com/Slicer/Slicer/pull/6847">PR-6847</a>)</li>
<li>Skip camera undo when undo is not enabled on <code>vtkMRMLCameraNode</code> (<a href="https://github.com/Slicer/Slicer/pull/7018">PR-7018</a>)</li>
<li>Fix splash screen loading text visibility (<a href="https://github.com/Slicer/Slicer/pull/7023">PR-7023</a>)</li>
<li>Fix crash when adding <code>%s</code> specifier to color legend label (<a href="https://github.com/Slicer/Slicer/pull/6795">PR-6795</a>)</li>
<li>Fix home shortcut behavior when Python console visible (<a href="https://github.com/Slicer/Slicer/pull/7167">PR-7167</a>)</li>
<li>Fix scene compatibility error message (<a href="https://github.com/Slicer/Slicer/pull/6755">PR-6755</a>)</li>
<li>Fix non-functional exit cross on “Save before exit” popup (<a href="https://github.com/Slicer/Slicer/pull/6906">PR-6906</a>)</li>
<li>Fix launching <code>.py</code> files in Slicer with <code>-I</code> argument (<a href="https://github.com/Slicer/Slicer/pull/6959">MR-6959</a>)</li>
</ul>
<h3 id="heading--io">IO</h3>
<ul>
<li>Enable process output retrieval during CLI execution (<a href="https://github.com/Slicer/Slicer/pull/6721">PR-6721</a>)</li>
<li>Support shallow and deep copy for scalar volume display node (<a href="https://github.com/Slicer/Slicer/pull/6857">PR-6857</a>)</li>
<li>Simplify loading of <code>.vtk</code> image files (<a href="https://github.com/Slicer/Slicer/pull/7117">PR-7117</a>)</li>
<li>Update <code>vtkMRMLParser</code> to support custom types ending with “Node” (<a href="https://github.com/Slicer/Slicer/pull/6715">PR-6715</a>)</li>
<li>Check file extension readers before inspecting content (<a href="https://github.com/Slicer/Slicer/pull/7139">PR-7139</a>)</li>
<li>Update MultiVolumeImporter to load as volume sequence by default (<a href="https://github.com/Slicer/Slicer/pull/7141">PR-7141</a>)</li>
<li>Load tables with default column type (<a href="https://github.com/Slicer/Slicer/pull/6775">PR-6775</a>)</li>
<li>Generate segment colors for raw NRRD files via storage node (<a href="https://github.com/Slicer/Slicer/pull/6959">MR-6959</a>)</li>
<li>Choose file reader/writer based on confidence level (<a href="https://github.com/Slicer/Slicer/pull/6998">PR-6998</a>)</li>
<li>Update <code>vtkMRMLWriteXMLMatrix4x4Macro</code> to separate values with a single space (<a href="https://github.com/Slicer/Slicer/pull/7039">PR-7039</a>)</li>
<li>Fix error message in <code>vtkMRMLColorTableNode</code> (<a href="https://github.com/Slicer/Slicer/pull/6729">PR-6729</a>)</li>
<li>Fix reading of vector fields from NIFTI files (<a href="https://github.com/Slicer/Slicer/pull/6791">PR-6791</a>)</li>
<li>Fix CLI module issue with reading output from initially empty nodes (<a href="https://github.com/Slicer/Slicer/pull/6959">MR-6959</a>)</li>
</ul>
<h3 id="heading--extension">Extension</h3>
<ul>
<li>Add API for downloading and installing extensions (<a href="https://github.com/Slicer/Slicer/pull/7145">PR-7145</a>)</li>
<li>Update ExtensionsManager install API to check for updates (<a href="https://github.com/Slicer/Slicer/pull/7151">PR-7151</a>)</li>
<li>Update server-based extension installation to return a boolean status (<a href="https://github.com/Slicer/Slicer/pull/7148">PR-7148</a>)</li>
<li>Fix blank Extensions Manager on Linux due to Chromium sandboxing (<a href="https://github.com/Slicer/Slicer/pull/6744">PR-6744</a>)</li>
<li>Fix <code>IsPluginInstalled()</code> behavior when the plugin is installed in the application build tree (<a href="https://github.com/Slicer/Slicer/pull/6970">PR-6970</a>)</li>
<li>Fix color setting in <code>qSlicerExtensionsLocalWidget</code> status messages (<a href="https://github.com/Slicer/Slicer/pull/7147">PR-7147</a>)</li>
</ul>
<h3 id="heading--scripting">Scripting</h3>
<ul>
<li>Add <a href="https://slicer.readthedocs.io/en/latest/developer_guide/parameter_nodes/index.html">Parameter Node Wrapper</a> for <code>vtkMRMLScriptedModuleNode</code> to provide typed member access (<a href="https://github.com/Slicer/Slicer/pull/6684">PR-6684</a>, <a href="https://github.com/Slicer/Slicer/pull/6725">PR-6725</a>, <a href="https://github.com/Slicer/Slicer/pull/6727">PR-6727</a>, <a href="https://github.com/Slicer/Slicer/pull/6740">PR-6740</a>, <a href="https://github.com/Slicer/Slicer/pull/6757">PR-6757</a>, <a href="https://github.com/Slicer/Slicer/pull/6772">PR-6772</a>, <a href="https://github.com/Slicer/Slicer/pull/6771">PR-6771</a>, <a href="https://github.com/Slicer/Slicer/pull/6783">PR-6783</a>, <a href="https://github.com/Slicer/Slicer/pull/6800">PR-6800</a>, <a href="https://github.com/Slicer/Slicer/pull/6808">PR-6808</a>, <a href="https://github.com/Slicer/Slicer/pull/6829">PR-6829</a>, <a href="https://github.com/Slicer/Slicer/pull/6843">PR-6843</a>, <a href="https://github.com/Slicer/Slicer/pull/6848">PR-6848</a>, <a href="https://github.com/Slicer/Slicer/pull/6862">PR-6862</a>, <a href="https://github.com/Slicer/Slicer/pull/6865">PR-6865</a>, <a href="https://github.com/Slicer/Slicer/pull/6871">PR-6871</a>, <a href="https://github.com/Slicer/Slicer/pull/6891">PR-6891</a>)</li>
<li>Enable use of <code>pathlib.Path</code> objects for paths in <code>slicer.util</code> (<a href="https://github.com/Slicer/Slicer/pull/6743">PR-6743</a>)</li>
<li>Add array size hints for improved Python wrapping (<a href="https://github.com/Slicer/Slicer/pull/6765">PR-6765</a>)</li>
<li>Implement ParameterNodeWrapper default by assignment (<a href="https://github.com/Slicer/Slicer/pull/6871">PR-6871</a>)</li>
<li>Add module paths to the application via drag-and-drop (<a href="https://github.com/Slicer/Slicer/pull/6872">PR-6872</a>)</li>
<li>Allow setting a custom editor for <code>.py</code> files (<a href="https://github.com/Slicer/Slicer/pull/7074">PR-7074</a>)</li>
<li>Add utility function to retrieve ROI box as <code>vtkPolyData</code> (<a href="https://github.com/Slicer/Slicer/pull/6958">PR-6958</a>)</li>
<li>Add “Test” button to ScriptedLoadableModule UI (<a href="https://github.com/Slicer/Slicer/pull/7038">PR-7038</a>)</li>
<li>Add convenience methods for locating markup control points (<a href="https://github.com/Slicer/Slicer/pull/6959">MR-6959</a>)</li>
<li>Update <code>slicer.util.updateVolumeFromArray</code> to support 1D NumPy arrays (<a href="https://github.com/Slicer/Slicer/pull/7142">PR-7142</a>)</li>
<li>Update DWMRIMultishellIOTests to remove nose function dependency (<a href="https://github.com/Slicer/Slicer/pull/7052">PR-7052</a>)</li>
<li>Improve error reporting in ScriptedFileReaderWriterTest (<a href="https://github.com/Slicer/Slicer/pull/7144">PR-7144</a>)</li>
<li>Register ParameterNodeWrapper plugins within corresponding modules (<a href="https://github.com/Slicer/Slicer/pull/6855">PR-6855</a>)</li>
<li>Apply miscellaneous scripted module fixes (<a href="https://github.com/Slicer/Slicer/pull/6993">PR-6993</a>)</li>
<li>Add Python utility functions for ITK image ↔ volume node conversion (<a href="https://github.com/Slicer/Slicer/pull/7094">PR-7094</a>)</li>
<li>Fix observer warning in scripted module template (<a href="https://github.com/Slicer/Slicer/pull/6720">PR-6720</a>)</li>
<li>Fix lost <code>setValue</code> function with nested parameter packs (<a href="https://github.com/Slicer/Slicer/pull/6851">PR-6851</a>)</li>
<li>Fix Python wrapping for methods using enum arguments (<a href="https://github.com/Slicer/Slicer/pull/6935">PR-6935</a>)</li>
</ul>
<h3 id="heading--internationalization-localization">Internationalization/Localization</h3>
<ul>
<li>Bundle Qt language tools (<a href="https://github.com/Slicer/Slicer/pull/6798">PR-6798</a>)</li>
<li>Ensure Qt language tools are bundled on macOS (<a href="https://github.com/Slicer/Slicer/pull/6904">PR-6904</a>)</li>
<li>Add translation function for Python scripted modules (<a href="https://github.com/Slicer/Slicer/pull/6917">PR-6917</a>)</li>
<li>Update CTK to the latest version for improved translations (<a href="https://github.com/Slicer/Slicer/pull/6926">PR-6926</a>)</li>
<li>Enable <code>update_translations.py</code> to create new translation components (<a href="https://github.com/Slicer/Slicer/pull/7107">PR-7107</a>)</li>
<li>Mark additional text as translatable (<a href="https://github.com/Slicer/Slicer/pull/6921">PR-6921</a>)</li>
<li>Position literals after string format specifiers for translation (<a href="https://github.com/Slicer/Slicer/pull/6777">PR-6777</a>)</li>
<li>Make loadable module titles translatable (<a href="https://github.com/Slicer/Slicer/pull/6828">PR-6828</a>)</li>
<li>Fix application’s <code>applicationLocale</code> object (<a href="https://github.com/Slicer/Slicer/pull/7035">PR-7035</a>)</li>
<li>Fix welcome module translation (<a href="https://github.com/Slicer/Slicer/pull/6810">PR-6810</a>)</li>
<li>Apply minor fixes to improve translations, remove warnings, and enhance Python wrapping (<a href="https://github.com/Slicer/Slicer/pull/6820">PR-6820</a>)</li>
<li>Mark translatable strings in various core components (Base/QTGUI, Base/QTCore, Base/QTApp, Base/QTCli) (<a href="https://github.com/Slicer/Slicer/pull/6704">PR-6704</a>, <a href="https://github.com/Slicer/Slicer/pull/6768">PR-6768</a>, <a href="https://github.com/Slicer/Slicer/pull/6784">PR-6784</a>, <a href="https://github.com/Slicer/Slicer/pull/6793">PR-6793</a>, <a href="https://github.com/Slicer/Slicer/pull/6821">PR-6821</a>)</li>
<li>Make all text in built-in CLI modules translatable (<a href="https://github.com/Slicer/Slicer/pull/6681">PR-6681</a>)</li>
<li>Mark translatable strings in DataProbe module (<a href="https://github.com/Slicer/Slicer/pull/6960">PR-6960</a>)</li>
<li>Mark translatable strings in Sequences module (<a href="https://github.com/Slicer/Slicer/pull/6977">PR-6977</a>)</li>
<li>Mark translatable strings in Markups module (<a href="https://github.com/Slicer/Slicer/pull/6962">PR-6962</a>)</li>
<li>Mark translatable strings in Segmentations module (<a href="https://github.com/Slicer/Slicer/pull/6948">PR-6948</a>)</li>
<li>Mark translatable strings in SegmentStatistics module (<a href="https://github.com/Slicer/Slicer/pull/6942">PR-6942</a>)</li>
<li>Mark translatable strings in Volume Rendering module (<a href="https://github.com/Slicer/Slicer/pull/6959">MR-6959</a>)</li>
<li>Mark translatable strings in Volumes module (<a href="https://github.com/Slicer/Slicer/pull/6655">PR-6655</a>)</li>
</ul>
<h2 id="heading--improved-modules">Improved Modules</h2>
<h3 id="heading--dicom">DICOM</h3>
<ul>
<li>Add DICOM patcher rules for character set and exposure fixes (<a href="https://github.com/Slicer/Slicer/pull/6940">PR-6940</a>)</li>
<li>Default to loading DICOM files using the DICOM module (<a href="https://github.com/Slicer/Slicer/pull/7077">PR-7077</a>)</li>
<li>Support special characters when saving scenes to DICOM SC (<a href="https://github.com/Slicer/Slicer/pull/6963">PR-6963</a>)</li>
<li>Add parsed parameters in <code>DICOMRequestHandler</code> (<a href="https://github.com/Slicer/Slicer/pull/6713">PR-6713</a>)</li>
<li>Save DICOM instance UID in the image sequence plugin (<a href="https://github.com/Slicer/Slicer/pull/7096">PR-7096</a>)</li>
<li>Allow multiple DICOM plugins with the same confidence level for export (<a href="https://github.com/Slicer/Slicer/pull/6863">PR-6863</a>)</li>
<li>Fix regression in DICOM patcher (<a href="https://github.com/Slicer/Slicer/pull/6950">PR-6950</a>)</li>
<li>Fix user warning triggered by the default progress callback in <code>send()</code> (<a href="https://github.com/Slicer/Slicer/pull/6822">PR-6822</a>)</li>
<li>Support color DICOM data series (<a href="https://github.com/Slicer/Slicer/pull/7089">PR-7089</a>)</li>
<li>Remove redundant “Warning:” prefix in DICOM popup messages (<a href="https://github.com/Slicer/Slicer/pull/7164">PR-7164</a>)</li>
<li>Import additional series information from DICOM images (<a href="https://github.com/Slicer/Slicer/pull/6877">PR-6877</a>)</li>
</ul>
<h3 id="heading--markups">Markups</h3>
<ul>
<li>Allow custom markup classes to store additional properties in the markups file as JSON (<a href="https://github.com/Slicer/Slicer/pull/6756">PR-6756</a>)</li>
<li>Add support for curve torsion measurement (<a href="https://github.com/Slicer/Slicer/pull/6774">PR-6774</a>)</li>
<li>Allow line/angle markups to remain visible even when control points are hidden (<a href="https://github.com/Slicer/Slicer/pull/6842">PR-6842</a>)</li>
<li>Support detaching the markups toolbar from the mouse mode toolbar (<a href="https://github.com/Slicer/Slicer/pull/6675">PR-6675</a>)</li>
<li>Fix reading of default markup active color (<a href="https://github.com/Slicer/Slicer/pull/6736">PR-6736</a>)</li>
<li>Fix markups curve measurements test (<a href="https://github.com/Slicer/Slicer/pull/6816">PR-6816</a>)</li>
<li>Add toggle action for markups in the Markups Place button menu (<a href="https://github.com/Slicer/Slicer/pull/6856">PR-6856</a>)</li>
<li>Improve example for exporting markup measurements (<a href="https://github.com/Slicer/Slicer/pull/6746">PR-6746</a>)</li>
<li>Increase robustness for loading legacy annotation fiducials, lines, and ROI nodes (<a href="https://github.com/Slicer/Slicer/pull/6814">PR-6814</a>)</li>
<li>Fix copying of curves using <code>CopyContent</code> (<a href="https://github.com/Slicer/Slicer/pull/6818">PR-6818</a>)</li>
<li>Fix static control point measurements for closed curves (<a href="https://github.com/Slicer/Slicer/pull/6887">PR-6887</a>)</li>
<li>Fix potential NaN in torsion calculations for markup curves (<a href="https://github.com/Slicer/Slicer/pull/7122">PR-7122</a>)</li>
<li>Enable translation/rotation of unlocked points in a list (<a href="https://github.com/Slicer/Slicer/pull/7025">PR-7025</a>)</li>
</ul>
<h3 id="heading--models">Models</h3>
<ul>
<li>Fix Models module name display issue (<a href="https://github.com/Slicer/Slicer/pull/6846">PR-6846</a>)</li>
</ul>
<h3 id="heading--sample-data">Sample Data</h3>
<ul>
<li>Fix sample dataset labels not appearing on large desktop monitors (<a href="https://github.com/Slicer/Slicer/pull/6731">PR-6731</a>)</li>
</ul>
<h3 id="heading--sequences">Sequences</h3>
<ul>
<li>Restore synchronized visibility for sequence table headers (<a href="https://github.com/Slicer/Slicer/pull/6951">PR-6951</a>)</li>
<li>Fix warning in sequence browser seek widget (<a href="https://github.com/Slicer/Slicer/pull/6959">MR-6959</a>)</li>
<li>Improve sequence editing functionality and fix related issues (<a href="https://github.com/Slicer/Slicer/pull/6930">PR-6930</a>)</li>
<li>Fix consistency check in <code>vtkMRMLVolumeSequenceStorageNode</code> (<a href="https://github.com/Slicer/Slicer/pull/7069">PR-7069</a>)</li>
</ul>
<h3 id="heading--segmentation">Segmentation</h3>
<ul>
<li>Add soft edge option to Mask Volume Segment Editor effect (<a href="https://github.com/Slicer/Slicer/pull/6849">PR-6849</a>)</li>
<li>Add <code>vtkITKGrowCut</code> filter (<a href="https://github.com/Slicer/Slicer/pull/6946">PR-6946</a>)</li>
<li>Use inclusive language for segmentation source representation (<a href="https://github.com/Slicer/Slicer/pull/6901">PR-6901</a>)</li>
<li>Create non-existing segments when importing a label map to segmentation node (<a href="https://github.com/Slicer/Slicer/pull/6835">PR-6835</a>)</li>
<li>Set segment “Pickable” display property to true if not specified (<a href="https://github.com/Slicer/Slicer/pull/7000">PR-7000</a>)</li>
<li>Fix behavior after invisible segment confirmation popup (<a href="https://github.com/Slicer/Slicer/pull/7084">PR-7084</a>)</li>
</ul>
<h3 id="heading--subject-hierarchy">Subject Hierarchy</h3>
<ul>
<li>Add option in Subject Hierarchy to set segment opacity (<a href="https://github.com/Slicer/Slicer/pull/6932">PR-6932</a>)</li>
<li>Add menu actions to hide or show selected items in the subject tree (<a href="https://github.com/Slicer/Slicer/pull/7028">PR-7028</a>)</li>
</ul>
<h3 id="heading--surfacetoolbox">SurfaceToolbox</h3>
<ul>
<li>Fix Dynamic Modeler layout in SurfaceToolbox module (<a href="https://github.com/Slicer/Slicer/pull/6938">PR-6938</a>)</li>
<li>Enable uniform remeshing in SurfaceToolbox for triangle strips (<a href="https://github.com/Slicer/Slicer/pull/6974">PR-6974</a>)</li>
</ul>
<h3 id="heading--tables">Tables</h3>
<ul>
<li>Fix initialization of non-string table cells to prevent random values (<a href="https://github.com/Slicer/Slicer/pull/6850">PR-6850</a>)</li>
<li>Preserve column order when reading tables from files (<a href="https://github.com/Slicer/Slicer/pull/6850">PR-6850</a>)</li>
</ul>
<h3 id="heading--terminologies">Terminologies</h3>
<ul>
<li>Fix handling of non-modified terminology types (<a href="https://github.com/Slicer/Slicer/pull/7009">PR-7009</a>)</li>
</ul>
<h3 id="heading--volume-rendering">Volume Rendering</h3>
<ul>
<li>Fix color synchronization inaccuracies in the Volume Rendering module (<a href="https://github.com/Slicer/Slicer/pull/7042">PR-7042</a>)</li>
<li>Prevent display of volume rendering if the volume is under a non-linear transform (<a href="https://github.com/Slicer/Slicer/pull/7065">PR-7065</a>)</li>
<li>Improve volume rendering presets (<a href="https://github.com/Slicer/Slicer/pull/6762">PR-6762</a>)</li>
</ul>
<h3 id="heading--webserver">WebServer</h3>
<ul>
<li>Add Web Server examples using Three.js and ModelViewer (<a href="https://github.com/Slicer/Slicer/pull/6985">PR-6985</a>)</li>
<li>Add VolView link to WebServer examples (<a href="https://github.com/Slicer/Slicer/pull/6995">PR-6995</a>)</li>
<li>Fix <code>SlicerRequestHandler</code> return value when reader does not return any node ID (<a href="https://github.com/Slicer/Slicer/pull/6752">PR-6752</a>)</li>
<li>Free notifier after request handling (<a href="https://github.com/Slicer/Slicer/pull/6824">PR-6824</a>)</li>
</ul>
<h2 id="heading--removed-modules">Removed Modules</h2>
<ul>
<li>Remove Annotations module (<a href="https://github.com/Slicer/Slicer/pull/6524">PR-6524</a>)</li>
<li>Move ACPC Transform module to SlicerNeuro extension (<a href="https://github.com/Slicer/Slicer/pull/7005">PR-7005</a>)</li>
</ul>
<h2 id="heading--infrastructure">Infrastructure</h2>
<h3 id="heading--packaging">Packaging</h3>
<ul>
<li>Change organization name and domain from NA-MIC to Slicer (<a href="https://github.com/Slicer/Slicer/pull/6750">PR-6750</a>)</li>
<li>Create a Windows Desktop shortcut during installation (<a href="https://github.com/Slicer/Slicer/pull/6761">PR-6761</a>)</li>
<li>Replace <code>lib</code> with <code>CMAKE_INSTALL_LIBDIR</code> for standardized library installation path (<a href="https://github.com/Slicer/Slicer/pull/6760">PR-6760</a>)</li>
<li>Fix issue with <code>CPACK_NSIS_INSTALL_SUBDIRECTORY</code> being overwritten (<a href="https://github.com/Slicer/Slicer/pull/7091">PR-7091</a>)</li>
<li>Update organization name and domain to <code>slicer.org</code> (<a href="https://github.com/Slicer/Slicer/pull/6879">PR-6879</a>)</li>
<li>Adjust package vendor setting for improved clarity (<a href="https://github.com/Slicer/Slicer/pull/6881">PR-6881</a>)</li>
<li>Fix Qt tools packaging (<a href="https://github.com/Slicer/Slicer/pull/6907">PR-6907</a>)</li>
</ul>
<h3 id="heading--testing">Testing</h3>
<ul>
<li>Fix <code>qMRMLLayoutManagerVisibilityTest</code> (<a href="https://github.com/Slicer/Slicer/pull/6797">PR-6797</a>)</li>
<li>Fix <code>qSlicerMouseModeToolBarTest1</code> (<a href="https://github.com/Slicer/Slicer/pull/6802">PR-6802</a>)</li>
<li>Update <code>SlicerOrientationSelectorTestTest</code> to accommodate widget rename (<a href="https://github.com/Slicer/Slicer/pull/7082">PR-7082</a>)</li>
<li>Update <code>test_slicer_util_save</code> to use a non-deprecated method (<a href="https://github.com/Slicer/Slicer/pull/7022">PR-7022</a>)</li>
<li>Fix failing <code>qMRMLLayoutManagerTest2</code> and <code>py_SubjectHierarchyGenericSelfTest</code> tests (<a href="https://github.com/Slicer/Slicer/pull/6755">PR-6755</a>)</li>
</ul>
<h3 id="heading--continuous-integration-ci">Continuous Integration (CI)</h3>
<ul>
<li>Fix “Build Slicer” CI workflow for push events (<a href="https://github.com/Slicer/Slicer/pull/7064">PR-7064</a>)</li>
<li>Skip steps in required jobs instead of skipping entire workflows (<a href="https://github.com/Slicer/Slicer/pull/7062">PR-7062</a>)</li>
<li>Update <code>codespell</code> GitHub workflow to include additional exceptions (<a href="https://github.com/Slicer/Slicer/pull/6853">PR-6853</a>)</li>
<li>Add Dependabot workflow to update GitHub Actions dependencies (<a href="https://github.com/Slicer/Slicer/pull/6888">PR-6888</a>)</li>
<li>Pin more GitHub actions to full-length commit SHA for consistency (<a href="https://github.com/Slicer/Slicer/pull/6898">PR-6898</a>)</li>
</ul>
<h3 id="heading--build-system">Build-System</h3>
<ul>
<li>Update minimum supported macOS versions (<a href="https://github.com/Slicer/Slicer/pull/6695">PR-6695</a>)</li>
<li>Remove exposure of <code>ui_*.h</code> files from public header files (<a href="https://github.com/Slicer/Slicer/pull/6909">PR-6909</a>)</li>
<li>Remove redundant includes (<a href="https://github.com/Slicer/Slicer/pull/7106">PR-7106</a>)</li>
<li>Fix timestamp warnings in external project download and extraction (<a href="https://github.com/Slicer/Slicer/pull/7138">PR-7138</a>)</li>
<li>Add missing include guards and remove unused header files (<a href="https://github.com/Slicer/Slicer/pull/7070">PR-7070</a>)</li>
<li>Prefer ITK Python wheels over building ITK Python from source (<a href="https://github.com/Slicer/Slicer/pull/7051">PR-7051</a>)</li>
<li>Fix various warnings (<a href="https://github.com/Slicer/Slicer/pull/6864">PR-6864</a>, <a href="https://github.com/Slicer/Slicer/pull/7048">PR-7048</a>)</li>
<li>Apply lint fixes (<a href="https://github.com/Slicer/Slicer/pull/7076">PR-7076</a>)</li>
<li>Update <code>vtkMRMLSliceNode</code> to use MRML helper macros (<a href="https://github.com/Slicer/Slicer/pull/7039">PR-7039</a>)</li>
<li>Fix build when OpenSSL support is disabled (<a href="https://github.com/Slicer/Slicer/pull/6747">PR-6747</a>)</li>
<li>Fix <code>vtkMarkupsAnnotationSceneTest</code> build with SceneViews module disabled (<a href="https://github.com/Slicer/Slicer/pull/6790">PR-6790</a>)</li>
<li>Support <code>slicerFunctionAddPythonQtResources()</code> for extension modules (<a href="https://github.com/Slicer/Slicer/pull/6792">PR-6792</a>)</li>
<li>Fix lint and spellchecker errors (<a href="https://github.com/Slicer/Slicer/pull/6949">PR-6949</a>)</li>
<li>Report error if an unsupported CMake version (3.25.0-3.25.2) is used (<a href="https://github.com/Slicer/Slicer/pull/6852">PR-6852</a>)</li>
<li>Speed up incremental builds on Linux (<a href="https://github.com/Slicer/Slicer/pull/6983">PR-6983</a>, <a href="https://github.com/Slicer/Slicer/pull/7001">PR-7001</a>)</li>
<li>Support enforcing specific Slicer revision during extension build (<a href="https://github.com/Slicer/Slicer/pull/7040">PR-7040</a>)</li>
<li>Fix deprecation warnings by explicitly calling <code>vtkStdString::c_str()</code> (<a href="https://github.com/Slicer/Slicer/pull/7044">PR-7044</a>)</li>
<li>Remove redundant <code>FindFontConfig</code> module (<a href="https://github.com/Slicer/Slicer/pull/6155">PR-6155</a>)</li>
<li>Fix potentially invalid pointer in <code>vtkSlicerSegmentationsModuleLogic</code> (<a href="https://github.com/Slicer/Slicer/pull/7050">PR-7050</a>)</li>
<li>Ensure consistent include guard definitions to match filenames (<a href="https://github.com/Slicer/Slicer/pull/7072">PR-7072</a>)</li>
<li>Replace deprecated Qt Script usage (<a href="https://github.com/Slicer/Slicer/pull/6710">PR-6710</a>)</li>
<li>Fix CMake 3.26 warning in <code>SlicerLinkerAsNeededFlagCheck</code> project (<a href="https://github.com/Slicer/Slicer/pull/7135">PR-7135</a>)</li>
<li>Ensure disabling <code>Slicer_USE_PYTHONQT</code> also disables <code>SimpleITK</code> (<a href="https://github.com/Slicer/Slicer/pull/7146">PR-7146</a>)</li>
<li>Fix Sphinx build warning in Python FAQ related to “txt” lexer (<a href="https://github.com/Slicer/Slicer/pull/7173">PR-7173</a>)</li>
<li>Fix Python-extension-manager-ssl-requirements build with <code>[crypto]</code> specifier (<a href="https://github.com/Slicer/Slicer/pull/7113">PR-7113</a>)</li>
<li>Add missing <code>QSslConfiguration</code> include (<a href="https://github.com/Slicer/Slicer/pull/6884">PR-6884</a>)</li>
<li>Validate application name in <code>slicerMacroBuildApplication</code> (<a href="https://github.com/Slicer/Slicer/pull/6880">PR-6880</a>)</li>
<li>Fix <code>vtkMarkupsAnnotationSceneTest</code> build with SceneViews module disabled (part 2) (<a href="https://github.com/Slicer/Slicer/pull/6834">PR-6834</a>)</li>
<li>Fix <code>-Wunused-parameter</code> warning in <code>vtkMRMLSliceLogic::VolumeWindowLevelEditable</code> (<a href="https://github.com/Slicer/Slicer/pull/6900">PR-6900</a>)</li>
<li>Fix <code>-Wrange-loop-construct</code> warning in Markups module (<a href="https://github.com/Slicer/Slicer/pull/6902">PR-6902</a>)</li>
<li>Fix Python linting issues (<a href="https://github.com/Slicer/Slicer/pull/6706">PR-6706</a>)</li>
<li>Remove unused <code>workaround_recommonmark_issue_191</code> custom Sphinx extension (<a href="https://github.com/Slicer/Slicer/pull/6714">PR-6714</a>)</li>
<li>Update markdown files to use LF line-endings (<a href="https://github.com/Slicer/Slicer/pull/6734">PR-6734</a>)</li>
<li>Fix Python lint errors (<a href="https://github.com/Slicer/Slicer/pull/6817">PR-6817</a>)</li>
<li>Correct various typos (<a href="https://github.com/Slicer/Slicer/pull/7032">PR-7032</a>, <a href="https://github.com/Slicer/Slicer/pull/7054">PR-7054</a>)</li>
<li>Ensure “<span class="hashtag-raw">#endif</span>” guards do not include comments (<a href="https://github.com/Slicer/Slicer/pull/7071">PR-7071</a>)</li>
<li>Fix typos in header comments (<a href="https://github.com/Slicer/Slicer/pull/7073">PR-7073</a>)</li>
<li>Improve comment clarity (<a href="https://github.com/Slicer/Slicer/pull/7075">PR-7075</a>)</li>
<li>Remove duplicated include in <code>qSlicerPersistentCookieJar</code> (<a href="https://github.com/Slicer/Slicer/pull/7158">PR-7158</a>)</li>
<li>Remove duplicated include in <code>vtkMRMLSequenceStorageNode.cxx</code> (<a href="https://github.com/Slicer/Slicer/pull/7162">PR-7162</a>)</li>
</ul>
<h3 id="heading--dependencies">Dependencies</h3>
<p><strong>vtkAddon:</strong></p>
<ul>
<li>Simplify wrapping of module logic and MRML libraries (<a href="https://github.com/Slicer/Slicer/pull/6885">PR-6885</a>)</li>
<li>Add support for Python module naming (<a href="https://github.com/Slicer/Slicer/pull/6841">PR-6841</a>)</li>
<li>Fix potential out-of-bounds issue in <code>vtkCurveGenerator</code> (<a href="https://github.com/Slicer/Slicer/pull/7043">PR-7043</a>)</li>
<li>Remove redundant Markups MRML classes (<a href="https://github.com/Slicer/Slicer/pull/6883">PR-6883</a>)</li>
</ul>
<p><strong>VTK:</strong></p>
<ul>
<li>Backport OpenXR and OpenXRRemoting updates (<a href="https://github.com/Slicer/Slicer/pull/6780">PR-6780</a>)</li>
<li>Backport rendering changes for VR, OpenVR, and OpenXR (<a href="https://github.com/Slicer/Slicer/pull/6967">PR-6967</a>)</li>
<li>Upgrade VTK from 9.1.20220125 to 9.2.20230607 (<a href="https://github.com/Slicer/Slicer/pull/7010">PR-7010</a>)</li>
<li>Reintroduce OpenVR API to retrieve last pose (<a href="https://github.com/Slicer/Slicer/pull/6754">PR-6754</a>)</li>
<li>Ensure valid OpenVR pose retrieval (<a href="https://github.com/Slicer/Slicer/pull/6779">PR-6779</a>)</li>
<li>Restore complex gesture support in SlicerVirtualReality (<a href="https://github.com/Slicer/Slicer/pull/6805">PR-6805</a>)</li>
<li>Fix regression blocking older <code>.vtp</code> file loading (<a href="https://github.com/Slicer/Slicer/pull/7080">PR-7080</a>)</li>
<li>Resolve regression in Dynamic Modeler curve cut (<a href="https://github.com/Slicer/Slicer/pull/7140">PR-7140</a>)</li>
<li>Address Windows build error related to <code>.pyi</code> file generation (<a href="https://github.com/Slicer/Slicer/pull/6903">PR-6903</a>)</li>
<li>Fix packaging error due to missing <code>.pyi</code> files (<a href="https://github.com/Slicer/Slicer/pull/6905">PR-6905</a>)</li>
<li>Support external build for RenderingOpenXRRemoting module (<a href="https://github.com/Slicer/Slicer/pull/6933">PR-6933</a>)</li>
<li>Workaround external project output error flagging (<a href="https://github.com/Slicer/Slicer/pull/7104">PR-7104</a>)</li>
</ul>
<p><strong>CTK:</strong></p>
<ul>
<li>Address warnings and miscellaneous issues (<a href="https://github.com/Slicer/Slicer/pull/7045">PR-7045</a>)</li>
<li>Fix crash when importing <code>ctk</code> or <code>qt</code> in standalone Python (<a href="https://github.com/Slicer/Slicer/pull/6886">PR-6886</a>)</li>
<li>Apply minor fixes in the latest version (<a href="https://github.com/Slicer/Slicer/pull/6939">PR-6939</a>)</li>
<li>Fix initial sizing of modules using <code>ctkFlowLayout</code> (<a href="https://github.com/Slicer/Slicer/pull/7111">PR-7111</a>)</li>
<li>Resolve build issue for CTK DICOM Core library (<a href="https://github.com/Slicer/Slicer/pull/6908">PR-6908</a>)</li>
<li>Correct styling of <code>ctkRangeSlider</code> (<a href="https://github.com/Slicer/Slicer/pull/7116">PR-7116</a>)</li>
<li>Remove code specific to Qt 4 (<a href="https://github.com/Slicer/Slicer/pull/7127">PR-7127</a>)</li>
<li>Ensure only required Qt components are included (<a href="https://github.com/Slicer/Slicer/pull/7129">PR-7129</a>, <a href="https://github.com/Slicer/Slicer/pull/7133">PR-7133</a>)</li>
<li>Update general CTK components (<a href="https://github.com/Slicer/Slicer/pull/7110">PR-7110</a>)</li>
</ul>
<p><strong>ITK:</strong></p>
<ul>
<li>Fix read/write of displacement fields in NIFTI format (<a href="https://github.com/Slicer/Slicer/pull/6799">PR-6799</a>)</li>
<li>Backport fixes for gcc13 compatibility in ITK and VTK (<a href="https://github.com/Slicer/Slicer/pull/6971">PR-6971</a>)</li>
<li>Improve dependency analysis for Flatpak (<a href="https://github.com/Slicer/Slicer/pull/7019">PR-7019</a>)</li>
<li>Clarify <code>image_from_vtk_image</code> usage (<a href="https://github.com/Slicer/Slicer/pull/7168">PR-7168</a>)</li>
</ul>
<p><strong>Other Dependencies:</strong></p>
<ul>
<li>Update RapidJSON to 2023.05.09 to resolve warnings (<a href="https://github.com/Slicer/Slicer/pull/7047">PR-7047</a>)</li>
<li>Correct GitHub organization for <code>qRestAPI</code> external project (<a href="https://github.com/Slicer/Slicer/pull/7085">PR-7085</a>)</li>
<li>Update Python packages to latest versions (<a href="https://github.com/Slicer/Slicer/pull/7046">PR-7046</a>, <a href="https://github.com/Slicer/Slicer/pull/6803">PR-6803</a>, <a href="https://github.com/Slicer/Slicer/pull/6859">PR-6859</a>)</li>
</ul>
<h3 id="heading--documentation">Documentation</h3>
<p><strong>Templates and Guides:</strong></p>
<ul>
<li>Tweak “release” issue template (<a href="https://github.com/Slicer/Slicer/pull/6699">PR-6699</a>)</li>
<li>Tweak “patch-release” issue template (<a href="https://github.com/Slicer/Slicer/pull/6701">PR-6701</a>)</li>
<li>Improve “release” and “patch-release” issue templates (<a href="https://github.com/Slicer/Slicer/pull/6703">PR-6703</a>)</li>
<li>Add “Self Tests” developer documentation (<a href="https://github.com/Slicer/Slicer/pull/6742">PR-6742</a>)</li>
</ul>
<p><strong>General Documentation Improvements:</strong></p>
<ul>
<li>Fix typos and grammar in various documents (<a href="https://github.com/Slicer/Slicer/pull/7063">PR-7063</a>, <a href="https://github.com/Slicer/Slicer/pull/7121">PR-7121</a>)</li>
<li>Update Debian distribution names in linux.md (<a href="https://github.com/Slicer/Slicer/pull/7020">PR-7020</a>)</li>
<li>Improve documentation on <code>slicer.util.pip_install</code> usage (<a href="https://github.com/Slicer/Slicer/pull/7172">PR-7172</a>)</li>
<li>Fix typo in Troubleshooting guide (<a href="https://github.com/Slicer/Slicer/pull/6707">PR-6707</a>)</li>
<li>Correct link to ImageStacks tutorial in Volumes module documentation (<a href="https://github.com/Slicer/Slicer/pull/6718">PR-6718</a>)</li>
<li>Update parameter node documentation (<a href="https://github.com/Slicer/Slicer/pull/6873">PR-6873</a>)</li>
</ul>
<p><strong>Scripting and API Documentation:</strong></p>
<ul>
<li>Describe <code>pip_install</code> usage in modules (<a href="https://github.com/Slicer/Slicer/pull/6913">PR-6913</a>)</li>
<li>Add Qt connection details to Python FAQ (<a href="https://github.com/Slicer/Slicer/pull/6737">PR-6737</a>)</li>
<li>Improve <code>slicer.util.to_bool</code> docstring (<a href="https://github.com/Slicer/Slicer/pull/6697">PR-6697</a>)</li>
<li>Add Python FAQ improvements (<a href="https://github.com/Slicer/Slicer/pull/7014">PR-7014</a>)</li>
</ul>
<p><strong>Code and Feature-Specific Documentation:</strong></p>
<ul>
<li>Clarify volume computation in Segment statistics documentation (<a href="https://github.com/Slicer/Slicer/pull/6739">PR-6739</a>)</li>
<li>Document how to add volume rendering presets (<a href="https://github.com/Slicer/Slicer/pull/6763">PR-6763</a>)</li>
<li>Clarify <code>GetTransformBetweenNodes</code> PostMultiply mode (<a href="https://github.com/Slicer/Slicer/pull/6840">PR-6840</a>)</li>
<li>Describe automatic resampling of binary labelmap representation (<a href="https://github.com/Slicer/Slicer/pull/7170">PR-7170</a>)</li>
<li>Improve “Interpolation order” parameter documentation (<a href="https://github.com/Slicer/Slicer/pull/7006">PR-7006</a>)</li>
<li>Add example for model point picking (<a href="https://github.com/Slicer/Slicer/pull/7026">PR-7026</a>)</li>
<li>Expand GUI documentation for Segment Editor module (<a href="https://github.com/Slicer/Slicer/pull/6955">PR-6955</a>)</li>
<li>Add limitations section to segmentations.md (<a href="https://github.com/Slicer/Slicer/pull/6978">PR-6978</a>)</li>
</ul>
<p><strong>Platform-Specific Notes and Fixes:</strong></p>
<ul>
<li>Add warning in linux.md about Debian’s OpenSSL (<a href="https://github.com/Slicer/Slicer/pull/7033">PR-7033</a>)</li>
<li>Add note in linux.md regarding Debian 12 and CMake (<a href="https://github.com/Slicer/Slicer/pull/7031">PR-7031</a>)</li>
<li>Update Windows build instructions (<a href="https://github.com/Slicer/Slicer/pull/7036">PR-7036</a>)</li>
<li>Confirm compatibility with newer CMake versions (<a href="https://github.com/Slicer/Slicer/pull/7053">PR-7053</a>)</li>
</ul>
<p><strong>Example Code and Practical Usage:</strong></p>
<ul>
<li>Add hanging protocol example to script repository (<a href="https://github.com/Slicer/Slicer/pull/6915">PR-6915</a>)</li>
<li>Update example usage in sequence browser documentation (<a href="https://github.com/Slicer/Slicer/pull/6854">PR-6854</a>)</li>
<li>Update segmenteditor.md with node reference info (<a href="https://github.com/Slicer/Slicer/pull/7134">PR-7134</a>)</li>
</ul>
<p><strong>Syntax and Formatting Adjustments:</strong></p>
<ul>
<li>Fix miscellaneous typos (<a href="https://github.com/Slicer/Slicer/pull/7055">PR-7055</a>, <a href="https://github.com/Slicer/Slicer/pull/7057">PR-7057</a>)</li>
<li>Update snippet syntax in developer guide (<a href="https://github.com/Slicer/Slicer/pull/7132">PR-7132</a>)</li>
<li>Refine syntax in <code>License.txt</code> and <code>Transforms.dox</code> (<a href="https://github.com/Slicer/Slicer/pull/7057">PR-7057</a>, <a href="https://github.com/Slicer/Slicer/pull/7055">PR-7055</a>)</li>
</ul>

---
