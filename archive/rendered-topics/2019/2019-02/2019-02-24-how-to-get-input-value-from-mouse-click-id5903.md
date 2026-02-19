---
topic_id: 5903
title: "How To Get Input Value From Mouse Click"
date: 2019-02-24
url: https://discourse.slicer.org/t/5903
---

# How to get input value from mouse click?

**Topic ID**: 5903
**Date**: 2019-02-24
**URL**: https://discourse.slicer.org/t/how-to-get-input-value-from-mouse-click/5903

---

## Post #1 by @zenox (2019-02-24 13:49 UTC)

<p>Hello,</p>
<p>I am looking to add a button in my extension GUI. The button should allow a user to click somewhere on the volume to retrieve the input value where is clicked.</p>
<p>Can someone say if it’s possible ? In Python.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d4708ee9fba44e4d1829e8ce5c46f23d2c0ed93.png" data-download-href="/uploads/short-url/b1CXjQIJv0z14e7GApVqpedGrOb.png?dl=1" title="2019-02-23-171215_1920x1080_scrot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d4708ee9fba44e4d1829e8ce5c46f23d2c0ed93_2_690x370.png" alt="2019-02-23-171215_1920x1080_scrot" data-base62-sha1="b1CXjQIJv0z14e7GApVqpedGrOb" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d4708ee9fba44e4d1829e8ce5c46f23d2c0ed93_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d4708ee9fba44e4d1829e8ce5c46f23d2c0ed93_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d4708ee9fba44e4d1829e8ce5c46f23d2c0ed93_2_1380x740.png 2x" data-dominant-color="7B7F94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2019-02-23-171215_1920x1080_scrot</span><span class="informations">1920×1030 380 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you,</p>
<p>zenox</p>

---

## Post #2 by @cpinter (2019-02-24 17:12 UTC)

<p>Without knowing the purpose and details of your module, I’d probably add a markups fiducial list that the user fills with clicking around. Then you can very easily get the voxel value under those fiducials.</p>

---

## Post #3 by @zenox (2019-02-24 17:54 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a>, Thank you very much for your answer.</p>
<p>The purpose is just to retrieve the value of input where the user clicked somewhere in a volume.</p>
<p>I will look at the official documentation to find an example of code, then try to implement this feature in my module.</p>

---

## Post #4 by @cpinter (2019-02-24 18:08 UTC)

<aside class="quote no-group" data-username="zenox" data-post="3" data-topic="5903">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/bb73d2/48.png" class="avatar"> zenox:</div>
<blockquote>
<p>The purpose is just to retrieve the value of input where the user clicked somewhere in a volume</p>
</blockquote>
</aside>
<p>Yes but the best way to do it could be very different depending of the bigger picture (real-time or not - interaction vs analysis, number of points, etc.), so it could be useful if you described the purpose of the module and the value picking.</p>

---

## Post #5 by @zenox (2019-02-24 18:26 UTC)

<p>Ok, the goal is to retrieve the value of 1 point to adjust my GUI and help the user of the extension. And this is not for real-time.</p>
<ul>
<li>First, the user clicks on a button <em>Get Value</em> (B)</li>
<li>Then, in the background, there is a listener that allows user to click somewhere in the volume and get <strong>input value</strong>
</li>
<li>Finally, we adjust the <em>Threshold Range</em> cursors (A) with this <strong>input value</strong> in the GUI</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c528c4f315ad763d41e961dcca7086cd07f8551f.jpeg" data-download-href="/uploads/short-url/s89pooYrMwxP3egfVhfkKCpyuqr.jpeg?dl=1" title="3d_slicer_gui" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c528c4f315ad763d41e961dcca7086cd07f8551f_2_690x388.jpeg" alt="3d_slicer_gui" data-base62-sha1="s89pooYrMwxP3egfVhfkKCpyuqr" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c528c4f315ad763d41e961dcca7086cd07f8551f_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c528c4f315ad763d41e961dcca7086cd07f8551f_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c528c4f315ad763d41e961dcca7086cd07f8551f.jpeg 2x" data-dominant-color="F3F1F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d_slicer_gui</span><span class="informations">1333×750 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>For example, if user clicked on <strong>input value</strong> = 1125, we will adjust the <em>Thresold Range</em> cursors (A) with +/- 125, so between 1000 and 1250.</p>

---

## Post #6 by @lassoan (2019-02-24 20:21 UTC)

<p>We usually use temporary markup nodes for this:</p>
<ul>
<li>User clicks “Get value” button</li>
<li>Module creates a markup node, adds an observer for point add event, sets the node as active node (in selection node singleton) and sets mouse interaction mode to Place fiducial mode (in interaction node singleton)</li>
<li>User clicks in the image</li>
<li>Module is notified about the added fiducial, retrieves its position, then deletes the markup node</li>
</ul>

---

## Post #7 by @zenox (2019-02-24 20:28 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, Thank you very much for your answer.</p>
<p>Now, that’s more clear for me.</p>
<p>I will come back here if I don’t find a way to implement it in my module.</p>
<p>Have a good day,</p>
<p>zenox</p>

---

## Post #8 by @lassoan (2019-02-24 20:37 UTC)

<p>You can use qSlicerMarkupsPlaceWidget to all the steps that I described above. The code below creates a button that places a markup (and it also provides signals that you can observe):</p>
<pre><code class="lang-auto"># Temporary markups node
markupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")

def placementModeChanged(active):
  print("Placement: " +("active" if active else "inactive"))
  # You can inspect what is in the markups node here, delete the temporary markup node, etc.

# Create and set up widget that contains a single "place markup" button. The widget can be placed in the module GUI.
placeWidget = slicer.qSlicerMarkupsPlaceWidget()
placeWidget.setMRMLScene(slicer.mrmlScene)
placeWidget.setCurrentNode(markupsNode)
placeWidget.buttonsVisible=False
placeWidget.placeButton().show()
placeWidget.connect('activeMarkupsFiducialPlaceModeChanged(bool)', placementModeChanged)
placeWidget.show()
</code></pre>

---

## Post #9 by @zenox (2019-02-24 21:04 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, This is really helpful, thank you ! Now, it should be easy enough to implement, I’ll let you know if it works.</p>

---

## Post #10 by @zenox (2019-02-25 22:16 UTC)

<p>It works, but opens a new window with the button.</p>
<p>Do you know how I could attach it to my “Get Value” button in the GUI ?</p>
<p>I define my widget to display a button:</p>
<pre><code>def setup(self):
  self.getValueButton = qt.QPushButton("Get Value")
  self.getValueButton.toolTip = "Get value from image"
  self.getValueButton.enabled = False
  self.getValueButton.connect('clicked(bool)', self.onGetValueButton)
</code></pre>
<p>A function to create a markup node, switch to Place fiducial mode and retrieve click position:</p>
<pre><code>def getMousePointValue(self):
  return position
</code></pre>
<p>A function connected to my button:</p>
<pre><code>def onGetValueButton(self):
  position = self.getMousePointValue()</code></pre>

---

## Post #11 by @lassoan (2019-02-25 22:48 UTC)

<p>Instead of calling <code>show()</code> method, add the widget to your module’s GUI the same way as you add any other buttons and widgets.</p>

---

## Post #12 by @zenox (2019-02-26 12:16 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, Oh obviously… it works ! And I can retrieve markup’s position without problem.</p>
<p>In the screenshot of my first post, I have 2 volumes (<em>input.nrrd</em> and <em>segmentation.nrrd</em>).<br>
I don’t find a way to retrieve the <strong>input</strong> value (here 1125) at markup’s position, have you an idea ?</p>

---

## Post #13 by @lassoan (2019-02-27 18:34 UTC)

<aside class="quote no-group" data-username="zenox" data-post="12" data-topic="5903">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/bb73d2/48.png" class="avatar"> zenox:</div>
<blockquote>
<p>I don’t find a way to retrieve the <strong>input</strong> value (here 1125) at markup’s position</p>
</blockquote>
</aside>
<p>See example in the script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>

---

## Post #14 by @zenox (2019-03-01 07:31 UTC)

<p>Ok, I can retrieve the voxel coordinates of my input volume without problem. But I don’t know how to access the value with theses coordinates, like volume[x, y , z] = 1125 ? Sorry, I’m really a noob with Slicer.</p>

---

## Post #15 by @pieper (2019-03-01 12:32 UTC)

<p>You just need to use <code>slicer.utils.array</code> to get a numpy array, and then you can index into it.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_the_values_of_all_voxels_for_a_label_value" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_the_values_of_all_voxels_for_a_label_value</a></p>

---

## Post #16 by @zenox (2019-03-04 02:19 UTC)

<p>Thank you very much <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/lassoan">@lassoan</a>, all is working.</p>

---

## Post #17 by @zenox (2019-03-04 02:23 UTC)

<p>I put a part of code here, that could help others in the futur:</p>
<pre><code> def getMousePointValue(self, volumeNode, markupsNode):
    # Get point coordinate in RAS
    point_ras = [0, 0, 0, 1]

    # Get number of markups
    num_fids = markupsNode.GetNumberOfFiducials()

    # Get coordinates of last markup
    markupsNode.GetNthFiducialWorldCoordinates(num_fids - 1, point_ras)

    # Apply that transform to get volume's RAS coordinates
    transform_ras_to_volume_ras = vtk.vtkGeneralTransform()
    slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(None, volumeNode.GetParentTransformNode(), transform_ras_to_volume_ras)
    point_volume_ras = transform_ras_to_volume_ras.TransformPoint(point_ras[0:3])

    # Get voxel coordinates from physical coordinates
    volume_ras_to_ijk = vtk.vtkMatrix4x4()
    volumeNode.GetRASToIJKMatrix(volume_ras_to_ijk)
    point_ijk = [0, 0, 0, 1]
    volume_ras_to_ijk.MultiplyPoint(np.append(point_volume_ras, 1.0), point_ijk)
    point_ijk = [ int(round(c)) for c in point_ijk[0:3] ]

    # Get markup's position
    x, y, z = point_ijk[0], point_ijk[1], point_ijk[2]

    # Get volume as slicer array
    a = arrayFromVolume(volumeNode)

    # Get value at markup's position
    value = a[z,y,x]</code></pre>

---
