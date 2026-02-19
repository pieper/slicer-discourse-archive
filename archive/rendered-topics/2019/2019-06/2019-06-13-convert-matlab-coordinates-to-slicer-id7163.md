---
topic_id: 7163
title: "Convert Matlab Coordinates To Slicer"
date: 2019-06-13
url: https://discourse.slicer.org/t/7163
---

# Convert Matlab coordinates to Slicer

**Topic ID**: 7163
**Date**: 2019-06-13
**URL**: https://discourse.slicer.org/t/convert-matlab-coordinates-to-slicer/7163

---

## Post #1 by @siaeleni (2019-06-13 16:25 UTC)

<p>Hello,</p>
<p>I would like to convert Matlab coordinates to Slicer.<br>
I load Dicom images to Matlab and I get some coordinates.<br>
Then, I try to load them on Slicer, but both are in a completely different position.</p>
<p>Could you please give me a hint?</p>
<p>Thanks,<br>
Eleni</p>

---

## Post #2 by @pieper (2019-06-13 16:41 UTC)

<p>Hi Eleni -</p>
<p>I don’t use matlab, but I understand the <a href="https://www.slicer.org/wiki/Documentation/4.10/Extensions/MatlabBridge" rel="nofollow noopener">matlabbridge extension</a> is a big help.</p>
<p>Also, maybe at the heart of your question, is that DICOM uses LPS coordinates and Slicer uses RAS.  These are described <a href="https://www.slicer.org/wiki/Coordinate_systems" rel="nofollow noopener">on this wiki page</a>.</p>
<p>Best,<br>
Steve</p>

---

## Post #3 by @siaeleni (2019-06-17 14:21 UTC)

<p>Thanks for the clarifications. I am going to describe better what I am going to achieve. I load a set of images on Matlab and picking there 3 points (red cross). And I want to convert these into Slicer. I load the same set of images and I plot these 3 point (red dots). I am trying to register the points with the image on Slicer. I have tried the following solutions:</p>
<ol>
<li>Apply diag(-1. -1, 1,1) to the points</li>
<li>regarding the coordinates systems that I have I imagine that I should rotate 180 around z axis and 90 degrees around x axis.</li>
</ol>
<p>Unfortunately, none of these are working.</p>
<p>Thanks,<br>
Eleni</p>

---

## Post #4 by @lassoan (2019-06-17 14:29 UTC)

<p>I guess in Matlab you use voxel indices as coordinates (IJK). You can see in this example how to convert between IJK and LPS (or RAS) coordinates by multiplying with ijkToLpsTransform.</p>
<p>By the way, why do you need to define points in Matlab? You can define points in Slicer using markups. If you have some function implemented in Matlab that automatically detects those points then you can call that function directly from Slicer using MatlabBridge (which provides convenience functions to pass images and point positions between Matlab and Slicer in various coordinate systems). Check out MatlabBridge tutorial and examples for details.</p>
<p>At some point it could make sense to remove dependency on Matlab, which should be much easier in recent Slicer-4.11 releases, as you can use any Python packages in Slicer.</p>

---

## Post #6 by @siaeleni (2019-06-17 14:34 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Which example exactly are you referring to?</p>

---

## Post #7 by @siaeleni (2019-06-17 15:04 UTC)

<p>Seems that the coordinates are in mm in Matlab.</p>
<p>Unfortunately, I do not have any control over that and I cannot run it through MatlabBridge.<br>
There is a software that I am using and I don’t have the source code. The only thing that I can get are these points as I have plotted on Matlab.</p>

---

## Post #8 by @lassoan (2019-06-17 15:26 UTC)

<aside class="quote no-group" data-username="siaeleni" data-post="6" data-topic="7163">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/b4bc9f/48.png" class="avatar"> siaeleni:</div>
<blockquote>
<p>Which example exactly are you referring to?</p>
</blockquote>
</aside>
<p><a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/Examples/FillAroundSeeds/FillAroundSeeds.m">FillAroundSeeds</a> example shows how to convert between Matlab-style (1-based) IJK and LPS physical coordinate systems.</p>
<aside class="quote no-group" data-username="siaeleni" data-post="7" data-topic="7163">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/b4bc9f/48.png" class="avatar"> siaeleni:</div>
<blockquote>
<p>Seems that the coordinates are in mm in Matlab.</p>
</blockquote>
</aside>
<p>You use multiple coordinate systems in both Slicer and Matlab and you convert between them using homogeneous transformation matrices. To convert, you need to simply multiply the homogeneous coordinates vector by the appropriate homogeneous transformation matrix from the left.</p>
<p>In Slicer, we usually use RAS physical coordinate system and 0-based IJK voxel coordinate system. Most other software use LPS physical coordinate systems for images, so we save images using LPS as physical coordinate system, therefore you’ll get that in Matlab. Also, in Matlab array indexing is 1-based, so you need to add/subtract this 1 offset. This is all taken into consideration in <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdread.m#L6">nrrdread.m for computing ijkToLps transform</a>, so you can convert between your Matlab-style IJK and physical LPS by multiplying with this transform (or its inverse).</p>
<aside class="quote no-group" data-username="siaeleni" data-post="7" data-topic="7163">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/b4bc9f/48.png" class="avatar"> siaeleni:</div>
<blockquote>
<p>Unfortunately, I do not have any control over that and I cannot run it through MatlabBridge.</p>
</blockquote>
</aside>
<p>What prevents you from running the processing through MatlabBridge? (it should be possible to use MatlabBridge for running any Matlab function). Also, if you can tell us what this black-box Matlab code does then we might be able to recommend potential open-source alternatives.</p>

---

## Post #9 by @pieper (2019-06-18 19:24 UTC)

<p>As a follow up, Eleni and I worked through the data and found a transformation that appears to be correct.  For reference here’s the script that works for us, but it’s probably a one-off solution specific to the way this particular matlab program generates the data (x and y coordinates in pixel space, but z coordinate scaled by slice spacing).</p>
<pre><code class="lang-auto">fp = open('/Users/pieper/Dropbox/data/MRRobot/Accuracy Phantom/Matlab/x-coordinate.txt', "r")
data = fp.read()
xcoords = map(float, data.strip().replace('\r\n', '\t').split('\t'))
fp.close()

fp = open('/Users/pieper/Dropbox/data/MRRobot/Accuracy Phantom/Matlab/y-coordinate.txt', "r")
data = fp.read()
ycoords = map(float, data.strip().replace('\r\n', '\t').split('\t'))
fp.close()

volumeNode = slicer.util.getNode('901*')
ijkToRAS = vtk.vtkMatrix4x4()
volumeNode.GetIJKToRASMatrix(ijkToRAS)

markupNode = slicer.mrmlScene.AddNode(slicer.vtkMRMLMarkupsFiducialNode())

for index in range(64):
    out = [0,]*4
    ijkToRAS.MultiplyPoint([ xcoords[index], ycoords[index], 21 , 1], out)  # 21 =  52.5 zcoord / 2.5 slice spacing
    markupNode.AddFiducial(*out[:3])
</code></pre>

---
