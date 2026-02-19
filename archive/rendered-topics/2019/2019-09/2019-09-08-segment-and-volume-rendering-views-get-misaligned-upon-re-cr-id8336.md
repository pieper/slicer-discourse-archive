---
topic_id: 8336
title: "Segment And Volume Rendering Views Get Misaligned Upon Re Cr"
date: 2019-09-08
url: https://discourse.slicer.org/t/8336
---

# Segment and Volume Rendering views get misaligned upon re-Crop input volume

**Topic ID**: 8336
**Date**: 2019-09-08
**URL**: https://discourse.slicer.org/t/segment-and-volume-rendering-views-get-misaligned-upon-re-crop-input-volume/8336

---

## Post #1 by @chir.set (2019-09-08 11:41 UTC)

<p>Hello,</p>
<p>The pictures below show that a segment gets displaced, or does not follow a re-cropped volume.</p>
<p>To reproduce :<br>
Crop a volume (CTA-Cardio here)<br>
Paint anything with a big sphere brush in Segment Editor and show its 3D representation<br>
Go to Volume Rendering and apply any filter<br>
Go back to Crop Volume, modify the bounds (enlarge here), and apply while keeping the same output node name<br>
In the 3D view, the 3D Volume Rendering view and the segment are no longer aligned</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/857c661c4ef362654c9af173e388cb250e16fd3a.png" alt="0" data-base62-sha1="j2S1FtojZfCsgxwynyqkcuu7AIq" width="644" height="455"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cd1f863d01696bef37c608bfe6cea3714248c5b.png" alt="1" data-base62-sha1="df7MLmUBVjd6Uv6sqs4pEyEPWpZ" width="644" height="455"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c161693cd31d4297fed092580ea3f43011d2dfd1.png" alt="2" data-base62-sha1="rAIQX5KiyI3onv3wGp3OhSk0wzn" width="644" height="455"></p>
<p>Is it a feature or does it need a fix ?</p>
<p>Regards.</p>

---

## Post #2 by @chir.set (2019-09-09 13:27 UTC)

<p>It’s related to LR alignment of the 3D view that is detached from the ROI coordinates. Segment representation is an artifact in the description, that showed the problem initially.</p>
<p>This <a href="https://yadi.sk/i/UU77UM4gAlbxEg" rel="nofollow noopener">screen recording</a> illustrates the problem.</p>

---

## Post #3 by @cpinter (2019-09-10 18:20 UTC)

<p>Thanks for the investigation and the video! It seems that the problem is neither in Segment Editor / Segmentation, nor Crop Volume, but in Volume Rendering. Is there anything you can do to fix this misalignment issue? Like Enable/Disable cropping, change preset or the transfer function… it might give us a clue where the bug is. Also is there any suspicious error in the log?</p>

---

## Post #4 by @chir.set (2019-09-10 20:20 UTC)

<p>The 3D Volume Rendering view remains unaligned for whatever value of</p>
<ul>
<li>Preset (transfer function I suppose)</li>
<li>Crop or Display ROI (in Volume Rendering widget)</li>
<li>CPU or GPU rendering</li>
<li>Memory size</li>
<li>Quality</li>
<li>Technique (Composite with shading, Maximim/Minimum intensity)</li>
<li>Surface smoothing</li>
<li>Synchronize with volume module</li>
<li>‘Closing/Opening’ the eye icon</li>
</ul>
<p>The 3D view gets aligned back correctly if one of these is changed :</p>
<ul>
<li>Memory size</li>
<li>Quality</li>
<li>Technique (Composite with shading, Maximim/Minimum intensity)</li>
<li>Surface smoothing</li>
</ul>
<p>Here is a sample console output :</p>
<blockquote>
<p>Switch to module:  “Volumes”<br>
Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
QObject::connect: No such signal ctkDoubleSpinBox::valueChanged(int)<br>
QObject::connect:  (sender name:   ‘NumberOfScalarsSpinBox’)<br>
QObject::connect:  (receiver name: ‘qMRMLVolumeInfoWidget’)<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Loading Slicer RC file [/home/user/.slicerrc.py]<br>
Loaded volume from file: /home/user/Desktop/BIG/Slicer/CTA-cardio.nrrd. Dimensions: 512x512x321. Number of components: 1. Pixel type: short.</p>
<p>“Volume” Reader has successfully read the file “/home/user/Desktop/BIG/Slicer/CTA-cardio.nrrd” “[1.17s]”<br>
Switch to module:  “CropVolume”<br>
void qSlicerCropVolumeModuleWidget::setInputROI(vtkMRMLNode*) : invalid parameter node<br>
Found SharedObject Module<br>
ModuleType: SharedObjectModule<br>
Resample Scalar/Vector/DWI Volume command line:</p>
<p>slicer:0x7f5ede5e6d00 --processinformationaddress 0x8d5bd08 --hfieldtype h-Field --interpolation linear --transform_order output-to-input --image_center input --spacing 0.933594,0.933594,1.25 --size 24,49,63 --origin 55.3847,70.2063,-66.9684 --direction_matrix -1,0,0,0,-1,0,0,0,1 --number_of_thread 0 --default_pixel_value 0 --window_function c --spline_order 3 --transform_matrix 1,0,0,0,1,0,0,0,1,0,0,0 --transform a slicer:0x1c758e0#vtkMRMLScalarVolumeNode1 slicer:0x1c758e0#vtkMRMLScalarVolumeNode2</p>
<p>Switch to module:  “VolumeRendering”<br>
Switch to module:  “CropVolume”<br>
Found SharedObject Module<br>
ModuleType: SharedObjectModule<br>
Resample Scalar/Vector/DWI Volume command line:</p>
<p>slicer:0x7f5ede5e6d00 --processinformationaddress 0x815acc8 --hfieldtype h-Field --interpolation linear --transform_order output-to-input --image_center input --spacing 0.933594,0.933594,1.25 --size 51,49,63 --origin 80.6069,70.2063,-66.9684 --direction_matrix -1,0,0,0,-1,0,0,0,1 --number_of_thread 0 --default_pixel_value 0 --window_function c --spline_order 3 --transform_matrix 1,0,0,0,1,0,0,0,1,0,0,0 --transform a slicer:0x1c758e0#vtkMRMLScalarVolumeNode1 slicer:0x1c758e0#vtkMRMLScalarVolumeNode2</p>
<p>Switch to module:  “VolumeRendering”</p>
</blockquote>
<p>I may give more information as per your instructions.</p>
<p>Regards.</p>

---

## Post #5 by @lassoan (2019-09-11 03:53 UTC)

<p>This was very useful, thank you, we could reproduce and fix the error (<a href="https://github.com/Slicer/Slicer/commit/d287bbb2467b0cbaeed7b39791c46005e364c27f">r28493</a>).</p>

---
