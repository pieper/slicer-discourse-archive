# Slicer 4.10.2: Summary, Highlights and Changelog

**Topic ID**: 6974
**Date**: 2019-05-30
**URL**: https://discourse.slicer.org/t/slicer-4-10-2-summary-highlights-and-changelog/6974

---

## Post #1 by @Sam_Horvath (2019-05-30 21:44 UTC)

<h1><a name="p-24679-table-of-contents-1" class="anchor" href="#p-24679-table-of-contents-1" aria-label="Heading link"></a>Table of Contents</h1>
<ul>
<li><a href="#heading--summary">Summary</a></li>
<li><a href="#heading--changelog">Changelog</a>
<ul>
<li><a href="#heading--fixes">Fixes</a>
<ul>
<li><a href="#heading--dicom">DICOM</a></li>
<li><a href="#heading--markups">Markups</a></li>
<li><a href="#heading--display">Display</a></li>
<li><a href="#heading--segmentations">Segmentations</a></li>
<li><a href="#heading--qwebengine">QWebEngine</a></li>
<li><a href="#heading--build-system">Build System</a></li>
</ul>
</li>
</ul>
</li>
</ul>
<h1 id="heading--summary"> Summary </h1>
<p>The community of 3D Slicer developers is proud to announce that version 4.10.2 is<a href="http://download.slicer.org/"> now available for download</a>. This patch release introduces ~30 bug fixes for better performance and stability.  It features many usability fixes for the segmentation and display modules.</p>
<p>The development of 3D Slicer—including its numerous modules, extensions, datasets, pull requests, patches, issues reports, suggestions—is made possible by users, developers, contributors and commercial partners around the world. This development is funded by various grants and agencies. For more details, please see the 3D Slicer<a href="https://www.slicer.org/wiki/Documentation/4.x/Acknowledgments"> Acknowledgments</a> page.</p>
<p><a href="https://www.slicer.org/">slicer.org</a> is the portal to the application, training materials, and the development community.</p>
<p>The<a href="https://www.slicer.org/wiki/Documentation/4.10/Training"> Slicer Training</a> page provides a series of tutorials and data sets for training in the use of Slicer.</p>
<p><em>Please note that Slicer continues to be a research package and is not intended for clinical use. Testing of functionality is an ongoing activity with high priority, however, some features of Slicer are not fully tested.</em></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84fe95245d8df4542b1d2ae83ac40e50402b8f96.jpeg" data-download-href="/uploads/short-url/iYwsWhrrvbKsL85q1dosKQ0HPBI.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84fe95245d8df4542b1d2ae83ac40e50402b8f96_2_690x419.jpeg" alt="image" data-base62-sha1="iYwsWhrrvbKsL85q1dosKQ0HPBI" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84fe95245d8df4542b1d2ae83ac40e50402b8f96_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84fe95245d8df4542b1d2ae83ac40e50402b8f96_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/84fe95245d8df4542b1d2ae83ac40e50402b8f96_2_1380x838.jpeg 2x" data-dominant-color="858484"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2715×1649 951 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><em>Improved Landmark Registration through Markups fixes</em></p>
<h1 id="heading--changelog"> Changelog </h1>
<h2 id="heading--fixes">Fixes</h2>
<h3 id="heading--dicom">DICOM</h3>
<p>Improve  DICOMScalarVolumePlugin robustness for multi-frame volumes by preventing errors when examining slice positions in a multi-frame DICOM file (just log a warning).</p>
<ul>
<li>Prevent confirm application close dialog from showing twice on macOS</li>
</ul>
<h3 id="heading--markups">Markups</h3>
<ul>
<li>
<p>Fix for the fiducial selection bug in 4.10: <a href="https://issues.slicer.org/view.php?id=4634">https://issues.slicer.org/view.php?id=4634</a></p>
<ul>
<li>Relies on a VTK update to fix visibility issues in widgets used for seed points</li>
</ul>
</li>
</ul>
<h3 id="heading--display">Display</h3>
<ul>
<li>
<p>Fix Data Probe display for scenes with custom slice view names</p>
</li>
<li>
<p>Improve Volume Rendering module  ensuring corrupted display nodes are ignored</p>
</li>
<li>
<p>Fix image not filling the entire slice view</p>
<ul>
<li>In some cases, for example, after changing font scale on Windows10, images only filled the bottom-left corner of slice view.</li>
</ul>
</li>
<li>
<p>Hide model slice display actor when model is not visible on slice</p>
<ul>
<li>Reduce “No input data” error spam</li>
</ul>
</li>
<li>
<p>Fix distance encoded projection in Slice view by normalizing the plane normal</p>
<ul>
<li>Implicit plane function for calculating distance now uses SliceXYToRAS matrix and  scale the distance is in the Z direction</li>
</ul>
</li>
</ul>
<h3 id="heading--segmentations">Segmentations</h3>
<ul>
<li>
<p>Fix loading of segmentation from generic Nrrd file</p>
<ul>
<li>
<p>Segmentation could not be loaded directly from a generic Nrrd file (that did not have any segmentation specific fields) because segment name was not filled and uninitialized segment name caused a crash.</p>
</li>
<li>
<p>Segment ID is now used as segment name if the segment name is not specified.</p>
</li>
</ul>
</li>
<li>
<p>Prevent SegmentStatistics module from causing a crash when invalid inputs were specified</p>
</li>
<li>
<p>Fix warning when exporting segmentation to labelmap</p>
</li>
<li>
<p>Fix Segment Editor “Show 3D” button state</p>
<ul>
<li>In some cases (when first segment was not the first segment alphabetically), the “Show 3D” button had to be clicked twice to actually hide the segmentation. This was fixedby not invoking segment modified events until all the segments have the same representations.</li>
</ul>
</li>
<li>
<p>Fix regression ensuring mouse cursor effect is shown in Segment Editor</p>
<ul>
<li>
<p>Since recent updates in VTK Qt widget, when a Segment Editor effect was active the mouse cursor remained the default arrow cursor.</p>
</li>
<li>
<p>Fixed by adding setViewCursor() method that calls appropriate method to change the cursor shape, and calling this method from Segment Editor.</p>
</li>
</ul>
</li>
<li>
<p>Fix export of segmentations to file with illegal characters in node name</p>
</li>
<li>
<p>Improve  Undo support to always restore deleted segments</p>
</li>
<li>
<p>Remove unneeded representation conversions when hardening transform on segmentation</p>
<ul>
<li>
<p>When hardening segmentation on a segmentation node containing a planar contour master and a closed surface, the conversion was performed multiple times, so it seemed like the application hang. Disabling an event for the hardening operation fixes this issue.</p>
</li>
<li>
<p><a href="https://discourse.slicer.org/t/harden-transform-on-large-segmentation-hangs-3d-slicer/5643">https://discourse.slicer.org/t/harden-transform-on-large-segmentation-hangs-3d-slicer/5643</a></p>
</li>
</ul>
</li>
</ul>
<h3 id="heading--qwebengine">QWebEngine</h3>
<ul>
<li>
<p>Stability fixes for QWebEngine</p>
<ul>
<li>
<p>Relay QWebEngineView signals to qSlicerWebWidget</p>
</li>
<li>
<p>Re-factor WebChannelTransport initialization</p>
</li>
</ul>
</li>
</ul>
<h3 id="heading--build-system">Build System</h3>
<ul>
<li>
<p>ExtensionBuildSystem Fixes</p>
<ul>
<li>
<p>Fix issues preventing build of dependent extensions. See <a href="https://issues.slicer.org/view.php?id=4247">https://issues.slicer.org/view.php?id=4247</a></p>
</li>
<li>
<p>Fix build of extensions using Ninja generator</p>
</li>
<li>
<p>Improve test robustness</p>
</li>
</ul>
</li>
<li>
<p>Update SimpleITK to add support for CMake instance, platform and toolset</p>
<ul>
<li>See <a href="https://discourse.slicer.org/t/3d-slicer-windows-10-build-fail-only-simpleitk-project/6727">https://discourse.slicer.org/t/3d-slicer-windows-10-build-fail-only-simpleitk-project/6727</a></li>
</ul>
</li>
</ul>

---

## Post #2 by @sd2018 (2019-05-30 22:15 UTC)

<p>Hi Sam,</p>
<p>Why are you sending this to me?</p>

---

## Post #3 by @jcfr (2019-06-03 14:20 UTC)

<p><a class="mention" href="/u/sd2018">@sd2018</a> Users subscribing to the forum will receive a notification when there is a post added to the “Announcements” category, you should be able to tweak your notification settings, screenshot below should provide some context and help you do this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3117b9392914dd59e11f247cf65f7cb7b978aa30.png" data-download-href="/uploads/short-url/70idR2TzDuhn0Qmujikfl89Nvos.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3117b9392914dd59e11f247cf65f7cb7b978aa30_2_690x252.png" alt="image" data-base62-sha1="70idR2TzDuhn0Qmujikfl89Nvos" width="690" height="252" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3117b9392914dd59e11f247cf65f7cb7b978aa30_2_690x252.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3117b9392914dd59e11f247cf65f7cb7b978aa30_2_1035x378.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3117b9392914dd59e11f247cf65f7cb7b978aa30.png 2x" data-dominant-color="F3F6F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1117×409 43.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @ButuiHu (2019-06-14 14:09 UTC)

<p>Great work! I wonder maybe we could have a download url related to the version? Something like <a href="https://download.slicer.org/bitstream/3dslicer-linux-4.10.1.tar.gz" rel="nofollow noopener">https://download.slicer.org/bitstream/3dslicer-linux-4.10.1.tar.gz</a>.</p>

---

## Post #5 by @jcfr (2019-06-18 07:16 UTC)

<p><a class="mention" href="/u/butuihu">@ButuiHu</a> Latest Slicer release can be downloaded from <a href="https://download.slicer.org/" rel="nofollow noopener">https://download.slicer.org/</a> , previous releases can be found at <a href="http://slicer.kitware.com/midas3/folder/274" rel="nofollow noopener">http://slicer.kitware.com/midas3/folder/274</a>.</p>
<p>If you are looking for the sources, you can find them at <a href="https://github.com/Slicer/Slicer" rel="nofollow noopener">https://github.com/Slicer/Slicer</a></p>

---
