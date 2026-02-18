# How to get the current ROINode programmingly according to the volume in the volume rendering module?

**Topic ID**: 21540
**Date**: 2022-01-20
**URL**: https://discourse.slicer.org/t/how-to-get-the-current-roinode-programmingly-according-to-the-volume-in-the-volume-rendering-module/21540

---

## Post #1 by @user4 (2022-01-20 06:45 UTC)

<p>Hi,all.<br>
There are three volumes in the volume rendering module and there are three corresponding AnnotationROIs,as follows：<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5111bca141c61259ded1e536014c629c6656d88c.png" data-download-href="/uploads/short-url/bzaFUVSOnbyMN301x3mxlDwu1re.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5111bca141c61259ded1e536014c629c6656d88c.png" alt="image" data-base62-sha1="bzaFUVSOnbyMN301x3mxlDwu1re" width="690" height="129" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">892×168 3.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/786ddcd95604f2b0f5461736bb78505eb5ef4ecb.png" data-download-href="/uploads/short-url/hbmFVfFWuwQuhwUh3Qgv06nRwfx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/786ddcd95604f2b0f5461736bb78505eb5ef4ecb.png" alt="image" data-base62-sha1="hbmFVfFWuwQuhwUh3Qgv06nRwfx" width="690" height="132" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">902×173 3.78 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77c2a7aeaeaf3bee5a446527eef91bc352113c40.png" data-download-href="/uploads/short-url/h5rREF9NKzt47cnGYqDIj8wZVPG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77c2a7aeaeaf3bee5a446527eef91bc352113c40.png" alt="image" data-base62-sha1="h5rREF9NKzt47cnGYqDIj8wZVPG" width="690" height="129" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">899×169 3.83 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
yeah,I want to get the current ROINode,for example right now,I choose the first volume so I get the vtkMRMLAnnotationROINode1 and when I change to select the second volume the ROINode should be vtkMRMLAnnotationROINode2.<br>
Usually, I hard code to get the ROINode but it is not convenient:</p>
<pre><code class="lang-auto"># get the first ROINode
AnnotationROINodeID='vtkMRMLAnnotationROINode1'
roi = slicer.mrmlScene.GetNodeByID(AnnotationROINodeID)

# get the second ROINode
AnnotationROINodeID='vtkMRMLAnnotationROINode2'
roi = slicer.mrmlScene.GetNodeByID(AnnotationROINodeID)
</code></pre>
<p>So,is there a way to get the current roiNode according to the  selected volume?<br>
Thank you in advance for your possible advice!</p>

---

## Post #2 by @mikebind (2022-01-21 19:52 UTC)

<p>This should work for that:</p>
<pre><code class="lang-auto">myVolumeName = 'MRHead' # replace with the displayed name of your volume
volNode = getNode(volumeName) # get the mrml scalar volume node
vrLogic = slicer.modules.volumerendering.logic() #  get the volume rendering module logic
vrDispNode = logic.GetFirstVolumeRenderingDisplayNode(volNode) # get the volume rendering display node 
roiNode = vrDispNode.GetROINode() # get the associated ROI node
</code></pre>
<p>If you have an ROI node and want to know which volume is rendered using that node, you can do this</p>
<pre><code class="lang-auto">vrLogic = slicer.modules.volumerendering.logic()
vrDispNode = logic.GetFirstVolumeRenderingDisplayNodeByROINode(roiNode)
vrDispNode.GetVolumeNode()
</code></pre>
<p>See the documentation here: <a href="https://apidocs.slicer.org/v4.11/classvtkSlicerVolumeRenderingLogic.html" class="inline-onebox">Slicer: vtkSlicerVolumeRenderingLogic Class Reference</a></p>

---

## Post #3 by @user4 (2022-01-27 02:14 UTC)

<p>Thanks Mike,<br>
This is not working and also I have seen the documentation ,still can’t figure it out.<br>
Maybe I am not making myself clear,my end goal is to take screenshots as png files as you helped me before.But when I load a scene.mrml file into Slicer ,there are three volumes.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/6361b1240e43a56935fd5099adf23087fc76c045.png" alt="image" data-base62-sha1="ebazz15flEZCDaglcEQ8oWfUZXn" width="290" height="313"><br>
I have currently designed a GUI like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddcb4fd2cb48d7f98f73dcc1abbe43df14d3ca85.png" data-download-href="/uploads/short-url/vE576bOGrCHrGhdRabnlKdef2Id.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddcb4fd2cb48d7f98f73dcc1abbe43df14d3ca85.png" alt="image" data-base62-sha1="vE576bOGrCHrGhdRabnlKdef2Id" width="690" height="306" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">898×399 16.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I can take screenshots given the necessary parameters ,but <strong>only the first volume</strong>,which means if I select the second volume in volume rendering module and click the eye icon to see it in display area,I still take screenshots in the first volume.So what I what is as follows:<br>
select the second volume and make it displayed:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caddb7a798e3b1e68cadd6db5ed3acc22a3b2a94.png" data-download-href="/uploads/short-url/sWDtxaIChxEEiMwd82ee7r2Xhru.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caddb7a798e3b1e68cadd6db5ed3acc22a3b2a94.png" alt="image" data-base62-sha1="sWDtxaIChxEEiMwd82ee7r2Xhru" width="690" height="135" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">880×173 3.81 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09c9f691cbaa77a56c4b750a87548582c5af67a4.jpeg" data-download-href="/uploads/short-url/1oB0530LhVKlPfp1iv6MlBCe1xi.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09c9f691cbaa77a56c4b750a87548582c5af67a4_2_690x204.jpeg" alt="image" data-base62-sha1="1oB0530LhVKlPfp1iv6MlBCe1xi" width="690" height="204" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09c9f691cbaa77a56c4b750a87548582c5af67a4_2_690x204.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09c9f691cbaa77a56c4b750a87548582c5af67a4.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09c9f691cbaa77a56c4b750a87548582c5af67a4.jpeg 2x" data-dominant-color="1B1C20"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1004×297 29.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is there someway to get the ROINode at the moment I selected the volume or clicked the eye icon to see it?<br>
In other words,at the moment I selected the third volume and clicked the eye icon,the ROINode should change itself.<br>
Thank you for your continued attention on this topic!</p>

---

## Post #4 by @mikebind (2022-01-27 17:30 UTC)

<p>I notice there was a typo in the included code from two posts ago.  I had changed a variable called <code>logic</code> to <code>vrLogic</code> to try to be a little clearer, but I didn’t change it everywhere in the pasted code. Hopefully that’s all that was leading to your errors.</p>
<pre><code class="lang-auto">vrLogic = slicer.modules.volumerendering.logic()

vol1node = getNode('vol1')
vol2node = getNode('vol2')

# Get or create the volume rendering display node for vol1
vrDispNode1 = vrLogic.GetFirstVolumeRenderingDisplayNode(vol1node)
if vrDispNode1 is None:
  # no existing display node, create a new one
  vrDispNode1 = vrLogic.CreateDefaultVolumeRenderingNodes(vol1Node)

# Get or create the volume rendering display node for vol2
vrDispNode2 = vrLogic.GetFirstVolumeRenderingDisplayNode(vol2node)
if vrDispNode2 is None:
  vrDispNode2  = vrLogic.CreateDefaultVolumeRenderingNodes(vol2node)
</code></pre>
<p>Then</p>
<pre><code class="lang-auto"># To show vol2 instead of vol1
vrDispNode1.SetVisibility(0) # hide vol1 rendering
vrDispNode2.SetVisibility(1) # show vol2 rendering</code></pre>

---

## Post #5 by @user4 (2022-01-28 01:17 UTC)

<p>Thanks Mike, it is not about the type error.It seems like if I want the ROINode I have to get the volumeNode by ID or name.<br>
Thank you for your code and help anyway!</p>

---

## Post #6 by @mikebind (2022-01-28 16:27 UTC)

<p>I think I’m not totally clear on what the problem you are running into is.  I thought you were saying that the problem you were having was that the first volume rendering was being captured twice instead of switching to the second volume, so I was showing how to hide one volume rendering and show another.</p>
<p>Separately, once you have a volume rendering display node, you can get the ROI node from that via the <code>GetROINode()</code> method.</p>

---
