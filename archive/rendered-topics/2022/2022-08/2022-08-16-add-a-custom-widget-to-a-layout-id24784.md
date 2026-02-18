# Add a custom widget to a layout

**Topic ID**: 24784
**Date**: 2022-08-16
**URL**: https://discourse.slicer.org/t/add-a-custom-widget-to-a-layout/24784

---

## Post #1 by @mau_igna_06 (2022-08-16 13:26 UTC)

<p>I tried this code to make a custom layout (with a custom widget) for a scripted module and it doesn’t work:</p>
<pre><code class="lang-auto">    #get custom layout widgets
    containingListWidget = slicer.util.loadUI(self.resourcePath('UI/containingListWidget.ui'))
    self.containingListUI = slicer.util.childWidgetVariables(containingListWidget)
    slicer.mrmlScene.AddDefaultNode(containingListWidget)

    # Set scene in MRML widgets. Make sure that in Qt designer the top-level qMRMLWidget's
    # "mrmlSceneChanged(vtkMRMLScene*)" signal in is connected to each MRML widget's.
    # "setMRMLScene(vtkMRMLScene*)" slot.
    containingListWidget.setMRMLScene(slicer.mrmlScene)

    customLayout = """
    &lt;layout type="vertical"&gt;
      &lt;item&gt;
      &lt;widget class="listFrame"&gt;
      &lt;/widget&gt;
      &lt;/item&gt;
      &lt;item&gt;
    &lt;/layout&gt;
    """
</code></pre>
<p>It brings up this error:</p>
<pre><code class="lang-auto">slicer.mrmlScene.AddDefaultNode(availableVersionsWidget)
TypeError: AddDefaultNode argument 1: method requires a VTK object
</code></pre>
<p>Could you help?</p>

---

## Post #2 by @Sunderlandkyl (2022-08-16 15:05 UTC)

<p>The error is because loadUI creates a QWiget, not a vtkMRMLNode.</p>
<p>Custom widgets can be added to view layouts using qSlicerSingletonViewFactory:</p>
<pre><code class="lang-python">containingListWidget = slicer.util.loadUI(self.resourcePath('UI/containingListWidget.ui'))
self.containingListUI = slicer.util.childWidgetVariables(containingListWidget)
containingListWidget.setMRMLScene(slicer.mrmlScene)

viewFactory = slicer.qSlicerSingletonViewFactory()
viewFactory.setTagName("listWidget")
viewFactory.setWidget(containingListWidget)
slicer.app.layoutManager().registerViewFactory(viewFactory)

layout = """
&lt;layout type=\"horizontal\"&gt;
  &lt;item&gt;
    &lt;listWidget&gt;&lt;/listWidget&gt;
  &lt;/item&gt;
&lt;/layout&gt;"""
layoutId = 1234

layoutNode = slicer.app.layoutManager().layoutLogic().GetLayoutNode()
layoutNode.AddLayoutDescription(
  layoutId, layout)

slicer.app.layoutManager().setLayout(layoutId)
</code></pre>

---

## Post #3 by @mau_igna_06 (2022-08-16 15:07 UTC)

<p>-Thank youas gdfdgfddfhffd</p>

---
