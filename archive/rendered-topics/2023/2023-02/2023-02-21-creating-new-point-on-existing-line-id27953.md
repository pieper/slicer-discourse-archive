---
topic_id: 27953
title: "Creating New Point On Existing Line"
date: 2023-02-21
url: https://discourse.slicer.org/t/27953
---

# Creating new point on existing line

**Topic ID**: 27953
**Date**: 2023-02-21
**URL**: https://discourse.slicer.org/t/creating-new-point-on-existing-line/27953

---

## Post #1 by @eliagre (2023-02-21 15:27 UTC)

<p>Hello,</p>
<p>My question is: Is there a way to define a new point on an existing line, based on the distance from one of the two points defining the line, preferably in percentages?<br>
The situation: I want to crop a model in a standardized way by using cut planes. For my model, there are only a limited number of landmarks available, so I would like to create new points to create the plane. I found two good landmarks/points to use and placed a line in between these points. Now I would like to create a new point on this line. This point should be placed on 80% of the distance between the points, starting from one of the points defining this line. E.g. if the line (defined by points A and B) is 10 cm long, I would like a point C on this line that is 8 cm away from A and 2 from B.<br>
I realize that this can probably be done by defining a sphere with a defined radius (e.g. 8 cm) and point A as the center and by then trying to intersect this sphere and the line to create the point. Although this seems like a long process to me. Is there any other way to obtain this point?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @muratmaga (2023-02-21 17:31 UTC)

<p>This is doable with a few lines of python code. First off though, line tool in slicer is restricted to two control points. So you can’t really add a third one to it. But you can do what you describe with the open curve tool, which will allow you do what you described. The rest is geometry.</p>
<p>Take a look at the python script repository to see how you can interact markups programmatically.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#adding-control-points-programmatically" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#adding-control-points-programmatically</a></p>

---

## Post #3 by @chir.set (2023-02-21 21:04 UTC)

<aside class="quote no-group" data-username="eliagre" data-post="1" data-topic="27953">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eliagre/48/18509_2.png" class="avatar"> eliagre:</div>
<blockquote>
<p>placed a line in between these points</p>
</blockquote>
</aside>
<p>Do you mean a markups line node ? As <a class="mention" href="/u/muratmaga">@muratmaga</a> said, there can be only 2 points.</p>
<aside class="quote no-group" data-username="eliagre" data-post="1" data-topic="27953">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eliagre/48/18509_2.png" class="avatar"> eliagre:</div>
<blockquote>
<p>define a new point on an existing line</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="eliagre" data-post="1" data-topic="27953">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eliagre/48/18509_2.png" class="avatar"> eliagre:</div>
<blockquote>
<p>trying to intersect this sphere and the line</p>
</blockquote>
</aside>
<p>We may conclude that you are interested in a point coordinate only, is it so ?</p>

---

## Post #4 by @eliagre (2023-02-22 08:46 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="27953">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>We may conclude that you are interested in a point coordinate only, is it so ?</p>
</blockquote>
</aside>
<p>Yes, I only need the point coordinate. I just wondered if there was any tool that allows to slide a point along a line (markups line node). This would allow me to see how the position of this point affects my plane. Does there exist anything like that (or is it easy to code)?</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="27953">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>This is doable with a few lines of python code. First off though, line tool in slicer is restricted to two control points. So you can’t really add a third one to it. But you can do what you describe with the open curve tool, which will allow you do what you described. The rest is geometry.</p>
</blockquote>
</aside>
<p>Right now, I fixed it with this script, but it still requires to define the desired distance between the two points. (I’m new to coding in python, so my apologies if the code is not so elegant).</p>
<p>pointListNode = slicer.util.getNode(“F”)<br>
data = <span class="chcklst-box fa fa-square-o fa-fw"></span><br>
for fidIndex in range(pointListNode.GetNumberOfControlPoints()):<br>
coords=[0,0,0]<br>
pointListNode.GetNthControlPointPosition(fidIndex,coords)<br>
data.append(coords)</p>
<p>distance_between_points = [data[0][0]-data[1][0], data[0][1]-data[1][1], data[0][2]-data[1][2]]<br>
percentage = float(input("What percentage do you want to use? "))<br>
added_value = [i * percentage for i in distance_between_points]<br>
new_coord = [data[0][0]-added_value[0], data[0][1]-added_value[1], data[0][2]-added_value[2]]<br>
slicer.modules.markups.logic().AddControlPoint(new_coord[0], new_coord[1], new_coord[2])</p>

---

## Post #5 by @chir.set (2023-02-22 11:05 UTC)

<aside class="quote no-group" data-username="eliagre" data-post="4" data-topic="27953">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eliagre/48/18509_2.png" class="avatar"> eliagre:</div>
<blockquote>
<p>Yes, I only need the point coordinate.</p>
</blockquote>
</aside>
<p>You may use this function to get a coordinate along a line (p1, p2) at a specified distance relative to p2.</p>
<pre><code class="lang-auto">def findLinearCoordinateByDistance(p1, p2, difference):
    rp2 = [ p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]]
    lineLength = math.sqrt(vtk.vtkMath().Distance2BetweenPoints(p1, p2))
    factor = (1.0 + (difference / lineLength))
    result = [ p1[0] + (rp2[0] * factor), p1[1] + (rp2[1] * factor), p1[2] + (rp2[2] * factor) ]
    return result
</code></pre>
<p>If you have a Fiducial node with 2 points, and you want a third point at 80% distance from p1 :</p>
<pre><code class="lang-auto">import math

# Paste the above function

f = slicer.util.getNode("F")
p1 = [ 0.0 ] * 3
p2 = [ 0.0 ] * 3
f.GetNthControlPointPositionWorld(0, p1)
f.GetNthControlPointPositionWorld(1, p2)
lineLength = math.sqrt(vtk.vtkMath().Distance2BetweenPoints(p1, p2))
newCoordinate = findLinearCoordinateByDistance(p1, p2, -lineLength * 0.2)
f.AddControlPointWorld(newCoordinate)
</code></pre>

---

## Post #6 by @chir.set (2023-02-22 11:10 UTC)

<aside class="quote no-group" data-username="eliagre" data-post="4" data-topic="27953">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eliagre/48/18509_2.png" class="avatar"> eliagre:</div>
<blockquote>
<p>slide a point along a line</p>
</blockquote>
</aside>
<p>You may check ‘<a href="https://github.com/vmtk/SlicerExtension-VMTK/tree/master/StenosisMeasurement1D" rel="noopener nofollow ugc">Stenosis measurement : 1D</a>’ module in SlicerVMTK extension, that you may install using the ‘Extensions manager’.</p>
<p>The input is a Markups open curve. In your case, use a curve with 3 points and slide the second point. You may experiment with more points also.</p>
<p>Please note that this module was written for a specific use case, hence its name. I suppose it could fit your purpose AFAIU.</p>

---
