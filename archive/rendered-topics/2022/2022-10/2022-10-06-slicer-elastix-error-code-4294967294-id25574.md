# Slicer Elastix Error Code: 4294967294

**Topic ID**: 25574
**Date**: 2022-10-06
**URL**: https://discourse.slicer.org/t/slicer-elastix-error-code-4294967294/25574

---

## Post #1 by @oliverhalaseh (2022-10-06 14:01 UTC)

<p>Dear All,</p>
<p>I started work on <a href="https://github.com/lassoan/SlicerSegmentationRecipes/tree/master/VesselSegmentationBySubtraction" class="inline-onebox" rel="noopener nofollow ugc">SlicerSegmentationRecipes/VesselSegmentationBySubtraction at master · lassoan/SlicerSegmentationRecipes · GitHub</a><br>
I tried to run the Elastix module, but I keep getting the same error :<br>
Error: Command ‘elastix’ returned non-zero exit status 4294967294.<br>
It occurs in both the Stable(5.0.3) and the Preview Release.<br>
Do you have any solution for it?</p>
<p>Thank You in advance,</p>
<p>Oliver Faris Halaseh</p>

---

## Post #2 by @PalkoD (2023-04-20 15:39 UTC)

<p>Dear All,</p>
<p>I got the same error message: “Command ‘elastix’ returned non-zero exit status 4294967294.”<br>
I am using Windows 10 and Slicer version 5.2.2.</p>
<p>This is the error message from the Python window</p>
<p>[FD] ERROR: the output directory "C:\Users\Palkovics Dániel\AppData\Local\Temp\Slicer\Elastix\20230420_172652_127\result-transform" does not exist.<br>
[FD] You are responsible for creating it.<br>
Traceback (most recent call last):<br>
File “C:/Slice/Slicer 5.2.2/NA-MIC/Extensions-31382/SlicerElastix/lib/Slicer-5.2/qt-scripted-modules/Elastix.py”, line 341, in onApplyButton<br>
self.logic.registerVolumes(self.fixedVolumeSelector.currentNode(), self.movingVolumeSelector.currentNode(),<br>
File “C:/Slice/Slicer 5.2.2/NA-MIC/Extensions-31382/SlicerElastix/lib/Slicer-5.2/qt-scripted-modules/Elastix.py”, line 635, in registerVolumes<br>
self.logProcessOutput(ep)<br>
File “C:/Slice/Slicer 5.2.2/NA-MIC/Extensions-31382/SlicerElastix/lib/Slicer-5.2/qt-scripted-modules/Elastix.py”, line 557, in logProcessOutput<br>
raise subprocess.CalledProcessError(return_code, “elastix”)<br>
subprocess.CalledProcessError: Command ‘elastix’ returned non-zero exit status 4294967294.</p>
<p>Is there a solution to this on Windows?</p>
<p>Thank you very much</p>
<p>Daniel</p>

---

## Post #3 by @lassoan (2023-04-20 16:49 UTC)

<p>Can you check if installing Slicer in a folder that only contains ASCII characters (no accented characters such as <code>á</code>) makes any difference?<br>
Does registration work between <code>MRBrainTumor1</code> and <code>MRBrainTumor2</code> sample data sets?</p>

---
