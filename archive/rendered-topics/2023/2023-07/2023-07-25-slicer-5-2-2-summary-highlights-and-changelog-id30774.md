# Slicer 5.2.2: Summary, Highlights and Changelog

**Topic ID**: 30774
**Date**: 2023-07-25
**URL**: https://discourse.slicer.org/t/slicer-5-2-2-summary-highlights-and-changelog/30774

---

## Post #1 by @jcfr (2023-07-25 05:41 UTC)

<h1><a name="p-98138-table-of-content-1" class="anchor" href="#p-98138-table-of-content-1" aria-label="Heading link"></a>Table of content</h1>
<ul>
<li><a href="#heading--summary">Summary</a></li>
<li><a href="#heading--highlights">Highlights</a></li>
<li><a href="#heading--changlog">Detailed Changlog</a></li>
</ul>
<h1 id="heading--summary">Summary</h1>
<p>Slicer 5.2.2 is a patch release published in February 2023, aimed at addressing various issues reported by the community and providing bug fixes, enhancements, and improvements. This release ensures a smoother and more stable user experience.</p>
<p>For more details and a comprehensive list of changes, enhancements, and highlights in the Slicer 5.2 release, please refer also to the <a href="https://discourse.slicer.org/t/slicer-5-2-summary-highlights-and-changelog/26916">Slicer 5.2 release notes</a></p>
<p><em>Please note that Slicer continues to be a research package and is not intended for clinical use (clinical users must obtain the necessary ethics or regulatory approvals).</em></p>
<h1 id="heading--highlights">Highlights</h1>
<h2 id="heading--dual-monitor">Dual monitor and picture-in-picture view layout</h2>
<p>Slicer can now display 3D, slice, plot, etc. views in <a href="https://discourse.slicer.org/t/new-feature-dual-monitor-and-picture-in-picture-view-layout/27218">multiple windows</a> and not just in the main application window. See <a href="https://youtu.be/PJuXSXkPvHs">1-minute demo video</a></p>
<div class="md-table">
<table>
<thead>
<tr>
<th><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/945d84356bec6a78f51de0c0ad19291699ff915c.jpeg" data-download-href="/uploads/short-url/lav1t0wcSOYkcp2uRBopGZhZ0sc.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/945d84356bec6a78f51de0c0ad19291699ff915c_2_690x425.jpeg" alt="image" data-base62-sha1="lav1t0wcSOYkcp2uRBopGZhZ0sc" width="690" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/945d84356bec6a78f51de0c0ad19291699ff915c_2_690x425.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/945d84356bec6a78f51de0c0ad19291699ff915c_2_1035x637.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/945d84356bec6a78f51de0c0ad19291699ff915c_2_1380x850.jpeg 2x" data-dominant-color="534150"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1184 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></th>
<th><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7f2e20028e00ce5877ceed72bf5d6116abc577a.jpeg" data-download-href="/uploads/short-url/x5UFwlp2G0OSDXgkUhJakKJOD5E.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7f2e20028e00ce5877ceed72bf5d6116abc577a_2_690x417.jpeg" alt="image" data-base62-sha1="x5UFwlp2G0OSDXgkUhJakKJOD5E" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7f2e20028e00ce5877ceed72bf5d6116abc577a_2_690x417.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7f2e20028e00ce5877ceed72bf5d6116abc577a_2_1035x625.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7f2e20028e00ce5877ceed72bf5d6116abc577a_2_1380x834.jpeg 2x" data-dominant-color="524E4D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1163 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></th>
<th><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7dbad7207bf86ebedd09fdd34c54156c32570f0.jpeg" data-download-href="/uploads/short-url/uNzjpqb75ZuAV0OurokpgNL4nL2.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7dbad7207bf86ebedd09fdd34c54156c32570f0_2_690x416.jpeg" alt="image" data-base62-sha1="uNzjpqb75ZuAV0OurokpgNL4nL2" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7dbad7207bf86ebedd09fdd34c54156c32570f0_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7dbad7207bf86ebedd09fdd34c54156c32570f0_2_1035x624.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7dbad7207bf86ebedd09fdd34c54156c32570f0_2_1380x832.jpeg 2x" data-dominant-color="565154"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1159 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></th>
</tr>
</thead>
<tbody>
<tr>
<td>Display views in separate windows - can be dragged to a second screen or additional touchscreen or drawing tablet.</td>
<td>The extra window can be displayed floating over the application window as “picture-in-picture”.</td>
<td>The additional window can be also docked into application window (any corners or sides).</td>
</tr>
</tbody>
</table>
</div><h2 id="heading--improved-volume-rendering-presets">Improved volume rendering presets</h2>
<p>Improve appearance of volume rendering preset selector and add micro-CT presets. Icons are now 2x higher resolution (so they don’t look small or blurred anymore on high-resolution screens), larger, and labeled.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b284e1fcfa880fc55e6c671b1c1b563e0d6024dc.jpeg" data-download-href="/uploads/short-url/ptfGLpFCvZYeOdxvON3wHEURpog.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b284e1fcfa880fc55e6c671b1c1b563e0d6024dc_2_345x219.jpeg" alt="image" data-base62-sha1="ptfGLpFCvZYeOdxvON3wHEURpog" width="345" height="219" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b284e1fcfa880fc55e6c671b1c1b563e0d6024dc_2_345x219.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b284e1fcfa880fc55e6c671b1c1b563e0d6024dc_2_517x328.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b284e1fcfa880fc55e6c671b1c1b563e0d6024dc_2_690x438.jpeg 2x" data-dominant-color="4E4B52"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1223 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h1 id="heading--changelog">Changelog</h1>
<ul>
<li><a href="#heading--improvements">Improvements</a></li>
<li><a href="#heading--fixes">Fixes</a></li>
<li><a href="#heading--build-system">Build-system</a></li>
<li><a href="#heading--dependencies">Dependencies</a></li>
<li><a href="#heading--documentation">Documentation</a></li>
</ul>
<h2 id="heading--improvements">Improvements</h2>
<ul>
<li>Implemented multi-monitor layout support (<a href="https://github.com/Slicer/Slicer/pull/6776">PR-6776</a>).</li>
<li>Added option for displaying the vertical slice controller (<a href="https://github.com/Slicer/Slicer/pull/6712">PR-6712</a>).</li>
<li>Improved plot title handling when no column name is specified (<a href="https://github.com/Slicer/Slicer/pull/6682">PR-6682</a>).</li>
<li>Improved volume rendering presets (<a href="https://github.com/Slicer/Slicer/pull/6762">PR-6762</a>).</li>
<li>Added support for using <code>pathlib.Path</code> object for paths in <code>slicer.util</code> (<a href="https://github.com/Slicer/Slicer/pull/6743">PR-6743</a>).</li>
<li>Updated <code>vtkMRMLParser</code> to support custom types ending with “Node” string (<a href="https://github.com/Slicer/Slicer/pull/6715">PR-6715</a>).</li>
<li>Updated <code>Slicer.crt</code> CA bundle (<a href="https://github.com/Slicer/Slicer/pull/6719">PR-6719</a>).</li>
<li>Exposed markups JSON reader/writer (<a href="https://github.com/Slicer/Slicer/pull/6756">PR-6756</a>).</li>
<li>Improved table loading and fixed errors in the table file reading/writing process (<a href="https://github.com/Slicer/Slicer/pull/6775">PR-6775</a>).</li>
<li>Improved computation of the offset direction label in slice view controller (<a href="https://github.com/Slicer/Slicer/pull/6781">PR-6781</a>).</li>
<li>Allow maximizing “Add data” and “Save data” dialog (<a href="https://github.com/Slicer/Slicer/commit/0eaffcfa2b0f330ead8943bcf49073e8f19410d3">0eaffcf</a>)</li>
<li>Make <code>qMRMLTableWidget::mrmlTableViewNode</code> accessible in Python (<a href="https://github.com/Slicer/Slicer/commit/6834c51215cd3217e01da622c4d4687255a92bea">6834c51</a>)</li>
</ul>
<h2 id="heading--fixes">Fixes</h2>
<ul>
<li>Resolved Python linting issue in the codebase (<a href="https://github.com/Slicer/Slicer/pull/6706">PR-6706</a>).</li>
<li>Fixed warnings in scripted module template observer (<a href="https://github.com/Slicer/Slicer/pull/6720">PR-6720</a>).</li>
<li>Fixed error message in <code>vtkMRMLColorTableNode</code> (<a href="https://github.com/Slicer/Slicer/pull/6729">PR-6729</a>).</li>
<li>Resolved an issue with sample data set labels not appearing on large desktop monitors (<a href="https://github.com/Slicer/Slicer/pull/6731">PR-6731</a>).</li>
<li>Fixed the blank Extensions manager in Linux package due to Chromium sandboxing (<a href="https://github.com/Slicer/Slicer/pull/6744">PR-6744</a>).</li>
<li>Fixed the reading of default markup active color (<a href="https://github.com/Slicer/Slicer/pull/6736">PR-6736</a>).</li>
<li>Fixed <code>SlicerRequestHandler</code> return value when the reader does not return any node ID (<a href="https://github.com/Slicer/Slicer/pull/6752">PR-6752</a>).</li>
<li>Resolved issues with more than one rotation slider being non-zero (<a href="https://github.com/Slicer/Slicer/pull/6759">PR-6759</a>).</li>
<li>Added missing array size hints for better Python wrapping (<a href="https://github.com/Slicer/Slicer/pull/6765">PR-6765</a>).</li>
<li>Fixed reading of vector fields from NIFTI files (<a href="https://github.com/Slicer/Slicer/pull/6791">PR-6791</a>).</li>
<li>Removed the annotations module (<a href="https://github.com/Slicer/Slicer/pull/6524">PR-6524</a>).</li>
<li>Fixed slicer.util.logProcessOutput (<a href="https://github.com/Slicer/Slicer/commit/f9dcc53b560a5f1d3f933a81c514175aed65a127">f9dcc53</a>).</li>
<li>Attempt to make Scissors effect more robust (<a href="https://github.com/Slicer/Slicer/commit/a5af8205d5ff2d0d137c9abf6d28d987fc21afee">a5af820</a> related to <a href="https://github.com/Slicer/Slicer/issues/6705">Crash on macOS when using Scissors effect #6705</a>).</li>
<li>Fixed volume sequence support in CLI modules (<a href="https://github.com/Slicer/Slicer/commit/f6a911153ceaaef8b264beb4d943a14dcfc26958">f6a9111</a>).</li>
<li>Fixed “Check for updates” checkbox in Welcome module (<a href="https://github.com/Slicer/Slicer/commit/d838e31d2f3e554db83eaeb59d46658ceb6dd9cb">d838e31</a>).</li>
<li>Fixed “Apply to all visible segments” option in Segment Editor (<a href="https://github.com/Slicer/Slicer/commit/b803ad48595c71a6e8768f920dab9f86c18be893">b803ad4</a>).</li>
<li>Fixed <code>arrayFromSegmentBinaryLabelmap</code> leaving temporary node behind (<a href="https://github.com/Slicer/Slicer/commit/5a3f3381d16c7151b695d2597695951869c9981d">5a3f338</a>).</li>
<li>Fixed subject hierarchy tree in DICOM module (<a href="https://github.com/Slicer/Slicer/commit/aa245559e6027c8bf568ff96365dff9aed5be773">aa24555</a>).</li>
<li>Added missing null-pointer checks to qMRMLSegmentEditorWidget (<a href="https://github.com/Slicer/Slicer/commit/9506e42834364ad528f5e26c0150ca25e4c44999">9506e42</a>, <a href="https://github.com/Project-MONAI/MONAILabel/issues/1300">Label Reviewer Not loading Project-MONAI/MONAILabel#1300</a>)</li>
<li>Fixed display of “An update is available.” message in Extensions Manager (<a href="https://github.com/Slicer/Slicer/commit/a943aa850467ba7b2425c236140f72f9d75ae686">a943aa8</a>)</li>
<li>Fixed various bugs related to crashes, typos, and display issues (<a href="https://github.com/Slicer/Slicer/pull/6795">PR-6795</a>, <a href="https://github.com/Slicer/Slicer/pull/6797">PR-6797</a>, <a href="https://github.com/Slicer/Slicer/pull/6798">PR-6798</a>, <a href="https://github.com/Slicer/Slicer/pull/6799">PR-6799</a>, <a href="https://github.com/Slicer/Slicer/pull/6805">PR-6805</a>, <a href="https://github.com/Slicer/Slicer/pull/6831">PR-6831</a>, <a href="https://github.com/Slicer/Slicer/pull/6824">PR-6824</a>, <a href="https://github.com/Slicer/Slicer/pull/6822">PR-6822</a>, <a href="https://github.com/Slicer/Slicer/pull/6810">PR-6810</a>, <a href="https://github.com/Slicer/Slicer/pull/6803">PR-6803</a>).</li>
</ul>
<h2 id="heading--build-system">Build-system</h2>
<ul>
<li>Improved build compatibility with OpenSSL support disabled (<a href="https://github.com/Slicer/Slicer/pull/6747">PR-6747</a>).</li>
<li>Added support for using <code>slicerFunctionAddPythonQtResources()</code> in extensions (<a href="https://github.com/Slicer/Slicer/pull/6792">PR-6792</a>).</li>
</ul>
<h2 id="heading--dependencies">Dependencies</h2>
<ul>
<li>Avoid logging errors during Python auto-completion with CTK update (<a href="https://github.com/Slicer/Slicer/commit/3ae750f4714cc38ab3c94600be1ce289e9b3c938">3ae750f</a>).</li>
<li>Update CTK to fix <code>ctk::vtkImageDataToQImage</code> function, to fix crash in <code>ctkDICOMQueryRetrieveWidget</code> and to expose <code>removeCachedTags</code> method in Python (<a href="https://github.com/Slicer/Slicer/commit/7f5f83e88120d75e6a5152b487626ffd9470921c">7f5f83e</a>, <a href="https://github.com/commontk/CTK/compare/2c89539632e503e7cf9b7c53adccd8f1f71b2ead...dec834fccffebdc3b0896c157d39e3c0031c4a0a">commontk/CTK@2c89539…dec834f</a>).</li>
</ul>
<h2 id="heading--documentation">Documentation</h2>
<ul>
<li>Fixed the ImageStacks tutorial link in the Volumes module documentation (<a href="https://github.com/Slicer/Slicer/pull/6718">PR-6718</a>).</li>
<li>Updated the documentation and removed references to Pixel Medical from commercial partners (<a href="https://github.com/Slicer/Slicer/pull/6767">PR-6767</a>).</li>
<li>Fixed various typos (<a href="https://github.com/Slicer/Slicer/commit/4f3d97c612b417cb8fe1c5688910f71d23a35852">4f3d97c</a>, <a href="https://github.com/Slicer/Slicer/commit/822a50ba2a0da3c3aca995eeae5e869abbf6ff43">822a50b</a>).</li>
</ul>

---

## Post #2 by @wenples (2023-07-25 12:18 UTC)

<p>Thanks for sending JC!</p>

---
