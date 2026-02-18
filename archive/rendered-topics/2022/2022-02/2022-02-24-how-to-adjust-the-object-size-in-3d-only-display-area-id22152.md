# How to adjust the object size in 3D only display area?

**Topic ID**: 22152
**Date**: 2022-02-24
**URL**: https://discourse.slicer.org/t/how-to-adjust-the-object-size-in-3d-only-display-area/22152

---

## Post #1 by @user4 (2022-02-24 07:55 UTC)

<p>Hi,all.I am struggling with this task,I will be very grateful if anyone can give me some possible advice.<br>
This question is more about <strong>vtk</strong>.<br>
I have a cube(volume) and the information is as follows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9741cf72dd83f8b2a0ef1fc4837580aad36e547.png" data-download-href="/uploads/short-url/sK8K3r6pkPxSDmBZRE7P27wkM8n.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9741cf72dd83f8b2a0ef1fc4837580aad36e547.png" alt="image" data-base62-sha1="sK8K3r6pkPxSDmBZRE7P27wkM8n" width="690" height="72" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">892×94 2.65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebffeff1d56856a4068d6e620faea4ac0e61c62a.png" data-download-href="/uploads/short-url/xFKy12nqpitc40IS3eyH5yqthUu.png?dl=1" title="1645688079(1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebffeff1d56856a4068d6e620faea4ac0e61c62a_2_690x418.png" alt="1645688079(1)" data-base62-sha1="xFKy12nqpitc40IS3eyH5yqthUu" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebffeff1d56856a4068d6e620faea4ac0e61c62a_2_690x418.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebffeff1d56856a4068d6e620faea4ac0e61c62a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebffeff1d56856a4068d6e620faea4ac0e61c62a.png 2x" data-dominant-color="39210C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1645688079(1)</span><span class="informations">1017×617 24.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><em>image dimensions * image spacing = 30,30,40</em>(mm)<br>
So I want to adjust the camera to make sure the size of volume is 30(mm)x30(mm)x40(mm) and also I use the P-A orientation and show the ruler as follows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/119020613697755f201b19d5f3af1b2834c34e33.png" data-download-href="/uploads/short-url/2vmUcPBMYXqqVIG56DoYq0pm7vR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/119020613697755f201b19d5f3af1b2834c34e33.png" alt="image" data-base62-sha1="2vmUcPBMYXqqVIG56DoYq0pm7vR" width="690" height="470" data-dominant-color="251509"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1020×695 3.08 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So my goal is to make sure the rectangle is 30mm by 40 mm in this case.<br>
I can get the camera</p>
<pre><code class="lang-auto">view = slicer.app.layoutManager().threeDWidget(0).threeDView()
renderWindow = view.renderWindow()
renderers = renderWindow.GetRenderers()
renderer = renderers.GetItemAsObject(0)
camera = renderer.GetActiveCamera() 
</code></pre>
<p>Also,I have many parameters</p>
<pre><code class="lang-auto">angle = math.radians(camera.GetViewAngle())
point = camera.GetFocalPoint()
direction = camera.GetDirectionOfProjection()
scale = camera.GetParallelScale()
distance = scale / math.sin(.5 * angle)
</code></pre>
<p>I wonder if there is a way to calculate the width and height of the cube with above parameters and adjust the camera to make the size of the cube become the one I need.</p>
<p>Thank you in advance for your help!<br>
Regards!</p>

---
