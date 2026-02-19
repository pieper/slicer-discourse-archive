---
topic_id: 23569
title: "Error With Installing Extension Breast Dcemri Ftv"
date: 2022-05-24
url: https://discourse.slicer.org/t/23569
---

# error with installing extension Breast_DCEMRI_FTV

**Topic ID**: 23569
**Date**: 2022-05-24
**URL**: https://discourse.slicer.org/t/error-with-installing-extension-breast-dcemri-ftv/23569

---

## Post #1 by @gekehe (2022-05-24 19:10 UTC)

<p>Operating system: windows 10<br>
Slicer version: 5.0.2<br>
Expected behavior: installing extension Breast_DCEMRI_FTV and calculate FTV<br>
Actual behavior: I am new here and I installed 3D slicer without reporting any error. An error occured when I installed extension Breast_DCEMRI_FTV: Error retrieving extension metadata: 30822, amd64, , win (expected 0 or 1 result, received 50). Whatever, extension manager showed “Breast_DCEMRI_FTV has been installed” and instructed me to restart 3D slice. After I restarted 3D slicer,  another error appeared: C:\3dslicer\Slicer 5.0.2\lib\Python\Lib\site-packages\dicom_<em>init</em>_.py:53: UserWarning:<br>
This code is using an older version of pydicom, which is no longer<br>
maintained as of Jan 2017.  You can access the new pydicom features and API<br>
by installing <code>pydicom</code> from PyPI.<br>
See ‘Transitioning to pydicom 1.x’ section at <a href="http://pydicom.readthedocs.org" rel="noopener nofollow ugc">pydicom.readthedocs.org</a><br>
for more information.</p>
<p>When I click on the button  “FTV Segmentation” and select “Module 1: Load DCE Images”,  another error occured after I chose a file of dicom data (standard dicom format): Error. Please decompress all files in exam directory, then try running module again. File “C:/3dslicer/Slicer 5.0.2/NA-MIC/Extensions-30822/Breast_DCEMRI_FTV/lib/Slicer-5.0/qt-scripted-modules/DCE_IDandPhaseSelect.py”, line 465, in setup<br>
visnum = self.visitstr<br>
AttributeError: ‘DCE_IDandPhaseSelectWidget’ object has no attribute ‘visitstr’</p>
<p>It seems Breast_DCEMRI_FTV is not compatible to this version of 3D slicer owing to the different versions of python. I checked the manual of  Breast_DCEMRI_FTV written by Rohan Nadkarni, who installed this extension on 3D slicer version 4.11.20200930. However, no usable extension of  Breast_DCEMRI_FTV can be found for this older version of 3D slicer on the extension manager, nor on the official website.</p>
<p>My questions are:</p>
<ol>
<li>Has anyone encountered a similar situation and how did you fix this problem?</li>
<li>Where can I find the extension of Breast_DCEMRI_FTV compatible for 3D slicer version 4.11.20200930?</li>
</ol>

---
