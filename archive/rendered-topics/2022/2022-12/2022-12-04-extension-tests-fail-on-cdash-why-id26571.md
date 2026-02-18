# Extension tests fail on CDash, why?

**Topic ID**: 26571
**Date**: 2022-12-04
**URL**: https://discourse.slicer.org/t/extension-tests-fail-on-cdash-why/26571

---

## Post #1 by @mau_igna_06 (2022-12-04 21:40 UTC)

<blockquote>
<p>For community interest <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/issues/65" rel="noopener nofollow ugc">this issue is duplicated from BoneReconstructionPlanner Github</a></p>
</blockquote>
<p>BRP is working correctly and the tests are succeded on my laptop.</p>
<p>Do you have some instruction on how to solve <a href="https://slicer.cdash.org/test/23550441" rel="noopener nofollow ugc">these tests failure</a> ?</p>

---

## Post #2 by @mau_igna_06 (2022-12-04 21:41 UTC)

<blockquote>
<p>Do you have some instruction on how to solve <a href="https://slicer.cdash.org/test/23550441" rel="noopener nofollow ugc">these test failure</a> ?</p>
</blockquote>
<p>According to <a href="https://slicer.cdash.org/test/23547875" rel="noopener nofollow ugc">this test results</a> of <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Plots/Testing/Python/PlotsSelfTest.py" rel="noopener nofollow ugc">the Plots module</a>:<br>
<code>RunTest</code> and all <code>test_*</code> matching functions are run in parallel on test-machine</p>
<p>It appears I should then use only <code>RunTest</code> function and use <code>section_</code> keyword</p>

---

## Post #3 by @mau_igna_06 (2022-12-05 15:07 UTC)

<p>CDash is still failing for BoneReconstructionPlanner… Core-devs do you know how to fix this?</p>

---

## Post #4 by @jamesobutler (2022-12-05 17:31 UTC)

<p>I see the following test failures on the Windows platform for BoneReconstructionPlanner (<a href="https://slicer.cdash.org/test/23557325" class="inline-onebox" rel="noopener nofollow ugc">SlicerPreview : Test Details</a>). Are you referring to these test failures?</p>
<pre><code class="lang-auto">======================================================================
FAIL: runTest (BoneReconstructionPlanner.BoneReconstructionPlannerTest)
Run as few or as many tests as needed here.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:/D/P/S-0-E-b/BoneReconstructionPlanner-build/lib/Slicer-5.3/qt-scripted-modules/BoneReconstructionPlanner.py", line 3466, in runTest
    self.section_LoadFinishedPlanSampleData()
  File "D:/D/P/S-0-E-b/BoneReconstructionPlanner-build/lib/Slicer-5.3/qt-scripted-modules/BoneReconstructionPlanner.py", line 3528, in section_LoadFinishedPlanSampleData
    self.assertEqual(
AssertionError: 6 != 2

----------------------------------------------------------------------
Ran 2 tests in 87.301s

FAILED (failures=1)
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "D:\D\P\S-0-build\Slicer-build\bin\Python\slicer\testing.py", line 26, in runUnitTest
    exitFailure()
  File "D:\D\P\S-0-build\Slicer-build\bin\Python\slicer\testing.py", line 10, in exitFailure
    raise Exception(message)
Exception
Switch to module:  ""
Warning: In D:\D\P\S-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx, line 3009
vtkMRMLSubjectHierarchyNode (0000026324DF87A0): GetItemByName: Multiple subject hierarchy item found with name 'Mandibular planes. Returning first


double __cdecl qSlicerSubjectHierarchyMarkupsPlugin::canOwnSubjectHierarchyItem(__int64) const : could not get the Markups module logic.
void __cdecl qMRMLSubjectHierarchyModel::updateItemDataFromSubjectHierarchyItem(class QStandardItem *,__int64,int) : Terminologies module is not found
double __cdecl qSlicerSubjectHierarchyMarkupsPlugin::canOwnSubjectHierarchyItem(__int64) const : could not get the Markups module logic.
void __cdecl qMRMLSubjectHierarchyModel::updateItemDataFromSubjectHierarchyItem(class QStandardItem *,__int64,int) : Terminologies module is not found
Traceback (most recent call last):
  File "D:/D/P/S-0-E-b/BoneReconstructionPlanner-build/lib/Slicer-5.3/qt-scripted-modules/BoneReconstructionPlanner.py", line 356, in exit
    mandibularPlanesList[i].RemoveObserver(self.logic.mandiblePlaneObserversAndNodeIDList[i][0])
IndexError: list index out of range
</code></pre>

---

## Post #5 by @mau_igna_06 (2022-12-05 18:09 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="26571">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Are you referring to these test failures?</p>
</blockquote>
</aside>
<p>Yes. Thank you, I forgot to put the link to the failing-test…</p>
<p>Here is the relevant code:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/830a793367b28f156b9a27947be5bcd6bf3b13dc/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3459-L3476">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/830a793367b28f156b9a27947be5bcd6bf3b13dc/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3459-L3476" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/830a793367b28f156b9a27947be5bcd6bf3b13dc/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3459-L3476" target="_blank" rel="noopener nofollow ugc">SlicerIGT/SlicerBoneReconstructionPlanner/blob/830a793367b28f156b9a27947be5bcd6bf3b13dc/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3459-L3476</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="3459" style="counter-reset: li-counter 3458 ;">
          <li>def runTest(self):
</li>
          <li>  """Run as few or as many tests as needed here.
</li>
          <li>  """
</li>
          <li>  self.setUp()
</li>
          <li>  self.section_EnterBRP()
</li>
          <li>  self.section_GetWidget()
</li>
          <li>  self.section_GetLogic()
</li>
          <li>  self.section_LoadFinishedPlanSampleData()
</li>
          <li>
</li>
          <li>  self.setUp()
</li>
          <li>  self.section_EnterBRP()
</li>
          <li>  self.section_GetWidget()
</li>
          <li>  self.section_GetLogic()
</li>
          <li>  self.section_LoadSampleData()
</li>
          <li>  self.section_MakeModels()
</li>
          <li>  self.section_AddMandibularCurve()
</li>
          <li>  self.section_AddMandiblePlanes()
</li>
          <li>  self.section_AddFibulaLineAndCenterIt()
</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I would like <code>runTest</code> to be executed only once and not in parallel but sequentially</p>

---

## Post #6 by @mau_igna_06 (2022-12-06 22:47 UTC)

<p>This is my research on the topic</p>
<p>Next is the command line to execute BRP tests on Slicer:</p>
<p><code>/work/Preview/Slicer-0-build/Slicer-build/Slicer "--no-splash" "--testing" "--launcher-additional-settings" "/work/Preview/S-0-E-b/BoneReconstructionPlanner-build/AdditionalLauncherSettings.ini" "--additional-module-paths" "/work/Preview/S-0-E-b/BoneReconstructionPlanner-build/lib/Slicer-5.3/qt-scripted-modules" "/work/Preview/S-0-E-b/BoneReconstructionPlanner-build/lib/Slicer-5.3/cli-modules" "/work/Preview/S-0-E-b/BoneReconstructionPlanner-build/lib/Slicer-5.3/qt-loadable-modules" "--python-code" "import slicer.testing; slicer.testing.runUnitTest(['/work/Preview/S-0-E-b/BoneReconstructionPlanner-build/BoneReconstructionPlanner', '/work/Preview/S-0-E-b/BoneReconstructionPlanner/BoneReconstructionPlanner'], 'BoneReconstructionPlanner')"</code></p>
<p>Which comes from this cmake file:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/CMake/SlicerMacroPythonTesting.cmake#L50-L71">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/CMake/SlicerMacroPythonTesting.cmake#L50-L71" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/CMake/SlicerMacroPythonTesting.cmake#L50-L71" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/CMake/SlicerMacroPythonTesting.cmake#L50-L71</a></h4>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="50" style="counter-reset: li-counter 49 ;">
          <li>macro(slicer_add_python_unittest)</li>
          <li>  set(options)</li>
          <li>  set(oneValueArgs TESTNAME_PREFIX SCRIPT)</li>
          <li>  set(multiValueArgs SLICER_ARGS)</li>
          <li>  cmake_parse_arguments(MY "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN})</li>
          <li>  get_filename_component(test_name ${MY_SCRIPT} NAME_WE)</li>
          <li>  get_filename_component(_script_source_dir ${MY_SCRIPT} PATH)</li>
          <li>  if("${_script_source_dir}" STREQUAL "")</li>
          <li>    set(_script_source_dir ${CMAKE_CURRENT_SOURCE_DIR})</li>
          <li>  endif()</li>
          <li>  ExternalData_add_test(${Slicer_ExternalData_DATA_MANAGEMENT_TARGET}</li>
          <li>    NAME py_${MY_TESTNAME_PREFIX}${test_name}</li>
          <li>    COMMAND ${Slicer_LAUNCHER_EXECUTABLE}</li>
          <li>    --no-splash</li>
          <li>    --testing</li>
          <li>    ${Slicer_ADDITIONAL_LAUNCHER_SETTINGS}</li>
          <li>    ${MY_SLICER_ARGS}</li>
          <li>    ${UNITTEST_LIB_PATHS}</li>
          <li>    --python-code "import slicer.testing\\; slicer.testing.runUnitTest(['${CMAKE_CURRENT_BINARY_DIR}', '${_script_source_dir}'], '${test_name}')"</li>
          <li>    )</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/CMake/SlicerMacroPythonTesting.cmake#L50-L71" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Here is the <code>runUnitTest</code> definition:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Base/Python/slicer/testing.py#L13-L26">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Base/Python/slicer/testing.py#L13-L26" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Base/Python/slicer/testing.py#L13-L26" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Base/Python/slicer/testing.py#L13-L26</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="13" style="counter-reset: li-counter 12 ;">
          <li>def runUnitTest(path, testname):</li>
          <li>    import sys</li>
          <li>    import unittest</li>
          <li>    if isinstance(path, str):</li>
          <li>        sys.path.append(path)</li>
          <li>    else:</li>
          <li>        sys.path.extend(path)</li>
          <li>    print("-------------------------------------------")</li>
          <li>    print(f"path: {path}\ntestname: {testname}")</li>
          <li>    print("-------------------------------------------")</li>
          <li>    suite = unittest.TestLoader().loadTestsFromName(testname)</li>
          <li>    result = unittest.TextTestRunner(verbosity=2).run(suite)</li>
          <li>    if not result.wasSuccessful():</li>
          <li>        exitFailure()</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If I run it on Slicer I get:</p>
<pre><code class="lang-auto">import unittest
suite = unittest.TestLoader().loadTestsFromName('BoneReconstructionPlanner')
print(suite)
</code></pre>
<blockquote>
<p>&lt;unittest.suite.TestSuite tests=[&lt;unittest.suite.TestSuite tests=[&lt;BoneReconstructionPlanner.BoneReconstructionPlannerTest testMethod=runTest&gt;]&gt;, &lt;unittest.suite.TestSuite tests=[&lt;slicer.ScriptedLoadableModule.ScriptedLoadableModuleTest testMethod=runTest&gt;]&gt;]&gt;</p>
</blockquote>
<p>There are two tests listed above, so that explains the logs from <a href="https://slicer.cdash.org/test/23564598" rel="noopener nofollow ugc">CDash</a>:</p>
<blockquote>
<p>runTest (BoneReconstructionPlanner.BoneReconstructionPlannerTest)<br>
…<br>
<a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/830a793367b28f156b9a27947be5bcd6bf3b13dc/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3459-L3461" rel="noopener nofollow ugc">Run as few or as many tests as needed here.</a> … FAIL<br>
runTest (slicer.ScriptedLoadableModule.ScriptedLoadableModuleTest)<br>
<a href="https://github.com/Slicer/Slicer/blob/8a1c2e03931ab06ca44c7a61fc3f15766c2b4ac1/Base/Python/slicer/ScriptedLoadableModule.py#L410-L413" rel="noopener nofollow ugc">Run a default selection of tests here.</a> … ok</p>
</blockquote>
<p>The code sources are linked in the above quote.</p>
<p>This code piece also looks relevant:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/8a1c2e03931ab06ca44c7a61fc3f15766c2b4ac1/Base/Python/slicer/ScriptedLoadableModule.py#L43-L50">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/8a1c2e03931ab06ca44c7a61fc3f15766c2b4ac1/Base/Python/slicer/ScriptedLoadableModule.py#L43-L50" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/8a1c2e03931ab06ca44c7a61fc3f15766c2b4ac1/Base/Python/slicer/ScriptedLoadableModule.py#L43-L50" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/8a1c2e03931ab06ca44c7a61fc3f15766c2b4ac1/Base/Python/slicer/ScriptedLoadableModule.py#L43-L50</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="43" style="counter-reset: li-counter 42 ;">
          <li># Add this test to the SelfTest module's list for discovery when the module</li>
          <li># is created.  Since this module may be discovered before SelfTests itself,</li>
          <li># create the list if it doesn't already exist.</li>
          <li>try:</li>
          <li>    slicer.selfTests</li>
          <li>except AttributeError:</li>
          <li>    slicer.selfTests = {}</li>
          <li>slicer.selfTests[self.moduleName] = self.runTest</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The main question I have right now is why my test data is loaded 3 times instead of 1 (as I intended on the <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/830a793367b28f156b9a27947be5bcd6bf3b13dc/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3459-L3476" rel="noopener nofollow ugc">test here</a> and <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/830a793367b28f156b9a27947be5bcd6bf3b13dc/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3509" rel="noopener nofollow ugc">this line</a>)</p>
<p>First load:</p>
<blockquote>
<p>Loaded volume from file: /home/kitware/.cache/NA-MIC/Slicer-tmp/Slicer-tmpIO/__BundleLoadTemp-2022-12-06_092933_484/TestPlanBRP/Data/Fibula.nrrd. Dimensions: 512x512x1213. Number of components: 1. Pixel type: int.</p>
</blockquote>
<blockquote>
<p>Loaded volume from file: /home/kitware/.cache/NA-MIC/Slicer-tmp/Slicer-tmpIO/__BundleLoadTemp-2022-12-06_092933_484/TestPlanBRP/Data/Skull.nrrd. Dimensions: 512x512x207. Number of components: 1. Pixel type: int.</p>
</blockquote>
<p>Second load:</p>
<blockquote>
<p>Loaded volume from file: /home/kitware/.cache/NA-MIC/Slicer-tmp/Slicer-tmpIO/__BundleLoadTemp-2022-12-06_092959_291/TestPlanBRP/Data/Fibula.nrrd. Dimensions: 512x512x1213. Number of components: 1. Pixel type: int.</p>
</blockquote>
<blockquote>
<p>Loaded volume from file: /home/kitware/.cache/NA-MIC/Slicer-tmp/Slicer-tmpIO/__BundleLoadTemp-2022-12-06_092959_291/TestPlanBRP/Data/Skull.nrrd. Dimensions: 512x512x207. Number of components: 1. Pixel type: int.</p>
</blockquote>
<p>Third load:</p>
<blockquote>
<p>Loaded volume from file: /home/kitware/.cache/NA-MIC/Slicer-tmp/Slicer-tmpIO/__BundleLoadTemp-2022-12-06_093041_333/TestPlanBRP/Data/Fibula.nrrd. Dimensions: 512x512x1213. Number of components: 1. Pixel type: int.</p>
</blockquote>
<blockquote>
<p>Loaded volume from file: /home/kitware/.cache/NA-MIC/Slicer-tmp/Slicer-tmpIO/__BundleLoadTemp-2022-12-06_093041_333/TestPlanBRP/Data/Skull.nrrd. Dimensions: 512x512x207. Number of components: 1. Pixel type: int.</p>
</blockquote>

---

## Post #7 by @mau_igna_06 (2022-12-09 15:33 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>
<p>It would be really nice if you could help me solve this test-break</p>

---

## Post #8 by @lassoan (2022-12-11 15:38 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="6" data-topic="26571">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>The main question I have right now is why my test data is loaded 3 times instead of 1</p>
</blockquote>
</aside>
<p>You can print the stack trace in the loading method to see what is executing the method:</p>
<pre data-code-wrap="python"><code class="lang-python">import traceback
traceback.print_stack()
</code></pre>
<p>In this case, loading of the scene is attempted 3 times because an error occurred during loading. SampleData module tries to download and load a data set 3 times before giving up. So, you need to check what causes the scene loading to return with failure and if you fix it then the scene will only be loaded once and probably all the other errors will go away.</p>
<p>If it is too difficult to find/fix the root cause of the scene loading error then you can use a lower-level SampleData API, where you can set number of attempts to 1:</p>
<pre data-code-wrap="python"><code class="lang-python">def downloadFromSource(self, source, maximumAttemptsCount=3): 
</code></pre>

---

## Post #9 by @mau_igna_06 (2022-12-11 16:55 UTC)

<p>Thanks for the answer Andras</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="26571">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">import traceback
traceback.print_stack()
</code></pre>
</blockquote>
</aside>
<p>So I guess I’ll add that code to the test after <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/8e2ead652c84fb8eb79fa4c270b94a738e400957/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3507" rel="noopener nofollow ugc">this line</a> so it gets executed by the Kitware-build-machine as the test doesn’t fail on my laptop</p>

---

## Post #10 by @lassoan (2022-12-11 17:00 UTC)

<p>It fails the same on my computer, too. I’ve simply downloaded the ExtensionsIndex repository, kept only those s4ext files that are relevant for BRP extension, and then <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-list-of-extensions-manually">built the extensions</a>. It reproduced the same error as you can see on the dashboard. Probably some extension is not fully loaded and that causes the scene load with errors.</p>
<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> had some issues with testing extensions that depend on other extensions - he might have some tips for you.</p>

---

## Post #11 by @mau_igna_06 (2022-12-11 18:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="26571">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It fails the same on my computer, too. I’ve simply downloaded the ExtensionsIndex repository, kept only those s4ext files that are relevant for BRP extension, and then <a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-list-of-extensions-manually" rel="noopener nofollow ugc">built the extensions </a>. It reproduced the same error as you can see on the dashboard. Probably some extension is not fully loaded and that causes the scene load with errors.</p>
</blockquote>
</aside>
<p>Thank you Andras. I could replicate the bug by installing BRP on Slicer and then disabling the MarkupsToModel extension it depends on.</p>
<p><a href="https://github.com/Slicer/ExtensionsIndex/search?q=MarkupsToModel" rel="noopener nofollow ugc">These are the Extensions that depend on MarkupsToModel</a></p>
<p>According to <a href="https://github.com/SlicerIGT/SlicerPathReconstruction/blob/5504e03ade1892e7c0186495c21e64ebf93d3cce/CMakeLists.txt" rel="noopener nofollow ugc">the CMakeLists of the PathReconstruction Extension</a></p>
<p>The next lines searching the dependencies are missing on <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/main/CMakeLists.txt" rel="noopener nofollow ugc">BoneReconstructionPlanner CMake file</a>:</p>
<pre><code class="lang-auto">find_package(SurfaceWrapSolidify REQUIRED)
find_package(MarkupsToModel REQUIRED)
find_package(Sandbox REQUIRED)
find_package(SlicerRT REQUIRED)
</code></pre>
<p>I hope it works, we’ll see tomorrow</p>
<p>Thank you</p>

---

## Post #12 by @RafaelPalomar (2022-12-12 14:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="26571">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> had some issues with testing extensions that depend on other extensions - he might have some tips for you.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>, <a class="mention" href="/u/lassoan">@lassoan</a> I’ll have a closer look to this and get back to you</p>

---

## Post #13 by @RafaelPalomar (2022-12-13 15:44 UTC)

<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> we were discussing this topic a few weeks ago in the devs meeting. It seems that tests requiring external module dependencies fail because the dependencies are not loaded in fresh environments. In a development setup, where you manually build the dependencies and set the paths everything should work. However, the testing environment for the extensions tests the modules in an independent manner without considering its dependencies (in the Slicer-Liver, we even have dependencies included in the same extension that are not loaded in some tests, making these fails.</p>
<p>I think this issue should be solved as it will improve the testing dashboards and the quaility of the tests, but solving this problem will require some CMake plumbing work. <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/pieper">@pieper</a> do you agree with this assessment? I could open an issue on this and even try to come up with some ideas if that would be helpful. Unfortunately, today I won’t be able to join the meeteing, but we can have this as a discussion point in upcoming meetings.</p>

---

## Post #14 by @pieper (2022-12-13 20:09 UTC)

<p>We talked about this on today’s call and yes, I think what you describe was the conclusion.  I believe Jc has an idea what needs to be done.</p>

---

## Post #15 by @mau_igna_06 (2022-12-20 20:52 UTC)

<p>Hi</p>
<p>As I see an effort to improve testing documentation <a href="https://github.com/Slicer/Slicer/pull/6742" rel="noopener nofollow ugc">here</a>, I would like to point out that I still cannot solve the issue of the testing data not loaded properly on BoneReconstructionPlanner <a href="https://slicer.cdash.org/test/23669199" rel="noopener nofollow ugc">test</a>. The test data can be loaded properly from the SampleData module GUI</p>
<p>Andras explained the problem below</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="26571">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>In this case, loading of the scene is attempted 3 times because an error occurred during loading. SampleData module tries to download and load a data set 3 times before giving up. So, you need to check what causes the scene loading to return with failure and if you fix it then the scene will only be loaded once and probably all the other errors will go away.</p>
</blockquote>
</aside>

---

## Post #16 by @lassoan (2022-12-20 21:22 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="15" data-topic="26571">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>The test data can be loaded properly from the SampleData module GUI</p>
</blockquote>
</aside>
<p>The problem is that loading of the scene requires SicerIGT extension, which is not loaded when the automatic test is used. If SlicerIGT modules are not present then Slicer does not know about some of the node types that SlicerIGT defines, therefore the loading ends with error code, therefore the SampleData module makes repeated attempts to download and load the scene file (3 times in total) until it gives up.</p>
<p>The fix would be to add all module paths from required extensions to additional module paths when running the tests.</p>

---
