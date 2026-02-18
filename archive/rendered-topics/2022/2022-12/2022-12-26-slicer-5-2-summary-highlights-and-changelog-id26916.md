# Slicer 5.2: Summary, Highlights and Changelog

**Topic ID**: 26916
**Date**: 2022-12-26
**URL**: https://discourse.slicer.org/t/slicer-5-2-summary-highlights-and-changelog/26916

---

## Post #1 by @jcfr (2022-12-26 07:40 UTC)

<h1><a name="p-88075-table-of-content-1" class="anchor" href="#p-88075-table-of-content-1" aria-label="Heading link"></a>Table of content</h1>
<ul>
<li><a href="#heading--summary">Summary</a></li>
<li><a href="#heading--highlights">Highlights</a></li>
<li><a href="https://discourse.slicer.org/t/slicer-5-2-summary-highlights-and-changelog/26916/2">Detailed Changlog</a></li>
</ul>
<h1 id="heading--summary">Summary</h1>
<p>The community of 3D Slicer developers is proud to announce that version 5.2 is<a href="http://download.slicer.org/"> now available for download</a>. This version begins our new release cycle, where we will aim for 3-4 releases per year. This release includes support for using 3D Slicer via its web API and support for installing ITK python packages through pip. It also includes many improved core modules and more than 10 new-and-improved extensions.</p>
<p>3D Slicer 5.2 builds on the success of earlier versions that have had over 1.2 million downloads of the core program and 6.1 million downloads of extensions during the last decade.</p>
<p>The development of 3D Slicer—including its numerous modules, extensions, datasets, pull requests, patches, issues reports, suggestions—is made possible by users, developers, contributors and commercial partners around the world. 3D Slicer is based on a stack of open-source software and we are working constantly on updating the underlying packages. This development is funded by various grants and agencies. For more details, please see the 3D Slicer <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#acknowledgments">Acknowledgments</a> page.</p>
<p>One of the main distinguishing features of 3D Slicer is its easy extensibility enabled by good quality documentation, a thriving community, cross-platform support &amp; open source code. 3D Slicer supports a number of extension types which offer a different mix of simplicity and range of control of the software.</p>
<p>A rigorous quality assurance system leveraging automated testing and user <a href="https://discourse.slicer.org/">feedback</a> ensures the timely detection of issues caused by ongoing work in different components of the platform. See the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/contributing.html">contributing guidelines</a></p>
<p><a href="https://www.slicer.org/">slicer.org</a> is the portal to the application, training materials, and the development community.</p>
<p>The <a href="https://slicer.readthedocs.io/en/5.2/user_guide/getting_started.html#tutorials">Slicer Tutorials</a> page provides a series of tutorials and data sets for training in the use of Slicer.</p>
<p><em>Please note that Slicer continues to be a research package and is not intended for clinical use (clinical users must obtain the necessary ethics or regulatory approvals).</em></p>
<h1 id="heading--highlights">Highlights</h1>
<h2 id="heading--highlights--itk-python-packages">ITK Python Packages</h2>
<ul>
<li>
<p><code>itk-*</code> Python packages <a href="https://slicer.readthedocs.io/en/5.2/developer_guide/script_repository/gui.html#install-a-python-package">can be installed directly into Slicer’s Python environment</a>. Previously this was not possible due to Slicer’ bundled ITK libraries conflicted with packages coming from PyPI.</p>
</li>
<li>
<p>Main ITK Python packages can be installed along with <a href="https://pypi.org/search/?q=itk-&amp;o=">packages built from ITK Remote Modules</a></p>
</li>
<li>
<p><a href="https://discourse.slicer.org/t/installing-itk-python-package-in-slicer-5-1-and-above/25636#example-applying-itk-filter-to-mrml-volume-node-3">ITK filters can be applied to images in Slicer.</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c691d761856398e1daafa4603f9c1f81b4aa59d1.png" data-download-href="/uploads/short-url/skD0aC4V7fkfofCvfL9B1D4G1Ff.png?dl=1" title="SlicerMorph"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c691d761856398e1daafa4603f9c1f81b4aa59d1_2_690x230.png" alt="SlicerMorph" data-base62-sha1="skD0aC4V7fkfofCvfL9B1D4G1Ff" width="690" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c691d761856398e1daafa4603f9c1f81b4aa59d1_2_690x230.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c691d761856398e1daafa4603f9c1f81b4aa59d1_2_1035x345.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c691d761856398e1daafa4603f9c1f81b4aa59d1_2_1380x460.png 2x" data-dominant-color="ABB3BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerMorph</span><span class="informations">1566×522 483 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<em>Alignment of primate skulls with <a href="https://slicermorph.github.io/">SlicerMorph</a> through ITK and ITK remote module Python packages. Registration of the skulls facilicates shape-based quantification of the morphological characteristics of specimens and related species.</em></p>
</li>
</ul>
<h2 id="heading--highlights--slicer-web-api">Slicer Web API</h2>
<ul>
<li>Slicer’s REST API is improved and extended, which web applications and other external software to use 3D Slicer features.</li>
<li>The new <code>slicerio.server</code> features of <a href="https://pypi.org/project/slicerio">slicerio Python package</a> allows using Slicer as a data viewer in any Python environment. All files are loaded into a single Slicer instance, which eliminates the wait time for application startup and also allows analyzing, comparing multiple data sets in one workspace.</li>
</ul>
<h2 id="heading--highlights--new-extensionsi">New extensions</h2>
<ul>
<li><a href="https://discourse.slicer.org/t/slicer-5-2-summary-highlights-and-changelog/26916/2#heading--extensions-new">10+ new and improved extensions</a>, including several AI segmentation tools, such as <a href="https://discourse.slicer.org/t/new-extension-fully-automatic-whole-body-ct-segmentation-in-2-minutes-using-totalsegmentator/26710">fully automatic segmentation of 100+ structures in CT images in less than 2-minutes using TotalSegmentator</a>, skull stripping, CMF segmentations, tools for liver intervention planning, 3d printing, computing proteins’ colocalization, experimental support of viewing large scale microscopy images.</li>
</ul>

---

## Post #2 by @jcfr (2022-12-26 07:40 UTC)

<h1 id="heading--changelog">Changelog</h1>
<ul>
<li>
<p><a href="#heading--core">Core</a></p>
<ul>
<li><a href="#heading--application">Application</a></li>
<li><a href="#heading--extension">Extension</a></li>
<li><a href="#heading--cli">CLI</a></li>
<li><a href="#heading--io">IO</a></li>
<li><a href="#heading--scripting">Scripting</a></li>
<li><a href="#heading--python-console">Python Console</a></li>
<li><a href="#heading--slice-view">Slice View</a></li>
<li><a href="#heading--mrml">MRML</a></li>
<li><a href="#heading--ui-customization">UI customization</a></li>
<li><a href="#heading--internationalization-localization">Internationalization/Localization</a></li>
<li><a href="#heading--documentation">Documentation</a></li>
</ul>
</li>
<li>
<p><a href="#heading--improved-modules">Improved Modules</a></p>
<ul>
<li><a href="#heading--dicom">DICOM</a></li>
<li><a href="#heading--markups">Markups</a></li>
<li><a href="#heading--segmentations">Segmentations</a></li>
<li><a href="#heading--subject-hierarchy">SubjectHierarchy</a></li>
<li><a href="#heading--surface-toolbox">Surface ToolBox</a></li>
<li><a href="#heading--webserver">WebServer</a></li>
<li><a href="#heading--volumes">Volumes</a></li>
<li><a href="#heading--sequence">Sequence</a></li>
</ul>
</li>
<li>
<p><a href="#heading--infrastructure">Infrastructure</a></p>
<ul>
<li><a href="#heading--continuous-integration">Continuous integration (CI)</a></li>
<li><a href="#heading--release-process">Release process</a></li>
<li><a href="#heading--packaging">Packaging</a></li>
<li><a href="#heading--openxr-support">OpenXR support</a></li>
<li><a href="#heading--dependencies">Dependencies</a></li>
</ul>
</li>
<li>
<p><a href="#heading--extensions">Extensions</a></p>
<ul>
<li><a href="#heading--extensions-new">New</a></li>
<li><a href="#heading--extensions-updated">Updated</a></li>
<li><a href="#heading--extensions-removed">Removed</a></li>
</ul>
</li>
</ul>
<h2 id="heading--core">Core</h2>
<h3 id="heading--application">Application</h3>
<ul>
<li>
<p><a href="https://discourse.slicer.org/t/stable-update-notification/23655/22">Display available application version in “About” box</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b471f1c759222193952990b76e57cfcf01468e7e.png" data-download-href="/uploads/short-url/pKi4ji7c9nlvkX1JhxhKzI3YNSm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b471f1c759222193952990b76e57cfcf01468e7e_2_516x322.png" alt="image" data-base62-sha1="pKi4ji7c9nlvkX1JhxhKzI3YNSm" width="516" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b471f1c759222193952990b76e57cfcf01468e7e_2_516x322.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b471f1c759222193952990b76e57cfcf01468e7e_2_774x483.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b471f1c759222193952990b76e57cfcf01468e7e_2_1032x644.png 2x" data-dominant-color="47474A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1344×838 68.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><a href="https://slicer.readthedocs.io/en/5.2/user_guide/settings.html#favorites">Support reordering favorite modules by drag and drop</a></p>
</li>
<li>
<p>In Help → Report a Bug, added <a href="https://github.com/Slicer/Slicer/commit/2395c07917">ability to quickly open to log file location</a>.</p>
</li>
</ul>
<h3 id="heading--extension">Extension</h3>
<ul>
<li>
<p><a href="https://slicer.readthedocs.io/en/5.2/developer_guide/script_repository.html#download-and-install-extension">Simplified extension installation from script</a></p>
</li>
<li>
<p><a href="https://discourse.slicer.org/t/enable-automatic-extension-update-check/25062">Extension auto-update is now on by default</a></p>
<ul>
<li>Added “Automatic updates” section in Welcome module</li>
<li>Show extensions with available updates at the top</li>
<li>Enabled automatic extension update check by default<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a92552d29cebfa8a9dc80c3c1ec1b20b1a0d6524.png" data-download-href="/uploads/short-url/o8kEMyffbxSRH5gLEzpdqebuw6M.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a92552d29cebfa8a9dc80c3c1ec1b20b1a0d6524.png" alt="image" data-base62-sha1="o8kEMyffbxSRH5gLEzpdqebuw6M" width="333" height="173"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">445×231 6.66 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
</li>
<li>
<p><a href="https://github.com/Slicer/Slicer/pull/6481">Display git diff when extension update is available</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55bfb68322fdddeeb686845ae88374fbef1b5b55.png" data-download-href="/uploads/short-url/cezkl4Y2od8rKaZhXjGasJGOGlD.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55bfb68322fdddeeb686845ae88374fbef1b5b55_2_517x306.png" alt="image" data-base62-sha1="cezkl4Y2od8rKaZhXjGasJGOGlD" width="517" height="306" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55bfb68322fdddeeb686845ae88374fbef1b5b55_2_517x306.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55bfb68322fdddeeb686845ae88374fbef1b5b55_2_775x459.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55bfb68322fdddeeb686845ae88374fbef1b5b55_2_1034x612.png 2x" data-dominant-color="363839"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1758×1040 76.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ul>
<h3 id="heading--cli">CLI</h3>
<ul>
<li>Allow using segmentation nodes directly as CLI module input/output (<a href="https://github.com/Slicer/Slicer/pull/6558">PR-6558</a>)</li>
<li>Allow selecting volume sequence nodes as CLI module input (<a href="https://github.com/Slicer/Slicer/pull/6482">PR-6482</a>)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1d39dae82949992afe6a0035948e07ba0870dbe.png" data-download-href="/uploads/short-url/pn7TDmVlII6wkSNX2Yo6KGp8dVI.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b1d39dae82949992afe6a0035948e07ba0870dbe.png" alt="image" data-base62-sha1="pn7TDmVlII6wkSNX2Yo6KGp8dVI" width="281" height="172"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">562×345 15.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
<h3 id="heading--io">IO</h3>
<ul>
<li>Updated ITK to allow opening a wider range of NIFTI files (<a href="https://github.com/Slicer/Slicer/pull/6545">PR-6545</a>)</li>
</ul>
<h3 id="heading--scripting">Scripting</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/installing-itk-python-package-in-slicer-5-1-and-above/25636">Added support for installing ITK Python packages</a></li>
</ul>
<h3 id="heading--python-console">Python Console</h3>
<ul>
<li>Developers can choose log level (error, warning, info, debug) that is displayed in the Python interactor (or can completely disable log message display) in Application Settings: Python / Python interactor / Log level.</li>
<li><a href="https://github.com/Slicer/Slicer/pull/5156#issuecomment-1278471951">Improved python console logging output</a>
<ul>
<li>Use origin as prefix for log messages in Python console (<a href="https://github.com/Slicer/Slicer/commit/92f24179e3">92f24179e</a>)</li>
<li>Updated CTK to <a href="https://github.com/Slicer/Slicer/commit/3a6d7b3d9a">improve logging API</a>, <a href="https://github.com/Slicer/Slicer/commit/53dbbf0c2e">fix cursor position during auto-complete</a>, <a href="https://github.com/Slicer/Slicer/commit/2e02a3581f">improve Python console</a> and <a href="https://github.com/Slicer/Slicer/commit/76d6542921">give access to log handlers</a>.</li>
</ul>
</li>
</ul>
<h3 id="heading--slice-view">Slice View</h3>
<ul>
<li>Changed the window/level reset operation to be control-left-doubleclick to avoid interfering with the default view operation of maximizing/restoring view size using left-double-click. (<a href="https://github.com/Slicer/Slicer/pull/6597">PR-6597</a>)</li>
<li>When setting window/level mode also activate it (<a href="https://github.com/Slicer/Slicer/pull/6572">PR-6572</a>)</li>
<li>Support setting slice view font file programmatically (<a href="https://github.com/Slicer/Slicer/pull/6642">PR-6642</a>)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b39099f46a19f6b34873a9b4c5febac596abbb28.jpeg" data-download-href="/uploads/short-url/pCvh0dz3TYyKldUh1ra2QBIOyFy.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b39099f46a19f6b34873a9b4c5febac596abbb28_2_517x163.jpeg" alt="image" data-base62-sha1="pCvh0dz3TYyKldUh1ra2QBIOyFy" width="517" height="163" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b39099f46a19f6b34873a9b4c5febac596abbb28_2_517x163.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b39099f46a19f6b34873a9b4c5febac596abbb28_2_775x244.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b39099f46a19f6b34873a9b4c5febac596abbb28_2_1034x326.jpeg 2x" data-dominant-color="554E5D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1144×363 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
<h3 id="heading--mrml">MRML</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/bug-in-create-new-volume-property/24984">Improved initialization of vtkMRMLVolumePropertyNode</a> (<a href="https://github.com/Slicer/Slicer/commit/0ff0e7bce5">0ff0e7bce</a>)</li>
<li>Fixed saving of MRB scene into root folder of windows drive (<a href="https://github.com/Slicer/Slicer/issues/6552">#6552</a>)</li>
<li><a href="https://discourse.slicer.org/t/embedding-uri-in-a-mrml-scene-file-for-viewing-the-mrml-scene-on-a-remote-slicer-application/25373/9">Allow referring to files hosted on https servers in the MRML scene</a> (<a href="https://github.com/Slicer/Slicer/pull/6604">PR-6604</a>)</li>
</ul>
<h3 id="heading--ui-customization">UI customization</h3>
<ul>
<li><a href="https://slicer.readthedocs.io/en/5.2/developer_guide/script_repository.html#change-the-crosshair-color">Added support for changing crosshair color</a> (<a href="https://github.com/Slicer/Slicer/pull/6496">PR-6496</a>)</li>
<li><a href="https://slicer.readthedocs.io/en/5.2/developer_guide/script_repository.html#change-box-color-in-3d-view">Added support for changing Box Color in 3D view</a> (<a href="https://github.com/Slicer/Slicer/pull/6467">PR-6467</a>)</li>
<li>Added option to hide the maximize view button (<a href="https://github.com/Slicer/Slicer/pull/6539">PR-6539</a>)</li>
<li>Added convenient ScriptedLoadableModule.resourcePath() function (<a href="https://github.com/Slicer/Slicer/pull/6678">PR-6678</a>)</li>
<li>Fixed generation of PythonSlicer and SlicerDesigner launcher settings for custom application (<a href="https://github.com/Slicer/Slicer/pull/6600">PR-6600</a>)</li>
</ul>
<h3 id="heading--internationalization-localization">Internationalization/Localization</h3>
<ul>
<li>Added helper script for updating language translation (.ts) files (<a href="https://github.com/Slicer/Slicer/pull/6674">PR-6674</a>)</li>
<li>Marked translatable strings in Data, EventBroker and Volumes modules</li>
<li>Marked some placeholder UI texts as non-translatable (<a href="https://github.com/Slicer/Slicer/commit/099721975">099721975</a>)</li>
</ul>
<h3 id="heading--documentation">Documentation</h3>
<ul>
<li>Added documentation for the following modules
<ul>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/dataprobe.html">Data Probe</a></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/cropvolume.html">Crop Volume</a></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/cropvolumesequence.html">Crop Volume Sequence</a></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/dynamicmodeler.html">Dynamic Modeler</a></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/extensionwizard.html">Extension Wizard</a></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/landmarkregistration.html">Landmark Registration</a></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/multivolumeexplorer.html">MultiVolumeExplorer</a></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/multivolumeimporter.html">MultiVolumeImporter</a></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/performance.html">Performance</a></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/sampledata.html">Sample Data</a></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/selftests.html">Self Tests</a></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/simplefilters.html">Simple Filters</a></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/surfacetoolbox.html">Surface Toolbox</a></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/texts.html">Texts</a></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/vectortoscalarvolume.html">Vector to Scalar Volume</a></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/slicerwelcome.html">Welcome</a></li>
</ul>
</li>
<li>Script repository
<ul>
<li>Added python snippets to <a href="https://slicer.readthedocs.io/en/5.2/developer_guide/script_repository.html#change-the-crosshair-color">change crosshair color</a> and <a href="https://slicer.readthedocs.io/en/5.2/developer_guide/script_repository.html#change-box-color-in-3d-view">change box color</a>.</li>
<li><a href="https://slicer.readthedocs.io/en/5.2/developer_guide/script_repository.html#export-dicom-series-from-the-database-to-research-file-format">Added script example for bulk export from DICOM database</a></li>
<li>Added <a href="https://slicer.readthedocs.io/en/5.2/developer_guide/script_repository.html#batch-processing">batch processing</a> examples</li>
<li>Updated DICOM examples to adapt to CTK API changes (<a href="https://github.com/Slicer/Slicer/pull/6535">PR-6535</a>)</li>
</ul>
</li>
<li>Get Help
<ul>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/get_help.html#slicer-application-does-not-start">Updated Windows Mesa renderer instructions</a></li>
</ul>
</li>
<li>Developer Guide
<ul>
<li>Added <a href="https://slicer.readthedocs.io/en/5.2/developer_guide/module_overview.html">Module Overview</a> documentation</li>
<li>Improved description of python wrapped C++ classes (<a href="https://github.com/Slicer/Slicer/commit/9f4f3ce209">9f4f3ce209</a>)</li>
<li>Improved vtkMRMLSegmentationNode documentation (<a href="https://github.com/Slicer/Slicer/commit/4f11f2c511">4f11f2c511</a>)</li>
<li>Clarified how to add more Python files to a scripted module (<a href="https://github.com/Slicer/Slicer/commit/2083046565">2083046565</a>)</li>
<li><a href="https://slicer.readthedocs.io/en/5.2/developer_guide/slicer.html#slicer.util.launchConsoleProcess">Added usage example to slicer.util.launchConsoleProcess &amp; logProcessOutput docstring</a></li>
<li>Updated extension installation code snippet (<a href="https://github.com/Slicer/Slicer/commit/680cd38345">680cd38345</a>)</li>
<li>Added information on <a href="https://slicer.readthedocs.io/en/5.2/developer_guide/build_instructions/windows.html#windows">build time and disk space need on Windows</a></li>
<li>Added “<a href="https://slicer.readthedocs.io/en/5.2/developer_guide/build_instructions/windows.html?highlight=decide%20between#set-up-source-and-build-folders">How to decide between Debug and Release mode?</a>” to Windows build instructions</li>
<li>Added “<a href="https://slicer.readthedocs.io/en/5.2/developer_guide/build_instructions/windows.html#custom-slicer-and-ctk-widgets-do-not-show-up-in-qt-designer">Custom Slicer and CTK widgets do not show up in Qt designer</a>” to common build errors section</li>
</ul>
</li>
<li>Markups
<ul>
<li>Added <a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/markups.html#creating-template-landmarks">Creating Template Landmarks</a>, <a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/markups.html#plane-settings-section">Plane settings</a> and <a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/markups.html#export-import-table-section">Export/Import Table</a> sections</li>
<li>Updated <a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/markups.html#display-section">Display</a>, <a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/markups.html#control-points-section">Control points</a> and <a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/markups.html#measurements-section">Measurements</a> sections</li>
</ul>
</li>
<li>Volume Rendering
<ul>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/volumerendering.html#limitations">Document limited rendering techniques in multi-volume rendering</a></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/volumerendering.html?highlight=TDR%20error#limitations">Added info to help address Timeout detection and recovery (TDR) errors on Windows</a></li>
</ul>
</li>
</ul>
<h2 id="heading--improved-modules">Improved Modules</h2>
<h3 id="heading--dicom">DICOM</h3>
<ul>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/dicom.html?highlight=drop-down%20menu#dicom-import">Allow choosing between add link/copy when importing DICOM files</a>: The copy option is now offered in a drop-down menu of the “Import DICOM files” button. The DICOM browser stores the selected value persistently in the application settings.</li>
<li><a href="https://discourse.slicer.org/t/distorted-malaligned-volumes-after-loading-dicom-sets/26088/8">Regularize acquisition geometry by default for DICOM image loading</a>. Since it has proven to work well over the past several years (it allows loading unusual image geometries correctly and does not seem to result in extra complications), it is now enabled by default.</li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database">Simplify scene export to Slicer Data Bundle (SDB) DICOM file</a>: Allows exporting an SDB DICOM file without a reference DICOM file. A simple template adapted from DCMTK is used as a basis for the export. (<a href="https://github.com/Slicer/Slicer/commit/f4656392f9">f4656392f</a>)</li>
<li>Make it easier to export multiple series under the same DICOM study by ensuring automatically created patient and study items have valid IDs. (<a href="https://github.com/Slicer/Slicer/commit/899e36a25a">899e36a25</a>)</li>
<li>Fixed DICOM tags saving in subject hierarchy: When no series-level tags were required for any of the exportables then modifications to patient and study level tags were not saved. (<a href="https://github.com/Slicer/Slicer/commit/4df0251fbc">4df0251fb</a>)</li>
</ul>
<h3 id="heading--markups">Markups</h3>
<ul>
<li>Fixed control point state not updated with hidden coordinates (<a href="https://github.com/Slicer/Slicer/pull/6657">PR-6657</a>)</li>
<li>Fixed bug in closed curve resampling (<a href="https://github.com/Slicer/Slicer/pull/6566">PR-6566</a>)</li>
<li>Added methods to markup line node for annotation ruler compatibility (<a href="https://github.com/Slicer/Slicer/pull/6557">PR-6557</a>)</li>
<li>Replaced deprecated markups API usage (<a href="https://github.com/Slicer/Slicer/pull/6641">PR-6641</a>)</li>
</ul>
<h3 id="heading--segmentations">Segmentations</h3>
<ul>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/data_loading_and_saving.html?highlight=ITK-Snap#other">Added support for reading ITK-Snap label description file</a></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/developer_guide/script_repository.html#load-a-3d-image-or-model-file-as-segmentation">Made it more convenient to load segmentations with custom color table in Python</a></li>
<li>Exposed segment conversion paths in Python. See <a href="https://github.com/Slicer/Slicer/blob/5.2/Modules/Loadable/Segmentations/Testing/Python/SegmentationsModuleTest1.py#L176-L222">ConvertBetweenRepresentations</a> test and added class <a href="https://apidocs.slicer.org/v5.2/classvtkSegmentationConversionPath.html">vtkSegmentationConversionPath</a> and <a href="https://apidocs.slicer.org/v5.2/classvtkSegmentationConversionParameters.html">vtkSegmentationConversionParameters</a> (<a href="https://github.com/Slicer/Slicer/pull/6507">PR-6507</a>)</li>
<li><a href="https://discourse.slicer.org/t/erase-using-a-segment-as-only-editable-area/20519/13">Updated scissors “Apply to visible segments” label</a>: The label was misleading, since enabling it caused the scissors effect to only apply on all visible segments. Changed label from “Apply to all segments” to “Apply to visible segments”.</li>
<li>Enabled GrowCut remote module in ITK (<a href="https://github.com/Slicer/Slicer/pull/5807">PR-5807</a>)</li>
<li>Fixed joint smoothing in Segment Editor (<a href="https://github.com/Slicer/Slicer/pull/6694">PR-6694</a>)</li>
<li>Fixed crash when exporting segment model node (<a href="https://github.com/Slicer/Slicer/pull/6614">PR-6614</a>)</li>
</ul>
<h3 id="heading--subject-hierarchy">SubjectHierarchy</h3>
<ul>
<li>Fixed warning <code>GetChildByPositionUnderParent: Failed to find subject hierarchy item under parent...</code> when setting item parent or moving an item to be the last item in a subject hierarchy folder (<a href="https://github.com/Slicer/Slicer/commit/a9cb8f63ff">a9cb8f63ff</a>)</li>
</ul>
<h3 id="heading--surface-toolbox">Surface ToolBox</h3>
<ul>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/surfacetoolbox.html#uniform-remeshing">Updated Surface Toolbox to add uniform remeshing (ACVD) option</a>. This resampling typically provides higher quality meshes than decimation, with similar computation time.</li>
</ul>
<h3 id="heading--webserver">WebServer</h3>
<ul>
<li>Updated <a href="https://pypi.org/project/slicerio">slicerio python package</a> for using 3D Slicer via its web API.</li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/webserver.html#get-system-version">Added GET /system/version method</a>: Version query can be used to check if an appropriate Slicer version is running.</li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/webserver.html#mrml-data-access">Added /mrml methods</a>:
<ul>
<li><code>GET /mrml[/(ids|names|properties|file)]</code> methods may be used to get node id or name lists, name properties, and the node content into a local file.</li>
<li><code>POST /mrml</code> method may be used to load a file from a local path (or remote URL) into the scene.</li>
<li><code>DELETE /mrml</code> method may be used to delete data in the scene.</li>
</ul>
</li>
<li>Updated <code>browse.html</code> adding a slicer button to the OHIF toolbar to allow starting Slicer on a remote computer via a web browser (<a href="https://github.com/Slicer/Slicer/pull/6559">PR-6559</a>)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da1df354e8087a626bee4b03b3afbcd365252238.png" data-download-href="/uploads/short-url/v7yfWPe5Z5bfbSk8D9sFkeAygVW.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da1df354e8087a626bee4b03b3afbcd365252238_2_345x146.png" alt="image" data-base62-sha1="v7yfWPe5Z5bfbSk8D9sFkeAygVW" width="345" height="146" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da1df354e8087a626bee4b03b3afbcd365252238_2_345x146.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da1df354e8087a626bee4b03b3afbcd365252238_2_517x219.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da1df354e8087a626bee4b03b3afbcd365252238_2_690x292.png 2x" data-dominant-color="06090E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1518×646 83.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li><a href="https://slicer.readthedocs.io/en/5.2/user_guide/modules/webserver.html?highlight=CORS#panels-and-their-use">Made Cross Origin Resource Sharing (CORS) optional</a> (<a href="https://github.com/Slicer/Slicer/pull/6569/files">PR-6569</a>)</li>
<li>Added Web Server API to reload storable node (<a href="https://github.com/Slicer/Slicer/commit/cca6ea5107">cca6ea5107</a>)</li>
<li>Improved DICOMweb support
<ul>
<li>Improved DICOMweb server compatibility in importFromDICOMWeb (<a href="https://github.com/Slicer/Slicer/pull/6547">PR-6547</a>)</li>
<li>Implemented instance retrieval in DICOMweb request handler (<a href="https://github.com/Slicer/Slicer/pull/6547">PR-6547</a>)</li>
<li>Simplified URL for browsing the DICOM database content (<a href="https://github.com/Slicer/Slicer/commit/5e3c81627e">5e3c81627</a>)</li>
<li>Made DICOM request handler in WebServer more robust (<a href="https://github.com/Slicer/Slicer/pull/6633">PR-6633</a>)</li>
</ul>
</li>
</ul>
<h3 id="heading--volumes">Volumes</h3>
<ul>
<li>Made <a href="https://slicer.readthedocs.io/en/5.2/developer_guide/slicer.html#slicer.util.updateVolumeFromArray">slicer.util.updateVolumeFromArray</a> accept a 2D array as input (<a href="https://github.com/Slicer/Slicer/commit/1b024a3c0a">1b024a3c0a</a>)</li>
<li>Fixed warning message when entering Volumes module: <code>ctkDoubleRangeSlider::setSingleStep( 0.0001 ) is outside of valid bounds.</code> warning was logged once during initialization of the widget. (<a href="https://github.com/Slicer/Slicer/commit/37711246e2">37711246e</a>)</li>
</ul>
<h3 id="heading--sequence">Sequence</h3>
<ul>
<li>Updated MultiVolumeImporter to add acquisition attributes to volume sequences node. (<a href="https://github.com/Slicer/Slicer/commit/5c6a247bae">5c6a247ba</a>)</li>
</ul>
<h2><a name="p-88076-infrastructure-1" class="anchor" href="#p-88076-infrastructure-1" aria-label="Heading link"></a>Infrastructure</h2>
<h3 id="heading--continuous-integration">Continuous integration (CI)</h3>
<ul>
<li>Added “Check Commit Message” and “Check Line Length” GitHub actions workflows.</li>
<li>Fixed use of run_ctest_ variables in dashboard driver script (<a href="https://github.com/Slicer/Slicer/pull/6585">PR-6585</a>)</li>
</ul>
<h3 id="heading--release-process">Release process</h3>
<ul>
<li>Added “<a href="https://github.com/Slicer/Slicer/blob/d451cf1e2189a84211fd0bbc13e898604b72f58a/.github/ISSUE_TEMPLATE/release.md">release</a>” and “<a href="https://github.com/Slicer/Slicer/blob/d451cf1e2189a84211fd0bbc13e898604b72f58a/.github/ISSUE_TEMPLATE/patch-release.md">patch-release</a>” issue templates.</li>
</ul>
<h3 id="heading--packaging">Packaging</h3>
<ul>
<li>Updated NSIS manifest to support packaging of files with a long paths (<a href="https://github.com/Slicer/Slicer/pull/6198">PR-6198</a>)</li>
</ul>
<h3 id="heading--openxr-support">OpenXR support</h3>
<ul>
<li>Updated VTK &amp; vtkAddon to backport OpenXR and OpenXRRemoting changes. (<a href="https://github.com/Slicer/Slicer/pull/6567">PR-6567</a>)</li>
<li>Updated VTK to include OpenVR/OpenXR volume rendering fix (<a href="https://github.com/Slicer/Slicer/pull/6584">PR-6584</a>)</li>
</ul>
<h2 id="heading--dependencies">Dependencies</h2>
<ul>
<li>
<p>Updated Python wheels</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Updated</th>
<th>from</th>
<th>to</th>
</tr>
</thead>
<tbody>
<tr>
<td>setuptools</td>
<td><code>60.9.3</code></td>
<td><code>65.5.0</code></td>
</tr>
<tr>
<td>pip</td>
<td><code>22.0.3</code></td>
<td><code>22.3</code></td>
</tr>
<tr>
<td>numpy</td>
<td><code>1.22.1</code></td>
<td><code>1.23.4</code></td>
</tr>
<tr>
<td>scipy</td>
<td><code>1.8.0</code></td>
<td><code>1.9.2</code></td>
</tr>
<tr>
<td>dicomweb-client</td>
<td><code>0.54.4</code></td>
<td><code>0.57.1</code></td>
</tr>
<tr>
<td>Pillow</td>
<td><code>9.0.1</code></td>
<td><code>9.2.0</code></td>
</tr>
<tr>
<td>pyparsing</td>
<td><code>3.0.7</code></td>
<td><code>3.0.9</code></td>
</tr>
<tr>
<td>requests</td>
<td><code>2.27.1</code></td>
<td><code>2.28.1</code></td>
</tr>
<tr>
<td>urllib3</td>
<td><code>1.26.8</code></td>
<td><code>1.26.12</code></td>
</tr>
<tr>
<td>charset-normalizer</td>
<td><code>2.0.12</code></td>
<td><code>2.1.1</code></td>
</tr>
<tr>
<td>idna</td>
<td><code>3.3</code></td>
<td><code>3.4</code></td>
</tr>
<tr>
<td>certifi</td>
<td><code>2021.10.8</code></td>
<td><code>2022.9.24</code></td>
</tr>
<tr>
<td>chardet</td>
<td><code>4.0.0</code></td>
<td><code>5.0.0</code></td>
</tr>
<tr>
<td>GitPython</td>
<td><code>3.1.27</code></td>
<td><code>3.1.29</code></td>
</tr>
<tr>
<td>PyJWT</td>
<td><code>2.3.0</code></td>
<td><code>2.5.0</code></td>
</tr>
<tr>
<td>wrapt</td>
<td><code>1.13.3</code></td>
<td><code>1.14.1</code></td>
</tr>
<tr>
<td>cffi</td>
<td><code>1.15.0</code></td>
<td><code>1.15.1</code></td>
</tr>
<tr>
<td>PyGithub</td>
<td><code>1.55</code></td>
<td><code>1.56</code></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p>Updated dependencies</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Updated</th>
<th>from</th>
<th>to</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>CTK</td>
<td><a href="https://github.com/commontk/CTK/commit/ec816cbb7">ec816cbb7</a></td>
<td><a href="https://github.com/commontk/CTK/commit/2c8953963">2c8953963</a></td>
<td>See <a href="https://github.com/commontk/CTK/compare/ec816cbb7...2c8953963">list of commits</a>.</td>
</tr>
<tr>
<td>ITK</td>
<td>5.3rc03<br><small><a href="https://github.com/Slicer/ITK/commit/46a71c744">46a71c744</a></small></td>
<td>5.3rc04-218<br><small><a href="https://github.com/Slicer/ITK/commit/be914a8b5">be914a8b5</a></small></td>
<td>See release notes for <a href="https://github.com/InsightSoftwareConsortium/ITK/releases/tag/v5.3rc03">5.3rc03</a> and <a href="https://github.com/InsightSoftwareConsortium/ITK/releases/tag/v5.3rc04">5.3rc04</a>.</td>
</tr>
<tr>
<td>VTK</td>
<td>9.1.20220125<br><small><a href="https://github.com/Slicer/VTK/commit/bccd2b8f7">Slicer/VTK@bccd2b8f7</a></small></td>
<td>9.1.20220125<br><small><a href="https://github.com/Slicer/VTK/commit/97a187572">Slicer/VTK@97a187572</a></small></td>
<td>Included backports:<br><small> - Fix empty volume crash and joint smoothing (<a href="https://github.com/Slicer/Slicer/commit/4c0f4a531082af25eff7d3392462aca458eab4a6">Slicer@4c0f4a531</a>)<br>- OpenXR and OpenXRRemoting changes (<a href="https://github.com/Slicer/Slicer/pull/6567">PR-6567</a>)<br>- OpenVR/OpenXR volume rendering fix (<a href="https://github.com/Slicer/Slicer/pull/6584">PR-6584</a>)</small></td>
</tr>
<tr>
<td>SimpleITK</td>
<td>2.2rc3<br><small><a href="https://github.com/SimpleITK/SimpleITK/commit/ffd48e274">SimpleITK/SimpleITK@ffd48e274</a></small></td>
<td>2.2.0<br><small><a href="https://github.com/SimpleITK/SimpleITK/commit/ca0c09386">SimpleITK/SimpleITK@ca0c09386</a></small></td>
<td>See release notes for <a href="https://github.com/SimpleITK/SimpleITK/releases/tag/v2.2rc3">2.2rc3</a> and <a href="https://github.com/SimpleITK/SimpleITK/releases/tag/v2.2.0">2.2.0</a></td>
</tr>
<tr>
<td>Bzip2</td>
<td>1.0.6 (Sept 2010)<br><small><a href="https://github.com/commontk/bzip2/commit/0e735f23032ececcf52ed49b27928390fff28e50">0e735f230</a></small></td>
<td>1.0.8 (July 2019)<br><small><a href="https://github.com/commontk/bzip2/commit/391dddabd24aee4a06e10ab6636f26dd93c21308">391dddabd</a></small></td>
<td>See <a href="https://sourceware.org/bzip2/CHANGES">release notes</a>.</td>
</tr>
</tbody>
</table>
</div></li>
</ul>
<h2 id="heading--extensions">Extensions</h2>
<p><em>Listed below are extensions added, removed or updated since the 5.0 release.</em></p>
<p>The Slicer<a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html"> extensions manager</a> enables Slicer users to install more than 150 extensions written and contributed by their peers from around the world.</p>
<h3 id="heading--extensions-new">New</h3>
<ul>
<li>
<p><a href="https://discourse.slicer.org/t/new-extension-fully-automatic-whole-body-ct-segmentation-in-2-minutes-using-totalsegmentator/26710">TotalSegmentator</a>: Fully automatic whole-body CT segmentation in 2 minutes using TotalSegmentator.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/617e93eec654cb6ff35149992dc535c467e0976c.jpeg" data-download-href="/uploads/short-url/dUtvoNOB71yBYoL6MZn9GgCVU84.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/617e93eec654cb6ff35149992dc535c467e0976c_2_517x282.jpeg" alt="image" data-base62-sha1="dUtvoNOB71yBYoL6MZn9GgCVU84" width="517" height="282" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/617e93eec654cb6ff35149992dc535c467e0976c_2_517x282.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/617e93eec654cb6ff35149992dc535c467e0976c_2_775x423.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/617e93eec654cb6ff35149992dc535c467e0976c_2_1034x564.jpeg 2x" data-dominant-color="413C39"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1050 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><a href="https://discourse.slicer.org/t/new-extension-hdbrainextraction-for-ai-based-skull-stripping/24420">HDBrainExtraction</a>: AI-based skull stripping (blanking out regions outside the brain in MRI images). The model is trained on a large set of images and proven to be more robust than many other similar tools.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe28939be7dbf32165390e73296c29dc5b82cdf1.jpeg" data-download-href="/uploads/short-url/AgodaFEzvETmfhMmp1ON6o5MhVf.jpeg?dl=1" title="HDBrainExtraction"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe28939be7dbf32165390e73296c29dc5b82cdf1_2_517x270.jpeg" alt="HDBrainExtraction" data-base62-sha1="AgodaFEzvETmfhMmp1ON6o5MhVf" width="517" height="270" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe28939be7dbf32165390e73296c29dc5b82cdf1_2_517x270.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe28939be7dbf32165390e73296c29dc5b82cdf1_2_775x405.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe28939be7dbf32165390e73296c29dc5b82cdf1_2_1034x540.jpeg 2x" data-dominant-color="6C696D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">HDBrainExtraction</span><span class="informations">1200×627 76.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Automated 3D Dental Model Segmentation and Labeling: <a href="https://github.com/DCBIA-OrthoLab/SlicerDentalModelSeg">SlicerDentalModelSeg</a> and <a href="https://github.com/DCBIA-OrthoLab/SlicerAutomatedDentalTools">SlicerAutomatedDentalTools</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d07e1744fc79f76f26a1afa0166f7efeb39214c.jpeg" data-download-href="/uploads/short-url/48OJjFIhTdUTzptdl9qiGOcMNJy.jpeg?dl=1" title="SlicerDentalModelSeg and SlicerAutomatedDentalTools"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d07e1744fc79f76f26a1afa0166f7efeb39214c_2_517x194.jpeg" alt="SlicerDentalModelSeg and SlicerAutomatedDentalTools" data-base62-sha1="48OJjFIhTdUTzptdl9qiGOcMNJy" width="517" height="194" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d07e1744fc79f76f26a1afa0166f7efeb39214c_2_517x194.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d07e1744fc79f76f26a1afa0166f7efeb39214c_2_775x291.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d07e1744fc79f76f26a1afa0166f7efeb39214c_2_1034x388.jpeg 2x" data-dominant-color="A9A79D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerDentalModelSeg and SlicerAutomatedDentalTools</span><span class="informations">2420×910 410 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><a href="https://github.com/gaoyi/SlicerBigImage">SlicerBigImage</a>: Add support for large scale microscopic image viewing and computing.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a97b0a947a7ce7e40fd92ca81d1ae3696bb27895.jpeg" data-download-href="/uploads/short-url/obij3oFDjPaiohT4K05eCRL0nuB.jpeg?dl=1" title="SlicerBigImage"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a97b0a947a7ce7e40fd92ca81d1ae3696bb27895_2_517x281.jpeg" alt="SlicerBigImage" data-base62-sha1="obij3oFDjPaiohT4K05eCRL0nuB" width="517" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a97b0a947a7ce7e40fd92ca81d1ae3696bb27895_2_517x281.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a97b0a947a7ce7e40fd92ca81d1ae3696bb27895_2_775x421.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a97b0a947a7ce7e40fd92ca81d1ae3696bb27895_2_1034x562.jpeg 2x" data-dominant-color="E7D1E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerBigImage</span><span class="informations">1386×754 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><a href="https://github.com/ChenXiang96/SlicerColoc-Z-Stats">SlicerColoc-Z-Stats</a>: Computing proteins’ colocalization (spatial overlap between different channels) of Z-stack images.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f560d62af447cc0d93abf71b86d61aaa1eb4f76e.jpeg" data-download-href="/uploads/short-url/z0Is0lB02Wbeo4GFzkvvlAOYI58.jpeg?dl=1" title="SlicerColoc-Z-Stats"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f560d62af447cc0d93abf71b86d61aaa1eb4f76e_2_517x263.jpeg" alt="SlicerColoc-Z-Stats" data-base62-sha1="z0Is0lB02Wbeo4GFzkvvlAOYI58" width="517" height="263" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f560d62af447cc0d93abf71b86d61aaa1eb4f76e_2_517x263.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f560d62af447cc0d93abf71b86d61aaa1eb4f76e_2_775x394.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f560d62af447cc0d93abf71b86d61aaa1eb4f76e_2_1034x526.jpeg 2x" data-dominant-color="8E8E95"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerColoc-Z-Stats</span><span class="informations">1920×978 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><a href="https://github.com/ALive-research/Slicer-Liver">SlicerLiver</a>: Provide tools for analysis, quantification and therapy planning for hepatic interventions.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b007c6473a98feef0b93a6c5f4323e200ea6850.jpeg" data-download-href="/uploads/short-url/8pXd8c2nfAteeOKcp09TinPLhde.jpeg?dl=1" title="SlicerLiver"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b007c6473a98feef0b93a6c5f4323e200ea6850_2_517x291.jpeg" alt="SlicerLiver" data-base62-sha1="8pXd8c2nfAteeOKcp09TinPLhde" width="517" height="291" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b007c6473a98feef0b93a6c5f4323e200ea6850_2_517x291.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b007c6473a98feef0b93a6c5f4323e200ea6850_2_775x436.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b007c6473a98feef0b93a6c5f4323e200ea6850_2_1034x582.jpeg 2x" data-dominant-color="B5B5D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerLiver</span><span class="informations">1280×720 59.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><a href="https://github.com/PerkLab/SlicerSkinMouldGenerator">SkinMouldGenerator</a>: 3D Slicer extension for generating 3D-printable HDR Brachytherapy applicator to be used in the treatment of skin cancer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73e9cca5d0228c8f61f54df41976cfbe51d530ef.jpeg" data-download-href="/uploads/short-url/gxpOXPDQ50IdHOn2F9FF89nLzcz.jpeg?dl=1" title="SkinMouldGenerator"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73e9cca5d0228c8f61f54df41976cfbe51d530ef_2_517x315.jpeg" alt="SkinMouldGenerator" data-base62-sha1="gxpOXPDQ50IdHOn2F9FF89nLzcz" width="517" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73e9cca5d0228c8f61f54df41976cfbe51d530ef_2_517x315.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73e9cca5d0228c8f61f54df41976cfbe51d530ef_2_775x472.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/73e9cca5d0228c8f61f54df41976cfbe51d530ef_2_1034x630.jpeg 2x" data-dominant-color="768974"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SkinMouldGenerator</span><span class="informations">1200×732 37 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><a href="https://github.com/HOA-2/SlicerNeuroSegmentation">SlicerNeuroSegmentation</a>: Provide access to tools for segmenting neurological structures.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b62e2739f9f2fb60869e8c710b56c3ed501b19dc.jpeg" data-download-href="/uploads/short-url/pZDMvLxmQkfgtLCqUK091nMqHJW.jpeg?dl=1" title="SlicerNeuroSegmentation"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b62e2739f9f2fb60869e8c710b56c3ed501b19dc_2_517x312.jpeg" alt="SlicerNeuroSegmentation" data-base62-sha1="pZDMvLxmQkfgtLCqUK091nMqHJW" width="517" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b62e2739f9f2fb60869e8c710b56c3ed501b19dc_2_517x312.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b62e2739f9f2fb60869e8c710b56c3ed501b19dc_2_775x468.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b62e2739f9f2fb60869e8c710b56c3ed501b19dc_2_1034x624.jpeg 2x" data-dominant-color="8F8B8B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerNeuroSegmentation</span><span class="informations">1920×1160 294 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><a href="https://github.com/KitwareMedical/SlicerMarkupConstraints">SlicerMarkupConstraints</a>: Enable Slicer extension developers to constrain and synchronize markups and control points of different nodes.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th><img src="https://github.com/KitwareMedical/SlicerMarkupConstraints/raw/main/Docs/project-anchor.gif" alt="Show line of projection to an axis" width="640" height="480"></th>
<th><img src="https://github.com/KitwareMedical/SlicerMarkupConstraints/raw/main/Docs/project-angle.gif" alt="Show mixture of arbitrary markup nodes" width="640" height="480"></th>
<th><img src="https://github.com/KitwareMedical/SlicerMarkupConstraints/raw/main/Docs/length-chain.gif" alt="Chain of fixed distance constraints on multiple line nodes" width="640" height="480"></th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Show line of projection to an axis</em></td>
<td><em>Show mixture of arbitrary markup nodes</em></td>
<td><em>Chain of fixed distance constraints on multiple line nodes</em></td>
</tr>
</tbody>
</table>
</div></li>
</ul>
<h3 id="heading--extensions-updated">Updated</h3>
<p>All the existing extensions have been maintained and updated to account for API and build environment changes.</p>
<h3 id="heading--extensions-removed">Removed</h3>
<p>Between Slicer 5.0 and Slicer 5.2, no extensions were removed.</p>
<p>List of archived extensions is documented at<a href="https://github.com/Slicer/ExtensionsIndex/blob/main/ARCHIVE/README.md"> Slicer/ExtensionsIndex/ARCHIVE/README.md</a></p>

---
