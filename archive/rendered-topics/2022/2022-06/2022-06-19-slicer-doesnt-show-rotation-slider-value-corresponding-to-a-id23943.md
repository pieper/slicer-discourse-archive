---
topic_id: 23943
title: "Slicer Doesnt Show Rotation Slider Value Corresponding To A"
date: 2022-06-19
url: https://discourse.slicer.org/t/23943
---

# Slicer doesn't show rotation slider value corresponding to a transform after rotation axis is not cannonical

**Topic ID**: 23943
**Date**: 2022-06-19
**URL**: https://discourse.slicer.org/t/slicer-doesnt-show-rotation-slider-value-corresponding-to-a-transform-after-rotation-axis-is-not-cannonical/23943

---

## Post #1 by @mau_igna_06 (2022-06-19 12:48 UTC)

<p>I would suggest we use this formula as a default to get the rotation slider values</p><aside class="onebox allowlistedgeneric" data-onebox-src="http://planning.cs.uiuc.edu/node102.html">
  <header class="source">

      <a href="http://planning.cs.uiuc.edu/node102.html" target="_blank" rel="noopener">planning.cs.uiuc.edu</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="http://planning.cs.uiuc.edu/node102.html" target="_blank" rel="noopener">Yaw, pitch, and roll rotations</a></h3>

  <p>Yaw, pitch, and roll rotations</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It may be useful for the users…</p>
<p>Do you think a pull request allowing a scale, rotationAxis and pivot point to define a the transform would be useful?</p>
<p>Also there is a button to switch between global and local coordinate systems… Why not allow any homogeneous transform as local?</p>
<p>Hope this comments are useful</p>

---

## Post #2 by @pieper (2022-06-19 14:08 UTC)

<p>Yes, it comes up from time to time that people wonder why the rotation sliders get reset.  Even if the rotation decomposition is not unique it may still be useful to show it and use it as the basis for modification.  An improved GUI to edit transforms would be very welcome.</p>

---

## Post #3 by @mau_igna_06 (2022-06-19 18:45 UTC)

<p>I’ll try to implement it</p>
<p>I think a third widget on the transforms module should show a scale-rotationAxisVector, a pivotPoint and and an angle (even if the pivotPoint ends up at infinity for some homogeneous transforms)</p>
<p>I’ve started diving into it but it’s hard. Should I create a new ctkvtkabstractmatrixwidget? Maybe with a checkbox to normalize the scale-rotatoonAxisVector<br>
How do I change the default number of rows and columns?</p>
<p>More importantly how do I make VS Community recognize my changes to the S4 code folder?</p>

---

## Post #4 by @pieper (2022-06-19 18:58 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="3" data-topic="23943">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>I’ve started diving into it but it’s hard. Should I create a new ctkvtkabstractmatrixwidget? Maybe with a checkbox to normalize the scale-rotatoonAxisVector</p>
</blockquote>
</aside>
<p>Probably start first with a list of features you want to implement.  Ideally yes, in a reusable widget at the ctk level, but possibly this is better as a mrml widget because you may rather use markups to define the pivot point, rotation lines, or reflection planes.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="3" data-topic="23943">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>How do I change the default number of rows and columns?</p>
</blockquote>
</aside>
<p>Not sure what you mean here.  Aren’t you wanting to edit 4x4 matrices?</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="3" data-topic="23943">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>More importantly how do I make VS Community recognize my changes to the S4 code folder?</p>
</blockquote>
</aside>
<p>This seems like a completely unrelated question - maybe start a new thread with more detail.</p>

---

## Post #5 by @mau_igna_06 (2022-06-20 15:03 UTC)

<p>I implemented an early version but I’m not able to make it work for sure, it’s unstable. I may need some help. Maybe I can show you all part of the implementation tomorrow on the developers call</p>

---

## Post #6 by @lassoan (2022-06-21 04:30 UTC)

<p>I’ve played around with this a few times because indeed it seems to make sense to have Euler angle sliders. However, in practice it works very poorly. You can find a complete implementation in Python in this post that you can easily test (and try to fix):</p>
<aside class="quote quote-modified" data-post="2" data-topic="15873">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/reformat-module-values-not-resetting/15873/2">Reformat module Values not resetting</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    The sliders are used only for relative rotations. See more details here: <a href="https://discourse.slicer.org/t/is-the-rotation-of-the-3d-slicers-transform-module-euler-or-quaternion/11944/2" class="inline-onebox">Is the rotation of the 3D Slicer's Transform module Euler or Quaternion? - #2 by lassoan</a> 
We should reset them to 0 more often to make sure users don’t mistake it for Euler angles or something similar. 
Euler angles (and similar representations that rely on successive rotations along multiple axes) are not well suited for representing arbitrary orientations, as it suffers from gimbal lock and there are multiple parametrizat…
  </blockquote>
</aside>


---

## Post #7 by @mau_igna_06 (2022-06-21 12:42 UTC)

<p>It appears this works:</p>
<pre><code class="lang-auto">import math
import numpy as np

transformNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformNode')
# transformNode = getNode('Transform')

def rotationToVtk(R):
    '''
    Concert a rotation matrix into the Mayavi/Vtk rotation paramaters (pitch, roll, yaw)
    '''
    def euler_from_matrix(matrix):
        """Return Euler angles (syxz) from rotation matrix for specified axis sequence.
        :Author:
          `Christoph Gohlke &lt;http://www.lfd.uci.edu/~gohlke/&gt;`_

        full library with coplete set of euler triplets (combinations of  s/r x-y-z) at
            http://www.lfd.uci.edu/~gohlke/code/transformations.py.html

        Note that many Euler angle triplets can describe one matrix.
        """
        # epsilon for testing whether a number is close to zero
        _EPS = np.finfo(float).eps * 5.0
        #
        # axis sequences for Euler angles
        _NEXT_AXIS = [1, 2, 0, 1]
        firstaxis, parity, repetition, frame = (1, 1, 0, 0) # ''
        #
        i = firstaxis
        j = _NEXT_AXIS[i+parity]
        k = _NEXT_AXIS[i-parity+1]
        #
        M = np.array(matrix, dtype='float', copy=False)[:3, :3]
        if repetition:
            sy = np.sqrt(M[i, j]*M[i, j] + M[i, k]*M[i, k])
            if sy &gt; _EPS:
                ax = np.arctan2( M[i, j],  M[i, k])
                ay = np.arctan2( sy,       M[i, i])
                az = np.arctan2( M[j, i], -M[k, i])
            else:
                ax = np.arctan2(-M[j, k],  M[j, j])
                ay = np.arctan2( sy,       M[i, i])
                az = 0.0
        else:
            cy = np.sqrt(M[i, i]*M[i, i] + M[j, i]*M[j, i])
            if cy &gt; _EPS:
                ax = np.arctan2( M[k, j],  M[k, k])
                ay = np.arctan2(-M[k, i],  cy)
                az = np.arctan2( M[j, i],  M[i, i])
            else:
                ax = np.arctan2(-M[j, k],  M[j, j])
                ay = np.arctan2(-M[k, i],  cy)
                az = 0.0
        #
        if parity:
            ax, ay, az = -ax, -ay, -az
        if frame:
            ax, az = az, ax
        return ax, ay, az
    #
    r_yxz = np.array(euler_from_matrix(R))*180/math.pi
    r_xyz = r_yxz[[1, 0, 2]]
    return r_xyz


transformObserver = 0
# Create widget
widget = qt.QFrame()
layout = qt.QFormLayout()
widget.setLayout(layout)
axisSliderWidgets = []
for i in range(3):
    axisSliderWidget = ctk.ctkSliderWidget()
    axisSliderWidget.singleStep = 1.0
    if i==1:
        axisSliderWidget.minimum = -90
        axisSliderWidget.maximum = 90
    else:
        axisSliderWidget.minimum = -180
        axisSliderWidget.maximum = 180
    axisSliderWidget.value = 0
    axisSliderWidget.tracking = False
    layout.addRow(f"Axis {i+1}: ", axisSliderWidget)
    axisSliderWidgets.append(axisSliderWidget)


def updateTransformFromWidget(value):
    global transformObserver
    transform = vtk.vtkTransform()
    transform.RotateY(axisSliderWidgets[1].value)
    axisOfRotation = [1,0,0,0]
    transform.GetMatrix().MultiplyPoint(axisOfRotation,axisOfRotation)
    transform.RotateWXYZ(axisSliderWidgets[0].value,axisOfRotation[0],axisOfRotation[1],axisOfRotation[2])
    #transform.RotateX(axisSliderWidgets[0].value)
    axisOfRotation = [0,0,1,0]
    transform.GetMatrix().MultiplyPoint(axisOfRotation,axisOfRotation)
    transform.RotateWXYZ(axisSliderWidgets[2].value,axisOfRotation[0],axisOfRotation[1],axisOfRotation[2])
    #transform.RotateZ(axisSliderWidgets[1].value)
    transformNode.RemoveObserver(transformObserver)
    transformNode.SetMatrixTransformToParent(transform.GetMatrix())
    transformObserver = transformNode.AddObserver(slicer.vtkMRMLTransformableNode.TransformModifiedEvent, updateWidgetFromTransform)

def updateWidgetFromTransform(caller, event):
    transformMatrix = transformNode.GetMatrixTransformToParent()
    transformMatrix_np = arrayFromVTKMatrix(transformMatrix)
    angles_xyz = rotationToVtk(transformMatrix_np)
    for i in range(3):
        axisSliderWidget = axisSliderWidgets[i]
        wasBlocked = axisSliderWidget.blockSignals(True)
        axisSliderWidget.value = angles_xyz[i]
        axisSliderWidget.blockSignals(wasBlocked)

def resetTransform():
    transformNode.SetMatrixTransformToParent(vtk.vtkMatrix4x4())

for i in range(3):
    axisSliderWidgets[i].connect("valueChanged(double)", updateTransformFromWidget)

resetButton = qt.QPushButton("Reset")
layout.addWidget(resetButton)
resetButton.connect("clicked()", resetTransform)

widget.show()

transformObserver = transformNode.AddObserver(slicer.vtkMRMLTransformableNode.TransformModifiedEvent, updateWidgetFromTransform)

# transformNode.RemoveObserver(transformObserver)
</code></pre>
<p>Your feedback would be great</p>

---

## Post #8 by @lassoan (2022-06-21 14:40 UTC)

<p>This script works beautifully in the sense that the rotation matrix to sliders mapping is invertible.</p>
<p>However, I could not make out any sense of the transform that is created from the sliders. For example, set rotation around Axis3 to 40 deg (nothing extreme) and see the wild spinning around a rotating axis:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de26e6eeaead112d7da4d6de217506c4e7e90c39.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de26e6eeaead112d7da4d6de217506c4e7e90c39.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de26e6eeaead112d7da4d6de217506c4e7e90c39.mp4</a>
    </source></video>
  </div><p></p>
<p>How would you use these sliders to achieve a desired orientation?</p>
<p>In contrast, Slicer’s rotations are really simple and meaningful and you can easily achieve any orientation:</p>
<p>Rotation around the head’s RAS axes:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38932b3d14478db9563c037c6e630aafcd43cf24.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38932b3d14478db9563c037c6e630aafcd43cf24.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38932b3d14478db9563c037c6e630aafcd43cf24.mp4</a>
    </source></video>
  </div><p></p>
<p>Rotation around the world’s RAS axes:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/104089dcc1566b4a84df43819d6113efab781fab.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/104089dcc1566b4a84df43819d6113efab781fab.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/104089dcc1566b4a84df43819d6113efab781fab.mp4</a>
    </source></video>
  </div><p></p>
<p>It seems that Blender struggles with this, too - see their <a href="https://docs.blender.org/manual/en/latest/advanced/appendices/rotations.html">documentation</a>. No good solution exists, so they offer multiple orientation parameterization options, each with its own problems. Blender seem to store the orientation using the chosen parametrization - probably because it needs to make those parameters adjustable in animations. But this has a very high price - modifying orientation becomes a really complicated task (you could not simply set an absolute transform, but you would need to know how to make incremental changes to a transform to achieve the desired orientation, with each parametrization option), so I don’t think we should do this in Slicer.</p>
<p>If we used the Gohlke parametrization then we could keep displaying the slider values (we would not need to reset the sliders to 0) but for me the displayed angle values don’t seem to be meaningful, so I’m not sure if it is worth the trouble. It is also not a standard parametrization, so it would not be portable to other applications (it would not correspond to angles displayed in Blender, ParaView, etc.).</p>

---

## Post #9 by @mau_igna_06 (2022-06-21 15:30 UTC)

<p>Hi Andras.</p>
<p>Please try this one:</p>
<pre><code class="lang-auto">import math
import numpy as np

transformNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTransformNode')
# transformNode = getNode('Transform')

def rotationToVtk(R):
    '''
    Concert a rotation matrix into the Mayavi/Vtk rotation paramaters (pitch, roll, yaw)
    '''
    def euler_from_matrix(matrix):
        """Return Euler angles (syxz) from rotation matrix for specified axis sequence.
        :Author:
          `Christoph Gohlke &lt;http://www.lfd.uci.edu/~gohlke/&gt;`_

        full library with coplete set of euler triplets (combinations of  s/r x-y-z) at
            http://www.lfd.uci.edu/~gohlke/code/transformations.py.html

        Note that many Euler angle triplets can describe one matrix.
        """
        # epsilon for testing whether a number is close to zero
        _EPS = np.finfo(float).eps * 5.0
        #
        # axis sequences for Euler angles
        _NEXT_AXIS = [0, 0, 1, 2]
        #
        #inner axis: code of axis (‘x’:0, ‘y’:1, ‘z’:2) of rightmost matrix.
        #parity : even (0) if inner axis ‘x’ is followed by ‘y’, ‘y’ is followed by ‘z’, or ‘z’ is followed by ‘x’. Otherwise odd (1).
        #repetition : first and last axis are same (1) or different (0).
        #frame : rotations are applied to static (0) or rotating (1) frame.
        #
        firstaxis, parity, repetition, frame = (2, 0, 0, 1) # ''
        #
        i = firstaxis
        j = _NEXT_AXIS[i+parity]
        k = _NEXT_AXIS[i-parity+1]
        #
        M = np.array(matrix, dtype='float', copy=False)[:3, :3]
        if repetition:
            sy = np.sqrt(M[i, j]*M[i, j] + M[i, k]*M[i, k])
            if sy &gt; _EPS:
                ax = np.arctan2( M[i, j],  M[i, k])
                ay = np.arctan2( sy,       M[i, i])
                az = np.arctan2( M[j, i], -M[k, i])
            else:
                ax = np.arctan2(-M[j, k],  M[j, j])
                ay = np.arctan2( sy,       M[i, i])
                az = 0.0
        else:
            cy = np.sqrt(M[i, i]*M[i, i] + M[j, i]*M[j, i])
            if cy &gt; _EPS:
                ax = np.arctan2( M[k, j],  M[k, k])
                ay = np.arctan2(-M[k, i],  cy)
                az = np.arctan2( M[j, i],  M[i, i])
            else:
                ax = np.arctan2(-M[j, k],  M[j, j])
                ay = np.arctan2(-M[k, i],  cy)
                az = 0.0
        #
        if parity:
            ax, ay, az = -ax, -ay, -az
        if frame:
            ax, az = az, ax
        return ax, ay, az
    #
    r_yxz = np.array(euler_from_matrix(R))*180/math.pi
    r_xyz = r_yxz[[1, 0, 2]]
    return r_xyz


transformObserver = 0
# Create widget
widget = qt.QFrame()
layout = qt.QFormLayout()
widget.setLayout(layout)
axisSliderWidgets = []
for i in range(3):
    axisSliderWidget = ctk.ctkSliderWidget()
    axisSliderWidget.singleStep = 1.0
    axisSliderWidget.minimum = -180
    axisSliderWidget.maximum = 180
    axisSliderWidget.value = 0
    axisSliderWidget.tracking = False
    layout.addRow(f"Axis {i+1}: ", axisSliderWidget)
    axisSliderWidgets.append(axisSliderWidget)


def updateTransformFromWidget(value):
    global transformObserver
    transform = vtk.vtkTransform()
    transform.RotateY(axisSliderWidgets[1].value)
    axisOfRotation = [1,0,0,0]
    transform.GetMatrix().MultiplyPoint(axisOfRotation,axisOfRotation)
    transform.RotateWXYZ(axisSliderWidgets[0].value,axisOfRotation[0],axisOfRotation[1],axisOfRotation[2])
    #transform.RotateX(axisSliderWidgets[0].value)
    axisOfRotation = [0,0,1,0]
    transform.GetMatrix().MultiplyPoint(axisOfRotation,axisOfRotation)
    transform.RotateWXYZ(axisSliderWidgets[2].value,axisOfRotation[0],axisOfRotation[1],axisOfRotation[2])
    #transform.RotateZ(axisSliderWidgets[1].value)
    transformNode.RemoveObserver(transformObserver)
    transformNode.SetMatrixTransformToParent(transform.GetMatrix())
    transformObserver = transformNode.AddObserver(slicer.vtkMRMLTransformableNode.TransformModifiedEvent, updateWidgetFromTransform)

def updateWidgetFromTransform(caller, event):
    transformMatrix = transformNode.GetMatrixTransformToParent()
    transformMatrix_np = arrayFromVTKMatrix(transformMatrix)
    angles_xyz = rotationToVtk(transformMatrix_np)
    for i in range(3):
        axisSliderWidget = axisSliderWidgets[i]
        wasBlocked = axisSliderWidget.blockSignals(True)
        axisSliderWidget.value = angles_xyz[i]
        axisSliderWidget.blockSignals(wasBlocked)

def resetTransform():
    transformNode.SetMatrixTransformToParent(vtk.vtkMatrix4x4())

for i in range(3):
    axisSliderWidgets[i].connect("valueChanged(double)", updateTransformFromWidget)

resetButton = qt.QPushButton("Reset")
layout.addWidget(resetButton)
resetButton.connect("clicked()", resetTransform)

widget.show()

transformObserver = transformNode.AddObserver(slicer.vtkMRMLTransformableNode.TransformModifiedEvent, updateWidgetFromTransform)

# transformNode.RemoveObserver(transformObserver)
</code></pre>
<p>I think it works</p>

---

## Post #10 by @lassoan (2022-06-21 18:45 UTC)

<p>Thanks for the update. Maybe it works slightly differently, but the main problems remain the same: when you set one angle to non-zero (e.g., axis3=40) then adjust rotation around a different axis then it spins the object around a rotating axis, which results in an very complicated motion pattern and non-meaningful angle values.</p>

---

## Post #11 by @mau_igna_06 (2022-06-22 18:30 UTC)

<p>I think there is a solution to this problem using euler intrinsic angles:</p>
<blockquote>
<p>Let’s say there are n sliders (could be 3) controlling the angle of rotation and a combobox defining the relative x, y or z axis of rotation (to the previous transform).<br>
That way the transformation T for rotations in post-multiply order of for example: z’‘’=15,x’‘=30,y’=20,x=25</p>
</blockquote>
<pre><code class="lang-auto">T = R(z''',15)*R(x'',30)*R(y',20)*R(x,25)
</code></pre>
<p>This is slider acculation is cumbersome but confortable for sequencial rotation transform definition. It could be compressed to only 3 sliders with angle values update according to the current transform when another of the 3 sliders is hovered. And changes to the last hovered slider (ie last rotation applied) would still be meaningful to a rotation axis that matches one of transformed, original axis of the polydata. Maybe some logic could be applied to hide this jumpy behavior of the angle values (as rotation axis vectors change but are not visible to the user when the previously explained behavior is executed)</p>

---

## Post #12 by @lassoan (2022-06-22 19:07 UTC)

<p>The problem is that it would be impossible to compute the value of those 4 sliders from a 4x4 matrix. To summarize the requirements:</p>
<ol>
<li>invertible conversion between parameters (adjusted by the sliders) and 3x3 orientation matrix</li>
<li>meaningful parameter values</li>
<li>rotation along a stationary axis when any of the parameters are changed</li>
<li>slight change of orientation when parameters are slightly changed (smooth orientation change, no jumps)</li>
</ol>
<p>I believe it is impossible to fulfill all these requirements. I don’t think any other software managed to solve this. There are many ways to solve this if we relax a few requirements, but which requirements to relax depends on the application (probably you would not use the same parameterization for a fluoroscopy C-arm as for a knee joint angle). Application-specific transform editing sliders are added in extensions (e.g., we’ll release a C-arm simulator in SlicerHeart soon and it has meaningful C-arm angle display and editing with sliders).</p>
<p>Currently in Slicer core we avoid any particular parametrization. Using slider widgets for this is probably a bit confusing, the proper representation would be a jogwheel control, but there is no suitable built-in control in Qt.</p>
<p>Horizontal jogwheel control (looks similar to a slider but it can be dragged at any point, there is no handle; would be usable instead of a Slicer, but it is not a built-in Qt feature):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6573ef20f7c628ed3f3b1e44e3d89da601085efa.png" alt="image" data-base62-sha1="etuBXbM3LEdu8AK4aKQtDQPdyEW" width="252" height="61"></p>
<p>Round jogwheel control (available in Qt as <code>QDial</code> - unfortunately, it is very inconvenient to use, as the user needs to move the mouse pointer in a circular pattern to adjust it):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54f58817c2806ce7ed65823c896cbe0eb8967e0e.png" alt="image" data-base62-sha1="c7A9HRmTtK9WboN0stVN3OmR4Gq" width="194" height="180"></p>

---

## Post #13 by @mau_igna_06 (2022-06-25 20:31 UTC)

<p>Please check this example:</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/mauigna06/627596274a2b3412989bae81cb060fed">
  <header class="source">

      <a href="https://gist.github.com/mauigna06/627596274a2b3412989bae81cb060fed" target="_blank" rel="noopener">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/mauigna06/627596274a2b3412989bae81cb060fed" target="_blank" rel="noopener">https://gist.github.com/mauigna06/627596274a2b3412989bae81cb060fed</a></h4>

  <h5>testExampleOfRotation.py</h5>
  <pre><code class="Python"># save in a len=3 buffer the last moved sliders
# generate transform for slider combination according to dictionary consulted by the buffer
# calculate transform in bufferOrder and set sliders



import math
import numpy as np

#source https://github.com/matthew-brett/transforms3d/blob/52321496a0d98f1f698fd3ed81f680d740202553/transforms3d/_gohlketransforms.py#L1680</code></pre>
    This file has been truncated. <a href="https://gist.github.com/mauigna06/627596274a2b3412989bae81cb060fed" target="_blank" rel="noopener">show original</a>

<p>
</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It achieves 3 and 4. More or less 2 and 1.<br>
It selects the most convenient intrinsic-euler angles representation and uses it for new calculations but shows the default Roll, Yaw, Pitch sliders to define the angles so it is comfortable and not jumpy.</p>
<p>Hope you consider it useful</p>

---
