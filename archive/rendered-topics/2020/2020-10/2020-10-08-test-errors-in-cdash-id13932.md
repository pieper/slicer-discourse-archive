# Test errors in CDash

**Topic ID**: 13932
**Date**: 2020-10-08
**URL**: https://discourse.slicer.org/t/test-errors-in-cdash/13932

---

## Post #1 by @Alex_Vergara (2020-10-08 12:53 UTC)

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

## Post #2 by @lassoan (2020-10-08 13:05 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/calls-to-cli-makes-tests-to-fail/13835">Calls to CLI makes tests to fail</a></p>

---

## Post #3 by @lassoan (2020-10-08 13:05 UTC)



---
