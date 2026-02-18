# Issue using the dicomPatcher through code

**Topic ID**: 2687
**Date**: 2018-04-25
**URL**: https://discourse.slicer.org/t/issue-using-the-dicompatcher-through-code/2687

---

## Post #1 by @EricWilson (2018-04-25 16:30 UTC)

<p>I am trying to patch some problematic dicom files to make sure the patcher will be able to handle any issues when loading dicom files in. running the process through the GUI has no issues, and the patch works as intended. running the code through python generates some issues though. an error is thrown when the patcher is attempting to create an output path for the patched file by using the patient name and patient id attributes from the dicom file. this dicom file has no patient name attribute, so an error is thrown and the process is stopped.</p>
<p>why is this different from the GUI, where no error is thrown for the same file, and how do i fix it?</p>
<p>i’m calling it with the code below. i would also like to know how the logic instance could be accessed without the widget representation, I have only found the abstract class for logic accessible outside of the widget:</p>
<pre><code class="lang-auto">logic = slicer.modules.dicompatcher.widgetRepresentation().self().logic
logic.clearRules()
logic.addRule('NormalizeFileNames')
logic.addRule('GenerateMissingIDs')
outputPath = path + '_DicomPatcherOutput'
logic.patchDicomDir(path, outputPath)

here is the stack trace:
logic.patchDicomDir(path, outputPath)
File "C:/Program Files/Slicer 4.9.0-2018-04-04/lib/Slicer-4.9/qt-scripted-modules/DICOMPatcher.py", line 571, in patchDicomDir
patchedFilePath = rule.generateOutputFilePath(patchedFilePath, ds)
File "C:/Program Files/Slicer 4.9.0-2018-04-04/lib/Slicer-4.9/qt-scripted-modules/DICOMPatcher.py", line 458, in generateOutputFilePath
patientNameID = ds.PatientName+"*"+ds.PatientID
AttributeError: 'str' object has no attribute 'PatientName'
</code></pre>

---

## Post #2 by @lassoan (2018-04-25 20:46 UTC)

<p>Create logic without GUI:</p>
<pre><code>import DICOMPatcher
logic = DICOMPatcher.DICOMPatcherLogic()
</code></pre>
<p>The error is that <code>ds</code> is a string instead of a DICOM dataset. The best would be to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_use_a_visual_debugger_for_step-by-step_debugging">attach a Python debugger</a> and inspect content of <code>ds</code>, the name and content of the file where the problem occurred, etc.</p>

---

## Post #3 by @EricWilson (2018-04-25 21:02 UTC)

<p>the problem is I know it is missing the content piece it is looking for, and that causes the error. if it were just that though, it wouldn’t work in the GUI at all, which it does. so my question is why is it different through code? I just want to be able to handle dicom files that might be missing pieces of information with the patcher.</p>

---

## Post #4 by @lassoan (2018-04-26 13:28 UTC)

<p>I was able to reproduce the problem. You’ve discovered a very interesting bug. <code>generateOutputFilePath</code> method was called with arguments in incorrect order, which flipped the order each time a rule was called. In the GUI, rules were added in a different order, that’s why it worked.</p>
<p>The fix will be included in tomorrow’s nightly build, but you can apply it on your computer right now - you just need to modify a single line: <a href="https://github.com/Slicer/Slicer/commit/937f5803431695549242eff624b23424c618a696">https://github.com/Slicer/Slicer/commit/937f5803431695549242eff624b23424c618a696</a></p>

---

## Post #5 by @EricWilson (2018-04-26 14:15 UTC)

<p>that’s interesting, I’m glad you were able to figure it out. thanks for the fix!</p>

---
