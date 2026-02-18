# DICOM data import error: patients are read as others

**Topic ID**: 12041
**Date**: 2020-06-15
**URL**: https://discourse.slicer.org/t/dicom-data-import-error-patients-are-read-as-others/12041

---

## Post #1 by @Alexandre_Huat (2020-06-15 17:57 UTC)

<p>Operating system: macOS 10.14.6 / Ubuntu 18.04 LTS<br>
Slicer version: 10.4.2<br>
Slicer extension used: SlicerRT</p>
<p>Expected behavior: I have a DICOM RT database: each folder is the RT image set of a specific patient, that is, 1 CT, 1 RTSTRUCT, 1-n RTDOSE, 0-n RTPLAN. Each DICOM series is in its specific subfolder. I open patients one by one using “Load DICOM data &gt; Import &gt; Load”.</p>
<p>When I load a new patient, I expect to visualise it in the Slicer viewers. If necessary, I delete the old patient from the data tree (“Subject Hierarchy”). I precise that I use Slicer <strong>only for visualisation</strong>, I modify no data, I write nothing.</p>
<p>Actual behavior: However, some patients are loaded as other patients. E.g., I load Patient187, I visualize what I need to visualise, then when I load Patient188 different buggy behaviors happen:</p>
<ul>
<li>sometimes the patient just does not load (it says “0 new series” etc.), everything behaves as if Patient188 was Patient187 (at the image and metadata level)</li>
<li>sometimes, if I remove Patient187 from the database before loading Patient188, then Patient188’s metadata are loaded correctly but its images are actually those of Patient187</li>
<li>sometimes, Patient187 is not even the real Patient187 when I compare its images to what I get from other DICOM viewing softwares or from other Slicer installations on other computers</li>
</ul>
<p>These bugs are very worrying. My intern is using Slicer to make quality control and I am afraid that many patients were badly reviewed because the loaded images were actually not those of the corresponding patient.</p>

---

## Post #2 by @lassoan (2020-06-15 18:16 UTC)

<p>All that you describe indicate that the data sets have inconsistent/missing UIDs. Did you modify the images in any way after you retrieved it from the treatment planning system? Have you anonymized the images? If yes, what software did you use for that?</p>
<p>Also make sure that you use latest Slicer Preview Release. We have made lots of improvements in DICOM support in recent years.</p>

---

## Post #3 by @pieper (2020-06-15 18:20 UTC)

<p>I agree with Andras, most likely explanation is that the data is incorrect somehow.  That said, if you ever see issues like this please share data that can be used to recreate and debug the issue.  We take these matters very seriously, so perhaps you can inspect the error logs for anomalies that should be flagged as warning dialogs.</p>

---

## Post #4 by @Alexandre_Huat (2020-06-15 18:57 UTC)

<p>Indeed the data were modified after retrieval. They were anonymized when transferred from the healthcare center to the data curator for storage on external servers. I will check the UIDs and the anonymisation process with the curator.</p>
<p>I was afraid that Slicer Preview Release might be too unstable to be used but I will try on your advice.</p>
<p>I thought about sharing data but I’m not sure about my rights to do so, even if the data were anonymized.</p>

---

## Post #5 by @pieper (2020-06-15 19:09 UTC)

<p>That sounds like a good plan.  For sure don’t share anything unless you are sure it’s okay.  If you are still running into issues see if you can recreate the issue with a scan of a phantom.</p>

---

## Post #6 by @Alexandre_Huat (2020-06-16 19:20 UTC)

<ol>
<li>I have checked the UIDs of the images causing these buggy behaviors (SOP Class, SOP Instance, Study Instance, Series Instance, Frame of Reference): none are the same for the buggy images that I have detected.</li>
<li>I reviewed the anonymization process with the data curator: only the SOP Instance UIDs are modified and the assignement process ensures no duplicates.</li>
<li>After deletion of Documents/SlicerDICOMDatabase and reinstallation of Slicer Stable Release 4.10.2, my intern wasn’t able to reproduce the bug on some patients but it seems to remain on a few others.</li>
</ol>
<p>All of this makes me think that the initial problem is due to Slicer. I stay confused by point 3.</p>
<p>For your record: when trying Slicer Preview Release 4.11.0 on macOS 10.14.6, my intern says the software bugs on start and that she doesn’t succeed in installing the SlicerRT extension. I don’t have enough time to dig into this problem  though.</p>

---

## Post #7 by @lassoan (2020-06-16 19:39 UTC)

<p>If you have data sets to reproduce the problem then it is great, it means that the problem can be easily fixed. If the problem is indeed due to a Slicer bug, then most likely it is already fixed in Slicer-4.11, so it would be great if you could switch to that and ask your intern to report here any problems.</p>

---

## Post #8 by @Alexandre_Huat (2020-06-24 18:44 UTC)

<p>I reexperienced the bug today on an Ubuntu 18.04 installation of Slicer 4.10.2. <strong>I was able to fix it by deleting Documents/SlicerDICOMDatabase</strong> without uninstalling Slicer.  I think I can regard this as a solution. It is good enough in my use case.</p>
<p>If I run into issues again, I will report it.</p>
<p>Thank you for your help.</p>

---

## Post #9 by @lassoan (2020-06-24 18:45 UTC)

<p>Thanks for the update. Please let us know if you find any issues with recent Slicer-4.11 versions.</p>

---

## Post #10 by @Alexandre_Huat (2020-07-15 09:14 UTC)

<p>Small update: A new quality check on the database has shown that some very specific pairs of patients whose images stayed the same after the deletion of DICOMSlicerDatabase were actually real duplicates. That is, the person who uploaded the DICOM data on our servers erroneously uploaded patient A’s images for both patient A and B. This was the source of the unexpected behavior listed in point 3 of <a href="https://discourse.slicer.org/t/dicom-data-import-error-patients-are-read-as-others/12041/6">my answer of June 16</a>.</p>
<p>So I reaffirm the validity of deleting DICOMSlicerDatabase to solve the initial problem.</p>

---
