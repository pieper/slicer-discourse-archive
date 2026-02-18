# How to programmatically use zoom in and zoom out to properly adjust the volume size of the 3D view?

**Topic ID**: 21886
**Date**: 2022-02-10
**URL**: https://discourse.slicer.org/t/how-to-programmatically-use-zoom-in-and-zoom-out-to-properly-adjust-the-volume-size-of-the-3d-view/21886

---

## Post #1 by @user4 (2022-02-10 06:27 UTC)

<p>Dear all,<br>
Here is the thing I want to do, thank you in advance for any possible help!</p>
<p>With Slicer 4.11,I am using capture screenshot module to record my volume slice along the P-A orientation.<br>
By default, I take a 3D only screenshot like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6f575819b1bf213bf001c5fe9ac963b4bb9bf47.jpeg" data-download-href="/uploads/short-url/uFC4trQWhuUv5tHZww6hdwytsVh.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6f575819b1bf213bf001c5fe9ac963b4bb9bf47_2_690x248.jpeg" alt="image" data-base62-sha1="uFC4trQWhuUv5tHZww6hdwytsVh" width="690" height="248" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6f575819b1bf213bf001c5fe9ac963b4bb9bf47_2_690x248.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6f575819b1bf213bf001c5fe9ac963b4bb9bf47_2_1035x372.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d6f575819b1bf213bf001c5fe9ac963b4bb9bf47_2_1380x496.jpeg 2x" data-dominant-color="88888A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×692 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a69b21acf710a89276c80dbfba30b6e0f4987925.png" alt="image" data-base62-sha1="nLRCVDE9h3R3QHWzHqeVLgrdHwN" width="507" height="469"></p>
<p>When I load this Screenshot.png file into MATLAB or Python, I checked this dimension which is  617x1015x4.There are four channels R,G,B,A so the last dimension is 4 but what I care is the 617x1015,this seems like to be the default display window size.<br>
Under this window size, my slice size is not quite right.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63c16e5d6123343d7b55c18a29fc35511f23ac5e.png" alt="image" data-base62-sha1="eetH133Nsg7fTc7lGr286ImWfDw" width="641" height="396"><br>
The red line rectangle is different from the particular 300x400 dimension in the volume information module as follows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c75ebbedccd6e204ce245c587943bc1a129f250a.png" data-download-href="/uploads/short-url/srHYYwqtT0bMRjlsSBxx3rkjpO2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c75ebbedccd6e204ce245c587943bc1a129f250a.png" alt="image" data-base62-sha1="srHYYwqtT0bMRjlsSBxx3rkjpO2" width="690" height="182" data-dominant-color="F5EFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">885×234 8.47 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I adjust the volume size manually by zooming in or zooming out,for example:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccfc00aa041bcd21a5f9591bab72eb09b0d72096.png" data-download-href="/uploads/short-url/tfnjEHriOexr8PGRZUFj18krzsq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccfc00aa041bcd21a5f9591bab72eb09b0d72096_2_690x475.png" alt="image" data-base62-sha1="tfnjEHriOexr8PGRZUFj18krzsq" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccfc00aa041bcd21a5f9591bab72eb09b0d72096_2_690x475.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccfc00aa041bcd21a5f9591bab72eb09b0d72096.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccfc00aa041bcd21a5f9591bab72eb09b0d72096.png 2x" data-dominant-color="0C0C0E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1034×713 25 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I can get the smaller size but it is too small than 300x400.So in this situation I have to adjust again and again until I load this png file into Python and find the dimesion is 300x400.<br>
Manual adjustment is quite time-comsuming and inefficient.So I am wondering if there is a way to let the volume zoom-in or zoom-out to become an exact size with python code.<br>
I think there maybe a node in the scene.mrml file that controls the size of the volume.<br>
Thank you for your attention and I will be grateful if you can give me some advice!</p>

---

## Post #2 by @lassoan (2022-02-10 20:25 UTC)

<p>You can get the camera as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-vtk-views-renderers-and-cameras">here</a> and then compute the camera parameters as discussed <a href="https://discourse.vtk.org/t/enable-parallel-projection-without-resetting-the-camera/5289/8">here</a>.</p>

---

## Post #3 by @user4 (2022-02-11 05:24 UTC)

<p>Thanks Andras, thank you very much for helping me solve this problem.</p>
<p>While I have never touched the VTK but I remembered you once gave me a VTKTextBook.I looked up this book especailly about the section <strong>3.6 Cameras</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a27ba77778c03b9f3a914c33ffb13c93cccbcd75.jpeg" data-download-href="/uploads/short-url/nboheNt9sodfJJu0of53vUcqKr3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a27ba77778c03b9f3a914c33ffb13c93cccbcd75_2_517x336.jpeg" alt="image" data-base62-sha1="nboheNt9sodfJJu0of53vUcqKr3" width="517" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a27ba77778c03b9f3a914c33ffb13c93cccbcd75_2_517x336.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a27ba77778c03b9f3a914c33ffb13c93cccbcd75_2_775x504.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a27ba77778c03b9f3a914c33ffb13c93cccbcd75_2_1034x672.jpeg 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1121×729 76.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I probably knew the basics after reading several times.I think I am close to the solution if you can help me again!<br>
So I first get the camera according to the Script repository as follows:</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
for threeDViewIndex in range(layoutManager.threeDViewCount) :
  view = layoutManager.threeDWidget(threeDViewIndex).threeDView()
  threeDViewNode = view.mrmlViewNode()
  cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(threeDViewNode)
</code></pre>
<p>Since I just have one ViewNode,</p>
<pre><code class="lang-auto">camera = cameraNode.GetCamera()
</code></pre>
<p>I have sucessfully got the camera<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce525831cc98c5f8ca3be20958b9836e3726af1e.png" data-download-href="/uploads/short-url/trcMqYw6dXrp8XP2uC4miVZyvqS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce525831cc98c5f8ca3be20958b9836e3726af1e.png" alt="image" data-base62-sha1="trcMqYw6dXrp8XP2uC4miVZyvqS" width="517" height="196" data-dominant-color="F6F7F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">768×292 7.57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
According to the VTKbook,I think in general, there are two ways to adjust the camera,one is modifying the camera’s postion while keeping the focal point fixed and another way is to do the opposite.<br>
And I found there are many attributes can be operated but particularly this Zoom method, which changes the camera’s view angle, so that more or less of the scene falls within the view frustum.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22ba0b7199f23ef2a586bec1be9573c6be57a819.png" data-download-href="/uploads/short-url/4XcPDMRrjm6lRur4b3c3STTAfTr.png?dl=1" title="1644549730(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22ba0b7199f23ef2a586bec1be9573c6be57a819.png" alt="1644549730(1)" data-base62-sha1="4XcPDMRrjm6lRur4b3c3STTAfTr" width="517" height="221" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1644549730(1)</span><span class="informations">732×313 7.46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I prefer to use the default settings but just resize the volume to a desired dimension.So I just use the <em>Zoom()</em> method and observed the results.<br>
When I first loaded the scene.mrml file into Slicer,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7afebc4151fc2c84b0212660dc008392b2402d3f.jpeg" data-download-href="/uploads/short-url/hy41cCkwDXMq21E6M1KUH2Oeont.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7afebc4151fc2c84b0212660dc008392b2402d3f_2_690x302.jpeg" alt="image" data-base62-sha1="hy41cCkwDXMq21E6M1KUH2Oeont" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7afebc4151fc2c84b0212660dc008392b2402d3f_2_690x302.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7afebc4151fc2c84b0212660dc008392b2402d3f_2_1035x453.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7afebc4151fc2c84b0212660dc008392b2402d3f_2_1380x604.jpeg 2x" data-dominant-color="8C8B8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×842 258 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
In this situation I need to zoom-out to adjust the dimension and <strong>I assume the zoom-out operation is exacly same with sliding the middle mouse button</strong>,so then I run this single line code:</p>
<pre><code class="lang-auto">camera.Zoom(0.5)
</code></pre>
<p>it produced the result below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25f10b609dd107f4a02b63c14528996cba01fecf.png" data-download-href="/uploads/short-url/5pE6j6r4rFU1kXo3GLpm9y4Ntf1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25f10b609dd107f4a02b63c14528996cba01fecf_2_690x305.png" alt="image" data-base62-sha1="5pE6j6r4rFU1kXo3GLpm9y4Ntf1" width="690" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25f10b609dd107f4a02b63c14528996cba01fecf_2_690x305.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25f10b609dd107f4a02b63c14528996cba01fecf_2_1035x457.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/25f10b609dd107f4a02b63c14528996cba01fecf_2_1380x610.png 2x" data-dominant-color="848485"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×850 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Sadly, I have no idea how to fine-tune the volume size to the desired dimension like 300x400.<br>
I have also seen this <a href="https://discourse.vtk.org/t/enable-parallel-projection-without-resetting-the-camera/5289/8" rel="noopener nofollow ugc">post</a>.But I am confused with the solution there especially I know very little about VTK.</p>
<pre><code class="lang-auto">ParallelScale = 2*(Distance*tan(0.5*ViewAngle))
</code></pre>
<p>Does Slicer use the orthographic projection (or parallel projection) as default?<br>
How to caculate between the distance and viewAngle in order to get the desired dimension(300x400 in my case)<br>
I would really appreciate it if you could give me some concrete code to illustrate the problem.<br>
Thank you in advance!</p>

---

## Post #4 by @lassoan (2022-02-11 05:54 UTC)

<p>I think what you miss is the volume’s size and location. You can get that information from the volume bounds (specified in the renderer coordinate system):</p>
<pre><code class="lang-auto">bounds=[0,0,0,0,0,0]
getNode('MRHead').GetRASBounds(bounds)
print(bounds)
</code></pre>

---

## Post #5 by @user4 (2022-02-13 05:32 UTC)

<p>Thanks Andras,<br>
I am not trying to switch between perspective and parallel projection that keeps an object the same size within the view but just want to calculate the exact voxel dimension of the volume.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="21886">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>specified in the renderer coordinate system</p>
</blockquote>
</aside>
<p>You are right,I can get the volume bounds which is associated with the ROI range.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cc50f33aac217ad96dca14eb7d2c3a7dcaa91a0.png" alt="image" data-base62-sha1="deG7KJnWyz3yb5sYao8CPC5pmw0" width="468" height="114"><br>
Also,I have these parameters:</p>
<pre><code class="lang-auto">camera = renderer.GetActiveCamera()
angle = math.radians(camera.GetViewAngle())
point = camera.GetFocalPoint()
direction = camera.GetDirectionOfProjection()
scale = camera.GetParallelScale()
distance = scale / math.sin(.5 * angle)
</code></pre>
<p>However,I have no idea how to put all these together to get what I need.<br>
I noticed that I am using the RAS coordinate but what I need is the 2D slice shape(300x400 pixel in my case), in other words,the IJK coordinate .<br>
Is there a simple way just to transfer the RAS to IJK and produce the dimension I need?<br>
I found the related matrix<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/688c4f58b8357a2720a3fef0875671bff570ee0b.png" data-download-href="/uploads/short-url/eUSgIlTNwaHQXFCktAeSqB6hjBh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/688c4f58b8357a2720a3fef0875671bff570ee0b.png" alt="image" data-base62-sha1="eUSgIlTNwaHQXFCktAeSqB6hjBh" width="690" height="86" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">882×110 2.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is it possible to zoom-in or zoom-out in order to change the image dimensions to the below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9120fe64571fbe103f8c8c2016cade170538e214.png" data-download-href="/uploads/short-url/kHRV9U0ii4kkGMyiMLMqExZ2Bog.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9120fe64571fbe103f8c8c2016cade170538e214.png" alt="image" data-base62-sha1="kHRV9U0ii4kkGMyiMLMqExZ2Bog" width="690" height="53" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">889×69 1.93 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you for your continued attention!</p>

---
