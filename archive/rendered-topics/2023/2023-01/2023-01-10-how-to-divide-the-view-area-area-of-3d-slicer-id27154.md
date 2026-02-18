# How to divide the view area area of 3d slicer

**Topic ID**: 27154
**Date**: 2023-01-10
**URL**: https://discourse.slicer.org/t/how-to-divide-the-view-area-area-of-3d-slicer/27154

---

## Post #1 by @dsa934 (2023-01-10 06:49 UTC)

<p>Operating system: windows 11<br>
Slicer version: slicer 4.13.0</p>
<p>I am developing a python extension version of a function that takes a depth map for markups points.<br>
I want to print this depthmap image in a small size in the view area of the 3D slicer,<br>
but what can I do about related actions?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52b9cf25fd4a90fe3502cb1d128cd65035d26aa0.png" data-download-href="/uploads/short-url/bNPfj3XPHjoNsytwHkDFpDsUJJC.png?dl=1" title="question" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52b9cf25fd4a90fe3502cb1d128cd65035d26aa0.png" alt="question" data-base62-sha1="bNPfj3XPHjoNsytwHkDFpDsUJJC" width="690" height="438" data-dominant-color="F6F6F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">question</span><span class="informations">797×506 2.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
&lt; feature explain &gt;</p>
<p>I want to make it like the shape above, but is there any way?</p>

---

## Post #2 by @RafaelPalomar (2023-01-11 08:32 UTC)

<p>Hello,</p>
<p>for the Slicer-Liver extension we have been playing lately with the same idea (an overlay that shows 2D information on top of the 3D viewer). I don’t think you can achieve this in Python, though. Our approach has been to create our own MRML nodes and MRMLDisplayableManagers (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/mrml_overview.html#the-displayable-manager" class="inline-onebox" rel="noopener nofollow ugc">MRML Overview — 3D Slicer documentation</a>) for the 3D view in C++.</p>
<p>Alternatively, you can generate the depth maps as volumes and display them in one of the 2D slice views. In this line, shortly there will be available the multi-monitor support (you can follow the progress at <a href="https://github.com/Slicer/Slicer/pull/6776" class="inline-onebox" rel="noopener nofollow ugc">Multi monitor layout by lassoan · Pull Request #6776 · Slicer/Slicer · GitHub</a>), which allows to spawn additional visualization windows (i.e, a single floating 2D window, which is separated from the main Slicer window) and probably can get you closer to what you want in Python.</p>
<p>One more approach that I have seen implemented (don’t remember where, though) is adding a Slice view widget  to the side panel, together with the rest of the module’s widgets. In this way you can have a single 3D view in the visualization area and the depth maps together with the module’s widgets. This should be doable in Python.</p>
<p>I hope this helps.</p>

---

## Post #3 by @dsa934 (2023-01-11 14:12 UTC)

<p>Hum… It seems difficult.</p>
<p>I’ll try my best</p>

---

## Post #4 by @cpinter (2023-01-11 14:56 UTC)

<p>Yes it is. Basically Slicer does not allow non-rectangular division of the layout. You can divide the layout vertically or horizontally, but this is it. Also, Qt does not support layers, so you cannot show widgets on top of widgets in a controlled way (if you add a widget with a parent but don’t add it to the layout it will show up in the corner but it may have unwanted consequences, it is not safe). What you can do is tweak the 3D rendering as <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> suggests with MRMLDMs and such, or you can add any widget in the module panel.</p>

---

## Post #5 by @dsa934 (2023-01-12 04:33 UTC)

<p>No matter how much I think about it, this seems too complicated, so I thought of another way.<br>
I know that 3D slicer has 4 views.( one for model , the others for DICOM data )</p>
<p>_view_node = slicer.mrmlScene.GetSingletonNode(“1”, “vtkMRMLViewNode”)<br>
_camera_node = slicer.modules.cameras.logic().GetViewActiveCameraNode(_view_node)</p>
<p>Through the code above, draw a depthmap from ‘Tag: 1, view node’ and save it as a dicom image.<br>
And if I make the saved Dicom image output from ‘Tag 2: viewnode’, will there be a problem?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/188c14fe94a249e6e2f61a41e4e98394bb221498.png" data-download-href="/uploads/short-url/3v9Abp7v8AKjJLyxftMwj3VgRdK.png?dl=1" title="questoin" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/188c14fe94a249e6e2f61a41e4e98394bb221498_2_690x374.png" alt="questoin" data-base62-sha1="3v9Abp7v8AKjJLyxftMwj3VgRdK" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/188c14fe94a249e6e2f61a41e4e98394bb221498_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/188c14fe94a249e6e2f61a41e4e98394bb221498.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/188c14fe94a249e6e2f61a41e4e98394bb221498.png 2x" data-dominant-color="32333E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">questoin</span><span class="informations">1017×552 10.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ul>
<li>I know the depthmap image isn’t  a dicom file.<br>
but  I’m doing this to ‘consider ease of use from a UX point of view’<br>
in order to immediately check the results of the depth map I drew.</li>
</ul>
<p>Asking to add wizet above seems to be an action similar to what I am trying to do, but I think this method will be a little easier.</p>
<p>If there is a better way, please let me know.</p>

---

## Post #6 by @RafaelPalomar (2023-01-12 10:59 UTC)

<p>Thinking in DICOM terms is useful when you are going to load/save data to disk. If you are thinking in getting a sort of interactive depth map visualization while you are modifying Markups, it is more useful to think in terms of <code>vtkMRML</code> nodes, which is what the Slicer application uses internally when it runs.</p>
<p>At a high level, the 3D slicer model is not based on direct manipulation of the views, but the manipulation of <code>vtkMRML</code> nodes and managers that dictate how these nodes are translated into visualizations in the different views. In C++, you have the possibility to create new <code>vtkMRMLDisplayableManager</code> classes that can define how certain nodes will be displayed; in Python, unfortunately you don’t have that option.</p>
<p>My first approach to this problem (in Python) would be to create a <code>vtkMRMLScalarVolumeNode</code> and configure it so it has a single slice where I can put my data. By modifying the data that the node is holding, you will get an updated visualization. Later you can also save this data in various formats.</p>
<p>There are a good set of examples on how to deal with volume nodes in 3D Slicer using Python in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#volumes" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a> in the volumes section.</p>
<p>I hope this can set you in a useful direction.</p>

---

## Post #7 by @cpinter (2023-01-12 11:57 UTC)

<p>This is a hack, but you can also potentially show any widget in a layout view. For example in a layout that has a table view, you can replace it with your widget like this:</p>
<pre><code class="lang-auto">tableWidget = layoutManager.tableWidget(tableViewIndex)
tableWidget.visible = True
tableWidget.tableController().visible = False
tableWidget.tableView().visible = False
# Add new widget, make sure it is visible
tableWidget.layout().addWidget(myWidget)
myWidget.visible = True
</code></pre>

---

## Post #8 by @lassoan (2023-01-12 18:41 UTC)

<p>Actually, this feature is already available. You can show any model as a corner annotation. It even keeps the orientation of the model aligned with the current view orientation. The feature is originally added for displaying orientation markers, but it can be used for displaying complex, dynamically changing content.</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b12b9d8a733ec7f16cb1c9b6e88697f468c1ccd4.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b12b9d8a733ec7f16cb1c9b6e88697f468c1ccd4.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b12b9d8a733ec7f16cb1c9b6e88697f468c1ccd4.mp4</a>
    </source></video>
  </div><p></p>
<p>All you need to do is to set the model as orientation marker in all 3D views:</p>
<pre><code class="lang-python">orientationMarkerNode = getNode('MyDepthMap')
orientationMarkerNode.GetDisplayNode().SetVisibility(False) # hide from the viewers, just use it as an orientation marker

viewNodes = slicer.util.getNodesByClass("vtkMRMLAbstractViewNode")
for viewNode in viewNodes:
  viewNode.SetOrientationMarkerHumanModelNodeID(orientationMarkerNode.GetID())
  viewNode.SetOrientationMarkerType(slicer.vtkMRMLAbstractViewNode.OrientationMarkerTypeHuman)
  viewNode.SetOrientationMarkerSize(slicer.vtkMRMLAbstractViewNode.OrientationMarkerSizeMedium)
</code></pre>

---

## Post #9 by @dsa934 (2023-01-13 02:09 UTC)

<p>I tried to summarize what you said, please check if it is correct.<br>
The depthmap I created has the form of an array.<br>
So, my procedure is as follows.</p>
<ol>
<li>
<p>Convert array to MRML node</p>
</li>
<li>
<p>Set the viewnode to render depthmap turned into MRML nodes</p>
</li>
<li>
<p>MRMLnode-depthmap rendering to the corresponding view.</p>
</li>
</ol>
<p>In the 3D slicer, many classes come together to form one meta data, and it seems that I can handle it as I want if I extract only the desired properties from the meta data, but It’s frustrating because I feel like I’m not good at it.</p>
<p>I’ll proceed step by step with the opinions of everyone who commented.<br>
Thanks for everyone’s help.</p>

---

## Post #10 by @pieper (2023-01-13 15:05 UTC)

<p>Yes, that sounds like the basic steps.  There is a lot to learn in order to implement custom functionality and it may take some time to feel comfortable but the advantage of Slicer is that all the code is available for inspection and you can learn from lots of examples.</p>

---

## Post #11 by @lassoan (2023-01-13 20:30 UTC)

<p>You can also expect that commonly needed operations are already implemented in Slicer.</p>
<p>For example, acquiring image from a depth camera, such as Intel RealSense and live display of the pint cloud is already available as free, open-source software.</p>
<p>Plus toolkit (<a href="http://www.plustoolkit.org">www.plustoolkit.org</a>) acquires the data and sends it to Slicer via OpenIGTLink, and SlicerOpenIGTLink extension receives the data, and <a href="https://github.com/PerkLab/DepthImageToPointCloud">DepthImageToPointCloud</a> extension can display the point cloud. The point cloud is already a model node, so you can choose to display it as an orientation marker.</p>

---
