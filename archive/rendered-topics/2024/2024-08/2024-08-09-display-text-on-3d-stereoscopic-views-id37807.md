---
topic_id: 37807
title: "Display Text On 3D Stereoscopic Views"
date: 2024-08-09
url: https://discourse.slicer.org/t/37807
---

# Display text on 3D stereoscopic views

**Topic ID**: 37807
**Date**: 2024-08-09
**URL**: https://discourse.slicer.org/t/display-text-on-3d-stereoscopic-views/37807

---

## Post #1 by @Laura_A (2024-08-09 21:27 UTC)

<p>How can I display text in pop-up 3D views?</p>
<p>Steps I follow:</p>
<ol>
<li>I create and show a right and left view with the following code:</li>
</ol>
<pre><code class="lang-auto">layoutName = "LeftEyeView"
layoutLabel = "Left Eye"
layoutColor = [1.0, 1.0, 0.0]

viewOwnerNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScriptedModuleNode")
                    
# Create MRML node
viewLogic = slicer.vtkMRMLViewLogic()
viewLogic.SetMRMLScene(slicer.mrmlScene)
            
# Left node
viewNodeLeft = viewLogic.AddViewNode(layoutName)
viewNodeLeft.SetLayoutLabel(layoutLabel)
viewNodeLeft.SetLayoutColor(layoutColor)
viewNodeLeft.SetAndObserveParentLayoutNodeID(viewOwnerNode.GetID())
viewNodeLeft.SetStereoType(3)# Quadbuffer Stereo layout 1 is left eye (dont know why)

# Create widget
self.viewWidgetLeft = slicer.qMRMLThreeDWidget()
self.viewWidgetLeft.setMRMLScene(slicer.mrmlScene)
self.viewWidgetLeft.setMRMLViewNode(viewNodeLeft)      
print("Left widget created")
self.viewWidgetLeft.show()       

</code></pre>
<ol start="2">
<li>I display some text on the 3D view from the Slicer UI</li>
</ol>
<pre><code class="lang-auto"># Get the 3D view renderer
self.layoutManager = slicer.app.layoutManager()
self.threeDView = self.layoutManager.threeDWidget(0).threeDView()
self.renderer = self.threeDView.renderWindow().GetRenderers().GetFirstRenderer()

# Create a text actor to display the text
self.textActor = vtk.vtkTextActor()
# Position the text actor in the corner
self.textActor.GetPositionCoordinate().SetCoordinateSystemToNormalizedViewport()
self.textActor.SetPosition(0.8, 0.9) 

# Add the text actor to the renderer
self.renderer.AddActor2D(self.textActor )
</code></pre>
<ol start="3">
<li>In order to add the text in the created left and right views, I need to access those views. Using “layoutManager.threeDWidget(<strong>–viewNumber–</strong>).threeDView()” does not let me display any text in those views.</li>
</ol>
<p>The view nodes I actually have are:<br>
View1 (from the UI): vtkMRMLViewNode1<br>
View (left eye): vtkMRMLViewNodeLeftEyeView<br>
View_1 (right eye): vtkMRMLViewNodeRightEyeView</p>
<p>How can I access the render windows of those views in order to be able to display text in those?</p>

---

## Post #2 by @lassoan (2024-08-10 13:18 UTC)

<p>The layout manager only manages the views in the layout. Since <em>you</em> create the other views and widgets you can directly use thise objects.</p>
<p>Note that you cannot use 2D actor to display anything in a stereo display, because inconsistent stereo parallax and occlusion (this most often causes double vision for the user). You can use 3D text actors instead.</p>

---

## Post #3 by @Laura_A (2024-08-12 14:22 UTC)

<p>Thanks a lot for the quick answer and explanation!</p>
<p>I created a 3D actor to display the text, but it doesn’t display it in the other views:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e1f1ddcd457bce22ee6a6aa5fa366c64b21c51f.png" data-download-href="/uploads/short-url/dqDy3EUa9qQKJFucfsKB4Y6vVwj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e1f1ddcd457bce22ee6a6aa5fa366c64b21c51f_2_690x400.png" alt="image" data-base62-sha1="dqDy3EUa9qQKJFucfsKB4Y6vVwj" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e1f1ddcd457bce22ee6a6aa5fa366c64b21c51f_2_690x400.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e1f1ddcd457bce22ee6a6aa5fa366c64b21c51f_2_1035x600.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e1f1ddcd457bce22ee6a6aa5fa366c64b21c51f_2_1380x800.png 2x" data-dominant-color="9C9DCF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1453×843 40.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>the code I used:<br>
renderer = slicer.app.layoutManager().threeDWidget(<strong>0</strong>).threeDView().renderWindow().GetRenderers().GetFirstRenderer()<br>
text_actor = vtk.vtkTextActor3D()<br>
renderer.AddActor(text_actor)</p>
<p>Also, when using threeDWidget(1) or (2), there was nothing displayed in the right and left views.</p>
<p>Therefore, as you suggested, I tried to use the views I create directly instead of retrieving them from the layout manager. However, I can only get the camera and the views, and there is no method for adding (3D) actors that way. Neither with the “viewOwnerNode” that I create.</p>
<p>Is there any other way to access the render windows of the nodes I create?</p>

---

## Post #4 by @lassoan (2024-08-12 23:04 UTC)

<aside class="quote no-group" data-username="Laura_A" data-post="3" data-topic="37807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/laura_a/48/77560_2.png" class="avatar"> Laura_A:</div>
<blockquote>
<p>I created a 3D actor to display the text, but it doesn’t display it in the other views:</p>
</blockquote>
</aside>
<p>You directly access the renderer by using low-level calls. If you add an actor in a view, it will be only added in that view. If you want to add an object that is displayed in all views automatically then you can create a polydata from text using <a href="https://vtk.org/doc/nightly/html/classvtkTextSource.html">vtkTextSource</a> and display it using a model node.</p>
<aside class="quote no-group" data-username="Laura_A" data-post="3" data-topic="37807">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/laura_a/48/77560_2.png" class="avatar"> Laura_A:</div>
<blockquote>
<p>when using threeDWidget(1) or (2), there was nothing displayed in the right and left views.</p>
</blockquote>
</aside>
<p>The layout manager only manages the views in the layout. The views that are outside the view layout are inaccessible for the layout manager, but it is not a problem at all, because <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-3d-view-outside-the-view-layout"><em>you</em> create all these other views and widgets</a> and so you can directly use these objects. For example, you can get the renderer from the view widget you created:</p>
<pre data-code-wrap="python"><code class="lang-python">renderer = viewWidget.threeDView().renderWindow().GetRenderers().GetFirstRenderer()
</code></pre>

---
