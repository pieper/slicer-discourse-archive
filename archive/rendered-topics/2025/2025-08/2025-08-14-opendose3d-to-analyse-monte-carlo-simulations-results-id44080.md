# OpenDose3D to analyse monte carlo simulations results

**Topic ID**: 44080
**Date**: 2025-08-14
**URL**: https://discourse.slicer.org/t/opendose3d-to-analyse-monte-carlo-simulations-results/44080

---

## Post #1 by @imbeatriz (2025-08-14 13:14 UTC)

<p>Hi everyone,</p>
<p>I am trying to use OpenDose3D to analyse the results of dose images from monte carlo simulations which are in the format .mhd.</p>
<p>From what I understood by the documentation, OpenDose3D is only able to perform the dose analysis of images in the dicom format. I found an old discussion where the author had the results also in metaimage and was asking advice on how to convert to dicom: <a href="https://discourse.slicer.org/t/convert-mhd-dose-volume-to-rtdose-file-and-export/15696" class="inline-onebox">Convert .mhd dose volume to RTDose file and export</a></p>
<p>I followed the video in the solution, however, OpenDose3D isn’t able to perform the analysis when I give the dicom files created. I get this error message:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/home/administrator/Slicer-5.8.0/slicer.org/Extensions-33216/OpenDose3D/lib/Slicer-5.8/qt-scripted-modules/OpenDose3D.py", line 1811, in onInitialButton
    self.getInitialTimeDataFromDICOM()
  File "/home/administrator/Slicer-5.8.0/slicer.org/Extensions-33216/OpenDose3D/lib/Slicer-5.8/qt-scripted-modules/OpenDose3D.py", line 1937, in getInitialTimeDataFromDICOM
    node = NodeDICOM(volumeNodeID, default_isotope="", default_activity=-1)
  File "/home/administrator/Slicer-5.8.0/slicer.org/Extensions-33216/OpenDose3D/lib/Slicer-5.8/qt-scripted-modules/Logic/NodeDICOM.py", line 27, in __init__
    self.setAttributes(default_isotope, default_activity)
  File "/home/administrator/Slicer-5.8.0/slicer.org/Extensions-33216/OpenDose3D/lib/Slicer-5.8/qt-scripted-modules/Logic/NodeDICOM.py", line 80, in setAttributes
    self.setAcquisition()
  File "/home/administrator/Slicer-5.8.0/slicer.org/Extensions-33216/OpenDose3D/lib/Slicer-5.8/qt-scripted-modules/Logic/NodeDICOM.py", line 268, in setAcquisition
    raise DICOMError(f"Attribute '{Attributes().acquisition}' is empty")
Logic.errors.DICOMError
[Python] Failed to read DICOM attribute 'DICOM.Acquisition.Date'
[Python] Attribute 'DICOM.Acquisition.Date' is empty
</code></pre>
<p>Another aspect I would like to understand about OpenDose3D is this: it says its able to analyse dose images resulted from monte carlo simulation from GATE. It even is able to create the macro to run. However, I am not able to upload my simulation image results to the program and for it to simply do the analysis.</p>
<p>I would really appreciate if anyone could give insights on how I could use openDose3D for my situation.</p>
<p>Thank you!</p>
<p>Greetings</p>

---

## Post #2 by @pieper (2025-08-14 14:57 UTC)

<p>I’m not very familiar with OpenDose3D, so I hope someone with more experience can comment on your second question.</p>
<p>But from what I understand of the process, having the correct dicom headers is essential for the calculations, so making sure your dicom files exactly conform to the module’s expectations is key.  I would think the Acquisition Date is one of those variables that’s needed to perform the dose calculations.  You probably need to specify it when you export mha to dicom.</p>

---

## Post #3 by @imbeatriz (2025-08-15 11:38 UTC)

<p>Hi,</p>
<p>Thank you for the suggestion. However, I did that, but I still get the same error. I don’t now if I am converting the mhd image correctly to dicom. This is its format:</p>
<p>ObjectType = Image<br>
NDims = 3<br>
BinaryData = True<br>
BinaryDataByteOrderMSB = False<br>
CompressedData = False<br>
TransformMatrix = -1 0 0 0 -1 0 0 0 1<br>
Offset = 91.654799999999994 140.34999999999999 -140.18799999999999<br>
CenterOfRotation = 0 0 0<br>
ElementSpacing = 2.2100000381469727 2.2100000381469727 2.2100000381469727<br>
DimSize = 125 122 93<br>
AnatomicalOrientation = ???<br>
ElementType = MET_FLOAT<br>
ElementDataFile = DOSE_.raw</p>
<p>Do I have to convert the dose image to RTDOSE file first? Because when I do that the image looks very pixelated and weird.</p>

---

## Post #4 by @pieper (2025-08-15 12:58 UTC)

<p>Looks like you’ve filed an issue at the OpenDose3D gitlab, and that’s the right place to hopefully get your question resolved.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://gitlab.com/opendose/opendose3d/-/issues?show=eyJpaWQiOiIxMTIiLCJmdWxsX3BhdGgiOiJvcGVuZG9zZS9vcGVuZG9zZTNkIiwiaWQiOjE3MTk0NDYyOX0%3D">
  <header class="source">
      <img src="https://gitlab.com/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" class="site-icon" alt="" width="32" height="32">

      <a href="https://gitlab.com/opendose/opendose3d/-/issues?show=eyJpaWQiOiIxMTIiLCJmdWxsX3BhdGgiOiJvcGVuZG9zZS9vcGVuZG9zZTNkIiwiaWQiOjE3MTk0NDYyOX0%3D" target="_blank" rel="noopener">GitLab</a>
  </header>

  <article class="onebox-body">
    <img width="64" height="64" src="https://gitlab.com/uploads/-/system/project/avatar/15399086/Dosimetry4D.png" class="thumbnail onebox-avatar" alt="">

<h3><a href="https://gitlab.com/opendose/opendose3d/-/issues?show=eyJpaWQiOiIxMTIiLCJmdWxsX3BhdGgiOiJvcGVuZG9zZS9vcGVuZG9zZTNkIiwiaWQiOjE3MTk0NDYyOX0%3D" target="_blank" rel="noopener">Issues · OpenDose / SlicerOpenDose3D · GitLab</a></h3>

  <p>This project implements a Slicer3D module aiming for molecular radiotherapy dosimetry</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Ludovic_Ferrer (2025-08-17 21:46 UTC)

<p>Hi,</p>
<p>OpenDose can create Gate macro from the mrmlscene that was created with the patient’s Dicom files. Once the simulation has run, one can get the simulated dose rate images into the dosimetry workflow as you would have gotten from the “normal” algorithms local deposition or kernel dose.</p>
<p>So basically, you cannot import doserate map without processing the upfront part of the workflow.</p>
<p>I hope this clears your interrogation.</p>
<p>Best regards</p>
<p>Ludovic</p>

---

## Post #6 by @imbeatriz (2025-08-27 14:24 UTC)

<p>Hi,</p>
<p>Thank you for the explanation, I understand it better.</p>
<p>So I have the ct and pet image I used for the monte carlo simulations but they aren’t in dicom, they are in .nii. How would I be able to pass them to dicom so that opendose3d can do it’s analysis and i can try using monte carlo gate there?</p>

---

## Post #7 by @Ludovic_Ferrer (2025-09-22 13:34 UTC)

<p>Hi,<br>
Sorry for my late reply.<br>
I am not sure that it would be so easy. The best I can think of would be to create dicom files from your CT/PET nifti files (some tools already exist but I did not try them myself). Alternatively, you use real CT/PET images that are present in the OpenDose3D ressources directory and try to substitute the image part with your nifty … Obviously, you have to change some dicom attributes to fit with your own files (pixel size, radiopharmaceutical injection date, etc.)… A lot of tries and errors in perspective <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=14" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"><br>
Once this is done, you have to process the regular OpenDose3D workflow up to the dose deposition calculation where you select the MC algorithm. Look at the generated gate scripts to look for what is the expected output format (normally nrrd files if I remember correctly) for the dosemap output. If you are able to change the gate’s output file with yours, then you should be able to continue the OpenDose3D process…</p>
<p>As you can imagine, this is a lot of work …with no guarantee of success<br>
Best regards<br>
Ludovic</p>

---
