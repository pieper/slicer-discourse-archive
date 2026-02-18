# Controlling brush diameter increment when using Shift+Scroll

**Topic ID**: 4247
**Date**: 2018-10-01
**URL**: https://discourse.slicer.org/t/controlling-brush-diameter-increment-when-using-shift-scroll/4247

---

## Post #1 by @matthew (2018-10-01 16:31 UTC)

<p>When using paint tool in segment editor, the brush diameter can be controlled by holding shift key and scrolling (in addition to using the arrow keys on the UI). I would like the jump in diameter when scrolling to be much smaller than the default. Could this feature be implemented by using a python script that listened for scroll event and overrides the default behavior? Or maybe there is a more direct way?</p>
<p>I am using the paint tool to segment abdominal aorta on many slices. Using the arrows on the interface to adjust diameter takes too much time and having this feature would greatly speed up my workflow.</p>
<p>Thanks for your help!</p>

---

## Post #2 by @lassoan (2018-10-01 17:12 UTC)

<p>Shift+mouse wheel is for gross adjustment of the brush size. For fine adjustments, zoom in/out the image (by default, brush size is defined in screen size, so brush size relative to the image depends on image zoom factor).</p>

---

## Post #3 by @lassoan (2018-10-01 17:28 UTC)

<aside class="quote no-group" data-username="matthew" data-post="1" data-topic="4247">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matthew/48/2238_2.png" class="avatar"> matthew:</div>
<blockquote>
<p>I am using the paint tool to segment abdominal aorta on many slices</p>
</blockquote>
</aside>
<p>There are several semi-automatic tools, which should be able to segment the aorta within a minute (depending on image quality). For example, try these options:</p>
<ul>
<li>Fast marching effect: available after you install SegmentEditorExtraEffects extension; you just need to paint a few seed regions inside the aorta, and choose how large region you want to grow</li>
<li>Grow from seeds effect: you need to paint inside with one segment and paint outside non-vessel background with another segment</li>
<li>If you prefer full more manual segmentation, then you can use paint tool (with non-sphere brush) on every 5th-10th slice and create a full 3D segmentation from these isolated slices using Fill between slices effect.</li>
</ul>

---

## Post #4 by @matthew (2018-10-01 18:55 UTC)

<p>Thanks for your reply! That is very helpful. I think I will use one of those automated methods you listed. However, I would like to also implement an override to the default resizing of brush size. The idea is to have two keys that when pressed will increase/decrease the brush diameter by a pixel size I specify. To do so, I need the ability to programatically change the diameter. Using other posts on this forum, I figured out how to change BrushSphere parameter with below:</p>
<blockquote>
<p>segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()<br>
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)<br>
segmentEditorNode = slicer.mrmlScene.GetSingletonNode(“SegmentEditor”, “vtkMRMLSegmentEditorNode”)<br>
slicer.mrmlScene.AddNode(segmentEditorNode)<br>
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)<br>
segmentEditorWidget.setActiveEffectByName(“Paint”)<br>
effect = segmentEditorWidget.activeEffect()<br>
effect.setParameter(“BrushSphere”,“1”)</p>
</blockquote>
<p>However, I have been unable to find the parameter name for brush diameter. Do you know what this is and is there documentation somewhere with a list of parameter names?</p>
<p>Also, is it possible to listen for keyboard press events using a python script within 3D-slicer? How would I go about doing this?</p>
<p>Thanks!</p>

---

## Post #5 by @matthew (2018-10-01 19:09 UTC)

<p>Actually, just found your comment on <a href="https://discourse.slicer.org/t/create-a-mesh-in-python-script/1543/5">this post</a>. And have figured out how to handle keyboard press events. An example that decreases brush diameter when “M” is pressed is shown below:</p>
<pre>
import qt
import slicer

PARAM_DIAM = "BrushAbsoluteDiameter"

def decreaseDiameter():
	segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
	segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
	segmentEditorNode = slicer.mrmlScene.GetSingletonNode("SegmentEditor", "vtkMRMLSegmentEditorNode")
	slicer.mrmlScene.AddNode(segmentEditorNode)
	segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)

	segmentEditorWidget.setActiveEffectByName("Paint")
	effect = segmentEditorWidget.activeEffect()

	currentDiam = float(effect.parameter(PARAM_DIAM))
	newDiam = currentDiam - 0.5
	print("decreasing to new diam of %0.2f" % newDiam)
	effect.setParameter(PARAM_DIAM, newDiam)
	effect.forceRender

shortcutDecrease = qt.QShortcut(slicer.util.mainWindow())
shortcutDecrease.setKey(qt.QKeySequence("M"))
shortcutDecrease.connect("activated()", decreaseDiameter)
</pre>
<p>However, I am having a problem where the brush diameter does not refresh until I move the mouse. Is there a way to force this to repaint?</p>

---

## Post #6 by @lassoan (2018-10-01 23:50 UTC)

<p>Nice, you’ve almost done it! The brush size is not updating because <code>effect.forceRender</code> without <code>()</code> does not call anything, just returns the address of the method and rendering does not force update of the brush model anyway. Replace <code>effect.forceRender</code> by this:</p>
<pre><code># get current slice node
crosshairNode=slicer.mrmlScene.GetSingletonNode('default','vtkMRMLCrosshairNode')
pos_unused = [0,0,0]
sliceNode = crosshairNode.GetCursorPositionXYZ(pos_unused)
if sliceNode:
    # force updating displayed brush size
    sliceNode.Modified()
</code></pre>
<p>Still, I would recommend to zoom in the image if you want to segment smaller details: it not just zooms in/out the image but also decreases/increases absolute brush size, and it is done very smoothly (no “jumps” in zoom factor) if you use right-click+mouse move up/down for zooming.</p>
<p>We introduced brush size defined in screen size exactly for this purpose: we realized that every time we decreased brush size we always had to zoom in as well. So, if you use brush size relative to screen size option (default) then you just need to set an approximate brush size once (dictated by how accurately you can move your mouse pointer) and you do the fine brush sizing by zooming the image in/out.</p>

---

## Post #7 by @matthew (2018-10-02 18:07 UTC)

<p>The smooth zooming is a very nice feature. For more customization, I am going to try and complete this python feature to give more control. Below is my updated code. Buttons “D” and “F” decrease and increase the diameter, and buttons “E” and “R” decrease/increase the increment by which the diameter is changed. One additional problem I had to deal with is that when there were multiple segments and a segment other than the first one was selected, after running my code the selection would change back to the first segment. I fixed this by getting the selected-segment-id from the segment-editor-node and then setting the ID later in the segment-editor widget.</p>
<pre>
import qt
import slicer
from functools import partial
from qt import QCursor
from time import sleep

PARAM_DIAM = "BrushAbsoluteDiameter"
increment = 0.5

def repaint():
	crosshairNode=slicer.mrmlScene.GetSingletonNode('default','vtkMRMLCrosshairNode')
	pos_unused = [0,0,0]
	sliceNode = crosshairNode.GetCursorPositionXYZ(pos_unused)
	if sliceNode:
	    # force updating displayed brush size
	    sliceNode.Modified()

def changeDiameter(direction):
	segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()

	segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
	segmentEditorNode = slicer.mrmlScene.GetSingletonNode("SegmentEditor", "vtkMRMLSegmentEditorNode")
	slicer.mrmlScene.AddNode(segmentEditorNode)

	# Once node passed to widget the selected segment will get set back to first
	selectedSegmentID = segmentEditorNode.GetSelectedSegmentID()
	
	segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)

	# Set selected segment back to what it was before
	segmentEditorWidget.setCurrentSegmentID(selectedSegmentID)
	
	segmentEditorWidget.setActiveEffectByName("Paint")
	effect = segmentEditorWidget.activeEffect()

	currentDiam = float(effect.parameter(PARAM_DIAM))
	newDiam = currentDiam + (increment*direction)

	if newDiam &lt;= 0:
		return

	print("decreasing to new diam of %0.2f" % newDiam)
	effect.setParameter(PARAM_DIAM, newDiam)
	repaint()

def changeIncrement(direction):
	global increment
	newIncrement = increment + (0.1*direction)
	if newIncrement &lt;= 0:
		return
	increment = newIncrement
	print("Increment: %0.2f" % increment)
	repaint()

shortcutDecrease = qt.QShortcut(slicer.util.mainWindow())
shortcutDecrease.setKey(qt.QKeySequence("D"))
shortcutDecrease.connect("activated()", partial(changeDiameter, -1))

shortcutIncrease = qt.QShortcut(slicer.util.mainWindow())
shortcutIncrease.setKey(qt.QKeySequence("F"))
shortcutIncrease.connect("activated()", partial(changeDiameter, 1))

shortcutDecreaseFactor = qt.QShortcut(slicer.util.mainWindow())
shortcutDecreaseFactor.setKey(qt.QKeySequence("E"))
shortcutDecreaseFactor.connect("activated()", partial(changeIncrement, -1))

shortcutIncreaseFactor = qt.QShortcut(slicer.util.mainWindow())
shortcutIncreaseFactor.setKey(qt.QKeySequence("R"))
shortcutIncreaseFactor.connect("activated()", partial(changeIncrement, 1))
</pre>
<p>While the code serves its functional purpose, the last remaining bug is that after running this code you can no longer use the UI of the segment editor widget to change the diameter. The diameter is held to whatever is programatically set and neither using Shift+Scroll nor the UI can change it. I figure there must be some way to release the effect back to the default but not sure how to do this. If you have the time would appreciate how I can eliminate this last bug.</p>
<p>Thanks for your continued help!</p>

---

## Post #8 by @lassoan (2018-10-02 18:15 UTC)

<p>One big issue (that might cause the not updating brush size) is that you call <code>slicer.qMRMLSegmentEditorWidget()</code> each time you change the brush size, which creates a completely new segment editor widget!! (you never show this widget, so you don’t see it, but probably after a while you would notice slowdowns)</p>
<p>If you want to interact with the existing segment editor widget then you can get it using:</p>
<pre><code>segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor</code></pre>

---

## Post #9 by @matthew (2018-10-02 18:47 UTC)

<p>Ah, I see. Updated changeDiameter method to following:</p>
<pre>
def changeDiameter(direction):
	segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor

	segmentEditorWidget.setActiveEffectByName("Paint")
	effect = segmentEditorWidget.activeEffect()

	currentDiam = float(effect.parameter(PARAM_DIAM))
	newDiam = currentDiam + (increment*direction)

	if newDiam &lt;= 0:
		return

	print("decreasing to new diam of %0.2f" % newDiam)
	effect.setParameter("BrushDiameterIsRelative","0")
	effect.setParameter(PARAM_DIAM, newDiam)
	repaint()
</pre>
<p>Still have the same bug as before (cannot change brush diameter through default means), but definitely much cleaner code</p>

---

## Post #10 by @lassoan (2018-10-02 20:12 UTC)

<p>Good. I guess not re-creating the segment editor widget fixed the selection reset issue.</p>
<p>Brush parameters are shared between paint and erase effects, so it is a common parameter, which need to be set by using <code>setCommonParameter</code> method:</p>
<pre><code>effect.setCommonParameter("BrushDiameterIsRelative", "0")
effect.setCommonParameter("BrushAbsoluteDiameter", newDiam)</code></pre>

---

## Post #11 by @matthew (2018-10-02 21:34 UTC)

<p>After that last change, it works perfectly! Thank you for all your help!!</p>

---
