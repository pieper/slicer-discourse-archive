# Changing the background of 3D view at startup

**Topic ID**: 7798
**Date**: 2019-07-29
**URL**: https://discourse.slicer.org/t/changing-the-background-of-3d-view-at-startup/7798

---

## Post #1 by @rprueckl (2019-07-29 18:40 UTC)

<p>Hi,</p>
<p>i have a class derived from qSlicerMainWindow (according to <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="nofollow noopener">https://github.com/KitwareMedical/SlicerCustomAppTemplate</a>).</p>
<p>In the method setupUi, after the line this-&gt;Superclass::setupUi(mainWindow); I am setting a custom layout. This works so far. The custom layout contains a new 3d view, which is generated correctly.<br>
After that, the scene contains three 3d views, which I find odd, I would have thought that the scene would only contain two of them after the change to my layout. One is called ‘View’, one is called ‘View1’, and one is called ‘View’.</p>
<p>When I then (still in setupUi) do the following:</p>
<pre><code class="lang-auto">  vtkMRMLViewLogic* ViewLogic = layoutManager-&gt;threeDWidget("My3dView")-&gt;viewLogic();
  vtkMRMLViewNode* ViewNode = layoutManager-&gt;threeDWidget("My3dView")-&gt;mrmlViewNode();
  ViewLogic-&gt;StartViewNodeInteraction(vtkMRMLViewNode::BackgroundColorFlag);
  int wasModifying = ViewNode-&gt;StartModify();
  ViewNode-&gt;SetBackgroundColor(0.0f, 0.0f, 0.0f);
  ViewNode-&gt;SetBackgroundColor2(0.0f, 0.0f, 0.0f);
  ViewNode-&gt;EndModify(wasModifying);
  ViewLogic-&gt;EndViewNodeInteraction();
</code></pre>
<p>the background color is unchanged when the main window appears.</p>
<p>Is there something wrong with my code or do I have to change the background color of the 3d views at a different place (i.e. somewhere later in program execution)?</p>
<p>Any advice would be appreciated.<br>
Robert</p>

---

## Post #2 by @lassoan (2019-07-30 02:54 UTC)

<p>Default view properties are read from application settings, written to default view and slice nodes in the scene, and then views are updated from the default nodes.</p>
<p>Here is an example of how <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_default_slice_view_orientation" rel="nofollow noopener">default nodes are set for slice views</a>.</p>
<p>I would recommend to attach a debugger and step through the view initialization process to get familiar how it works.</p>

---

## Post #3 by @rprueckl (2019-07-30 09:55 UTC)

<p>Thank you for the hint Andras, that helped me solve it.</p>
<p>I found out the following sequence of vtkMRMLViewNode creations:</p>
<ol>
<li>Creation of qSlicerApplication - RegisterNodeClass (vtkMRMLScene constructor)</li>
<li>qSlicerMainWindow initialization - layout manager creates new node - no default node yet present, thus <code>node-&gt;Reset(defaultNode);</code> is not called</li>
<li>Initialization of the window object derived from qSlicerMainWindow - I set a new layout here - the layout manager creates a new node - no default node yet present, thus <code>node-&gt;Reset(defaultNode);</code> is not called</li>
<li>In <code>vtkMRMLLayoutLogic::CreateMissingViews</code> the node is set to the scene, which leads to <code>vtkMRMLViewLogic::UpdateViewNode()</code> that tries to get the view node of the scene which fits to its name, however does not find one. So it creates a new vtkMRMLViewNode for itself and also adds this node to the scene. The name is auto-generated: “View”.</li>
<li>A new scene for vtkSlicerunitsLogic is created ( RegisterNodeClass (vtkMRMLScene constructor) )</li>
<li>postInitializeApplication: default 3d view node is created while loading the module ‘ViewControllers’ and set to the scene. Only the settings <code>BoxVisibility, AxisLabelsVisibility, UseOrthographicProjection, UseDepthPeeling, OrientationMarkerType, OrientationMarkerSize, RulerType</code> are read from QSettings and set to the default node. Maybe it would be worth to read also other settings from the QSettings. All present views are then reset to the default node.</li>
</ol>
<p>What I did to solve my problem was to make the following connection in my main window:</p>
<pre><code class="lang-auto">Q_Q(MyMainWindow);
QObject::connect(q, SIGNAL(initialWindowShown()), q, SLOT(startupCompleted()));
</code></pre>
<p>with</p>
<pre><code class="lang-auto">void MyMainWindow::startupCompleted()
{
    qSlicerApplication * app = qSlicerApplication::application();
    std::vector&lt;vtkMRMLNode*&gt; nodes;
    app-&gt;mrmlScene()-&gt;GetNodesByClass("vtkMRMLViewNode", nodes);
    nodes.push_back(app-&gt;mrmlScene()-&gt;GetDefaultNodeByClass("vtkMRMLViewNode"));
    
    for (auto&amp;&amp; node : nodes)
    {
        vtkMRMLViewNode* viewNode = vtkMRMLViewNode::SafeDownCast(node);
        int wasModifying = viewNode-&gt;StartModify();
        viewNode-&gt;SetBackgroundColor(0.0f, 0.0f, 0.0f);
        viewNode-&gt;SetBackgroundColor2(0.0f, 0.0f, 0.0f);
        viewNode-&gt;SetBoxVisible(false);
        viewNode-&gt;SetAxisLabelsVisible(false);
        viewNode-&gt;EndModify(wasModifying);
    }
}
</code></pre>
<p>This works now, the settings are correctly taken over. However, I suspect a malfunction here in the Slicer code. The standard vtkMRMLViewNode that is created at Slicer startup is called View1, so this is clearly step 2 in the list above. The third (step 3) is created by my layout change request. The fourth creation, however, is suspicious to me. Maybe there is a mixup between Name, SingletonTag, and LayoutLabel? Here the fields of the nodes for comparison:</p>
<p><strong>NodeFromStep3</strong><br>
Name: Viewcx3dView (probably generated based on the SingletonTag)<br>
SingletonTag: cx3dView (correct according to my layout definition)<br>
LayoutLabel: 3D view (correct according to my layout definition)</p>
<p><strong>NodeFromStep4</strong><br>
Name: View (autogenerated)<br>
SingletonTag: 3D view (from my LayoutLabel?)<br>
LayoutLabel: 1 (autogenerated?)</p>
<p>Moreover, when I do the following:</p>
<pre><code class="lang-auto">vtkMRMLViewLogic* ViewLogic = layoutManager-&gt;threeDWidget("Viewcx3dView")-&gt;viewLogic();
vtkMRMLViewNode* ViewNode1 = layoutManager-&gt;threeDWidget("Viewcx3dView")-&gt;mrmlViewNode();
vtkMRMLViewNode* ViewNode2 = ViewLogic-&gt;GetViewNode();
</code></pre>
<p>then <code>ViewNode1</code> is <strong>NodeFromStep3</strong> and <code>ViewNode2</code> is <strong>NodeFromStep4</strong>. Is this how it should be?</p>
<p>Best,<br>
Robert</p>

---

## Post #4 by @lassoan (2019-07-30 13:39 UTC)

<aside class="quote no-group" data-username="rprueckl" data-post="3" data-topic="7798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>What I did to solve my problem was to make the following connection in my main window</p>
</blockquote>
</aside>
<p>As soon as the scene is created, you can define default view nodes with modified properties (see and follow <a href="https://github.com/Slicer/Slicer/blob/1cff95e84339e70649841f34479cc6daded7700b/Modules/Loadable/ViewControllers/Logic/vtkSlicerViewControllersLogic.cxx#L86-L102">this pattern</a>). So, you should be able to do just before you register and set your custom layout, no need to add a callback function for this.</p>
<aside class="quote no-group" data-username="rprueckl" data-post="3" data-topic="7798">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rprueckl/48/4240_2.png" class="avatar"> rprueckl:</div>
<blockquote>
<p>then <code>ViewNode1</code> is <strong>NodeFromStep3</strong> and <code>ViewNode2</code> is <strong>NodeFromStep4</strong> . Is this how it should be?</p>
</blockquote>
</aside>
<p>I agree that this is somewhat complicated but it probably works correctly. <a href="https://apidocs.slicer.org/master/classqMRMLLayoutManager.html#a810df79c97d1772d995de70b9e4b442d"><code>threeDWidget(QString)</code></a> is a convenience method that returns widget by name. If you have multiple view nodes by the same name then you will get the first view with matching name. To get view nodes that are used in the current layout, you can iterate through all view nodes in the scene and only use those that are <a href="https://apidocs.slicer.org/master/classvtkMRMLAbstractViewNode.html#a9f5f661e2310e58753e4a63c4891e02e">mapped in current layout</a>.</p>

---

## Post #5 by @rprueckl (2019-07-30 19:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="7798" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>As soon as the scene is created, you can define default view nodes with modified properties (see and follow <a href="https://github.com/Slicer/Slicer/blob/1cff95e84339e70649841f34479cc6daded7700b/Modules/Loadable/ViewControllers/Logic/vtkSlicerViewControllersLogic.cxx#L86-L102" rel="noopener nofollow ugc">this pattern</a>).</p>
</blockquote>
</aside>
<p>This kind of works. It sets the background black, but for the Box and AxisLabels the result is as follows:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc7c462cb2faafb1277b081024a4f579f6d68f88.png" alt="Unbenannt" data-base62-sha1="qTq1gRV4ov4fGcou9JIyQKY1vcI" width="462" height="306"><br>
Not sure why this happens.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="7798" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you have multiple view nodes by the same name then you will get the first view with matching name.</p>
</blockquote>
</aside>
<p>Well, this is not the case. I looked at the following parts of the code:<br>
<a href="https://github.com/Slicer/Slicer/blob/69d0f7d9b71ece1d987f9ed665015687cbbe154c/Libs/MRML/Widgets/qMRMLLayoutManager.cxx#L133" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/69d0f7d9b71ece1d987f9ed665015687cbbe154c/Libs/MRML/Widgets/qMRMLLayoutManager.cxx#L133</a><br>
and<br>
<a href="https://github.com/Slicer/Slicer/blob/69d0f7d9b71ece1d987f9ed665015687cbbe154c/Libs/MRML/Widgets/qMRMLLayoutManager.cxx#L378" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/69d0f7d9b71ece1d987f9ed665015687cbbe154c/Libs/MRML/Widgets/qMRMLLayoutManager.cxx#L378</a></p>
<p>and encountered that for the <code>threeDView</code> the <code>LayoutLabel</code> is taken as the name of the logic (it is set in the method <code>setViewLabel</code>) whereas for the slice view, there is a separate method (<code>setSliceViewName</code> in line 376) which sets the <code>LayoutName</code> to the logic. In both cases, however, the logic tries to find the respective node by its name:<br>
<a href="https://github.com/Slicer/Slicer/blob/69d0f7d9b71ece1d987f9ed665015687cbbe154c/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L326" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/69d0f7d9b71ece1d987f9ed665015687cbbe154c/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L326</a><br>
and<br>
<a href="https://github.com/Slicer/Slicer/blob/69d0f7d9b71ece1d987f9ed665015687cbbe154c/Libs/MRML/Logic/vtkMRMLViewLogic.cxx#L351" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/69d0f7d9b71ece1d987f9ed665015687cbbe154c/Libs/MRML/Logic/vtkMRMLViewLogic.cxx#L351</a></p>
<p>So, as an experiment, I implemented also for the <code>qMRMLThreeDWidget</code> a separate method <code>setViewName</code>, which is used by the <code>qMRMLLayoutThreeDViewFactory</code> to set the name of the logic according to the <code>LayoutName</code> and removed setting the logic name from <code>setViewLabel</code>. Now, the previously created additional view node (and also an additional camera node that was created) is not created anymore. This is how I would have expected it to be. Of course I am not sure if I miss side effects here or if there was some reason for the different implementations.</p>

---

## Post #6 by @lassoan (2019-07-30 22:14 UTC)

<p>Thank you for digging into this!</p>
<p>You are right, it is indeed incorrect in qMRMLThreeDViewControllerWidget that view logic name is set based on layout <em>label</em> instead of layout <em>name</em>. Probably it did not come up as an error before because in built-in view layouts, layout name and label are always the same for 3D views. I’ve fixed the issue and I’ll push a fix today if no complications come up during testing.</p>

---
