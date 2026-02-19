---
topic_id: 8718
title: "Vtklookuptable Bad Table Range 0 1"
date: 2019-10-09
url: https://discourse.slicer.org/t/8718
---

# vtkLookUpTable. Bad table range: [0, -1]

**Topic ID**: 8718
**Date**: 2019-10-09
**URL**: https://discourse.slicer.org/t/vtklookuptable-bad-table-range-0-1/8718

---

## Post #1 by @danial (2019-10-09 13:51 UTC)

<p>Operating system: macOS 10.14.6<br>
Slicer version: 4.10.2</p>
<p>Hello,</p>
<p>I used a vtkLookUpTable to color a vtkPolyData like this :</p>
<pre><code>vtkSmartPointer&lt;vtkPolyData&gt; surface = m_optimizations.at(i).m_map-&gt;getShape();

 // set the lookup table (allows to draw each vertex with its own color, according to the table of values resulting from the occlusion filter)
 vtkLookupTable *vtkLUT = vtkLookupTable::New();
 vtkLUT-&gt;SetTableRange(0.0, 255.0);
 vtkLUT-&gt;SetNumberOfTableValues(26);
 vtkLUT-&gt;SetTableValue(0, 0.0, 0.5, 1.0, 1); // blue
 vtkLUT-&gt;SetTableValue(1, 0.0, 0.8, 0.5, 1); // green
 vtkLUT-&gt;SetTableValue(2, 0.0, 1.0, 0.0, 1); // green
 vtkLUT-&gt;SetTableValue(3, 0.0, 1.0, 0.0, 1); // green
 vtkLUT-&gt;SetTableValue(4, 0.2, 1.0, 0.0, 1); // green-yellow
 vtkLUT-&gt;SetTableValue(5, 0.2, 1.0, 0.0, 1); // green-yellow
 vtkLUT-&gt;SetTableValue(6, 0.5, 1.0, 0.0, 1); // yellow-green
 vtkLUT-&gt;SetTableValue(7, 0.8, 1.0, 0.0, 1); // yellow-green
 vtkLUT-&gt;SetTableValue(8, 0.5, 1.0, 0.0, 1); // yellow-green
 vtkLUT-&gt;SetTableValue(9, 0.8, 1.0, 0.0, 1); // yellow-green
 vtkLUT-&gt;SetTableValue(10, 1.0, 1.0, 0.0, 1); // yellow
 vtkLUT-&gt;SetTableValue(11, 1.0, 1.0, 0.0, 1); // yellow
 vtkLUT-&gt;SetTableValue(12, 1.0, 0.8, 0.3, 1); // yellow-orange
 vtkLUT-&gt;SetTableValue(13, 1.0, 0.8, 0.3, 1); // yellow-orange
 vtkLUT-&gt;SetTableValue(14, 1.0, 0.5, 0.0, 1); // orange
 vtkLUT-&gt;SetTableValue(15, 1.0, 0.5, 0.0, 1); // orange
 vtkLUT-&gt;SetTableValue(16, 1.0, 0.2, 0.0, 1); // dark orange
 vtkLUT-&gt;SetTableValue(17, 1.0, 0.2, 0.0, 1); // dark orange
 vtkLUT-&gt;SetTableValue(18, 1.0, 0.0, 0.0, 1); // red
 vtkLUT-&gt;SetTableValue(19, 1.0, 0.0, 0.0, 1); // red
 vtkLUT-&gt;SetTableValue(20, 1.0, 0.0, 0.0, 1); // red
 vtkLUT-&gt;SetTableValue(21, 1.0, 0.0, 0.0, 1); // red
 vtkLUT-&gt;SetTableValue(22, 1.0, 0.0, 0.0, 1); // red
 vtkLUT-&gt;SetTableValue(23, 1.0, 0.0, 0.0, 1); // red
 vtkLUT-&gt;SetTableValue(24, 1.0, 0.0, 0.0, 1); // red
 vtkLUT-&gt;SetTableValue(25, 1.0, 0.0, 0.0, 1); // red
 vtkLUT-&gt;Build();

 surface-&gt;GetPointData()-&gt;GetScalars()-&gt;SetLookupTable(vtkLUT);
</code></pre>
<p>But this message is appeared regularly :</p>
<blockquote>
<p>Bad table range: [0, -1]</p>
</blockquote>
<p>Can you help me to solve this problem, please ?</p>
<p>Thank you.</p>

---

## Post #3 by @lassoan (2019-10-09 15:24 UTC)

<p>Why do you do this? What would you like to achieve? Normally in Slicer you use MRML color node to set up color mapping for models.</p>

---

## Post #4 by @danial (2019-10-09 15:57 UTC)

<p>Thank you for this solution.</p>

---
