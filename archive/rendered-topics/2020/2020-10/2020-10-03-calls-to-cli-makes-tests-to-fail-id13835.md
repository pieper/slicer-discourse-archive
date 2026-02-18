# Calls to CLI makes tests to fail

**Topic ID**: 13835
**Date**: 2020-10-03
**URL**: https://discourse.slicer.org/t/calls-to-cli-makes-tests-to-fail/13835

---

## Post #1 by @Alex_Vergara (2020-10-03 03:18 UTC)

<p>In my module I have some calls to Slicer CLI scripts, like brainsresample. In my code I do</p>
<pre><code class="lang-auto">parameters = {'inputVolume': nodeCT.data, 'referenceVolume': nodeSPECT.data, 'outputVolume': CTRSNode,
              'interpolationMode': 'Lanczos', 'defaultValue': minCT}
slicer.cli.run(slicer.modules.brainsresample,
               None, parameters, wait_for_completion=True, update_display=False)
</code></pre>
<p>This makes the <a href="http://slicer.cdash.org/testDetails.php?test=10161333&amp;build=2026803" rel="noopener nofollow ugc">test fail</a> ith this error</p>
<pre><code class="lang-auto">======================================================================
ERROR: runTest (Dosimetry4DTest.Dosimetry4DTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Volumes/D/P/S-0-E-b/OpenDose3D/Dosimetry4D/Logic/Dosimetry4DTest.py", line 79, in runTest
    self.FullTest_positive()
  File "/Volumes/D/P/S-0-E-b/OpenDose3D/Dosimetry4D/Logic/Dosimetry4DTest.py", line 484, in FullTest_positive
    self.logic.resampleCT()
  File "/Volumes/D/P/S-0-E-b/OpenDose3D-build/lib/Slicer-4.13/qt-scripted-modules/Logic/Dosimetry4DLogic.py", line 601, in resampleCT
    None, parameters, wait_for_completion=True, update_display=False)
  File "/Volumes/D/P/S-0-build/Slicer-build/bin/Python/slicer/cli.py", line 72, in run
    node = createNode(module, parameters)
  File "/Volumes/D/P/S-0-build/Slicer-build/bin/Python/slicer/cli.py", line 13, in createNode
    node = cliLogic.CreateNodeInScene()
AttributeError: 'SlicerBaseLogic.vtkSlicerModuleLogic' object has no attribute 'CreateNodeInScene'

----------------------------------------------------------------------
</code></pre>
<p>Has something changed in <code>cli.py</code> or in the <code>cliLogic</code>?</p>

---

## Post #2 by @jamesobutler (2020-10-03 12:58 UTC)

<p>Note that if this error just recently happened it is probably due to the update of the preview build to use VTK9. So there’s likelihood of a lot of underlying issues since VTK is a core dependency. Things will stabilize over the next week or more.</p>

---

## Post #3 by @Alex_Vergara (2020-10-04 17:31 UTC)

<p>if it helps this is the line that raises the exceptions <a href="https://github.com/Slicer/Slicer/blob/0b1560371fa1ad1bc0d87f42004353e66f583535/Libs/MRML/Core/vtkMRMLScene.cxx#L314" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/0b1560371fa1ad1bc0d87f42004353e66f583535/Libs/MRML/Core/vtkMRMLScene.cxx#L314</a></p>

---

## Post #4 by @Alex_Vergara (2020-10-08 12:53 UTC)

<p>Recently <a href="https://discourse.slicer.org/t/calls-to-cli-makes-tests-to-fail/13835">I have reported</a> some test failing in CDash.</p>
<p>The main error is</p>
<pre><code class="lang-auto">======================================================================
ERROR: runTest (Dosimetry4DTest.Dosimetry4DTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Volumes/D/P/S-0-E-b/OpenDose3D/Dosimetry4D/Logic/Dosimetry4DTest.py", line 79, in runTest
    self.FullTest_positive()
  File "/Volumes/D/P/S-0-E-b/OpenDose3D/Dosimetry4D/Logic/Dosimetry4DTest.py", line 484, in FullTest_positive
    self.logic.resampleCT()
  File "/Volumes/D/P/S-0-E-b/OpenDose3D-build/lib/Slicer-4.13/qt-scripted-modules/Logic/Dosimetry4DLogic.py", line 614, in resampleCT
    None, parameters, wait_for_completion=True, update_display=False)
  File "/Volumes/D/P/S-0-build/Slicer-build/bin/Python/slicer/cli.py", line 72, in run
    node = createNode(module, parameters)
  File "/Volumes/D/P/S-0-build/Slicer-build/bin/Python/slicer/cli.py", line 13, in createNode
    node = cliLogic.CreateNodeInScene()
AttributeError: 'SlicerBaseLogic.vtkSlicerModuleLogic' object has no attribute 'CreateNodeInScene'

----------------------------------------------------------------------
</code></pre>
<p>Digging a little in Slicer code I found that indeed there is no ‘CreateNodeInScene’ attribute inside ‘SlicerBaseLogic.vtkSlicerModuleLogic’, but it exists inside ‘SlicerBaseLogic.vtkSlicerCLIModuleLogic’. The first is abstract class now and the second inherits from the first. Somehow the cli is losing the concrete class and it is using the abstract one.</p>
<p>Has somebody else noticed this behaviour?</p>

---

## Post #5 by @lassoan (2020-10-08 13:04 UTC)

<p>This works well for me:</p>
<pre><code class="lang-python">cliModule = slicer.modules.resamplescalarvolume
cliLogic = cliModule.logic()
parameterNode = cliLogic.CreateNodeInScene()
print(parameterNode)
</code></pre>
<p>Can you provide a minimal example that reproduces the problem you have?</p>
<p>Typically if Python cannot find a specific class (and returns a class at a higher level in the hierarchy) if the Python module is not imported. You may need to do something like <code>import vtkSomeLibraryPython</code> before you try to access a class defined in <code>SomeLibrary</code>. Normally this import happens automatically for all modules that follow conventions but maybe you do something special or something broke in Slicer.</p>
<p>If you experience this in latest Slicer master then enter a bug report and we’ll get to it when other VTK upgrade related errors are fixed.</p>

---

## Post #6 by @Alex_Vergara (2020-10-08 13:49 UTC)

<p>It works well for me too in Slicer directly and even in my Docker image pre VTK change. It only raises this exception in the CDash build system.</p>
<p>Maybe I shall create a more recent Docker image to test.</p>

---

## Post #7 by @Alex_Vergara (2020-10-09 14:06 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="6" data-topic="13835">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Maybe I shall create a more recent Docker image to test.</p>
</blockquote>
</aside>
<p>The new Docker version (bishopwolf/slicer3d-nightly:0.4.2) still behaves normally, these errors are not showing. I don’t know how to reproduce the problem. But it is still present in CDash.</p>

---

## Post #8 by @Alex_Vergara (2020-10-10 18:43 UTC)

<p>Tried with home made Slicer in Manjaro with qt 5.15.1. No test failed. I am out of options to try to replicate the CDash errors.</p>

---

## Post #9 by @lassoan (2020-10-10 18:50 UTC)

<p>I could reproduce the problem on Windows by simply building a latest Slicer master version. We’ll get to it after we fixed more urgent issues (e.g., image not appearing in slice views).</p>

---

## Post #10 by @lassoan (2020-10-11 02:45 UTC)

<p>Using Slicer-4.11.20200930:</p>
<pre><code class="lang-nohighlight">&gt;&gt;&gt; slicer.vtkSlicerCLIModuleLogic()
(qSlicerBaseQTCLIPython.vtkSlicerCLIModuleLogic)00000167BA933648
</code></pre>
<p>Using latest master:</p>
<pre><code class="lang-nohighlight">&gt;&gt;&gt; slicer.vtkSlicerCLIModuleLogic()
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
TypeError: this class cannot be instantiated
</code></pre>
<p>I’ve debugged into wrappython.exe and the problem is that for some reason the hierarchy cannot find the parent’s class in the hierarchy and so it determines that vtkSlicerCLIModuleLogic is not a VTK class, therefore it looks for a public constructor (instead of <code>New()</code>), which is of course is not found. <a class="mention" href="/u/jcfr">@jcfr</a> I guess you know what’s going on. Could you have a look?</p>

---

## Post #11 by @Alex_Vergara (2020-10-25 18:49 UTC)

<p>Any news on this? I am still getting these errors in CDash</p>

---

## Post #12 by @lassoan (2020-10-25 21:07 UTC)

<p>We still have higher-priority issues to fix in Slicer-4.13, but I’ve added a ticket to ensure that it gets fixed: <a href="https://github.com/Slicer/Slicer/issues/5266">https://github.com/Slicer/Slicer/issues/5266</a></p>

---

## Post #13 by @Alex_Vergara (2020-11-12 14:29 UTC)

<p>In the <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2020-11-12&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Opendose" rel="noopener nofollow ugc">last CDash</a> this issue appears to be solved</p>

---

## Post #14 by @lassoan (2020-11-12 14:34 UTC)

<p>The issue probably has not been resolved yet, we just switched back temporarily to VTK8 in factory builds due to this and other problems. Keep discussion at <a href="https://github.com/Slicer/Slicer/issues/5266">https://github.com/Slicer/Slicer/issues/5266</a> to avoid parallel discussion of the same issue at two places.</p>

---

## Post #15 by @gaoyi.cn (2021-02-04 11:51 UTC)

<p>I had the same issue: calling cli.run gives the error.<br>
and i confirm that reverting to VTK8 solves the problem.</p>

---
