---
topic_id: 22122
title: "How To Programmatically Split The Rgb Channels And Store The"
date: 2022-02-22
url: https://discourse.slicer.org/t/22122
---

# How to programmatically split the RGB channels and store them separately as a segmentation node

**Topic ID**: 22122
**Date**: 2022-02-22
**URL**: https://discourse.slicer.org/t/how-to-programmatically-split-the-rgb-channels-and-store-them-separately-as-a-segmentation-node/22122

---

## Post #1 by @PhilipDavis (2022-02-22 23:13 UTC)

<p>Hi there,</p>
<p>I’m new to 3D Slicer, as this title mentions, here is a RGB stack TIFF image:<br>
<a href="https://drive.google.com/file/d/1rH9DZPQGbinYuE6T_UYZSeLCWzYd-oE7/view?usp=sharing" rel="noopener nofollow ugc">RGB STACK</a><br>
and now I’d like to implement a procedure in python that splits the RGB channels and converts/stores the RGB channels in the three corresponding segmentation nodes.<br>
The result is similar to the following:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fe2dc1e75c31bf339f1060ef9815df592370788.png" data-download-href="/uploads/short-url/6PCu8tzCuepN2yNb3GGiyGAYmPS.png?dl=1" title="Figure1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fe2dc1e75c31bf339f1060ef9815df592370788_2_345x132.png" alt="Figure1" data-base62-sha1="6PCu8tzCuepN2yNb3GGiyGAYmPS" width="345" height="132" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fe2dc1e75c31bf339f1060ef9815df592370788_2_345x132.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fe2dc1e75c31bf339f1060ef9815df592370788_2_517x198.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fe2dc1e75c31bf339f1060ef9815df592370788_2_690x264.png 2x" data-dominant-color="838484"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Figure1</span><span class="informations">1267×488 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Each channel will be stored in a corresponding segmentation node.<br>
Thank you very much for any specific guidance in advance!</p>

---

## Post #2 by @lassoan (2022-02-23 00:54 UTC)

<p>Segmentations are typically represented as binary labelmap images, so normally you threshold the input scalar (grayscale) image to get the segmentation. Slicer supports fractional labelmaps for segmentations, too, but only a limited set of segmentation tools are supported for those, so I’m not sure if they would work better for you.</p>
<p>I had a look at the image that you provided and the R, G, B components are exactly the same, so what you have is actually single-channel image (the same channel is repeated 3 times).</p>
<p>When I loaded it using the default image loader then only the first component was loaded. So, instead of loading the image using drag-and-drop you can load it as 3 separate volumes using scikit-image using this Python code snippet:</p>
<pre><code class="lang-python">filename = r"c:\Users\andra\Downloads\RGB STACK.tif"

# Install scikit-image
try:
    from skimage import io
except:
    pip_install('scikit-image')
    from skimage import io

# Read the image into numpy array
im = io.imread(filename)

# Create 3 separate volumes
# Useful for segmentation, volume rendering with color mapping, etc.

for component in range(im.shape[3]):
    volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", f"image-c{component}")
    slicer.util.updateVolumeFromArray(volumeNode, im[:,:,:,component])

# Show in slice views
slicer.util.setSliceViewerLayers(background=volumeNode, fit=True)

# Show volume rendering
vrDisplayNode = slicer.modules.volumerendering.logic().CreateDefaultVolumeRenderingNodes(volumeNode)
</code></pre>
<p>You can then create 3 segments from them using thresholding, but I’m not sure if this is really what you want to achieve.</p>
<p>For example, if you want to visualize the image then probably volume rendering is more appropriate. With slight adjustment of the opacity and color transfer function you can get a 3D visualization like this:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1bd0608a3369e45de2aa4f6020b50ae1ed93b41.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1bd0608a3369e45de2aa4f6020b50ae1ed93b41.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1bd0608a3369e45de2aa4f6020b50ae1ed93b41.mp4</a>
    </source></video>
  </div><p></p>
<p>If you acquire volumes that have different data on each channel then you can load it as a single RGB volume like this:</p>
<pre><code class="lang-auto"># Create a single volume
# Useful for actual RGB volumes (that has different values in each channel)
volumeNodeRGB = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLVectorVolumeNode", "image-rgb")
slicer.util.updateVolumeFromArray(volumeNodeRGB, im)
</code></pre>
<p>If you do want to create segmentation (for example, to measure volumes, count objects, etc.) you can create a segmentation from a numpy array as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array">this example</a>.</p>

---

## Post #3 by @PhilipDavis (2022-02-23 03:01 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
Thank you so much for your kind and quick reply!</p>
<blockquote>
<p>I had a look at the image that you provided and the R, G, B components are exactly the same.</p>
</blockquote>
<p>Sorry about that, this image was processed by using FIJI, I re-uploaded a new image and it should be fine now(It now have different data on each channel): <a href="https://drive.google.com/file/d/1IuIFFL9th6D9CxVjfBvgInFlYUbzAoo3/view?usp=sharing" rel="noopener nofollow ugc">RGB STACK2</a></p>
<p>The script you provided are very useful, after I run it, I got 3 volumeNode: image-c0(red), image-c1(green), image-c2(blue). Therefore I see I can take these volume nodes as ‘Master volume’ and create 3 segmentation nodes/segments separately for them:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b027388a2707b169a158a0b78dad8783f2b8f46.png" alt="Figure7" data-base62-sha1="m7hg6IO9aTTwsF0e9upqJRRGxJY" width="490" height="204"></p>
<p>So what need to be add to the script you provided to do this? (<strong>To create 3 separate segmentation nodes/segments for these 3 volume nodes programmatically</strong>)  For example, how to create 3 segmentation nodes with separate thresholds:<br>
Red: 20  Green:30  Blue:40.</p>
<p>Thank you very much!</p>

---

## Post #4 by @lassoan (2022-02-23 06:05 UTC)

<p>This script creates 3 segments by thresholding each channel, displays the segmentation in 3D, and displays the 3 channels as an RGB image:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79c9c5095ba8e4de2943d7e7d9f714d2167075f6.png" data-download-href="/uploads/short-url/hno3VVDZBfywRSEi31QVIbm1zRs.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/79c9c5095ba8e4de2943d7e7d9f714d2167075f6_2_690x420.png" alt="image" data-base62-sha1="hno3VVDZBfywRSEi31QVIbm1zRs" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/79c9c5095ba8e4de2943d7e7d9f714d2167075f6_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/79c9c5095ba8e4de2943d7e7d9f714d2167075f6_2_1035x630.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/79c9c5095ba8e4de2943d7e7d9f714d2167075f6_2_1380x840.png 2x" data-dominant-color="252327"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1375 480 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code class="lang-python"># Inputs
filename = r"c:\Users\andra\OneDrive\Projects\SlicerTesting2022\20220222-Confocal\RGB STACK2.tif"
channelThresholds = [20, 30, 40]

# Install scikit-image
try:
    import skimage
except:
    pip_install('scikit-image')

from skimage import io
import numpy as np

# Read the image into numpy array
im = io.imread(filename)

# Create segments by thresholding each channel

# Create temporary labelmap volume node (it will store the thresholded image that will be imported into the segmentation)
tempLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
tempLabelmapVolumeNode.CreateDefaultDisplayNodes()
# Do not set a color node ID. This will make segment names set based on the labelmap volume's name (instead of looking up the segment name in the color node)
tempLabelmapVolumeNode.GetDisplayNode().SetAndObserveColorNodeID("")

segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
for component in range(im.shape[3]):
    componentImage = im[:,:,:,component]
    componentThreshold = channelThresholds[component]
    thresholdedComponentImage = np.zeros(componentImage.shape)
    thresholdedComponentImage[componentImage &gt; componentThreshold] = 1
    tempLabelmapVolumeNode.SetName(f"Component-{component}")  # the volume node's name will be used as segment name
    slicer.util.updateVolumeFromArray(tempLabelmapVolumeNode, thresholdedComponentImage)
    slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(tempLabelmapVolumeNode, segmentationNode)

slicer.mrmlScene.RemoveNode(tempLabelmapVolumeNode)

# Show segmentation in 3D
segmentationNode.CreateClosedSurfaceRepresentation()
segmentationNode.GetDisplayNode().SetOpacity(0.6)

# Show the image as an RGB volume in slice views
volumeNodeRGB = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLVectorVolumeNode", "image-rgb")
slicer.util.updateVolumeFromArray(volumeNodeRGB, im)
slicer.util.setSliceViewerLayers(background=volumeNodeRGB, fit=True)
</code></pre>

---

## Post #5 by @PhilipDavis (2022-02-23 17:44 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
Thank you very much for your thoughtful guidance!<br>
However, after I run the code you just provided above, only one empty segmentaion node was created, it doesn’t contain three separate segments as shown in the figure you provided, and there are no 3D surfaces showing in the render window :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c3d26fbd2d677733b6e9c837cdfe24fdb078211.png" data-download-href="/uploads/short-url/41Oo0TaI3hIFWOOsMiWKjt4jFUl.png?dl=1" title="Figure10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c3d26fbd2d677733b6e9c837cdfe24fdb078211_2_517x296.png" alt="Figure10" data-base62-sha1="41Oo0TaI3hIFWOOsMiWKjt4jFUl" width="517" height="296" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c3d26fbd2d677733b6e9c837cdfe24fdb078211_2_517x296.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c3d26fbd2d677733b6e9c837cdfe24fdb078211_2_775x444.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c3d26fbd2d677733b6e9c837cdfe24fdb078211_2_1034x592.png 2x" data-dominant-color="C4C4E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Figure10</span><span class="informations">1457×836 32 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<details>
<summary>
the code I am running</summary>
<pre><code class="lang-auto"># Inputs
filename = r"d:\IMAGE\RGB STACK2.tif"
channelThresholds = [20, 30, 40]

# Install scikit-image
try:
    import skimage
except:
    pip_install('scikit-image')

from skimage import io
import numpy as np

# Read the image into numpy array
im = io.imread(filename)

# Create segments by thresholding each channel

# Create temporary labelmap volume node (it will store the thresholded image that will be imported into the segmentation)
tempLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
tempLabelmapVolumeNode.CreateDefaultDisplayNodes()
# Do not set a color node ID. This will make segment names set based on the labelmap volume's name (instead of looking up the segment name in the color node)
tempLabelmapVolumeNode.GetDisplayNode().SetAndObserveColorNodeID("")

segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
for component in range(im.shape[3]):
  componentImage = im[:,:,:,component]
  componentThreshold = channelThresholds[component]
  thresholdedComponentImage = np.zeros(componentImage.shape)
  tempLabelmapVolumeNode.SetName(f"Component-{component}")  # the volume node's name will be used as segment name
  slicer.util.updateVolumeFromArray(tempLabelmapVolumeNode, thresholdedComponentImage)
  slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(tempLabelmapVolumeNode, segmentationNode)

slicer.mrmlScene.RemoveNode(tempLabelmapVolumeNode)

# Show segmentation in 3D
segmentationNode.CreateClosedSurfaceRepresentation()
segmentationNode.GetDisplayNode().SetOpacity(0.6)
</code></pre>
</details>
<p>Could you please point out how to fix it? Since in the next steps I need to apply the logical operator effect to these three segments. Thank you so much!</p>

---

## Post #6 by @lassoan (2022-02-23 17:52 UTC)

<p>Are you using the latest Slicer Preview Release?</p>

---

## Post #7 by @PhilipDavis (2022-02-23 18:48 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
Yes, what I’m using now is the latest Slicer Preview Release for <strong>Windows: 3D Slicer 4.13.0-2022-02-22</strong>:<br>
Or do I need to uninstall all other versions of Slicer just to keep this one?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa90ecc0afad706705d8c0fc4cb07e3832a517b9.png" data-download-href="/uploads/short-url/okTFxkpYsPRLBUJ9E2JFIEBjUDL.png?dl=1" title="Figure11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa90ecc0afad706705d8c0fc4cb07e3832a517b9_2_478x375.png" alt="Figure11" data-base62-sha1="okTFxkpYsPRLBUJ9E2JFIEBjUDL" width="478" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa90ecc0afad706705d8c0fc4cb07e3832a517b9_2_478x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa90ecc0afad706705d8c0fc4cb07e3832a517b9_2_717x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa90ecc0afad706705d8c0fc4cb07e3832a517b9_2_956x750.png 2x" data-dominant-color="C6C7E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Figure11</span><span class="informations">1289×1010 50.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2022-02-23 19:35 UTC)

<p>The Slicer version you are using is good. It seems that I missed a line when I copied the code into the post above. I’ve added the missing line, please try <a href="https://discourse.slicer.org/t/how-to-programmatically-split-the-rgb-channels-and-store-them-separately-as-a-segmentation-node/22122/4">my script</a> again.</p>

---

## Post #9 by @PhilipDavis (2022-02-23 19:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="22122">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>thresholdedComponentImage[componentImage &gt; componentThreshold] = 1</code></p>
</blockquote>
</aside>
<p>Thank you very much for your great guidance! It’s working now <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---
