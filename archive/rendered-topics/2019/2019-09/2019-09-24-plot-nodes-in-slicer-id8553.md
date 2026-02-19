---
topic_id: 8553
title: "Plot Nodes In Slicer"
date: 2019-09-24
url: https://discourse.slicer.org/t/8553
---

# Plot Nodes in Slicer

**Topic ID**: 8553
**Date**: 2019-09-24
**URL**: https://discourse.slicer.org/t/plot-nodes-in-slicer/8553

---

## Post #1 by @wieke.prummel (2019-09-24 21:06 UTC)

<p>Hi everyone,</p>
<p>I am working on a module to generate a 2D Visualization of the Brain Connectome Network.</p>
<p>I am trying to understand all the 2D plot options in Slicer with Python. So my question is the following:<br>
What are all the node classes that can be added in slicer.mrmlScene.AddNewNodeByClass( ? ) ?</p>
<p>Also, if I would like to plot a vtkSpiderPlot() in an existing window of Slicer, would that be possible? Until now I’ve only managed to plot it in a pop up window that uses the OpenGL Visualization ToolKit.</p>
<p>Thank you all in advance!</p>

---

## Post #2 by @lassoan (2019-09-25 17:51 UTC)

<p>Currently line, scatter, and bar plots are available via the GUI. To show spider plots, you would need to do some Python scripting. I would recommend to show this plot first in a plain VTK render window. Once you have that working, then I can help with making that window show up in the view layout.</p>

---

## Post #3 by @wieke.prummel (2019-09-26 20:17 UTC)

<p>Thank you for your reply Andras.</p>
<p>I am pretty new to VTK and Slicer.</p>
<p>I have generated the spider plot in a plain VTK render window, which is the pop up window I was talking about before. To do so I used vtkRenderer(), vtkRenderWindow(), vtkRenderWindowInteractor().</p>
<p>So as I would like to make that window show up in Slicer you suggest me to use the view layout.<br>
Should I look at the slicer.app.layoutManager() ? If so, could you help me understand how that should be implemented and what vtkMRML Node to use?</p>

---

## Post #4 by @lassoan (2019-09-27 22:30 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> could you advise how the view class that you recently added to Slicer could be used for this? Thank you.</p>

---

## Post #5 by @Sunderlandkyl (2019-09-28 00:13 UTC)

<p>You can add your vtkRenderWindow to a QVTKWidget, and then add that widget to a layout using <a href="https://apidocs.slicer.org/master/classqSlicerSingletonViewFactory.html" rel="nofollow noopener">qSlicerSingletonViewFactory</a>.</p>
<p>Ex.</p>
<ul>
<li>
<p>Add view factory to layout manager:</p>
<pre><code>  singletonViewFactory = slicer.qSlicerSingletonViewFactory()
  singletonViewFactory.setTag("yourtagname")
  singletonViewFactory.setWidget(yourWidget)
  slicer.app.layoutManager().registerViewFactory(singletonViewFactory)
</code></pre>
</li>
<li>
<p>Add custom layout to layout manager:</p>
<pre><code>  yourLayoutID = 1234
  layoutManager = slicer.app.layoutManager()
  layout = (
    "&lt;layout type=\"horizontal\"&gt;"
    " &lt;item&gt;"
    "  &lt;yourtagname&gt;&lt;/yourtagname&gt;"
    " &lt;/item&gt;"
    "&lt;/layout&gt;"
  )
  layoutNode = slicer.app.layoutManager().layoutLogic().GetLayoutNode()
  layoutNode.AddLayoutDescription(
    yourLayoutID, layout)
</code></pre>
</li>
<li>
<p>Switch to layout with custom widget:</p>
<pre><code>slicer.app.layoutManager().setLayout(yourLayoutID)</code></pre>
</li>
</ul>

---

## Post #6 by @wieke.prummel (2019-10-01 14:52 UTC)

<p>Hi <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>,</p>
<p>Thank you for your response.</p>
<p>I think I am close. I just can’t access QVTKWidget or QVTKRenderWindowInteractor.<br>
I am using 3D Slicer version 4.10.1-2019-01-16.  with qt5.<br>
Do you know how I can access those ?<br>
I tried calling defining it like this :</p>
<blockquote>
<p>qWidget = vtk.QVTKWidget()</p>
</blockquote>
<p>But I get:</p>
<blockquote>
<p>AttributeError: ‘module’ object has no attribute ‘QVTKWidget’</p>
</blockquote>

---

## Post #7 by @Sunderlandkyl (2019-10-01 19:56 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Do you know of an alternative to QVTKWidget that is wrapped in python?</p>
<p>Alternatively, is there a better way to embed a vtkRenderWindow() in a QWidget?</p>

---

## Post #8 by @lassoan (2019-10-01 21:10 UTC)

<p><a href="https://github.com/commontk/CTK/blob/master/Libs/Visualization/VTK/Widgets/ctkVTKOpenGLNativeWidget.h" rel="nofollow noopener">ctkVTKOpenGLNativeWidget</a> can be used for this.</p>

---

## Post #9 by @joinvar (2023-07-17 01:35 UTC)

<p>hi, lassoan,  When I use ctkVTKOpenGLNativeWidget in python, I encounter a problem. Show “AttributeError: ctkVTKOpenGLNativeWidget has no<br>
attribute named ‘setRenderWindow’”. Here is a screenshot below.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35319bb9bfe08eae6486c8c51be445095b47fde6.png" alt="(U4$A74Z}7LN~NF45~E1M" data-base62-sha1="7AzAEHmpNwQUXr2tEc15plF5DjE" width="684" height="254"><br>
But i noticed that it has been used like this in the ctk source code.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/480627d73d1053299fefe2bdc60d15c86da965e8.png" data-download-href="/uploads/short-url/ah9z6DVSQkHuGinfgFXIy8Ed4WQ.png?dl=1" title="{G{VTHYAFHTIELDH3XWWIPW" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/480627d73d1053299fefe2bdc60d15c86da965e8.png" alt="{G{VTHYAFHTIELDH3XWWIPW" data-base62-sha1="ah9z6DVSQkHuGinfgFXIy8Ed4WQ" width="690" height="348" data-dominant-color="262728"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{G{VTHYAFHTIELDH3XWWIPW</span><span class="informations">879×444 16.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
And, when I was reviewing the source code in ctk,<br>
i found that ctkVTKOpenGLNativeWidget  may inherit from three classes, and all of the parent classes has a public function setRenderWindow or SetRenderWindow .<br>
So, I wonder to know if it is not obtainable in python .I am not familiar with python’s wrapper. Thanks a lot.</p>

---

## Post #10 by @joinvar (2023-07-21 01:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> In addition, i used slicer version is 5.2.2. I can get ctkVTKOpenGLNativeWidget’s setRenderWindow function in a c++ loadable module.</p>

---

## Post #11 by @lassoan (2023-07-21 04:13 UTC)

<p>The generic Python-wrapped Qt widget for VTK rendering is <code>ctk.ctkVTKRenderView()</code>. A complete example:</p>
<pre><code class="lang-python">widget = ctk.ctkVTKRenderView()
renderer = widget.renderWindow().GetRenderers().GetFirstRenderer()

cylinder = vtk.vtkCylinderSource()
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cylinder.GetOutputPort())
actor = vtk.vtkActor()
actor.SetMapper(mapper)
renderer.AddActor(actor)

renderer.ResetCamera()
widget.show()
</code></pre>

---

## Post #12 by @joinvar (2023-07-21 05:53 UTC)

<p>Thank you, I’ll try it.</p>

---
