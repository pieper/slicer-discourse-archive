# Remove CT patient bed from dicom file automatically

**Topic ID**: 23614
**Date**: 2022-05-27
**URL**: https://discourse.slicer.org/t/remove-ct-patient-bed-from-dicom-file-automatically/23614

---

## Post #1 by @gzt036 (2022-05-27 19:04 UTC)

<p>Is it possible to remove CT bed background noise from DICOM automatically without opening Slicer’s graphic window? The python script needs to be run by the server so human intervene needs to be avoided. My question is,</p>
<ol>
<li>is there any scripts available for this</li>
<li>how could I run the script<br>
Thanks!</li>
</ol>

---

## Post #2 by @lassoan (2022-05-27 23:11 UTC)

<p>Are all the images acquired by the same scanner, of the same body part, using the same imaging protocol? Or you are looking for a completely generic solution that can blank out the patient table on any CT image?</p>

---

## Post #3 by @gzt036 (2022-05-27 23:32 UTC)

<p>The images could be different. However, I would only be interested in the bones. Yes, I am looking for a completely generic solution to remove the patient bed from the images. Thanks.</p>

---

## Post #4 by @lassoan (2022-05-28 02:17 UTC)

<p>If you are only interested in the bones then it’s not a hard problem because there is always enough low-density material (muscles, fat, skin, padding on the table) to separate your region of interest (bones) from the table.</p>
<p>I’ve developed a short script for this some time ago, but to make it easier to use, I’ve now added it as a <a href="https://github.com/PerkLab/SlicerSandbox#remove-ct-table">module in the Sandbox extension</a>:</p>
<p>                    <a href="https://raw.githubusercontent.com/PerkLab/SlicerSandbox/master/RemovePatientTable.jpg" target="_blank" rel="noopener" class="onebox">
            <img src="https://raw.githubusercontent.com/PerkLab/SlicerSandbox/master/RemovePatientTable.jpg" width="690" height="419">
          </a>

</p>
<p>It will be available in the extensions manager from tomorrow.</p>

---

## Post #5 by @gzt036 (2022-05-28 06:12 UTC)

<p>Your solution looks great. Is it possible to run the script and obtain the modified DICOM files without opening slicer or any human intervention. Thanks!</p>

---

## Post #6 by @lassoan (2022-05-28 11:58 UTC)

<p>Yes, everything that you can do using the GUI of Slicer is accessible via Python scripting.</p>
<p>I would recommend to spend some time with testing on a handful of randomly selected cases, carefully inspect the results and see if the default parameters work or if you need some tuning. Let me know if you think the defaults would need to be changed.</p>
<p>Then, you can use examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a> to see how to load images from DICOM and how to write results to files using Python scripting. You can see in the <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/RemoveCtTable/RemoveCtTable.py#L407">module’s unit test</a> how you can use it from a script. Note that you can <a href="https://github.com/Slicer/SlicerJupyter">use Slicer as a Jupyter kernel</a>, if you like working with notebooks.</p>

---
