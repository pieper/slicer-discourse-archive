# Finding bounding box of the head model

**Topic ID**: 30097
**Date**: 2023-06-17
**URL**: https://discourse.slicer.org/t/finding-bounding-box-of-the-head-model/30097

---

## Post #1 by @Muhammed_Fatih_Talu (2023-06-17 12:47 UTC)

<p>I’m trying to find the values of the bounding box that covers the model.<br>
But the code is very very slow. Is there a different way?</p>
<pre><code class="lang-auto">Widget = slicer.app.layoutManager().threeDWidget(0)
modelDispManager = Widget.threeDView().displayableManagerByClassName("vtkMRMLModelDisplayableManager")

k=1500; minx=k; miny=k; maxx=0; maxy=0;
for i in range(k):
    for j in range(k):
        if modelDisplayableManager.Pick(i,j) and modelDisplayableManager.GetPickedNodeID():
            if i&lt;miny: miny=i;
            if j&lt;minx: minx=j;
            if i&gt;maxy: maxy=i;
            if j&gt;maxx: maxx=j;
print("x:",[minx,maxx],"  y:",[miny,maxy])
</code></pre>

---
