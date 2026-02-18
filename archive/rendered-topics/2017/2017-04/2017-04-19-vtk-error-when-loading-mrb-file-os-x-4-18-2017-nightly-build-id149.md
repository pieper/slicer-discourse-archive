# VTK error when loading mrb file [OS X, 4-18-2017 nightly build]

**Topic ID**: 149
**Date**: 2017-04-19
**URL**: https://discourse.slicer.org/t/vtk-error-when-loading-mrb-file-os-x-4-18-2017-nightly-build/149

---

## Post #1 by @hherhold (2017-04-19 16:05 UTC)

<p>Hi,</p>
<p>I have a MRB I’m trying to load, and it gives me the following error:</p>
<p>Error parsing XML in stream at line 62, column 658, byte index 17722: not well-formed (invalid token)</p>
<p>Is this from the mrml file? If so I’ve appended the line below. Any ideas on the problem?</p>
<p>Thanks in advance!</p>
<p>-Hollister</p>
<p>&lt;AnnotationROI<br>
id=“vtkMRMLAnnotationROINode1” name=“AnnotationROI” hideFromEditors=“false” selectable=“true” selected=“false” displayNodeRef=“vtkMRMLAnnotationLineDisplayNode1 vtkMRMLAnnotationPointDisplayNode1 vtkMRMLAnnotationTextDisplayNode1” storageNodeRef=“vtkMRMLAnnotationLinesStorageNode1” references=“display:vtkMRMLAnnotationLineDisplayNode1 vtkMRMLAnnotationPointDisplayNode1 vtkMRMLAnnotationTextDisplayNode1;storage:vtkMRMLAnnotationLinesStorageNode1;” userTags="" referenceNodeID=“None” locked=“0” textList="" textSelected="" textVisible="" ctrlPtsCoord="-300.5 -322 497.5|301 322.5 498" ctrlPtsSelected=“1 1” ctrlPtsVisible=“1 1” ctrlPtsNumberingScheme=“0"linePtsID=“0 1” lineSelected=“1” lineVisible=“1” labelText=”" insideOut=“true” interactiveMode=“true” &gt;</p>

---

## Post #2 by @pieper (2017-04-19 16:23 UTC)

<p>Looks like this was recently fixed by <a class="mention" href="/u/lassoan">@lassoan</a>:</p>
<p><a href="https://github.com/Slicer/Slicer/commit/5a934f44067e50b59fda794ca5511c24da9e2d95" class="onebox" target="_blank">https://github.com/Slicer/Slicer/commit/5a934f44067e50b59fda794ca5511c24da9e2d95</a></p>
<p>To load the existing scene you could add a space manually like in the commit message.</p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @hherhold (2017-04-19 16:34 UTC)

<p>Got it, thank you very much!</p>
<p>-Hollister</p>

---
