---
topic_id: 17735
title: "3D View Interactive Roi Cropping"
date: 2021-05-22
url: https://discourse.slicer.org/t/17735
---

# 3D View interactive ROI Cropping

**Topic ID**: 17735
**Date**: 2021-05-22
**URL**: https://discourse.slicer.org/t/3d-view-interactive-roi-cropping/17735

---

## Post #1 by @spycolyf (2021-05-22 15:48 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6979953ae7b19fdf9d90c8f2415691ab799002b4.png" alt="image" data-base62-sha1="f34CJ3g4E1D3TKs2EULQBSu2jWc" width="462" height="396"></p>
<p>Could you point me to how I can enable interactive 3D cropping on a 3D rendering in 3D view with Python?</p>

---

## Post #2 by @pieper (2021-05-22 16:23 UTC)

<p>Here’s the recipe for finding the code to implement GUI features - it’s very powerful - it will help you better understand the code and find solutions to a lot of questions:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features</a></p>
<p>Also in this case there’s already useful information in the script repository, so its recommended to read through all the snippets there to save time in the future:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#limit-volume-rendering-to-a-specific-region-of-the-volume" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#limit-volume-rendering-to-a-specific-region-of-the-volume</a></p>

---

## Post #3 by @spycolyf (2021-05-22 18:34 UTC)

<p>Thanks you Steve. That’s the best response ever. Teach me to fish. I’ll get my pole and tackle and get to work.</p>
<p><img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji only-emoji" alt=":slight_smile:"></p>

---

## Post #4 by @spycolyf (2021-05-23 20:00 UTC)

<p>OK, I’m trying to get through the docs. I will keep struggling through them, but here’s where I am so far.</p>
<p>I’ve enabled cropping with this code…</p>
<pre><code>   def enable3DCroppingUI(self, volumeNode):

    displayNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLViewNode")

    roiNode = slicer.vtkMRMLAnnotationROINode()
    roiNode.Initialize(slicer.mrmlScene)

    displayNode.SetAndObserveROINodeID(roiNode.GetID())
    displayNode.CroppingEnabled = True
</code></pre>
<p>Here’s what I get.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2daf6265daa98040f152054cebdfe545310afac9.jpeg" alt="image" data-base62-sha1="6w9fdtTwOZ3lfbtrDH0OaLFTUqB" width="320" height="274"></p>
<p>AttributeError: ‘MRMLCore.vtkMRMLViewNode’ object has no attribute ‘SetAndObserveROINodeID’</p>
<p>How do I get it to crop? It seems my ROI and/or cropping is not associated with the rendering. I’m almost there. Shall I play around with the code in the “CropVolumeSelfTest.py” function (found via <a class="mention" href="/u/pieper">@pieper</a> recipe for finding the code)?</p>
<p>I am really excited about displaying this powerful Slicer capability to my physicians this week since they tell me the slice planes rendering is useless. They will be pleasantly surprised I think.</p>

---

## Post #5 by @spycolyf (2021-05-23 21:48 UTC)

<p>This comes up first when I initially turn on cropping. This has to be ROI related I think…</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/340d925ef20b739a3a6530bc2eb35d146344a9ad.jpeg" alt="image" data-base62-sha1="7qtUa06VGdjxIsB1l9jRwRlln3f" width="350" height="312"></p>
<p>Here’s my code…</p>
<pre><code>def enable3DCroppingUI(self, volumeNode):

    roi = slicer.vtkMRMLAnnotationROINode()
    roi.Initialize(slicer.mrmlScene)

    cropVolumeNode = slicer.vtkMRMLCropVolumeParametersNode()
    cropVolumeNode.SetScene(slicer.mrmlScene)

    cropVolumeNode.SetIsotropicResampling(True)
    cropVolumeNode.SetSpacingScalingConst(0.5)
    slicer.mrmlScene.AddNode(cropVolumeNode)

    cropVolumeNode.SetInputVolumeNodeID(volumeNode.GetID())
    cropVolumeNode.SetROINodeID(roi.GetID())

    cropVolumeLogic = slicer.modules.cropvolume.logic()
    cropVolumeLogic.Apply(cropVolumeNode)
</code></pre>

---

## Post #6 by @mau_igna_06 (2021-05-23 22:57 UTC)

<p>I think your displayNode definition is wrong.</p>
<p>I think this could work:</p>
<pre><code class="lang-auto">   def enable3DCroppingUI(self, volumeNode):

    displayNode = slicer.modules.volumerendering.logic().GetFirstVolumeRenderingDisplayNode(volumeNode)

    roiNode = slicer.vtkMRMLAnnotationROINode()
    roiNode.Initialize(slicer.mrmlScene)

    displayNode.SetAndObserveROINodeID(roiNode.GetID())
    displayNode.CroppingEnabled = True
</code></pre>
<p>I don’t know if there are more mistakes in the above code.</p>

---

## Post #7 by @spycolyf (2021-05-24 17:24 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="6" data-topic="17735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>I think your displayNode definition is wrong.</p>
</blockquote>
</aside>
<p>Hello <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>,</p>
<p>Thank you for the response. I tried that and as you implied, there are obviously other mistakes. Do you have or know of other slicer modules that successfully implement 3D cropping?  How do you initially set up your 3D View? My renderings always includes the 3 slice planes. If you can help me to achieve this goal, that would be great.</p>
<p>I’m thinking the slice planes rendering is getting in the way, and maybe the ROI is using it.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05886d8642bbae3a5fb60581ba64a1eee0e6ff47.png" alt="image" data-base62-sha1="MWGk1MMP6zYaDvJIa66MvOYP4z" width="266" height="247"></p>

---

## Post #8 by @jamesobutler (2021-05-24 18:42 UTC)

<p>In your image there you have both the volume rendering shown and also the slice intersections. You need to turn off/on slice intersections as you want. See this example of how to turn on slice intersections. <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#turn-on-slice-intersections" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>

---

## Post #9 by @spycolyf (2021-05-25 22:21 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/pieper">@pieper</a></p>
<p>OK, after 5, 12 hour days in a row, I am still having the most difficult time getting my cropping ROI associated with my 3D View image. Can I pay someone to show look at my code and show me what I’m doing wrong? $$$ Sensing some desperation here? You’re right! This is clearly beyond my threshold of complexity. If you’re interested, we can take this off line and I’ll hire you. mail me at <a href="mailto:knufunk@live.com">knufunk@live.com</a>. This is not necessarily for work, just for my knowledge and then I’ll use my knowledge for work. Consider it a private lesson. An education.</p>
<p>I just want this functionality,</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b175b596f7182f2e1eff63669bb106e9f936802.png" alt="image" data-base62-sha1="aIhQPlMt9E2cJKaWjPJd9nUhFaq" width="408" height="114"></p>
<p>If it can’t be done, please let me know so that I can stop wasting my time. Thanks! <img src="https://emoji.discourse-cdn.com/twitter/expressionless.png?v=12" title=":expressionless:" class="emoji" alt=":expressionless:" loading="lazy" width="20" height="20"></p>

---

## Post #10 by @jamesobutler (2021-05-26 02:38 UTC)

<p>Hi <a class="mention" href="/u/spycolyf">@spycolyf</a>, I don’t know all of your individual requirements, but addressing turning on the VolumeRendering crop ROI for interactive cropping in the 3D View these are the steps for learning how to do this task.</p>
<p>Starting with the Slicer script repository, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#limit-volume-rendering-to-a-specific-region-of-the-volume" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>, provides information about how to use a specific ROI node for cropping in the volume rendering widget.</p>
<p>From this example we learn that we need a VolumeRenderingDisplayNode object to manipulate cropping. From another <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#display-volume-using-volume-rendering" rel="noopener nofollow ugc">Slicer script repository example</a> we learn how to get that object. There are different ways to do this, but I will use this existing example.</p>
<pre><code class="lang-python">logic = slicer.modules.volumerendering.logic()
volumeNode = slicer.mrmlScene.GetNodeByID('vtkMRMLScalarVolumeNode1')
displayNode = logic.CreateVolumeRenderingDisplayNode()
displayNode.UnRegister(logic)
slicer.mrmlScene.AddNode(displayNode)
volumeNode.AddAndObserveDisplayNodeID(displayNode.GetID())
logic.UpdateDisplayNodeFromVolumeNode(displayNode, volumeNode)
</code></pre>
<p>A good method for making sure you get the correct object is to try things out in the Slicer python interactor and examine the type as such. Here we see that we currently have a special type of VolumeRenderingDisplayNode which is specific to GPU rendering and not the CPU type volume rendering. We can see how it inherits thing in its <a href="https://apidocs.slicer.org/master/classvtkMRMLGPURayCastVolumeRenderingDisplayNode.html" rel="noopener nofollow ugc">documentation</a>.</p>
<pre><code class="lang-python">&gt;&gt;&gt; displayNode
(vtkSlicerVolumeRenderingModuleMRML.vtkMRMLGPURayCastVolumeRenderingDisplayNode)000001E46534FB28
</code></pre>
<p>From there a common technique I use is to see what options are available to the object that I have. Therefore I do “displayNode.[TAB]” where pressing the tab key after the dot will break up autocompletion of available methods and attributes for this object. It will show all inherited things as well. When viewing documentation online it usually shows only methods introduced in that object specifically and links to documentation of classes that it inherits. This method of searching is not always efficient, but it allows you to learn to see what is available and to try things out and explore the API.</p>
<p>I can find how to turn on the display node which shows the volume rendering in the 3D view.</p>
<pre><code class="lang-python">displayNode.SetVisibility(True)
</code></pre>
<p>I can also scroll through the autocompletion and find that there is a method for turning on/off cropping.</p>
<pre><code class="lang-python">displayNode.SetCroppingEnabled(True)
</code></pre>
<p>I also find the ROI Node associated with the volume rendering display node for cropping.</p>
<pre><code class="lang-python">&gt;&gt;&gt; displayNode.GetROINode()
(vtkSlicerAnnotationsModuleMRML.vtkMRMLAnnotationROINode)00000180F1134D08
</code></pre>
<p>From here I have learned that the ROI is a vtkMRMLAnnotationROINode type. Now I just need to figure out how to turn the visibility on for that ROI so it can be seen in the 3D view. I can search vtkMRMLAnnotationROINode documentation online or use tab completion on this object to look for methods to turn on visibility. Is it <code>setVisible</code> or <code>VisibilityOn()</code> or <code>SetDisplayVisibility</code>? I can search for methods like this.</p>
<p>I then find that for a vtkMRMLAnnotationROINode it is <code>SetDisplayVisibility</code> that is available and works to show the ROI in all the views including the slice views and 3D view.</p>
<pre><code class="lang-python">displayNode.GetROINode().SetDisplayVisibility(True)
</code></pre>
<p>Putting everything together into a self contained example that can be pasted into the Python interactor upon starting Slicer.</p>
<pre><code class="lang-python">import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
volumeNode= sampleDataLogic.downloadMRHead()

logic = slicer.modules.volumerendering.logic()
displayNode = logic.CreateVolumeRenderingDisplayNode()
displayNode.UnRegister(slicer.mrmlScene)  # See https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MemoryManagement
slicer.mrmlScene.AddNode(displayNode)
volumeNode.AddAndObserveDisplayNodeID(displayNode.GetID())
logic.UpdateDisplayNodeFromVolumeNode(displayNode, volumeNode)

displayNode.SetVisibility(True)  # Volume Rendering shown in 3D view
displayNode.SetCroppingEnabled(True)  # Cropping Enabled
displayNode.GetROINode().SetDisplayVisibility(True)  # Show ROI used for cropping Volume Rendering

</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea989fef1f4a612b516e3ef0a573efd614602e10.jpeg" data-download-href="/uploads/short-url/xtkIXeHJEfEWXmUaqsnZz3VCpTq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ea989fef1f4a612b516e3ef0a573efd614602e10_2_690x370.jpeg" alt="image" data-base62-sha1="xtkIXeHJEfEWXmUaqsnZz3VCpTq" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ea989fef1f4a612b516e3ef0a573efd614602e10_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ea989fef1f4a612b516e3ef0a573efd614602e10_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ea989fef1f4a612b516e3ef0a573efd614602e10_2_1380x740.jpeg 2x" data-dominant-color="7F7F84"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 349 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here I’ve manually rotated the volume in the 3D view and clicked a control point on the ROI to crop the volume rendering.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a11bcaf481dff14ccac8914abaded953058eec7.jpeg" data-download-href="/uploads/short-url/f8kC1BAkbBUbH61aK4QPOnS0uAn.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a11bcaf481dff14ccac8914abaded953058eec7_2_690x370.jpeg" alt="image" data-base62-sha1="f8kC1BAkbBUbH61aK4QPOnS0uAn" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a11bcaf481dff14ccac8914abaded953058eec7_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a11bcaf481dff14ccac8914abaded953058eec7_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a11bcaf481dff14ccac8914abaded953058eec7_2_1380x740.jpeg 2x" data-dominant-color="808085"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 374 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @spycolyf (2021-05-26 15:01 UTC)

<p>Oh wow <a class="mention" href="/u/jamesobutler">@jamesobutler</a>! I am so grateful for your response and for making an attempt to help me out. I show onw physician/Radiologist this functionality in Slicer and he was blown away and said  “Surgical Services would go nuts over this (in a good way).” I continue to be amazed by the lack of awareness of Kitware and Slicer in the medical imaging community. This will definitely expand that awareness here. Anyway, thanks so much for giving me a flashlight if you will. I’m eager to continue this endeavor. I’ll let you know my progress.</p>

---

## Post #12 by @spycolyf (2021-05-26 15:05 UTC)

<p>And thank you for showing  me a little more about how to use the documentation and put things together.</p>

---

## Post #13 by @spycolyf (2021-05-27 15:39 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>Thanks to your response I was able to accomplish what I needed. Soon, I will post instructions describing all that I did to achieve my solution. I think it will help others.</p>
<p>Thanks so much!</p>

---

## Post #14 by @spycolyf (2021-05-27 22:25 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a>,</p>
<p>Hello, do you know a way to reset the cropping ROI back to be fully enclosing as when initally created?</p>
<p>Thanks</p>

---

## Post #15 by @jamesobutler (2021-05-27 22:37 UTC)

<p>You are describing the functionality of the following button in the GUI. Determining how to do this in Python would be a good practice if you haven’t already. I would suggest that you start by searching for the methods available in <code>slicer.modules.volumerendering.logic()</code>. There is a method name in the logic class that should pop out to you for doing this action.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2dce28ae019950b769d52b52802a7ae82e483a6c.jpeg" data-download-href="/uploads/short-url/6xdb8kHiDj7yf4Iubol0KCPkio4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2dce28ae019950b769d52b52802a7ae82e483a6c_2_690x373.jpeg" alt="image" data-base62-sha1="6xdb8kHiDj7yf4Iubol0KCPkio4" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2dce28ae019950b769d52b52802a7ae82e483a6c_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2dce28ae019950b769d52b52802a7ae82e483a6c_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2dce28ae019950b769d52b52802a7ae82e483a6c_2_1380x746.jpeg 2x" data-dominant-color="747477"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 285 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #16 by @spycolyf (2021-05-27 22:57 UTC)

<p>ok thanks! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>

---

## Post #17 by @spycolyf (2021-06-01 20:54 UTC)

<p>Hello <a class="mention" href="/u/jamesobutler">@jamesobutler</a>,</p>
<p>Every advice you gave led me to success. Thanks You so much!</p>
<p>Now there’s one final (I think) thing that need to accomplish and I have sort of working, but it’s not smooth. I’m trying to implement the shift function in the following figure.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b175b596f7182f2e1eff63669bb106e9f936802.png" alt="image" data-base62-sha1="aIhQPlMt9E2cJKaWjPJd9nUhFaq" width="408" height="114"></p>
<p>I’m changing the Gradient Threshold with the value of a slider (0 to 99). But, it’s pretty jerky (not smooth changes). It works best if I slide the slider slowly. What is the proper way to do this in Python? Do I need to add delays in the event handler to give the display time to catch up as I slide?</p>
<p>Here’s my code:</p>
<pre><code>def updateRenderShift(self):

    # Here's where I assign the slider value (0 to 99) to the gradient threshold
    gradientThreshold = self.ui.RenderShiftSlider.value

    maxOpacity = 1.0
    gradientOpacityTransferFunction = self.displayNode.GetVolumePropertyNode().GetVolumeProperty().GetGradientOpacity()
    gradientOpacityTransferFunction.RemoveAllPoints()
    gradientOpacityTransferFunction.AddPoint(0, 0.0)
    gradientOpacityTransferFunction.AddPoint(gradientThreshold-1, 0.0)
    gradientOpacityTransferFunction.AddPoint(gradientThreshold+1, maxOpacity)
</code></pre>

---

## Post #18 by @jamesobutler (2021-06-02 19:22 UTC)

<p>When I change the shift slider as you indicate in your picture when displaying the volume rendering of the MRHead sample data it is smooth for me. What GPU is being used when you observe that it is not smooth?</p>

---

## Post #19 by @lassoan (2021-06-02 19:57 UTC)

<p>You can enter interactive rendering mode when you start moving the slider and exit when you release the slider (this is particularly effective if you use CPU volume rendering, and this is used in Volume rendering module to make the updates smoother).</p>
<p>You can also disable tracking in the slider, which make the slider only generate value changed events when the slider is released.</p>

---

## Post #20 by @spycolyf (2021-06-08 15:38 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>This thread is very long and all over the place. My Bad. How can I extract an earlier part of it to a new topic?</p>
<p>Thanks</p>

---

## Post #21 by @lassoan (2021-06-08 16:11 UTC)

<p>Only administrators can move posts between topics. If you give a list of posts that you want to move out to a separate topic then I can move them for you, but it is probably easier to just create a new topic and include links to relevant posts.</p>

---

## Post #22 by @spycolyf (2021-06-08 17:24 UTC)

<p>Sorry, I’m referring to the SlicerQREADS Development topic. I will post about the extraction to a new topic there…</p>

---

## Post #23 by @spycolyf (2021-06-10 20:25 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="19" data-topic="17735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can enter interactive rendering mode</p>
</blockquote>
</aside>
<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>, what do you mean by “enter interactive rendering mode?”</p>
<p>Thanks</p>

---

## Post #24 by @lassoan (2021-06-10 21:52 UTC)

<p>The renderer (or the interactor) has a flag that temporarily changes the desired update rate while interacting with the view (typically zooming/rotating the view). This results in faster, lower-quality rendering while the view is being rotated and when you release the mouse button then a normal-quality rendering is done. This interactive mode is enabled by the volume rendering offset slider, too. Note that this makes the most difference for CPU volume rendering, which should not be used on modern hardware.</p>

---

## Post #25 by @spycolyf (2021-06-11 06:35 UTC)

<p>OK, new terms; Volume rendering offset slider. Is this a type of widget? Also, shouldn’t the lower-quality rendering mode be enabled automatically for CPU volume rendering? How do you set this flag? What’s the name of it.</p>
<p>Thanks</p>

---

## Post #26 by @lassoan (2021-06-11 17:15 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="25" data-topic="17735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>OK, new terms; Volume rendering offset slider. Is this a type of widget?</p>
</blockquote>
</aside>
<p>I meant the slider labeled as “Shift” (sorry for the confusion with mentioning “offset”):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b92d6709ecda6af424e3a288e11c944e0c2e480b.png" data-download-href="/uploads/short-url/qq9BB7ltUPLkknWW4hc4X3LKv2P.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b92d6709ecda6af424e3a288e11c944e0c2e480b_2_472x500.png" alt="image" data-base62-sha1="qq9BB7ltUPLkknWW4hc4X3LKv2P" width="472" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b92d6709ecda6af424e3a288e11c944e0c2e480b_2_472x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b92d6709ecda6af424e3a288e11c944e0c2e480b_2_708x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b92d6709ecda6af424e3a288e11c944e0c2e480b.png 2x" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">755×799 36.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="spycolyf" data-post="25" data-topic="17735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Also, shouldn’t the lower-quality rendering mode be enabled automatically for CPU volume rendering?</p>
</blockquote>
</aside>
<p>You want to have high-quality volume rendering. You just want to temporarily lower the resolution while you are interactively adjusting parameters. Nowadays average laptops have enough graphics capability that GPU volume rendering is a few times faster than CPU volume rendering (and discrete GPUs are 10-100x faster), so I would recommend using GPU volume rendering by default. Most likely you would run into issues with GPU rendering only if you are trying to render a large, high-resolution CT on a low-performance computer, but there I would recommend to downsample the volume (lower the resolution by a factor of 2x along each axis would results in 8x smaller memory requirement and barely visible image quality loss for volume rendering of a high-resolution volume).</p>
<p>If there are many users with old computers in your organization that would like to volume-render high-resolution volumes then it could worth adding an option to automatically downsample large volumes after loading.</p>
<aside class="quote no-group" data-username="spycolyf" data-post="25" data-topic="17735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>How do you set this flag? What’s the name of it.</p>
</blockquote>
</aside>
<p>You can find source code for a function on the GUI by searching for text that you see in the GUI and then following the references, as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html?highlight=.ui#how-to-find-a-python-function-for-any-slicer-features">this example</a>. I give an example for this “Shift” slider, too:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/search?q=shift+ui">search for <code>shift ui</code> in the Slicer github repository</a> (we add <code>ui</code> to the search terms because most user interface elements are specified in .ui files)</li>
<li>the first search hit has volume rendering in its name and it is a .ui file (<code>qSlicerVolumeRenderingPresetComboBox.ui</code>), so it looks like this is the file we need, <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/VolumeRendering/Resources/UI/qSlicerVolumeRenderingPresetComboBox.ui">click on that link</a></li>
<li>Search for <code>offset</code> in the file and you can find a slider with the name <code>PresetOffsetSlider</code>. This is the name how the slider is referred to in source code. Now you just need to <a href="https://github.com/Slicer/Slicer/search?q=PresetOffsetSlider">search for <code>PresetOffsetSlider</code> in the source code</a>.</li>
<li>Again, the first hit is the correct one. Click on the link to see the file.</li>
<li>Search for <code>PresetOffsetSlider</code> in the file and you can see how interaction events (<code>SliderPressed</code>, <code>SliderReleased</code>, etc. map to methods). You can search for the associated method names <code>startInteraction</code>, <code>endInteraction</code> to see how interactive rendering mode is activated/deactivated:</li>
</ul>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/VolumeRendering/Widgets/qSlicerVolumeRenderingPresetComboBox.cxx#L186-L215">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/VolumeRendering/Widgets/qSlicerVolumeRenderingPresetComboBox.cxx#L186-L215" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/VolumeRendering/Widgets/qSlicerVolumeRenderingPresetComboBox.cxx#L186-L215" target="_blank" rel="noopener">Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/VolumeRendering/Widgets/qSlicerVolumeRenderingPresetComboBox.cxx#L186-L215</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="186" style="counter-reset: li-counter 185 ;">
          <li>void qSlicerVolumeRenderingPresetComboBox::startInteraction()</li>
          <li>{</li>
          <li>  Q_D(qSlicerVolumeRenderingPresetComboBox);</li>
          <li>  if (!d-&gt;VolumePropertyNode)</li>
          <li>    {</li>
          <li>    return;</li>
          <li>    }</li>
          <li></li>
          <li>  vtkVolumeProperty* volumeProperty = d-&gt;VolumePropertyNode-&gt;GetVolumeProperty();</li>
          <li>  if (volumeProperty)</li>
          <li>    {</li>
          <li>    volumeProperty-&gt;InvokeEvent(vtkCommand::StartInteractionEvent);</li>
          <li>    }</li>
          <li>}</li>
          <li></li>
          <li>// --------------------------------------------------------------------------</li>
          <li>void qSlicerVolumeRenderingPresetComboBox::endInteraction()</li>
          <li>{</li>
          <li>  Q_D(qSlicerVolumeRenderingPresetComboBox);</li>
          <li>  if (!d-&gt;VolumePropertyNode)</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/VolumeRendering/Widgets/qSlicerVolumeRenderingPresetComboBox.cxx#L186-L215" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #27 by @spycolyf (2021-06-11 18:08 UTC)

<p>Thank you and yes <a class="mention" href="/u/lassoan">@lassoan</a>. I tried this search method after <a class="mention" href="/u/jamesobutler">@jamesobutler</a> instructed me on how to use the Slicer Code Repo to search for the code. I totally did not know how to do the final translation to Python code. Do I need to create new code on the C++ level, or is there a way to reuse this code? That’s where I got stuck.</p>
<p>Thanks</p>

---

## Post #28 by @lassoan (2021-06-11 18:38 UTC)

<p>You can use the same classes from C++ and Python. There are just a number of trivial syntax differences between Python and C++ that we listed <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#doxygen-style-documentation">here</a>.</p>

---

## Post #29 by @spycolyf (2021-06-18 17:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="26" data-topic="17735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Search for <code>PresetOffsetSlider</code> in the file and you can see how interaction events ( <code>SliderPressed</code> , <code>SliderReleased</code> , etc. map to methods). You can search for the associated method names <code>startInteraction</code> , <code>endInteraction</code> to see how interactive rendering mode is activated/deactivated:</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>OK, just to complete my understanding of how to translate to Python from the C++ I find. I appreciate your patience here and please forgive me for my gap in understanding…</p>
<p>In <strong>qSlicerVolumeRenderingPresetComboBox.cxx</strong> I found the following…</p>
<pre><code class="lang-auto">  QObject::connect(this-&gt;PresetOffsetSlider, SIGNAL(valueChanged(double)),
    q, SLOT(offsetPreset(double)));
  QObject::connect(this-&gt;PresetOffsetSlider, SIGNAL(sliderPressed()),
    q, SLOT(startInteraction()));
  QObject::connect(this-&gt;PresetOffsetSlider, SIGNAL(valueChanged(double)),
    q, SLOT(interaction()));
  QObject::connect(this-&gt;PresetOffsetSlider, SIGNAL(sliderReleased()),
    q, SLOT(endInteraction()));
</code></pre>
<p>From here, do I set up 4 corresponding signal/slot connections in Python? I.e,…</p>
<pre><code class="lang-auto">self.ui.RenderShiftSlider.connect("valueChanged(double)", self.offsetPreset()
self.ui.RenderShiftSlider.connect("sliderPressed", self.startInteraction()
self.ui.RenderShiftSlider.connect("valueChanged(double)", self.interaction()
self.ui.RenderShiftSlider.connect("sliderReleased", self.endInteraction()
</code></pre>
<p>Thanks</p>

---

## Post #30 by @spycolyf (2021-06-18 18:34 UTC)

<p>… and I imagine for example, in this function</p>
<pre><code class="lang-auto">void qSlicerVolumeRenderingPresetComboBox::startInteraction()
{
  Q_D(qSlicerVolumeRenderingPresetComboBox);
  if (!d-&gt;VolumePropertyNode)
    {
    return;
    }

  vtkVolumeProperty* volumeProperty = d-&gt;VolumePropertyNode-&gt;GetVolumeProperty();
  if (volumeProperty)
    {
    volumeProperty-&gt;InvokeEvent(vtkCommand::StartInteractionEvent);
    }
}
</code></pre>
<p>I don’t know how I would somehow invoke the StartInteractionEvent from Python.</p>

---

## Post #31 by @spycolyf (2021-06-18 19:15 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="26" data-topic="17735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>PresetOffsetSlider</code></p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> is using a similar Slider control to change the thickness. But, the only Slot (or event handler) is updateParameterNodeFromGUI</p>
<p><code>self.ui.SlabThicknessSliderWidget.connect("valueChanged(double)", self.updateParameterNodeFromGUI)</code></p>
<p>In updateParameterNodeFromGUI is this staement…</p>
<p><code>self._parameterNode.SetParameter("SlabThicknessInMm", str(self.ui.SlabThicknessSliderWidget.value))</code></p>
<p>… and things magically happen from there.</p>
<p>I guess “SlabThicknessInMm” is a slicer parameter?</p>

---

## Post #32 by @lassoan (2021-06-18 19:16 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="29" data-topic="17735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>From here, do I set up 4 corresponding signal/slot connections in Python? I.e,…</p>
<pre><code class="lang-auto">self.ui.RenderShiftSlider.connect("valueChanged(double)", self.offsetPreset()
</code></pre>
</blockquote>
</aside>
<p>The correct syntax is:</p>
<pre><code class="lang-auto">self.ui.RenderShiftSlider.connect("valueChanged(double)", self.offsetPreset
</code></pre>
<aside class="quote no-group" data-username="spycolyf" data-post="30" data-topic="17735" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>… and I imagine for example, in this function</p>
<pre><code class="lang-auto">void qSlicerVolumeRenderingPresetComboBox::startInteraction()
{
  Q_D(qSlicerVolumeRenderingPresetComboBox);
  if (!d-&gt;VolumePropertyNode)
    {
    return;
    }

  vtkVolumeProperty* volumeProperty = d-&gt;VolumePropertyNode-&gt;GetVolumeProperty();
  if (volumeProperty)
    {
    volumeProperty-&gt;InvokeEvent(vtkCommand::StartInteractionEvent);
    }
}
</code></pre>
</blockquote>
</aside>
<p>It will look something like this in Python:</p>
<pre data-code-wrap="python"><code class="lang-python">def startInteraction(self):
  if not self.VolumePropertyNode:
    return
  volumeProperty = self.VolumePropertyNode.GetVolumeProperty()
  if volumeProperty:
    volumeProperty.InvokeEvent(vtk.vtkCommand.StartInteractionEvent)
</code></pre>
<aside class="quote no-group" data-username="spycolyf" data-post="31" data-topic="17735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>In updateParameterNodeFromGUI is this staement…</p>
<p><code>self._parameterNode.SetParameter("SlabThicknessInMm", str(self.ui.SlabThicknessSliderWidget.value))</code></p>
<p>… and things magically happen from there.</p>
<p>I guess “SlabThicknessInMm” is a slicer parameter?</p>
</blockquote>
</aside>
<p>There is nothing magical, it’s just the GUI and logic are nicely separated. Most likely you have added an observer to the parameter node in your logic class, so if the parameter node changes then a callback function is executed, which updates your view.</p>

---

## Post #33 by @spycolyf (2021-06-18 21:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="32" data-topic="17735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The correct syntax is</p>
</blockquote>
</aside>
<p>here is all of my code…</p>
<pre><code class="lang-auto">   self.OldPresetPosition = 0

   self.ui.RenderShiftSlider.connect("sliderPressed", self.startInteraction)
   self.ui.RenderShiftSlider.connect("valueChanged(double)", self.offsetPreset)
   self.ui.RenderShiftSlider.connect("valueChanged(double)", self.interaction)
   self.ui.RenderShiftSlider.connect("sliderReleased", self.endInteraction)

  def startInteraction(self):
    if not self.displayNode:
      return
    volumeProperty = self.displayNode.GetVolumeProperty()
    if volumeProperty:
      volumeProperty.InvokeEvent(vtk.vtkCommand.StartInteractionEvent)

  def endInteraction(self):
    if not self.displayNode:
      return
    volumeProperty = self.displayNode.GetVolumeProperty()
    if volumeProperty:
      volumeProperty.InvokeEvent(vtk.vtkCommand.EndInteractionEvent)

  def offsetPreset(self,newPosition):
    if not self.displayNode:
      return

    # WRONG SYTAX  emit presetOffsetChanged(newPosition - self.OldPresetPosition, 0., False)

    self.OldPresetPosition = newPosition

  def interaction(self):
    if not self.displayNode:
      return
    volumeProperty = self.displayNode.GetVolumeProperty()
    if volumeProperty:
      volumeProperty.InvokeEvent(vtk.vtkCommand.InteractionEvent)
</code></pre>
<p>In the above code, I’m using the node referencing my volume rendering named  self.displayNode, instead of self.VolumePropertyNode. self.OldPresetPosition is a local variable that keeps track of the old value.</p>
<p>I hope that’s mostly correct, how do I translate …</p>
<p><code>emit presetOffsetChanged(newPosition - self.OldPresetPosition, 0., False)</code></p>
<p>… to Python. What is “emit”?</p>

---

## Post #34 by @lassoan (2021-06-18 21:26 UTC)

<p>“emit” is a Qt keyword, it makes a Qt class emit a signal that can be observed or connected to Qt slots. Since you don’t need to notify anyone about the offset change, you can simply skip this line.</p>

---

## Post #35 by @spycolyf (2021-06-18 22:25 UTC)

<p>Do I replace the it with code that change the render opacity? I’m guessing the presetOffsetChanged or<br>
moveAllPoints code does exactly that…</p>
<p>I found this in the code…</p>
<pre><code class="lang-auto">  QObject::connect(this-&gt;PresetComboBox, SIGNAL(presetOffsetChanged(double, double, bool)),
                   this-&gt;VolumePropertyNodeWidget, SLOT(moveAllPoints(double, double, bool)));
</code></pre>
<p>Shall I implement the moveAllPoints method?</p>

---

## Post #36 by @lassoan (2021-06-18 22:32 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="35" data-topic="17735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>Shall I implement the moveAllPoints method?</p>
</blockquote>
</aside>
<p>Yes, unfortunately this method is implemented at the wrong level (in GUI instead of widget) therefore it cannot be reused but you need to implement it in your own code.</p>

---

## Post #37 by @spycolyf (2021-06-18 22:33 UTC)

<p>… or shall I use this one…</p>
<pre><code class="lang-auto">def updateRenderShift(self):
    gradientThreshold = self.ui.RenderShiftSlider.value
    maxOpacity = 1.0
    gradientOpacityTransferFunction = self.displayNode.GetVolumePropertyNode().GetVolumeProperty().GetGradientOpacity()
    gradientOpacityTransferFunction.RemoveAllPoints()
    gradientOpacityTransferFunction.AddPoint(0, 0.0)
    gradientOpacityTransferFunction.AddPoint(gradientThreshold-1, 0.0)
    gradientOpacityTransferFunction.AddPoint(gradientThreshold+1, maxOpacity)
    self.displayNode.SetVisibility(True)
</code></pre>
<p>Thanks</p>

---

## Post #38 by @lassoan (2021-06-18 22:57 UTC)

<p>Something similar. The code snippet above removes all the points, then creates a new gradient opacity transfer function. If you want to shift an existing preset then you need to iterate through its points of the opacity and color transfer functions and change the x coordinate values of the points.</p>

---

## Post #39 by @spycolyf (2021-06-21 16:44 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> .</p>
<p>For adjusting the x coordinate (gradient threshold), the documentation states…</p>
<pre><code class="lang-auto">  :param gradientThreshold: regions that has gradient value below this threshold will be made transparent
    (minimum value is 0.0, higher values make more tissues transparent, starting with soft tissues)
</code></pre>
<p>Question: What do I use for the max gradientThreshold value? The series max pixel value? If not, then what?</p>
<p>Thanks</p>

---

## Post #40 by @lassoan (2021-06-21 17:01 UTC)

<p>Note that the code snippet above adjusts the gradient opacity transfer function. The offset slider in volume rendering module does not touch the gradient opacity transfer function, just the scalar opacity and color transfer (because the gradient is not sensitive to absolute image intensity changes, so it should not be adjusted along with the two other transfer functions).</p>

---

## Post #41 by @spycolyf (2021-06-22 01:31 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>OK, this function seems to be working. I found a way to expose and use moveAllPoints…</p>
<blockquote>
<pre><code>newPresetPosition = self.ui.RenderShiftSlider.value * self.scalarRange[1] # scalar Range set in showVolumeRendering() function

volumePropertyNodeWidget.moveAllPoints(newPresetPosition - self.OldPresetPosition, 0, False)    
self.OldPresetPosition = newPresetPosition
</code></pre>
</blockquote>
<p>However, my slider values range from 0 to 1.0. MoveAllPoint takes delta value of a range much greater than 0 to 1. Therefore, I’m using the slider value as a scale factor for a bigger range. Here, I am using the  scalar range of the volume as the max. That’s much too big in most cases (CT range from -3500 to 3500).</p>
<p>How can I find exactly what value to multiply by my scalar?</p>
<p>Thanks</p>

---

## Post #42 by @lassoan (2021-06-22 02:43 UTC)

<p>In the volume rendering module, we only use offset to map the transfer functions to a particular volume, and we don’t use scaling. I’m not exactly why this is the case, but most likely because scaling is just not necessary, as you choose a preset based on the scalar range of the image (255 → ultrasound; several hundred → MRI; few thousand → CT) and you adjust the offset to accommodate for small acquisition or patient specific differences. Maybe <a class="mention" href="/u/pieper">@pieper</a> or <a class="mention" href="/u/finetjul">@finetjul</a> remembers why exactly this decision was made.</p>
<p>It could be an interesting study to evaluate the usefulness of applying scaling to the transfer functions - for example, to have “universal” transfer functions that can be applied to multiple modalities. But maybe evaluating and tuning existing presets (and maybe implementing logic for automatically recommending the best preset) for your clinical use cases would make a bigger practical impact.</p>

---

## Post #43 by @pieper (2021-06-22 12:27 UTC)

<p>The Volume Rendering module has evolved over the years based mostly on trial and error, where people have ideas about what might work or inspiration from other programs and try to make something useful.  There are lots of ways it could be improved but no particular formula to indicate which changes will be better for a wide range of images.</p>

---

## Post #44 by @spycolyf (2021-06-22 17:08 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I’m just trying to duplicate exactly how your shift function works in Slicer. But, I can’t determine what exactly VolumePropertyWidget-&gt;moveAllPoints does underneath the hood. Sounds like I’m doing something wrong here. Using your method of searching for code, am I correct by using moveAllPoints to shift?</p>
<p>FYI: My slider is defined exactly like <code>PresetOffsetSlider</code></p>
<p>Thanks</p>

---

## Post #45 by @lassoan (2021-06-22 18:31 UTC)

<p>The offset slider in Volume Rendering module just adds/subtract a value from the x coordinate of thr control points (does not multiply the coordinate with a value).</p>

---
