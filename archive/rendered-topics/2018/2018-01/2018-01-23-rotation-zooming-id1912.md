# Rotation&zooming 

**Topic ID**: 1912
**Date**: 2018-01-23
**URL**: https://discourse.slicer.org/t/rotation-zooming/1912

---

## Post #1 by @Ahmed_Soufane (2018-01-23 16:13 UTC)

<p>Hello,</p>
<p>How can I modify or call the rotation of an image on the python interactor  on 3dslicer ?</p>
<p>Is it possible to modify or edit zooming in and out of the image on python console ?</p>

---

## Post #2 by @pieper (2018-01-23 17:38 UTC)

<p>here’s a snippet to get the slice logic from the interface:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulate_a_Slice_View" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulate_a_Slice_View</a></p>
<p>Once you have that you can call methods either on the sliceLogic [1] or you can get the sliceNode [2] and call methods like redLogic.GetSliceNode().SetFieldOfView(20,30,1) to change the zoom.</p>
<p>[1] <a href="http://apidocs.slicer.org/master/classvtkMRMLSliceLogic.html">http://apidocs.slicer.org/master/classvtkMRMLSliceLogic.html</a></p>
<p>[2] <a href="http://apidocs.slicer.org/master/classvtkMRMLSliceNode.html">http://apidocs.slicer.org/master/classvtkMRMLSliceNode.html</a></p>

---

## Post #3 by @Ahmed_Soufane (2018-01-27 23:25 UTC)

<p>Hello,<br>
I have tried  redLogic.GetSliceNode().SetFieldOfView(20,30,1) in order to change the zoom, but it did not change anything. I was using the four up view, and the red window turned black when I used redlogic for some reason. How can I use it properly in order to change the zoom ?</p>

---

## Post #4 by @Ahmed_Soufane (2018-01-27 23:33 UTC)

<p>This is what I get when I plug in <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b92485f6df8bd2ad7922373041f122c68df67348.png" data-download-href="/uploads/short-url/qpQA8qLQ1klMSRzz2jFr2uVj2t2.png?dl=1" title="21%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b92485f6df8bd2ad7922373041f122c68df67348_2_690x431.png" alt="21%20PM" data-base62-sha1="qpQA8qLQ1klMSRzz2jFr2uVj2t2" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b92485f6df8bd2ad7922373041f122c68df67348_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b92485f6df8bd2ad7922373041f122c68df67348_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b92485f6df8bd2ad7922373041f122c68df67348_2_1380x862.png 2x" data-dominant-color="827E86"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">21%20PM</span><span class="informations">2880×1800 1.09 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6df1137267ec170a3d724a3b34379bdafbf36ae3.png" data-download-href="/uploads/short-url/fGAxVfkoti3dKTdQr25a1iNLc8H.png?dl=1" title="group__Slicer__QtModules" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6df1137267ec170a3d724a3b34379bdafbf36ae3_2_221x500.png" alt="group__Slicer__QtModules" data-base62-sha1="fGAxVfkoti3dKTdQr25a1iNLc8H" width="221" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6df1137267ec170a3d724a3b34379bdafbf36ae3_2_221x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6df1137267ec170a3d724a3b34379bdafbf36ae3_2_331x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6df1137267ec170a3d724a3b34379bdafbf36ae3.png 2x" data-dominant-color="363636"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">group__Slicer__QtModules</span><span class="informations">331×747 22.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>when I plug in redLogic.SetSliceOffset(10):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b92485f6df8bd2ad7922373041f122c68df67348.png" data-download-href="/uploads/short-url/qpQA8qLQ1klMSRzz2jFr2uVj2t2.png?dl=1" title="21%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b92485f6df8bd2ad7922373041f122c68df67348_2_690x431.png" alt="21%20PM" data-base62-sha1="qpQA8qLQ1klMSRzz2jFr2uVj2t2" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b92485f6df8bd2ad7922373041f122c68df67348_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b92485f6df8bd2ad7922373041f122c68df67348_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b92485f6df8bd2ad7922373041f122c68df67348_2_1380x862.png 2x" data-dominant-color="827E86"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">21%20PM</span><span class="informations">2880×1800 1.09 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I presume that redlogic is controlling the shape of the image and the brightness at the same time one of the windows turned black, instead of controlling the zoom.</p>

---

## Post #5 by @Ahmed_Soufane (2018-01-27 23:38 UTC)

<p>I have figured how it works thanks a lot. However, I do not know how to control the rotation of the image via python interactor ?</p>
<p>Thanks again!</p>

---

## Post #6 by @lassoan (2018-01-28 06:09 UTC)

<blockquote>
<p>I do not know how to control the rotation of the image via python interactor</p>
</blockquote>
<p>Adjust SliceToRAS transform in the slice node. It is a homogeneous transform, so the top-left 3x3 matrix specifies the slice orientation (first column is slice X, second column is slice Y, third column is slice normal direction) and 4th column specifies slice position.</p>

---

## Post #7 by @Ahmed_Soufane (2018-03-06 04:36 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30e75f3d7c3765b00dbbdfc0abcb6a120e82baf6.png" data-download-href="/uploads/short-url/6YCD74T1H47az7oba9XJcrgBICq.png?dl=1" title="20%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30e75f3d7c3765b00dbbdfc0abcb6a120e82baf6_2_690x212.png" alt="20%20PM" data-base62-sha1="6YCD74T1H47az7oba9XJcrgBICq" width="690" height="212" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30e75f3d7c3765b00dbbdfc0abcb6a120e82baf6_2_690x212.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30e75f3d7c3765b00dbbdfc0abcb6a120e82baf6_2_1035x318.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/30e75f3d7c3765b00dbbdfc0abcb6a120e82baf6_2_1380x424.png 2x" data-dominant-color="5A575B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20%20PM</span><span class="informations">2712×834 427 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>As you can see in the attached image whenever I try to execute any different numbers for the x,y and normal slices for the axial view, I do not get to zoom in or out, instead a black image. I believe the problem is I am zooming in a lot, however what I want to know how to control is to zoom in or out of the image itself only via python interactor.</p>

---

## Post #8 by @Ahmed_Soufane (2018-03-06 04:44 UTC)

<p>instead I would like to control the zooming in the following mechanism which can be done by using the mouse.   But, in my case I want to control the zooming mechanism into the image and out of the image like it can be seen on the following images on the 2D yellow image view.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/615f9cd4d143732a9f0bbfffa091a2ac8e58ffbb.png" data-download-href="/uploads/short-url/dTpa9nXpj8arzhCApkIrNjTagoH.png?dl=1" title="23%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/615f9cd4d143732a9f0bbfffa091a2ac8e58ffbb_2_460x500.png" alt="23%20PM" data-base62-sha1="dTpa9nXpj8arzhCApkIrNjTagoH" width="460" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/615f9cd4d143732a9f0bbfffa091a2ac8e58ffbb_2_460x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/615f9cd4d143732a9f0bbfffa091a2ac8e58ffbb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/615f9cd4d143732a9f0bbfffa091a2ac8e58ffbb.png 2x" data-dominant-color="10100E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">23%20PM</span><span class="informations">670×728 11.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2018-03-06 05:20 UTC)

<p>FieldOfView defines the zoom factor. Get the old value, multiply x and y components by a factor (e.g., by 1.1 to zoom out a bit), and set the resulting values as new FOV.</p>

---

## Post #10 by @Ahmed_Soufane (2018-03-07 00:41 UTC)

<p>I tried the same thing you suggested, but the image disappeared and I could not bring it back.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1a501f6ae2bf8f62bb0c7bb0ff14b7f8a10c4dd.png" data-download-href="/uploads/short-url/rD3G6sv7XYRQ9BuwG6FeJX9AqSh.png?dl=1" title="48%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1a501f6ae2bf8f62bb0c7bb0ff14b7f8a10c4dd_2_690x196.png" alt="48%20PM" data-base62-sha1="rD3G6sv7XYRQ9BuwG6FeJX9AqSh" width="690" height="196" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1a501f6ae2bf8f62bb0c7bb0ff14b7f8a10c4dd_2_690x196.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1a501f6ae2bf8f62bb0c7bb0ff14b7f8a10c4dd_2_1035x294.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1a501f6ae2bf8f62bb0c7bb0ff14b7f8a10c4dd_2_1380x392.png 2x" data-dominant-color="626265"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">48%20PM</span><span class="informations">2768×790 487 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @lassoan (2018-03-07 00:58 UTC)

<p>You’ve forgot to get the old FOV value (or at least the screenshot that you attached did not show how you got the old value).</p>

---

## Post #12 by @Ahmed_Soufane (2018-03-07 21:00 UTC)

<p>How do I set the resulting values as new FOV ?</p>

---

## Post #13 by @lassoan (2018-03-11 04:32 UTC)

<p>Use GetFieldOfView method to get current values, scale them, and set the new values using SetFieldOfView.</p>

---
