# Crashes when selecting directory to save models & segments

**Topic ID**: 45877
**Date**: 2026-01-23
**URL**: https://discourse.slicer.org/t/crashes-when-selecting-directory-to-save-models-segments/45877

---

## Post #1 by @merrikat (2026-01-23 05:36 UTC)

<p><strong>Issue:</strong> Whenever I try to save my segmentation or model files and I open the window to change which directory to save files into (whether I use the ‘…’ or ‘Change directory for selected files,’ 3D Slicer will crash while I am selecting a folder, eg when I double click on the folder.</p>
<p>I am currently using version 5.10.0 for Linux and updated to this version after this problem started occurring while I was using 5.6.1 for Linux. I was able to save segments previously on 5.6.1 and I’m not sure what could have changed and created this issue. Slicer only doesn’t crash if I am saving a segmentation file that contains a single segment. Once I add a second segment, the issue reoccurs and I lose my work.</p>
<p>I have the whole bug report from the last session which crashed, but it is too long to include the whole thing, so I’ve included the last few lines. Please let me know if some other part is needed.</p>
<details open="">
<summary>
Error log</summary>
<p>/home/banham112/QMG Applications/Slicer-5.10.0-linux-amd64/bin/../lib/Slicer-5.10/cli-modules/Decimation --reductionFactor 0.63 --method FastQuadric --deleteBoundary --aggressiveness 7.0 /tmp/Slicer-banham112/EIIBD_vtkMRMLModelNodeH.obj /tmp/Slicer-banham112/EIIBD_vtkMRMLModelNodeH.obj[INFO][VTK] 23.01.2026 10:53:14 [vtkSlicerCLIModuleLogic (0x1b39a6c0)] (/work/Stable/Slicer-0/Base/Logic/vtkSlicerCLIModuleLogic.cxx:1868) - Decimation standard output:</p>
<p>Input: 1353054 vertices,2703424 triangles (target 1000267)Output: 501421 vertices,1000266 triangles (0.63 reduction)[INFO][VTK] 23.01.2026 10:53:14 [vtkSlicerCLIModuleLogic (0x1b39a6c0)] (/work/Stable/Slicer-0/Base/Logic/vtkSlicerCLIModuleLogic.cxx:1894) - Decimation completed without errors[WARNING][VTK] 23.01.2026 10:53:15 [vtkMRMLModelStorageNode (0x25c8f0f0)] (vtkMRMLModelStorageNode.cxx:452) - ReadDataInternal (vtkMRMLModelStorageNode2): File /tmp/Slicer-banham112/EIIBD_vtkMRMLModelNodeH.obj does not contain coordinate system information. Using LPS.[INFO][Python] 23.01.2026 10:53:15 [Python] (/home/banham112/QMG Applications/Slicer-5.10.0-linux-amd64/bin/../lib/Slicer-5.10/qt-scripted-modules/SurfaceToolbox.py:655) - Processing completed in 8.70 seconds[DEBUG][Qt] 23.01.2026 10:53:17  (unknown:0) - Switch to module:  “Data”[WARNING][Qt] 23.01.2026 10:53:51  (unknown:0) - WARNING QAccessibleTable::indexOfChild Fix my children… QAccessible::Client “”</p>
</details>

---

## Post #2 by @ebrahim (2026-01-23 06:27 UTC)

<p>I could not reproduce this. I tried with some sample data, adding two segments are you said. I’m on Ubuntu 22.04 using Slicer 5.10.</p>
<p>Does it happen for you in a fresh scene with sample data, or do you only get this crash when starting from some specific scene?</p>

---

## Post #3 by @merrikat (2026-01-23 07:45 UTC)

<p>Thanks for your reply - this computer is running Ubuntu 20.04.6 LTS. I actually haven’t been loading in scenes at all, always importing an .nrrd image stack on its own each time to work from. I just tried loading a different set of data (same file type) and still got the same crash. Maybe it’s worth testing other sample data, but I’m not sure how to find that.</p>
<p>Unfortunately it’s also been happening with just one segment since I made my first post.</p>
<p>I tried troubleshooting the error logs with chatGPT and it got me to try disabling different qt &amp; dbus (I’m afraid I’m completely unfamiliar) accessibility-type settings when booting 3D slicer, but didn’t have any luck.</p>

---

## Post #4 by @muratmaga (2026-01-23 15:55 UTC)

<aside class="quote no-group" data-username="merrikat" data-post="3" data-topic="45877">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/e5b9ba/48.png" class="avatar"> merrikat:</div>
<blockquote>
<p>. I actually haven’t been loading in scenes at all, always importing an .nrrd image stack on its own each time to work from.</p>
</blockquote>
</aside>
<p>That might be your problem. Import the image stack, then save it immediately as a NRRD file and see if it crashes. Then reset your Slicer reload the NRRD file you saved (do not import the imagestack), and then proceed with segmentaiton and let us know whether this works or not.</p>

---
