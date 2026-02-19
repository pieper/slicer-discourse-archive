---
topic_id: 2648
title: "Is It Possible To Edit The Imageorientationpatient Dicom Tag"
date: 2018-04-20
url: https://discourse.slicer.org/t/2648
---

# Is it possible to edit the ImageOrientationPatient DICOM tag in slicer?

**Topic ID**: 2648
**Date**: 2018-04-20
**URL**: https://discourse.slicer.org/t/is-it-possible-to-edit-the-imageorientationpatient-dicom-tag-in-slicer/2648

---

## Post #1 by @Lowey (2018-04-20 13:42 UTC)

<p>Hi,</p>
<p>I am hoping it is possible to edit the ImageOrientationPatient DICOM tag and associated image within Slicer.</p>
<p>My problem,</p>
<p>I have a CT image which has been transformed with 6 degrees of freedom (3 Translations and 3 Rotations), hence, its ImageOrientationPatient DICOM tag has gone from [1;0;0;0;1;0]  to [0.9998;0.0189;0.0056;-0.0189;0.9998;-0.0056]</p>
<p>I want to dose a dose calculation on the transformed CT, however, my treatment planning system does not allow dose calculations on tilted images. Is there a way I can correct the ImageOrientationPatient DICOM tag back to [1;0;0;0;1;0] within Slicer? This would also be required for the radiotherapy structures DICOM file too</p>
<p>Many thanks!!</p>

---

## Post #2 by @ihnorton (2018-04-20 13:54 UTC)

<p><s>I don’t think this can be done within Slicer, but there are command line tools that can edit headers.</s></p>
<p>As you are likely aware, extreme caution, prudence, and oversight should be exercised when integrating any non-standard modifications into a human clinical pipeline. Note that Slicer is not FDA approved (although some Slicer-based products could potentially be – with liability assumed by the providing commercial entity). The open source Slicer license <a href="https://github.com/Slicer/Slicer/blob/0f8926d1391f5abc2be845890dae369453465317/License.txt#L147-L156">explicitly disclaims liability</a> for clinical use.</p>

---

## Post #3 by @lassoan (2018-04-20 21:06 UTC)

<p>Actually, Slicer can solve this. Correct loading of tilted-gantry images has been recently added. You have to enable application of an acquisition transform in Application Settings / DICOM section. Then:</p>
<ul>
<li>load the volume from DICOM</li>
<li>go to Transforms module and “harden” on the acquisition transform on the volume</li>
<li>go to Data module and right-click on the volume to export to DICOM</li>
</ul>
<p>Gantry-tilted acquisitions are quite rare and so this feature is not tested extensively, but it should work. Let us know if you have any issues.</p>

---

## Post #4 by @Lowey (2018-04-23 01:45 UTC)

<p>Thank you kindly for your reply! Much appreciated!</p>

---

## Post #5 by @Lowey (2018-05-02 04:33 UTC)

<p>Hi Andras,</p>
<p>I have tried the approach you suggested above but seem to be having difficulty. I am using Slice version 4.8.1</p>
<p>To confirm, this is what I have done,</p>
<ol>
<li>Open Slicer, go to Edit &gt; Application Settings. Then under the DICOM section I changed the Acquisition geometry regularization field to ‘apply regularization transform’</li>
<li>Imported my tilted CT volume. Note the gantry isn’t tilted but the treatment couch is, leading to a non-[1;0;0;0;1;0] value for ImageOrientationPatient</li>
<li>Went to the Transforms module, but there is no ‘acquisition transform’ to harden</li>
<li>I tried hardening a new transform, but after exporting the DICOM CT volume is still tilted</li>
</ol>
<p>Any suggestions would be fantastic!</p>
<p>EDIT: I have found that for some patient data, I am indeed able to harden the ‘deformed image export acquisition transform’. However, once I export this, my treatment planning system still registers a tilted image</p>
<p>Thanks</p>

---

## Post #6 by @lassoan (2018-05-02 05:57 UTC)

<p>If gantry was not tilted then it is even simpler: save your data set as .nrrd file, then load the .nrrd file - but before clicking OK in “Add data…” dialog check “Show options” checkbox and check “Ignore Orientation” checkbox.</p>

---

## Post #7 by @JFC (2025-06-25 08:01 UTC)

<p>Dear Nick:<br>
I am new with 3D slicer. Please, may I conatct you regarding the same issue you posted?. Thanks so  much for your support. Sincerely<br>
Juan Francisco</p>

---
