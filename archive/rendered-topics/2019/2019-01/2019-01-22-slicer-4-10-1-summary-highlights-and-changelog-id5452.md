# Slicer 4.10.1: Summary, Highlights and Changelog

**Topic ID**: 5452
**Date**: 2019-01-22
**URL**: https://discourse.slicer.org/t/slicer-4-10-1-summary-highlights-and-changelog/5452

---

## Post #1 by @jcfr (2019-01-22 18:05 UTC)

<h1><a name="p-20095-table-of-contents-1" class="anchor" href="#p-20095-table-of-contents-1" aria-label="Heading link"></a>Table of Contents</h1>
<ul>
<li><a href="#heading--summary">Summary</a></li>
<li><a href="#heading--highlights">Highlights</a></li>
<li><a href="https://discourse.slicer.org/t/slicer-4-10-1-summary-highlights-and-changelog/5452/2">Detailed Changelog</a></li>
</ul>
<h1 id="heading--summary">Summary</h1>
<p>The community of 3D Slicer developers is proud to announce that version 4.10.1 is<a href="http://download.slicer.org/"> now available for download</a>. This patch release introduces ~150 feature enhancements and bug fixes for better performance and stability. It includes a new extension as well as more than 10 improved core modules.</p>
<p>To learn about the ~500 feature enhancements and bug fixes already introduced in version 4.10, consider reading the previous post, “<a href="https://discourse.slicer.org/t/slicer-4-10-summary-highlights-and-changelog/4610">Slicer 4.10: Summary, Highlights and Changelog</a>”.</p>
<p>The development of 3D Slicer—including its numerous modules, extensions, datasets, pull requests, patches, issues reports, suggestions—is made possible by users, developers, contributors and commercial partners around the world. This development is funded by various grants and agencies. For more details, please see the 3D Slicer<a href="https://www.slicer.org/wiki/Documentation/4.x/Acknowledgments"> Acknowledgments</a> page.</p>
<p><a href="https://www.slicer.org/">slicer.org</a> is the portal to the application, training materials, and the development community.</p>
<p>The<a href="https://www.slicer.org/wiki/Documentation/4.10/Training"> Slicer Training</a> page provides a series of tutorials and data sets for training in the use of Slicer.</p>
<p><em>Please note that Slicer continues to be a research package and is not intended for clinical use. Testing of functionality is an ongoing activity with high priority, however, some features of Slicer are not fully tested.</em></p>
<h1 id="heading--highlights">Highlights</h1>
<h2 id="heading--data-module-improvements">Data module improvements</h2>
<p>Many improvements and fixes have been implemented in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Data">Data</a> and related modules. More specifically, the following were added:</p>
<ul>
<li>
<p>a jump slices option to the segment visibility menu in the Data module.</p>
</li>
<li>
<p>the ability to toggle visibility for multi-select in the Data module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21a042d0f20e89ec4d4acd2a1bd93df3352917af.png" data-download-href="/uploads/short-url/4Nt74JERTRHiJaQlePPNpPce9ob.png?dl=1" title="data_improvement_4_sh_toggle_visibility"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21a042d0f20e89ec4d4acd2a1bd93df3352917af.png" alt="data_improvement_4_sh_toggle_visibility" data-base62-sha1="4Nt74JERTRHiJaQlePPNpPce9ob" width="620" height="119"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">data_improvement_4_sh_toggle_visibility</span><span class="informations">620×119 10.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>a color column in subject hierarchy.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/2808d721d85f668e316a17e8a0e0b4a5130ad54b.png" data-download-href="/uploads/short-url/5Ia2qH0vAsYaEfXD7jdH19qMplh.png?dl=1" title="data_improvement_1_color_column"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/2808d721d85f668e316a17e8a0e0b4a5130ad54b.png" alt="data_improvement_1_color_column" data-base62-sha1="5Ia2qH0vAsYaEfXD7jdH19qMplh" width="468" height="165"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">data_improvement_1_color_column</span><span class="informations">468×165 25.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ul>
<p>Additional improvements include these:</p>
<ul>
<li>
<p>a visibility context menu action called ‘Apply color to branch’ allows overriding the color of the model nodes in the folder.</p>
</li>
<li>
<p>a folder can override branch color. This is an important step towards making subject hierarchy usable as model hierarchy.</p>
</li>
<li>
<p>an Improved transform column in subject hierarchy.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ee85c44234bffb37fb63283d366b958ae93e981.png" data-download-href="/uploads/short-url/8YvqQGpzr1406R4WGy8giFZpVhn.png?dl=1" title="data_improvement_3_transform_column"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ee85c44234bffb37fb63283d366b958ae93e981.png" alt="data_improvement_3_transform_column" data-base62-sha1="8YvqQGpzr1406R4WGy8giFZpVhn" width="211" height="117"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">data_improvement_3_transform_column</span><span class="informations">211×117 5.69 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ul>
<h2 id="heading--segmentation-improvements">Segmentation improvements</h2>
<p>Many improvements and fixes have also been implemented in <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">Segment Editor</a> and related modules. They result in the following:</p>
<ul>
<li>
<p>allow you to use a <a href="https://discourse.slicer.org/t/new-segment-editor-feature-masking-in-grow-from-seeds-effect/4978">mask with grow from seeds effect</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f66379efcc3d3624a24ccd8df8affe5efa9751d.jpeg" data-download-href="/uploads/short-url/ib1DznPDr35zNQ2rfeYp7A0fRx3.jpeg?dl=1" title="Slicer-masked-region-growing"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f66379efcc3d3624a24ccd8df8affe5efa9751d_2_690x365.jpeg" alt="Slicer-masked-region-growing" data-base62-sha1="ib1DznPDr35zNQ2rfeYp7A0fRx3" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f66379efcc3d3624a24ccd8df8affe5efa9751d_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f66379efcc3d3624a24ccd8df8affe5efa9751d_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f66379efcc3d3624a24ccd8df8affe5efa9751d_2_1380x730.jpeg 2x" data-dominant-color="ADADAF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer-masked-region-growing</span><span class="informations">1920×1018 395 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>make segmentation geometry update more robust.</p>
</li>
<li>
<p>improve automatic oversampling calculation.</p>
</li>
<li>
<p>allow segmentation without the selection of a master volume.</p>
</li>
<li>
<p>add a “Show 3D” option for segmentation auto-complete results preview.</p>
</li>
</ul>
<h2 id="heading--built-in-web-browser-improvements">Built-in web browser improvements</h2>
<ul>
<li>
<p>the improved qSlicerWebWidget allow you to directly load data from standard web sites, which may have logins and custom download forms.  This functionality is being used as a building block for the new <a href="https://slicermorph.github.io/">SlicerMorph</a> project to build improved analysis tools for biological specimens.  A demo of the functionality is available <a href="https://www.youtube.com/watch?v=t8Dj3rOmt78&amp;feature=youtu.be">here</a>.  Improvements also enable the evaluation of web-page JavaScript code from C++ or Python, or the evaluation of Slicer Python from the page’s JavaScript as shown in <a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/WebEngine.py#L142-L225">the WebEngine test code</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b55a614761c484341cc7e549c7a31857f4a936e7.jpeg" data-download-href="/uploads/short-url/pSk3KaEhv4LkuzIz7aAdGR7z4l9.jpeg?dl=1" title="image_2"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b55a614761c484341cc7e549c7a31857f4a936e7_2_421x500.jpeg" alt="image_2" data-base62-sha1="pSk3KaEhv4LkuzIz7aAdGR7z4l9" width="421" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b55a614761c484341cc7e549c7a31857f4a936e7_2_421x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b55a614761c484341cc7e549c7a31857f4a936e7_2_631x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b55a614761c484341cc7e549c7a31857f4a936e7_2_842x1000.jpeg 2x" data-dominant-color="C5C5CD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image_2</span><span class="informations">1362×1616 581 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ul>
<h2 id="heading--compressed-video-support">Compressed video support</h2>
<ul>
<li>
<p>a new infrastructure has been added for the management of compressed video frames. Extensions can implement and register their own video compression codecs for decoding and encoding frames. The <a href="https://github.com/IGSIO/SlicerIGSIO">SlicerIGSIO </a>extension provides an example of codec registration with VP9, as well as support for both compressed video recording/replay and MKV loading/saving.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24d5ccb7e3e15e580bfe12f15be4e40f045d0e41.png" data-download-href="/uploads/short-url/5fRfF9bKxxLQ3xQJEBOJs2WHK01.png?dl=1" title="slicer-video-compression"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24d5ccb7e3e15e580bfe12f15be4e40f045d0e41_2_690x232.png" alt="slicer-video-compression" data-base62-sha1="5fRfF9bKxxLQ3xQJEBOJs2WHK01" width="690" height="232" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24d5ccb7e3e15e580bfe12f15be4e40f045d0e41_2_690x232.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24d5ccb7e3e15e580bfe12f15be4e40f045d0e41.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24d5ccb7e3e15e580bfe12f15be4e40f045d0e41.png 2x" data-dominant-color="E0EAE5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer-video-compression</span><span class="informations">998×336 36 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ul>

---

## Post #2 by @jcfr (2019-01-22 18:05 UTC)

<h1 id="heading--changelog">Changelog</h1>
<ul>
<li>
<a href="#heading--core">Core</a>
<ul>
<li><a href="#heading--fixes">Fixes</a></li>
<li><a href="#heading--features">Features</a></li>
<li><a href="#heading--dicom">DICOM</a></li>
<li><a href="#heading--mrml">MRML</a></li>
<li><a href="#heading--io">IO</a></li>
<li><a href="#heading--python-scripting">Python Scripting</a></li>
<li><a href="#heading--testing">Testing</a></li>
<li><a href="#heading--extension-development">Extension development</a></li>
</ul>
</li>
<li>
<a href="#heading--improved-modules">Improved Modules</a>
<ul>
<li><a href="#heading--colors">Colors</a></li>
<li><a href="#heading--data--subject-hierarchy">Data / Subject Hierarchy</a></li>
<li><a href="#heading--landmarkregistration">LandmarkRegistration</a></li>
<li><a href="#heading--markups">Markups</a></li>
<li><a href="#heading--multivolumeimporter">MultiVolumeImporter</a></li>
<li><a href="#heading--screencapture">ScreenCapture</a></li>
<li><a href="#heading--segment-editor">Segment Editor</a></li>
<li><a href="#heading--segmentation">Segmentation</a></li>
<li><a href="#heading--segmentstatistics">SegmentStatistics</a></li>
<li><a href="#heading--terminologies">Terminologies</a></li>
<li><a href="#heading--vectortoscalarvolume">VectorToScalarVolume</a></li>
<li><a href="#heading--volume-rendering">Volume Rendering</a></li>
<li><a href="#heading--editor-deprecated">Editor (deprecated)</a></li>
</ul>
</li>
<li>
<a href="#heading--infrastructure">Infrastructure</a>
<ul>
<li>
<a href="#heading--dependencies">Dependencies</a>
<ul>
<li><a href="#heading--vtk">VTK</a></li>
<li><a href="#heading--itk">ITK</a></li>
</ul>
</li>
<li>
<a href="#heading--custom-slicer-application-support">Custom Slicer application support</a>
<ul>
<li><a href="#heading--slicer-application">Slicer Application</a></li>
<li><a href="#heading--build-system">Build-System</a></li>
</ul>
</li>
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
<h2 id="heading--core">Core</h2>
<h3 id="heading--fixes">Fixes</h3>
<ul>
<li>
<p>Fix 3D picking in displayable managers. [<a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27517" rel="nofollow noopener">Commit</a>].</p>
</li>
<li>
<p>Update crosshair RAS position when slice is moved. Crosshair RAS position was only updated from XYZ when mouse position was updated. This caused DataProbe to show outdated RAS position when slice position was updated without moving the mouse pointer (using mouse wheel or keyboard shortcuts).</p>
</li>
<li>
<p>Change default colormap for model scalars and transforms to Viridis. Viridis provides continuous transition, so there are no specific iso-values that are displayed more prominently. Due to this, viridis seems to be a more generic colormap, which seems more suitable as a default colormap than rainbow. [<a href="https://github.com/Slicer/Slicer/pull/989" rel="nofollow noopener">PR</a>]</p>
</li>
<li>
<p>Set associated node for fiducial on volume. The associated node ID for for a markup fiducial was being set when selecting a model, but not when selecting a volume. [<a href="https://discourse.slicer.org/t/vtkmrmlmodeldisplayablemanager-issue/4709/2">Discussion</a>]</p>
</li>
<li>
<p>Ensure mouse mode icon is always visible when placing annotations.</p>
</li>
<li>
<p>Ensure slice interactor style “OnMouseWheelBackward” respect Zoom action.</p>
</li>
<li>
<p>Re-factor DataProbe, CompareVolumes,LandmarkRegistration to use ScriptedLoadableModule base classes.</p>
</li>
<li>
<p>Improve error reporting in vtkOpenGLShaderComputation. This helps for debugging framebuffer attachment issues.</p>
</li>
<li>
<p>Reduce minimum size of module settings panel. On some computers, module settings panel was too tall and the “Reset” button was not visible after adding an additional module path and restart hint appeared.</p>
</li>
</ul>
<h3 id="heading--features">Features</h3>
<ul>
<li>
<p>Improve qSlicerWebWidget [<a href="https://github.com/Slicer/Slicer/pull/1071" rel="nofollow noopener">PR</a>]</p>
<ul>
<li>Improve JavaScript interoperability.</li>
<li>Allow to directly load data from standard websites, which may have logins and custom download forms.</li>
<li>Enable the evaluation of webpage JavaScript code from C++ or Python or the evaluation of Slicer Python from the page’s JavaScript.</li>
<li>Improve download options and control</li>
</ul>
</li>
</ul>
<h3 id="heading--dicom">DICOM</h3>
<ul>
<li>
<p>Fixes</p>
<ul>
<li>
<p>Fix multiple loading of DICOM files. The mechanism that ensured that a single DICOM plugin offers only one loadable selected by default was broken and therefore sometimes multiple nodes were loaded from the same set of files.</p>
</li>
<li>
<p>Reduce warning logs during DICOM import.</p>
</li>
<li>
<p>Fix cutoff in DICOM browser toolbar on Windows.</p>
</li>
<li>
<p>Fix scalar volume DICOM export.</p>
</li>
<li>
<p>Add check for non-ASCII characters when drag-and-dropping a DICOM folder. User is informed that importing from that folder may not work but he can still continue. The test is only performed when the folder is drag-and-dropped to the application window.</p>
</li>
<li>
<p>Precache image size DICOM tags. Precaching the rows and columns tags are necessary to show the image size in the DICOM browser.</p>
</li>
<li>
<p>Fix ForceSamePatientNameIdInEachDirectory rule in DICOMPatcher and fix “error global name ‘patientIndex’ is not defined”.</p>
</li>
</ul>
</li>
<li>
<p>Features</p>
<ul>
<li>
<p>Update DCMTK to fix DICOM TR support for along-track measurements.</p>
</li>
<li>
<p>Allow specifying study, series, content datetime for DICOM image export. It was not possible to export 4D data sets, because study, series, frame of reference UIDs were always generated and it was not possible to set content time (to distinguish between image frames at the same spatial position at different time points). Now study, series, frame of reference UIDs can be specified optionally and study, series, content date&amp;time can be set.</p>
</li>
</ul>
</li>
</ul>
<h3 id="heading--mrml">MRML</h3>
<ul>
<li>
<p>Fixes</p>
<ul>
<li>
<p>Fix default display and storage node creation. The CreateDefaultDisplayNodes and CreateDefaultStorageNode functions did not use the CreateNewNodeByClass infrastructure so default nodes were not considered. This has been fixed in all node classes using such functions.</p>
</li>
<li>
<p>Fix error message “AddMRMLDisplayableManagerEvent - eventId:16004 already added”</p>
</li>
</ul>
</li>
<li>
<p>Features</p>
<ul>
<li>
<p>Add option to get directly referenced nodes. GetReferencedNodes and AddReferencedNodes always collected the referenced nodes recursively. An argument has been added to these functions for turning off the recursive functioning to only get the nodes that directly reference the argument node. This should not break anything because the default value for the argument is true (recursive).</p>
</li>
<li>
<p>Add MRMLSliceNode property to allow show/hide of reformat widget outline.</p>
</li>
<li>
<p>Add support for associating view with specific interaction node. It adds support for adding an interaction node reference to view. By default, all views are implicitly associated with the interaction singleton node. This allows to explicitly associate a subset of the views with a particular interaction node. Widgets expecting to work with an interaction node have also been updated to have interactionNode()/setInteractionNode() functions allowing to override the default interaction node. [<a href="https://discourse.slicer.org/t/setting-mouse-place-mode-for-specific-view/4938">Discussion</a>]</p>
</li>
</ul>
</li>
</ul>
<h3 id="heading--io">IO</h3>
<ul>
<li>
<p>Allow loading .obj file as segmentation.</p>
</li>
<li>
<p>Track file compression by node, add compression options to save dialog. [<a href="https://github.com/Slicer/Slicer/pull/1035" rel="nofollow noopener">PR</a>, <a href="https://github.com/Slicer/Slicer/pull/1038" rel="nofollow noopener">PR</a>, <a href="https://discourse.slicer.org/t/how-to-unset-default-compress-option-during-save/4488/18">Discussion</a>]</p>
</li>
<li>
<p>New infrastructure has been added for the management of compressed video frames. Extensions can implement and register their own video compression codecs for decoding and encoding frames. The <a href="https://github.com/IGSIO/SlicerIGSIO" rel="nofollow noopener">SlicerIGSIO </a>extension provides an example of codec registration with VP9, as well as support for both compressed video recording/replay and MKV loading/saving. [<a href="https://github.com/Slicer/Slicer/pull/1028" rel="nofollow noopener">PR</a>]</p>
<ul>
<li>
<p>vtkMRMLStreamingVolumeNode: Stores both compressed frames and uncompressed images. Decodes compressed frames into images and images to frames if requested using vtkStreamingVolumeCodec</p>
</li>
<li>
<p>vtkStreamingVolumeCodec: Handles encoding and decoding of images.</p>
</li>
<li>
<p>vtkStreamingVolumeFrame: Stores compressed frame data along with the necessary information required to decode it (link to previous frame, uncompressed image size, codec FourCC, etc.).</p>
</li>
<li>
<p>Adds a framework for specifying different preset levels of compression in vtkMRMLStorageNode.</p>
</li>
</ul>
</li>
<li>
<p>Fix FreeSurfer surface reader.</p>
</li>
</ul>
<h3 id="heading--python-scripting">Python Scripting</h3>
<ul>
<li>
<p>Add methods to access view controllers in plot and table widgets.</p>
</li>
<li>
<p>Make view controller widget components more accessible. Add Python wrapping and exposed a few buttons of slice and view controller widgets. This allows fine-tuning appearance of view controllers in custom applications.</p>
</li>
</ul>
<h3 id="heading--testing">Testing</h3>
<ul>
<li>
<p>Relocation of test data and binary dependencies to GitHub</p>
<ul>
<li>
<a href="https://github.com/Slicer/SlicerTestingData" rel="nofollow noopener">Test data</a> and <a href="https://github.com/Slicer/SlicerBinaryDependencies" rel="nofollow noopener">binary dependencies</a> are now stored as release assets in Github repositories in the Slicer organization.</li>
</ul>
</li>
<li>
<p>Improvements to the SampleData module and test data infrastructure .[<a href="https://discourse.slicer.org/t/improving-testing-data-management-for-self-test/5014">Discussion</a>]</p>
<ul>
<li>
<p>New download API decouples downloading from loading into Slicer.</p>
</li>
<li>
<p>Improve SampleData API to support scene loading and zip file download.</p>
</li>
</ul>
</li>
<li>
<p>Improve test run speed [<a href="https://github.com/Slicer/Slicer/pull/1053" rel="nofollow noopener">PR</a>]</p>
<ul>
<li>2x to 10x faster for running Python tests.</li>
</ul>
</li>
<li>
<p>Re-factor scripted module tests to use ScriptedLoadableModule base classes.</p>
</li>
</ul>
<h3 id="heading--extension-development">Extension development</h3>
<ul>
<li>
<p>Fixes</p>
<ul>
<li>Fix lookup of Qt5 designer executable when configuring Slicer launcher. This means ./Slicer --designer works again.</li>
</ul>
</li>
<li>
<p>Features</p>
<ul>
<li>
<p>Configure extension build-tree launcher for starting Slicer. This convenience launcher allows to start Slicer ensuring the extensions being developed (and its dependencies) are properly loaded.</p>
</li>
<li>
<p>Add template for creating scripted modules with .ui files [<a href="https://github.com/Slicer/Slicer/pull/1072" rel="nofollow noopener">PR</a>, <a href="https://discourse.slicer.org/t/workflow-that-brings-together-a-few-modules-as-tabs-in-a-unifying-parent-module/5314/14">Discussion</a>]</p>
</li>
<li>
<p>Package Qt Designer. It can be started on all platform using ./bin/SlicerDesigner. [<a href="https://discourse.slicer.org/t/workflow-that-brings-together-a-few-modules-as-tabs-in-a-unifying-parent-module/5314/11?u=jcfr">Discussion</a>]</p>
</li>
</ul>
</li>
</ul>
<h2 id="heading--improved-modules">Improved Modules</h2>
<h3 id="heading--colors">Colors</h3>
<ul>
<li>
<p>Fixes</p>
<ul>
<li>Make color scalar bar resizeable. Label text was often too small in color scalar bar (Colors module / Scalar bar / Display scalar bar) because the default width of the scalar widget was too small. Made the scalar widget resizable by drag-and-dropping the borders (before the change, only height of the widget was adjustable).</li>
</ul>
</li>
</ul>
<h3 id="heading--data--subject-hierarchy">Data / Subject Hierarchy</h3> 
<ul>
<li>
<p>Fixes:</p>
<ul>
<li>
<p>Prevent deleting scene in SH when nothing is selected</p>
<ul>
<li>In case of deletion with no selection in subject hierarchy the whole scene was deleted. This could not happen in Slicer application, but it was possible in other SH tree views set up in a way that allowed the presence of items that the proxy model rejected. For example filtering out node types that showed up because they were parents of otherwise accepted items (so their parents showed up to show their position in the tree and allow them to show in general).</li>
</ul>
</li>
<li>
<p>Fix update of imported nodes in subject hierarchy.</p>
</li>
<li>
<p>Show direct and recursive referenced nodes with slightly different color.</p>
</li>
<li>
<p>Improve SH transform delegate UI: Radio button like indication of the selected transform (or none) instead of checkbox.</p>
</li>
</ul>
</li>
<li>
<p>Features:</p>
<ul>
<li>
<p>Add jump slices option to segment visibility menu in Data module. Fix Slicer issue <a href="https://issues.slicer.org/view.php?id=4659" rel="nofollow noopener">4659</a></p>
</li>
<li>
<p>Add toggle visibility for multi-select in Data module</p>
</li>
<li>
<p>Remove subject hierarchy automatic hints. Clicking the help button still shows the hint as before.</p>
</li>
<li>
<p>Add color column and improve transform column in subject hierarchy. See <a href="https://github.com/PerkLab/SlicerOpenAnatomy/issues/4" rel="nofollow noopener">PerkLab/SlicerOpenAnatomy#4</a>, Slicer issue <a href="https://issues.slicer.org/view.php?id=4401" rel="nofollow noopener">4401</a> and  <a href="https://github.com/Slicer/Slicer/pull/1046" rel="nofollow noopener">PR</a>.</p>
<ul>
<li>
<p>Add new column for color between visibility and transform columns. It shows the color for segments, models, and markup fiducials (selected color).</p>
</li>
<li>
<p>Double-clicking the color brings up terminology selector where terminology and color can be selected. Terminology information is stored in segments as before (segment attributes), and for models and markups it is stored in MRML node attributes. When selecting a terminology type, color is overwritten but name is not by default.</p>
</li>
<li>
<p>Transform column now shows icon instead of the first few letters of the transform name. There is a separate icon for linear and deformable transforms.</p>
</li>
<li>
<p>Double-clicking the icon brings up a menu instead of a node selector that had to be clicked again.</p>
</li>
<li>
<p>Subject hierarchy reference highlights are now updated immediately after selecting a transforms, so the highlighted transform node is always correct.</p>
</li>
</ul>
</li>
<li>
<p>Add opacity plugin to subject hierarchy. The opacity plugin adds an Opacity action in the visibility context menu with a sub-menu that contains a slider showing the opacity and which can be used to change the opacity of the item.</p>
</li>
<li>
<p>Add subject hierarchy filter by node type.</p>
<ul>
<li>
<p>Subject hierarchy can now filter items based on the node types of their associated data nodes.</p>
</li>
<li>
<p>NodeTypes is a list of MRML node class names that are accepted (including all subclasses).</p>
</li>
<li>
<p>HideChildNodeTypes list allows excluding subclasses that NodeTypes would otherwise allow.</p>
</li>
<li>
<p>Propagate new filters to SH tree view and combobox widgets.</p>
</li>
<li>
<p>Fix issue where an item was shown because of its virtual branch content although the item was rejected by a filter.</p>
</li>
</ul>
</li>
<li>
<p>Allow folder to override branch color. An important step towards making subject hierarchy usable as model hierarchy. Model hierarchy nodes have been represented as folders in subject hierarchy already, so it makes sense to use the folders for the same purpose:</p>
<ul>
<li>
<p>Folders now can have color associated to them. If it’s a mirrored model hierarchy node, then it uses the display node of the MH node, otherwise it creates a model display node associated to the folder item.</p>
</li>
<li>
<p>A visibility context menu action called ‘Apply color to branch’ allows overriding the color of the model nodes in the folder, the same way the checkbox does in the model hierarchy (the two functions are reflected in the two types of hierarchies so there is no confusion if used together).</p>
</li>
<li>
<p>Right-clicking the color column now shows the visibility context menu as color is related to visibility.</p>
</li>
</ul>
</li>
<li>
<p>Implement whitelist and blacklist for SH plugins. It is now possible to determine a subset of enabled subject hierarchy plugins for each subject hierarchy tree and combobox. See <a href="https://github.com/PerkLab/SlicerOpenAnatomy/issues/4" rel="nofollow noopener">PerkLab/SlicerOpenAnatomy#4</a></p>
<ul>
<li>
<p>Whitelist contains the enabled plugins, and if it’s not empty, then all plugins not in the list are disabled.</p>
</li>
<li>
<p>Blacklist contains the disabled plugins; all other plugins are enabled. By default both lists are empty, meaning that all plugins are enabled.</p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="heading--landmarkregistration">LandmarkRegistration</h3>
<ul>
<li>
<p>Fixes</p>
<ul>
<li>Fix issues performing landmark refinement near image borders when using the SimpleITK method.</li>
</ul>
</li>
</ul>
<h3 id="heading--markups">Markups</h3>
<ul>
<li>
<p>Fixes</p>
<ul>
<li>AddPointToNthMarkup: Fix NthMarkupModifiedEvent event call data. Similarly to other use of the event, it ensures the markupIndex is associated with the event.</li>
</ul>
</li>
</ul>
<h3 id="heading--multivolumeimporter">MultiVolumeImporter</h3>
<ul>
<li>
<p>Fixes</p>
<ul>
<li>Fix loading confidence values.</li>
</ul>
</li>
</ul>
<h3 id="heading--screencapture">ScreenCapture</h3>
<ul>
<li>
<p>Fixes</p>
<ul>
<li>Fix 3D view rendering updates during in ScreenCapture.</li>
</ul>
</li>
<li>
<p>Features</p>
<ul>
<li>Allow screen capture with transparent background. Add a check “Transparent background” checkbox.</li>
</ul>
</li>
</ul>
<h3 id="heading--segment-editor">Segment Editor</h3>
<ul>
<li>
<p>Fixes:</p>
<ul>
<li>Update level tracing on mouse wheel. This allows the level tracing effect to be updated when the user scrolls through the slices. [<a href="https://github.com/Slicer/Slicer/pull/1073" rel="nofollow noopener">PR</a>]</li>
</ul>
</li>
<li>
<p>Features:</p>
<ul>
<li>
<p>Allow using mask with grow from seeds effect [<a href="https://discourse.slicer.org/t/new-segment-editor-feature-masking-in-grow-from-seeds-effect/4978">Discussion</a>]</p>
</li>
<li>
<p>Simplify surface smoothing setting in Segment Editor.</p>
<ul>
<li>
<p>Add simple checkbox to quickly enable/disable smoothing. Smoothing factor adjustment is more accessible, too, using a slider in a sub-menu.</p>
</li>
<li>
<p>Add application setting to enable/disable segmentation surface smoothing by default.</p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="heading--segmentation">Segmentation</h3>
<ul>
<li>
<p>Features:</p>
<ul>
<li>
<p>Allow segmentation without choosing a master volume. If a volume is not available, the user can still edit a segmentation by clicking on segmentation geometry button (next to master volume selector) and specifying geometry. A blank master volume is automatically created (if no master volume was selected before).</p>
</li>
<li>
<p>Add “Show 3D” option for segmentation auto-complete results preview. Segmentation results can be previewed in 3D for auto-complete effects (Grow from seeds, Fill between slices, Watershed) by clicking “Show 3D” in “Display” line, next to the input/results opacity slider.</p>
</li>
</ul>
</li>
<li>
<p>Fixes:</p>
<ul>
<li>
<p>Fix Segment Editor to work with multi-component master volume. Segment editor expects single-component scalar volume as master volume. If a vector volume is selected as input then now the first component is used. In the future, user may be offered to choose a component or use vector magnitude.</p>
</li>
<li>
<p>Fix closed surface to labelmap conversion in segmentation. When converting closed surface representation to binary labelmap representation in segmentation, Slicer was running out of memory if physical size of the object was large. Internal labelmap extent computation was incorrect, it assumed 1.0mm spacing. Fixed by using the actual spacing value.</p>
</li>
<li>
<p>Fix segment remaining completely transparent after Threshold effect. When user changed current segment while Threshold effect was active, the segment that was originally selected remained completely transparent (invisible) after thresholding was completed. Now opacity of all segments are properly restored after preview, even if user selects a different segment during thresholding.</p>
</li>
<li>
<p>Improve automatic oversampling calculation. Relative structure size was calculated based on the volume of the whole image instead of a single voxel. With this change the size of a single voxel is considered for the RSS measure (cubic root of the ratio of the structure volume and the volume of one voxel in the reference image, i.e. the number of voxels the structure spans on average along each axis). The fuzzy sets have also been updated. This fixes the problem with very low or very high resolution images.</p>
</li>
<li>
<p>Make segmentation geometry update more robust. Models imported into segmentation (with labelmap as master representation). After that segmentation geometry was modified. This caused Slicer to crash, as GUI update was attempted before labelmap was fully initialized. Fix the problem by preventing display updates during segmentation resampling using StartModify/EndModify.</p>
</li>
</ul>
</li>
</ul>
<h3 id="heading--segmentstatistics">SegmentStatistics</h3>
<ul>
<li>
<p>Fixes</p>
<ul>
<li>
<p>Improved SegmentStatistics usability.</p>
<ul>
<li>
<p>Automatically create parameter node and select segmentation node when switching to the module.</p>
</li>
<li>
<p>Create output table automatically if none is selected.</p>
</li>
<li>
<p>Collapse advanced section by default.</p>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="heading--terminologies">Terminologies</h3>
<ul>
<li>
<p>Fixes</p>
<ul>
<li>
<p>Filter out duplicate types in terminology selector.</p>
</li>
<li>
<p>Make anatomic region expand button blink 3x.</p>
</li>
</ul>
</li>
<li>
<p>Features</p>
<ul>
<li>Highlight anatomy option in terminology selector. If the anatomic region panel is collapsed but the selected type supports anatomy information then the expand button is briefly highlighted to let the user know there are extra options available. If it’s not available then the expand button is disabled (if still collapsed) until a type is selected that supports it.</li>
</ul>
</li>
</ul>
<h3 id="heading--vectortoscalarvolume">VectorToScalarVolume</h3>
<ul>
<li>
<p>Fixes</p>
<ul>
<li>Improve VectorToScalarVolume usability. Improve input selection checks and move luminance to the top of the method combobox so that it is selected by default when the parameter node is deleted.</li>
</ul>
</li>
</ul>
<h3 id="heading--volume-rendering">Volume Rendering</h3>
<ul>
<li>
<p>Fixes</p>
<ul>
<li>
<p>Optimize volume rendering clipping plane smoothness. Default ClippedVoxelIntensity was extremely large and did not result in completely smooth surface in all cases (probably due to numerical errors).</p>
</li>
<li>
<p>Fix volume rendering ROI reset. When volume rendered node’s transform was changed, ROI was reset. This made it impossible to review clipped volume sequences or transform clipped volumes.</p>
</li>
</ul>
</li>
</ul>
<h3>Editor (deprecated)</h3>
<ul>
<li>
<p>Fixes</p>
<ul>
<li>Fix memory leak in vtkPichonFastMarching.</li>
</ul>
</li>
</ul>
<h2 id="heading--infrastructure">Infrastructure</h2>
<h3 id="heading--dependencies">Dependencies</h3>
<h4 id="heading--vtk">VTK</h4>
<ul>
<li>
<p>Update to support python wrapping of VTKRenderingOpenVR.</p>
</li>
<li>
<p>Backport to Slicer/VTK fork selected fixes. See <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27574" rel="nofollow noopener">here</a> for more details.</p>
</li>
</ul>
<h4 id="heading--itk">ITK</h4>
<ul>
<li>Future proofing for transition to ITK5 and C++11.</li>
</ul>
<h3 id="heading--custom-slicer-application-support">Custom Slicer application support</h3>
<h4 id="heading--slicer-application">Slicer Application</h4>
<ul>
<li>
<p>Make custom application version more accessible.</p>
</li>
<li>
<p>Scripted modules in custom applications can easily access application version and repository information using new methods in qSlicerCoreApplication.</p>
</li>
<li>
<p>Both Slicer core and custom application version is logged.</p>
</li>
<li>
<p>For custom applications, now the main application’s repository revision is displayed in “About dialog” (and not Slicer core’s revision).</p>
</li>
</ul>
<h4 id="heading--build-system">Build-System</h4>
<ul>
<li>
<p>Fixes</p>
<ul>
<li>
<p>Fix DEFAULT_SETTINGS_FILE support in slicerMacroBuildApplication macro.</p>
</li>
<li>
<p>Initialize revisionUserSettings using default settings. This ensures that default settings are used to initialize both userSettings and revisionUserSettings. This is particularly useful when creating slicer custom application.</p>
</li>
<li>
<p>Fix logic discovering bundled extension superbuild directory and external project names for bundled superbuild extension.</p>
</li>
<li>
<p>Document support for “SuperBuild-type” extension in <a href="https://github.com/Slicer/Slicer/blob/v4.10.1/CMakeLists.txt#L1056-L1080" rel="nofollow noopener">CMakeLists.txt</a>.</p>
</li>
</ul>
</li>
<li>
<p>Features</p>
<ul>
<li>
<p>Support excluding bundled extension external projects. Setting the variable &lt;extension_name&gt;_EXTERNAL_PROJECT_EXCLUDE_ALL to TRUE prevents Slicer build system from considering the extension dependencies. This is particularly useful when (1) an extension support to be built as both a standalone project or a Slicer extension and (2) external projects from the extension are either not needed when bundled into Slicer or conflicting with Slicer ones.</p>
</li>
<li>
<p>Support restricting list of external project dependencies for bundled extension of superbuild type. By setting “&lt;extension_name&gt;_EXTERNAL_PROJECT_DEPENDENCIES” to a list of , it allows to constrain the list of external project dependencies appended to Slicer_DEPENDENCIES. This is particularly useful when not all external projects found in an extension superbuild folder should be added as Slicer dependency.</p>
</li>
</ul>
</li>
</ul>
<h2 id="heading--extensions">Extensions</h2>
<p>The Slicer<a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager" rel="nofollow noopener"> extensions manager</a> enables Slicer users to install more than 100 extensions written and contributed by their peers from around the world.</p>
<h3 id="heading--new">New</h3>
<ul>
<li>
<a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/GeodesicSlicer" rel="nofollow noopener">GeodesicSlicer</a>: This extension calculates geodesic path in 3D structure. Moreover, thanks to this geodesic path, this module can draw an EEG 10-20 system, determine the projected scalp stimulation site (MRI guided brain stimulation without the use of a neuronavigation System) and correct the rTMS resting motor threshold by correction factor. See <a href="https://discourse.slicer.org/t/new-extension-release-geodesicslicer/5405">Announcement</a>.</li>
</ul>
<h3 id="heading--improved">Improved</h3>
<ul>
<li>
<p><a href="https://github.com/KitwareMedical/SlicerVirtualReality#slicervirtualreality" rel="nofollow noopener">SlicerVirtualReality</a></p>
<ul>
<li>
<p>Fix virtual reality picking error. When the pick position was close or inside non-selectable object, picking often failed because VTK’s cell picker found that actor. Now if a model, segmentation, or volume rendering node is not selectable. then it is completely excluded from picking.</p>
</li>
<li>
<p>Fix initialization of model displayable manager. The logic of adding actors for slice models was incorrect (not all slice models were added when all slice models were already in the scene - for example when a virtual reality view was created). Fixes <a href="https://github.com/KitwareMedical/SlicerVirtualReality/issues/33" rel="nofollow noopener">KitwareMedical/SlicerVirtualReality#33</a></p>
</li>
</ul>
</li>
</ul>

---

## Post #3 by @rkikinis (2019-01-22 18:05 UTC)

<p>Hi,</p>
<p>This is awesome. Congratulations to the leaders and the community.</p>
<p>Ron</p>

---
