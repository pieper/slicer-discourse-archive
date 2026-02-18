# Display vtkimage in 2D views

**Topic ID**: 9891
**Date**: 2020-01-21
**URL**: https://discourse.slicer.org/t/display-vtkimage-in-2d-views/9891

---

## Post #1 by @park (2020-01-21 09:20 UTC)

<p>I have a vtkImage data and I would like to display this data in my slicer 2D views</p>
<p>After run this code, I could find node in my Slicer<br>
However, I can not find image in my 2D views</p>
<p>And also, the in volume module the “Auto W/L” and “Threshold” section is deactivated.</p>
<p>This is my code,<br>
Is there any problem?</p>
<pre><code>## read vtk object convert to vtkimage
result_image = hlp.vtk_grid2image("/Users/home/Desktop/Simulation/Simulation/SMA_full_0.vtk")
result_volume = slicer.vtkMRMLScalarVolumeNode()
result_volume.SetAndObserveImageData(result_image)

## image to 2D scene
defaultVolumeDisplayNode = slicer.mrmlScene.CreateNodeByClass("vtkMRMLScalarVolumeDisplayNode")
defaultVolumeDisplayNode.AutoWindowLevelOn()
defaultVolumeDisplayNode.SetVisibility(True)
defaultVolumeDisplayNode.AddWindowLevelPresetFromString("ColdToHotRainbow")
slicer.mrmlScene.AddDefaultNode(defaultVolumeDisplayNode)
result_volume.SetAndObserveDisplayNodeID(defaultVolumeDisplayNode.GetID())
defaultVolumeDisplayNode.SetInputImageDataConnection(result_volume.GetImageDataConnection())

## volume node set name
slicer.mrmlScene.AddNode(result_volume).SetName("simulation_result")</code></pre>

---

## Post #2 by @Alex_Vergara (2020-01-21 09:24 UTC)

<p>You can use this to display any Scalar Volume Node in Slicer</p>
<pre><code class="lang-python">def setSlicerViews(backgroundID, foregroundID):
    mainWindow = slicer.util.mainWindow()
    if mainWindow is not None:
        layoutManager = slicer.app.layoutManager()
        if layoutManager is not None:
            makeSlicerLinkedCompositeNodes()

            slicer.util.setSliceViewerLayers(background=backgroundID, foreground=foregroundID, foregroundOpacity=0.5)

            layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView)
            slicer.util.resetSliceViews()

def makeSlicerLinkedCompositeNodes():
    # Set linked slice views  in all existing slice composite nodes and in the default node
    sliceCompositeNodes = slicer.util.getNodesByClass('vtkMRMLSliceCompositeNode')
    defaultSliceCompositeNode = slicer.mrmlScene.GetDefaultNodeByClass('vtkMRMLSliceCompositeNode')
    if not defaultSliceCompositeNode:
        defaultSliceCompositeNode = slicer.mrmlScene.CreateNodeByClass('vtkMRMLSliceCompositeNode')
        slicer.mrmlScene.AddDefaultNode(defaultSliceCompositeNode)
    for sliceCompositeNode in sliceCompositeNodes:
        sliceCompositeNode.SetLinkedControl(True)
    defaultSliceCompositeNode.SetLinkedControl(True)
</code></pre>

---

## Post #3 by @park (2020-01-27 17:53 UTC)

<p>Thank you Alex</p>
<p>I tried your code, however, it is still not working<br>
In the volume module, the “Auto W/L” and “Threshold” section was still deactivated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb2ab5e22d22fe776f37520c2463e9c72adb714f.gif" data-download-href="/uploads/short-url/qHKNddmy79C6u61bq0WPYKJkfxB.gif?dl=1" title="스크린샷 2020-01-28 오전 2.51.41" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb2ab5e22d22fe776f37520c2463e9c72adb714f_2_589x500.gif" alt="스크린샷 2020-01-28 오전 2.51.41" data-base62-sha1="qHKNddmy79C6u61bq0WPYKJkfxB" width="589" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb2ab5e22d22fe776f37520c2463e9c72adb714f_2_589x500.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb2ab5e22d22fe776f37520c2463e9c72adb714f_2_883x750.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb2ab5e22d22fe776f37520c2463e9c72adb714f.gif 2x" data-dominant-color="E8E8E7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">스크린샷 2020-01-28 오전 2.51.41</span><span class="informations">938×796 49.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-01-27 19:56 UTC)

<aside class="quote no-group" data-username="park" data-post="1" data-topic="9891">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/park/48/5717_2.png" class="avatar"> park:</div>
<blockquote>
<p>“Auto W/L” and “Threshold” section is deactivated</p>
</blockquote>
</aside>
<p>This happens when you don’t have a display node associated with your volume or the volume is invalid (no or empty vtkImageData).</p>
<p>Does calling <code>CreateDefaultDisplayNodes</code> on the volume node after it was added to the scene fix the problem?</p>
<p>Can you show what you have in “Volume Information” section?</p>

---

## Post #5 by @park (2020-01-29 12:28 UTC)

<p>Iassoan, Thank you for your reply</p>
<p>The vtkImageData is not empty because I made a volume rendering scene from this vtkImageData.<br>
(like figure below)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51205b982ce097125ab467926ac8b74106c78882.gif" data-download-href="/uploads/short-url/bzG05cxxAooQcfohfSALzMjkbv4.gif?dl=1" title="스크린샷 2020-01-29 오후 9.25.56" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/51205b982ce097125ab467926ac8b74106c78882_2_690x273.gif" alt="스크린샷 2020-01-29 오후 9.25.56" data-base62-sha1="bzG05cxxAooQcfohfSALzMjkbv4" width="690" height="273" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/51205b982ce097125ab467926ac8b74106c78882_2_690x273.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/51205b982ce097125ab467926ac8b74106c78882_2_1035x409.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/51205b982ce097125ab467926ac8b74106c78882_2_1380x546.gif 2x" data-dominant-color="ADB0D7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">스크린샷 2020-01-29 오후 9.25.56</span><span class="informations">2868×1136 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>And this is my Volume Information</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa7e859ffb5902021aeb2623938dead9d1db03c2.gif" data-download-href="/uploads/short-url/okgf0rLwZpaLPt7abKI8MgVUZNw.gif?dl=1" title="스크린샷 2020-01-29 오후 9.26.16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa7e859ffb5902021aeb2623938dead9d1db03c2_2_690x438.gif" alt="스크린샷 2020-01-29 오후 9.26.16" data-base62-sha1="okgf0rLwZpaLPt7abKI8MgVUZNw" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa7e859ffb5902021aeb2623938dead9d1db03c2_2_690x438.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa7e859ffb5902021aeb2623938dead9d1db03c2_2_1035x657.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa7e859ffb5902021aeb2623938dead9d1db03c2.gif 2x" data-dominant-color="F5F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">스크린샷 2020-01-29 오후 9.26.16</span><span class="informations">1256×798 38.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @Alex_Vergara (2020-01-29 16:04 UTC)

<p>After you do this</p>
<aside class="quote no-group" data-username="park" data-post="1" data-topic="9891">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/park/48/5717_2.png" class="avatar"> park:</div>
<blockquote>
<p>result_volume = slicer.vtkMRMLScalarVolumeNode()</p>
</blockquote>
</aside>
<p>you always need to do</p>
<pre><code class="lang-auto">result_volume.CreateDefaultDisplayNodes()
</code></pre>
<p>as <a class="mention" href="/u/lassoan">@lassoan</a> explained</p>

---

## Post #7 by @lassoan (2020-01-29 17:23 UTC)

<p>Maybe the issue is that a volume rendering display node is created very early and therefore a regular volume display node is not created (since you already have display node). Creating the default scalar volume display node before creating any additional special display nodes should fix the problem.</p>

---

## Post #8 by @park (2020-01-30 02:23 UTC)

<p>Thanks for your reply</p>
<p>As your advise, I added “CreateDefaultDisplayNodes()”<br>
After added that the “Auto W/L” and “Threshold” section was activated</p>
<p>However, when I click the “visibility” in volume model<br>
Slicer program immediately turn off</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75ef44d6046fe3e5d0420f1dee32b44c5f203367.gif" data-download-href="/uploads/short-url/gPiuHQge4w69cFvx6GujIVHXUyj.gif?dl=1" title="스크린샷 2020-01-30 오전 11.18.08" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/75ef44d6046fe3e5d0420f1dee32b44c5f203367_2_690x149.gif" alt="스크린샷 2020-01-30 오전 11.18.08" data-base62-sha1="gPiuHQge4w69cFvx6GujIVHXUyj" width="690" height="149" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/75ef44d6046fe3e5d0420f1dee32b44c5f203367_2_690x149.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/75ef44d6046fe3e5d0420f1dee32b44c5f203367_2_1035x223.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75ef44d6046fe3e5d0420f1dee32b44c5f203367.gif 2x" data-dominant-color="F3F3E9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">스크린샷 2020-01-30 오전 11.18.08</span><span class="informations">1172×254 17.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My code was written like this,<br>
Is there any problem?</p>
<pre><code> ## read vtk object convert to vtkimage
result_image = hlp.vtk_grid2image("/Users/home/Desktop/Simulation/Simulation/SMA_full_0.vtk")
result_volume = slicer.vtkMRMLScalarVolumeNode()
result_volume.SetAndObserveImageData(result_image)
result_volume.SetName("simulation_result")
slicer.mrmlScene.AddNode(result_volume)
result_volume.CreateDefaultDisplayNodes()

## image to 2D scene
displaynode = result_volume.GetScalarVolumeDisplayNode()
displaynode.AutoWindowLevelOff()
displaynode.SetWindowLevelMinMax(10,900)
displaynode.AddWindowLevelPresetFromString("ColdToHotRainbow")
# displaynode.SetInputImageDataConnection(result_volume.GetImageDataConnection())
displaynode.SetVisibility(True)
slicer.mrmlScene.AddDefaultNode(displaynode)
result_volume.SetAndObserveDisplayNodeID(displaynode.GetID())
</code></pre>

---

## Post #9 by @lassoan (2020-01-30 03:54 UTC)

<p>The problem is in these lines:</p>
<aside class="quote no-group quote-modified" data-username="park" data-post="8" data-topic="9891">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/park/48/5717_2.png" class="avatar"> park:</div>
<blockquote>
<p>result_image = hlp.vtk_grid2image(“/Users/home/Desktop/Simulation/Simulation/SMA_full_0.vtk”) result_volume = slicer.vtkMRMLScalarVolumeNode() result_volume.SetAndObserveImageData(result_image)</p>
</blockquote>
</aside>
<p>If you allocate memory in Python then you cannot transfer its ownership to a VTK class. If performance is extremely important and you work with enormous data sets then you may try to manually manage memory, but in general I would recommend to use <code>slicer.util.updateVolumeFromArray</code> to safely copy values from numpy array to vtkImageData in a volume node.</p>

---

## Post #10 by @park (2020-01-30 07:15 UTC)

<p>Finally It is work !!<br>
Thank you</p>
<p>However ,<br>
Why I could not see negative coordinate on this scene ?<br>
Is there any other code do I have to update ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbcc0becf83fcf834cea2ebe0d5c6a9f87c4c503.gif" data-download-href="/uploads/short-url/t4S5QsxQ7a4DRJo3w77FUFZDxPJ.gif?dl=1" title="스크린샷 2020-01-30 오후 4.13.26" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbcc0becf83fcf834cea2ebe0d5c6a9f87c4c503_2_461x500.gif" alt="스크린샷 2020-01-30 오후 4.13.26" data-base62-sha1="t4S5QsxQ7a4DRJo3w77FUFZDxPJ" width="461" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbcc0becf83fcf834cea2ebe0d5c6a9f87c4c503_2_461x500.gif, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbcc0becf83fcf834cea2ebe0d5c6a9f87c4c503.gif 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbcc0becf83fcf834cea2ebe0d5c6a9f87c4c503.gif 2x" data-dominant-color="1C185B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">스크린샷 2020-01-30 오후 4.13.26</span><span class="informations">592×642 62.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code>## read vtk object convert to vtkimage
result_image, pressure = hlp.vtk_grid2image("/Users/home/Desktop/Simulation/Simulation/SMA_full_0.vtk")
dimension = result_image.GetDimensions()
reshapePressure = np.reshape(pressure, (dimension[2]-1,dimension[0]-1, dimension[1]-1))

result_volume = slicer.vtkMRMLScalarVolumeNode()
result_volume.SetAndObserveImageData(result_image)
slicer.util.updateVolumeFromArray(result_volume, reshapePressure)
result_volume.SetName("simulation_result")
slicer.mrmlScene.AddNode(result_volume)
result_volume.CreateDefaultDisplayNodes()

## image to 2D scene
displaynode = result_volume.GetScalarVolumeDisplayNode()
displaynode.AutoWindowLevelOff()
displaynode.SetWindowLevelMinMax(10,900)
displaynode.AddWindowLevelPresetFromString("ColdToHotRainbow")
# displaynode.SetInputImageDataConnection(result_volume.GetImageDataConnection())
displaynode.SetVisibility(True)
slicer.mrmlScene.AddDefaultNode(displaynode)
result_volume.SetAndObserveDisplayNodeID(displaynode.GetID())
</code></pre>

---

## Post #11 by @lassoan (2020-01-30 15:23 UTC)

<aside class="quote no-group" data-username="park" data-post="10" data-topic="9891">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/park/48/5717_2.png" class="avatar"> park:</div>
<blockquote>
<p>Why I could not see negative coordinate on this scene ?</p>
</blockquote>
</aside>
<p>Slice offset slider range is determined from the extent of the displayed background volume. If you have a single-slice volume then you will not be able to move away from it using the slider. You can use <kbd>Shift</kbd> + Mouse Move in other views or set a larger volume as background volume.</p>

---

## Post #12 by @park (2020-01-31 01:47 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="9891">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can use <kbd>Shift</kbd> + Mouse Move in other views or set a larger volume as background volume.</p>
</blockquote>
</aside>
<p>How could I set extent in my volume node or make large background volume?<br>
I already set extent in “vtkimage.SetExtent()” but it seems like not working.</p>

---

## Post #13 by @lassoan (2020-01-31 02:11 UTC)

<aside class="quote no-group" data-username="park" data-post="12" data-topic="9891">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/park/48/5717_2.png" class="avatar"> park:</div>
<blockquote>
<p>I already set extent in “vtkimage.SetExtent()” but it seems like not working.</p>
</blockquote>
</aside>
<p>After calling <code>SetExent()</code> you need to call <code>AllocateScalars</code> (see example <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_new_volume">here</a>). Of course reallocation clears current image content, so if you want to keep the image content then create a new image and resample the old image into that (an implementation of this is available in “Crop volume” module).</p>

---
