# Layout Manager cannot get the right qMRMLSliceWidget

**Topic ID**: 36460
**Date**: 2024-05-29
**URL**: https://discourse.slicer.org/t/layout-manager-cannot-get-the-right-qmrmlslicewidget/36460

---

## Post #1 by @nnzzll (2024-05-29 10:37 UTC)

<p>I create a qMRMLSliceWidget by using this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-slice-view-outside-the-view-layout" rel="noopener nofollow ugc">scipt</a>.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; # layout name is used to create and identify the underlying slice node and  should be set to a value that is not used in any of the layouts owned by the layout manager
&gt;&gt;&gt; layoutName = "TestSlice1"
&gt;&gt;&gt; layoutLabel = "TS1"
&gt;&gt;&gt; layoutColor = [1.0, 1.0, 0.0]
&gt;&gt;&gt; # ownerNode manages this view instead of the layout manager (it can be any node in the scene)
&gt;&gt;&gt; viewOwnerNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScriptedModuleNode")
&gt;&gt;&gt; 
&gt;&gt;&gt; # Create MRML nodes
&gt;&gt;&gt; viewLogic = slicer.vtkMRMLSliceLogic()
&gt;&gt;&gt; viewLogic.SetMRMLScene(slicer.mrmlScene)
&gt;&gt;&gt; viewNode = viewLogic.AddSliceNode(layoutName)
&gt;&gt;&gt; viewNode.SetLayoutLabel(layoutLabel)
&gt;&gt;&gt; viewNode.SetLayoutColor(layoutColor)
&gt;&gt;&gt; viewNode.SetAndObserveParentLayoutNodeID(viewOwnerNode.GetID())
True
&gt;&gt;&gt; 
&gt;&gt;&gt; # Create widget
&gt;&gt;&gt; viewWidget = slicer.qMRMLSliceWidget()
&gt;&gt;&gt; viewWidget.setMRMLScene(slicer.mrmlScene)
&gt;&gt;&gt; viewWidget.setMRMLSliceNode(viewNode)
&gt;&gt;&gt; sliceLogics = slicer.app.applicationLogic().GetSliceLogics()
&gt;&gt;&gt; viewWidget.setSliceLogics(sliceLogics)
&gt;&gt;&gt; sliceLogics.AddItem(viewWidget.sliceLogic())
</code></pre>
<p>Then I use the layoutManager to get the slice widget I have just created, but layoutManager give me a wrong object:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; print(viewWidget)
qMRMLSliceWidget(0x560a750d2900, name="qMRMLSliceWidget") 
&gt;&gt;&gt; print(layoutManager.sliceWidget("TestSlice1"))
qMRMLSliceWidget(0x560a742ca520, name="qMRMLSliceWidgetTestSlice1") 
</code></pre>
<p>How does this happen?</p>

---

## Post #2 by @lassoan (2024-05-29 13:45 UTC)

<p>The layout manager has no way of knowing that you created some view widgets.</p>
<p>Also note that since you have explicitly set that the layout manager is not the owner of the view node (by calling <code>SetAndObserveParentLayoutNodeID</code>), the layout manager should ignore this view node completely. The layout manager only knows about the view node because you have set the parent layout node too late (after it was already added to the scene).</p>

---

## Post #3 by @nnzzll (2024-05-30 02:42 UTC)

<p>My final purpose is to use SegmentEditor on my own widget, if layout manager has no way of knowing newly created widgets, then I should use the default slice widget(“Red”,“Green”,etc) right?</p>
<p>I tried the code below but it didn’t work</p>
<pre><code class="lang-auto">&gt;&gt;&gt; layoutManager = slicer.app.layoutManager()
&gt;&gt;&gt; layoutNode = layoutManager.layoutLogic().GetLayoutNode()
&gt;&gt;&gt; myWidget = qt.QWidget()
&gt;&gt;&gt; viewFactory = slicer.qSlicerSingletonViewFactory()
&gt;&gt;&gt; viewFactory.setTagName("MyWidget")
&gt;&gt;&gt; viewFactory.setWidget(myWidget)
&gt;&gt;&gt; layoutManager.registerViewFactory(viewFactory)
&gt;&gt;&gt; viewLayout = """&lt;layout type="vertical"&gt;&lt;item&gt;&lt;MyWidget&gt;&lt;/MyWidget&gt;&lt;/item&gt;&lt;/layout&gt;"""
&gt;&gt;&gt; layoutNode.AddLayoutDescription(501, viewLayout)
True
&gt;&gt;&gt; layoutManager.setLayout(501)
&gt;&gt;&gt; gridLayout = qt.QGridLayout()
&gt;&gt;&gt; sliceWidget = layoutManager.sliceWidget("Red")
&gt;&gt;&gt; gridLayout.addWidget(sliceWidget)
&gt;&gt;&gt; myWidget.setLayout(gridLayout)
&gt;&gt;&gt; print(myWidget)
QWidget(0x56546c7cf570) 
&gt;&gt;&gt; print(sliceWidget.parent())
QWidget(0x56546c7cf570) 
&gt;&gt;&gt; print(sliceWidget.isVisible())
False
&gt;&gt;&gt; 
</code></pre>
<p>Now the slice widget Red is child widget of <code>myWidget</code>, but it is unvisible. Is there anything wrong with this code?</p>

---

## Post #4 by @lassoan (2024-05-30 03:29 UTC)

<p>The segment editor widget queries the list of views from the layout manager, so if you want to edit segments then you have to let the layout manager create the view and widget for you. If want to have an additional view outside the main viewport then you can specify multiple viewports (see examples in the script repository).</p>

---
