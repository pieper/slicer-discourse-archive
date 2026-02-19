---
topic_id: 14895
title: "Model Maker Crashes Slicer"
date: 2020-12-05
url: https://discourse.slicer.org/t/14895
---

# Model Maker crashes Slicer

**Topic ID**: 14895
**Date**: 2020-12-05
**URL**: https://discourse.slicer.org/t/model-maker-crashes-slicer/14895

---

## Post #1 by @chir.set (2020-12-05 11:17 UTC)

<p>I know that Model Maker is <a href="https://discourse.slicer.org/t/model-maker-does-not-create-model-from-label-map/3977/6">dinosaur</a> and have not been using it since long.</p>
<p>Just had a try today with a labelmap volume and noticed that Slicer always crashes with the following output :</p>
<blockquote>
<p>“Volume” Reader has successfully read the file “/home/user/Desktop/BIG/Slicer/aaa_cropped.nrrd” “[0.21s]”<br>
Switch to module:  “ModelMaker”<br>
Found SharedObject Module<br>
ModuleType: SharedObjectModule<br>
Model Maker command line:</p>
<p>slicer:0x7fbd4d292940 --processinformationaddress 0x55ab86373828 --color /tmp/Slicer/CAJAJJ_vtkMRMLColorTableNodeFileGenericColors.txt.ctbl --modelSceneFile /tmp/Slicer/CAJAJJ_AxHfbdCcAACcAA.mrml#vtkMRMLModelHierarchyNode1 --name Model --generateAll --start -1 --end -1 --skipUnNamed --smooth 10 --filtertype Sinc --decimate 0.25 --splitnormals --pointnormals --pad slicer:0x55ab80098da0#vtkMRMLLabelMapVolumeNode1</p>
<p>vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open /home/user/slicer:0x55ab80098da0#vtkMRMLLabelMapVolumeNode1. ITK exception info: error in unknown:  Could not create IO object for reading file slicer:0x55ab80098da0#vtkMRMLLabelMapVolumeNode1<br>
The file doesn’t exist.<br>
Filename = slicer:0x55ab80098da0#vtkMRMLLabelMapVolumeNode1</p>
<p>Algorithm vtkITKArchetypeImageSeriesScalarReader(0x7fbd2c1bf3d0) returned failure for request: vtkInformation (0x7fbd2c1bdce0)<br>
Debug: Off<br>
Modified Time: 363522<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
ALGORITHM_AFTER_FORWARD: 1<br>
FORWARD_DIRECTION: 0</p>
<p>No whole extent has been set in the information for output port 0 on algorithm vtkITKArchetypeImageSeriesScalarReader(0x7fbd2c1bf3d0).</p>
<p>error: [/home/user/programs/Slicer/bin/SlicerApp-real] exit abnormally - Report the problem.</p>
</blockquote>
<p>Reporting it for any useful purpose. The module is still available.</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2020-12-05 16:04 UTC)

<p>Does enabling “Prefer executable CLIs” in application settings / Modules fix the problem?</p>

---

## Post #3 by @chir.set (2021-02-01 18:42 UTC)

<p>Sorry, I missed your reply.</p>
<p>Enabling “Prefer executable CLIs” in application settings / Modules does fix the problem.</p>
<p>Thanks.</p>

---
