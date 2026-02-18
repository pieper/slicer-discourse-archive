# Sequence tracking error after installing 29/09 nightly

**Topic ID**: 4235
**Date**: 2018-10-01
**URL**: https://discourse.slicer.org/t/sequence-tracking-error-after-installing-29-09-nightly/4235

---

## Post #1 by @Melanie (2018-10-01 05:52 UTC)

<p>Hi, repeatedly I ve failed to track RAS coordinates of anatomical points marked on my transformed sequence. I ve pasted the log; Could someone help me, whether I ve installed something wrong, is it a problem with my steps. I could do the with the pervious version. Thanks a lot. (sorry tried to enter the log here but does not allow the whole thing)</p>
<details>
<summary>
 see logfile here</summary>
<pre><code class="lang-auto">[WARNING][VTK] 01.10.2018 14:42:32 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [57]
[ERROR][VTK] 01.10.2018 14:42:32 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:42:32 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:42:32 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [57]
[ERROR][VTK] 01.10.2018 14:42:34 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:42:34 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:42:34 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [81]
[ERROR][VTK] 01.10.2018 14:42:34 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:42:34 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:42:34 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [81]
[ERROR][VTK] 01.10.2018 14:42:36 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:42:36 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:42:36 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [81]
[ERROR][VTK] 01.10.2018 14:42:45 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:42:45 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:42:45 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [0]
[ERROR][VTK] 01.10.2018 14:42:45 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:42:45 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:42:45 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [0]
[ERROR][VTK] 01.10.2018 14:45:01 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:45:01 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:45:01 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [0]
[ERROR][VTK] 01.10.2018 14:45:19 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:45:19 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:45:19 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [0]
[ERROR][VTK] 01.10.2018 14:45:38 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:45:38 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:45:38 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [1]
[ERROR][VTK] 01.10.2018 14:45:38 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:45:38 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:45:38 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [1]
[ERROR][VTK] 01.10.2018 14:45:59 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:45:59 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:45:59 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [2]
[ERROR][VTK] 01.10.2018 14:45:59 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:45:59 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:45:59 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [2]
[DEBUG][Qt] 01.10.2018 14:46:03 [] (unknown:0) - Switch to module:  "Transforms"
[DEBUG][Qt] 01.10.2018 14:46:17 [] (unknown:0) - Switch to module:  "Markups"
[DEBUG][Qt] 01.10.2018 14:46:19 [] (unknown:0) - Switch to module:  "Transforms"
[ERROR][VTK] 01.10.2018 14:46:23 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:46:23 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:46:23 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [2]
[ERROR][VTK] 01.10.2018 14:46:33 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:46:33 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:46:33 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [6]
[ERROR][VTK] 01.10.2018 14:46:33 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:46:33 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:46:33 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [6]
[ERROR][VTK] 01.10.2018 14:46:35 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:46:35 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:46:35 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [25]
[ERROR][VTK] 01.10.2018 14:46:35 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:46:35 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:46:35 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [25]
[ERROR][VTK] 01.10.2018 14:46:37 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:46:37 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:46:37 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [44]
[ERROR][VTK] 01.10.2018 14:46:37 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:46:37 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:46:37 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [44]
[ERROR][VTK] 01.10.2018 14:46:39 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:46:39 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:46:39 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [62]
[ERROR][VTK] 01.10.2018 14:46:39 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:46:39 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:46:39 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [62]
[ERROR][VTK] 01.10.2018 14:46:40 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:46:40 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:46:40 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [62]
[ERROR][VTK] 01.10.2018 14:46:51 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:46:51 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:46:51 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [0]
[ERROR][VTK] 01.10.2018 14:46:51 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:46:51 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:46:51 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [0]
[ERROR][VTK] 01.10.2018 14:47:09 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:47:09 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:47:09 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [1]
[ERROR][VTK] 01.10.2018 14:47:09 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:47:09 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:47:09 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [1]
[DEBUG][Qt] 01.10.2018 14:47:17 [] (unknown:0) - Switch to module:  "Markups"
[ERROR][VTK] 01.10.2018 14:47:33 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:47:33 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:47:33 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [2]
[ERROR][VTK] 01.10.2018 14:47:33 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:47:33 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:47:33 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [2]
[ERROR][VTK] 01.10.2018 14:47:39 [vtkMRMLTransformNode (0000027CDBF1ED00)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:47:39 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:47:39 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [3]
[ERROR][VTK] 01.10.2018 14:47:39 [vtkMRMLTransformNode (0000027CDBF1ED00)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:47:39 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:47:39 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [3]
[ERROR][VTK] 01.10.2018 14:47:54 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:47:54 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:47:54 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [4]
[ERROR][VTK] 01.10.2018 14:47:55 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:47:55 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:47:55 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [4]
[ERROR][VTK] 01.10.2018 14:48:54 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:48:54 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:48:54 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [5]
[ERROR][VTK] 01.10.2018 14:48:54 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 14:48:54 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 14:48:54 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [5]
[DEBUG][Qt] 01.10.2018 14:53:37 [] (unknown:0) - Switch to module:  "FiducialRegistrationWizard"
[DEBUG][Qt] 01.10.2018 14:59:22 [] (unknown:0) - Switch to module:  "Markups"
[ERROR][VTK] 01.10.2018 14:59:22 [vtkMRMLMarkupsFiducialNode (0000027CDE69B220)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\MRML\vtkMRMLMarkupsNode.cxx:370) - MarkupExists: n of -1 must be greater than or equal to zero.
[DEBUG][Qt] 01.10.2018 14:59:28 [] (unknown:0) - Switch to module:  "Transforms"
[DEBUG][Qt] 01.10.2018 14:59:37 [] (unknown:0) - Switch to module:  "Markups"
[ERROR][VTK] 01.10.2018 15:01:34 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 15:01:34 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 15:01:34 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [4]
[ERROR][VTK] 01.10.2018 15:01:34 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 15:01:34 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 15:01:34 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [4]
[ERROR][VTK] 01.10.2018 15:01:41 [vtkMRMLTransformNode (0000027CDBF1ED00)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 15:01:41 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 15:01:41 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [3]
[ERROR][VTK] 01.10.2018 15:01:41 [vtkMRMLTransformNode (0000027CDBF1ED00)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 15:01:41 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 15:01:41 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [3]
[ERROR][VTK] 01.10.2018 15:01:49 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 15:01:49 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 15:01:49 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [2]
[ERROR][VTK] 01.10.2018 15:01:49 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 15:01:49 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 15:01:49 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [2]
[ERROR][VTK] 01.10.2018 15:02:03 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 15:02:03 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 15:02:03 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [1]
[ERROR][VTK] 01.10.2018 15:02:03 [vtkMRMLTransformNode (0000027CDE471840)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx:841) - Failed to get transformation matrix because transform is not linear
[WARNING][VTK] 01.10.2018 15:02:03 [] (unknown:0) - Generic Warning: In D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLTransformNode.cxx, line 906
vtkMRMLTransformNode::GetMatrixTransformBetweenNodes failed: expected linear transforms between nodes
[WARNING][VTK] 01.10.2018 15:02:03 [vtkMRMLVolumeRenderingDisplayableManager (0000027CDA7FBB80)] (D:\D\P\Slicer-0\Modules\Loadable\VolumeRendering\MRMLDM\vtkMRMLVolumeRenderingDisplayableManager.cxx:583) - GetVolumeTransformToWorld: Non-linear parent transform found for volume node RT R/U DEV  0.6  Br64 - as a 87 frames Volume Sequence by ImagePositionPatient+AcquisitionTime [1]
</code></pre>
</details>

---

## Post #2 by @lassoan (2018-10-01 14:56 UTC)

<p>The errors indicate that you are trying to volume render a non-linearly transformed sequence. This is currently not supported. You need to harden the transform on each volume (resample image data using the transform). You can use Crop volume sequence module for this resampling.</p>
<p>If your problem is not with volume rendering then let us know what you did exactly, what expected to happen, and what happened instead.</p>

---

## Post #3 by @Melanie (2018-10-01 15:13 UTC)

<p>Thank you very much Prof Lasso <a class="mention" href="/u/lassoan">@lassoan</a>  for your time. I did not want to volume render, I wanted to track marked anatomical points on bone with time. As last time you advised, I did load the 4D dicom data as a volume sequence. Then I registered selected images (as the whole sequence gives error message), to get transform sequence. (fixed frame to moving frame- I did try the other way too) Then I created fiducial node and then applied transform wit transform sequence as the acitive node. (clicked right arrow for Fidcial node and transform volumes).then added markers under the fiducial node. and replayed.  I expected the fiducial markers would indicate the RAS coordinates of the anatomical points that I ve put them on. RAS coordinates do seem to change with playing frame by frame , but when I send them to excel separately it alwayd gives the coordinates of the middle frame/ fixed frame on which I ve put markers on. But on screen RAS coordinates do change.(excel gave changing values when I did it last with a earlier version of slicer, but may be  my steps are faulty)</p>
<p>My questions are am I following the steps that you ve advised in my last post ( I cannot figure out where I ve gone wrong) and second why the RAS change on screen and does not get saved to my fscv file?</p>
<p>I am sorry for taking your time. Your advise is much appreciated. Thank you</p>

---

## Post #4 by @lassoan (2018-10-01 15:31 UTC)

<aside class="quote no-group" data-username="Melanie" data-post="3" data-topic="4235">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>I registered selected images (as the whole sequence gives error message)</p>
</blockquote>
</aside>
<p>What error did you get?</p>
<aside class="quote no-group" data-username="Melanie" data-post="3" data-topic="4235">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>I expected the fiducial markers would indicate the RAS coordinates of the anatomical points that I ve put them on</p>
</blockquote>
</aside>
<p>If you apply a transforms to a node, the node is not changed persistently, but the transformation result is computed in real-time.</p>
<p>To get transformed point coordinates, you can <a href="http://apidocs.slicer.org/master/classvtkMRMLTransformableNode.html#a1e1b5b0059e2eea22224b243492bdc5c">harden the transform</a> on the markup fiducial node at each time step. Since hardening also removes the parent transform, after you switch to the next frame, you probably need to apply the transform to the markup fiducial again, and then harden it.</p>
<p>Another option is to <a href="http://apidocs.slicer.org/master/classvtkMRMLMarkupsFiducialNode.html#a14a8907c299bb3b030e76b15e006505a">retrieve markup points in world coordinates</a>, which are the transformed point coordinates and write those to a text file using Python scripting.</p>

---

## Post #5 by @Melanie (2018-10-01 15:57 UTC)

<p>Thank you ever so much Prof Lasso <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>When I start registering whole sequence which is about 80 to 90 frames each it stops registering after about 20+ frames and says ‘ slicer caught an internal error , you may continue but etc  and stops registering. I have tried reducing the number of frames but sometimes it happens in 17-18 range but never registers beyond frame 30. Not sure it’s my data set , my computer memory ( 8 gb ram and 100 gb remaining in main hard).</p>
<p>If I keep the same fiducial node and markers and command transform for every frame would the fiducial markers give me the exact RAS coordinates  of my marked anatomical points please. This is because if I am place makers manually frame by frame the error is very significant.</p>
<p>Once again I thank you very much for all this help to the research community.</p>

---

## Post #6 by @lassoan (2018-10-01 17:18 UTC)

<aside class="quote no-group" data-username="Melanie" data-post="5" data-topic="4235">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>When I start registering whole sequence which is about 80 to 90 frames each it stops registering after about 20+ frames and says ‘ slicer caught an internal error , you may continue but etc and stops registering</p>
</blockquote>
</aside>
<p>It seems you run out of memory. Since displacement fields are extremely memory consuming (3D vector fields), you need to have huge amount of virtual memory. In Windows, you can set virtual memory size in system settings, on MacOS you need to make sure you have plenty of free hard disk space. Of course, memory swapping slows things down by magnitudes, so if you cannot get more physical memory into your PC then you may consider cropping/downsampling your input using Crop volume sequence module.</p>
<aside class="quote no-group" data-username="Melanie" data-post="5" data-topic="4235">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>This is because if I am place makers manually frame by frame the error is very significant.</p>
</blockquote>
</aside>
<p>Do you place fiducials manually at every frame and/or you place fiducials only on one frame and compute the position on other frames based on the transform sequence?</p>

---

## Post #7 by @Melanie (2018-10-01 20:47 UTC)

<p>I try to do the second (1 frame and compute) because the other way even if I am using existing anatomical details manual placement will give significant error. Thanks a lot Prof Lasso <a class="mention" href="/u/lassoan">@lassoan</a>. Sorry to have posted many questions.</p>
<p>I tried hardening the transform for every frame and also tried transforming the same Fiducial node with every frame of output volumes (active frame is selected as the output sequence)but as you said RAS on screen changes like earlier but when I copy and paste on excel its different. The same value appears on excel sheet . (this did not happen last week). My question is , Is it accurate still to take RAS values appear on screen for tracking the displacement of those fiducial pints I ve marked. If its accurate I can manually enter them into excel as I don’t know any python. I would not mind this being tedious if its accurate.</p>
<p>Thanks again for your time.</p>

---

## Post #8 by @lassoan (2018-10-04 02:40 UTC)

<aside class="quote no-group" data-username="Melanie" data-post="7" data-topic="4235">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>I tried hardening the transform for every frame and also tried transforming the same Fiducial node with every frame of output volumes</p>
</blockquote>
</aside>
<p>Non-transformed values are copied to clipboard (check/uncheck “Transformed” checkbox in Markups module to see transformed/non-transformed values). If you harden the transform on a fiducial node then non-transformed values will not be different anymore (they will be set to the transformed values), so if you copy markups to the clipboard then you’ll have the transformed values on the clipboard.</p>
<aside class="quote no-group" data-username="Melanie" data-post="7" data-topic="4235">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>Is it accurate still to take RAS values appear on screen for tracking the displacement</p>
</blockquote>
</aside>
<p>Yes.</p>

---

## Post #9 by @Melanie (2018-10-04 12:25 UTC)

<p>Thank you very much Prof Lasso. <a class="mention" href="/u/lassoan">@lassoan</a>. I went frame by frame and collected the transformed node coordinates copying it t clipboard. Thanks a lot for all the advice. One last question (sorry for continuing the thread) Should I be concerned that looking at the image my Fiducial points go everywhere  and not on the anatomical point I placed them on? It feels ( to someone who has no software knowledge )as if the pointer is off the place being tracked; But from earlier threads what I understand is that regardless  where the fiducial on the image ( as seen on the view) it gives the correct coordinates? Thanks for your time and concern.</p>

---

## Post #10 by @lassoan (2018-10-04 13:38 UTC)

<aside class="quote no-group" data-username="Melanie" data-post="9" data-topic="4235">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>Should I be concerned that looking at the image my Fiducial points go everywhere and not on the anatomical point I placed them on?</p>
</blockquote>
</aside>
<p>Yes, you should be concerned. Fiducial points should appear at the correct anatomical position. Do they appear at correct position initially and then they move to incorrect positions or they have never been in correct position?</p>

---

## Post #11 by @Melanie (2018-10-04 13:40 UTC)

<p>Thank you very much for replying. Yes, I place them on relevant anatomical points in one frame  (stays there after transforming; cannot see a big difference for 2-3 frames but after about 5-6 frames they are on another bone. )but as the frames n=move on even if I transform each frame the point is quite far off where I place it. Thanks again.</p>

---

## Post #12 by @Melanie (2018-10-04 14:54 UTC)

<p>The moving of F points were not clearly visible because I analyse batch wise, 20 frames. But if frame number 1 and 20 are compared it’s a huge difference from the initial placement.</p>

---

## Post #13 by @Melanie (2018-10-06 07:26 UTC)

<p>I ve pasted the log if its of any help  solving this. I get two problems, sequence registration get stuck in the middle of the process. ( After correcting the memory issue)</p>
<p>Second is fiducial points do move away from where I place it . I am very grateful if you could help. Thanks Prof Lasso <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>[ERROR][VTK] 06.10.2018 14:56:38 [vtkMRMLSequenceNode (000001CC8377D490)] (D:\D\P\S-0-E-b\Sequences\Sequences\MRML\vtkMRMLSequenceNode.cxx:529) - vtkMRMLSequenceNode::GetNthIndexValue failed, invalid seqItemIndex value: 23</p>
<p>[ERROR][VTK] 06.10.2018 14:56:38 [vtkMRMLSequenceNode (000001CC8377D490)] (D:\D\P\S-0-E-b\Sequences\Sequences\MRML\vtkMRMLSequenceNode.cxx:529) - vtkMRMLSequenceNode::GetNthIndexValue failed, invalid seqItemIndex value: 23</p>
<p>[INFO][Stream] 06.10.2018 14:56:39 [] (unknown:0) - ---------------------</p>
<p>[INFO][Python] 06.10.2018 14:56:39 [Python] (C:/Users/melan/AppData/Roaming/NA-MIC/Extensions-27390/SlicerElastix/lib/Slicer-4.9/qt-scripted-modules/Elastix.py:378) - Registering item 5 of 51</p>
<p>[INFO][Stream] 06.10.2018 14:56:39 [] (unknown:0) - Registering item 5 of 51</p>
<p>[INFO][Python] 06.10.2018 14:56:39 [Python] (C:/Users/melan/AppData/Roaming/NA-MIC/Extensions-27390/SlicerElastix/lib/Slicer-4.9/qt-scripted-modules/Elastix.py:378) - Volume registration is started in working directory: D:/slicer temp/Elastix/20181006_145639_659</p>
<p>[INFO][Stream] 06.10.2018 14:56:39 [] (unknown:0) - Volume registration is started in working directory: D:/slicer temp/Elastix/20181006_145639_659</p>
<p>[INFO][Python] 06.10.2018 14:56:40 [Python] (C:/Users/melan/AppData/Roaming/NA-MIC/Extensions-27390/SlicerElastix/lib/Slicer-4.9/qt-scripted-modules/Elastix.py:378) - Register volumes…</p>
<p>ERROR][VTK] 06.10.2018 14:49:11 [vtkMRMLSequenceNode (000001CC8377D490)] (D:\D\P\S-0-E-b\Sequences\Sequences\MRML\vtkMRMLSequenceNode.cxx:529) - vtkMRMLSequenceNode::GetNthIndexValue failed, invalid seqItemIndex value: 20</p>
<p>[ERROR][VTK] 06.10.2018 14:49:11 [vtkMRMLSequenceNode (000001CC8377D490)] (D:\D\P\S-0-E-b\Sequences\Sequences\MRML\vtkMRMLSequenceNode.cxx:529) - vtkMRMLSequenceNode::GetNthIndexValue failed, invalid seqItemIndex value: 20</p>
<p>[ERROR][VTK] 06.10.2018 15:26:00 [vtkMRMLSequenceNode (000001CC8377D490)] (D:\D\P\S-0-E-b\Sequences\Sequences\MRML\vtkMRMLSequenceNode.cxx:529) - vtkMRMLSequenceNode::GetNthIndexValue failed, invalid seqItemIndex value: 34</p>
<p>[ERROR][VTK] 06.10.2018 15:26:00 [vtkMRMLSequenceNode (000001CC8377D490)] (D:\D\P\S-0-E-b\Sequences\Sequences\MRML\vtkMRMLSequenceNode.cxx:529) - vtkMRMLSequenceNode::GetNthIndexValue failed, invalid seqItemIndex value: 34</p>
<p>Zip: adding: D:/slicer temp/__BundleSaveTemp-2018-10-06_16+03+36.638/OutputTransforms0610/Data/Transform_8.h5</p>
<p>[INFO][VTK] 06.10.2018 16:07:14 [] (unknown:0) - Info: In D:\D\P\Slicer-0\Libs\MRML\Logic\vtkArchive.cxx, line 35</p>
<p>Zip: adding rel: OutputTransforms0610/Data/Transform_8.h5</p>
<p>[INFO][VTK] 06.10.2018 16:07:14 [] (unknown:0) - Info: In D:\D\P\Slicer-0\Libs\MRML\Logic\vtkArchive.cxx, line 35</p>
<p>Zip: adding: D:/slicer temp/__BundleSaveTemp-2018-10-06_16+03+36.638/OutputTransforms0610/Data/Transform_9.h5</p>
<p>[INFO][VTK] 06.10.2018 16:07:14 [] (unknown:0) - Info: In D:\D\P\Slicer-0\Libs\MRML\Logic\vtkArchive.cxx, line 35</p>
<p>Zip: adding rel: OutputTransforms0610/Data/Transform_9.h5</p>
<p>[INFO][VTK] 06.10.2018 16:07:14 [] (unknown:0) - Info: In D:\D\P\Slicer-0\Libs\MRML\Logic\vtkArchive.cxx, line 35</p>
<p>Zip: adding: D:/slicer temp/__BundleSaveTemp-2018-10-06_16+03+36.638/OutputTransforms0610/OutputTransforms0610.mrml</p>
<p>[INFO][VTK] 06.10.2018 16:07:14 [] (unknown:0) - Info: In D:\D\P\Slicer-0\Libs\MRML\Logic\vtkArchive.cxx, line 35</p>
<p>Zip: adding rel: OutputTransforms0610/OutputTransforms0610.mrml</p>
<p>[DEBUG][Qt] 06.10.2018 16:07:14 [] (unknown:0) - saved "D:/slicer temp/OutputTransforms0610.seq.mrb"</p>
<p>[DEBUG][Qt] 06.10.2018 16:07:47 [] (unknown:0) - Switch to module: "Sequences"</p>
<p>[DEBUG][Qt] 06.10.2018 16:09:14 [] (unknown:0) - Switch to module: "SequenceBrowser"</p>
<p>[DEBUG][Qt] 06.10.2018 16:09:36 [] (unknown:0) - Switch to module: "SequenceRegistrati</p>

---

## Post #14 by @lassoan (2018-10-06 14:02 UTC)

<p>You may need tens of gigabytes of memory to register long sequences. Specify a shorter range using start/end frames. You may have chosen the transformation direction incorrectly: you can compute motion compensation transform that you apply to images to align all of them to the reference frame; or you can compute tracking transform that will transform your landmark points correctly. Also make sure to specify landmark points on your reference frame. If you can share a sample data set then I can set up the scene and send it back to you.</p>

---

## Post #15 by @Melanie (2018-10-08 05:08 UTC)

<p>Thank you ever so much. How would I share a sample data set  please. Is it as a shorts sequence? Thanks again</p>

---

## Post #16 by @lassoan (2018-10-08 14:37 UTC)

<p>You can upload it to dropbox/onedrive/gdrive and post the link here. Make sure the data does not contain patient identifiable information.</p>

---
