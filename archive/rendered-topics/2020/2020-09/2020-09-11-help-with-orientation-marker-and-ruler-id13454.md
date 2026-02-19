---
topic_id: 13454
title: "Help With Orientation Marker And Ruler"
date: 2020-09-11
url: https://discourse.slicer.org/t/13454
---

# Help with orientation marker and ruler

**Topic ID**: 13454
**Date**: 2020-09-11
**URL**: https://discourse.slicer.org/t/help-with-orientation-marker-and-ruler/13454

---

## Post #1 by @rohan_n (2020-09-11 23:53 UTC)

<p>Hello,<br>
I need help with the following.</p>
<ol>
<li>
<p>Is there a line of Python code that I can add to my scripted module to make the Axes Orientation Marker show up on the red and yellow slices automatically, without navigating to the “Show Orientation Marker” menu for the red &amp; yellow slices?</p>
</li>
<li>
<p>What tools can I use to measure objects in an image other than this one? Something that allows the user to get more precise measurement of things like tumor diameter would be great.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce8cbd9e5d10227a30ffcc6e3fb955b98ca036ec.png" data-download-href="/uploads/short-url/ttdTskrshZ4N98ICmMY4C7YvaGM.png?dl=1" title="ruler_ex" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ce8cbd9e5d10227a30ffcc6e3fb955b98ca036ec_2_690x388.png" alt="ruler_ex" data-base62-sha1="ttdTskrshZ4N98ICmMY4C7YvaGM" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ce8cbd9e5d10227a30ffcc6e3fb955b98ca036ec_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ce8cbd9e5d10227a30ffcc6e3fb955b98ca036ec_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ce8cbd9e5d10227a30ffcc6e3fb955b98ca036ec_2_1380x776.png 2x" data-dominant-color="B9B9B9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ruler_ex</span><span class="informations">2560×1440 215 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Please note that I want the user to be able to use the ruler while still having my scripted module selected. I don’t want the user switching back and forth between a “Measurement” module and my module in order to make a tumor diameter measurement. Is there any ruler option other than the one shown in my screenshot that is not a separate module?<br>
Thanks,<br>
Rohan Nadkarni</p>
</li>
</ol>

---

## Post #2 by @lassoan (2020-09-12 01:54 UTC)

<aside class="quote no-group" data-username="rohan_n" data-post="1" data-topic="13454">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rohan_n/48/78474_2.png" class="avatar"> rohan_n:</div>
<blockquote>
<p>Is there a line of Python code that I can add to my scripted module to make the Axes Orientation Marker show up on the red and yellow slices automatically, without navigating to the “Show Orientation Marker” menu for the red &amp; yellow slices?</p>
</blockquote>
</aside>
<p>Orientation markers can be configured by adjusting properties of the corresponding view node. For example:</p>
<pre data-code-wrap="python"><code class="lang-python">viewNode = getNode('vtkMRMLSliceNodeRed')
viewNode.SetOrientationMarkerType(viewNode.OrientationMarkerTypeHuman)
</code></pre>
<aside class="quote no-group" data-username="rohan_n" data-post="1" data-topic="13454">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rohan_n/48/78474_2.png" class="avatar"> rohan_n:</div>
<blockquote>
<p>What tools can I use to measure objects in an image other than this one? Something that allows the user to get more precise measurement of things like tumor diameter would be great.</p>
</blockquote>
</aside>
<p>For manual diameter measurements, you can use markup line.</p>
<p>For automated measurements, you can segment the tumor using one of the semi-automatic or fully automatic methods in Segment Editor, then use Segment Statistics to compute its parameters (volume, largest diameter, smallest diameter, sphericity, surface area, mean/min/max intensity etc.).</p>
<aside class="quote no-group" data-username="rohan_n" data-post="1" data-topic="13454">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rohan_n/48/78474_2.png" class="avatar"> rohan_n:</div>
<blockquote>
<p>Please note that I want the user to be able to use the ruler while still having my scripted module selected. I don’t want the user switching back and forth between a “Measurement” module and my module in order to make a tumor diameter measurement. Is there any ruler option other than the one shown in my screenshot that is not a separate module?</p>
</blockquote>
</aside>
<p>I would recommend to add a <code>qSlicerSimpleMarkupsWidget</code> to your module GUI. It allows you to create a new markups (the type(s) you specify), rename, delete, start/stop placement, edit control points, show/hide, jump to points, etc.</p>
<p>You can see results in your module by adding a <code>qMRMLSubjectHierarchyTreeView</code> to your module widget.</p>
<p>To view/edit/copy/save quantification results, you can also add a <code>qMRMLTableView</code>. It can display the content of a table node. Table node is stored as a .csv file.</p>

---

## Post #3 by @rohan_n (2020-09-14 18:44 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="13454">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would recommend to add a <code>qSlicerSimpleMarkupsWidget</code> to your module GUI. It allows you to create a new markups (the type(s) you specify), rename, delete, start/stop placement, edit control points, show/hide, jump to points, etc.</p>
<p>You can see results in your module by adding a <code>qMRMLSubjectHierarchyTreeView</code> to your module widget.</p>
<p>To view/edit/copy/save quantification results, you can also add a <code>qMRMLTableView</code> . It can display the content of a table node. Table node is stored as a .csv file.</p>
</blockquote>
</aside>
<p>Thanks. I got the orientation marker part. Is there a good Slicer python code example for me to look at for the Markups Widget and Hierarchy Tree View?</p>

---

## Post #4 by @rohan_n (2020-10-22 16:58 UTC)

<p>Hello again,<br>
I spoke to the people who will be the end users of my Slicer module and they really do want something more precise than the built-in ruler tool I referred to in the first post in this thread.<br>
If you have any links to share that could help me figure out the syntax for adding a ruler tool to my module (using qSlicerSimpleMarkupsWidget?) that would be greatly appreciated.</p>

---

## Post #5 by @lassoan (2020-10-23 02:59 UTC)

<p>The new markups line tool is as accurate as it gets, with manual point placement. You can zoom in the image as much as you need and you can also set shape, size, opacity, thickness of markups control point marker and line to maximize visibility:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/645f17c7cfba26ca6f56ebe30ba77e801c407371.jpeg" data-download-href="/uploads/short-url/ejVtVdHLmqY94GclnFnf22Z9ik9.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/645f17c7cfba26ca6f56ebe30ba77e801c407371_2_690x419.jpeg" alt="image" data-base62-sha1="ejVtVdHLmqY94GclnFnf22Z9ik9" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/645f17c7cfba26ca6f56ebe30ba77e801c407371_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/645f17c7cfba26ca6f56ebe30ba77e801c407371_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/645f17c7cfba26ca6f56ebe30ba77e801c407371_2_1380x838.jpeg 2x" data-dominant-color="494A50"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1372 558 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You can refine the position of a markup point in 3D by clicking on it (which it jumps to that slice in all views) and then adjust the position any any of the views.</p>

---

## Post #6 by @rohan_n (2020-10-23 16:15 UTC)

<p>Great. Is there an easy way to add this feature to my own scripted module, or would I have to switch to the markups module?</p>

---

## Post #7 by @lassoan (2020-10-23 16:17 UTC)

<p>Of course, you can do this in your own module. All these properties are defined in the markups node’s display node. You can also set parameters that you like and click “Save to defaults” button in Markups module / Display section, to use those values as default for new markups.</p>

---

## Post #8 by @rohan_n (2020-11-03 18:14 UTC)

<p>Would you be able to share any example code for how to add and use a markups line tool as part of a scripted module?<br>
Preferably something that’s compatible with Slicer 4.11.0, but I’m open to hearing about newer features too.</p>

---

## Post #9 by @lassoan (2020-11-03 20:39 UTC)

<p>You can find many examples in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>. If you have trouble finding an example for a specific task then let us know.</p>

---

## Post #10 by @rohan_n (2020-11-04 21:48 UTC)

<p>Thanks for the link.<br>
I added the code from this link</p><aside class="onebox githubgist" data-onebox-src="https://gist.github.com/lassoan/bf0954d93cacc8cbe27cd4a3ad503f2f">
  <header class="source">

      <a href="https://gist.github.com/lassoan/bf0954d93cacc8cbe27cd4a3ad503f2f" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/lassoan/bf0954d93cacc8cbe27cd4a3ad503f2f" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/lassoan/bf0954d93cacc8cbe27cd4a3ad503f2f</a></h4>

  <h5>MarkupsInfo.py</h5>
  <pre><code class="Python">from __main__ import qt, slicer

#
# MarkupsInfo module
#

class MarkupsInfo:
  def __init__(self, parent):
    import string
    parent.title = "Markups info"</code></pre>
    This file has been truncated. <a href="https://gist.github.com/lassoan/bf0954d93cacc8cbe27cd4a3ad503f2f" target="_blank" rel="noopener nofollow ugc">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
directly to my module.</p>
<p>However, no matter where I place the two fiducials, I always get a distance of 0 between them, as you can see here.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88c429c2507efb386cb09708bbe886e61004d12f.jpeg" data-download-href="/uploads/short-url/jvTdeObRowSWdxkdXe62BwYzIYf.jpeg?dl=1" title="screenshot_2020114.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/88c429c2507efb386cb09708bbe886e61004d12f_2_690x380.jpeg" alt="screenshot_2020114.PNG" data-base62-sha1="jvTdeObRowSWdxkdXe62BwYzIYf" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/88c429c2507efb386cb09708bbe886e61004d12f_2_690x380.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/88c429c2507efb386cb09708bbe886e61004d12f_2_1035x570.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/88c429c2507efb386cb09708bbe886e61004d12f_2_1380x760.jpeg 2x" data-dominant-color="939292"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot_2020114.PNG</span><span class="informations">1722×950 258 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there something wrong with how I’m placing the fiducials?<br>
Alternatively, how can I make minor changes to this code so that I’m calculating the length of a line chosen from the “Create and Place” instead of distance between 2 fiducials?</p>
<p>Thanks,<br>
Rohan Nadkarni</p>

---

## Post #11 by @lassoan (2020-11-04 22:01 UTC)

<p>The module was developed for an earlier version of Slicer and markups have been greatly improved since then and the API has change, too.</p>
<p>You can now use Markups ruler and curves to measure distances, so this custom module should not be necessary anymore.</p>

---

## Post #12 by @rohan_n (2020-11-04 22:17 UTC)

<p>Is there a script repository example using the markups ruler?</p>
<p>Sorry to have so many follow-up questions about this.</p>

---

## Post #13 by @lassoan (2020-11-04 22:19 UTC)

<p>You can get length of markups line and curve like this:</p>
<pre><code class="lang-python">print(getNode('L').GetLineLengthWorld())
print(getNode('C').GetCurveLengthWorld())
</code></pre>

---

## Post #14 by @rohan_n (2020-11-05 00:31 UTC)

<p>Sounds good, thanks.<br>
But does this command have some compatibility issue with Slicer 4.11.0?<br>
I’m getting:</p>
<pre><code>print(getNode('L').GetLineLengthWorld())

AttributeError: 'vtkSlicerMarkupsModuleMRMLPython.vtkMRMLMarkupsLin' object has no attribute 'GetLineLengthWorld'</code></pre>

---

## Post #15 by @lassoan (2020-11-05 00:49 UTC)

<p>Use the most recent stable (Slicer-4.11.20200930).</p>

---

## Post #16 by @rohan_n (2020-11-05 17:38 UTC)

<p>Unfortunately, it’s not working in the most recent stable either.<br>
The curve length command works fine but the line length one doesn’t.</p>
<p>Is there any sort of work-around where I could save the line’s description to a string and get the length from there?</p>

---

## Post #17 by @lassoan (2020-11-05 17:44 UTC)

<aside class="quote no-group" data-username="rohan_n" data-post="16" data-topic="13454">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rohan_n/48/78474_2.png" class="avatar"> rohan_n:</div>
<blockquote>
<p>Unfortunately, it’s not working in the most recent stable either.</p>
</blockquote>
</aside>
<p>I can confirm that does work with the latest stable (Slicer-4.11.20200930). Copy-paste this code into the Python console and let me know what you see (you should see a line showing up in the viewers and “50.0” printed on the console.</p>
<pre data-code-wrap="python"><code class="lang-python">lineNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsLineNode")
lineNode.AddControlPointWorld(vtk.vtkVector3d(0,0,0))
lineNode.AddControlPointWorld(vtk.vtkVector3d(30,40,0))
print(lineNode.GetLineLengthWorld())
</code></pre>

---

## Post #18 by @rohan_n (2020-11-05 18:03 UTC)

<p>You’re right, I mistakenly opened the earlier version of Slicer without realizing it.<br>
It works in the latest stable release for me too.</p>
<p>Thank you so much for all your help with this task.</p>

---

## Post #19 by @spycolyf (2021-04-16 18:26 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Could you direct me to Python scripting that will allow user interactive measurement by moving and adjusting the line length?</p>
<p>Thanks</p>

---

## Post #20 by @spycolyf (2021-04-16 18:41 UTC)

<p><span class="mention">@lasson</span></p>
<p>Wait! That example does do exactly that. And it’s very nice!!! So, all I need now is to be able to manually draw a line on a any of the 3 orthogonal planes and have them reflected in the 3D graphics. How do I enable the user to draw the line?</p>

---

## Post #21 by @mau_igna_06 (2021-04-16 19:01 UTC)

<p>I don’t know if this is exactly what you need but here is code I used to make the user draw a line:</p>
<pre><code class="lang-auto">lineNode = slicer.mrmlScene.CreateNodeByClass("vtkMRMLMarkupsLineNode")
lineNode.SetName("temp")
slicer.mrmlScene.AddNode(lineNode)
slicer.modules.markups.logic().AddNewDisplayNodeForMarkupsNode(lineNode)
lineNode.SetName(slicer.mrmlScene.GetUniqueNameByString("line"))

#setup placement
slicer.modules.markups.logic().SetActiveListID(lineNode)
interactionNode = slicer.mrmlScene.GetNodeByID("vtkMRMLInteractionNodeSingleton")
interactionNode.SwitchToSinglePlaceMode()
</code></pre>

---

## Post #22 by @spycolyf (2021-04-16 20:00 UTC)

<p>Hey <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>, I owe you big time! This is perfect! Wow! Made my day!</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji only-emoji" alt=":slight_smile:"></p>

---

## Post #23 by @spycolyf (2021-04-21 16:48 UTC)

<p>How does one delete the lines using Python?</p>

---

## Post #24 by @mikebind (2021-04-21 17:09 UTC)

<p><code>slicer.mrmlScene.RemoveNode(lineNode)</code> to remove</p>

---

## Post #25 by @spycolyf (2021-04-21 19:38 UTC)

<p>Is there a Slicer Python Scripting reference manual that I can use so that I can stop bugging you guys about every little command? Thanks! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #26 by @smrolfe (2021-04-21 19:55 UTC)

<p>The Python <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="noopener nofollow ugc">script repository</a> is a good place to start.</p>

---
