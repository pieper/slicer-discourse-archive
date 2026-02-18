# TextNode changes not saved with scene

**Topic ID**: 14664
**Date**: 2020-11-17
**URL**: https://discourse.slicer.org/t/textnode-changes-not-saved-with-scene/14664

---

## Post #1 by @mikebind (2020-11-17 17:24 UTC)

<p>Hi, I am using vtkMRMLTextNodes, but am having problems with modifications to them being saved when I save the scene.  Basically, changes to text nodes never seem to trigger that the scene has been changed or that they have been changed in a way that needs to be saved.  In the save data window, text node lines are never checked as needing saving, and changing only text node text does not indicate that the scene has changed.</p>
<p>Here is a minimal example to reproduce:</p>
<ul>
<li>Open Slicer</li>
<li>At python interactor enter tn = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLTextNode’, ‘testText’)</li>
<li>Save scene</li>
<li>Modify text in text node, either via the Texts module or via tn.setText()</li>
<li>Click to open save data window<br>
The scene does not register that anything has changed, and the mrml line is unchecked. If the text is &gt;250 characters, the text file save line is there, but it is unchecked, even though this is a brand new never-before-saved file.</li>
</ul>
<p>Having the text node send a tn.Modified() signal doesn’t make any difference.</p>
<p>I’m using 4.11.20200930.</p>
<p>I’m guessing that some signal is going awry, but I’m not sure how to figure out what it is or how to fix it if I did realize.  Any help you can provide would be appreciated, thanks!</p>

---

## Post #2 by @lassoan (2020-11-17 20:58 UTC)

<p>Thanks for reporting this. The issue was fixed about a month ago, so it is available in latest preview release, but not in the latest stable release.</p>

---

## Post #3 by @mikebind (2020-11-18 00:04 UTC)

<p>Is the current preview release still pretty unstable due to the VTK9 transition?  If so, is there a way for me to fix it in the current stable release without rebuilding Slicer?</p>

---

## Post #4 by @lassoan (2020-11-18 00:26 UTC)

<p>We reverted to use VTK8.2 in the preview releases until VTK errors are fixed, so it should work well now.</p>

---
