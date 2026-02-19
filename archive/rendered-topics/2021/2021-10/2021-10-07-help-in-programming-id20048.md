---
topic_id: 20048
title: "Help In Programming"
date: 2021-10-07
url: https://discourse.slicer.org/t/20048
---

# Help in programming

**Topic ID**: 20048
**Date**: 2021-10-07
**URL**: https://discourse.slicer.org/t/help-in-programming/20048

---

## Post #1 by @Bence_Horvath (2021-10-07 09:12 UTC)

<p>Hi,</p>
<p>I would like to get position of a fiducial markup and add it to a variables.</p>
<p>I try this way, but I get ‘none’ for result. There are exist a fiducial.</p>
<p>self.Incus = slicer.qMRMLNodeComboBox()<br>
self.Incus.nodeTypes = [“vtkMRMLMarkupsFiducialNode”]<br>
self.point = self.Incus.currentNode()<br>
pos = [0.0, 0.0, 0.0]<br>
print(self.point.GetNthFiducialPosition(0,pos))</p>
<p>result: None</p>
<p>when I printed only self.point it return all data of the fiducial</p>
<p>Best regards!<br>
Bence</p>

---

## Post #2 by @S_Arbabi (2021-10-07 10:46 UTC)

<p>you can access <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" rel="noopener nofollow ugc">a repository of codes</a> in here, there’s a line of code that can help you:<br>
something like this: fidList.GetNthFiducialWorldCoordinates(0,world)</p>

---

## Post #3 by @cpinter (2021-10-07 13:06 UTC)

<p>Szia Bence,</p>
<p>Your print statement prints out the return value of the function. But GetNthFiducialPosition does not return anything, it puts the result in the argument array, in your case <code>pos</code>.<br>
So if you do <code>print(pos)</code> after the GetNthFiducialPosition call, you’ll see the coordinates.</p>

---

## Post #4 by @Bence_Horvath (2021-10-11 07:13 UTC)

<p>Oooohh,  thank you very very much!!! <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=10" title=":blush:" class="emoji" alt=":blush:"></p>

---

## Post #5 by @Bence_Horvath (2021-10-11 08:44 UTC)

<p>And how can I get positions of LineMarkup’s control point?<br>
GetControlPoints() doesn’t work with “vtkMRMLMarkupsLineNode” .</p>

---

## Post #6 by @cpinter (2021-10-11 11:53 UTC)

<p><code>GetControlPoints</code> is not a Python enabled function. You need to use <code>GetNthControlPointPosition</code>. I think it owuld be useful if you checked out the API. Then you’ll see what you can use. <a href="http://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html" class="inline-onebox">Slicer: vtkMRMLMarkupsNode Class Reference</a></p>

---

## Post #7 by @lassoan (2021-10-11 14:32 UTC)

<p>The most convenient way for getting all the control positions in Python is the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.arrayFromMarkupsControlPointData">slicer.util.arrayFromMarkupsControlPointData</a> function.</p>

---
