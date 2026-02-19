---
topic_id: 22440
title: "How To Change Line Color"
date: 2022-03-10
url: https://discourse.slicer.org/t/22440
---

# how to change line color?

**Topic ID**: 22440
**Date**: 2022-03-10
**URL**: https://discourse.slicer.org/t/how-to-change-line-color/22440

---

## Post #1 by @wiselyfox (2022-03-10 21:25 UTC)

<blockquote>
<p>I use ‘vtkMRMLMarkupsLineNode’ function to define five lines,but how to change these lines’s color?<br>
use python complete this job .</p>
</blockquote>
<p>slicer.util.loadMarkupsFiducialList(“D:\m.fcsv”)<br>
import numpy as np</p>
<p>def file2array(path, delimiter=’ '):<br>
path = ‘D:\F.txt’<br>
fp = open(path, ‘r’, encoding=‘utf-8’)<br>
string = fp.read()<br>
fp.close()<br>
row_list = string.splitlines()<br>
data_list = [[float(i) for i in row.strip().split(delimiter)] for row in row_list]<br>
return np.array(data_list)</p>
<p>xa = file2array(‘./data.txt’)<br>
n=0<br>
while n&lt;=len(xa):<br>
print(xa[n:n+2])<br>
curveNode = slicer.mrmlScene.AddNewNodeByClass(“<strong>vtkMRMLMarkupsLineNode</strong>”)<br>
slicer.util.updateMarkupsControlPointsFromArray(curveNode, xa[n:n+2])<br>
n+=2<br>
if n==len(xa):<br>
break</p>

---
