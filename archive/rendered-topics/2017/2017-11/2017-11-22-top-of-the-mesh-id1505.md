# Top of the mesh

**Topic ID**: 1505
**Date**: 2017-11-22
**URL**: https://discourse.slicer.org/t/top-of-the-mesh/1505

---

## Post #1 by @Frederic (2017-11-22 17:11 UTC)

<p>Hi all,<br>
In 3d slicer, I have a point (x,y,z) -a fiducial- into a brain 3D model (mesh). Without changing the x and y coordinates, I would like to create a new point where the z coordinate will be at the top of the mesh. Do you know how could I do that (perhaps by the different voxel value between the inside/outside of the mesh)?</p>
<p>Thanks in advance,<br>
Frederic</p>

---

## Post #2 by @cpinter (2017-11-22 18:33 UTC)

<p>It’s relatively easy to do with some python scripting. Something like this</p>
<pre><code>m=getNode('Segment_1')
mp=m.GetPolyData()
top=-10.0**11
for i in xrange(0, mp.GetNumberOfPoints()):
  p=mp.GetPoint(i)
  if p[2] &gt; top:
    top = p[2]
f=getNode('F')
fp=[0]*4
f.GetNthFiducialWorldCoordinates(0,fp)
fp[2] = top
f.SetNthFiducialWorldCoordinates(0,fp)
</code></pre>
<p>Please note that this is very simplistic (does not account for transforms on the model or the fiducial), and the code snippet is very sloppy (not dynamic, bad variable names etc), but it can be a good starting point.</p>

---

## Post #3 by @lassoan (2017-11-22 19:13 UTC)

<p>To get the “top” point, you can also use <code>GetBounds()</code> method of the vtkPolyData instead of iterating through all the points (which may take long time for large meshes).</p>

---

## Post #4 by @cpinter (2017-11-22 19:27 UTC)

<p>Actually it’s a good point, not sure why I didn’t consider that. Use bounds for sure</p>
<pre><code>b=[0]*3
mp.GetBounds(b)</code></pre>

---

## Post #5 by @Frederic (2017-11-23 10:21 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a> and <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
Thus, the script will be:</p>
<blockquote>
<p>mod = model.GetModelDisplayNode()<br>
mod_out=mod.GetOutputPolyData()<br>
b=[0]*6 #(xmin,xmax, ymin,ymax, zmin,zmax)<br>
mod_out.GetBounds(b)</p>
</blockquote>

---

## Post #6 by @cpinter (2017-11-23 15:33 UTC)

<p>No need to go through the dispay node, it contains display properties so should not be involved.</p>
<pre><code>m=getNode('Segment_1')
mp=m.GetPolyData()
b=[0]*6 #(xmin,xmax, ymin,ymax, zmin,zmax)
mp.GetBounds(b)
f=getNode('F')
fp=[0]*4
f.GetNthFiducialWorldCoordinates(0,fp)
fp[2] = c[5]
f.SetNthFiducialWorldCoordinates(0,fp)</code></pre>

---

## Post #7 by @Frederic (2017-11-23 15:40 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="1505">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>No need to go through the dispay node, it contains display properties so should not be involved.</p>
</blockquote>
</aside>
<p>Thanks for your suggestion.<br>
However, I don’t arrive to acces to the getNode of my model:</p>
<pre><code>filename = "/directory/human-head.stl"
[success, model]= slicer.util.loadModel(filename, returnNode=True)
m=getNode(filename)
mp=m.GetPolyData()
</code></pre>
<p>AttributeError: ‘NoneType’ object has no attribute ‘GetPolyData’</p>
<p>Do you know why?</p>

---

## Post #8 by @cpinter (2017-11-23 16:30 UTC)

<p>If you load the model from file using this script, then you already have the model node in the variable called “model”, so you don’t need to find it in the scene.</p>
<p>Note that the name of the model will not be the full path. If you drag&amp;drop the model and want to know its name, Go to Data module and see the name of your model. Enter the model name instead of “filename”.</p>
<p>A gerenal advice is that in the python interactor you can type commands one by one. After each command it’s prudent to see if the variable contains what you expect or not. The error you got happens because the value of variable “m” will be None.</p>

---

## Post #9 by @Frederic (2017-11-23 16:55 UTC)

<aside class="quote no-group quote-modified" data-username="cpinter" data-post="6" data-topic="1505">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>b=[0]*6 #(xmin,xmax, ymin,ymax, zmin,zmax)<br>
mp.GetBounds(b)<br>
f=getNode(‘F’)<br>
fp=[0]*4<br>
f.GetNthFiducialWorldCoordinates(0,fp)<br>
fp[2] = c[5]<br>
f.SetNthFiducialWorldCoordinates(0,fp)</p>
</blockquote>
</aside>
<p>Thanks a lot for your advice, the correct script is then:</p>
<blockquote>
<p>b=[0]*6 #(xmin,xmax, ymin,ymax, zmin,zmax)<br>
model.GetPolyData().GetBounds(b)<br>
f=getNode(‘F’)<br>
fp=[0]*4<br>
f.GetNthFiducialWorldCoordinates(0,fp)<br>
fp[2] = b[5]<br>
f.SetNthFiducialWorldCoordinates(0,fp)</p>
</blockquote>

---

## Post #10 by @cpinter (2017-11-23 17:28 UTC)

<p>Again, you run unnecessary circles, because “m” will be the same as “model”. Just use “model”</p>

---

## Post #11 by @Frederic (2017-11-23 17:31 UTC)

<p>Ok sorry. Thanks <a class="mention" href="/u/cpinter">@cpinter</a></p>

---
