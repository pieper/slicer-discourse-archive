# Adding Slicer to official VTK Continuous Integration aka "Contract Testing"

**Topic ID**: 15848
**Date**: 2021-02-04
**URL**: https://discourse.slicer.org/t/adding-slicer-to-official-vtk-continuous-integration-aka-contract-testing/15848

---

## Post #1 by @jcfr (2021-02-04 21:26 UTC)

<p>To more effectively identify and address issues associated with the latest version of VTK that may impact  Slicer, we are working with the VTK team to setup what we call “contract testing”.</p>
<p>In a nutshell, Slicer will be built automatically by the VTK CI infrastructure:</p>
<ul>
<li>on a nightly basis</li>
<li>on “demand” for merge request</li>
</ul>
<p>For more details, see <a href="https://gitlab.kitware.com/vtk/vtk/-/issues/18113" class="inline-onebox">CI jobs for contract testing (#18113) · Issues · VTK / VTK · GitLab</a></p>
<h3>Which Slicer build option to build on VTK CI ?</h3>
<p>We suggest the following:</p>
<pre><code class="lang-auto">Slicer_BUILD_CLI:BOOL=OFF
Slicer_USE_QtTesting:BOOL=OFF
Slicer_USE_SimpleITK:BOOL=OFF
Slicer_BUILD_PARAMETERSERIALIZER_SUPPORT:BOOL=OFF
</code></pre>
<h3>Which tests to run on VTK CI ?</h3>
<p>While running all tests would be ideal, we would like to instead maximize the use of available resources by identifying existing tests and also implementing new ones.</p>
<p>Here is an initial list of functionality to focus one (based on prior regressions):</p>
<ul>
<li>Fiducial selection</li>
<li>Occlusion and transparency</li>
<li>Volume rendering, multi-volume rendering, depth peeling</li>
<li>Smoothing of segmentation in 3D view</li>
<li>Building of Slicer Extension like SlicerLookingGlass and SlicerVirtualReality</li>
</ul>
<p>We also discussed building VTK and Slicer against Qt6 and that will happen later.</p>
<h3>If you would like to help, here are some ideas:</h3>
<ol>
<li>
<p>Update Slicer to build against latest VTK:</p>
<ul>
<li>
<p>While working on Slicer <a href="https://github.com/Slicer/Slicer/pull/5381">PR-5381</a> that updates VTK 9 in Slicer from <code>9.0.20201111</code> to <code>9.0.20210108</code> and sqlite from <code>3.30</code> to <code>3.33</code>, we identified issues related to building CPython.</p>
</li>
<li>
<p>Prior moving forward with VTK 9 update, we would first need help to update <a href="https://github.com/python-cmake-buildsystem/python-cmake-buildsystem">python-cmake-buildsystem</a> to support building python &gt;= 3.7. See Slicer issue <a href="https://github.com/Slicer/Slicer/issues/5014">#5014</a></p>
</li>
</ul>
</li>
<li>
<p>The Slicer/VTK fork associated with VT9 currently has 3 patches, at least 2 of them would need to be addressed so that we can use an install tree of VTK:</p>
<ul>
<li>
<p><code> BUG: Update vtkPythonUtil to disable relative import causing crash for Slicer modules</code>. See <a href="https://github.com/Slicer/VTK/commit/065a176e2130c705295a9bead81576d38547d67e">Slicer/VTK@065a176e2</a></p>
<ul>
<li>There is no corresponding issue in VTK tracker yet, we would need to first better understand the problem. For additional context, see also <a href="https://discourse.vtk.org/t/issue-with-using-vtkpythonutil-getobjectfrompointer-for-custom-vtk-classes/4100" class="inline-onebox">Issue with using vtkPythonUtil::GetObjectFromPointer for custom VTK classes - Development - VTK</a>
</li>
</ul>
</li>
<li>
<p><code>Remove FindTBB and expect VTK to be configured with TBB_DIR</code>. See <a href="https://github.com/Slicer/VTK/commit/38048ca4a264f89a97418b35d7fc99cbb25ff19a">Slicer/VTK@38048ca4a</a>.</p>
<ul>
<li>If you would like to help, this is tracked by issue <a href="https://gitlab.kitware.com/vtk/vtk/-/issues/18112">vtk#18112</a>.</li>
</ul>
</li>
</ul>
</li>
<li>
<p>Help to (a) identify relevant Slicer tests and (b) implement new ones</p>
</li>
<li>
<p>The VTK CI will build Slicer by passing the option <code>VTK_DIR</code> pointing to an install tree of VTK9, we  need help testing.</p>
</li>
</ol>

---

## Post #2 by @lassoan (2021-02-05 03:39 UTC)

<p>This sounds like a lot of work, but nevertheless useful. QtTesting can drive the GUI and set up rendering tests, which could be useful for catching errors in rendering output, so we could try to enable it.</p>

---
