# Issue with ProjectSemiLM

**Topic ID**: 41438
**Date**: 2025-02-01
**URL**: https://discourse.slicer.org/t/issue-with-projectsemilm/41438

---

## Post #1 by @Dlmeyer (2025-02-01 00:52 UTC)

<p>Hello, I am trying to use the ProjectSemiLM utility to project a field of pseudolandmarks across my dataset of Squamate wrist elements. I have manually placed 6 orientation landmarks on each element, and have selected one out of the sample to be the base mesh on whcih I generated the pseudolandmarks.</p>
<p>When I try this, I reveive the following warning message, which repeats for each elemetn I am trying to project the landmarks on:</p>
<p>“Warning: In vtkMRMLMarkupsNode.cxx, line 3166<br>
vtkMRMLMarkupsFiducialNode (000002951C72DBB0): vtkMRMLMarkupsNode::GetMarkupPoint method is deprecated, please use GetNthControlPointPosition instead”</p>
<p>I was wondering if there was something wrong with the way that my orientation landmarks are formatted (I have them all saved as .mrk.json files, or if there was some other way I could address this.</p>
<p>Thanks,<br>
Dalton</p>

---

## Post #2 by @muratmaga (2025-02-01 01:45 UTC)

<p>While annoying,  it is a warning.  You can ignore.</p>
<p>Are lms not projected?</p>

---

## Post #3 by @Dlmeyer (2025-02-01 02:33 UTC)

<p>No, the lms are not being projected, I had assumed that was why.</p>
<p>This traceback message also comes up:</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/Dalton/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/ProjectSemiLM.py”, line 198, in onApplyButton<br>
logic.run(self.modelSelector.currentNode(), self.baseLMSelect.currentNode(), self.baseSLMSelect.currentNode(), self.meshDirectory.currentPath,<br>
File “C:/Users/Dalton/AppData/Local/slicer.org/Slicer 5.8.0/slicer.org/Extensions-33216/SlicerMorph/lib/Slicer-5.8/qt-scripted-modules/ProjectSemiLM.py”, line 239, in run<br>
subjectID = [int(x) for x in regex.findall(meshFileName)][0]<br>
IndexError: list index out of range</p>

---

## Post #4 by @muratmaga (2025-02-01 09:48 UTC)

<p>Error suggest there is an issue with the number of landmarks in you samples, but I can’t replicate on my end.</p>
<p>Can you provide a sample test of your LMs?</p>

---

## Post #5 by @Dlmeyer (2025-02-01 16:26 UTC)

<p>Absolutely, I just sent you some of them via email. Thank you very much.</p>

---

## Post #6 by @Dlmeyer (2025-02-06 18:14 UTC)

<p>Just wanted to update that this issue was solved with the latest update to SlicerMorph! I still had to go in and change many of the file names in order to successfully process the entire dataset, but it worked!</p>
<p>-Thanks so much to the dev team!</p>

---
