---
topic_id: 33275
title: "Python Script To Automate Rotation"
date: 2023-12-06
url: https://discourse.slicer.org/t/33275
---

# Python script to automate rotation

**Topic ID**: 33275
**Date**: 2023-12-06
**URL**: https://discourse.slicer.org/t/python-script-to-automate-rotation/33275

---

## Post #1 by @Michael_Allen (2023-12-06 23:41 UTC)

<p>Hi all, I’m working on a project creating radiographic views from CT scans, rotating one volume inside another using the repository script (<a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/ScriptedLoadableModule.py</a>). This works great. I need to make 1 degree increments and save time images each time, which for multiple patient samples, I’m hoping to automate. I wrote a Python script for exporting video and 3d spins of a CT volume for other projects, and that works well. Python and most programming is new to me but I can figure most stuff out with pointers in the right direction and google. In looking at the transform scripts that start to get into C++, I can’t really figure out whats going on though and could use some direction.</p>
<p>My workflow will be:</p>
<ol>
<li>use the Script linked above to set the rotation point for my volume.</li>
<li>Increase the rotation by 1 degree.</li>
<li>Capture screenshot.</li>
</ol>
<p>In a python script, is there a way to change the rotation of a volume transform? Does anyone know any places to start looking around for ideas?</p>
<p>I’ve been looking at these scripts on the slicer github to try and figure out what’s going on with little progress:<br>
Modules/Loadable/Transforms/qSlicerTransformsModuleWidget.h<br>
Modules/Loadable/Transforms/qSlicerTransformsModule.cxx<br>
Libs/MRML/Widgets/qMRMLTransformSliders.cxx<br>
Libs/MRML/Widgets/qMRMLTransformSliders.h</p>
<p>Thanks for any suggestions!</p>

---

## Post #2 by @Michael_Allen (2023-12-08 18:29 UTC)

<p>Progress!</p>
<p>I found the qMRMLLinearTransformSliders pages by following the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features" rel="noopener nofollow ugc">instructions</a> for tracking down a slicer function, go figure <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Trial and error led me to:</p>
<pre><code class="lang-auto">increment = 1
transformNode = getNode('LinearTransform')
w = slicer.qMRMLLinearTransformSlider()
w.setMRMLTransformNode(transformNode)
w.TypeOfTransform = w.ROTATION_IS
w.applyTransformation(increment)
</code></pre>
<p>This is after using the repository script for rotation around a point. The ‘LinearTransform’ node is the transform that is adjusted with the transform sliders, and that is what I’m controlling with the script. You can adjust which slider by changing the TypeOfTransform line (Rotation or Translation, IS/LR/PA).</p>
<p>Now I need to write something simple to iterate through a range for the increment and take a picture each time.</p>

---

## Post #3 by @Michael_Allen (2023-12-10 19:55 UTC)

<p>Here is the final code for anyone interested.</p>
<p>First I load up the repository script for rotation around a point as linked above. Then I input my code below to setup the manual increment of the transform.</p>
<pre><code class="lang-auto">from slicer import qMRMLLinearTransformSlider

increment = 1
transformNode = getNode('LinearTransform')
w = slicer.qMRMLLinearTransformSlider()
w.setMRMLTransformNode(transformNode)
w.TypeOfTransform = w.ROTATION_IS
w.applyTransformation(increment)
</code></pre>
<p>To automate and export a high resolution image, I use the script from <a href="https://discourse.slicer.org/t/higher-resolution-for-screen-captures-of-3d-view/8880/30">here.</a></p>
<p>Adjust the range, image resolution, and the output directory/filename structure as needed:</p>
<pre><code class="lang-auto">for x in range (0, 61):
    w.applyTransformation(increment)
    vtk.vtkGraphicsFactory()
    gf = vtk.vtkGraphicsFactory()
    gf.SetOffScreenOnlyMode(1)
    gf.SetUseMesaClasses(1)
    rw = vtk.vtkRenderWindow()
    rw.SetOffScreenRendering(1)
    ren = vtk.vtkRenderer()
    rw.SetSize(3000, 3000)

    lm = slicer.app.layoutManager()
    ren3d = lm.threeDWidget(0).threeDView().renderWindow().GetRenderers().GetItemAsObject(0)
    # actors = ren3d.GetActors()
    # for index in range(actors.GetNumberOfItems()):
    #    ren.AddActor(actors.GetItemAsObject(index))
    # lights = ren3d.GetLights()
    # for index in range(lights.GetNumberOfItems()):
    #    ren.AddLight(lights.GetItemAsObject(index))
    volumes = ren3d.GetVolumes()
    for index in range(volumes.GetNumberOfItems()):
        ren.AddVolume(volumes.GetItemAsObject(index))
    camera = ren3d.GetActiveCamera()
    ren.SetActiveCamera(camera)

    rw.AddRenderer(ren)
    rw.Render()

    wti = vtk.vtkWindowToImageFilter()
    wti.SetInput(rw)
    wti.Update()
    writer = vtk.vtkPNGWriter()
    writer.SetInputConnection(wti.GetOutputPort())
    writer.SetFileName("Out/%d.png" % (x-30))
    writer.Update()
    writer.Write()
    i = wti.GetOutput()
</code></pre>

---

## Post #4 by @Michael_Allen (2023-12-10 20:01 UTC)

<p>worth noting that for rotation, 1 slider unit increment is equal to 1 degree change. I haven’t tried with translation but that may not be the case</p>

---
