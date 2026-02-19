---
topic_id: 5846
title: "Creating Vtkpolydatamodel From Png Stack"
date: 2019-02-20
url: https://discourse.slicer.org/t/5846
---

# Creating vtkPolyDataModel from PNG stack

**Topic ID**: 5846
**Date**: 2019-02-20
**URL**: https://discourse.slicer.org/t/creating-vtkpolydatamodel-from-png-stack/5846

---

## Post #1 by @Michael_Ef (2019-02-20 14:07 UTC)

<p>Hi all,</p>
<p>so I’m new to slicer and I want to visualize the surface of a stack of png’s by marching cubes algorithm (as python module).<br>
So far my slides are already segmented and registrated, I loaded them to slicer and converted them to a scalar volume node. Now I want to pass these image data to vtkMarchingCubes to generate a surface model of my slides, but after running the algorithm, it returns an empty poly data object.</p>
<p>So could anyone please tell me, what is the best practice to load in the data and process the visualization? And what kind of preprocessing needs to be done to get that running?</p>
<p>Thanks in advance!</p>
<p>Regards Michael</p>

---
