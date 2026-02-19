---
topic_id: 20656
title: "Logarithmic Color Scale Bar"
date: 2021-11-17
url: https://discourse.slicer.org/t/20656
---

# Logarithmic Color scale Bar

**Topic ID**: 20656
**Date**: 2021-11-17
**URL**: https://discourse.slicer.org/t/logarithmic-color-scale-bar/20656

---

## Post #1 by @MathiasBrucker (2021-11-17 12:20 UTC)

<p>Slicer version: 4.11.202<br>
Operating system: Windows 10 x64<br>
Software: Jupyter Notebook with Slicer Kernel 4.11</p>
<p>Is it possible to generate a Color Scale Bar with Logarithmic Values.<br>
Since I am working with low distances in the modeltomodeldistance, a logarithmic color scale is needed. With the vtkMRMLProceduralColorNode i can log the LUT colors and the labels are all with the same distances as seen in this picture below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a20bf8d7204a37db7af2b0b0dc1cb8d763952980.png" data-download-href="/uploads/short-url/n7x00FwjUatUIDX0X1MbDSjL7Og.png?dl=1" title="LogarithmicColors" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a20bf8d7204a37db7af2b0b0dc1cb8d763952980_2_690x283.png" alt="LogarithmicColors" data-base62-sha1="n7x00FwjUatUIDX0X1MbDSjL7Og" width="690" height="283" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a20bf8d7204a37db7af2b0b0dc1cb8d763952980_2_690x283.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a20bf8d7204a37db7af2b0b0dc1cb8d763952980_2_1035x424.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a20bf8d7204a37db7af2b0b0dc1cb8d763952980_2_1380x566.png 2x" data-dominant-color="B9C2DC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">LogarithmicColors</span><span class="informations">1859×765 91.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
My question is now to switch the bar and the labels, so the label are logarithmic with low values have a bigger range than higher labels and the color bar with the lut stays in normal range. I tried it with the ProceduralNode and also had a look with at the ColorTableNode but couldn’t figure out how to deal with my problem.<br>
Thanks in advance for dealing with my problem and I am thankful for all the input of the community<br>
Mathias Brucker</p>

---

## Post #2 by @lassoan (2021-11-17 17:57 UTC)

<p><a class="mention" href="/u/mik">@Mik</a> you have been doing a great job in reworking the color bar display. Can you comment on feasibility of logarirthmic scale? Is log scal already supported by the scalar bar widget?</p>

---

## Post #3 by @Mik (2021-11-17 18:44 UTC)

<p>I have not tested it with logarithmic scale it yet. The <a href="https://vtk.org/doc/nightly/html/classvtkScalarBarActor.html" rel="noopener nofollow ugc">ScalarBar</a> manual says that if vtkLookupTable has a logarithmic scale then the labels are created using a logarithmic scale.</p>
<p>Anyway it shouldn’t be to difficult to add a check box and flag to the node to switch between log and linear scale.</p>
<p><a class="mention" href="/u/mathiasbrucker">@MathiasBrucker</a> You can try to set <a href="https://vtk.org/doc/nightly/html/classvtkLookupTable.html#a93a46edc6ca10b0ba0e7cfff4acb52e9" rel="noopener nofollow ugc">log scale</a> to the LUT instead of linear scale.</p>
<p>Do you have any king of test data so i can check the log scale support?</p>

---

## Post #4 by @Mik (2021-11-20 07:28 UTC)

<p>Here what i have got with logarithmic scale<br>
Test LUT</p>
<pre><code class="lang-auto">colorTableNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLProceduralColorNode", "TestLogColors")
colorTableNode.SetType(slicer.vtkMRMLColorTableNode.User)
colorTransferFunction = vtk.vtkDiscretizableColorTransferFunction()
colorTransferFunction.AddRGBPoint(0.01, 1.0, 0.0, 0.0)
colorTransferFunction.AddRGBPoint(0.1, 0.0, 1.0, 0.0)
colorTransferFunction.AddRGBPoint(1.0, 0.3, 0.0, 1.0)
colorTransferFunction.AddRGBPoint(10.0, 0.6, 0.0, 1.0)
colorTransferFunction.AddRGBPoint(100.0, 0.6, 0.6, 1.0)
colorTransferFunction.AddRGBPoint(1000.0, 1., 1., 1.0)
colorTableNode.SetAndObserveColorTransferFunction(colorTransferFunction) 
</code></pre>
<p>LUT screenshot:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/786e27609aceacfa0970a15f3f368e721f40910b.jpeg" data-download-href="/uploads/short-url/hbniATmDrz2CEVdAktNjHbnkett.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/786e27609aceacfa0970a15f3f368e721f40910b_2_690x376.jpeg" alt="image" data-base62-sha1="hbniATmDrz2CEVdAktNjHbnkett" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/786e27609aceacfa0970a15f3f368e721f40910b_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/786e27609aceacfa0970a15f3f368e721f40910b_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/786e27609aceacfa0970a15f3f368e721f40910b_2_1380x752.jpeg 2x" data-dominant-color="6C666E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1047 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>ColorBarDisplayNode parameters screenshot:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32f7245e9f67b43478eab44169e2d8696217647a.jpeg" data-download-href="/uploads/short-url/7gRn7FuYSzYTzzReY6ok8FgVgts.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/32f7245e9f67b43478eab44169e2d8696217647a_2_690x376.jpeg" alt="image" data-base62-sha1="7gRn7FuYSzYTzzReY6ok8FgVgts" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/32f7245e9f67b43478eab44169e2d8696217647a_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/32f7245e9f67b43478eab44169e2d8696217647a_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/32f7245e9f67b43478eab44169e2d8696217647a_2_1380x752.jpeg 2x" data-dominant-color="6F6A6F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1047 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Unfortunately it still doesn’t work quiet well with Models (the program crashes if the model has already been visible).</p>

---

## Post #5 by @MathiasBrucker (2021-11-22 11:40 UTC)

<p>Thanks <a class="mention" href="/u/mik">@Mik</a> for your reply, I couldn’t test it yet but i will try it with the logarithmic LUT on the color Node.</p>

---
