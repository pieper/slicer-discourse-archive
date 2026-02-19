---
topic_id: 18849
title: "How To Change Color Of Fudicial And Line"
date: 2021-07-21
url: https://discourse.slicer.org/t/18849
---

# How to change color of fudicial and line?

**Topic ID**: 18849
**Date**: 2021-07-21
**URL**: https://discourse.slicer.org/t/how-to-change-color-of-fudicial-and-line/18849

---

## Post #1 by @Guillaume (2021-07-21 10:17 UTC)

<p>Hello, I still have a problem …<br>
Well I need to change the color of the fudicial, I saw that it was possible but I do not know why, I am blocking with … I have already tried something but without success.</p>
<pre><code class="lang-auto">    viridis = cm.get_cmap('viridis', 8)
    nbClust = -1

    if len(points) != 0:
      for i in range(len(points)):
        if points['nbClust'][i] != nbClust:
          nodeName = f"Cluster {nbClust+2}"
          markupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode", nodeName)
          markupsNode.CreateDefaultDisplayNodes()

        nbClust=points['nbClust'][i]
        pos = [points['p1z'][i], points['p1y'][i], points['p1x'][i]]  

        markupsNode.AddFiducialFromArray(pos, 'point')

        # --------- Couleur ----------
        color = points['volume'][i]/100
        color = viridis(color)

        # color = (r, g, b, a)
        '''
          points = {
                    'p1x': p1[0],
                    'p1y': p1[1],
                    'p1z': p1[2],
                    'volume': volume,
                    'nbClust': nbClust,
                    'red': color[0],
                    'blue': color[1],
                    'green': color[2],
                }
             '''
</code></pre>
<p>So i need to display a part of point with the color.</p>
<p>In addition, I also need to change the color of the lines but hey, there I found nothing.</p>
<p>Thank’s for your help !</p>

---

## Post #3 by @lassoan (2021-07-21 13:02 UTC)

<p>Would you like to display each fiducial point with a different color?</p>

---

## Post #4 by @Guillaume (2021-07-21 13:03 UTC)

<p>No, not especially, I have point clusters registered in different suites. And each suite must have a different color.</p>

---

## Post #5 by @lassoan (2021-07-21 13:16 UTC)

<p>You can use two colors in one markups fiducial list - selected and unselected. See example for setting color <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-markup-fiducial-display-properties">here</a>. API reference is available <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsFiducialDisplayNode.html">here</a> - color setting methods are in “Public member functions inherited from vtkMRMLDisplayNode” section.</p>

---

## Post #6 by @Guillaume (2021-07-21 13:18 UTC)

<p>Oh yes, thank you but I forgot to precise that I work with the 14.11 version.</p>
<p>EDIT:<br>
Finally it works. Great ! Thank you ! But, why I can’t find “SetSelectedColor” in <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsFiducialDisplayNode.html" class="inline-onebox" rel="noopener nofollow ugc">Slicer: vtkMRMLMarkupsFiducialDisplayNode Class Reference</a> ?</p>

---
