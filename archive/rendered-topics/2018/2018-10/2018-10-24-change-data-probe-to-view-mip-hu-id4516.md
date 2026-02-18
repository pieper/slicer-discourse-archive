# Change data probe to view MIP HU

**Topic ID**: 4516
**Date**: 2018-10-24
**URL**: https://discourse.slicer.org/t/change-data-probe-to-view-mip-hu/4516

---

## Post #1 by @mag (2018-10-24 01:16 UTC)

<p>Hi, I’m looking at very small features on CTA scans and there are 2 things I’d like data probe to do but it doesn’t and I’m not sure how to modify it to get the behaviour I want.</p>
<ol>
<li>
<p>When I am in one of the slice viewers, e.g. the red one, and scroll up and down with the mouse wheel or the arrows in a fixed point, data probe does not update the HU nor the position. I have to move the mouse in the viewer for data probe to update. Is there a way to make it update even when the mouse position has not changed but the slice has?</p>
</li>
<li>
<p>I am visualizing MIP in the slice views with this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Thick_slab_reconstruction_and_maximum.2Fminimum_intensity_volume_projections" rel="noopener nofollow ugc">code</a>, however when I move the mouse around one of the slice viewer, the scalar value that I see in data probe in the left bottom corner is still the HU of the single slice, not the one of the MIP.  Is there a way to change this behaviour? (I have attached an example in case it’s not clear: in the screenshot I am looking at a 5 mm MIP. The mouse arrow is not captured but I was pointing at the red slice exactly on the intersection of the yellow and green axes. I’d like data probe to show me the HU of the MIP view, so something around 300, but it shows me the HU of the single slice which is 7)<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd0f7ed22ef11fb342a17b7a8979c066ff801e2d.jpeg" data-download-href="/uploads/short-url/A6FZVcVDXMQCWIR463j74Y3V6vH.jpeg?dl=1" title="38%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd0f7ed22ef11fb342a17b7a8979c066ff801e2d_2_690x388.jpeg" alt="38%20PM" data-base62-sha1="A6FZVcVDXMQCWIR463j74Y3V6vH" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd0f7ed22ef11fb342a17b7a8979c066ff801e2d_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd0f7ed22ef11fb342a17b7a8979c066ff801e2d_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fd0f7ed22ef11fb342a17b7a8979c066ff801e2d_2_1380x776.jpeg 2x" data-dominant-color="85858E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">38%20PM</span><span class="informations">5120×2880 1.98 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> .</p>
</li>
</ol>
<p>Thank you for any help,</p>
<p>Marta</p>

---

## Post #2 by @jamesobutler (2018-10-31 03:42 UTC)

<p>Hi Marta,</p>
<p>Sorry for not getting a response sooner!</p>
<p>Regarding 1) what you are describing is behavior that is like the same as <a href="https://issues.slicer.org/view.php?id=3262" rel="nofollow noopener">issue 3262</a> in Slicer’s issue tracker. I have added a note to that issue specifying with your experience as a way to increase its likelihood of it getting fixed in the future.</p>
<p>Regarding 2) I’m not exactly sure what is going on there. I would point you to using the <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/SimpleFilters" rel="nofollow noopener">SimpleFilters</a> module which makes it easy to generate projections and use other volume filters. You would set the output volume to be a new volume, and DataProbe should provide you updated results when you move your mouse position over this output volume.</p>

---

## Post #3 by @lassoan (2018-10-31 04:52 UTC)

<aside class="quote no-group" data-username="mag" data-post="1" data-topic="4516">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/58f4c7/48.png" class="avatar"> mag:</div>
<blockquote>
<p>HU of the single slice, not the one of the MIP. Is there a way to change this behaviour?</p>
</blockquote>
</aside>
<p>Since thick slice feature is not exposed on the GUI, we most likely not update the data probe’s behavior for now. However, you can print pixel value of the resliced image by copy-pasting this code snippet into the Python interactor:</p>
<pre><code class="lang-auto">def onMouseMoved(observer,eventid):  
  xyz = [0,0,0]
  crosshairNode.GetCursorPositionXYZ(xyz)
  pixelValue = reslice.GetOutput().GetScalarComponentAsDouble(int(xyz[0]),int(xyz[1]), int(xyz[2]), 0)
  print("{0} -&gt; {1}".format(xyz, pixelValue))

sliceNode = slicer.mrmlScene.GetNodeByID('vtkMRMLSliceNodeRed')
appLogic = slicer.app.applicationLogic()
sliceLogic = appLogic.GetSliceLogic(sliceNode)
sliceLayerLogic = sliceLogic.GetBackgroundLayer()
reslice = sliceLayerLogic.GetReslice()

crosshairNode=slicer.util.getNode('Crosshair') 
crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, onMouseMoved)
</code></pre>
<p>Why do you need the MIP value?</p>

---

## Post #4 by @jamesobutler (2018-11-01 14:17 UTC)

<p><a class="mention" href="/u/mag">@mag</a> To provide you with an update, the issue described in 1) I can now confirm is solved thanks to a fix by <a class="mention" href="/u/lassoan">@lassoan</a>. You can download and install today’s nightly build and it will have that fix.</p>

---

## Post #5 by @mag (2018-11-01 19:53 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="4516">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>issue 3262</p>
</blockquote>
</aside>
<p>That’s awesome, thanks so much!</p>

---

## Post #6 by @mag (2018-11-01 20:04 UTC)

<p>I am extending an existing study and need to determine the location of maximum contrast enhancement in some vascular segments. The way the previous research fellow did it was to look at 5 mm MIP to find the maximum HU on the axial view, then refine the location by scrolling up and down single slices, so I am trying to follow the exact same steps even if with a different software. Once I have the point of interest I create a small spherical segment and get the average HU at that position.</p>

---

## Post #7 by @mag (2019-01-07 22:16 UTC)

<p>Hi,</p>
<p>I  have come back to this problem after some time and I’d have some more questions if anybody has time to help.<br>
Last time when I had to look at the MIPs I used to copy the code that Andras posted into the Python interactor whenever I needed it. However I would like to have it in my script so that when I click my custom button to display the MIP this code is automatically executed. Also, I’d like to add some code such that when I click my custom button to return to the non-MIP visualization, Slicer stops printing the mouse position/HU in the interactor.</p>
<p>I already had the buttons to show/disable MIPs. So I tried to just add the onMouseMoved function to print mouse position/HU, but I get an error about the number of arguments every time I move the mouse (see screenshot) and I don’t understand why.</p>
<p>In the widget code I have:</p>
<p>[…]</p>
<pre><code>    self.showMIPRedButton = qt.QPushButton("MIP Red")
    self.showMIPRedButton.toolTip = "Show MIP in red viewer"
    self.showMIPRedButton.enabled = True
    self.parametersFormLayout.addRow(self.showMIPRedButton)

    self.undoMIPButton = qt.QPushButton("Default view")
    self.undoMIPButton.toolTip = "Reset view to default mode"
    self.undoMIPButton.enabled = True
    self.layout.addWidget(self.undoMIPButton)

    self.showMIPRedButton.connect('clicked(bool)', self.onShowMIPRedButton)
    self.undoMIPButton.connect('clicked(bool)', self.onUndoMIPButton)

def onShowMIPRedButton(self):
    logic = probeMIPLogic()
    logic.showMIPRed(self.inputSelector.currentNode())

def onUndoMIPButton(self):
    logic = probeMIPLogic()
    logic.MIPreset()
</code></pre>
<p>And then in the logic code:</p>
<pre><code>    # ======== FROM ANDRAS POST ======== #
def onMouseMoved(observer,eventid):
    xyz = [0,0,0]
    crosshairNode.GetCursorPositionXYZ(xyz)
    pixelValue = reslice.GetOutput().GetScalarComponentAsDouble(int(xyz[0]),int(xyz[1]), int(xyz[2]), 0)
    print("{0} -&gt; {1}".format(xyz, pixelValue))
    # ==================================== #

def showMIPRed(self, inputVolume):
    """ Show maximum intensity projection in Red slice viewer. Does not change scalar volume, only modifies
    viewing settings.
        """
    sliceNode = None
    sliceLogic = None
    vtkMRMLSliceNode = 'vtkMRMLSliceNodeRed'
    sliceNode = slicer.mrmlScene.GetNodeByID(vtkMRMLSliceNode)
    if sliceNode:
        appLogic = slicer.app.applicationLogic()
    if appLogic:
        sliceLogic = appLogic.GetSliceLogic(sliceNode)
    if not sliceNode or not sliceLogic:
        print "Err"
        return
    sliceLayerLogic = sliceLogic.GetBackgroundLayer()
    self.reslice = sliceLayerLogic.GetReslice()
    self.reslice.SetSlabModeToMax()
    self.reslice.SetSlabNumberOfSlices(20)
    self.reslice.SetSlabSliceSpacingFraction(1)
    sliceNode.Modified()

    # ======== FROM ANDRAS POST ======== #
    crosshairNode=slicer.util.getNode('Crosshair')
    crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, self.onMouseMoved)
    # =================================== #
    return

def MIPreset(self):
    """ Reset slice viewers to default setting (no MIP).
        """
    print "Disabling MIP in the slice viewers"
    sliceNode = None
    sliceLogic = None
    for slice_color in ["Green", "Red", "Yellow"]:
        vtkMRMLSliceNode = 'vtkMRMLSliceNode' + slice_color
        sliceNode = slicer.mrmlScene.GetNodeByID(vtkMRMLSliceNode)
        if sliceNode:
            appLogic = slicer.app.applicationLogic()
        if appLogic:
            sliceLogic = appLogic.GetSliceLogic(sliceNode)
        if not sliceNode or not sliceLogic:
            print "Err"
            return
        sliceLayerLogic = sliceLogic.GetBackgroundLayer()
        reslice = sliceLayerLogic.GetReslice()
        reslice.SetSlabModeToMax()
        reslice.SetSlabNumberOfSlices(1)
        reslice.SetSlabSliceSpacingFraction(1)
        sliceNode.Modified()
    return
</code></pre>
<p>Thanks in advance for any help!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f36ca4afaee0bfe6fa95e4cba98863b08086172.png" data-download-href="/uploads/short-url/2aAy4p6l4vUjLab2oVg0I9N48qS.png?dl=1" title="screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0f36ca4afaee0bfe6fa95e4cba98863b08086172_2_690x388.png" alt="screenshot" data-base62-sha1="2aAy4p6l4vUjLab2oVg0I9N48qS" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0f36ca4afaee0bfe6fa95e4cba98863b08086172_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0f36ca4afaee0bfe6fa95e4cba98863b08086172_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0f36ca4afaee0bfe6fa95e4cba98863b08086172_2_1380x776.png 2x" data-dominant-color="9A9597"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot</span><span class="informations">1920×1080 361 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @jamesobutler (2019-01-07 23:46 UTC)

<p><code>def onMouseMoved(observer,eventid):</code><br>
Previously it was a simple function.  If you have made it a method of a class you will need <code>self</code> as an argument like other methods such as <code>showMIPRed</code>. The error you’re having is because of the mismatch of expected arguments.</p>
<p>Try changing to <code>def onMouseMoved(self, observer, eventid)</code>.</p>

---

## Post #9 by @mag (2019-01-08 00:14 UTC)

<p>That’s right, sorry. As you can tell I’m a very beginner at Python.<br>
I am still a bit confused though because when I call the method in this line</p>
<pre><code>crosshairNode.AddObserver(slicer.vtkMRMLCrosshairNode.CursorPositionModifiedEvent, self.onMouseMoved)
</code></pre>
<p>I’m not specifying any argument at all. How does onMouseMoved know what observer and eventid are? Is it AddObserver who passes these argument to onMouseMoved? And if so how can I pass crosshairNode to onMouseMoved without having to specifying eventid and observer which I don’t have?</p>
<p>Thanks</p>

---

## Post #10 by @lassoan (2019-01-08 03:54 UTC)

<p>The easiest way is to store variables in the object (for example, you can store the crosshair node in self.crosshairNode variable).</p>
<p>You can use lambda functions to pass arbitrary additional arguments to callback functions. If you need to access the caller object then you can use the technique described <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_can_I_access_callData_argument_in_a_VTK_object_observer_callback_function" rel="nofollow noopener">here</a>.</p>

---
