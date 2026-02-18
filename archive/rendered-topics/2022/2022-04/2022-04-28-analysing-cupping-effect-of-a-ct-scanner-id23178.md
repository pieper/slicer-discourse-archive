# Analysing Cupping Effect of a CT-Scanner

**Topic ID**: 23178
**Date**: 2022-04-28
**URL**: https://discourse.slicer.org/t/analysing-cupping-effect-of-a-ct-scanner/23178

---

## Post #1 by @Joshua (2022-04-28 16:47 UTC)

<p>Hello,<br>
I’d like to analyse the homogeneity of the voxel values along the x, y and z axis.<br>
Is there any way of getting the mean voxel value of an area along an axis.<br>
Like for each slice the same area → calculating the voxel value mean of that are → Plotting voxel value over the depth of the slice [mm].</p>
<p>I hope you understand what i mean and can help me out.</p>

---

## Post #2 by @Joshua (2022-05-19 19:27 UTC)

<p>I Wrote a Python Program to solve my problem</p>
<blockquote>
<p><span class="hashtag-raw">#Bereich</span> in z Richtung</p>
<pre><code>#x 122 bis 153 (31 Pixel)

#y 71 bis 107 (36 pixel)

#Slices 140 bis 800 (660)
</code></pre>
<p>n=getNode(“NodeName”)</p>
<p>nD=n.GetDisplayNode()</p>
<p>a=array(“NodeName”)</p>
<p>mid = <span class="chcklst-box fa fa-square-o fa-fw"></span></p>
<p>z = 0</p>
<p>sum = 0</p>
<p>h=0</p>
<p>for s in range(140, 802): <span class="hashtag-raw">#662</span> Slices 140 bis einschließlich 801</p>
<pre><code>for y in range(71, 108): #37 Pixel 71 bis 107 fließt ein

    for x in range(122, 154): #32 Pixel 122 bis 153 fließt ein

        if z &lt; 1184:

            sum = sum + a[s,y,x]

            z = z + 1

        else:

            m = sum / z    

            mid.append(m)

            sum = 0

            z = 0

            sum = sum + a[s,y,x]

            z = z + 1
</code></pre>
<p>m=sum/z</p>
<p>mid.append(m)</p>
<p>import numpy as np</p>
<p>np.savetxt(“DateiName.csv”, mid, delimiter=‘,’) # zum Exportieren</p>
</blockquote>
<blockquote>
<p><span class="hashtag-raw">#Bereich</span> in x Richtung</p>
<p>n=getNode(“NodeName”)</p>
<p>nD=n.GetDisplayNode()</p>
<p>a=array(“NodeName”)</p>
<p>mid = <span class="chcklst-box fa fa-square-o fa-fw"></span></p>
<p>z = 0</p>
<p>sum = 0</p>
<p>h=0</p>
<p>for x in range(56, 325): # 269 Pixel 56 bis 324 fließt ein</p>
<pre><code>for s in range(40, 891): # 851 Slices 40 bis einschließlich 890

    for y in range(214, 244): # 32 Pixel 123 bis 155 fließt ein

        if z &lt; 25530:

            sum = sum + a[s,y,x]

            z = z + 1

        else:

            m = sum / z    

            mid.append(m)

            sum = 0

            z = 0

            sum = sum + a[s,y,x]

            z = z + 1
</code></pre>
<p>m=sum/z</p>
<p>mid.append(m)</p>
<p>import numpy as np</p>
<p>np.savetxt(“DateiName.csv”, mid, delimiter=‘,’) # zum Exportieren</p>
</blockquote>

---
