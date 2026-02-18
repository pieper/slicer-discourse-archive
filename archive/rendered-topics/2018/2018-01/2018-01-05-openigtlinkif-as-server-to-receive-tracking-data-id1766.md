# OpenIGTLinkIF as server to receive tracking data

**Topic ID**: 1766
**Date**: 2018-01-05
**URL**: https://discourse.slicer.org/t/openigtlinkif-as-server-to-receive-tracking-data/1766

---

## Post #1 by @terajnol (2018-01-05 15:48 UTC)

<p>Hi all,</p>
<p>Still working on the PlusToolkit for my Xsens IMU. Because it is not that easy for me, I also try to work in parallel directly with the OpenIGTLink library (to get a functionnal prototype faster).</p>
<p>I am trying to receive data through the OpenIGTLinkIF module (using Slicer as a server). In parallel, I run an OpenIGTLink example (TrackerClient). I want to be able to use the module both as a front-end user and in a python script.</p>
<ul>
<li>
<p>About the python script:<br>
I followed the first steps of the OpenIGTLinkIF <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/OpenIGTLinkIF#Extended_Interface_for_External_Software_.28Ideas.29" rel="nofollow noopener">developer tutorial</a> (which is only for slicer as Client) and I am able to set Slicer as a server and to receive tracking data. But I couldn’t figure out how to access it. I think the <code>RegisterIncomingMRMLNode()</code> function from vtkMRMLIGTLConnectorNode.h is not formatted for Python yet (even the help function doe not recognize it).</p>
</li>
<li>
<p>About the OpenIGTLinkIF module:<br>
The small <a href="https://www.slicer.org/wiki/Modules:OpenIGTLinkIF#Step_3:_Connecting_the_Tracker_Client" rel="nofollow noopener">tutorial</a> on the OpenIGTLinkIF is about an old version of OpenIGTLinkIF and I caanot figure out the last steps. Again, I can set Slicer as Server, and receive tracking data (STATUS = ON), but I cannot access it and make the stylus (or whatever else) turn relating to the random matrices sent by TrackerClient.</p>
</li>
</ul>
<p>Again, thank you for your time,</p>

---

## Post #2 by @lassoan (2018-01-05 16:38 UTC)

<aside class="quote no-group" data-username="terajnol" data-post="1" data-topic="1766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/eb8c5e/48.png" class="avatar"> terajnol:</div>
<blockquote>
<p>Still working on the PlusToolkit for my Xsens IMU. Because it is not that easy for me</p>
</blockquote>
</aside>
<p>If you have any problems, just commit your code and post your question and the link to the relevant code part here.</p>
<aside class="quote no-group" data-username="terajnol" data-post="1" data-topic="1766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/eb8c5e/48.png" class="avatar"> terajnol:</div>
<blockquote>
<p>I couldn’t figure out how to access it</p>
</blockquote>
</aside>
<p>If you have the tracking data in Slicer then you just access it as a regular node. Slicer takes care of all communication, updating of the scene based on information that it collects on communications threads, etc. - in your Slicer scripts or modules you don’t need to deal with OpenIGTLink at all.</p>
<p>See this example how to observe transform changes and access the transformation matrix:</p>
<pre><code># Create a new transform
transformNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformNode", "MyTransform")

# Callback function that will be called each time the transform is modified
def onMyTransformModified(caller, event):
  transformMatrix = vtk.vtkMatrix4x4()
  caller.GetMatrixTransformToWorld(transformMatrix)
  print("Transform modified. Translation X = {0}".format(transformMatrix.GetElement(0,3)))

# Add an observer that will make the callback function called each time the transform is modified
observationTag = transformNode.AddObserver(slicer.vtkMRMLTransformableNode.TransformModifiedEvent, onMyTransformModified)
</code></pre>
<p>At this point, go to transforms module and move the Translation LR slider to change X translation. Changed translation value will be printed on the Python console.</p>
<p>If you don’t need the observe transform changes anymore, you can remove the observer:</p>
<pre><code>transformNode.RemoveObserver(observationTag)
</code></pre>

---

## Post #3 by @lassoan (2018-01-05 16:42 UTC)

<aside class="quote no-group" data-username="terajnol" data-post="1" data-topic="1766">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/eb8c5e/48.png" class="avatar"> terajnol:</div>
<blockquote>
<p>I cannot access it and make the stylus (or whatever else) turn relating to the random matrices sent by TrackerClient</p>
</blockquote>
</aside>
<p>Complete <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a> to learn this and many other very useful techniques.</p>

---

## Post #4 by @leochan2009 (2018-01-08 14:15 UTC)

<p><a class="mention" href="/u/terajnol">@terajnol</a>,<br>
I cannot access it and make the stylus (or whatever else) turn relating to the random matrices sent by TrackerClient</p>
<p>Please try using “TrackingDataServer” in OpenIGTLink library instead, i think igtl::TransformMessage type is not converted in OpenIGTLinkIF module.<br>
After you establish the connector with the TrackingDataServer. Input the following lines in the Slicer Python Interactor:<br>
a = slicer.mrmlScene.GetNodeByID(“vtkMRMLIGTLConnectorNode1”) // Checke the Node ID in Slicer<br>
b=slicer.vtkMRMLIGTLQueryNode()<br>
b.SetQueryType(b.TYPE_START)<br>
b.SetIGTLName(“TDATA”)<br>
a.PushQuery(b)</p>
<p>Then open “Transforms” module in Slicer. you will see the received tranformation</p>

---
