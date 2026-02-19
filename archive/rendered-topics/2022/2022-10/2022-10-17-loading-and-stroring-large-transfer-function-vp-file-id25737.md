---
topic_id: 25737
title: "Loading And Stroring Large Transfer Function Vp File"
date: 2022-10-17
url: https://discourse.slicer.org/t/25737
---

# loading and stroring large transfer function (vp file)

**Topic ID**: 25737
**Date**: 2022-10-17
**URL**: https://discourse.slicer.org/t/loading-and-stroring-large-transfer-function-vp-file/25737

---

## Post #1 by @Amin_Nasim_saravi (2022-10-17 20:44 UTC)

<p>Hello,</p>
<p>I’m working on a project to automatically create transfer functions (TF) and use Slicer as a reference and also to render the results. The approach is as follows,</p>
<ol>
<li>I generate a transfer function.</li>
<li>I sample it and put the values in VP format.</li>
<li>I load the VP file in Slicer and see the results.<br>
However, the problem is as I get more samples from the generated TF (say 50 or 100) slicer discards values at the end of the range.<br>
Is there a way to increase the Slicer’s threshold when dealing with vp files?</li>
</ol>
<p>Thanks</p>

---

## Post #2 by @lassoan (2022-10-17 20:55 UTC)

<p>Currently, line length in .vp files is (quite arbitrarily) <a href="https://github.com/Slicer/Slicer/blob/367c2bb2426e36ad9c7cb41fdbd4dd45b2ddb972/Modules/Loadable/VolumeRendering/MRML/vtkMRMLVolumePropertyStorageNode.cxx#L77">limited to 1024 characters</a>. This is certainly not nice and it should not be hard to change this (probably we could just use the C++ verison of getline that does not require preallocation of a buffer).</p>
<p>Transfer functions are expected to contain only a limited number of control points to make sure they are conveniently editable; and usually there is a limit in how many different structures can be distinguished by varying the colors. Could you tell a bit more about your use case? Where do these large number of control points come from? Are you considering using volume rendering for displaying labelmap volumes with many labels?</p>

---

## Post #3 by @Amin_Nasim_saravi (2022-10-17 22:33 UTC)

<p>In my experiment, I’m using machine learning to produce a customized transfer function (TF) for a given volume, mapping the scalar field to RGBA. The TF is continuous (regression) and can be a bit spiky in some cases. I sample the TF and store it in VP format. It would be amazing if I could feed this kinda big VP file to Slicer.</p>

---

## Post #4 by @pieper (2022-10-17 23:14 UTC)

<p>Yes, the .vp files are pretty ad hoc - at the time I recall that we looked around for some standard way to store them but couldn’t find anything so we came up with something simple.  It would be great to remove the 1024 character limitation.</p>
<p>As a side note I’l mention that there is now a dicom standard for volume rendering.  It covers a lot of territory in addition to transfer functions and I’ve never looked seriously at whether we could support this in Slicer (I’m not sure any other software supports it since it is so broad).</p>
<p><a href="https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.80" class="onebox" target="_blank" rel="noopener">https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_A.80</a></p>

---
