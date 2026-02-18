# Using Markups module in custom Python module

**Topic ID**: 29862
**Date**: 2023-06-06
**URL**: https://discourse.slicer.org/t/using-markups-module-in-custom-python-module/29862

---

## Post #1 by @Patrick_Li (2023-06-06 12:54 UTC)

<p>Hello, I’m working on a custom Python scripted module that’ll deal with contours. Therefore, I want to be able to create markups with the custom module, and save these markups in certain directories after the user has finished drawing. Is there a way to use Markups in my own module?</p>

---

## Post #2 by @Patrick_Li (2023-06-06 18:43 UTC)

<p>I found this on the repository, which brings up a pop-up that allows you to create markups.</p>
<p>w=slicer.qSlicerMarkupsPlaceWidget()<br>
w.setMRMLScene(slicer.mrmlScene)<br>
markupsNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLMarkupsCurveNode”)<br>
w.setCurrentNode(slicer.mrmlScene.GetNodeByID(markupsNode.GetID()))<br>
w.buttonsVisible=False<br>
w.placeButton().show()<br>
w.show()</p>
<p>The issue is that when I use this in my Python file, the pop-up shows up and then immediately closes. Is there a condition I can use to keep the pop-up open until the user closes it?</p>

---

## Post #3 by @pearsonm (2023-06-07 00:57 UTC)

<p>I don’t know what OS you are using but the behavior in linux is that popup will still exist but is behind the Slicer window after placing the Markup.</p>

---

## Post #4 by @Patrick_Li (2023-06-07 02:30 UTC)

<p>I’m on Windows. I can’t find the popup anywhere, not even behind the Slicer window. What seems to happen is that the popup briefly appears before disappearing. However, the markup is still made and accessible in the subject hierarchy, though it has no control points.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/895ac2dadef088af48f941cc7b68b3ea43e65e7a.png" data-download-href="/uploads/short-url/jB5RPPKRobXntz6HUHyts5URKJA.png?dl=1" title="Screenshot (855)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/895ac2dadef088af48f941cc7b68b3ea43e65e7a_2_690x388.png" alt="Screenshot (855)" data-base62-sha1="jB5RPPKRobXntz6HUHyts5URKJA" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/895ac2dadef088af48f941cc7b68b3ea43e65e7a_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/895ac2dadef088af48f941cc7b68b3ea43e65e7a_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/895ac2dadef088af48f941cc7b68b3ea43e65e7a_2_1380x776.png 2x" data-dominant-color="7E828A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (855)</span><span class="informations">1920×1080 203 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @pearsonm (2023-06-07 05:31 UTC)

<p>I tested the script repository code on a fresh install of Slicer stable on Win 10 and the results were the same as linux, the popup persists but moves behind the Slicer window. The code itself works so there must be something else about your system causing it to fail.</p>

---
