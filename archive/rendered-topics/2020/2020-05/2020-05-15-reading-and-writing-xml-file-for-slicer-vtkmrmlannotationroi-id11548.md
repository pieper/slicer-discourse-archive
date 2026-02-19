---
topic_id: 11548
title: "Reading And Writing Xml File For Slicer Vtkmrmlannotationroi"
date: 2020-05-15
url: https://discourse.slicer.org/t/11548
---

# Reading and writing xml file for slicer.vtkMRMLAnnotationROINode

**Topic ID**: 11548
**Date**: 2020-05-15
**URL**: https://discourse.slicer.org/t/reading-and-writing-xml-file-for-slicer-vtkmrmlannotationroinode/11548

---

## Post #1 by @rohan_n (2020-05-15 00:02 UTC)

<p>Does anyone have any good examples to share for how the WriteXML() and ReadXMLAttributes() functions of vtkMRMLAnnotationROINode are used?</p>
<p>I did see this link:<br>
<a href="https://apidocs.slicer.org/master/classvtkMRMLAnnotationROINode.html#a59dcbe3b69f14f6b927f605b29390b2f" class="onebox" target="_blank" rel="nofollow noopener">https://apidocs.slicer.org/master/classvtkMRMLAnnotationROINode.html#a59dcbe3b69f14f6b927f605b29390b2f</a></p>
<p>But I would like to see an example of these being used in a module because it’s not clear to me what exactly the inputs should look like based on that documentation.</p>
<p>Thanks,<br>
Rohan</p>

---

## Post #2 by @lassoan (2020-05-15 03:24 UTC)

<p>The methods are used internally when the node is written to/read from a scene file. It should not be necessary for you to use them.</p>
<p>What would you like to achieve?</p>

---

## Post #3 by @rohan_n (2020-05-15 16:23 UTC)

<p>I was hoping Slicer might have built-in functions that I can call in a module to save the center and radius of vtkMRMLAnnotationROINode to an xml file, or to read the center and radius from an xml file and set the initial position of the vtkMRMLAnnotationROINode to the values read from the file.</p>
<p>Although I know how to write functions that do these things, I was wondering if there is an easier way.</p>

---

## Post #4 by @lassoan (2020-05-16 22:18 UTC)

<p>Reading and writing this information to XML files is very easy with vtkXMLDataElement class.</p>

---
