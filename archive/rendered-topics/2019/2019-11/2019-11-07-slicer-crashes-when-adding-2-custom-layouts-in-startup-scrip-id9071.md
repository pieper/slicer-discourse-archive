# Slicer crashes when adding 2 custom layouts in startup script

**Topic ID**: 9071
**Date**: 2019-11-07
**URL**: https://discourse.slicer.org/t/slicer-crashes-when-adding-2-custom-layouts-in-startup-script/9071

---

## Post #1 by @Prashant_Pandey (2019-11-07 20:17 UTC)

<p>I want to configure and enable two additional custom layouts that are available in all my Slicer instances. I’m doing this by adding the attached script to my .slicerrc file.<br>
However when I start Slicer and select one of the custom views from the layout menu, Slicer crashes.</p>
<p>This only seems to be a problem with <strong>two</strong> or more custom views. If I only configure and add one layout, there are no issues.</p>
<p>I know it’s not good practice to have object and object2 but that’s me trying to debug why this issue is happening</p>
<pre><code># Python commands in this file are executed on Slicer startup

# Examples:
#
# Load a scene file
# slicer.util.loadScene('c:/Users/SomeUser/Documents/SlicerScenes/SomeScene.mrb')
#
# Open a module (overrides default startup module in application settings / modules)
# slicer.util.mainWindow().moduleSelector().selectModule('SegmentEditor')
#

# Set up 3-slice view for 2D viz.
customLayout = """
&lt;layout type="horizontal" split="true"&gt;
	&lt;item&gt;
		&lt;view class="vtkMRMLSliceNode" singletontag="Red"&gt;
			&lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
			&lt;property name="viewlabel" action="default"&gt;R&lt;/property&gt;
			&lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;
		&lt;/view&gt;
	&lt;/item&gt;
	&lt;item&gt;
		&lt;view class="vtkMRMLSliceNode" singletontag="Yellow"&gt;
			&lt;property name="orientation" action="default"&gt;Sagittal&lt;/property&gt;
			&lt;property name="viewlabel" action="default"&gt;Y&lt;/property&gt;
			&lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;
		&lt;/view&gt;
	&lt;/item&gt;
	&lt;item&gt;
		&lt;view class="vtkMRMLSliceNode" singletontag="Green"&gt;
			&lt;property name="orientation" action="default"&gt;Coronal&lt;/property&gt;
			&lt;property name="viewlabel" action="default"&gt;G&lt;/property&gt;
			&lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;
		&lt;/view&gt;
	&lt;/item&gt;
&lt;/layout&gt;
"""
# Built-in layout IDs are all below 100, so you can choose any large random number
# for your custom layout ID.
twoDLayoutID=100

layoutManager = slicer.app.layoutManager()
layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(twoDLayoutID, customLayout)                                         

## Switch to the new custom layout 
layoutManager.setLayout(twoDLayoutID)

## Add button to layout selector toolbar for this custom layout
viewToolBar = mainWindow().findChild('QToolBar', 'ViewToolBar')
layoutMenu = viewToolBar.widgetForAction(viewToolBar.actions()[0]).menu()
layoutSwitchActionParent = layoutMenu  # use `layoutMenu` to add inside layout list, use `viewToolBar` to add next the standard layout list
layoutSwitchAction = layoutSwitchActionParent.addAction("All three 2D Views") # add inside layout list
layoutSwitchAction.setIcon(qt.QIcon(':Icons/Go.png'))
layoutSwitchAction.setToolTip('All three 2D Views')
layoutSwitchAction.connect('triggered()', lambda layoutId = twoDLayoutID: slicer.app.layoutManager().setLayout(layoutId))

# Set up volume renderings for 3D viz.
customLayout2 = """
&lt;layout type="horizontal" split="true"&gt;
	&lt;item&gt;
		&lt;view class="vtkMRMLViewNode" singletontag="1"&gt;
			&lt;property name="viewlabel" action="default"&gt;1&lt;/property&gt;
		&lt;/view&gt;
	&lt;/item&gt;
	&lt;item&gt;
		&lt;view class="vtkMRMLSliceNode" singletontag="Yellow"&gt;
			&lt;property name="orientation" action="default"&gt;Sagittal&lt;/property&gt;
			&lt;property name="viewlabel" action="default"&gt;Y&lt;/property&gt;
			&lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;
		&lt;/view&gt;
	&lt;/item&gt;
	&lt;item&gt;
		&lt;view class="vtkMRMLViewNode" singletontag="2"&gt;
			&lt;property name="viewlabel" action="default"&gt;2&lt;/property&gt;
		&lt;/view&gt;
	&lt;/item&gt;
&lt;/layout&gt;
"""
# Built-in layout IDs are all below 100, so you can choose any large random number
# for your custom layout ID.
threeDlayoutID=200

layoutManager2 = slicer.app.layoutManager()
layoutManager2.layoutLogic().GetLayoutNode().AddLayoutDescription(threeDlayoutID, customLayout2)                                         

## Switch to the new custom layout 
layoutManager2.setLayout(threeDlayoutID)

# Add button to layout selector toolbar for this custom layout
viewToolBar2 = mainWindow().findChild('QToolBar', 'ViewToolBar')
layoutMenu2 = viewToolBar2.widgetForAction(viewToolBar2.actions()[0]).menu()
layoutSwitchActionParent2 = layoutMenu2  # use `layoutMenu2` to add inside layout list, use `viewToolBar2` to add next the standard layout list
layoutSwitchAction2 = layoutSwitchActionParent2.addAction("Custom 3D and Slice") # add inside layout list
layoutSwitchAction2.setIcon(qt.QIcon(':Icons/Go.png'))
layoutSwitchAction2.setToolTip('Double 3D and slice view')
layoutSwitchAction2.connect('triggered()', lambda layoutId = threeDlayoutID: slicer.app.layoutManager().setLayout(layoutId))</code></pre>

---

## Post #2 by @lassoan (2019-11-07 20:57 UTC)

<p>You need to set the layout ID as custom data in the layout switch action. Add these two lines:</p>
<pre><code>layoutSwitchAction.setData(twoDLayoutID)
layoutSwitchAction2.setData(threeDlayoutID)</code></pre>

---

## Post #3 by @Prashant_Pandey (2019-11-07 21:04 UTC)

<p>Thanks, works perfectly now!</p>

---

## Post #4 by @Prashant_Pandey (2019-11-08 23:50 UTC)

<p>How would I access the variables <code>layoutManager, twoDLayoutID</code>, and others defined in .slicerrc in a scripted module? I’ve tried using global or globals() in my scripted module file but I can’t seem to access them.</p>

---

## Post #5 by @lassoan (2019-11-09 00:53 UTC)

<p>Thr easiest is to put all “global” variables in an easily accessible namespace, such as slicer: <code>slicer.myVar=555</code></p>

---
