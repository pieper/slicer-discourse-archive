# Slicer mrml scene not loading

**Topic ID**: 2090
**Date**: 2018-02-15
**URL**: https://discourse.slicer.org/t/slicer-mrml-scene-not-loading/2090

---

## Post #1 by @drusmanbashir (2018-02-15 11:05 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.8.1<br>
Expected behavior: Stored studies should load<br>
Actual behavior: Nothing loads and screen remains blank</p>
<p>Hi,<br>
I save a mrml scene with 2x2 view, 1 view containing a PET volume and the rest different MRI sequences. I save all volumes as slicer .nrrd files and the scene as well through the ‘data’ option in the menubar. When i load the scene after starting a new slicer instance, it remains blank even though i can see the mrml file (even .mrb) are quite sizeable</p>

---

## Post #2 by @pieper (2018-02-15 13:39 UTC)

<p>Can you describe steps to recreate the issue using sample data?</p>
<p>Are there messages in the error log? (See the Report a bug in the Help menu).</p>

---

## Post #3 by @drusmanbashir (2018-02-16 21:08 UTC)

<p>Hi,<br>
The steps are very basic. I load a PET volume (DICOM) on slicer. Window it (because for some reason PET volumes always disappear afte loading and presumably after SUV calculator runs on them). Then save the mrml scene AND the PET volume(nrrd) . I have tried saving just mrml scene and same problem.<br>
THe message in the error log says</p>
<p>Error parsing XML in stream at line 36, column 71, byte index 10184: not well-formed (invalid token)</p>

---

## Post #4 by @lassoan (2018-02-16 22:04 UTC)

<p>Can you copy-paste line 36 of the scene .mrml  file?</p>

---

## Post #5 by @drusmanbashir (2018-02-17 10:04 UTC)

<p>Hi Here goes</p>
<pre><code>   &lt;SubjectHierarchyItem id="19" name="research^H&amp;N_INSIGHT_CCR3926 (20140812)" parent="18" type="DICOM" expanded="true" uids="DICOM^1.2.840.113564.9.1.2728161578.69.2.5000656996|" attributes="DICOM.StudyDate^20140812|DICOM.StudyDescription^research^H&amp;N_INSIGHT_CCR3926|DICOM.StudyTime^103856.078000|Level^Study|StudyID^RPY0130070512302|StudyInstanceUID^1.2.840.113564.9.1.2728161578.69.2.5000656996|"&gt;</code></pre>

---

## Post #6 by @lassoan (2018-02-17 14:48 UTC)

<p>The error is due to having special character (&amp;) in the patient name. We’ll fix this soon, but until then you have to manually remove special characters from the patient name in Data module.</p>

---

## Post #7 by @lassoan (2018-02-17 16:38 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Could you have a look and if you can encode/decode subject hierarchy strings when written to XML, using these new methods?</p>
<p><a href="http://apidocs.slicer.org/master/classvtkMRMLNode.html#a565950b5bc18bb237cc4b2b3cd92a248" class="onebox" target="_blank">http://apidocs.slicer.org/master/classvtkMRMLNode.html#a565950b5bc18bb237cc4b2b3cd92a248</a></p>

---

## Post #8 by @cpinter (2018-02-20 15:45 UTC)

<p>Yes I’ll do that soon.</p>

---

## Post #9 by @cpinter (2018-02-23 20:52 UTC)

<p>Fixed in <a href="https://github.com/Slicer/Slicer/commit/1248aef7a85cf430cd8bf9681366001875675d63">https://github.com/Slicer/Slicer/commit/1248aef7a85cf430cd8bf9681366001875675d63</a></p>
<p>This will be available in tomorrow’s preview release.</p>

---

## Post #10 by @drusmanbashir (2018-03-06 14:22 UTC)

<p>Hi, The issue remains as of nightly build 2018-03-04:</p>
<p>Error log:<br>
Error parsing XML in stream at line 36, column 71, byte index 9456: not well-formed (invalid token)</p>
<p>Line 36 of mrml scene (without starting  ‘&lt;’ ):<br>
SubjectHierarchyItem id=“24” name=“Research^CCR3926_H&amp;N_INSIGHT (20160113)” parent=“23” type=“DICOM” expanded=“true” uids=“DICOM^1.2.840.113564.9.1.2843759204.47.2.5000942147|” attributes=“DICOM.StudyDate^20160113|DICOM.StudyDescription^Research^CCR3926_H&amp;N_INSIGHT|DICOM.StudyTime^094327.220000|Level^Study|StudyID^RPY0130094269703|StudyInstanceUID^1.2.840.113564.9.1.2843759204.47.2.5000942147|”</p>

---

## Post #11 by @lassoan (2018-03-06 14:44 UTC)

<p>Thanks for reporting this. I’ve checked this and the problem is that somehow we missed encoding the node names as well. I’ll add this now so it should work in tomorrow’s build.</p>

---
