# Slicer 5.10: Summary, Highlights, and Changelog

**Topic ID**: 45224
**Date**: 2025-12-03
**URL**: https://discourse.slicer.org/t/slicer-5-10-summary-highlights-and-changelog/45224

---

## Post #1 by @ebrahim (2025-12-03 22:15 UTC)

<h1><a name="p-130133-table-of-contents-1" class="anchor" href="#p-130133-table-of-contents-1" aria-label="Heading link"></a>Table of contents</h1>
<ul>
<li><a href="#heading--summary">Summary</a></li>
<li><a href="#heading--highlights">Highlights</a></li>
<li><a href="https://discourse.slicer.org/t/slicer-5-10-summary-highlights-and-changelog/45224/2">Detailed Changelog 5.10.0</a></li>
</ul>
<h1 id="heading--summary">Summary</h1>
<p>The community of 3D Slicer developers is proud to announce that version 5.10 is <a href="http://download.slicer.org/">now available for download</a>. This release consists of a few new features and a large set of fixes, enhancements, performance and usability improvments, and core library upgrades.</p>
<p>Users will find new <strong>interactive editing and display of image window/level and transfer functions</strong>, completely redesigned <strong>scene views</strong> (visual bookmarks), a new module for <strong>plotting image intensity along a line</strong>, <strong>multi-component volume rendering</strong>, storage of <strong>time sequences of color and multi-component volumes and displacement fields (up to 5D)</strong>.</p>
<p>Developers will benefit from <strong>upgrade to Python 3.12</strong>, infrastructure for <strong>unlimited number of image layers in slice views</strong>, <strong>curved planar reformat (CPR)</strong> support, <strong>TLS support for DICOM communication</strong>, and better support of the <strong>trame web framework</strong>.</p>
<p>Extensions received new modules and numerous fixes and improvements. Over <a href="https://discourse.slicer.org/t/slicer-5-10-summary-highlights-and-changelog/45224/2#heading--new">15 new extensions</a> have been added to the existing 200+ extensions.</p>
<p>Download counts of 3D Slicer continue to increase, reaching record breaking 400,000+ downloads of the application in the past 12 months, and over 2.2 million downloads of the core application and 8.8 million downloads of extensions in the past 10 years.</p>
<p>The development of 3D Slicer—including its numerous modules, extensions, datasets, pull requests, patches, issues reports, suggestions—is made possible by users, developers, contributors and commercial partners around the world. 3D Slicer is based on a stack of open-source software and we are working constantly on updating the underlying packages. This development is funded by various grants and agencies. For more details, please see the 3D Slicer <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#acknowledgments">Acknowledgments</a> page.</p>
<p>Feel free to share your insights on <a href="https://discourse.slicer.org/">Discourse</a> and explore how to contribute to the project (please, read our <a href="https://slicer.readthedocs.io/en/latest/developer_guide/contributing.html">contributing guidelines</a>). If you need help using Slicer, want to report a problem, request a feature, or share how Slicer has contributed to your work, visit our <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html">Get Help</a> section.</p>
<p><a href="https://www.slicer.org/">slicer.org</a> serves as the central hub for the application, training materials, and the development community, offering a series of tutorials and data sets through the <a href="https://slicer.readthedocs.io/en/5.10/user_guide/getting_started.html#tutorials">Slicer Tutorials</a> page.</p>
<p><em>Please note that Slicer continues to be a research package and is not intended for clinical use (clinical users must obtain the necessary ethics or regulatory approvals).</em></p>
<p><em>The <code>5.10.0</code> version was released on November 10th, 2025, under the tag <a href="https://github.com/Slicer/Slicer/tree/v5.10.0">v5.10.0</a>.  For information on prior releases, please see the <a href="https://github.com/Slicer/Slicer/wiki/Release-Details">Release Details</a> page.</em></p>
<h1 id="heading--highlights">Highlights</h1>
<ul>
<li><strong>New module: <a href="https://slicer.readthedocs.io/en/5.10/user_guide/modules/lineprofile.html">Line Profile</a></strong>, which can be used to compute intensity profile from an image along a line or curve.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fd834f26ed51f9d08ee2083967064735cacc57a.jpeg" data-download-href="/uploads/short-url/dFSA07DOABznyo0Lna1zFYrzTw6.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fd834f26ed51f9d08ee2083967064735cacc57a_2_690x338.jpeg" alt="image" data-base62-sha1="dFSA07DOABznyo0Lna1zFYrzTw6" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fd834f26ed51f9d08ee2083967064735cacc57a_2_690x338.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fd834f26ed51f9d08ee2083967064735cacc57a.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fd834f26ed51f9d08ee2083967064735cacc57a.jpeg 2x" data-dominant-color="50514D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">800×393 82 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li><a href="https://discourse.slicer.org/t/scene-views-modernization/45359"><strong>Re-engineered Scene Views</strong></a>: Scene Views are visual bookmarks to store snapshot of display settings (view layout, point of view, slice position, visibility, color, etc.) for easy review and sharing of interesting details of the scene. The feature has been available for a long time, but could not be used because it was not working reliably. It has now been completely redesigned internally to use “sequences” module for data management.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5dda82f5036e6c670290958d4ffb639d6178a775.jpeg" data-download-href="/uploads/short-url/dogyWruhDojYGI5AeQRIeODqjWZ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dda82f5036e6c670290958d4ffb639d6178a775_2_690x370.jpeg" alt="image" data-base62-sha1="dogyWruhDojYGI5AeQRIeODqjWZ" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dda82f5036e6c670290958d4ffb639d6178a775_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dda82f5036e6c670290958d4ffb639d6178a775_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5dda82f5036e6c670290958d4ffb639d6178a775_2_1380x740.jpeg 2x" data-dominant-color="747378"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1032 366 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li><a href="https://github.com/Slicer/Slicer/pull/8739"><strong>Easier interactive editing of volume rendering transfer functions</strong></a>: Users <a href="https://slicer.readthedocs.io/en/5.10/user_guide/modules/volumerendering.html#display-a-ct-or-mri-volume">can now adjust window/level directly on volume-rendered images in 3D views</a>, similar to slice views. If multiple volumes are visible, the one clicked is adjusted. Additionally, a new visibility menu checkbox, <em>Volume rendering settings follow slice views</em>, toggles synchronization of window/level, color table, and threshold settings between slice views and volume rendering.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/921d81ed1782025d3ef71c3b3a37b3e7ff3827a4.gif" alt="transfer-function" data-base62-sha1="kQAVFVZo03Ipq4NSwe4Lo4bdZXu" width="600" height="410" class="animated"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/245526ff591ef4c8d142c15b1aff865e0b7565bc.png" data-download-href="/uploads/short-url/5bpCS4uyvwTiekOlB3rVKu8yqni.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/245526ff591ef4c8d142c15b1aff865e0b7565bc_2_690x225.png" alt="image" data-base62-sha1="5bpCS4uyvwTiekOlB3rVKu8yqni" width="690" height="225" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/245526ff591ef4c8d142c15b1aff865e0b7565bc_2_690x225.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/245526ff591ef4c8d142c15b1aff865e0b7565bc_2_1035x337.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/245526ff591ef4c8d142c15b1aff865e0b7565bc_2_1380x450.png 2x" data-dominant-color="D5DBDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1749×572 47.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li><a href="https://discourse.slicer.org/t/new-feature-independent-multi-component-volume-rendering/45356"><strong>Multi-component volume rendering</strong></a>: independently render each component of multi-component volumes (such as 3D color Doppler ultrasound or multispectral microscopy images) in 3D views. A new json-based file format is introduced to store the volume rendering settings.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74d45e18c7ed4eb1c08ed65a01a28b588767cd0a.jpeg" data-download-href="/uploads/short-url/gFwnGlfBKzqhxZzFyq68QFAddto.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74d45e18c7ed4eb1c08ed65a01a28b588767cd0a.jpeg" alt="image" data-base62-sha1="gFwnGlfBKzqhxZzFyq68QFAddto" width="417" height="315"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">417×315 28.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li><a href="https://github.com/Slicer/Slicer/pull/8391"><strong>Support reading and writing 5D volumes and transforms</strong></a>: Slicer can now store 5D images and displacement fields, efficiently, in standard single NRRD file format. Supported data sets include 4D (multi-channel 3D) volumes, such as RGB color volumes, color Doppler ultrasound, multi-channel microscopy, images, and displacement fields (a.k.a. grid transforms) that are changing in time.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/832cb141e99a16940b82dea4e8352722bca97603.gif" alt="seq_of_transforms_scale50" data-base62-sha1="iIqiHELOHxIeF1L9mNGxUTnA6RB" width="624" height="492" class="animated"></li>
<li>Introduce over <a href="https://discourse.slicer.org/t/slicer-5-10-summary-highlights-and-changelog/45224/2#heading--new"><strong>15 new extensions</strong></a> that integrate advanced AI-based segmentation, improved segmentation and annotation workflows, generative modality conversion, specialized shape analysis, and more.</li>
</ul>
<h1 id="heading--developer-highlights">Developer Highlights</h1>
<ul>
<li><a href="https://github.com/Slicer/Slicer/pull/8466"><strong>Upgrade from python 3.9.10 to 3.12.10</strong></a>.</li>
<li><a href="https://github.com/Slicer/Slicer/pull/8121"><strong>TLS authentication support for DICOM Sender and Listener</strong></a>: The DICOM storage listener in the DICOM module (available under “DICOM Networking”) now supports TLS authentication. The <code>DICOMSender</code> now calls <code>storescu</code> with the appropriate TLS arguments when the DIMSE protocol is used, ensuring secure communication.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fb322c93ae4ccee0e154edb79962a2575d0a48e.png" alt="image" data-base62-sha1="6NYeKL19PVtNeRD7dlzb9DMRT66" width="577" height="96"></li>
<li><strong>Infrastructure updates toward supporting Qt6 integration</strong>, including <a href="https://github.com/Slicer/Slicer/issues/6388#issuecomment-3050603759">over 20 PRs updating CTK</a>, <a href="https://github.com/Slicer/Slicer/issues/6388#issuecomment-3133856664">over 20 PRs updating AppLauncher</a>, and <a href="https://github.com/Slicer/Slicer/issues/6388#issuecomment-3084596642">many more PRs updating other dependencies such as PythonQt</a>. Slicer 5.10 is a stable release and still builds with Qt 5.15.2, with the infrastructure available to enable Qt6 in future nightly releases and the next stable release.</li>
<li><a href="https://github.com/Slicer/Slicer/pull/8210"><strong>Groundwork to support blending an arbitrary number of layers in Slice views</strong></a>: The classes <code>vtkMRMLSliceLogic</code> and <code>vtkMRMLSliceCompositeNode</code> have been refactored to provide an API that enables managing and blending multiple layers. The API is now in place to support future integration into the GUI.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/2096fb799e94a4b57174258316c59aad3fe00df5.jpeg" data-download-href="/uploads/short-url/4EiKWEeVdqvSJjLIJC3lMUOU10h.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2096fb799e94a4b57174258316c59aad3fe00df5_2_690x183.jpeg" alt="image" data-base62-sha1="4EiKWEeVdqvSJjLIJC3lMUOU10h" width="690" height="183" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2096fb799e94a4b57174258316c59aad3fe00df5_2_690x183.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2096fb799e94a4b57174258316c59aad3fe00df5_2_1035x274.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/2096fb799e94a4b57174258316c59aad3fe00df5_2_1380x366.jpeg 2x" data-dominant-color="2B2620"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×511 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li><a href="https://github.com/Slicer/Slicer/pull/8148"><strong>Add curved planar reformatting support</strong></a>: This is made available as an API in the <code>GeneralizedReformat</code> module, not exposed to the GUI. It is used to straighten vessels, bones, or other structures for easier visualization and quantification. For example it can be used to create panoramic dental X-rays.</li>
<li><strong>Infrastructure updates toward supporting use of Slicer over the web through <a href="https://www.kitware.com/trame-slicer-announcement/">trame integration</a></strong>. trame Slicer is a bridge between the 3D Slicer core components and the trame web server, allowing web native access to 3D Slicer features.</li>
</ul>

---

## Post #2 by @jcfr (2025-12-03 22:15 UTC)

<h1 id="heading--changelog-5-10-0">Changelog: 5.10.0</h1>
<ul>
<li><a href="#heading--changelog-5100">Changelog: 5.10.0</a>
<ul>
<li><a href="#heading--core">Core</a>
<ul>
<li><a href="#heading--rendering--display">Rendering &amp; display</a></li>
<li><a href="#heading--io">IO</a></li>
<li><a href="#heading--performance">Performance</a></li>
<li><a href="#heading--fixes">Fixes</a></li>
<li><a href="#heading--application">Application</a></li>
<li><a href="#heading--extension">Extension</a></li>
<li><a href="#heading--cli">CLI</a></li>
<li><a href="#heading--scripting">Scripting</a></li>
<li><a href="#heading--internationalizationlocalization">Internationalization/Localization</a></li>
<li><a href="#heading--installation">Installation</a></li>
<li><a href="#heading--mrml">MRML</a></li>
<li><a href="#heading--api-updates">API Updates</a></li>
<li><a href="#heading--documentation">Documentation</a></li>
</ul>
</li>
<li><a href="#heading--new-modules">New Modules</a></li>
<li><a href="#heading--improved-modules">Improved Modules</a>
<ul>
<li><a href="#heading--dicom">DICOM</a></li>
<li><a href="#heading--markups">Markups</a></li>
<li><a href="#heading--models">Models</a></li>
<li><a href="#heading--generalizedreformat">GeneralizedReformat</a></li>
<li><a href="#heading--sampledata">SampleData</a></li>
<li><a href="#heading--segmentations">Segmentations</a></li>
<li><a href="#heading--sequences">Sequences</a></li>
<li><a href="#heading--terminologies">Terminologies</a></li>
<li><a href="#heading--crop-volume">Crop Volume</a></li>
</ul>
</li>
<li><a href="#heading--infrastructure">Infrastructure</a>
<ul>
<li><a href="#heading--packaging">Packaging</a></li>
<li><a href="#heading--continuous-integration-ci">Continuous integration (CI)</a></li>
<li><a href="#heading--build-system">Build system</a></li>
<li><a href="#heading--platform-support">Platform support</a></li>
<li><a href="#heading--dependencies">Dependencies</a></li>
<li><a href="#heading--custom-slicer-application-support">Custom Slicer application support</a>
<ul>
<li><a href="#heading--slicer-application">Slicer Application</a></li>
<li><a href="#heading--build-system-1">Build-System</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#heading--style">Style</a></li>
<li><a href="#heading--extensions">Extensions</a>
<ul>
<li><a href="#heading--new">New</a></li>
<li><a href="#heading--updated">Updated</a></li>
<li><a href="#heading--removed">Removed</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="#heading--changelog-5101">Changelog: 5.10.1</a>
<ul>
<li><a href="#heading--core-1">Core</a>
<ul>
<li><a href="#heading--improvements">Improvements</a></li>
<li><a href="#heading--fixes-1">Fixes</a></li>
<li><a href="#heading--documentation-1">Documentation</a></li>
</ul>
</li>
<li><a href="#heading--infrastructure-1">Infrastructure</a>
<ul>
<li><a href="#heading--packaging-1">Packaging</a></li>
<li><a href="#heading--continuous-integration-ci-1">Continuous Integration (CI)</a></li>
<li><a href="#heading--dependencies-1">Dependencies</a></li>
</ul>
</li>
<li><a href="#heading--new-contributors">New Contributors</a></li>
</ul>
</li>
</ul>
<h2 id="heading--core">Core</h2>
<h3 id="heading--rendering-display">Rendering &amp; display</h3>
<ul>
<li>Add segment visibility toggle option (<a href="https://github.com/Slicer/Slicer/pull/8247">PR-8247</a>)</li>
<li>Update VTK (vtkMultiVolume bounds computation fix) (<a href="https://github.com/Slicer/Slicer/pull/8309">PR-8309</a>)</li>
<li>Add invert colors option to Volumes module (<a href="https://github.com/Slicer/Slicer/pull/8341">PR-8341</a>)</li>
<li>Improve histogram display in Volumes module (<a href="https://github.com/Slicer/Slicer/pull/8342">PR-8342</a>)</li>
<li>Add reset ambient shading options (<a href="https://github.com/Slicer/Slicer/pull/8337">PR-8337</a>)</li>
<li>Make it easier to render large volumes on macOS (<a href="https://github.com/Slicer/Slicer/pull/8430">PR-8430</a>)</li>
<li>Add fast clipping shortcut for volume rendering (<a href="https://github.com/Slicer/Slicer/pull/8438">PR-8438</a>)</li>
<li>Match color label title font size to legend font size (<a href="https://github.com/Slicer/Slicer/pull/8668">PR-8668</a>)</li>
<li>Restore OpenGL core profile usage on Windows platform (<a href="https://github.com/Slicer/Slicer/pull/8669">PR-8669</a>)</li>
<li>Make volume rendering transfer function adjustment easier (<a href="https://github.com/Slicer/Slicer/pull/8739">PR-8739</a>)</li>
<li>Remove support for obsolete OpenGL VTK backend (<a href="https://github.com/Slicer/Slicer/pull/8249">PR-8249</a>)</li>
<li>Add support for managing and blending arbitrary number of layers in Slice viewer (<a href="https://github.com/Slicer/Slicer/pull/8210">PR-8210</a>)</li>
</ul>
<h3 id="heading--io">IO</h3>
<ul>
<li>Volume sequence IO 5D (<a href="https://github.com/Slicer/Slicer/pull/8391">PR-8391</a>)</li>
<li>Make maximum file length configurable (<a href="https://github.com/Slicer/Slicer/pull/8245">PR-8245</a>)</li>
<li>Allow reading/writing of 2 component vector volumes (<a href="https://github.com/Slicer/Slicer/pull/8732">PR-8732</a>)</li>
<li>Add support for reading/writing 2 component sequence files (<a href="https://github.com/Slicer/Slicer/pull/8772">PR-8772</a>)</li>
<li>Make vtkITKImageWriter more robust (<a href="https://github.com/Slicer/Slicer/pull/8697">PR-8697</a>)</li>
<li>Add support for storing modeling displacement field transforms (<a href="https://github.com/Slicer/Slicer/pull/8757">PR-8757</a>)</li>
<li>Save node attributes in volume and transform sequence files (<a href="https://github.com/Slicer/Slicer/pull/8762">PR-8762</a>)</li>
</ul>
<h3 id="heading--performance">Performance</h3>
<ul>
<li>Improve sequence node storage performance for simple nodes (<a href="https://github.com/Slicer/Slicer/pull/8696">PR-8696</a>)</li>
<li>Remove unnecessary threshold preview pipeline in unused views (<a href="https://github.com/Slicer/Slicer/pull/8622">PR-8622</a>)</li>
</ul>
<h3 id="heading--fixes">Fixes</h3>
<ul>
<li>Fix duplicated registration of Markups node in tests (<a href="https://github.com/Slicer/Slicer/pull/8187">PR-8187</a>)</li>
<li>Add cleanup to SegmentEditorEffect (<a href="https://github.com/Slicer/Slicer/pull/8199">PR-8199</a>)</li>
<li>Fix saving into .mrb with long node names (<a href="https://github.com/Slicer/Slicer/pull/8214">PR-8214</a>)</li>
<li>Avoid additional error message in DICOMReaders.py (<a href="https://github.com/Slicer/Slicer/pull/8215">PR-8215</a>)</li>
<li>Fix scene loading warning message (<a href="https://github.com/Slicer/Slicer/pull/8216">PR-8216</a>)</li>
<li>Fix crash in vtkSlicerApplicationLogic destructor (<a href="https://github.com/Slicer/Slicer/pull/8213">PR-8213</a>)</li>
<li>Add missing newlines and fix  indentation in <code>PrintSelf</code> (<a href="https://github.com/Slicer/Slicer/pull/8235">PR-8235</a>)</li>
<li>Do not load DWMRI volumes as sequences (<a href="https://github.com/Slicer/Slicer/pull/8242">PR-8242</a>)</li>
<li>Fix py_UtilTest on Windows (<a href="https://github.com/Slicer/Slicer/pull/8252">PR-8252</a>)</li>
<li>Fix crash in SystemTools::RemoveADirectory (<a href="https://github.com/Slicer/Slicer/pull/8250">PR-8250</a>)</li>
<li>Ensure blend pipeline is updated when setting operation Add or Subtract (<a href="https://github.com/Slicer/Slicer/pull/8233">PR-8233</a>)</li>
<li>Avoid unnecessary error message in UpdateAddSubOperation (<a href="https://github.com/Slicer/Slicer/pull/8257">PR-8257</a>)</li>
<li>Fix core IO manager initialization (<a href="https://github.com/Slicer/Slicer/pull/8287">PR-8287</a>)</li>
<li>Fix qSlicerTransformsModuleWidgetTest (<a href="https://github.com/Slicer/Slicer/pull/8291">PR-8291</a>)</li>
<li>Fix DICOM scene export (<a href="https://github.com/Slicer/Slicer/pull/8300">PR-8300</a>)</li>
<li>Show the currently selected volume rendering preset name (<a href="https://github.com/Slicer/Slicer/pull/8305">PR-8305</a>)</li>
<li>Fix 3D view bounds computation with multivolume rendering (<a href="https://github.com/Slicer/Slicer/pull/8314">PR-8314</a>)</li>
<li>Fix crash in multivolume rendering (<a href="https://github.com/Slicer/Slicer/pull/8315">PR-8315</a>)</li>
<li>Fix failing py_nomainwindow_* tests (<a href="https://github.com/Slicer/Slicer/pull/8331">PR-8331</a>)</li>
<li>Fix invalid scene view indexing (<a href="https://github.com/Slicer/Slicer/pull/8332">PR-8332</a>)</li>
<li>Call Modified if segment display properties changed during copy (<a href="https://github.com/Slicer/Slicer/pull/8344">PR-8344</a>)</li>
<li>Fixing writing empty color names into ctbl format (<a href="https://github.com/Slicer/Slicer/pull/8348">PR-8348</a>)</li>
<li>Fix excessive qMRMLSceneViewMenu::resetMenu calls (<a href="https://github.com/Slicer/Slicer/pull/8358">PR-8358</a>)</li>
<li>Fix crash in vtkSlicerTerminologiesModuleLogic (<a href="https://github.com/Slicer/Slicer/pull/8361">PR-8361</a>)</li>
<li>Update CTK to fix <code>ctkDICOMDatabase::fileValue</code> for non-cached files (<a href="https://github.com/Slicer/Slicer/pull/8371">PR-8371</a>)</li>
<li>Disable logging of VTK deprecation warnings during Python autocompletion (<a href="https://github.com/Slicer/Slicer/pull/8372">PR-8372</a>)</li>
<li>Update CTK to ensure robust Python auto-completion anticipating VTK 9.4 (<a href="https://github.com/Slicer/Slicer/pull/8380">PR-8380</a>)</li>
<li>Fix crash when entering into Transforms module (<a href="https://github.com/Slicer/Slicer/pull/8388">PR-8388</a>)</li>
<li>Adjust the FieldOfView to match the aspect ratio of the slice dimensions. (<a href="https://github.com/Slicer/Slicer/pull/8370">PR-8370</a>)</li>
<li>Fix vtkMRMLMarkupsLineNode::GetLineStartPosition crash for empty node (<a href="https://github.com/Slicer/Slicer/pull/8412">PR-8412</a>)</li>
<li>Fix volume rendering clipping for volumes with negative scalar (<a href="https://github.com/Slicer/Slicer/pull/8403">PR-8403</a>)</li>
<li>Fix editing color list in picker widget (<a href="https://github.com/Slicer/Slicer/pull/8417">PR-8417</a>)</li>
<li>Fix editing of segment color (<a href="https://github.com/Slicer/Slicer/pull/8424">PR-8424</a>)</li>
<li>Restore fallback DICOM SEG upload with alternative storescu config (<a href="https://github.com/Slicer/Slicer/pull/8401">PR-8401</a>)</li>
<li>Fix incorrect expected warnings in vtkMRMLAnnotationSceneTest (<a href="https://github.com/Slicer/Slicer/pull/8437">PR-8437</a>)</li>
<li>Do not attempt to import obsolete qSlicerBaseQTCLIPython module (<a href="https://github.com/Slicer/Slicer/pull/8480">PR-8480</a>)</li>
<li>Avoid invalid default when retrieving active place node class name (<a href="https://github.com/Slicer/Slicer/pull/8487">PR-8487</a>)</li>
<li>Make color table csv file reading more robust (<a href="https://github.com/Slicer/Slicer/pull/8472">PR-8472</a>)</li>
<li>Update CTK to improve ctkAxesWidget styling and support CMake 4+ (<a href="https://github.com/Slicer/Slicer/pull/8493">PR-8493</a>)</li>
<li>Fix invalid typing usage in parameter node following pyupgrade (<a href="https://github.com/Slicer/Slicer/pull/8494">PR-8494</a>)</li>
<li>Ensure deepcopy is propagated in vtkMRMLSequenceBrowserNode::CopyContent (<a href="https://github.com/Slicer/Slicer/pull/8515">PR-8515</a>)</li>
<li>Fix runtime loading of JsonCpp library from build tree on Windows (<a href="https://github.com/Slicer/Slicer/pull/8532">PR-8532</a>)</li>
<li>Prevent WindowLevelPreset duplication in volume display node (<a href="https://github.com/Slicer/Slicer/pull/8542">PR-8542</a>)</li>
<li>Incorrect number of arguments given when weightAdjustment was desired. (<a href="https://github.com/Slicer/Slicer/pull/8552">PR-8552</a>)</li>
<li>Fix reordering of subject hierarchy nodes (<a href="https://github.com/Slicer/Slicer/pull/8422">PR-8422</a>)</li>
<li>Fix incorrect QDir assignment introduced during refactoring (<a href="https://github.com/Slicer/Slicer/pull/8581">PR-8581</a>)</li>
<li>Fix improper Python initialization causing inconsistent interpreter state (<a href="https://github.com/Slicer/Slicer/pull/8582">PR-8582</a>)</li>
<li>Select first component when RGBA volume rendering is selected (<a href="https://github.com/Slicer/Slicer/pull/8587">PR-8587</a>)</li>
<li>Fix crashes caused by range-based loops over temporary Qt containers (<a href="https://github.com/Slicer/Slicer/pull/8589">PR-8589</a>)</li>
<li>Add missing return from WriteVolumePropertyNode (<a href="https://github.com/Slicer/Slicer/pull/8592">PR-8592</a>)</li>
<li>Add krb5-gssapi-stub to avoid GSSAPI runtime linkage issues on Linux (<a href="https://github.com/Slicer/Slicer/pull/8598">PR-8598</a>)</li>
<li>Fix qMRMLNodeAttributeTableViewTest reintroducing empty QString init (<a href="https://github.com/Slicer/Slicer/pull/8602">PR-8602</a>)</li>
<li>Fix system git invocation in GSSAPI stub builds and generalize executable wrapper (<a href="https://github.com/Slicer/Slicer/pull/8613">PR-8613</a>)</li>
<li>Update CompareVolumes to fix Hot Link selection issue (<a href="https://github.com/Slicer/Slicer/pull/8614">PR-8614</a>)</li>
<li>Fix invalid node type in GetViewNodeClasses() (<a href="https://github.com/Slicer/Slicer/pull/8615">PR-8615</a>)</li>
<li>Make node type labels translatable (<a href="https://github.com/Slicer/Slicer/pull/8091">PR-8091</a>)</li>
<li>Fix removal of dash characters from exported segmentation filename (<a href="https://github.com/Slicer/Slicer/pull/8617">PR-8617</a>)</li>
<li>Replace u8‑prefixed unit suffix literals with narrow strings (<a href="https://github.com/Slicer/Slicer/pull/8610">PR-8610</a>)</li>
<li>Avoid cursor jump on edit in extension LineEdit (<a href="https://github.com/Slicer/Slicer/pull/8621">PR-8621</a>)</li>
<li>Initialize environment from launcher before Python to fix macOS startup (<a href="https://github.com/Slicer/Slicer/pull/8632">PR-8632</a>)</li>
<li>Fix empty volume display histogram group box (<a href="https://github.com/Slicer/Slicer/pull/8630">PR-8630</a>)</li>
<li>Ensure MRMLApplicationLogic is initialized in all modules, fix Colors (<a href="https://github.com/Slicer/Slicer/pull/8644">PR-8644</a>)</li>
<li>Fix Windows graphics preference not set when installing app with admin privileges (<a href="https://github.com/Slicer/Slicer/pull/8645">PR-8645</a>)</li>
<li>Drop unneeded nsl and nis dependencies to resolve libtirpc symbol error (<a href="https://github.com/Slicer/Slicer/pull/8649">PR-8649</a>)</li>
<li>Restore https download on macOS fixing packaging of SSL python modules (<a href="https://github.com/Slicer/Slicer/pull/8654">PR-8654</a>)</li>
<li>Fix traceback using line profile on 2D image (<a href="https://github.com/Slicer/Slicer/pull/8657">PR-8657</a>)</li>
<li>Fix not returning GUI tag after connection (<a href="https://github.com/Slicer/Slicer/pull/8667">PR-8667</a>)</li>
<li>Update CTK to ensure VTK views are always up-to-date (<a href="https://github.com/Slicer/Slicer/pull/8672">PR-8672</a>)</li>
<li>Show all referenced series as checkboxes in DICOM popup (<a href="https://github.com/Slicer/Slicer/pull/8605">PR-8605</a>)</li>
<li>Fix VTK errors drawing line profile plot with undefined points (<a href="https://github.com/Slicer/Slicer/pull/8677">PR-8677</a>)</li>
<li>Fixed hidden slice edges kept appearing in 3D views (<a href="https://github.com/Slicer/Slicer/pull/8684">PR-8684</a>)</li>
<li>Fix automatic conversion of annotation nodes (<a href="https://github.com/Slicer/Slicer/pull/8686">PR-8686</a>)</li>
<li>Fix py_nomainwindow_test_slicer_parameter_node_wrapper_guis test (<a href="https://github.com/Slicer/Slicer/pull/8687">PR-8687</a>)</li>
<li>Improve scene view storage and conversion, fix model visibility issues (<a href="https://github.com/Slicer/Slicer/pull/8693">PR-8693</a>)</li>
<li>Suppress unnecessary warning for hidden subject hierarchy items (<a href="https://github.com/Slicer/Slicer/pull/8695">PR-8695</a>)</li>
<li>Fix crash in vtkSegmentation::CollapseBinaryLabelmaps (<a href="https://github.com/Slicer/Slicer/pull/8700">PR-8700</a>)</li>
<li>Prevent crash on SH reparent without displayable node (<a href="https://github.com/Slicer/Slicer/pull/8701">PR-8701</a>)</li>
<li>Use UVW layer opacities when building the UVW blending pipeline (<a href="https://github.com/Slicer/Slicer/pull/8711">PR-8711</a>)</li>
<li>Fix loading of multi-file volumes in SampleData module (<a href="https://github.com/Slicer/Slicer/pull/8710">PR-8710</a>)</li>
<li>Fix ReverseAlpha compositing inverting opacities not layers (<a href="https://github.com/Slicer/Slicer/pull/8712">PR-8712</a>)</li>
<li>Fix Add/Subtract compositing clobbering background input (<a href="https://github.com/Slicer/Slicer/pull/8709">PR-8709</a>)</li>
<li>Update SampleData test for multi-file volume loading behavior (<a href="https://github.com/Slicer/Slicer/pull/8713">PR-8713</a>)</li>
<li>Improve error reporting and fix Color module tests (<a href="https://github.com/Slicer/Slicer/pull/8717">PR-8717</a>)</li>
<li>Manage correctly row deletion in qMRMLSubjectHierarchyCombobox (<a href="https://github.com/Slicer/Slicer/pull/8692">PR-8692</a>)</li>
<li>Fix MIP and MinIP VolumeRendering with SSAO render pass (<a href="https://github.com/Slicer/Slicer/pull/8719">PR-8719</a>)</li>
<li>Fix Undo/Redo in the segment editor logic (<a href="https://github.com/Slicer/Slicer/pull/8722">PR-8722</a>)</li>
<li>Fix reading of vector volumes (<a href="https://github.com/Slicer/Slicer/pull/8718">PR-8718</a>)</li>
<li>Make DICOMProcess init cooperative so TLS mixin is initialized (<a href="https://github.com/Slicer/Slicer/pull/8751">PR-8751</a>)</li>
<li>Preserve <code>sys.path</code> during Slicer module discovery &amp; add startup test (<a href="https://github.com/Slicer/Slicer/pull/8727">PR-8727</a>)</li>
<li>Delete IO options when using native file dialog to prevent leak (<a href="https://github.com/Slicer/Slicer/pull/8753">PR-8753</a>)</li>
<li>Fix geometry initialization from empty segmentation file (<a href="https://github.com/Slicer/Slicer/pull/8761">PR-8761</a>)</li>
<li>Do not reset markups control points when reading XML attributes (<a href="https://github.com/Slicer/Slicer/pull/8748">PR-8748</a>)</li>
<li>Fixed cloning of composite transforms (<a href="https://github.com/Slicer/Slicer/pull/8768">PR-8768</a>)</li>
<li>Make mrb file loading more robust (<a href="https://github.com/Slicer/Slicer/pull/8771">PR-8771</a>)</li>
<li>Clear existing node references before parsing new ones (<a href="https://github.com/Slicer/Slicer/pull/8749">PR-8749</a>)</li>
<li>childwidgetvariables do not return an object with an empty attribute (<a href="https://github.com/Slicer/Slicer/pull/8775">PR-8775</a>)</li>
<li>Fix OpenGL error at startup in debug mode (<a href="https://github.com/Slicer/Slicer/pull/8795">PR-8795</a>)</li>
<li>Fix loading of orientation marker and fonts (<a href="https://github.com/Slicer/Slicer/pull/8800">PR-8800</a>)</li>
<li>Ensure launcher splash-screen gets hidden on app restart (<a href="https://github.com/Slicer/Slicer/pull/8808">PR-8808</a>)</li>
<li>Update CTK to fix AUTOMOC DCMTK/Python clash and chart refresh (<a href="https://github.com/Slicer/Slicer/pull/8823">PR-8823</a>)</li>
<li>Fix Line Profile issues showing multiple lines (<a href="https://github.com/Slicer/Slicer/pull/8809">PR-8809</a>)</li>
<li>Update VTK to include vtkSurfaceNets3D fix for orientation consistency (<a href="https://github.com/Slicer/Slicer/pull/8831">PR-8831</a>)</li>
<li>Fix hardening of inverted composite transform (<a href="https://github.com/Slicer/Slicer/pull/8365">PR-8365</a>)</li>
<li>A collection of traceback fixes in automated tests (<a href="https://github.com/Slicer/Slicer/pull/8423">PR-8423</a>)</li>
</ul>
<h3 id="heading--application">Application</h3>
<ul>
<li>Define a window icon for all windows  (<a href="https://github.com/Slicer/Slicer/pull/8186">PR-8186</a>)</li>
<li>Simplify qSlicerStyle removing obsolete workaround <span class="hashtag-raw">#7418</span> (<a href="https://github.com/Slicer/Slicer/pull/8376">PR-8376</a>)</li>
<li>Remove old deprecation warning (<a href="https://github.com/Slicer/Slicer/pull/8433">PR-8433</a>)</li>
<li>Add customizable application display name property (<a href="https://github.com/Slicer/Slicer/pull/8731">PR-8731</a>)</li>
<li>Set Windows registry key to use high performance graphics (<a href="https://github.com/Slicer/Slicer/pull/8643">PR-8643</a>)</li>
<li>Use subject hierarchy tree as node selector in Volumes, Volume Rendering, Segmentations, Transforms modules (<a href="https://github.com/Slicer/Slicer/pull/8119">PR-8119</a>)</li>
<li>Add keyboard and mouse shortcuts for Module Selector navigation (<a href="https://github.com/Slicer/Slicer/pull/8681">PR-8681</a>)</li>
<li>Include slice intersection mouse move info in tooltip (<a href="https://github.com/Slicer/Slicer/pull/8392">PR-8392</a>)</li>
<li>Decouple Base, Libs, and Modules/Loadable from app-specific paths via runtime Home/Share in vtkMRMLApplicationLogic (<a href="https://github.com/Slicer/Slicer/pull/8004">PR-8004</a>)</li>
<li>Add widget to select any node for scene views (<a href="https://github.com/Slicer/Slicer/pull/8607">PR-8607</a>)</li>
</ul>
<h3 id="heading--extension">Extension</h3>
<ul>
<li>Support specifying extension contributors as CMake list (<a href="https://github.com/Slicer/Slicer/pull/8175">PR-8175</a>)</li>
<li>Support fixup overrides in app and extension packaging contexts (<a href="https://github.com/Slicer/Slicer/pull/8516">PR-8516</a>)</li>
</ul>
<h3 id="heading--cli">CLI</h3>
<ul>
<li>Add option to show CLI executable windows on Windows (<a href="https://github.com/Slicer/Slicer/pull/8172">PR-8172</a>)</li>
<li>Add PET support to CreateDICOMSeries CLI (<a href="https://github.com/Slicer/Slicer/pull/8538">PR-8538</a>)</li>
</ul>
<h3 id="heading--scripting">Scripting</h3>
<ul>
<li>Warn when setting volume node with invalid vtkImageData (<a href="https://github.com/Slicer/Slicer/pull/8178">PR-8178</a>)</li>
<li>Add support for additional NumPy types in <code>slicer.util.updateTableFromArray</code> (<a href="https://github.com/Slicer/Slicer/pull/8180">PR-8180</a>)</li>
<li>Add <code>ctkColorPickerButton</code> support with <code>QColor</code> in <code>parameterNodeWrapper</code> (<a href="https://github.com/Slicer/Slicer/pull/8195">PR-8195</a>)</li>
<li>Replace deprecated imp module with importlib to support Python 3.12+ (<a href="https://github.com/Slicer/Slicer/pull/8459">PR-8459</a>)</li>
<li>Replace deprecated assertRegexpMatches with assertRegex to support Python 3.12+ (<a href="https://github.com/Slicer/Slicer/pull/8461">PR-8461</a>)</li>
<li>Upgrade from python 3.9.10 to 3.12.10 (<a href="https://github.com/Slicer/Slicer/pull/8466">PR-8466</a>)</li>
<li>Replace deprecated pydicom API usage (<a href="https://github.com/Slicer/Slicer/pull/8488">PR-8488</a>)</li>
<li>Enforce python 3.12 and newer syntax (<a href="https://github.com/Slicer/Slicer/pull/8489">PR-8489</a>)</li>
<li>Update Python initialization to use PyConfig API (<a href="https://github.com/Slicer/Slicer/pull/8548">PR-8548</a>)</li>
<li>Enable relative import of Slicer Python-wrapped libraries (<a href="https://github.com/Slicer/Slicer/pull/8535">PR-8535</a>)</li>
<li>Add parameter node GUI connector for qMRMLSubjectHierarchyComboBox (<a href="https://github.com/Slicer/Slicer/pull/8573">PR-8573</a>)</li>
<li>Add parameter node GUI connectors (<a href="https://github.com/Slicer/Slicer/pull/8646">PR-8646</a>)</li>
</ul>
<h3 id="heading--internationalization-localization">Internationalization/Localization</h3>
<ul>
<li>Make JSON files in extensions translatable (<a href="https://github.com/Slicer/Slicer/pull/8519">PR-8519</a>)</li>
</ul>
<h3 id="heading--installation">Installation</h3>
<ul>
<li>Make NSIS Windows installer prettier with application branding  (<a href="https://github.com/Slicer/Slicer/pull/8192">PR-8192</a>)</li>
<li>Update CTKAppLauncher from 0.1.32 to 33 (<a href="https://github.com/Slicer/Slicer/pull/8801">PR-8801</a>)</li>
<li>Show launcher splashscreen until Slicer is started (<a href="https://github.com/Slicer/Slicer/pull/8802">PR-8802</a>)</li>
</ul>
<h3 id="heading--mrml">MRML</h3>
<ul>
<li>Centralize retrieval of Markups Moving attributes in display node (<a href="https://github.com/Slicer/Slicer/pull/8173">PR-8173</a>)</li>
<li>Mark SlicerLogic UpdateBlendLayers() &amp; UpdateFractions() helpers as static (<a href="https://github.com/Slicer/Slicer/pull/8234">PR-8234</a>)</li>
<li>Consolidate SliceLogic calls to SetInterpolateTexture (<a href="https://github.com/Slicer/Slicer/pull/8232">PR-8232</a>)</li>
<li>Generalize SliceLogic API introducing “Nth Layer” functions (<a href="https://github.com/Slicer/Slicer/pull/8277">PR-8277</a>)</li>
<li>Generalize CompositeNode API introducing “Nth Layer” functions (<a href="https://github.com/Slicer/Slicer/pull/8278">PR-8278</a>)</li>
<li>Refactor vtkMRMLSliceLogic::UpdatePipeline to use “Nth Layer” API (<a href="https://github.com/Slicer/Slicer/pull/8279">PR-8279</a>)</li>
<li>Generalize CompositeNode “opacity” API introducing “Nth Layer” functions (<a href="https://github.com/Slicer/Slicer/pull/8280">PR-8280</a>)</li>
<li>Move singleton declaration from vtkMRMLLayoutNode constructor (<a href="https://github.com/Slicer/Slicer/pull/8317">PR-8317</a>)</li>
<li>Add CopyContent methods to vtkMRMLLayoutNode and vtkMRMLSequenceBrowserNode (<a href="https://github.com/Slicer/Slicer/pull/8318">PR-8318</a>)</li>
<li>Refactor observations in MRML nodes (<a href="https://github.com/Slicer/Slicer/pull/8350">PR-8350</a>)</li>
<li>Move Markups MRML JSON helper classes to MRMLCore (<a href="https://github.com/Slicer/Slicer/pull/8452">PR-8452</a>)</li>
</ul>
<h3 id="heading--api-updates">API Updates</h3>
<ul>
<li>Remove support for building against VTK &lt;= 9.1 (<a href="https://github.com/Slicer/Slicer/pull/8244">PR-8244</a>)</li>
<li>Update VTK from 9.2.20230607 to 9.4.2 (<a href="https://github.com/Slicer/Slicer/pull/8238">PR-8238</a>)</li>
<li>Remove additional code handling VTK support &lt;= 9.1 (<a href="https://github.com/Slicer/Slicer/pull/8310">PR-8310</a>)</li>
<li>Add convenience methods to get/set terminology in segments (<a href="https://github.com/Slicer/Slicer/pull/8296">PR-8296</a>)</li>
<li>Select the first suitable node by default in tree views (<a href="https://github.com/Slicer/Slicer/pull/8306">PR-8306</a>)</li>
<li>Make all colors defined by default when setting a LUT  (<a href="https://github.com/Slicer/Slicer/pull/8349">PR-8349</a>)</li>
<li>Add option to hide missing display nodes in sequences (<a href="https://github.com/Slicer/Slicer/pull/8354">PR-8354</a>)</li>
<li>Add functions to update the contents of existing scene views (<a href="https://github.com/Slicer/Slicer/pull/8393">PR-8393</a>)</li>
<li>Update CTK to add components to ctkVTKVolumePropertyWidget (<a href="https://github.com/Slicer/Slicer/pull/8414">PR-8414</a>)</li>
<li>Add support for building against VTK version 9.5.0 (<a href="https://github.com/Slicer/Slicer/pull/8427">PR-8427</a>)</li>
<li>Add multi-component handling for vtkMRMLVolumePropertyNode (<a href="https://github.com/Slicer/Slicer/pull/8439">PR-8439</a>)</li>
<li>Avoid changing selected volume rendering component when switching modes (<a href="https://github.com/Slicer/Slicer/pull/8588">PR-8588</a>)</li>
<li>Add API to retrieve view displayable managers without Qt widgets (<a href="https://github.com/Slicer/Slicer/pull/8658">PR-8658</a>)</li>
<li>Split segment editor logic (<a href="https://github.com/Slicer/Slicer/pull/8666">PR-8666</a>)</li>
<li>Simplify Slice view removing LightBox feature (<a href="https://github.com/Slicer/Slicer/pull/8776">PR-8776</a>)</li>
<li>Improvements to default node usage across different node creation methods (<a href="https://github.com/Slicer/Slicer/pull/8420">PR-8420</a>)</li>
<li>Segment Editor: class rename, MRML logic integration, and logging controls (<a href="https://github.com/Slicer/Slicer/pull/8746">PR-8746</a>)</li>
<li>Expose segment editor effect cursor functions (<a href="https://github.com/Slicer/Slicer/pull/8763">PR-8763</a>)</li>
</ul>
<h3 id="heading--documentation">Documentation</h3>
<ul>
<li>Fix links to slicer doxygen in the developer guide (<a href="https://github.com/Slicer/Slicer/pull/8171">PR-8171</a>)</li>
<li>Dynamically generate links to slicer doxygen based on ReadTheDocs version (<a href="https://github.com/Slicer/Slicer/pull/8176">PR-8176</a>)</li>
<li>Fix various broken documentation links in developer guide (<a href="https://github.com/Slicer/Slicer/pull/8179">PR-8179</a>)</li>
<li>Add documentation for help menu (<a href="https://github.com/Slicer/Slicer/pull/8169">PR-8169</a>)</li>
<li>Update Transforms module API documentation adding missing Doxygen links (<a href="https://github.com/Slicer/Slicer/pull/8185">PR-8185</a>)</li>
<li>Update vtkMRMLSliceCompositeNode and vtkMRMLSliceLogic to use doxygen grouping markers (<a href="https://github.com/Slicer/Slicer/pull/8231">PR-8231</a>)</li>
<li>Update BlendPipeline comment to correctly depict pipeline (<a href="https://github.com/Slicer/Slicer/pull/8236">PR-8236</a>)</li>
<li>Remove obsolete comment from vtkMRMLSliceLogic::UpdatePipeline (<a href="https://github.com/Slicer/Slicer/pull/8237">PR-8237</a>)</li>
<li>Improve or add comments in vtkMRMLSliceLogic::UpdatePipeline (<a href="https://github.com/Slicer/Slicer/pull/8243">PR-8243</a>)</li>
<li>Add ambient shadows section to documentation (<a href="https://github.com/Slicer/Slicer/pull/8304">PR-8304</a>)</li>
<li>Update model maker documentation (<a href="https://github.com/Slicer/Slicer/pull/8313">PR-8313</a>)</li>
<li>Moved 2 modules to match application module selector (<a href="https://github.com/Slicer/Slicer/pull/8335">PR-8335</a>)</li>
<li>Remove link to wiki from list of modules (<a href="https://github.com/Slicer/Slicer/pull/8338">PR-8338</a>)</li>
<li>Update build instructions to warn users about CMake 4 incompatibility (<a href="https://github.com/Slicer/Slicer/pull/8381">PR-8381</a>)</li>
<li>Fix VTK coding conventions dead link (<a href="https://github.com/Slicer/Slicer/pull/8445">PR-8445</a>)</li>
<li>Fix entry in “Script repository / Segmentations” (<a href="https://github.com/Slicer/Slicer/pull/8511">PR-8511</a>)</li>
<li>Add DOI and dynamic citation count badges for Slicer reference paper (<a href="https://github.com/Slicer/Slicer/pull/8561">PR-8561</a>)</li>
<li>Fix build instructions updating Qt installer URLS for macOS and Linux (<a href="https://github.com/Slicer/Slicer/pull/8593">PR-8593</a>)</li>
<li>Add Ubuntu 25.04 build instructions and GSS/Kerberos workaround (<a href="https://github.com/Slicer/Slicer/pull/8634">PR-8634</a>)</li>
<li>Fix broken links to the PolySeg paper (<a href="https://github.com/Slicer/Slicer/pull/8639">PR-8639</a>)</li>
<li>Remove warning section for libtirpc GSS/Kerberos symbol lookup error (<a href="https://github.com/Slicer/Slicer/pull/8652">PR-8652</a>)</li>
<li>Add dedicated GOVERNANCE document and reference it from the about page (<a href="https://github.com/Slicer/Slicer/pull/8656">PR-8656</a>)</li>
<li>Reference “Code of Conduct” in Governance section and Update contribution processes (<a href="https://github.com/Slicer/Slicer/pull/8661">PR-8661</a>)</li>
<li>Support GitHub-style alerts in documentation and improve CONTRIBUTING document formatting (<a href="https://github.com/Slicer/Slicer/pull/8662">PR-8662</a>)</li>
<li>Fix segmentation oversampling snippet in script repository (<a href="https://github.com/Slicer/Slicer/pull/8679">PR-8679</a>)</li>
<li>Add Fedora 37+ launch troubleshooting (<a href="https://github.com/Slicer/Slicer/pull/7114">PR-7114</a>)</li>
<li>Add top-level “Extensions” page (<a href="https://github.com/Slicer/Slicer/pull/8453">PR-8453</a>)</li>
<li>Warn about uncommon volume format options (<a href="https://github.com/Slicer/Slicer/pull/8756">PR-8756</a>)</li>
<li>Add “Slicer integration in hospital/PACS context” to DICOM module docs (<a href="https://github.com/Slicer/Slicer/pull/8786">PR-8786</a>)</li>
<li>Document the new .vp.json volume property file format (<a href="https://github.com/Slicer/Slicer/pull/8791">PR-8791</a>)</li>
<li>Update transforms.md (<a href="https://github.com/Slicer/Slicer/pull/8534">PR-8534</a>)</li>
<li>Bump docs dependencies to resolve vulnerability alerts (<a href="https://github.com/Slicer/Slicer/pull/8478">PR-8478</a>)</li>
<li>Bump doc dependency pygments version to resolve vulnerability (<a href="https://github.com/Slicer/Slicer/pull/8482">PR-8482</a>)</li>
<li>Bump docs dependency urllib3 to resolve vulnerability alert (<a href="https://github.com/Slicer/Slicer/pull/8495">PR-8495</a>)</li>
<li>Fix typo in Grow From Seeds help text (<a href="https://github.com/Slicer/Slicer/pull/8166">PR-8166</a>)</li>
</ul>
<h2 id="heading--new-modules">New Modules</h2>
<ul>
<li>Add line profile module (<a href="https://github.com/Slicer/Slicer/pull/8435">PR-8435</a>)</li>
</ul>
<h2 id="heading--improved-modules">Improved Modules</h2>
<h3 id="heading--dicom">DICOM</h3>
<ul>
<li>Add TLS authentication support to DICOM Sender and Listener (<a href="https://github.com/Slicer/Slicer/pull/8121">PR-8121</a>)</li>
<li>Add dicom instance number in the dataProbe (<a href="https://github.com/Slicer/Slicer/pull/8432">PR-8432</a>)</li>
</ul>
<h3 id="heading--markups">Markups</h3>
<ul>
<li>Remove Slicer mention from Markups save to default display tooltip (<a href="https://github.com/Slicer/Slicer/pull/8428">PR-8428</a>)</li>
</ul>
<h3 id="heading--models">Models</h3>
<ul>
<li>Improve tooltip for model nodes in subject hierarchy (<a href="https://github.com/Slicer/Slicer/pull/8425">PR-8425</a>)</li>
</ul>
<h3 id="heading--generalizedreformat">GeneralizedReformat</h3>
<ul>
<li>Add Curved Planar Reformation (CPR) support to GeneralizedReformat (<a href="https://github.com/Slicer/Slicer/pull/8148">PR-8148</a>)</li>
</ul>
<h3 id="heading--sampledata">SampleData</h3>
<ul>
<li>Improve custom sample data download (<a href="https://github.com/Slicer/Slicer/pull/8736">PR-8736</a>)</li>
</ul>
<h3 id="heading--segmentations">Segmentations</h3>
<ul>
<li>Reduce unnecessary error reporting in segmentation SH (<a href="https://github.com/Slicer/Slicer/pull/8299">PR-8299</a>)</li>
<li>Propagate terminology when exporting segments to models (<a href="https://github.com/Slicer/Slicer/pull/8765">PR-8765</a>)</li>
</ul>
<h3 id="heading--sequences">Sequences</h3>
<ul>
<li>Update Scene Views to use Sequences (<a href="https://github.com/Slicer/Slicer/pull/8303">PR-8303</a>)</li>
</ul>
<h3 id="heading--terminologies">Terminologies</h3>
<ul>
<li>Store and edit terminologies in color table nodes (<a href="https://github.com/Slicer/Slicer/pull/8112">PR-8112</a>)</li>
<li>Color table terminology fixes (<a href="https://github.com/Slicer/Slicer/pull/8297">PR-8297</a>)</li>
<li>Select first preferred terminology if no entry is found (<a href="https://github.com/Slicer/Slicer/pull/8395">PR-8395</a>)</li>
<li>Set color picker to use basic colors tab by default (<a href="https://github.com/Slicer/Slicer/pull/8416">PR-8416</a>)</li>
<li>Always show context selector in terminology navigator (<a href="https://github.com/Slicer/Slicer/pull/8436">PR-8436</a>)</li>
</ul>
<h3 id="heading--crop-volume">Crop Volume</h3>
<ul>
<li>Add volume reorientation to Crop Volume module (<a href="https://github.com/Slicer/Slicer/pull/8737">PR-8737</a>)</li>
</ul>
<h2 id="heading--infrastructure">Infrastructure</h2>
<ul>
<li>Increase git hook maximum line length from 160 to 180 (<a href="https://github.com/Slicer/Slicer/pull/8545">PR-8545</a>)</li>
</ul>
<h3 id="heading--packaging">Packaging</h3>
<h3 id="heading--continuous-integration-ci">Continuous integration (CI)</h3>
<h3 id="heading--build-system">Build system</h3>
<ul>
<li>Ensure setting <code>run_ctest_with_upload</code> to <code>FALSE</code> skips package upload (<a href="https://github.com/Slicer/Slicer/pull/8170">PR-8170</a>)</li>
<li>Reduce warnings during legacy scene load (<a href="https://github.com/Slicer/Slicer/pull/8357">PR-8357</a>)</li>
<li>Update build-system to support forcing extension revision (<a href="https://github.com/Slicer/Slicer/pull/6378">PR-6378</a>)</li>
</ul>
<h3 id="heading--platform-support">Platform support</h3>
<h3 id="heading--dependencies">Dependencies</h3>
<p><strong>CTK:</strong></p>
<ul>
<li>Update CTK to include PythonQt updates (<a href="https://github.com/Slicer/Slicer/pull/8527">PR-8527</a>)</li>
<li>Update CTKAppLauncherLib and CTKAPPLAUNCHER (<a href="https://github.com/Slicer/Slicer/pull/8629">PR-8629</a>)</li>
<li>Update CTK to include PythonQt minimizing commontk fork deltas (<a href="https://github.com/Slicer/Slicer/pull/8803">PR-8803</a>)</li>
<li>Update CTK and align MOC include names with Qt AUTOMOC convention (<a href="https://github.com/Slicer/Slicer/pull/8813">PR-8813</a>)</li>
<li>Update CTK to modernize PythonQt integration (<a href="https://github.com/Slicer/Slicer/pull/8817">PR-8817</a>)</li>
<li>Update CTK to fix PythonQt build ensuring Qt DIR is passed (<a href="https://github.com/Slicer/Slicer/pull/8824">PR-8824</a>)</li>
<li>Update CTK to include changes for Qt5/Qt6 compatibility (<a href="https://github.com/Slicer/Slicer/pull/8833">PR-8833</a>)</li>
</ul>
<p><strong>ITK:</strong></p>
<ul>
<li>Update ITK to 5.4.3 (<a href="https://github.com/Slicer/Slicer/pull/8339">PR-8339</a>)</li>
</ul>
<p><strong>libarchive:</strong></p>
<ul>
<li>Update LibArchive from 3.6.1 to 3.8.1 to resolve CMake deprecation issues (<a href="https://github.com/Slicer/Slicer/pull/8594">PR-8594</a>)</li>
</ul>
<p><strong>VTK:</strong></p>
<ul>
<li>Update VTK with vtkAxisActor2D tick and label position fix (<a href="https://github.com/Slicer/Slicer/pull/8636">PR-8636</a>)</li>
<li>Update VTK to 9.5.1 (<a href="https://github.com/Slicer/Slicer/pull/8683">PR-8683</a>)</li>
<li>Update VTK to 9.5.2 (<a href="https://github.com/Slicer/Slicer/pull/8733">PR-8733</a>)</li>
</ul>
<p><strong>Other Dependencies:</strong></p>
<ul>
<li>Update teem from r6245 to r7265 (<a href="https://github.com/Slicer/Slicer/pull/8500">PR-8500</a>)</li>
<li>Update JsonCpp from 0.10.6 to 1.9.6 (<a href="https://github.com/Slicer/Slicer/pull/8492">PR-8492</a>)</li>
<li>Update python packages to latest (<a href="https://github.com/Slicer/Slicer/pull/8455">PR-8455</a>)</li>
<li>Update RapidJSON to latest revision (<a href="https://github.com/Slicer/Slicer/pull/8502">PR-8502</a>)</li>
<li>Update SimpleITK to 2.5.2 and corresponding dependencies (<a href="https://github.com/Slicer/Slicer/pull/8522">PR-8522</a>)</li>
<li>Update bzip2 from 1.0.8 to 1.1.0 to resolve CMake deprecation issues (<a href="https://github.com/Slicer/Slicer/pull/8595">PR-8595</a>)</li>
<li>Switch from zlib 1.2.3 to maintained zlib-ng 2.2.4 fork (<a href="https://github.com/Slicer/Slicer/pull/8597">PR-8597</a>)</li>
<li>Update BRAINSTools from 2024-05-31 to 2024-11-09 (<a href="https://github.com/Slicer/Slicer/pull/8191">PR-8191</a>)</li>
<li>Update vtkAddon (<a href="https://github.com/Slicer/Slicer/pull/8227">PR-8227</a>)</li>
<li>Update vtkAddon anticipating update to VTK &gt;= 9.4 (<a href="https://github.com/Slicer/Slicer/pull/8239">PR-8239</a>)</li>
<li>Update SurfaceToolbox to integrate Dynamic Modeler Revolve tool (<a href="https://github.com/Slicer/Slicer/pull/8544">PR-8544</a>)</li>
<li>Update CompareVolumes to include optional return mapping and reuse of layout selection widget from LandmarkRegistration (<a href="https://github.com/Slicer/Slicer/pull/8678">PR-8678</a>)</li>
</ul>
<h3 id="heading--custom-slicer-application-support">Custom Slicer application support</h3>
<h4 id="heading--slicer-application">Slicer Application</h4>
<h4 id="heading--build-system">Build-System</h4>
<ul>
<li>Generalize internal <code>qt_root_dir</code> path (<a href="https://github.com/Slicer/Slicer/pull/8219">PR-8219</a>)</li>
<li>Update python-cmake-buildsystem anticipating python version update (<a href="https://github.com/Slicer/Slicer/pull/8165">PR-8165</a>)</li>
<li>Move classes from Modules/Loadable/Markups/MRML to Libs/MRML/Core (<a href="https://github.com/Slicer/Slicer/pull/8155">PR-8155</a>)</li>
<li>Update VTK backporting fix to support building on Linux with clang (<a href="https://github.com/Slicer/Slicer/pull/8183">PR-8183</a>)</li>
<li>Improve compatibility with ITK_LEGACY_REMOVE flag  (<a href="https://github.com/Slicer/Slicer/pull/8105">PR-8105</a>)</li>
<li>Use std::thread instead of deprecated ITK threading functions (<a href="https://github.com/Slicer/Slicer/pull/8194">PR-8194</a>)</li>
<li>Update BRAINSTools to fix macOS build (<a href="https://github.com/Slicer/Slicer/pull/8197">PR-8197</a>)</li>
<li>Fix Windows build errors by explicitly including <code>Windows.h</code> (<a href="https://github.com/Slicer/Slicer/pull/8196">PR-8196</a>)</li>
<li>Update external project to support externally built TBB libraries (<a href="https://github.com/Slicer/Slicer/pull/8202">PR-8202</a>)</li>
<li>Fix -Winconsistent-missing-override in <code>vtkMRMLMarkupsROINode</code> (<a href="https://github.com/Slicer/Slicer/pull/8218">PR-8218</a>)</li>
<li>Improve system Qt detection on Debian usr-merge and multiarch systems (<a href="https://github.com/Slicer/Slicer/pull/8111">PR-8111</a>)</li>
<li>Fix Windows build error by explicitly including Windows.h (<a href="https://github.com/Slicer/Slicer/pull/8292">PR-8292</a>)</li>
<li>Exclude dependabot and pre-commit pull requests from changelog (<a href="https://github.com/Slicer/Slicer/pull/8293">PR-8293</a>)</li>
<li>Make vtkSlicerTerminologiesModuleLogic API backward compatible (<a href="https://github.com/Slicer/Slicer/pull/8326">PR-8326</a>)</li>
<li>Fix warning due to missing return path (<a href="https://github.com/Slicer/Slicer/pull/8340">PR-8340</a>)</li>
<li>Make build fail with meaningful error message with CMake 4 (<a href="https://github.com/Slicer/Slicer/pull/8383">PR-8383</a>)</li>
<li>Update LandmarkRegistration module to latest (<a href="https://github.com/Slicer/Slicer/pull/8390">PR-8390</a>)</li>
<li>Update vtkAddon to fix wrapping error reported when using VTK 9.5 (<a href="https://github.com/Slicer/Slicer/pull/8429">PR-8429</a>)</li>
<li>Update CTK to fix build when using VTK 9.5 (<a href="https://github.com/Slicer/Slicer/pull/8431">PR-8431</a>)</li>
<li>Add documentation for building Slicer on Ubuntu 24.04, remove obsolete instructions for Ubuntu 20.04 (<a href="https://github.com/Slicer/Slicer/pull/8444">PR-8444</a>)</li>
<li>Update python-cmake-buildsystem anticipating python version update (<a href="https://github.com/Slicer/Slicer/pull/8454">PR-8454</a>)</li>
<li>Modernize integration of VTK build with Python site-packages (<a href="https://github.com/Slicer/Slicer/pull/8457">PR-8457</a>)</li>
<li>Remove unused Qt includes in vtkMRMLSequenceStorageNode.cxx (<a href="https://github.com/Slicer/Slicer/pull/8462">PR-8462</a>)</li>
<li>Remove unused logic includes from CropVolume module (<a href="https://github.com/Slicer/Slicer/pull/8465">PR-8465</a>)</li>
<li>Update python-cmake-buildsystem anticipating python version update (<a href="https://github.com/Slicer/Slicer/pull/8467">PR-8467</a>)</li>
<li>Move unreferenced node cleanup methods from MRMLLogic to MRMLScene  (<a href="https://github.com/Slicer/Slicer/pull/8470">PR-8470</a>)</li>
<li>Move vtkSlicerCLIModuleLogic from Base/QTCLI to Base/Logic (<a href="https://github.com/Slicer/Slicer/pull/8464">PR-8464</a>)</li>
<li>Remove obsolete includes from vtkSlicerApplicationLogic (<a href="https://github.com/Slicer/Slicer/pull/8476">PR-8476</a>)</li>
<li>Fix macOS build removing obsolete VTK wrapping of qSlicerBaseQTCLI (<a href="https://github.com/Slicer/Slicer/pull/8475">PR-8475</a>)</li>
<li>Update python-cmake-buildsystem anticipating python version update (<a href="https://github.com/Slicer/Slicer/pull/8479">PR-8479</a>)</li>
<li>Make vtkSlicerTerminologiesModuleLogic API backward compatible (<a href="https://github.com/Slicer/Slicer/pull/8484">PR-8484</a>)</li>
<li>Update teem to fix windows build (<a href="https://github.com/Slicer/Slicer/pull/8503">PR-8503</a>)</li>
<li>Update minimum required CMake version from 3.16.3 to 3.20.6 (<a href="https://github.com/Slicer/Slicer/pull/8501">PR-8501</a>)</li>
<li>Fix configuration on Windows by updating RapidJSON project installation (<a href="https://github.com/Slicer/Slicer/pull/8508">PR-8508</a>)</li>
<li>Fix unsigned comparison &amp; unused variable compiler warnings (<a href="https://github.com/Slicer/Slicer/pull/8497">PR-8497</a>)</li>
<li>Fix deprecated declarations related to vtkStdString (<a href="https://github.com/Slicer/Slicer/pull/8509">PR-8509</a>)</li>
<li>OpenSSL 1.1.1w is needed to fix missing include (<a href="https://github.com/Slicer/Slicer/pull/8504">PR-8504</a>)</li>
<li>Fix OpenSSL 1.1.1w build on macOS with non-system zlib (<a href="https://github.com/Slicer/Slicer/pull/8513">PR-8513</a>)</li>
<li>Fix unused variable warning in qMRMLSortFilterColorProxyModel (<a href="https://github.com/Slicer/Slicer/pull/8510">PR-8510</a>)</li>
<li>Update JsonCpp to skip installation of object files (<a href="https://github.com/Slicer/Slicer/pull/8517">PR-8517</a>)</li>
<li>Replace WIN32 with _WIN32 in VTK and ITK-related code (<a href="https://github.com/Slicer/Slicer/pull/8521">PR-8521</a>)</li>
<li>Fix return type of extraPythonScriptProcessedArgumentsCount property (<a href="https://github.com/Slicer/Slicer/pull/8523">PR-8523</a>)</li>
<li>Update MultiVolumeExplorer version for excluding Qt4 support (<a href="https://github.com/Slicer/Slicer/pull/8528">PR-8528</a>)</li>
<li>Update BRAINSTools to fix CMake warning due to version mismatch (<a href="https://github.com/Slicer/Slicer/pull/8529">PR-8529</a>)</li>
<li>Ensure correct handling of maximum representable double values (<a href="https://github.com/Slicer/Slicer/pull/8550">PR-8550</a>)</li>
<li>Remove redundant Slicer_HAVE_QT5 definitions (<a href="https://github.com/Slicer/Slicer/pull/8554">PR-8554</a>)</li>
<li>QObject must be listed first in multiple inheritance (<a href="https://github.com/Slicer/Slicer/pull/8556">PR-8556</a>)</li>
<li>Replace <code>fabs</code> with <code>std::abs</code> for consistency in types (<a href="https://github.com/Slicer/Slicer/pull/8551">PR-8551</a>)</li>
<li><code>showViewContextMenuActionsForItem</code> as <code>override</code> (<a href="https://github.com/Slicer/Slicer/pull/8553">PR-8553</a>)</li>
<li>Refactor QDir assignment to use setPath for consistency (<a href="https://github.com/Slicer/Slicer/pull/8558">PR-8558</a>)</li>
<li>Fix variable name closet-&gt;closest (<a href="https://github.com/Slicer/Slicer/pull/8560">PR-8560</a>)</li>
<li>Revert removal of redundant Slicer_HAVE_QT5 definitions (<a href="https://github.com/Slicer/Slicer/pull/8562">PR-8562</a>)</li>
<li>Remove obsolete Qt version checks related to Qt4 (<a href="https://github.com/Slicer/Slicer/pull/8570">PR-8570</a>)</li>
<li>Update CTK with PythonQt wrapping support for Qt 5.15 (<a href="https://github.com/Slicer/Slicer/pull/8572">PR-8572</a>)</li>
<li>signed vs unsigned compiler warning (<a href="https://github.com/Slicer/Slicer/pull/8574">PR-8574</a>)</li>
<li>Ensure <code>isPythonDisabled</code> is defined regardless of Python support (<a href="https://github.com/Slicer/Slicer/pull/8577">PR-8577</a>)</li>
<li>Prefer c++11 range for to Qt macros (<a href="https://github.com/Slicer/Slicer/pull/8580">PR-8580</a>)</li>
<li>Always enable CLI support and remove Slicer_BUILD_CLI_SUPPORT option (<a href="https://github.com/Slicer/Slicer/pull/8633">PR-8633</a>)</li>
<li>Replace deprecated use of TestBigEndian CMake module (<a href="https://github.com/Slicer/Slicer/pull/8650">PR-8650</a>)</li>
<li>Fix Windows build error in debug mode due to python312_d.lib (<a href="https://github.com/Slicer/Slicer/pull/8651">PR-8651</a>)</li>
<li>Remove unneeded setting of WORDS_BIGENDIAN/WORDS_LITTLEENDIAN macros (<a href="https://github.com/Slicer/Slicer/pull/8653">PR-8653</a>)</li>
<li>Fix linux build errors (<a href="https://github.com/Slicer/Slicer/pull/8665">PR-8665</a>)</li>
<li>Fix pattern for excluding bots from auto-generated changelog (<a href="https://github.com/Slicer/Slicer/pull/8673">PR-8673</a>)</li>
<li>Ensure BUILD_JOB_SERVER_AWARE is set for external projects (<a href="https://github.com/Slicer/Slicer/pull/8691">PR-8691</a>)</li>
<li>Set BUILD_JOB_SERVER_AWARE for extension ExternalProject on CMake ≥ 3.28 (<a href="https://github.com/Slicer/Slicer/pull/8702">PR-8702</a>)</li>
<li>Fix quoting of BUILD_JOB_SERVER_AWARE in extension ExternalProject (<a href="https://github.com/Slicer/Slicer/pull/8704">PR-8704</a>)</li>
<li>Enable building with CMake 4 (<a href="https://github.com/Slicer/Slicer/pull/8740">PR-8740</a>)</li>
<li>Fix compiler warnings unused variables/missing enumerations (<a href="https://github.com/Slicer/Slicer/pull/8743">PR-8743</a>)</li>
<li>Update FindVcvars from v1.8 to v1.12 (<a href="https://github.com/Slicer/Slicer/pull/8744">PR-8744</a>)</li>
<li>Qt AUTOGEN migration: enable AUTOUIC, AUTORCC, AUTOMOC across Slicer (<a href="https://github.com/Slicer/Slicer/pull/8814">PR-8814</a>)</li>
<li>Fix AUTOUIC include dir for multi-config generators (<a href="https://github.com/Slicer/Slicer/pull/8818">PR-8818</a>)</li>
<li>Add support for Visual Studio 2026 (<a href="https://github.com/Slicer/Slicer/pull/8742">PR-8742</a>)</li>
<li>Reduce threshold determining use of response file with AUTOMOC (<a href="https://github.com/Slicer/Slicer/pull/8834">PR-8834</a>)</li>
<li>Require Qt XmlPatterns only when QtTesting is enabled (<a href="https://github.com/Slicer/Slicer/pull/8835">PR-8835</a>)</li>
</ul>
<h2 id="heading--style">Style</h2>
<ul>
<li>Consistent formatting and indentation of C++ sources (<a href="https://github.com/Slicer/Slicer/pull/7603">PR-7603</a>)</li>
</ul>
<h2 id="heading--extensions">Extensions</h2>
<p><em>Listed below are extensions added, removed or updated since the 5.8 release.</em></p>
<p>The Slicer <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html">extensions manager</a> enables Slicer users to install more than 190 extensions written and contributed by their peers from around the world.</p>
<h3 id="heading--new">New</h3>
<ul>
<li>
<p><a href="https://github.com/andrey-titov/SlicerAnatomyCarve">AnatomyCarve</a>: Allows interactive visualization of 3D medical images by enabling users to perform clipping on segments of their choice</p>
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
<td><img src="https://raw.githubusercontent.com/andrey-titov/SlicerAnatomyCarve/main/AnatomyCarve/Resources/Icons/AnatomyCarve.png" alt="" role="presentation" width="500" height="500"></td>
<td><img src="https://raw.githubusercontent.com/andrey-titov/SlicerAnatomyCarve/main/docs/Screenshot%202025-07-16%20170326.png" alt="" role="presentation" width="690" height="347"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/LOAMRI/Slicer-ASLtoolkit">ASLtoolkit</a>: Applies image processing techniques for Arterial Spin Labeling (ASL) MRI protocols</p>
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
<td><img src="https://raw.githubusercontent.com/LOAMRI/Slicer-ASLtoolkit/refs/heads/main/Slicer_ASLtoolkit.png" alt="" role="presentation" width="500" height="500"></td>
<td><img src="https://raw.githubusercontent.com/LOAMRI/Slicer-ASLtoolkit/refs/heads/main/docs/assets/att_map.png" alt="" role="presentation" width="497" height="500"></td>
</tr>
<tr>
<td><img src="https://raw.githubusercontent.com/LOAMRI/Slicer-ASLtoolkit/refs/heads/main/docs/assets/cbf_map.png" alt="" role="presentation" width="498" height="500"></td>
<td><img src="https://raw.githubusercontent.com/LOAMRI/Slicer-ASLtoolkit/refs/heads/main/docs/assets/t1_blood_gm_map.png" alt="" role="presentation" width="442" height="500"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/murong-xu/SlicerCADSWholeBodyCTSeg">CADSWholeBodyCTSeg</a>: Fully automated segmentation of 167 anatomical structures in CT.</p>
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
<td><img src="https://raw.githubusercontent.com/murong-xu/SlicerCADSWholeBodyCTSeg/main/CADSWholeBodyCTSeg.png" alt="" role="presentation" width="128" height="128"></td>
<td><img src="https://raw.githubusercontent.com/murong-xu/SlicerCADSWholeBodyCTSeg/main/Screenshot_01.png" alt="" role="presentation" width="611" height="500"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/lorenaromeo/SlicerClassAnnotation">ClassAnnotation</a>: Enables the annotation of clinical image datasets generating CSV reports and organized output folders for analysis.</p>
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
<td><img src="https://raw.githubusercontent.com/lorenaromeo/SlicerClassAnnotation/refs/heads/main/ClassAnnotation.png" alt="" role="presentation" width="500" height="500"></td>
<td><img src="https://raw.githubusercontent.com/lorenaromeo/SlicerClassAnnotation/refs/heads/main/ClassAnnotation_screenshot.png" alt="" role="presentation" width="690" height="379"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/SlicerMorph/SlicerDenseCorrespondenceAnalysis">DenseCorrespondenceAnalysis</a>: Dense Correspondence Analysis (DeCA) for Surfaces. DeCA integrates biological insights in the form of homologous landmark points with dense surface registration to provide highly detailed shape analysis of smooth and complex structures that are typically challenging to analyze with sparse manual landmarks alone.</p>
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
<td><img src="https://github.com/SlicerMorph/SlicerDenseCorrespondenceAnalysis/raw/main/DeCA.png" width="200" height="192"></td>
<td><img src="https://na-mic.github.io/ProjectWeek/PW30_2019_GranCanaria/Projects/SlicerMorphGeometricMorphometricToolset/SM_screen.png" alt="" role="presentation" width="690" height="402"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/rwic/SlicerEVARSim">EVARSim</a>: Slicer extension to simulate positioning of endovascular devices.</p>
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
<td><img src="https://raw.githubusercontent.com/rwic/SlicerEVARSim/refs/heads/main/EVARSim/Resources/Icons/EVARSim.png" alt="" role="presentation" width="128" height="128"></td>
<td><img src="https://raw.githubusercontent.com/rwic/SlicerEVARSim/refs/heads/main/EVARSim/Resources/Icons/1.jpeg" width="288" height="500"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/SenonETS/SlicerIGSpineDeformity">IGSpineDeformity</a>: Spine deformity analysis from 3D ultrasound imaging.</p>
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
<td><img src="https://raw.githubusercontent.com/SenonETS/SlicerIGSpineDeformity/main/SlicerIGSpineDeformity_Icon_128x128.png" alt="" role="presentation" width="128" height="128"></td>
<td><img src="https://raw.githubusercontent.com/SenonETS/SlicerIGSpineDeformity/main/sl_01__LaminaLandmark_Labeling/SL_ScreenShot.PNG" alt="" role="presentation" width="690" height="388"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/KitwareMedical/SlicerLayerDisplayableManager">LayerDisplayableManager</a>: An experimental module designed to simplify the integration of new display pipelines in 3D Slicer. It introduces a flexible and extensible framework for managing layered rendering, interaction forwarding, and camera synchronization across multiple pipelines.</p>
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
<td><img src="https://github.com/KitwareMedical/SlicerLayerDisplayableManager/raw/main/Doc/LayerDisplayableManager.png" alt="" role="presentation" width="256" height="256"></td>
<td><img src="https://github.com/KitwareMedical/SlicerLayerDisplayableManager/raw/main/Doc/LayeredDisplayableManager_UML.jpg" alt="" role="presentation" width="690" height="203"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/ciroraggio/SlicerModalityConverter">ModalityConverter</a>: Medical image-to-image (I2I) translation. The ModalityConverter module integrates multiple deep learning models trained for different kind of I2I translation, providing a user-friendly interface.</p>
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
<td><img src="https://raw.githubusercontent.com/ciroraggio/SlicerModalityConverter/main/ModalityConverter.png" alt="" role="presentation" width="690" height="388"></td>
<td><img src="https://raw.githubusercontent.com/ciroraggio/SlicerModalityConverter/main/ModalityConverter/assets/ScreenshotResultExample.png" alt="" role="presentation" width="690" height="397"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/coendevente/SlicerNNInteractive">NNInteractive</a>: Efficient segmentation with nnInteractive, a deep learning-based framework for interactive segmentation of 3D images, allowing for fast voxel-wise segmentation using prompts like points, scribbles, bounding boxes, and lasso.</p>
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
<td><img src="https://raw.githubusercontent.com/coendevente/SlicerNNInteractive/main/slicer_plugin/SlicerNNInteractive/Resources/Icons/SlicerNNInteractive.png" width="200" height="211"></td>
<td><img src="https://raw.githubusercontent.com/coendevente/SlicerNNInteractive/main/img/segmentation_result.jpg" alt="" role="presentation" width="690" height="358"></td>
</tr>
<tr>
<td><img src="https://raw.githubusercontent.com/coendevente/SlicerNNInteractive/main/img/plugin_first_sight.png" alt="" role="presentation" width="658" height="500"></td>
<td></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/4burakfe/SlicerRadioembolizationDosimetry">RadioembolizationDosimetry</a>: Taranis is an open-source suite of Python modules for voxel-based liver radioembolization dosimetry, developed for use within 3D Slicer. It enables lung shunt fraction estimation, predictive dose planning, and post-treatment quantification using PET or SPECT images.</p>
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
<td><img src="https://github.com/4burakfe/SlicerRadioembolizationDosimetry/blob/3e18fb523c923a330f4e347263ff3bbae9c5eae8/taranis_logo.png?raw=true" alt="" role="presentation" width="256" height="256"></td>
<td><img src="https://raw.githubusercontent.com/4burakfe/SlicerRadioembolizationDosimetry/3e18fb523c923a330f4e347263ff3bbae9c5eae8/Screenshot1.jpg" alt="" role="presentation" width="690" height="442"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/SlicerMorph/SlicerANTsPy">SlicerANTsPy</a>: Makes ANTsPy available in 3D Slicer. The ANTsPy library wraps the image processing framework ANTs in Python. It includes reading and writing of medical images, algorithms for registration, segmentation, statistical learning.</p>
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
<td><img src="https://raw.githubusercontent.com/SlicerMorph/SlicerANTsPy/main/SlicerANTsPy.png" alt="" role="presentation" width="256" height="256"></td>
<td><img src="https://raw.githubusercontent.com/SlicerMorph/SlicerANTsPy/main/AntsPy_GUI.png" alt="" role="presentation" width="451" height="500"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/payabvashlab/SlicerHeadCTDeid">SlicerHeadCTDeid</a>: Remove PHI from head CT DICOM metadata, detect and eliminate DICOM images with burned-in text, and strip superficial facial tissue at the air–skin interface to prevent facial feature recognition in 3D reconstructed head CTs.</p>
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
<td><img src="https://raw.githubusercontent.com/payabvashlab/SlicerHeadCTDeid/refs/heads/main/HeadCTDeid/Resources/Icons/HeadCTDeid.png" alt="" role="presentation" width="128" height="128"></td>
<td><img src="https://raw.githubusercontent.com/payabvashlab/SlicerHeadCTDeid/refs/heads/main/screenshot.png" alt="" role="presentation" width="660" height="385"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/dalcalab/SlicerMultiverSeg">SlicerMultiverSeg</a>: Interactive in-context segmentation with MultiverSeg.</p>
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
<td><img src="https://raw.githubusercontent.com/dalcalab/SlicerMultiverSeg/refs/heads/main/MultiverSeg/Resources/Icons/SegmentEditorMultiverSeg.png" alt="" role="presentation" width="500" height="500"></td>
<td><img src="https://raw.githubusercontent.com/dalcalab/SlicerMultiverSeg/refs/heads/main/Screenshots/Demo_1.png" alt="" role="presentation" width="690" height="330"></td>
</tr>
<tr>
<td><img src="https://raw.githubusercontent.com/dalcalab/SlicerMultiverSeg/refs/heads/main/Screenshots/Demo_2.png" alt="" role="presentation" width="690" height="331"></td>
<td><img src="https://raw.githubusercontent.com/dalcalab/SlicerMultiverSeg/refs/heads/main/Screenshots/Demo_3.png" alt="" role="presentation" width="690" height="343"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/OpenwaterHealth/SlicerOpenLIFU">SlicerOpenLIFU</a>: Low Intensity Focused Ultrasound research platform by Openwater.</p>
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
<td><img src="https://github.com/OpenwaterHealth/SlicerOpenLIFU/raw/main/SlicerOpenLIFU.png" alt="" role="presentation" width="128" height="128"></td>
<td><img src="https://github.com/OpenwaterHealth/SlicerOpenLIFU/raw/main/screenshots/1.png" alt="" role="presentation" width="690" height="431"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/chz31/SlicerOrbitSurgerySim">SlicerOrbitSurgerySim</a>: Enables users to interactively register and compare the fit of surgical plates for orbital fracture repair. Users can compare preformed plates with different contours or alternative ways of plate placement.</p>
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
<td><img src="https://raw.githubusercontent.com/chz31/SlicerOrbitSurgerySim/main/orbitSurgerySim.png" alt="" role="presentation" width="500" height="500"></td>
<td><img src="https://raw.githubusercontent.com/chz31/SlicerOrbitSurgerySim/main/orbitSurgerySimScreeshot.png" alt="" role="presentation" width="690" height="331"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/PyTomography/SlicerSPECTRecon">SPECTRecon</a>: Enables the reconstruction of raw SPECT projection data, providing customizable options for image modeling and image reconstruction. The module has a SIMIND to DICOM converter to permit reconstruction of SIMIND Monte Carlo data.</p>
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
<td><img src="https://raw.githubusercontent.com/PyTomography/Slicer/main/Pytomography.png" alt="" role="presentation" width="690" height="350"></td>
<td><img src="https://raw.githubusercontent.com/PyTomography/Slicer/main/images/screenshot.png" alt="" role="presentation" width="690" height="292"></td>
</tr>
</tbody>
</table>
</div></li>
<li>
<p><a href="https://github.com/capenaka/SlicerUpperAirwaySegmentator">UpperAirwaySegmentator</a>: Fully automatic segmentation of the upper airway (nasal cavity, nasopharynx, and oropharynx) on CT and CBCT volumes.</p>
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
<td><img src="https://github.com/capenaka/SlicerUpperAirwaySegmentator/raw/main/UpperAirwaySegmentator/Resources/Icons/UpperAirwaySegmentator_full_icon.png" alt="" role="presentation" width="499" height="500"></td>
<td><img src="https://github.com/capenaka/SlicerUpperAirwaySegmentator/raw/main/Screenshots/11.png" alt="" role="presentation" width="690" height="373"></td>
</tr>
</tbody>
</table>
</div></li>
</ul>
<h3 id="heading--updated">Updated</h3>
<p>All the existing extensions have been maintained and updated to account for API and build environment changes.</p>
<ul>
<li><a href="https://www.slicerheart.org">SlicerHeart extension</a> was extended with two new modules. Virtual Cath Lab and PDA quantification.</li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20232c3d27c1c5490f258bcab3b78b20c684b705.gif" alt="short2" data-base62-sha1="4AiDsvrUzq1I0Q5ckucH39M834x" width="690" height="362" class="animated"></p>
<h3 id="heading--removed">Removed</h3>
<p>Between Slicer 5.8 and Slicer 5.10, the extension SlicerWMA was removed.</p>
<p>List of archived extensions is documented at <a href="https://github.com/Slicer/ExtensionsIndex/blob/main/ARCHIVE/README.md">Slicer/ExtensionsIndex/ARCHIVE/README.md</a>.</p>

---
