# Got the wrong color on the cell

**Topic ID**: 16645
**Date**: 2021-03-19
**URL**: https://discourse.slicer.org/t/got-the-wrong-color-on-the-cell/16645

---

## Post #1 by @jackxiong (2021-03-19 15:26 UTC)

<p>Hi guys,</p>
<p>I’m new to Slicer and VTK library, for some special requirements, I need to set different cell to different color on the surface, so I have such draft code as below:</p>
<pre data-code-wrap="python"><code class="lang-python"># Hide the cube
v = slicer.util.getNode('View1')
v.SetBoxVisible(False)

# Sphere
sphereSource = vtk.vtkSphereSource()
sphereSource.SetCenter(0,0,0)
sphereSource.SetRadius(60.0)
sphereSource.Update()
sphereSource = sphereSource.GetOutput() # vtkPolyData()

# Create a model with the cube and add it to scene
modelNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode')
modelNode.SetAndObservePolyData(sphereSource)
modelNode.CreateDefaultDisplayNodes()
modelNode.SetName('My sphere')

colors = vtk.vtkUnsignedCharArray()
colors.SetName('selection')
colors.SetNumberOfComponents(3)
colors.SetNumberOfTuples(sphereSource.GetNumberOfCells())
for c in range(sphereSource.GetNumberOfCells()):
    #Set color to green, but got red color actually
    colors.SetTuple(c, [0.0, 255.0, 0.0])
sphereSource.GetCellData().SetScalars(colors)

# Set up coloring by selection array
modelNode.GetDisplayNode().SetActiveScalar("selection", vtk.vtkAssignAttribute.CELL_DATA)
modelNode.GetDisplayNode().SetScalarVisibility(True)
</code></pre>
<p>As the above code, I want to set the cell’s color to green, but I got red color actually. I really don’t know what’s wrong with the code.</p>
<p>environment information:</p>
<p>OS:  Win10 x64<br>
3D Slicer version: 4.11.20200930</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5085f899b753b75e5f5332778f490b9f899a61d.png" data-download-href="/uploads/short-url/yXEV1uOGDstmjkcpTYnnQgNZYXX.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5085f899b753b75e5f5332778f490b9f899a61d_2_551x500.png" alt="图片" data-base62-sha1="yXEV1uOGDstmjkcpTYnnQgNZYXX" width="551" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5085f899b753b75e5f5332778f490b9f899a61d_2_551x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5085f899b753b75e5f5332778f490b9f899a61d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5085f899b753b75e5f5332778f490b9f899a61d.png 2x" data-dominant-color="9D87B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">616×558 15.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks a lot for your great help!</p>
<p>Best regards</p>
<p>Jack X.</p>

---

## Post #2 by @lassoan (2021-03-19 15:29 UTC)

<p>See a complete working example for this in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Select_cells_of_a_model_using_markups_fiducial_points">script repository</a>.</p>

---

## Post #3 by @jackxiong (2021-03-22 02:52 UTC)

<p>Thanks a lot for your quick reply. I managed to update the example script and run in my environment, unfortunately, it didn’t solve my problem, my question is: 1. I have markupsNode composed by many points in it, each point has its own attribute(for example, Cardiac mapping point LAT etc.), I want to coloring the closest cell of each point with different color according to the point’s different attribute(maybe the color table is composed by some colors gradient from red to purple or whatever). But seems the example script cannot do it, I got the screenshot as below(each cell coloring with the same color):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6feb87979feef95055f7cc5a67cc9535973b6448.jpeg" data-download-href="/uploads/short-url/fY5Co8KNgLgiFMfJ3mt1yFnWjmE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6feb87979feef95055f7cc5a67cc9535973b6448_2_576x500.jpeg" alt="image" data-base62-sha1="fY5Co8KNgLgiFMfJ3mt1yFnWjmE" width="576" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6feb87979feef95055f7cc5a67cc9535973b6448_2_576x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6feb87979feef95055f7cc5a67cc9535973b6448.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6feb87979feef95055f7cc5a67cc9535973b6448.jpeg 2x" data-dominant-color="9D9B8F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">700×607 92.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I have also update the SetAndObserveColorNodeID()  method’s parameter from “vtkMRMLColorTableNodeWarm1” to other value, it got almost the same result.<br>
are there any solutions for it? look forward to your kindly reply. Thank you so much!</p>

---

## Post #4 by @jackxiong (2021-03-22 08:58 UTC)

<p>Hi Andras, thanks a lot for your quick response. Could you pls check my comments as below. Thanks!</p>

---

## Post #5 by @lassoan (2021-03-24 17:52 UTC)

<p>If you want to show different colors then you have two options:</p>
<ul>
<li>Option A: set different scalar values in the cell data and set colors in the Color node associated with the model</li>
<li>Option B: if you want to assign arbitrary color to each surface patch (that cannot be derived from a single scalar value using a colormap) then set the number of components in the cell data to 3 and specify RGB values (and choose direct mapping scalar mode in the display node)</li>
</ul>

---

## Post #6 by @jackxiong (2021-03-25 00:53 UTC)

<p>Hi Andras, thanks a lot for your help! I will try it.</p>

---

## Post #7 by @SCY (2023-04-25 13:11 UTC)

<p>Hi Andras,<br>
I somehow could not find how to set direct mapping scalar mode in the display node. I am using a model node and try to assign different colors for each point as well. Thank you!</p>

---

## Post #8 by @lassoan (2023-05-02 19:10 UTC)

<p>Please provide a sample data set and your current script and we can have a look.</p>

---

## Post #9 by @SCY (2023-05-03 08:56 UTC)

<p>Thank you for the reply! I found the API I need. It is SetScalarRangeFlag() and sets the flag to UseDirectMapping. Then it shows the specified RGB values(0-255).</p>

---
