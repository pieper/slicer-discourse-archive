---
topic_id: 26575
title: "A Problem About Camera Position Setting"
date: 2022-12-05
url: https://discourse.slicer.org/t/26575
---

# A problem about camera position setting

**Topic ID**: 26575
**Date**: 2022-12-05
**URL**: https://discourse.slicer.org/t/a-problem-about-camera-position-setting/26575

---

## Post #1 by @f1oNae (2022-12-05 09:12 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5aab83e2e04fc4dc1fbd3ee2a19bffc44337592c.jpeg" data-download-href="/uploads/short-url/cW6roJW41CYxJBxxzTGF9qKRb5i.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5aab83e2e04fc4dc1fbd3ee2a19bffc44337592c_2_690x488.jpeg" alt="image" data-base62-sha1="cW6roJW41CYxJBxxzTGF9qKRb5i" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5aab83e2e04fc4dc1fbd3ee2a19bffc44337592c_2_690x488.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5aab83e2e04fc4dc1fbd3ee2a19bffc44337592c_2_1035x732.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5aab83e2e04fc4dc1fbd3ee2a19bffc44337592c_2_1380x976.jpeg 2x" data-dominant-color="8284B0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1623×1148 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
When I set the position of cameras,I found that the 3dview disappeared if the position of camera was a little far from the origin.I must interact with the 3dview so that I can get the image,but it will change the picture.</p>
<pre><code class="lang-auto">cam1 = slicer.mrmlScene.GetNodeByID("vtkMRMLCameraNode1")
cam1.SetPosition(0,800,0)
cam2 = slicer.mrmlScene.GetNodeByID("vtkMRMLCameraNode2")
cam2.SetPosition(0,1200,0)
cam3 = slicer.mrmlScene.GetNodeByID("vtkMRMLCameraNode3")
cam3.SetPosition(0,1700,0)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79970aec2dadf230b160e862e9538cc46f2c7970.png" data-download-href="/uploads/short-url/hlDnDT3d1G7CwJV2mNHRxGyiaGc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79970aec2dadf230b160e862e9538cc46f2c7970_2_690x480.png" alt="image" data-base62-sha1="hlDnDT3d1G7CwJV2mNHRxGyiaGc" width="690" height="480" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79970aec2dadf230b160e862e9538cc46f2c7970_2_690x480.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79970aec2dadf230b160e862e9538cc46f2c7970_2_1035x720.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/9/79970aec2dadf230b160e862e9538cc46f2c7970_2_1380x960.png 2x" data-dominant-color="9598CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1634×1137 77 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It’s strange.Can you do me a favour?What’s wrong with this?<br>
How can i solve it?</p>

---

## Post #2 by @RafaelPalomar (2022-12-05 11:37 UTC)

<p><a class="mention" href="/u/f1onae">@f1oNae</a>, after setting the position of the camera, you need to re-compute the clipping range (for reference <a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Libs/MRML/Core/vtkMRMLCameraNode.h#L114-L119" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Libs/MRML/Core/vtkMRMLCameraNode.h#L114-L119</a>)</p>
<p>In python, you could simply do something like this:</p>
<pre><code class="lang-python">cam1 = slicer.mrmlScene.GetNodeByID("vtkMRMLCameraNode1")
cam1.SetPosition(0,800,0)
cam1.ResetClippingRange()
cam2 = slicer.mrmlScene.GetNodeByID("vtkMRMLCameraNode2")
cam2.SetPosition(0,1200,0)
cam2.ResetClippingRange()
cam3 = slicer.mrmlScene.GetNodeByID("vtkMRMLCameraNode3")
cam3.SetPosition(0,1700,0)
cam3.ResetClippingRange()
</code></pre>

---

## Post #3 by @f1oNae (2022-12-05 12:04 UTC)

<p>Thanks a lot.it works!</p>

---
