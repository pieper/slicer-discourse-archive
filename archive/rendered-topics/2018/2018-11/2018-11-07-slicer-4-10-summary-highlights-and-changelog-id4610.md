# Slicer 4.10: Summary, Highlights and Changelog

**Topic ID**: 4610
**Date**: 2018-11-07
**URL**: https://discourse.slicer.org/t/slicer-4-10-summary-highlights-and-changelog/4610

---

## Post #1 by @jcfr (2018-11-07 13:48 UTC)

<h1><a name="p-17243-table-of-contents-1" class="anchor" href="#p-17243-table-of-contents-1" aria-label="Heading link"></a>Table of Contents</h1>
<ul>
<li><a href="#heading--summary">Summary</a></li>
<li><a href="#heading--highlights">Highlights</a></li>
<li><a href="https://discourse.slicer.org/t/slicer-4-10-summary-highlights-and-changelog/4610/2">Detailed Changelog</a></li>
</ul>
<h1 id="heading--summary">Summary</h1>
<p>The community of 3D Slicer developers is proud to announce that version 4.10 is <a href="http://download.slicer.org/">now available for download</a>. This version introduces ~500 feature enhancements and bug fixes for better performance and stability. It includes more than 20 new-and-improved core modules and more than 25 new-and-improved extensions.</p>
<p>The development of 3D Slicer—including its numerous modules, extensions, datasets, pull requests, patches, issues reports, suggestions—is made possible by users, developers, contributors and commercial partners around the world. This development is funded by various grants and agencies. For more details, please see the 3D Slicer <a href="https://www.slicer.org/wiki/Documentation/4.x/Acknowledgments">Acknowledgments</a> page.</p>
<p><a href="https://www.slicer.org/">slicer.org</a> is the portal to the application, training materials, and the development community.</p>
<p>The <a href="https://www.slicer.org/wiki/Documentation/4.10/Training">Slicer Training</a> page provides a series of tutorials and data sets for training in the use of Slicer.</p>
<p><em>Please note that Slicer continues to be a research package and is not intended for clinical use. Testing of functionality is an ongoing activity with high priority, however, some features of Slicer are not fully tested.</em></p>
<h1 id="heading--highlights">Highlights</h1>
<h2 id="heading--highlights--rendering">Rendering improvements</h2>
<p>Switched to completely reworked rendering infrastructure, which enables 10-100x <strong>faster rendering of complex surface models</strong>, faster <strong>GPU-accelerated volume rendering</strong>, available on a wider range of devices, such as <strong>laptops with integrated GPU</strong>. The minimum required OpenGL version is now 3.2.</p>
<ul>
<li>
<p>GPU volume rendering has now <strong>Surface smoothing</strong> option to remove woodgrain artifacts without increasing rendering time (enable at Volume rendering / Advanced / Techniques / Advanced rendering properties).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28ea022579bace2614b7ae45618e14e82e1216ce.jpeg" data-download-href="/uploads/short-url/5PWsucmoRp1kxZAa48HZtxui1R4.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28ea022579bace2614b7ae45618e14e82e1216ce_2_483x220.jpeg" alt="image" data-base62-sha1="5PWsucmoRp1kxZAa48HZtxui1R4" width="483" height="220" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28ea022579bace2614b7ae45618e14e82e1216ce_2_483x220.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28ea022579bace2614b7ae45618e14e82e1216ce_2_724x330.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28ea022579bace2614b7ae45618e14e82e1216ce_2_966x440.jpeg 2x" data-dominant-color="9D816F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1226×560 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>New <strong>optimized volume rendering quality option</strong>: “Normal” optimized image sampling parameters based on volume size and resolution</p>
</li>
<li>
<p>New <strong>multi-volume rendering</strong> mode (Volume renderig/Display/Rendering: VTK Multi-Volume): experimental, shading and dynamic clipping not supported yet. Example of skull rendered from CT and stripped brain from MRI:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc64a43e3c0af9821b1c0819b2008802744ebfd1.jpeg" data-download-href="/uploads/short-url/A0LWEVPsUnjoLEvf8RKjKMFkPgR.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc64a43e3c0af9821b1c0819b2008802744ebfd1.jpeg" alt="image" data-base62-sha1="A0LWEVPsUnjoLEvf8RKjKMFkPgR" width="303" height="300"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">303×300 28.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><strong>Smooth clipped surfaces</strong>: clipping ROI boundaries are now rendered as smooth planes<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/921f19a3e4aceb719e5c33add4783b39c0405427.jpeg" data-download-href="/uploads/short-url/kQEleqWs5lzSSw5FxOcCTYygPTF.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/921f19a3e4aceb719e5c33add4783b39c0405427_2_483x245.jpeg" alt="image" data-base62-sha1="kQEleqWs5lzSSw5FxOcCTYygPTF" width="483" height="245" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/921f19a3e4aceb719e5c33add4783b39c0405427_2_483x245.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/921f19a3e4aceb719e5c33add4783b39c0405427.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/921f19a3e4aceb719e5c33add4783b39c0405427.jpeg 2x" data-dominant-color="65667E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">700×357 91.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Gradient opacity mapping: gradient opacity mapping can be used to <strong>make soft-tissues</strong> (or other regions with slowly varying image intensity) <strong>semi-transparent</strong>. It now works with both CPU and GPU volume rendering.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb2ee73f715deaf4062842455e6c1a7668929fee.jpeg" data-download-href="/uploads/short-url/sZrpOzMVyxc4DeorlOJkLHSqStw.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb2ee73f715deaf4062842455e6c1a7668929fee.jpeg" alt="image" data-base62-sha1="sZrpOzMVyxc4DeorlOJkLHSqStw" width="624" height="438"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">624×438 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Depth peeling: <strong>transparent surface meshes (models, segmentations) are now correctly rendered</strong> (enable depth peeling by clicking push-pin icon in 3D view, triple-dot button, Use depth peeling checkbox)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36c9b917bf8f5e5b1b4d014dd9b7e4de004bb694.jpeg" data-download-href="/uploads/short-url/7OFYk7ZPVZ3mZvWMjivRUkZRNnm.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36c9b917bf8f5e5b1b4d014dd9b7e4de004bb694.jpeg" alt="image" data-base62-sha1="7OFYk7ZPVZ3mZvWMjivRUkZRNnm" width="481" height="225"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">481×225 53.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><strong>Improved performance on systems with many CPU cores</strong> by using <a href="https://www.threadingbuildingblocks.org/">Threaded Building Blocks (TBB)</a> as SMP backend in VTK. It is enabled by default on Windows. Multi-threaded image filter execution is typically improved by 20-30%. For more details, read the <a href="https://discourse.slicer.org/t/slicer-4-10-summary-highlights-and-changelog/4610#heading--performances">Performances</a> section in the Changelog.</p>
</li>
</ul>
<h2 id="heading--highlights--segmentation">Segmentation improvements</h2>
<p>Many improvements and fixes has been implemented in <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">Segment Editor</a> and related modules.</p>
<ul>
<li>
<p><strong>Convert solid segments to <a href="https://discourse.slicer.org/t/new-segment-editor-effect-for-creating-hollow-objects">hollow objects</a></strong>, for example to create 3D-printable vessel wall from segmented blood pool.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/3/3dcaf6fe895d6bbd23f37fc006f33a66191e40d1.jpg" data-download-href="/uploads/short-url/8ODYv3Esp7oHaIyuhVKlro8AbsZ.jpg?dl=1" title="Hollow segment example"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3dcaf6fe895d6bbd23f37fc006f33a66191e40d1_2_544x500.jpg" alt="Hollow segment example" width="544" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3dcaf6fe895d6bbd23f37fc006f33a66191e40d1_2_544x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3dcaf6fe895d6bbd23f37fc006f33a66191e40d1_2_816x750.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3dcaf6fe895d6bbd23f37fc006f33a66191e40d1_2_1088x1000.jpg 2x" data-dominant-color="75727C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Hollow segment example</span><span class="informations">1842×1690 548 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>New Draw Tube effect added for <strong>segmentation of tubular shapes</strong> (nerves, flexible catheters, etc.) from control points placed in slice or 3D viewers - available in <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects">SegmentEditorExtraEffects</a> extension.</p>
</li>
<li>
<p><strong><a href="https://discourse.slicer.org/t/save-segmentation-directly-to-stl-or-obj-files/2428">Save segmentations directly to STL or OBJ files</a> for 3D printing</strong> or exporting to external modeling software</p>
</li>
<li>
<p><strong>Improve segmentation quality</strong> by setting finer resolution, isotropic voxel size in the segmentation node’s internal labelmap representation. Click the box icon <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff80036411d1ba5196c892be54b39a1e25992d9b.png" alt="image" data-base62-sha1="Asg1mRVggx9mUMBrbqfU7oVMx9p" width="21" height="21"> next to the master volume selector to open the Segmentation geometry window.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/dea4355dab2fbc9e0f400e2d64f54de7c7b766d4.png" data-download-href="/uploads/short-url/vLzOqSqWklB4tLfcgyh6AiRFJm4.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/dea4355dab2fbc9e0f400e2d64f54de7c7b766d4.png" alt="image" data-base62-sha1="vLzOqSqWklB4tLfcgyh6AiRFJm4" width="500" height="431"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">500×431 39.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><strong>Improved 3D update speed</strong> by up to 5x: disable surface smoothing (surface smoothing factor is set to 0) and then 3D view is updated immediately after a segmentation is edited<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a96176130766d3142e8d856197e4f35fecf2b36.png" data-download-href="/uploads/short-url/cVmxzCxP0unHwhHsILxFAal9lUa.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a96176130766d3142e8d856197e4f35fecf2b36_2_483x319.png" alt="image" data-base62-sha1="cVmxzCxP0unHwhHsILxFAal9lUa" width="483" height="319" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a96176130766d3142e8d856197e4f35fecf2b36_2_483x319.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a96176130766d3142e8d856197e4f35fecf2b36_2_724x478.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a96176130766d3142e8d856197e4f35fecf2b36.png 2x" data-dominant-color="DFDEE4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">731×484 37.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><strong>Automatically alignment of slice views</strong>: if slice views are not oriented according to axes of internal labelmap then a warning icon <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/165c6fd3126aa23c4947c20207234983a1bf64c2.png" alt="image" data-base62-sha1="3bOy3yiQ9DvyXtz1umDLedN7MIy" width="21" height="21"> appears. Clicking the icon automatically realigns all slice views.</p>
</li>
<li>
<p><strong>Find small segments</strong> in a large volume easier: click “Jump slices” option to context menu (right-click menu) of segment list to show segment centered in all slice views.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af25e2fc5dbe5d3ab8fe441ee4df3b9c793b1741.png" data-download-href="/uploads/short-url/oZqJcMb1O49QrwvxxBk0Cc4j16x.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af25e2fc5dbe5d3ab8fe441ee4df3b9c793b1741.png" alt="image" data-base62-sha1="oZqJcMb1O49QrwvxxBk0Cc4j16x" width="361" height="221"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">361×221 6.93 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><strong>Improved paint and erase effect</strong>: (1) Made painting/erasing in 3D view optional, (2) Added “smudge” option to paint effect: auto-select segment at click position, and (3) added option to erase in all segments.</p>
</li>
</ul>
<h2 id="heading--highlights--python">Improved Python support</h2>
<ul>
<li>
<p><strong><a href="https://discourse.slicer.org/t/jupyter-notebooks-are-now-usable-in-3d-slicer">Slicer can be used via Jupyter notebooks</a></strong>. Supports auto-complete, inspection (documentation lookup), showing slice and 3D view content in the notebook.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18d37c9434e0ad3614217cf31ddfa051edefff86.jpeg" data-download-href="/uploads/short-url/3xCzaM9ZmBGpgFS0LNDAtTjjxcy.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18d37c9434e0ad3614217cf31ddfa051edefff86_2_464x350.jpeg" alt="image" data-base62-sha1="3xCzaM9ZmBGpgFS0LNDAtTjjxcy" width="464" height="350" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18d37c9434e0ad3614217cf31ddfa051edefff86_2_464x350.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/18d37c9434e0ad3614217cf31ddfa051edefff86_2_696x525.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18d37c9434e0ad3614217cf31ddfa051edefff86.jpeg 2x" data-dominant-color="D9D9DC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">800×603 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><strong>Slicer notebooks</strong> can be launched directly <strong>on the cloud in any web browser</strong>. Can be used on any platforms, even on a phone, <strong>no Slicer installation is necessary</strong>. <a href="https://mybinder.org/v2/gh/slicer/SlicerNotebooks/master">Try now!</a> <a href="https://mybinder.org/v2/gh/slicer/SlicerNotebooks/master"><img src="https://mybinder.org/badge.svg" alt="Binder" width="92" height="20"></a></p>
</li>
<li>
<p><strong>Any Python script can be loaded into Slicer as a CLI module</strong>. User interface in Slicer is generated automatically from module descriptor XML file. See <a href="https://github.com/Radiomics/SlicerRadiomics/tree/master/SlicerRadiomicsCLI">Radiomics module</a> as an example.</p>
</li>
</ul>
<h2>Virtual Reality</h2>
<p><a href="https://blog.kitware.com/slicervirtualreality/">3D Slicer scenes can be viewed in any OpenVR-compatible virtual reality headset</a>(<a href="https://blog.kitware.com/slicervirtualreality/">https://blog.kitware.com/slicervirtualreality/</a>), such as HTC Vive, any Windows MR headset, or Oculus Rift, by a single button click. 3D Slicer supports all rendering modes, including 4D volume rendering. User can walk or “fly” around, look in inside objects. <strong>Individual objects or the entire scene can be moved</strong>, translated, rotated using controllers: can be used for exploring anatomy (may replace 3D printing in some applications),  simulated device placement, interactive 3D registration, etc.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="F_UBoE4FaoY" data-video-title="Pedicle screw insertion in virtual reality" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=F_UBoE4FaoY" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/F_UBoE4FaoY/maxresdefault.jpg" title="Pedicle screw insertion in virtual reality" width="690" height="388">
  </a>
</div>

<h2 id="heading--highlights--other">Other improvements</h2>
<ul>
<li>
<p><strong>Plotting</strong> capabilities have improved with the new <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots">Plots</a> module. Plots can be created directly from tables (stored as .csv files). Line, scatter, bar plot types, various line styles. Custom labels, axes, interactive editing and selection of values.<br>
<img src="https://www.slicer.org/w/img_auth.php/thumb/6/69/VtkPlot.png/800px-VtkPlot.png" alt="Sample plot" width="400" height="250"></p>
</li>
<li>
<p><strong>Custom 3D Slicer-based clinical research or commercial applications</strong> can now be developed and maintained more easily: a new <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate">application template was developed</a> that gives broad control over the application’s look and feel (custom stylesheet, icons, branding, main window content) and content (custom extensions, modules can be bundled, any Slicer core modules can be disabled). The template is already used for building custom research tools, such as <a href="http://salt.slicer.org/">SlicerSALT</a> and multiple clinical software applications.</p>
</li>
<li>
<p><strong>Markup fiducials can be copied to clipboard</strong> and pasted into Excel or into other markup fiducial list.</p>
</li>
<li>
<p><strong>Screen capture</strong>: <strong>Master view can be different from captured views</strong>, therefore for example it is now possible to sweep a slice view and capture it in 3D view (master view is a slice node; capture all frames enabled; layout is 1-up 3D). Video can be exported that repeats the animation multiple times, optionally in forward/backward direction, which enables <strong>sharing very short (few-second) videos on YouTube</strong> or other video players where continuous looped playback is not available.</p>
</li>
<li>
<p><strong>26 new extensions</strong> have been added - <a href="#heading--new">see complete list below</a></p>
</li>
</ul>

---

## Post #2 by @lassoan (2018-11-08 06:49 UTC)

<h1 id="heading--changelog">Changelog</h1>
<ul>
<li>
<a href="#heading--core">Core</a>
<ul>
<li><a href="#heading--performances">Performances</a></li>
<li><a href="#heading--features">Features</a></li>
<li><a href="#heading--fixes">Fixes</a></li>
<li><a href="#heading--internationalizationlocalization">Internationalization/Localization</a></li>
<li><a href="#heading--io">IO</a></li>
<li><a href="#heading--dicom">DICOM</a></li>
<li><a href="#heading--multivolumesequences-support">Multivolume/Sequences Support</a></li>
<li><a href="#heading--api-updates">API Updates</a></li>
<li><a href="#heading--python-scripting">Python Scripting</a></li>
</ul>
</li>
<li>
<a href="#heading--infrastructure">Infrastructure</a>
<ul>
<li><a href="#heading--dashboard-and-factories">Dashboard and Factories</a></li>
<li><a href="#heading--build-system">Build System</a></li>
<li><a href="#heading--custom-slicer-application-support">Custom Slicer application support</a></li>
<li><a href="#heading--dependencies">Dependencies</a></li>
<li><a href="#heading--qt">Qt</a></li>
<li><a href="#heading--itk">ITK</a></li>
<li><a href="#heading--vtk">VTK</a></li>
</ul>
</li>
<li>
<a href="#heading--new-modules">New Modules</a>
<ul>
<li><a href="#heading--plots">Plots</a></li>
</ul>
</li>
<li>
<a href="#heading--improved-modules">Improved Modules</a>
<ul>
<li><a href="#heading--brainstools">BRAINSTools</a></li>
<li><a href="#heading--colors">Colors</a></li>
<li><a href="#heading--data">Data</a></li>
<li><a href="#heading--data-probe">Data Probe</a></li>
<li><a href="#heading--extract-skeleton">Extract Skeleton</a></li>
<li><a href="#heading--endoscopy">Endoscopy</a></li>
<li><a href="#heading--extension-wizard">Extension Wizard</a></li>
<li><a href="#heading--cameras">Cameras</a></li>
<li><a href="#heading--label-map-statistics">Label Map Statistics</a></li>
<li><a href="#heading--landmark-registration">Landmark Registration</a></li>
<li><a href="#heading--markups--fiducials--annotations">Markups / Fiducials / Annotations</a></li>
<li><a href="#heading--models-surface-toolbox">Models, Surface Toolbox</a></li>
<li><a href="#heading--probevolumewithmodel">ProbeVolumeWithModel</a></li>
<li><a href="#heading--sample-data">Sample Data</a></li>
<li><a href="#heading--segmentations--segment-editor--segment-statistics">Segmentations / Segment Editor / Segment Statistics</a></li>
<li><a href="#heading--simple-filters">Simple Filters</a></li>
<li><a href="#heading--scene-views">Scene Views</a></li>
<li><a href="#heading--screen-capture">Screen Capture</a></li>
<li><a href="#heading--transforms">Transforms</a></li>
<li><a href="#heading--vectortoscalarvolume">VectorToScalarVolume</a></li>
<li><a href="#heading--volumes">Volumes</a></li>
<li><a href="#heading--volume-rendering">Volume Rendering</a></li>
</ul>
</li>
<li><a href="#heading--removed-modules">Removed Modules</a></li>
<li>
<a href="#heading--extensions">Extensions</a>
<ul>
<li><a href="#heading--new">New</a></li>
<li><a href="#heading--improved">Improved</a></li>
</ul>
</li>
</ul>
<h2 id="heading--core">Core</h2>
<h3 id="heading--performances">Performances</h3>
<ul>
<li>
<p><a href="https://www.threadingbuildingblocks.org/">Threaded Building Blocks (TBB)</a> is now available as a SMP backend in VTK.</p>
<ul>
<li>
<p>It provides tools for writing parallel C++ programs and VTK can use TBB to improve efficiency of execution of many filters.</p>
</li>
<li>
<p>Using TBB over default multi-threading (Sequential), multi-threaded image filter execution is typically improved by 20-30%. In cases where many threads are created (e.g., pipeline updates performed 10-100 per second, on an 8 or more core machine) and the computation load is very small, the speed may be improved by a factor of 10-20x.</p>
</li>
<li>
<p>On some systems image reslicing performance is increased from 10fps to 130fps by switching from Sequential to TBB.</p>
</li>
<li>
<p>TBB is now enabled by default on Windows. Slicer with TBB has not been tested on Linux and macOS yet.</p>
</li>
</ul>
</li>
<li>
<p>Speedup app startup time by lazily instantiating extension dialog: With the introduction of Qt5, this became an issue because instantiating a QWebEngineView also means that QtWebEngineProcess is started. Read details at <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26960">r26960</a>.</p>
</li>
<li>
<p>Use new, optimized VTK filters for isosurface extraction and plane cutting. vtkDiscreteMarchingCubes replaced with vtkDiscreteFlyingEdges3D, and vtkCutter replaced with vtkPlaneCutter. With TBB backend, computation time for complex surfaces (e.g., obtained by thresholding a noisy grayscale volume) is decreased by a factor of 30-500%.</p>
</li>
<li>
<p>Speedup application launch by 50% when handling of command-line argument displays a message and exits the application. This was done by introducing the function quickExit allowing to quickly terminate the process. More details at <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27015">r27015</a>.</p>
</li>
<li>
<p>Ensure application quickly exit if problem parsing cmd line arguments</p>
</li>
<li>
<p>Improve reslicing performance: When slice position was changed, all inputs of slice image blend filters were reset, which caused measurable slowdown in some cases. This fix makes sure that slice inputs are only reset if they have been changed. It improves reslice speed by a few FPS, and much more in some special cases.</p>
</li>
<li>
<p>Improve rotate to volume plane algorithm. Slice plane is always rotated to the closest matching plane orientation. If a single-slice volume is selected then volume plane normal is selected as slice plane normal. Also added RotateToAxes method, which allows aligning slice with an arbitrary coordinate system, defined by a homogeneous transformation.</p>
</li>
<li>
<p>Hide/show crosshairs actor instead of using the more expensive add/remove.</p>
</li>
<li>
<p>Prevent unnecessary 3D view updates. When slice view was moved or crosshair was moved, 3D view was always updated, even if slice and crosshair were not visible in the 3D view. This caused unnecessary slowdown of slice browsing.</p>
</li>
</ul>
<h3 id="heading--features">Features</h3>
<ul>
<li>
<p>Add 3d views linking capability.</p>
</li>
<li>
<p>Add confirmation dialog for scene close. User can choose to disable confirmation dialog in application settings (“Confirm on scene close” checkbox).</p>
</li>
<li>
<p>Enable high-resolution screenshots of slice views.</p>
</li>
<li>
<p>Update CTKAppLauncher: Add support for interactive process. See <a href="https://discourse.slicer.org/t/static-build-of-qt5-to-update-the-application-launcher-and-support-interactive-process/3801">https://discourse.slicer.org/t/static-build-of-qt5-to-update-the-application-launcher-and-support-interactive-process/3801</a></p>
</li>
<li>
<p>Add the ability to restore extensions from a previous Slicer install.</p>
</li>
<li>
<p>Ensure Slicer process has a name in macOS Activity monitor.</p>
</li>
</ul>
<h3 id="heading--fixes">Fixes</h3>
<ul>
<li>
<p>Report insufficient OpenGL support instead of crashing.</p>
</li>
<li>
<p>Fix Windows remote desktop re-connection on OpenGL version check. If insufficient OpenGL version is found on Windows then a “Retry” option is offered, which closes current remote desktop session and restarts Slicer.</p>
</li>
<li>
<p>Fix high DPI display on windows with multiple screens.</p>
</li>
<li>
<p>Fix passing module paths containing single quote. Add SlicerCorePythonManager::toPythonStringLiteral method to create Python string literals from string values.</p>
</li>
<li>
<p>Create user-specific temporary directory on unix systems. Slicer temporary directory is owned by the user who started Slicer first and is not writeable for other users.</p>
</li>
<li>
<p>Reset scene name when closing the scene.</p>
</li>
<li>
<p>Fix running of script specified with native path separators.</p>
</li>
<li>
<p>Fix crash on scene close caused by annotation ROI node.</p>
</li>
<li>
<p>Fix add and subtract slice blending modes.</p>
</li>
<li>
<p>Fix slice normal flipping by rotate to volume plane. “Rotate to volume” always set slice (X, Y, normal) axes to form a right-handed coordinate system. However, by default, axial and sagittal views are set up with a left-handed coordinate system, so “Rotate to volume” feature flipped the slice normal (slice moved in opposite direction when moving the slider the same direction) for axial and sagittal views. Fix problem by flipping the slice plane normal if and only if input slice coordinate system was left-handed.</p>
</li>
</ul>
<h3 id="heading--internationalizationlocalization">Internationalization/Localization</h3>
<ul>
<li>
<p>Add translation support for loadable modules as well as MRML Widgets.</p>
</li>
<li>
<p>Improve support for Chinese language by fixing qSlicerCoreApplication::loadTranslations() and also encoding special characters for subject hierarchy item attributes. See <a href="https://discourse.slicer.org/t/slicer-mrml-scene-not-loading/2090">https://discourse.slicer.org/t/slicer-mrml-scene-not-loading/2090</a></p>
</li>
<li>
<p>Add more string translation in qSlicerAppMainWindow and qMRMLCaptureToolBar.</p>
</li>
</ul>
<h3 id="heading--io">IO</h3>
<ul>
<li>
<p>Features</p>
<ul>
<li>
<p>Scene view is not created automatically on save. Scene views make large files significantly larger, clutter the scene view list, and scene views are still not very reliable. Therefore, scene view is not created automatically on file save anymore. A screenshot is still saved (same folder and file basename as the .mrml file but with .png extension).</p>
</li>
<li>
<p>Save the scene in same file format as it is loaded from.</p>
</li>
<li>
<p>Update IO manager adding convenience function “openAddMarkupsDialog”</p>
</li>
<li>
<p>Write coordinate system name (currently RAS, in the future it may be RAS or LPS) into OBJ, STL, and PLY file header. This will allow better compatibility with all software that save meshes in LPS coordinate system.</p>
</li>
<li>
<p>Show wait cursor while loading data using Slicer file dialog</p>
</li>
</ul>
</li>
<li>
<p>Fixes</p>
<ul>
<li>
<p>Add Latin1 encoding specification to saved MRML file to ensure correct loading of names with special characters.</p>
</li>
<li>
<p>qSlicerXcedeCatalogReader: Fix reading of description in importVolumeNode.</p>
</li>
<li>
<p>Improve SceneView saving and loading (Fix storage file names in scene views when saving MRB, fix crash in subject hierarchy node when restoring a scene view).</p>
</li>
<li>
<p>Fix save location of nodes with updated file name.</p>
</li>
<li>
<p>Fix range check in vtkMRMLStorageNode::ResetNthFileName.</p>
</li>
<li>
<p>Fix crash when attempted to save node without specifying filename.</p>
</li>
<li>
<p>Fix User color node reverting to File on scene reload</p>
</li>
<li>
<p>Fix filename overrides when saving to MRB.</p>
</li>
<li>
<p>Fix saving of vtkMRMLScriptedModuleNode parameters with special chars</p>
</li>
<li>
<p>Remove full file extension to generate node name when loading volume.</p>
</li>
<li>
<p>Fix loading of custom model display scalar range from scene.</p>
</li>
<li>
<p>Fix confirmation of saved scenes. Confirmation was asked even if “always close” checkbox was checked.</p>
</li>
<li>
<p>Fix volume rendering display node saving.</p>
</li>
<li>
<p>Fix double-saving of VolumeRendering MRML node attribute.</p>
</li>
<li>
<p>Fix too bright material in .obj material files. Models exported into .obj file showed up too bright in Blender and other software. Fix color scale so that sum of diffuse, ambient, and specular component has correct intensity.</p>
</li>
<li>
<p>DiffusionWeightedVolumeNode must only accept unit-length gradients.</p>
</li>
<li>
<p>vtkNRRDWriter: don’t dup ‘space’ field as k-v from node attribute.</p>
</li>
</ul>
</li>
</ul>
<h3 id="heading--dicom">DICOM</h3>
<p>Most changes to the DICOM module are under-the-hood improvements to provide additional flexibility to load a wider variety acquisition types with fewer warning messages and redundant confirmation dialogs. Added extensive options to DICOM header (metadata) viewer to allow exporting all or selected fields for troubleshooting and data mining. Also improved DICOM utility methods to make it easier for developers to import and load DICOM data sets.</p>
<h3>Multivolume/Sequences Support</h3>
<p>MultiVolume support was improved with new features (support of multivolume import from 4D NIfTI), incremental improvements (improved robustness of cardiac CT import, support of import of multivolume as Sequences, improved progress reporting, migration of the infrastructure to use Plotting module in place of VTK plots) and bug fixes.</p>
<h3>API Updates</h3>
<ul>
<li>
<p>Add API to add border around fullscreen app window. On Windows, when turning on OpenGL and using the full screen mode (mainWindow=slicer.util.mainWindow().showFullScreen()), menus and tooltips were no longer visible. By enabling setHasBorderInFullScreen, a one-pixel border is added around the window, which fixes the problem. See <a href="http://doc.qt.io/qt-5/windows-issues.html#fullscreen-opengl-based-windows">http://doc.qt.io/qt-5/windows-issues.html#fullscreen-opengl-based-windows</a></p>
</li>
<li>
<p>User information can be saved to application settings using slicer.app.applicationLogic().GetUserInformation(). User information can be edited in application settings (User panel).</p>
</li>
<li>
<p>Set default attribute value for Scene::Clear(bool). This change allows clearing the scene by simply calling scene.Clear().</p>
</li>
<li>
<p>Add Pick3D function for 3D displayable managers. 3D displayable managers can implement their Pick3D function which takes a RAS point, and finds the display node that was picked. It can be queried using GetPickedNodeID. Implemented for models, segmentations, and volume rendering</p>
</li>
<li>
<p>Allow excluding views from main layout management. See <a href="https://github.com/KitwareMedical/SlicerOpenVR/issues/18">KitwareMedical/SlicerOpenVR#18</a></p>
</li>
<li>
<p>Add pause render functions to qMRMLLayoutManager and qSlicerApplication: When modifying or setting up nodes that may trigger a render event, pauseRender can be called to temporarily stop the view from rendering intermediate steps. Once all modifications have been completed, calling resumeRender will restore the previously stored pause states.</p>
</li>
<li>
<p>Add method in ThreeDViewControllerWidgetPrivate to retrieve ViewLogic from ViewNode.</p>
</li>
<li>
<p>Add color support to 3D view controllers. The layout view property ‘viewcolor’ was only available for slice views. By sinking the LayoutColor member variable from vtkMRMLSliceNode to vtkMRMLAbstractViewNode, and adding accessor functions to qMRMLThreeDWidget and controller similar to those in the slice widgets, this property can now be set to 3D views as well.</p>
</li>
<li>
<p>Add fit option to slicer.util.setSliceViewerLayers().</p>
</li>
<li>
<p>Refactor and improve underlying infrastructure to support browsing capabilities provided by Qt4 (QWebView) and Qt5 (QWebEngineView).</p>
</li>
<li>
<p>Add C++ macros for reading, writing, copying, and printing MRML node properties. For more details, read <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26900">Why use macros instead of functions ?</a>.</p>
</li>
<li>
<p>Add Set/GetOrientationMatrixColumn methods to vtkAddonMathUtilities.</p>
</li>
<li>
<p>Add “IsNodeClassRegistered” function to vtkMRMLScene.</p>
</li>
<li>
<p>Add MeanDiffusivity calculation to vtkDiffusionTensorMathematics class.</p>
</li>
</ul>
<h3>Python Scripting</h3>
<ul>
<li>
<p>Change Slicer’s Python executable to PythonSlicer. This allows using Slicer’s Python executable as an interpreter in PyCharm (to make available auto-complete and method documentation in the editor).</p>
</li>
<li>
<p>Support import of Slicer python packages using PythonSlicer.</p>
</li>
<li>
<p>Support loading module script starting with ‘!#’ as Python CLI.</p>
</li>
<li>
<p>Add python utilities that download, unzip, import, and load DICOM data.</p>
</li>
<li>
<p>Add accessor functions to layout manager and factory.</p>
</li>
<li>
<p>Numpy Integration</p>
<ul>
<li>
<p>Add functions for indicating numpy array modification to slicer.util: arrayFromVolumeModified, arrayFromModelPointsModified and arrayFromGridTransformModified.</p>
</li>
<li>
<p>Add arrayFromVolume support for vtkMRMLDiffusionWeightedVolumeNode.</p>
</li>
<li>
<p>Add convenience function for creating table node from numpy array.</p>
</li>
<li>
<p>Add slicer.util.arrayFromSegment helper function.</p>
</li>
</ul>
</li>
<li>
<p>Wrapping</p>
<ul>
<li>
<p>ModulePanel: Add support for setting/getting module manager from python.</p>
</li>
<li>
<p>Add Python wrapping for all qMRMLSliceWidget methods.</p>
</li>
<li>
<p>Add DICOMUtils.refreshDICOMWidget to refresh browser from database.</p>
</li>
<li>
<p>Throw an exception if getNode() does not find a node.</p>
</li>
<li>
<p>Fix wrapping of QSocketNotifier.</p>
</li>
</ul>
</li>
<li>
<p>Performance</p>
<ul>
<li>
<p>Reduce usage of slicer.util.getNode using simpler, faster, more specific methods like slicer.mrmlScene.GetFirstNodeByClass.</p>
</li>
<li>
<p>Update CTK to ensure PythonQt python module only have init func visible. Reducing the number of symbols the dynamic loader has to go through to find the desired symbol improves your app’s performance". See <a href="https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/DynamicLibraryUsageGuidelines.html#//apple_ref/doc/uid/TP40001928-SW22">https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/DynamicLibraryUsageGuidelines.html#//apple_ref/doc/uid/TP40001928-SW22</a></p>
</li>
</ul>
</li>
<li>
<p>Fixes</p>
<ul>
<li>
<p>Ensure user site-packages are not imported by PythonQt</p>
</li>
<li>
<p>Ensure python is not initialized if Slicer started with --disable-python</p>
</li>
<li>
<p>Do instantiate any scripted plugins when python is disabled</p>
</li>
<li>
<p>Fix copy-paste issue with Python console: When copy-pasting something somewhere before the last character in the command line, the rest of the line was ignored when executing.</p>
</li>
</ul>
</li>
</ul>
<h2 id="heading--infrastructure">Infrastructure</h2>
<h3>Dashboard and Factories</h3>
<ul>
<li>
<p>Switch continuous integration to CircleCI 2.0 leveraging the “slicer/slicer-base” docker image based of “slicer/buildenv-qt5-centos7”. See <a href="https://github.com/Slicer/SlicerBuildEnvironment">https://github.com/Slicer/SlicerBuildEnvironment</a> and <a href="https://github.com/thewtex/SlicerDocker">https://github.com/thewtex/SlicerDocker</a>.</p>
</li>
<li>
<p>Improve dashboard driver script used to test both Slicer application and Slicer extensions as well as custom Slicer-based applications. Dashboard script templates is also easier to customize and read (50% less lines).</p>
</li>
<li>
<p>Add support for uploading extension packages to a Girder based server.</p>
</li>
<li>
<p>“Slicer Nightly” build has been renamed to “Slicer Preview”. See <a href="https://discourse.slicer.org/t/different-dashboard-for-master-and-stable-builds/2091">https://discourse.slicer.org/t/different-dashboard-for-master-and-stable-builds/2091</a>.</p>
</li>
<li>
<p>License information is now tracked for all external projects and remote modules: A license-.txt file is generated for each external projects. This should help compose the list of open source packages used in a Slicer based applications.</p>
</li>
<li>
<p>Add <a href="https://github.com/codespell-project/codespell#readme">runCodespell</a> maintenance script to identify and help fix typo in Slicer source code.</p>
</li>
<li>
<p>Reduce noise reported on the quality dashboard updating CTestCustom warning exception list.</p>
</li>
<li>
<p>Add support for uploading extension package to a Girder based server. See <a href="https://github.com/girder/slicer_extension_manager#readme">https://github.com/girder/slicer_extension_manager#readme</a>.</p>
</li>
</ul>
<h3>Build System</h3>
<ul>
<li>
<p>Support building Slicer against either Qt4 or Qt5.</p>
<ul>
<li>
<p>Configuring Slicer with QT_QMAKE_EXECUTABLE CMake option means that Qt4 is required and defaults to C++98 and VTK7 with legacy OpenGL backend.</p>
</li>
<li>
<p>Configuring Slicer with Qt5_DIR CMake option means Qt5 is required and defaults to C++11 and VTK8 with new OpenGL backend.</p>
</li>
</ul>
</li>
<li>
<p>Subversion is no longer required to configure Slicer.</p>
</li>
<li>
<p>SuperBuild extension templates have been improved.</p>
</li>
<li>
<p>IDE support</p>
<ul>
<li>
<p>Add support for “Slicer --VisualStudioProject” option to automatically open the Visual Studio with the Slicer project.</p>
</li>
<li>
<p>Associate python wrapping Hierarchy targets with an IDE folder. This will ensure that within IDE like VisualStudio each hierarchy targets will be organized in their corresponding “folder”.</p>
</li>
</ul>
</li>
<li>
<p>Update infrastructure used to regenerate the Slicer.crt Certificate authority bundle. The bundle is used to confirm the “digital identity” of peers when establishing secure connection over https. See <a href="https://github.com/Slicer/Slicer/blob/master/Base/QTCore/Resources/Certs/README">Slicer/Base/QTCore/Resources/Certs/README</a>.</p>
</li>
<li>
<p>Streamline future update of major version of ITK and VTK by renaming external project file.</p>
</li>
<li>
<p>Fix build issues with GCC7.</p>
</li>
<li>
<p>Fix building with a virtualenv system python.</p>
</li>
<li>
<p>Update SlicerInitializeOSXVariables CMake module with latest macOS version.</p>
</li>
<li>
<p>Improve build system to fail early if requirements are not met.</p>
</li>
<li>
<p>Improve consistency of external projects (External_*.cmake) in Slicer and CTK.</p>
</li>
<li>
<p>Update dynamic analysis infrastructure. Read <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26993">r26993</a> commit message for more details.</p>
</li>
<li>
<p>Improve support for ninja build tool adding support for CMAKE_JOB_* options. See <a href="https://discourse.slicer.org/t/ninja-build-using-too-many-cores/2304">https://discourse.slicer.org/t/ninja-build-using-too-many-cores/2304</a></p>
</li>
<li>
<p>Fix configuration of valgrind script on macOS</p>
</li>
<li>
<p>Update SuperBuild extension template to work around ExternalProject issue and submit a CMake fix. See <a href="https://gitlab.kitware.com/cmake/cmake/merge_requests/1838">https://gitlab.kitware.com/cmake/cmake/merge_requests/1838</a>  and <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27038">viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27038</a></p>
</li>
<li>
<p>Contribute improvements to <a href="https://cmake-artichoke.readthedocs.io">ExternalProjectDependency</a> CMake module:</p>
<ul>
<li>
<p>Introduce ExternalProject_AlwaysConfigure function</p>
</li>
<li>
<p>Add support for EXTERNAL_PROJECT_ADDITIONAL_DIRS.</p>
</li>
<li>
<p>If set propagate CMAKE_EXPORT_COMPILE_COMMANDS and CMAKE_JOB_*  to all CMake-based external projects.</p>
</li>
<li>
<p>Ensure USES_TERMINAL_* options are always enabled.</p>
</li>
<li>
<p>Fix incorrect behavior supporting variables ending with “-NOTFOUND”.</p>
</li>
</ul>
</li>
<li>
<p>Update UseSlicer to conveniently include ExternalProject CMake module and ensure that the CMAKE_OSX_ variables are passed to all external projects when used in SuperBuild extension.</p>
</li>
</ul>
<h3>Custom Slicer application support</h3>
<ul>
<li>
<p>Modernize the Slicer Custom Application template <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate">https://github.com/KitwareMedical/SlicerCustomAppTemplate</a> and introduce use of cookiecutter template for generating a custom application.</p>
</li>
<li>
<p>Introduce application properties to differentiate Slicer and main app version. Custom Slicer application can have their own metadata (version number, description, …) in addition of the Slicer ones. See <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27316">r27316</a> for more details.</p>
</li>
<li>
<p>Slicer util messageBox now shows current actual application name.</p>
</li>
<li>
<p>Dependencies</p>
<ul>
<li>
<p>Allow custom Slicer application to list other Slicer external projects: This can be done in the YourCusomApp/CMakeLists.txt by updating the list of EXTERNAL_PROJECT_ADDITIONAL_DIRS with the path containing the external project files and (2) appending  to the variable Slicer_ADDITIONAL_DEPENDENCIES.</p>
</li>
<li>
<p>Support configuring and building against custom install of Python. Note that creating a package bundling a custom installation of the python libraries is still NOT supported, instead of failing with an error message, an obvious warning message is now reported.</p>
</li>
</ul>
</li>
<li>
<p>Slicer Refactoring:</p>
<ul>
<li>
<p>Simplify Main.cxx introducing (pre|post)InitializeApplication functions. This allows to remove duplicated code from Slicer-based application.</p>
</li>
<li>
<p>Split main window class to allow re-use in Slicer custom application. Add the class “qSlicerMainWindow” to Base/QTApp library. This allows to use a standard derivation approach in Slicer custom application. See <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27324">r27324</a>.</p>
</li>
<li>
<p>Rename and relocate qSlicerAppErrorReportDialog into Base/QTApp library</p>
</li>
<li>
<p>Rename qSlicerAppAboutDialog to qSlicerAboutDialog and relocate into Base/QTApp library. Update API to support customization of properties like logo and URLs.</p>
</li>
<li>
<p>Introduce “mainApplicationName” SlicerCoreApplication property.</p>
</li>
</ul>
</li>
<li>
<p>Packaging:</p>
<ul>
<li>
<p>Superbuild-type extension can be bundled to the Slicer package by adding it to Slicer_EXTENSION_SOURCE_DIRS.</p>
</li>
<li>
<p>Support macOS packaging of shared third-party libraries installed by extension: This commit allows to specify a variable _FIXUP_BUNDLE_LIBRARY_DIRECTORIES in the extension CMakeLists.txt and ensure that fix-up script will successfully find and copy the shared libraries being a dependency an extension modules.</p>
</li>
<li>
<p>Update UseSlicer add variables for macOS link flags for 3rd-party binaries and libraries. Variables Slicer_INSTALL_THIRDPARTY_EXECUTABLE_LINK_FLAGS and Slicer_INSTALL_THIRDPARTY_LIBRARY_LINK_FLAGS useful for linking executable and binaries that depends on Slicer external projects but are installed in Slicer_INSTALL_THIRDPARTY_BIN_DIR and Slicer_INSTALL_THIRDPARTY_LIB_DIR. This is the case of extensions building tools or libraries that are respectively not CLIs and not loadable module libraries but are expected to be linked against project like VTK or ITK.</p>
</li>
</ul>
</li>
<li>
<p>Slicer CMake modules</p>
<ul>
<li>
<p>Refactor vtkMacroKitPythonWrap to streamline integration in other project</p>
</li>
<li>
<p>Introduce SlicerApplicationOptions, SlicerInitializeBuildType and SlicerInitializeReleaseType CMake modules.</p>
</li>
<li>
<p>Introduce SlicerDirectories CMake module: This module allows to get the (relative) directories for both build and install tree. It was re-factored into its own module to allow Slicer-based app to get the value of the directories.</p>
</li>
<li>
<p>Rename CMake module SlicerBlockSetCMakeOSXVariables to SlicerInitializeOSXVariables</p>
</li>
<li>
<p>Ensure ExternalProjectAddSource module can directly be included and used in custom Slicer application.</p>
</li>
</ul>
</li>
</ul>
<h3 id="heading--dependencies">Dependencies</h3>
<h4 id="heading--qt">Qt</h4>
<ul>
<li>Update from Qt 4.8 to Qt 5.11</li>
</ul>
<h4 id="heading--itk">ITK</h4>
<ul>
<li>
<p>Update ITK to 4.13.1, for more information on the new features available see the <a href="https://discourse.itk.org/t/itk-4-13-has-been-released/549">ITK 4.13 release notes</a>.</p>
</li>
<li>
<p>DICOM image reading, which is provided by ITK, can now optionally use ITK’s DCMTK backend in addition to the GDCM backend.</p>
</li>
<li>
<p>Anticipating the transition to ITK 5, the code has been updated to build with the option ITK_LEGACY_REMOVE set to ON.</p>
</li>
</ul>
<h4 id="heading--vtk">VTK</h4>
<ul>
<li>
<p>Update from VTK 7.1 to VTK 8.2:</p>
<ul>
<li>
<p><a href="https://discourse.slicer.org/t/highlighted-vtk-changes-associated-with-slicer-4-10-virtual-reality-rendering-volume-rendering-python-wraping-opengl-performance-and-threading-management/4574">https://discourse.slicer.org/t/highlighted-vtk-changes-associated-with-slicer-4-10-virtual-reality-rendering-volume-rendering-python-wraping-opengl-performance-and-threading-management/4574</a></p>
</li>
<li>
<p><a href="https://blog.kitware.com/vtk-8-0-0/">https://blog.kitware.com/vtk-8-0-0/</a></p>
</li>
<li>
<p><a href="https://blog.kitware.com/vtk-8-1-0/">https://blog.kitware.com/vtk-8-1-0/</a>.</p>
</li>
</ul>
</li>
</ul>
<h2>New Modules</h2>
<h3 id="heading--plots">Plots</h3>
<ul>
<li>
<p>Features</p>
<ul>
<li>
<p>Add subject hierarchy plugin for plot series node. It is now easy to add/remove series from a chart using visibility icon in subject hierarchy.</p>
</li>
<li>
<p>Add tooltip to plot series widget explaining why x axis column cannot be selected for non-scatter plots.</p>
</li>
<li>
<p>Add logarithmic axis scaling option for plot axes.</p>
</li>
<li>
<p>Add option to specify custom plot axes range.</p>
</li>
<li>
<p>Made plot legend font size adjustable.</p>
</li>
<li>
<p>Read FAQ: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#What_is_the_difference_between_Slicer_Plots_and_Charts_.3F">What is the difference between Slicer Plot and Chart ?</a></p>
</li>
</ul>
</li>
<li>
<p>Python API</p>
<ul>
<li>Add slicer.util.plot function for easy creation of plots from numpy arrays.</li>
</ul>
</li>
</ul>
<h2>Improved Modules</h2>
<h3 id="heading--brainstools">BRAINSTools</h3>
<ul>
<li>Update DWIConvert module to fix conversion of FSL (*.nii.gz) to NRRD file</li>
</ul>
<h3 id="heading--colors">Colors</h3>
<ul>
<li>
<p>Feature:</p>
<ul>
<li>Add centered label display to color node scalar bar: Start/end position of labels were always the start/end of scalar range, which made color names misaligned with the color swatches. The new centered mode allows placing a label right in the center of each color swatch.</li>
</ul>
</li>
</ul>
<h3 id="heading--data">Data</h3>
<ul>
<li>
<p>Features</p>
<ul>
<li>
<p>Subject Hierarchy module has been merged into the Data module as a new tab. Available tabs in the module are “Subject hierarchy”, “Transform hierarchy” and “All nodes”. The “Display tab” has been removed.</p>
</li>
<li>
<p>Add subject hierarchy visibility actions. There are two new actions when right-clicked on the eye icon: (1) Models plugin: “Toggle slice intersection visibility”, (2) Volume Rendering plugin: “Toggle volume rendering” + “Volume rendering options…”.</p>
</li>
</ul>
</li>
<li>
<p>API</p>
<ul>
<li>Add utility function in volume rendering logic called CreateDefaultVolumeRenderingNodes for convenient setup of nodes required for rendering a volume. Only creates nodes if they did not already exist.</li>
</ul>
</li>
<li>
<p>Fixes</p>
<ul>
<li>
<p>Encode subject hierarchy item names: If subject hierarchy item name contained special character (such as &amp;) then it was written directly to the XML file, causing parsing errors.</p>
</li>
<li>
<p>Prevent cell with visibility toggle from being text editable.</p>
</li>
<li>
<p>Fix subject hierarchy treeview popup height.</p>
</li>
<li>
<p>Update combobox label on SubjectHierarchyItemModifiedEvent. The subject hierarchy combobox text would not get updated when its item or one of its parent was modified.</p>
</li>
</ul>
</li>
</ul>
<h3 id="heading--data">Data</h3> Probe
<ul>
<li>
<p>Improve user experience keeping DataProbe height consistent.</p>
</li>
<li>
<p>Fix logic used to hide slice view corner annotations.</p>
</li>
</ul>
<h3>Extract Skeleton</h3>
<ul>
<li>Fix centerline points computation.</li>
</ul>
<h3 id="heading--endoscopy">Endoscopy</h3>
<ul>
<li>
<p>Fix camera update: No camera Modified event is invoked until all camera parameters are updated. Camera view up vector and clipping range is automatically recomputed.</p>
</li>
<li>
<p>Increase maximum replay speed by allowing skipping 50 points (was 10 before).</p>
</li>
</ul>
<h3>Extension Wizard</h3>
<ul>
<li>
<p>Add created module paths to search paths by default.</p>
</li>
<li>
<p>Include name of target in pull request title</p>
</li>
<li>
<p>Fix contribution of extensions targeting a specific version of the ExtensionsIndex.</p>
</li>
</ul>
<h3 id="heading--cameras">Cameras</h3>
<ul>
<li>
<p>Fix vtkMRMLCameraNode::ResetClippingRange(): Far clipping plane was approximated from camera distance form focal point, which was often incorrect.</p>
</li>
<li>
<p>Fix start/end modify for vtkMRMLCameraNode: ModifiedEvent was invoked directly by calling InvokeEvent(), which was not intercepted in DisabledModified state. Fixed by using Modified() method instead.</p>
</li>
</ul>
<h3>Label Map Statistics</h3>
<ul>
<li>Add Median computation support.</li>
</ul>
<h3>Landmark Registration</h3>
<ul>
<li>Known issue: This module has not changed much, but is currently not working pending the resolution of <a href="https://issues.slicer.org/view.php?id=4634">bug #4634</a>.</li>
</ul>
<h3>Markups / Fiducials / Annotations</h3>
<ul>
<li>
<p>Features</p>
<ul>
<li>
<p>Allow cut, copy, and paste of fiducials in markups module.</p>
</li>
<li>
<p>Replace old markup copy/move by new clipboard based new version.</p>
</li>
</ul>
</li>
<li>
<p>Fixes</p>
<ul>
<li>
<p>Ensure vtkMRMLMarkupsNode::AddPointToNthMarkup return value on failure.</p>
</li>
<li>
<p>Fix markups fiducial appearing when clicking on a different slice. When clicked&amp;dragged at a screen position where there was a fiducial at that position on a different slice, the fiducial jumped to the current slice.</p>
</li>
<li>
<p>Ensure markup is visible after clicking in 3d in persistent mode.</p>
</li>
<li>
<p>Prevent MarkupsFiducialStorage saving if invalid coordinate system.</p>
</li>
<li>
<p>Define annotation ROI widget handle size relative to window size.</p>
</li>
</ul>
</li>
</ul>
<h3>Models, Surface Toolbox</h3>
<ul>
<li>
<p>Features</p>
<ul>
<li>
<p>Add direct color mapping option to Models module. Files that contain RGB color for each cell or vertex as 3-component scalar can now be displayed correctly by selecting the new “Direct color mapping” option in models module / display / scalar section.</p>
</li>
<li>
<p>Add Fill Holes step to SurfaceToolbox module</p>
</li>
</ul>
</li>
<li>
<p>Fixes</p>
<ul>
<li>
<p>Fix model scalar thresholding.</p>
</li>
<li>
<p>Fix model clipping by scalar.</p>
</li>
</ul>
</li>
</ul>
<h3 id="heading--probevolumewithmodel">ProbeVolumeWithModel</h3>
<ul>
<li>Add support for volumetric meshes.</li>
</ul>
<h3>Sample Data</h3>
<ul>
<li>
<p>Support adding custom data category.</p>
</li>
<li>
<p>Add Development category that only shows up in Developer mode</p>
</li>
<li>
<p>Add one dataset in the Development category: TinyPatient, containing a 10x10x10 CT and a binary labelmap segmentation with two segments.</p>
</li>
<li>
<p>Stop trying to download data after five attempts (it could get into infinite loop)</p>
</li>
<li>
<p>Add MRBrain sample data set.</p>
</li>
<li>
<p>Try to download sample data again if loading fails.</p>
</li>
</ul>
<h3>Segmentations / Segment Editor / Segment Statistics</h3>
<ul>
<li>
<p>Features</p>
<ul>
<li>
<p>Move Editor module to Legacy category.</p>
</li>
<li>
<p>Allow saving empty segmentation node.</p>
</li>
<li>
<p>Add Jump slices option to context menu of segment list. This makes it easy to find a small segment in a large volume.</p>
</li>
<li>
<p>Make segment editor brush appear in yellow instead of white.</p>
</li>
<li>
<p>Add size scale option to segmentation file export.</p>
</li>
<li>
<p>Add widget to specify labelmap geometry in segmentations. More details in <a>r27288</a> commit message.</p>
</li>
<li>
<p>Improve loading of model node as segmentation. Default representation is set to closed surface, so no conversion to labelmap will happen. Reference geometry spacing is computed from extent of the model (to have approximately 250^3 voxel labelmap) instead of hardcoding to 1.0mm.</p>
</li>
<li>
<p>Add rotate to volume plane warning button to Segment editor. When slice views are not aligned with the internal labelmap representation stored in segmentation node, then a warning button is displayed to the user.</p>
</li>
<li>
<p>Simplify Segment editor automatic thresholding interface. No need to press “Set” button - when a method or options are changed, the threshold is set automatically.</p>
</li>
<li>
<p>Add automatic thresholding to Segment editor. Various methods (Otsu, Huang, Li, etc.) can be used in Segment Editor’s Threshold effect to set threshold value in a reproducible way.</p>
</li>
<li>
<p>Add function to reorder segments in segments table view. In context menu there are two new actions to move selected segment(s) up or down. This is available in the segments table view in both Segment Editor and the Segmentations module.</p>
</li>
<li>
<p>Always set segmentation nrrd file vector axis to “list” kind. When only a few segments were in the segmentation then axis kind was set to complex, RGB, RGBA, …, which was not meaningful and caused some nrrd readers to fail to read the image (see this discussion for an example <a href="https://discourse.itk.org/t/reading-segmentation-file-from-slicer-nrrd-with-multiple-segments-with-simpleitk-shows-exception/808/14">https://discourse.itk.org/t/reading-segmentation-file-from-slicer-nrrd-with-multiple-segments-with-simpleitk-shows-exception/808/14</a>).</p>
</li>
<li>
<p>Improve segment editor scissors outside fill/erase in slice mode. When positive/negative slice clip is enabled, outside fill/erase modified the segmentation on both sides of the slice plane. Improve the behavior so that only the selected side of the slice is filled/erased, because this is generally more useful behavior. If needed, the other side of the slice can be easily erased/filled with an additional scissor operation.</p>
</li>
<li>
<p>Add option to open folder after segmentation export is done.</p>
</li>
<li>
<p>Add Hollow effect to Segment Editor. See <a href="https://discourse.slicer.org/t/new-segment-editor-effect-for-creating-hollow-objects">https://discourse.slicer.org/t/new-segment-editor-effect-for-creating-hollow-objects</a>.</p>
</li>
<li>
<p>Allow loading STL files as segmentation node. See <a href="https://discourse.slicer.org/t/save-segmentation-directly-to-stl-or-obj-files/2428">https://discourse.slicer.org/t/save-segmentation-directly-to-stl-or-obj-files/2428</a>.</p>
</li>
<li>
<p>Add options in Data module to convert labelmap/model to segmentation.</p>
</li>
<li>
<p>Hide background segment after Grow from seeds effect. Determine whether a segment is background by checking corner voxel values (if 5 or more are non-zero, then background).</p>
</li>
<li>
<p>Add direct file export from segmentation. It allows to export segments (all or just visible) directly to STL or OBJ files. Segments may be exported to separate STL files or one merged file. OBJ files contain color and opacity information.</p>
</li>
<li>
<p>Do not reset view when Segmentation master node selected. User may have carefully set up view, so resetting it when switching to Segment Editor module would cause inconvenience.</p>
</li>
<li>
<p>Improve painting and erase effect: (1) Made painting/erasing in 3D view optional, (2) Added “smudge” option to paint effect: auto-select segment at click position, and (3) added option to erase in all segments.</p>
</li>
<li>
<p>Add median to Segmentation statistics module.</p>
</li>
</ul>
</li>
<li>
<p>Python</p>
<ul>
<li>Add slicer.util.arrayFromSegment helper function.</li>
</ul>
</li>
<li>
<p>Performance</p>
<ul>
<li>
<p>Prevent unnecessary memory allocation in vtkMRMLSegmentationNode::GenerateMergedLabelmap.</p>
</li>
<li>
<p>Improve rendering speed of transformed models and segmentations. For more details, read <a>r27244</a> commit message.</p>
</li>
</ul>
</li>
<li>
<p>Fixes</p>
<ul>
<li>
<p>Fix scalar range in colormap exported from segmentation.  When a segmentation node is exported to labelmap volume node, a color node is automatically created. When this colormap is used by volume rendering module, the colors are mapped using scalar range of the lookup table. By default the range was set to [0, 255], which resulted in incorrect mapping. Fixed range by setting it to [0, number of segments].</p>
</li>
<li>
<p>0801966fd BUG: Fixed hiding of node selectors in qMRMLSegmentEditorWidge</p>
</li>
<li>
<p>Fix saving of color nodes of labelmaps exported from segmentation. Color nodes are hidden by default, but hidden nodes cannot be saved in .mrml files (only as .mrb). Updated exporting of segmentation nodes to labelmaps so that the created color nodes are now not hidden.</p>
</li>
<li>
<p>Fix segment jump slice position. While segment center IJK position is stored in a double because that is needed for computations, the values must an integer to make the center always in the middle of a voxel.</p>
</li>
<li>
<p>abd52b276 BUG: Fix small segment geometry widget issues. For more details,  read <a>r27304</a> commit message.</p>
</li>
<li>
<p>Make segment editor auto-threshold more robust. Added exception handling (Kittler-Illingworth method may throw exceptions). Temporarily removed Li method from the GUI (computation may crash).</p>
</li>
<li>
<p>Make late-registered effects show up in Segment editor. When Segment editor module was chosen to be startup module, effects provided in SegmentEditorExtraEffects extension did not show up.</p>
</li>
<li>
<p>Fix joint smoothing mode in segment editor effect.</p>
</li>
<li>
<p>Fix segment color in 3D when polydata has active array.</p>
</li>
<li>
<p>Fix crash in segment editor widget on scene close.</p>
</li>
<li>
<p>Fix loading of segment display properties from scene file.</p>
</li>
<li>
<p>Fix segmentation logic ExportAllSegmentsToModelHierarchy.</p>
</li>
<li>
<p>Fix new segment color after last segment has been removed.</p>
</li>
<li>
<p>Fix segmentation slice intersection update after transform change.</p>
</li>
<li>
<p>SegmentStatistics: Changing parameter set now update selected plugin list.</p>
</li>
<li>
<p>Fix normals in labelmap to surface conversion.</p>
</li>
</ul>
</li>
</ul>
<h3>Simple Filters</h3>
<ul>
<li>
<p>Update SimpleITK version to v1.1.0</p>
</li>
<li>
<p>Avoid installing SimpleITK archive lib and reduce Slicer package size</p>
</li>
</ul>
<h3>Scene Views</h3>
<ul>
<li>
<p>Fix writing of scene view description to scene file keeping HTML tags.</p>
</li>
<li>
<p>Prevent crash when saving MRML scene with SceneView module is disabled.</p>
</li>
<li>
<p>Refactor scene views module to use Qt Widgets instead of a web widget.</p>
</li>
</ul>
<h3>Screen Capture</h3>
<ul>
<li>
<p>Allow frames-per-second specification as alternative to video length: this makes it easier to create videos from sequences that are played at original acquisition speed (e.g., X-ray fluoroscopy frames taken at particular FPS).</p>
</li>
<li>
<p>Allow using not visible master view: It is now possible to have a slice sweep and capture 3D view (master view is a slice node; capture all frames enabled; layout is 1-up 3D).</p>
</li>
<li>
<p>It is now possible to export a video that is playing the animation forward and backwards.</p>
</li>
<li>
<p>Animation can be repeated multiple times. This allows making very short (few-second) videos easier to view in players where continuous looped playback is not available (e.g., YouTube and some media players).</p>
</li>
</ul>
<h3 id="heading--transforms">Transforms</h3>
<ul>
<li>
<p>Extend volume if non-linear transform is hardened: Voxel grid of the volume was not changed when non-linear transform was hardened on it, which could cause clipping of the volume. Now volume is automatically extended to contain the transformed volume.</p>
</li>
<li>
<p>Prevent re-registration of custom ITK transform types: Profiling indicated that it takes noticeable time to re-register when a large number of transform nodes are instantiated.</p>
</li>
<li>
<p>Fix transform hierarchy errors after scene load.</p>
</li>
</ul>
<h3 id="heading--vectortoscalarvolume">VectorToScalarVolume</h3>
<ul>
<li>Expand the module with two new options: (2) Extract a single component from any vector image, not only RGB and (3) Compute the average of all the components of the vector image. Existing option (1) allows computing the luminance from a RGB image.</li>
</ul>
<h3 id="heading--volumes">Volumes</h3>
<ul>
<li>
<p>Fix crash if a volume with empty image data is exported by volumes logic. See <a href="https://discourse.slicer.org/t/convert-label-map-volume-into-a-scalarvolumenode/3550">https://discourse.slicer.org/t/convert-label-map-volume-into-a-scalarvolumenode/3550</a> and <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27291">r27291</a> commit message.</p>
</li>
<li>
<p>Volumes module histogram:</p>
<ul>
<li>
<p>Compute histogram only if needed: If Histogram section in Volumes module is not open then now the histogram is not computed to avoid unnecessary (and potentially lengthy) computation.</p>
</li>
<li>
<p>Updated bin count computation. For values with discrete values, number of values in range will be used as bin count (but max. 1000). For floating-point volumes bin count is always 1000.</p>
</li>
</ul>
</li>
<li>
<p>Update CTK to prevent crash in ctkVTKVolumePropertyWidget</p>
</li>
</ul>
<h3>Volume Rendering</h3>
<ul>
<li>
<p>Features</p>
<ul>
<li>
<p>Support Volume rendering of multiple volumes: Experimental multi-volume renderer allowing to correctly display multiple intermixed volumes. Note that is does not yet support shading.</p>
</li>
<li>
<p>Clipped surfaces are now smooth (looks the same as if the volume was cropped)</p>
</li>
<li>
<p>Improve volume rendering quality in “Adaptive” mode, and add new volume rendering quality option named “Normal”.</p>
</li>
<li>
<p>Improved volume rendering speed: GPU-accelerated volume rendering is now working on many more computers than before. Note that it requires OpenGL version 3.2 or higher.</p>
</li>
<li>
<p>Support configuring available GPU memory in both Application Settings and in Volume Rendering module.</p>
</li>
<li>
<p>Add CT-Air volume rendering preset: It can be used for visualizing regions that appear dark in the image, such as air or blood. Users have often trouble with volume rendering “inverted” images - where dark regions should be visible and bright regions should be hidden (showing airways, blood vessels, ventricles, etc.), but so far all the volume rendering presets are showing bright regions and hiding dark regions. Since creating an inverted transfer function requires a lot of clicking, this preset can be used as a basis and shifted or slightly tuned as needed.</p>
</li>
<li>
<p>Add volume rendering options to Application Settings.</p>
</li>
</ul>
</li>
<li>
<p>API</p>
<ul>
<li>
<p>Add ability to load custom volume rendering presets. See <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27160">r27160</a> commit message.</p>
</li>
<li>
<p>Move volume rendering properties from display node to 3D view node. Note that this change breaks backwards compatibility in terms of loading a scene containing special volume rendering settings, so those settings will not be loaded correctly. For more details, read <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27240">r27240</a> commit message.</p>
</li>
</ul>
</li>
<li>
<p>Fixes</p>
<ul>
<li>
<p>Apply volume rendering preset when re-selecting current preset.</p>
</li>
<li>
<p>Volume rendering image data modified update bug fix. Volume rendering now triggers rendering when underlying image data of a displayed volume node is modified.</p>
</li>
<li>
<p>Fix volume rendering ROI scene compatibility issue</p>
</li>
<li>
<p>Fix old bug with volume rendering preset selection when changing volume. When the rendered volume was changed, then the preset combobox selection stayed at the previous selection, but that selection was not applied. Because of this, many times the user had to change selection to something else than back. In addition it was confusing. Now the selected preset is remembered, and set when the volume changes.</p>
</li>
<li>
<p>Fix volume rendering preset range issue</p>
</li>
<li>
<p>Fix hang when volume rendering in one-up 3D view.</p>
</li>
<li>
<p>Fix disappearing volume rendering.</p>
</li>
</ul>
</li>
</ul>
<h2>Removed Modules</h2>
<ul>
<li>
<p>Remove EMSegment modules and disable support for Tcl and associated python-tcl bridges.</p>
</li>
<li>
<p>Remove OpenIGTLink from Slicer core. Instead, OpenIGTLink modules are distributed in an extension. This allows more frequent updates with fixes and new features.</p>
</li>
</ul>
<h2 id="heading--extensions">Extensions</h2>
<p>The Slicer <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager">extensions manager</a> enables Slicer users to install more than 100 extensions written and contributed by their peers from around the world.</p>
<h3 id="heading--new">New</h3>
<ul>
<li>
<p><a href="https://github.com/pnlbwh/SlicerDiffusionQC#readme"><strong>DiffusionQC</strong></a>: This extension provides a quality-estimation algorithm for diffusion-weighted MRI gradient images, paired with an interactive, graphical review and approval tool. It identifies bad gradients by comparing distance of each gradient to a median line. The median line is obtained from <a href="https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence">KL divergences</a> between consecutive slices. After above processing, it allows user to manually review each gradient: keep or discard them.</p>
</li>
<li>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/LesionSpotlight#Introduction_and_Acknowledgements"><strong>LesionSpotlight</strong></a>: This extension implements a modern image segmentation and enhancement approaches allowing to highlight abnormal white matter voxels in magnetic resonance images. It provides the following modules: <strong>LS Segmenter</strong>: specific for hyperintense Multiple Sclerosis lesion segmentation on T2-FLAIR images. It implements a hyperintense T2-FLAIR lesion segmentation based on a hybrid segmentation algorithm, published by Senra Filho, A.C. See <a href="http://dx.doi.org/10.1007/s11517-017-1747-2">http://dx.doi.org/10.1007/s11517-017-1747-2</a>, <strong>LS Contrast Enhancement</strong>: specific to increase the contrast of abnormal voxels of the same T2-FLAIR images and  <strong>AFT Segmenter</strong>: A simple implementation of another recent MS lesion segmentation algorithm based on the method described in Cabezas M. et al. See <a href="http://dx.doi.org/10.1016/j.cmpb.2014.04.006">http://dx.doi.org/10.1016/j.cmpb.2014.04.006</a></p>
</li>
<li>
<p><a href="https://github.com/KitwareMedical/OsteotomyPlanner/wiki"><strong>OsteotomyPlanner</strong></a>: This extension is used for arranging, cutting and bending closed surface mesh models that represent bone structures. It is an an open source implementation of an open-source tool for osteotomy simulation. It can be used for the planning of surgical procedures and analysis of the resulting structures. The input models for this module would typically be generated by segmenting a CT/MRI/etc dataset. This pre-processing should also include registering the model to a fixed space, in order to allow for direct comparison with reference models.</p>
</li>
<li>
<p><a href="https://github.com/SlicerIGT/SlicerPathReconstruction#readme"><strong>PathReconstruction</strong></a>: This extension is used for creating 3D surface models of catheters from a spatially tracked wire (e.g. transform updated through <strong>SlicerOpenIGTLink</strong>). The user specifies which transform corresponds to the wire then records points along the length of the catheters. The main output is a pair of model nodes for each catheter - one model node for storing raw points, and one for storing a surface representation of the catheter.</p>
</li>
<li>
<p><a href="https://github.com/lassoan/PedicleScrewSimulator/#readme"><strong>PedicleScrewSimulator</strong></a>: This extension is used for pedicle screw insertion training.</p>
</li>
<li>
<p><a href="https://github.com/gsi-biomotion/SlicerRegistrationQA/wiki/Introduction-and-Tutorial"><strong>RegQAExtension</strong></a>: This extension enables quality assurance (QA) for image registration. It can perform different test, both qualitative and quantitative to estimate registration quality. It can also create output files, which can serve as documentation for specific registration QA.</p>
</li>
<li>
<p><a href="https://github.com/SNRLab/SNRMeasurement#readme"><strong>SNRMeasurement</strong></a>: This extension provides a command line module (CLI) allowing to calculate signal-to-nose ratio of MR images using “difference image” method.</p>
</li>
<li>
<p><a href="https://github.com/PerkLab/SlicerSandbox"><strong>Sandbox</strong></a>: This extension is a collection of utilities that are not polished implementations but can be useful to users. It provides the LineProfile module allowing to compute the intensity profile in an image along a line.</p>
</li>
<li>
<p><a href="https://github.com/lassoan/SlicerSegmentMesher#readme"><strong>SegmentMesher</strong></a>: This extension is used for creating volumetric meshes from segmentation using Cleaver2 or TetGen. <a href="https://sciinstitute.github.io/cleaver.pages">Cleaver2</a> mesher is freely usable, without any restrictions. <a href="http://www.tetgen.org">TetGen</a> mesher is only free for private, research, and educational use (see <a href="https://people.sc.fsu.edu/~jburkardt/examples/tetgen/license.txt">license</a> for details).</p>
</li>
<li>
<p><a href="https://github.com/KitwareMedical/ShapeRegressionExtension#readme"><strong>ShapeRegressionExtension</strong></a>: This extension enables the computation and visualization of time-regressed shapes in a collection of 3D shape inputs associated to a linear variable. It provides two modules: <strong>RegressionComputation</strong> and <strong>RegressionVisualization</strong>.</p>
</li>
<li>
<p><a href="https://github.com/KitwareMedical/SlicerSkeletalRepresentation#readme"><strong>SkeletalRepresentation</strong></a>: This extension provides modules to establish, refine and visualize skeletal representation model of an object. The skeletal representation is then used as a model for shape analysis.</p>
</li>
<li>
<p><a href="https://github.com/JoostJM/SlicerCaseIterator#readme"><strong>SlicerCaseIterator</strong></a>: This extension provides a simple scripted module allowing to iterate through a set of cases defined in a csv-file. It’s purpose is to streamline the segmentation of image datasets by handling loading and saving.</p>
</li>
<li>
<p><a href="https://medicalimageanalysistutorials.github.io/SlicerCochlea"><strong>SlicerCochlea</strong></a>: The cochlea is a very important part of the inner ear. It is responsible for the transfer of audio signals to the brain. There are two modules in this extension: <strong>Cochlea Registration</strong> module allowing to register and fuse cochlea images from different modalities and <strong>Cochlea Segmentation</strong> module allowing to segment out the cochlea structure, scala tympani and other scalae (media and vestibuli) and to measure the length and the size of the scala tympani. Both modules require a few seconds to complete the tasks. They use a customized set of parameters from the <a href="https://github.com/SuperElastix/elastix">elastix toolbox</a> itself based on <a href="https://itk.org/">Insight Toolkit (ITK)</a>.</p>
</li>
<li>
<p><a href="https://github.com/SlicerFab/SlicerFab#readme"><strong>SlicerFab</strong></a>: This extension is used for fabrication of physical objects. It supports a bitmap-based multimaterial 3D printing workflow for the rapid and highly accurate generation of physical models directly from volumetric data stacks. Learn more, reading <a href="https://www.researchgate.net/publication/325436455_From_Improved_Diagnostics_to_Presurgical_Planning_High-Resolution_Functionally_Graded_Multimaterial_3D_Printing_of_Biomedical_Tomographic_Data_Sets">From Improved Diagnostics to Presurgical Planning: High-Resolution Functionally Graded Multimaterial 3D Printing of Biomedical Tomographic Data Sets</a>.</p>
</li>
<li>
<p><a href="https://github.com/Slicer/SlicerJupyter#readme"><strong>SlicerJupyter</strong></a>: This extension provides a Jupyter kernel, which allows running Jupyter notebooks in 3D Slicer. There are two options to run the notebooks: <strong>Option 1</strong>: Run using Binder, no installation or setup is needed, just click on <a href="https://mybinder.org/v2/gh/slicer/SlicerNotebooks/master">this link</a> and start using Slicer via Jupyter notebook in your web browser. <strong>Option 2</strong>: Run Slicer and Jupyter on your own computer after following <a href="https://github.com/Slicer/SlicerJupyter#option-2-run-slicer-and-jupyter-on-your-own-computer">these instructions</a>.</p>
</li>
<li>
<p><a href="https://github.com/QIICR/SlicerLayoutButtons#readme"><strong>SlicerLayoutButtons</strong></a>: This extension facilitates the selection/display of labels or foreground/background images for a specific slice view. The module panel consists of “colored” buttons that are arranged with the exact same layout as the current slice view layout used in 3D Slicer. Anytime the slice view layout changes, the module widget will adapt its layout and buttons so that those buttons “mirror” the exact same layout. Furthermore information are provided for each button about the currently selected label and background/foreground image for each corresponding slice view.</p>
</li>
<li>
<p><a><strong>SlicerOpenIGTLink</strong></a>: This extension adds <a href="http://openigtlink.org/">OpenIGTLink</a> communication interface to 3D Slicer to exchange real-time imaging, tracking, and other data.</p>
</li>
<li>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/PETCPhantomAnalysis"><strong>SlicerPETPhantomAnalysis</strong></a>: This extension is used for the Analysis of Uniform Cylinder Phantoms in PET scans. Quantitative verification of calibration and spatial homogeneity of PET scanners is an essential prerequisite for quantitative analysis of clinical PET scans. For this purpose uniform cylindrical phantoms are commonly utilized. The provided module enables automated analysis of produced PET scans.</p>
</li>
<li>
<p><a href="https://github.com/SlicerProstate/SlicerProstateAblation#overview"><strong>SlicerProstateAblation</strong></a>: This extension was designed to support the workflow of the in-bore MRI-guided therapies. It was developed and tested to support transperineal prostate cryo-ablation procedures in the <a href="http://www.brighamandwomens.org/research/amigo/default.aspx">Advanced Multimodality Image Guided Operating (AMIGO)</a> at the Brigham and Women’s Hospital, Boston. Its applicability to other types of procedures has not been evaluated. See also <a href="https://ncigt.org/prostate-biopsy">https://ncigt.org/prostate-biopsy</a>.</p>
</li>
<li>
<p><a href="https://github.com/VASST/SlicerVASST#readme"><strong>SlicerVASST</strong></a>: This extension contains a number of modules developed by the VASST laboratory at the Robarts Research Institute. It provides access to RobartsVTK, a library for visualization and image processing. It provides the following modules: <strong>EpiGuide</strong>, a guidelet used to perform image guided navigation for epidural needle insertions. It requires a Plus connections to an image and tracking server, as well as a single element transducer server, <strong>NeoGuidance</strong>, a loadable module enabling surgical guidance for NeoChord surgical procedures.</p>
</li>
<li>
<p><a href="https://github.com/VASST/SlicerVideoCameras#readme"><strong>SlicerVideoCameras</strong></a>: This extension is used for interacting and calibrating videoCameras using 3D Slicer streamed from a PlusServer. It provides the following modules: <strong>Intrinsic calibration</strong>: Assuming a <a href="http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html">pinhole model</a>, this module discovers the camera parameters using a <a href="https://github.com/VASST/SlicerVideoCameras/blob/master/Documentation/checkerboardPattern.png">6x9 checkerboard</a> or <a href="https://github.com/VASST/SlicerVideoCameras/blob/master/Documentation/circles_pattern.png">4x11 circle pattern</a> image. <strong>Tracker registration</strong>: This module enables the registration of an external tracker marker attached to the camera and the camera coordinate system.</p>
</li>
<li>
<p><a href="https://github.com/KitwareMedical/SlicerVirtualReality#readme"><strong>SlicerVirtualReality</strong></a>: This extension enables user to interact with the 3D scene using virtual reality. The extension works with all OpenVR-compatible headsets, such as <a href="https://github.com/KitwareMedical/SlicerVirtualReality/#setup-htc-vive">HTC Vive</a>, all <a href="https://github.com/KitwareMedical/SlicerVirtualReality/#setup-windows-mixed-reality">Windows Mixed Reality headsets</a> (by Acer, Lenovo, HP, etc.), and with <a href="https://github.com/KitwareMedical/SlicerVirtualReality/#setup-oculus-rift">Oculus Rift</a>. See this <a href="https://www.youtube.com/watch?v=F_UBoE4FaoY">YouTube video</a> as well as this <a href="https://blog.kitware.com/slicervirtualreality/">Kitware blog post</a> for some more background and application examples.</p>
</li>
<li>
<p><a href="https://github.com/SlicerDMRI/SlicerWMA#readme"><strong>SlicerWMA</strong></a>: This extension  provides the <a href="https://github.com/SlicerDMRI/whitematteranalysis">WhiteMatterAnalysis</a> clustering and tractography analysis python package and its dependencies installed within Slicer’s Python environment.</p>
</li>
<li>
<p><a href="https://github.com/gattia/Slicer-T2mapping#readme"><strong>T2mapping</strong></a>: This extension  can be used to create a T2 Map from a 4D multi-echo MRI.</p>
</li>
<li>
<p><a href="https://github.com/faustomilletari/TOMAAT-Slicer#readme"><strong>TOMAAT</strong></a>: This extension allows to run deep learning based analysis of medical volumes through inference service deployed on the cloud via <em>TOMAAT</em>. Learn more at <a href="https://tomaat.readthedocs.io">https://tomaat.readthedocs.io</a></p>
</li>
<li>
<p><a href="https://github.com/VASST/VASSTAlgorithms#readme"><strong>VASSTAlgorithms</strong></a>: This extension contains a number of algorithms for algebra, geometry, registration, and other library functions. It is a dependency of <strong>SlicerVASST</strong> and <strong>SlicerVideoCameras</strong> extensions.</p>
</li>
</ul>
<h3 id="heading--improved">Improved</h3>
<ul>
<li>
<p><a href="https://github.com/QIICR/DSC_Analysis#readme"><strong>DSC_Analysis</strong></a></p>
</li>
<li>
<p><a href="https://github.com/SlicerIGT/SlicerMarkupsToModel"><strong>MarkupsToModel</strong></a>: Added multiple new algorithms for generating approximating curves from markup point list.</p>
</li>
<li>
<p><a href="https://github.com/QIICR/PkModeling#readme"><strong>PkModeling</strong></a></p>
</li>
<li>
<p><a href="https://qiicr.gitbooks.io/quantitativereporting-guide/content/"><strong>QuantitativeReporting</strong></a></p>
</li>
<li>
<p><a href="http://dmri.slicer.org/"><strong>SlicerDMRI</strong></a></p>
<ul>
<li>
<p>Interactive multi-tensor unscented Kalman filter tractography.</p>
</li>
<li>
<p>New white matter atlas <a href="http://dmri.slicer.org/atlases/">publicly released</a>.</p>
</li>
<li>
<p>New module templates for the Extension Wizard for DWI and tractography data.</p>
</li>
<li>
<p>New utility modules to extract DWI shells and downsample tractography.</p>
</li>
<li>
<p>Improvements to multishell DWI I/O, display speed, and general fixes.</p>
</li>
</ul>
</li>
<li>
<p><a href="https://github.com/lassoan/SlicerElastix#readme"><strong>SlicerElastix</strong></a></p>
</li>
<li>
<p><a href="https://github.com/SlicerIGT/SlicerIGT#readme"><strong>SlicerIGT</strong></a>: Fiducial registration wizard module can match two fiducial lists even if points are missing or out of order.</p>
</li>
<li>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerRT"><strong>SlicerRT</strong></a></p>
<ul>
<li>
<p>Improved RT structure set import stability</p>
</li>
<li>
<p>Added capability to use external beam dose engines defined in a separate extension</p>
</li>
<li>
<p>Dose volume histogram</p>
<ul>
<li>
<p>Added Dose surface histogram feature</p>
</li>
<li>
<p>Use new Plots infrastructure: more interactive and responsive charts, improved data interoperability for DVH tables</p>
</li>
</ul>
</li>
<li>
<p>Isodose</p>
<ul>
<li>
<p>Can now handle different isodose level sets for different dose volumes</p>
</li>
<li>
<p>Numerous fixes around dose scalar bars</p>
</li>
</ul>
</li>
</ul>
</li>
</ul>

---
