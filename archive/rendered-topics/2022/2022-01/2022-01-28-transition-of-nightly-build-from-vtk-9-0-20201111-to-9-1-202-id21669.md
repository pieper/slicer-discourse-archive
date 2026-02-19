---
topic_id: 21669
title: "Transition Of Nightly Build From Vtk 9 0 20201111 To 9 1 202"
date: 2022-01-28
url: https://discourse.slicer.org/t/21669
---

# Transition of nightly build from VTK 9.0.20201111 to 9.1.20220125

**Topic ID**: 21669
**Date**: 2022-01-28
**URL**: https://discourse.slicer.org/t/transition-of-nightly-build-from-vtk-9-0-20201111-to-9-1-20220125/21669

---

## Post #1 by @jcfr (2022-01-28 00:15 UTC)

<p>The pull request updating VTK is ready for review (see <a href="https://github.com/Slicer/Slicer/pull/5978">PR-5978</a>)</p>
<p>It fixes issue <a href="https://github.com/Slicer/Slicer/issues/5956">#5956</a>: <code>Update VTK9 to the latest master</code></p>
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
<td>2022.01.27</td>
<td>Experimental build for <code>PR-5978</code> have been started. See <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2022-01-27&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=groupname&amp;compare1=61&amp;value1=Experimental&amp;field2=site&amp;compare2=63&amp;value2=kitware">dashboard</a> <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></td>
</tr>
<tr>
<td>2022.01.28</td>
<td>Upload packages in Google drive folder <a href="https://drive.google.com/drive/u/0/folders/1Rt4SDZSIjqGmHEQI3wG4tpMhS63pH6l4">3D Slicer Experimental Packages</a> <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></td>
</tr>
</tbody>
</table>
</div><h3><a name="p-73135-acknowledgments-1" class="anchor" href="#p-73135-acknowledgments-1" aria-label="Heading link"></a>Acknowledgments</h3>
<p>This was made possible by the contributions and help of many <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=15" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>More specifically, I would like to acknowledge the specific help of <a class="mention" href="/u/sankhesh_jhaveri">@Sankhesh_Jhaveri</a> , <a href="https://gitlab.kitware.com/dgobbi">dgobbi</a>, <a href="https://gitlab.kitware.com/ben.boeckel">ben.boeckel</a>, <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/connor-bowley">@Connor-Bowley</a>, <a href="https://gitlab.kitware.com/will.schroeder">will.schroeder</a> who helped track down &amp; address issues, as well as <a class="mention" href="/u/jadh4v">@jadh4v</a> who helped test &amp; finalized the integration.</p>
<h3><a name="p-73135-status-of-the-transition-2" class="anchor" href="#p-73135-status-of-the-transition-2" aria-label="Heading link"></a>Status of the transition</h3>
<h4><a name="p-73135-slicer-application-3" class="anchor" href="#p-73135-slicer-application-3" aria-label="Heading link"></a>Slicer Application</h4>
<p>After the pull requests list below are integrated, Slicer application will be expected to be successfully build and package on Linux, macOS and Windows.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th>description</th>
<th>merged?</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/Slicer/Slicer/pull/6059">PR-6059</a></td>
<td><code>COMP: Update SystemTools use anticipating update from VTK 9.0 to 9.1</code></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></td>
</tr>
<tr>
<td><a href="https://github.com/Slicer/Slicer/pull/5978">PR-5978</a></td>
<td><code>ENH: Update VTK9 from 9.0.20201111 to 9.1.20220125</code></td>
<td><img src="https://emoji.discourse-cdn.com/twitter/hourglass_flowing_sand.png?v=15" title=":hourglass_flowing_sand:" class="emoji only-emoji" alt=":hourglass_flowing_sand:" loading="lazy" width="20" height="20"></td>
</tr>
</tbody>
</table>
</div><h4><a name="p-73135-help-needed-to-confirm-there-are-no-regressions-4" class="anchor" href="#p-73135-help-needed-to-confirm-there-are-no-regressions-4" aria-label="Heading link"></a>Help needed to confirm there are no regressions</h4>
<p>Check the following:</p>
<ul>
<li>Markups module</li>
<li>Volume rendering</li>
<li>Coincident topology</li>
<li>…</li>
</ul>
<p>Help create a check list ? Including reference to previous issue reports.</p>
<p>Issues to reevaluate once update is complete:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/issues/5312">Multi-volume rendering much slower using VTK9 #5312</a></li>
<li><a href="https://github.com/Slicer/Slicer/issues/4270">VTK OpenGL2 Backend: Dashed line rendering broken with OpenGL2 rendering backend #4270</a></li>
</ul>
<h4><a name="p-73135-slicer-extension-support-5" class="anchor" href="#p-73135-slicer-extension-support-5" aria-label="Heading link"></a>Slicer Extension support</h4>
<p>Remaining tasks will be the following:</p>
<ul>
<li>Support building VTK modules <code>Rendering/VR</code>, <code>Rendering/OpenVR</code> within  the <code>SlicerVirtualReality</code> extension. See <a href="https://github.com/KitwareMedical/SlicerVirtualReality/pull/89">PR KitwareMedical/SlicerVirtualReality#89</a></li>
</ul>

---

## Post #2 by @jcfr (2022-01-28 06:48 UTC)

<p>Experimental packages are available for download here: <a href="https://drive.google.com/drive/u/0/folders/1Rt4SDZSIjqGmHEQI3wG4tpMhS63pH6l4">3D Slicer Experimental Packages</a></p>
<h3><a name="p-73143-additional-failing-tests-building-against-vtk-9120220125-1" class="anchor" href="#p-73143-additional-failing-tests-building-against-vtk-9120220125-1" aria-label="Heading link"></a>Additional failing tests building against VTK 9.1.20220125</h3>
<div class="md-table">
<table>
<thead>
<tr>
<th>computron (macOS)</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://slicer.cdash.org/test/21153377">vtkMRMLThreeDReformatDisplayableManagerTest1</a> (segfault)</td>
</tr>
</tbody>
</table>
</div><div class="md-table">
<table>
<thead>
<tr>
<th>metroplex (Linux)</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://slicer.cdash.org/test/21154137">vtkMRMLThreeDReformatDisplayableManagerTest1</a> (segfault)</td>
</tr>
</tbody>
</table>
</div><div class="md-table">
<table>
<thead>
<tr>
<th>overload (Windows)</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://slicer.cdash.org/test/21156757">vtkMRMLThreeDReformatDisplayableManagerTest1</a> (invalid output)</td>
</tr>
<tr>
<td><a href="https://slicer.cdash.org/test/21156764">py_nomainwindow_SlicerOptionDisableSettingsTest</a> (AssertionError)</td>
</tr>
</tbody>
</table>
</div><h3><a name="p-73143-output-of-vtkmrmlthreedreformatdisplayablemanagertest1-2" class="anchor" href="#p-73143-output-of-vtkmrmlthreedreformatdisplayablemanagertest1-2" aria-label="Heading link"></a>Output of <code>vtkMRMLThreeDReformatDisplayableManagerTest1</code></h3>
<h4><a name="p-73143-overload-windows-3" class="anchor" href="#p-73143-overload-windows-3" aria-label="Heading link"></a>overload (windows)</h4>
<div class="md-table">
<table>
<thead>
<tr>
<th>Valid image</th>
<th>Test image</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae2d3d8eca75059c941adad63cbe2363c9dc3d7e.png" data-download-href="/uploads/short-url/oQQ0rhmJ5H4dQkkHdrcjRZgQuTQ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae2d3d8eca75059c941adad63cbe2363c9dc3d7e_2_501x500.png" alt="image" data-base62-sha1="oQQ0rhmJ5H4dQkkHdrcjRZgQuTQ" width="501" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae2d3d8eca75059c941adad63cbe2363c9dc3d7e_2_501x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae2d3d8eca75059c941adad63cbe2363c9dc3d7e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae2d3d8eca75059c941adad63cbe2363c9dc3d7e.png 2x" data-dominant-color="080706"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">600×598 35.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
<td></td>
</tr>
</tbody>
</table>
</div><p><em>Source: <a href="https://slicer.cdash.org/test/21156757">https://slicer.cdash.org/test/21156757</a></em></p>

---

## Post #3 by @jcfr (2022-02-04 21:43 UTC)

<p>The regression has been fixed in Slicer/VTK in <a href="https://github.com/Slicer/VTK/commit/e0d1851e22db9ae1d39096464964e7f1fe333436">e0d1851e2</a> and a merge request in being review in upstream VTK at <a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/8885" class="inline-onebox">BUG: Rename vtkInteractionCallback class to avoid symbol clash (!8885) · Merge requests · VTK / VTK · GitLab</a></p>
<h3><a name="p-73564-impact-of-the-regression-on-slicer-application-1" class="anchor" href="#p-73564-impact-of-the-regression-on-slicer-application-1" aria-label="Heading link"></a>Impact of the regression on Slicer application</h3>
<p>Enabling the “Lock Normal to Camera” associated with the reformat widget was leading to a crash.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12881f3692079c245de3eff6c02ff6d2cd362719.png" data-download-href="/uploads/short-url/2DWewQgEXNQwrxq659j0xsNZfNn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12881f3692079c245de3eff6c02ff6d2cd362719.png" alt="image" data-base62-sha1="2DWewQgEXNQwrxq659j0xsNZfNn" width="473" height="192"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">473×192 30 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-73564-details-2" class="anchor" href="#p-73564-details-2" aria-label="Heading link"></a>Details</h3>
<p>After hunting down the regression (performing a manual bisection of the history), I discovered that the following commits introduced the regression:</p>
<p><a href="https://github.com/Kitware/VTK/commit/7451dd2d1">kitware/vtk@7451dd2d1</a>: <code>vtkDisplaySizedImplicitPlaneWidget/Representation: Implementation </code></p>
<p><a href="https://github.com/Kitware/VTK/commit/cd42f785d">kitware/vtk@cd42f785d</a>: <code>vtkCoordinateFrameWidget: Implementation</code></p>
<p>At first, it didn’t make sense because we <strong>do not instantiate these new widgets in Slicer</strong>.</p>
<p>Looking at the issue more closely, I realized that the commit referenced above introduced the class <code>vtkDisplaySizedImplicitPlaneWidget</code> based of <code>vtkImplicitPlaneWidget2</code> that we effectively used in Slicer (see <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Libs/MRML/DisplayableManager/vtkMRMLThreeDReformatDisplayableManager.cxx#L240">here</a>).</p>
<p>It turns out that these classes all defined the class <code>vtkInteractionCallback</code> in their private implementation along with:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th><code>vtkImplicitPlaneWidget2</code></th>
<th><code>vtkDisplaySizedImplicitPlaneWidget</code></th>
<th><code>vtkCoordinateFrameWidget</code></th>
</tr>
</thead>
<tbody>
<tr>
<td>static constructor</td>
<td><a href="https://github.com/Kitware/VTK/blob/67eaef6433e15644fd1b51d814b535dc66816464/Interaction/Widgets/vtkImplicitPlaneWidget2.cxx#L37-L51">link</a></td>
<td><a href="https://github.com/Kitware/VTK/blob/67eaef6433e15644fd1b51d814b535dc66816464/Interaction/Widgets/vtkDisplaySizedImplicitPlaneWidget.cxx#L38-L52">link</a></td>
<td><a href="https://github.com/Kitware/VTK/blob/67eaef6433e15644fd1b51d814b535dc66816464/Interaction/Widgets/vtkCoordinateFrameWidget.cxx#L35-L49">link</a></td>
</tr>
<tr>
<td><code>friend</code> statement in header</td>
<td><a href="https://github.com/Kitware/VTK/blob/67eaef6433e15644fd1b51d814b535dc66816464/Interaction/Widgets/vtkImplicitPlaneWidget2.h#L104">link</a></td>
<td><a href="https://github.com/Kitware/VTK/blob/67eaef6433e15644fd1b51d814b535dc66816464/Interaction/Widgets/vtkDisplaySizedImplicitPlaneWidget.h#L108">link</a></td>
<td><a href="https://github.com/Kitware/VTK/blob/67eaef6433e15644fd1b51d814b535dc66816464/Interaction/Widgets/vtkCoordinateFrameWidget.h#L101">link</a></td>
</tr>
</tbody>
</table>
</div><p>Since these classes were compiled within the same “program” (in that case the shared library <code>libvtkInteraction-9.1.(dll|dylib|so)</code>), the ODR (<a href="https://en.cppreference.com/w/cpp/language/definition">One Definition Rule</a>) was violated and it now explains the following backtrace:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2c094af32f907446906a694aa6ea100452aa463.png" data-download-href="/uploads/short-url/rMRemKsXUBteH5mmyAg7Ru4yGHx.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2c094af32f907446906a694aa6ea100452aa463.png" alt="image" data-base62-sha1="rMRemKsXUBteH5mmyAg7Ru4yGHx" width="690" height="269" data-dominant-color="D1D1D1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1557×609 35.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><em>Backtrace obtained runing <code>ctest -R vtkMRMLThreeDReformatDisplayableManagerTest1 -V</code> and analyzing the core dump following the Slicer guide <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/linuxcpp.html#analyze-a-segmentation-fault">C++ debugging on GNU/Linux systems: Analyze a segmentation fault</a>.</em></p>
<h4><a name="p-73564-symbol-analysis-3" class="anchor" href="#p-73564-symbol-analysis-3" aria-label="Heading link"></a>Symbol analysis</h4>
<p>The following invocation of <code>nm</code> allows to confirm there the patch effectively ensure there are different instances of callback classes instead of a single <code>vtkInteractionCallback</code>:</p>
<p>Before integrating our fix:</p>
<pre data-code-wrap="bash"><code class="lang-bash">$ nm lib/libvtkInteraction-9.1.so  | c++filt | ack "typeinfo for vtk.+Callback$"
0000000000501f70 d typeinfo for vtkCWCallback
000000000050b938 d typeinfo for vtkPWCallback
000000000050b950 d typeinfo for vtkPW1Callback
000000000050b968 d typeinfo for vtkPW2Callback
00000000004fae80 d typeinfo for vtkAngleWidgetCallback
00000000004f7a28 d typeinfo for vtkImageViewerCallback
0000000000503d88 d typeinfo for vtkInteractionCallback
00000000004f7c10 d typeinfo for vtkImageViewer2Callback
0000000000500f70 d typeinfo for vtkCaptionAnchorCallback
0000000000505d58 d typeinfo for vtkDistanceWidgetCallback
00000000004fca38 d typeinfo for vtkBiDimensionalWidgetCallback
00000000004f7f28 d typeinfo for vtkResliceImageViewerScrollCallback
</code></pre>
<p>After integrating our fix:</p>
<pre data-code-wrap="bash"><code class="lang-bash">$ nm lib/libvtkInteraction-9.1.so  | c++filt | ack "typeinfo for vtk.+Callback$"
0000000000501df0 d typeinfo for vtkCWCallback
000000000050b948 d typeinfo for vtkPWCallback
000000000050b960 d typeinfo for vtkPW1Callback
000000000050b978 d typeinfo for vtkPW2Callback
00000000004fad00 d typeinfo for vtkAngleWidgetCallback
00000000004f78a8 d typeinfo for vtkImageViewerCallback
00000000004f7a90 d typeinfo for vtkImageViewer2Callback
0000000000500df0 d typeinfo for vtkCaptionAnchorCallback
0000000000505ca0 d typeinfo for vtkDistanceWidgetCallback
00000000004fc8b8 d typeinfo for vtkBiDimensionalWidgetCallback
00000000004f7da8 d typeinfo for vtkResliceImageViewerScrollCallback
000000000050aa80 d typeinfo for vtkImplicitPlaneWidget2InteractionCallback
0000000000503c08 d typeinfo for vtkCoordinateFrameWidgetInteractionCallback
0000000000504518 d typeinfo for vtkDisplaySizedImplicitPlaneInteractionCallback
</code></pre>
<h4><a name="p-73564-running-test-interactively-disabling-event-replay-4" class="anchor" href="#p-73564-running-test-interactively-disabling-event-replay-4" aria-label="Heading link"></a>Running test interactively disabling event replay</h4>
<p>For future reference, it has also been useful to run the test interactively by disabling the replay of event,  this was done by appending <code>-I --DisableReplay</code> to the command reported running the test with <code>-V</code>:</p>
<pre data-code-wrap="bash"><code class="lang-bash">SLICER_SOURCE_DIR=/home/jcfr/Projects/Slicer
SLICER_BUILD_DIR=/home/jcfr/Projects/Slicer-rwdi

${SLICER_BUILD_DIR}/Slicer-build/Slicer --launch \
  ${SLICER_BUILD_DIR}/Slicer-build/bin/MRMLDisplayableManagerCxxTests \
  vtkMRMLThreeDReformatDisplayableManagerTest1\
    -D ${SLICER_SOURCE_DIR}/Libs/MRML/DisplayableManager/Testing/Cxx/../ \
    -T ${SLICER_BUILD_DIR}/Slicer-build/Testing/Temporary \
    -V Baseline/vtkMRMLThreeDReformatDisplayableManagerTest1.png \
    -I --DisableReplay
</code></pre>
<h4><a name="p-73564-further-analysis-of-the-vtk-toolkit-5" class="anchor" href="#p-73564-further-analysis-of-the-vtk-toolkit-5" aria-label="Heading link"></a>Further analysis of the VTK toolkit</h4>
<p>Running the following commands allowed to discover other duplication and these ones will be discussed with the team as well:</p>
<ul>
<li><a href="https://gitlab.kitware.com/vtk/vtk/-/issues/18456">#18456</a> (Remove duplicated class vtkTextureArray)</li>
<li><a href="https://gitlab.kitware.com/vtk/vtk/-/issues/18455">#18455</a> (Remove duplicated class vtkmOutputFilterPolicy)</li>
<li><a href="https://gitlab.kitware.com/vtk/vtk/-/issues/18457">#18457</a> (Improve continuous integration to detect duplicated symbols)</li>
</ul>
<pre data-code-wrap="bash"><code class="lang-bash">$ cd VTK
$ ack -h --ignore-dir=Testing "^class.+vtk.+ \: " | ack "\:" | sort  &gt; /tmp/vtk-classes.txt
$ ack -h --ignore-dir=Testing "^class.+vtk.+ \: " | ack "\:" | sort | uniq &gt; /tmp/vtk-uniq-classes.txt
$ diff /tmp/vtk-classes.txt /tmp/vtk-uniq-classes.txt
</code></pre>
<pre data-code-wrap="diff"><code class="lang-diff">diff /tmp/vtk-classes.txt /tmp/vtk-uniq-classes.txt
1481,1482d1480
&lt; class vtkInteractionCallback : public vtkCommand
&lt; class vtkInteractionCallback : public vtkCommand
2047d2044
&lt; class vtkmOutputFilterPolicy : public vtkm::filter::PolicyBase&lt;vtkmOutputFilterPolicy&gt;
2607d2603
&lt; class vtkTextureArray : public std::map&lt;int, vtkSmartPointer&lt;vtkImageData&gt;&gt;
</code></pre>
<p>Occurrences of <code>vtkmOutputFilterPolicy</code>:</p>
<ul>
<li><a href="https://github.com/Kitware/VTK/blob/164226edbe09ac420e1367c2c54c8e85a34a5939/Accelerators/Vtkm/Core/vtkmFilterPolicy.h">Accelerators/Vtkm/DataModel/vtkmFilterPolicy.h</a></li>
<li><a href="https://github.com/Kitware/VTK/blob/67eaef6433e15644fd1b51d814b535dc66816464/Accelerators/Vtkm/DataModel/vtkmFilterPolicy.h">Accelerators/Vtkm/DataModel/vtkmFilterPolicy.h</a></li>
</ul>
<p>Occurrences of <code>vtkTextureArray</code>:</p>
<ul>
<li><a href="https://github.com/Kitware/VTK/blob/67eaef6433e15644fd1b51d814b535dc66816464/Interaction/Widgets/vtkTexturedButtonRepresentation2D.cxx#L36-L39">Interaction/Widgets/vtkTexturedButtonRepresentation2D.cxx</a></li>
<li><a href="https://github.com/Kitware/VTK/blob/67eaef6433e15644fd1b51d814b535dc66816464/Interaction/Widgets/vtkTexturedButtonRepresentation.cxx#L43-L46">Interaction/Widgets/vtkTexturedButtonRepresentation.cxx</a></li>
</ul>

---

## Post #4 by @pieper (2022-02-04 21:59 UTC)

<p>Impressive work Jc!  Glad you were able to track this down <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:"></p>

---
