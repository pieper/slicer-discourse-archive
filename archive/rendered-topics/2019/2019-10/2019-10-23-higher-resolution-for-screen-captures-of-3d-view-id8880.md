# Higher resolution for screen captures of 3D view?

**Topic ID**: 8880
**Date**: 2019-10-23
**URL**: https://discourse.slicer.org/t/higher-resolution-for-screen-captures-of-3d-view/8880

---

## Post #1 by @nick (2019-10-23 17:23 UTC)

<p>Hello,<br>
I’m wondering if there’s a way to get higher resolution screen captures of the 3D view. I need images of my segmentations with a high enough dpi to print on a poster (about 300 is what I’m thinking). Is there a way to increase the resolution in 3D slicer/export images in some other way? Open to other suggestions as well…<br>
Thanks!<br>
-Nick</p>

---

## Post #2 by @pieper (2019-10-23 17:48 UTC)

<p>The Screen Capture dialog (<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/754a7c424feb16cf0b140dff9418db860d8d16da.png" alt="image" data-base62-sha1="gJBrN40WLkGVJTBITeKPlGrjq7E" width="49" height="42"> has an oversample mode to get higher resolution captures, but we’ve noticed it’s sometimes buggy with the current VTK OpenGL back end for GPU volume rendering, but should be okay for looking at slice views and segmentations, but use CPU if you do volume rendering.  If you haven’t used it before, you can capture the image to the scene, and then save it from the regular Save dialog.</p>
<p>Also for slice visibility in the 3D view can be controlled independently from the 2D views, so you might try working with those options.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5ccbd065326c5623666b5d37e3e7d6abc00507d4.png" alt="image" data-base62-sha1="deUB0jJry9Uj4suvd52ACRDyz8o" width="604" height="267"></p>

---

## Post #3 by @nick (2019-10-23 23:43 UTC)

<p>Thanks for the quick reply! Are you referring to the “sample factor” in this menu? I can’t seem to find the oversample mode…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/304e1db6a7ecde16c456411d5336c2ec2244fbb1.png" data-download-href="/uploads/short-url/6Tkhs21PZuz0Sn1m9Ef4kdl9GzD.png?dl=1" title="03%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/304e1db6a7ecde16c456411d5336c2ec2244fbb1_2_559x500.png" alt="03%20PM" data-base62-sha1="6Tkhs21PZuz0Sn1m9Ef4kdl9GzD" width="559" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/304e1db6a7ecde16c456411d5336c2ec2244fbb1_2_559x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/304e1db6a7ecde16c456411d5336c2ec2244fbb1_2_838x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/304e1db6a7ecde16c456411d5336c2ec2244fbb1.png 2x" data-dominant-color="F4F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">03%20PM</span><span class="informations">920×822 47.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2019-10-24 02:19 UTC)

<p>Yes, I meant <code>Scale factor</code>.  Be careful with it - it rerenders at the magnification you enter, so do like 2 not 100 or it’ll take forever.  Let us know how it goes - fixing this to be more user friendly is on our wishlist.  Like putting a Save As button directly in the dialog, and maybe some feedback about the capture resolution.</p>

---

## Post #5 by @Fernando (2019-10-24 11:02 UTC)

<p>+1 for the Save As button!</p>

---

## Post #6 by @pieper (2019-10-25 23:42 UTC)

<p>Okay, by popular demand, I’ve added a Save As button.  It will be in tomorrow’s preview build.</p>
<p>As mentioned, there are still some problems with the Scale factor that need to be addressed at some point.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd22dc3f29c8e244d577ef2b3af08470d2f49366.png" alt="image" data-base62-sha1="qZaVEkp4rq1EiVCSe4CvU0GGJN4" width="493" height="464"></p>

---

## Post #7 by @lassoan (2019-10-27 17:17 UTC)

<p>If high-resolution screenshots are useful then maybe we could add them to Screen Capture module, too. It would allow us to create high-resolution videos and not just static screenshots.</p>

---

## Post #8 by @pieper (2019-10-27 18:08 UTC)

<p>Murat and I talked about it and the current driving use case was publications, not videos.  But yes, highres videos would be nice too.</p>
<p>The underlying problem right now is that <a href="https://vtk.org/doc/nightly/html/classvtkRenderLargeImage.html">vtkRenderLargeImage</a> doesn’t work well.  I’m not sure it’s the right method anyway, since things like the orientation marker don’t work with it.  Probably making an actual viewer instance of the desired size would cause the least headaches.</p>

---

## Post #9 by @hherhold (2019-10-27 18:23 UTC)

<p>Specifically for poster-size prints, I export models to Blender and then render at whatever resolution I need - I’ve rendered out 5000x5000 and larger. My scene files are typically simple - camera, model, maybe 3 lights (key, fill, kick) and usually very simple surface shaders. Takes a little while to render out, depending on your machine, but it’s very flexible.</p>
<p>I should add that some models I’ve rendered out in Blender are 30 million polys or more. It’s fairly robust.</p>

---

## Post #10 by @hherhold (2019-10-27 18:32 UTC)

<p>Here is an example of a fossil snail shell segmented in 3D Slicer and exported as a model to Blender, then rendered at (I think) 600dpi, (might have been 300dpi?) Anyway, very simple shader, 2 or 3 area lights, black background. With a little knowledge of Blender, it takes a few minutes to set it up.</p>
<p>I’ve been meaning to add this to the list of works using Slicer…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2e1b7d17ac48ab110acb074450cdbf22348e10d.jpeg" data-download-href="/uploads/short-url/rO0e8bXJ4oRGMGf2BhPcCQI24Gx.jpeg?dl=1" title="40%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2e1b7d17ac48ab110acb074450cdbf22348e10d_2_515x500.jpeg" alt="40%20PM" data-base62-sha1="rO0e8bXJ4oRGMGf2BhPcCQI24Gx" width="515" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2e1b7d17ac48ab110acb074450cdbf22348e10d_2_515x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2e1b7d17ac48ab110acb074450cdbf22348e10d_2_772x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2e1b7d17ac48ab110acb074450cdbf22348e10d_2_1030x1000.jpeg 2x" data-dominant-color="4F483D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">40%20PM</span><span class="informations">1240×1202 284 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>From David A. Bullis, Hollister W. Herhold, Jesse E. Czekanski-Moir, David A. Grimaldi, Rebecca J. Rundell, Diverse new tropical land snail species from mid-Cretaceous Burmese amber (Mollusca: Gastropoda: Cyclophoroidea, Assimineidae), Cretaceous Research, 2019, <a href="https://doi.org/10.1016/j.cretres.2019.104267" rel="noopener nofollow ugc">https://doi.org/10.1016/j.cretres.2019.104267</a>.</p>

---

## Post #11 by @muratmaga (2019-10-27 19:42 UTC)

<p>Blender is no doubt a powerful software.</p>
<p>Nevertheless, it doesn’t support voxel data and volume rendering, so you have to have a surface AFAIK.</p>
<p>Second, people have to get familiar with extracting surface, cleaning up/editing meshes understanding issues about polygon format (lack of units in STLs for example). For someone downloading a 3D specimen from morphosource to do comparative anatomy, they will be using 3D Slicer to visualize, segment, etc. Why not do hi-res screen capture within Slicer? All the tools are there. I would be more inclined to support fixing the current issues, so that we can render arbitrarily large still image.  If people want to do a lot more in terms of animation, perhaps they should use Blender. But let’s make sure basic use case is covered sufficiently well in Slicer.</p>
<p>As far as the high-resolution animations, I am not sure if there would be any immediate reason need to render more than 4K, which you can do if your screen resolution supports it. But sure, it would be nice to have that capability too. Between in terms of prioritizing I would say still image capture is more important and immediate need.</p>

---

## Post #12 by @hherhold (2019-10-27 20:15 UTC)

<p>Yep, very good points, and I totally agree on the utility of being able to volume render out to high resolution in Slicer. I only added the Blender suggestion in the interest of time, because it sounded like Nick’s segmentation was complete, and could be exported as models. But I’d love to see high-res capture in Slicer, it would save me many steps. Since Andras added his Lights, for me there are fewer and fewer reasons to export to another program.</p>

---

## Post #13 by @Lorensen (2019-10-27 23:49 UTC)

<p>Does slicer use vtkRenderImage?</p>

---

## Post #14 by @Lorensen (2019-10-27 23:57 UTC)

<p>I meant vtkRenderLargeImage?</p>

---

## Post #15 by @pieper (2019-10-28 17:40 UTC)

<p>Hi Bill - Yes, we use it but it seems to be missing up with the new opengl back end.  It works in Slicer 4.10.2 with old opengl, but in the current nightly with vtk opengl2 not all actors work - cpu ray casting seems to work but not gpu - haven’t yet tried this in pure vtk.</p>

---

## Post #16 by @Fernando (2019-11-27 20:06 UTC)

<p>Hi Steve,</p>
<p>Did the <code>Save as...</code> button ever made it to the build? I can’t see it.</p>

---

## Post #17 by @jamesobutler (2019-11-27 20:37 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>, Indeed it appears you added a new <code>saveAs</code> method in <a href="https://github.com/Slicer/Slicer/commit/17b485e520a821d562e9a7792735b40cd0cdd321" rel="nofollow noopener">https://github.com/Slicer/Slicer/commit/17b485e520a821d562e9a7792735b40cd0cdd321</a><br>
, but you didn’t commit any changes to <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Widgets/Resources/UI/qMRMLScreenShotDialog.ui" rel="nofollow noopener">qMRMLScreenShotDialog.ui</a> for connecting the new method to a GUI object as you showed in the image you posted earlier in this thread.</p>

---

## Post #18 by @pieper (2019-11-27 23:10 UTC)

<p>Oops, sorry, forgot to add that part.  Just committed it.</p>
<p><a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28653" class="onebox" target="_blank">http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28653</a></p>
<p>p.s. thanks for the reminder!</p>

---

## Post #19 by @dmjaffey (2020-12-09 23:12 UTC)

<p>Hi, just wondering if high-res screen capture ever proceeded beyond the discussion of the possibility in this thread.  It’s something I’d want to make use of, if the capability is there.  Thanks,</p>

---

## Post #20 by @muratmaga (2020-12-09 23:38 UTC)

<p>Yes, you can increase the output dimensions by specifying the scaling factor (e.g., if your screen is 1920x1080, scaling x2 would give you a 3840x2160 output). However, make sure you switch to 3D only layout first and use full layout option in screen capture.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afdc248728d24e2c315d6e0e1518b053b7acbce1.png" data-download-href="/uploads/short-url/p5Jd4y5rw3LawbxVMzKRWfyxhL3.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afdc248728d24e2c315d6e0e1518b053b7acbce1_2_523x500.png" alt="image" data-base62-sha1="p5Jd4y5rw3LawbxVMzKRWfyxhL3" width="523" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afdc248728d24e2c315d6e0e1518b053b7acbce1_2_523x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/afdc248728d24e2c315d6e0e1518b053b7acbce1_2_784x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/afdc248728d24e2c315d6e0e1518b053b7acbce1.png 2x" data-dominant-color="484A52"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">918×876 44 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #21 by @aldoSanchez (2021-02-11 01:28 UTC)

<p>do you know some python code for this scale factor</p>

---

## Post #22 by @lassoan (2021-02-11 03:16 UTC)

<p>Full layout is just digital zoom, so it just makes the image bigger but does not improve image quality.</p>
<p>Rendering of individual views actually increases the resolution but it is <a href="https://github.com/Slicer/Slicer/issues/3885">currently broken</a>. Slicer’s VTK version will be upgraded in a couple of weeks, there is a chance that it will fix the high-resolution rendering.</p>

---

## Post #23 by @aldoSanchez (2021-02-11 04:01 UTC)

<p>its any python code for this rendering I’m using the 4.10.2 version because it supports FreeSurferLabel</p>

---

## Post #24 by @aldoSanchez (2021-02-11 04:04 UTC)

<p>also if theres any code for this scale factor (magnification factore) I would like to try it</p>

---

## Post #25 by @lassoan (2021-02-11 04:16 UTC)

<aside class="quote no-group" data-username="aldoSanchez" data-post="23" data-topic="8880" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/5f9b8f/48.png" class="avatar"> aldoSanchez:</div>
<blockquote>
<p>its any python code for this rendering I’m using the 4.10.2 version because it supports FreeSurferLabel</p>
</blockquote>
</aside>
<p>Current Slicer release has this label, too, just install SlicerFreeSurfer extension.</p>
<aside class="quote no-group" data-username="aldoSanchez" data-post="24" data-topic="8880" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/5f9b8f/48.png" class="avatar"> aldoSanchez:</div>
<blockquote>
<p>also if theres any code for this scale factor (magnification factore) I would like to try it</p>
</blockquote>
</aside>
<p>You can use any of the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture">capture code snippets in the script repository</a>. Right now, there is no benefit in using the annotation screenshot tool and adjusting the scaling factor.</p>

---

## Post #26 by @aldoSanchez (2021-02-11 08:56 UTC)

<p>I have this code<br>
#########</p>
<p>viewNodeID = ‘vtkMRMLSliceNodeRed’<br>
import ScreenCapture<br>
cap = ScreenCapture.ScreenCaptureLogic()<br>
view = cap.viewFromNode(slicer.mrmlScene.GetNodeByID(viewNodeID))<br>
cap.captureImageFromView(view,‘C:/Users/aldot/Desktop/python/Red.png’)</p>
<p>#########<br>
but I also want to change the Scale factor lets say to 3 and that information is not  in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture" rel="noopener nofollow ugc">capture code snippets in the script repository</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edef1f3a9dfe93594c8f7df501f5b39e46f2ef30.png" alt="image" data-base62-sha1="xWRtzyRvKVXBf3LTmpylCSNatbi" width="222" height="72"></p>

---

## Post #27 by @lassoan (2021-02-11 17:45 UTC)

<p>We will make sure the scale factor is exposed in Python when scaling gets fixed.</p>

---

## Post #28 by @aldoSanchez (2021-02-11 18:07 UTC)

<p>thanks for your reply.</p>

---

## Post #29 by @dale.fournier (2023-03-19 17:34 UTC)

<p>Hi there. I am interested to rehash this previous forum (RE. exporting high quality images from the 3D view). It is such valuable data to properly showcase.</p>
<p>In the end, does adjusting the “scale factor” remain the only current option? OR have there been any changes since the last post in 2021?</p>
<p>Thanks,<br>
Dale</p>

---

## Post #30 by @pieper (2023-03-19 18:15 UTC)

<p>You made me curious, so I tried <a href="https://kitware.github.io/vtk-examples/site/Cxx/Utilities/OffScreenRendering/">offscreen rendering</a> and it basically works, although it sometimes leads to a crash when interacting with the view after rendering.  But something like the code below could be added as a feature if someone wants to play with it.  It could use more tweaks, but if it’s useful for people we could put it in the script repository for now.</p>
<p>Here’s the full res 5kx5x version:</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1sJh1qNYKqzur0kPGharPd_fLKPXcLjIj/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1sJh1qNYKqzur0kPGharPd_fLKPXcLjIj/view?usp=sharing" target="_blank" rel="noopener">drive.google.com</a>
  </header>

  <article class="onebox-body">
    
<img src="https://lh6.googleusercontent.com/d0vJdufjSyyEtaOhk80i-oF3SGceeIdZ0ZITSkovUXMvn_2StqCGkDK-a-gc8Z-Cveg=w1200-h630-p" class="thumbnail" width="" height="">

<h3><a href="https://drive.google.com/file/d/1sJh1qNYKqzur0kPGharPd_fLKPXcLjIj/view?usp=sharing" target="_blank" rel="noopener">out.png</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e786811920cc3e684ad3f938add3e1a5cc22ce52.jpeg" data-download-href="/uploads/short-url/x2at7QZEtOgPUulGLquLePyQ0G6.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e786811920cc3e684ad3f938add3e1a5cc22ce52_2_500x500.jpeg" alt="image" data-base62-sha1="x2at7QZEtOgPUulGLquLePyQ0G6" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e786811920cc3e684ad3f938add3e1a5cc22ce52_2_500x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e786811920cc3e684ad3f938add3e1a5cc22ce52_2_750x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e786811920cc3e684ad3f938add3e1a5cc22ce52_2_1000x1000.jpeg 2x" data-dominant-color="493E34"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1920 936 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code class="lang-auto">
vtk.vtkGraphicsFactory()
gf = vtk.vtkGraphicsFactory()
gf.SetOffScreenOnlyMode(1)
gf.SetUseMesaClasses(1)
rw = vtk.vtkRenderWindow()
rw.SetOffScreenRendering(1)
ren = vtk.vtkRenderer()
rw.SetSize(5000,5000)

lm = slicer.app.layoutManager()
ren3d = lm.threeDWidget(0).threeDView().renderWindow().GetRenderers().GetItemAsObject(0)
actors = ren3d.GetActors()
for index in range(actors.GetNumberOfItems()):
    ren.AddActor(actors.GetItemAsObject(index))
lights = ren3d.GetLights()
for index in range(lights.GetNumberOfItems()):
    ren.AddLight(lights.GetItemAsObject(index))
volumes = ren3d.GetVolumes()
for index in range(volumes.GetNumberOfItems()):
    ren.AddVolume(volumes.GetItemAsObject(index))
camera = ren3d.GetActiveCamera()
ren.SetActiveCamera(camera)


rw.AddRenderer(ren)
rw.Render()

wti = vtk.vtkWindowToImageFilter()
wti.SetInput(rw)
wti.Update()
writer = vtk.vtkPNGWriter()
writer.SetInputConnection(wti.GetOutputPort())
writer.SetFileName("/tmp/out.png")
writer.Update()
writer.Write()
i = wti.GetOutput()

</code></pre>
<p>Here’s an inset of what the full resolution looks like:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84feaa85766872c302812aa11b5fd27252c517f8.jpeg" alt="image" data-base62-sha1="iYwE24nABrIJBDm4wtXGUgOwDhu" width="565" height="499"></p>

---

## Post #31 by @pieper (2023-03-19 19:38 UTC)

<p>Here’s an example with volume rendering at 5k x 5k:</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1x5I0h_z0AUIkYgvLWO9hAztUgap2LWXi/view?usp=share_link">
  <header class="source">

      <a href="https://drive.google.com/file/d/1x5I0h_z0AUIkYgvLWO9hAztUgap2LWXi/view?usp=share_link" target="_blank" rel="noopener">drive.google.com</a>
  </header>

  <article class="onebox-body">
    
<div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://lh3.googleusercontent.com/zSl2s1UWJkkf49NgxxJJhtMptLnKcP5r5qZ1ySUjFwFzMAmizW0omP_N2xjaxscX36c=w1200-h630-p" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://drive.google.com/file/d/1x5I0h_z0AUIkYgvLWO9hAztUgap2LWXi/view?usp=share_link" target="_blank" rel="noopener">specimin5k.png</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The crashes are because actors are not meant to be shared across render windows like this script does, but for doing one-off renders this works.  If someone wants to give it a shot, integrating off-screen rendering properly with the application wouldn’t be too hard since we know it will work.</p>

---

## Post #32 by @nsvitek (2023-08-07 13:16 UTC)

<p>I’d like to second this question 2.5 years later: is high-resolution screen capture possible? I tried last week and had the same issue described with the scaling factor (increases size, but not resolution). It’s one big thing keeping Slicer from being a complete solution for descriptive research.</p>

---

## Post #33 by @pieper (2023-08-07 14:47 UTC)

<p>Did you try the workaround posted above?</p>

---

## Post #34 by @nsvitek (2023-08-07 16:43 UTC)

<p>I did, twice. I tried before I posted and the program froze. I tried again line by line just now and it did write an image file this time, but the image was 72 kb and completely blank. Admittedly, I’m a novice to Slicer and python is very, very rusty.</p>

---

## Post #35 by @pieper (2023-08-07 18:13 UTC)

<p>It may just take time to render a big image.  That code tries to make a 5k x 5k image and maybe that’s bigger than you need or maybe you can try on a different computer.  I tested on a mac pro with lots of memory.</p>

---

## Post #36 by @nsvitek (2023-08-15 14:32 UTC)

<p>Okay, it’s working now to take the kind of images you included, but there’s one more hurdle I can’t figure out how to overcome:</p>
<p>For a lot of publication-quality imagery, I need a scale bar. I’ve tried modifying your example to change the view node by modifying line 10 into:</p>
<pre><code class="lang-auto">lm = slicer.app.layoutManager()
view = lm.threeDWidget(0).threeDView()
view.mrmlViewNode().SetRenderMode(1)
view.mrmlViewNode().SetRulerType(1)
view.mrmlViewNode().SetRulerColor(2)
ren3d = view.renderWindow().GetRenderers().GetItemAsObject(0)
</code></pre>
<p>And that might change the view I can see in Slicer, but it doesn’t change what gets written to the file. I’ve been trying to follow the code and it seems I’m not properly accessing  what gets added to the vtkRenderer…where do rulers interact with the renderer?</p>

---

## Post #37 by @pieper (2023-08-15 21:56 UTC)

<p>Right, the example I pasted above only transfers some of the basic elements of the rendered scene over to the high res rendering.  The Color Legend and rulers are rendered as overlays so they would need to be added to the script.  I don’t recall, but they may be in dedicated renderers.  It should be possible to add them if you study the vtk code and the slicer displayable managers, but I believe they are rendered in pixel space, meaning they could look very small in the resulting images (this would be a problem in the original scale factor approach too).  If you just need the reference ruler, you might just add a markup line of the reference size and set the thickness so it looks nicer.</p>

---

## Post #38 by @nsvitek (2023-08-31 14:46 UTC)

<p>Thank you for the suggestions. I followed the latter and got it working well enough.</p>
<p>If anyone else is looking to something similar in the future, I modified the example code at the link <a href="https://discourse.slicer.org/t/how-to-draw-a-simple-line-with-vtkmrmlmarkupslinenode/18820">here</a> to create a horizontal markup line of desired size, then ran the rest of the scene rendering / writing code. The line was included in the image and functioned perfectly well as a scale bar.</p>

---

## Post #39 by @JaredAmudeo (2024-09-08 06:43 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="9" data-topic="8880">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>My scene files are typically simple - camera, model, maybe 3 lights (key, fill, kick) and usually very simple surface shaders</p>
</blockquote>
</aside>
<p>How do you do it to be able to export or work with the scale bar when exporting the model and working on it in Blender?</p>

---

## Post #40 by @hherhold (2024-09-08 14:38 UTC)

<p>Hey Jared,</p>
<p>I just DM’d you my “method” for making scale bars in rendered images, let me know if you have any questions. Happy to repost here if people are interested.</p>

---

## Post #41 by @muratmaga (2024-09-08 15:03 UTC)

<p>Fyi, HiResScreenCapture module of slicermorph does this fine.  You may need s preview version of slicer to run it (current stable lake the features we need)</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/Tutorials/blob/main/HiResScreenCapture/readme.md">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/blob/main/HiResScreenCapture/readme.md" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/Tutorials/blob/main/HiResScreenCapture/readme.md" target="_blank" rel="noopener nofollow ugc">SlicerMorph/Tutorials/blob/main/HiResScreenCapture/readme.md</a></h4>


      <pre><code class="lang-md"># HiResScreenCapture Module for SlicerMorph
![HRSCScreenCap.png](HRSCScreenCap.png)
This module is a part of the SlicerMorph extension for 3D Slicer, designed to capture high-resolution screenshots of 3D views within the application. This module is only available for Slicer versions 5.7 or higher, as it relies on some recent changes in core Slicer functionality.

## Usage

1. **Open SlicerMorph:** Launch 3D Slicer and open the SlicerMorph module.

2. **Access the High Resolution Screen Capture Module:**
   - In the SlicerMorph module, navigate to the `Input and Output` dropdown menu.
   - Look for the `HiResScreenCapture` module in the list of available modules.

3. **Configure Settings:**
   - ***Output File**: Specify the path to save the screenshot. You can type the path directly or click `Select Output File` to browse.
   - ***Resolution Scaling Factor**: Use the spin box to set the scaling factor. The range is from 0.1 to 100.0.
   - ***Current 3D Resolution**: Displays the current resolution of the 3D view.
   - ***Expected Screenshot 3D Resolution**: Displays the resolution of the screenshot based on the scaling factor.

4. **Capture Screenshot:** Click `Export Screenshot` to capture the screenshot with the specified settings.
</code></pre>




  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #42 by @pieper (2024-09-08 15:06 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="40" data-topic="8880">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>my “method” for making scale bars in rendered images</p>
</blockquote>
</aside>
<p>It would be great if you could share your method here so that other people (and chatbots) can learn : )</p>

---

## Post #43 by @hherhold (2024-09-29 17:47 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>, Sorry for the delay in writing this up.</p>
<p>My quick overview for making scale bars in images for publication. Note that I pay The Adobe Tax and use Photoshop and Illustrator; this is largely because many of the journals I submit to accept these formats natively. In short, this works for me, it is almost certainly <em>not</em> the best way. (Your mileage may vary.)</p>
<p>Method number 1:</p>
<ol>
<li>Segment your shell (or whatever). Change slicer to Orthogonal view (NOT perspective).</li>
<li>in 3D view, position your model as close as possible to how you’re planning on rendering it in Blender.</li>
<li>Turn on the scale bar in 3D view.</li>
<li>Take a screen capture and keep it as your “reference”.</li>
<li>Export your 3D model and then import into a blender scene.</li>
<li>Change the blender camera to Orthogonal and arrange the view so it is as close as possible to your Slicer reference picture.</li>
<li>Render out to whatever resolution you like and save this as your “rendered” image. This step is a primary reason why I use Blender to do this - I often render 600 dpi images that are over 30" in a single dimension.</li>
<li>In photoshop or Illustrator, load in your reference and rendered images in 2 separate layers. Place your rendered image behind the reference.</li>
<li>Change the opacity of the reference so that you can see the rendered image behind it.</li>
<li>Uniformly scale the reference image until it matches the rendered image.</li>
<li>Make a new layer. With the line tool, draw a scale bar over the scale bar present in the reference image.</li>
<li>make the reference image invisible. You now have a scale bar line that matches the scale. It is arguably not <em>precise</em>, but for most things, it is more than sufficient.</li>
</ol>
<p>Method 2: probably more precise.</p>
<ol>
<li>In Slicer, make a new segment in your segmentation that is a 1x1x1 cube. You’ll have to pick the appropriate units for whatever you’re working on; for me I think I used 1cm on a side. You can do this in code using the python function below; I have this in my .slicerrc.py file.</li>
<li>Export this as a model along with your segmented item (shell, whatever).</li>
<li>Import both of these into blender. You now have something that is of perfect known dimensions in Blender, so you can arrange it as needed to make a scale bar either in Blender or in another application.</li>
</ol>
<p>I generally use method 1 far more often than method 2. I find it to be good enough for my work.</p>
<pre><code class="lang-auto">def CubeSegment(volumeName, segmentationName, segmentName, sizeInMillimeters):
    volumeNode = getNode(volumeName)
    segmentationNode = getNode(segmentationName)
    segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)

    one_unit = round( sizeInMillimeters / volumeNode.GetSpacing()[0] )

    segmentArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId, volumeNode)

    segmentArray[:] = 0
    segmentArray[0:one_unit, 0:one_unit, 0:one_unit] = 1

    slicer.util.updateSegmentBinaryLabelmapFromArray(segmentArray, segmentationNode, segmentId, volumeNode)

</code></pre>

---

## Post #44 by @muratmaga (2024-09-30 03:20 UTC)

<p>Did you try the <a href="https://github.com/SlicerMorph/Tutorials/tree/main/HiResScreenCapture" rel="noopener nofollow ugc">HiResScreenCapture module in SlicerMorph</a> (you need a preview version)?</p>
<p>It may save you a few steps. I went as far as 9000-10000px, but haven’t tried 18000px.</p>

---

## Post #46 by @muratmaga (2024-10-02 03:37 UTC)

<p>One example:</p>
<p><a href="https://js2.jetstream-cloud.org:8001/swift/v1/SampleData/Rendering/molar.png" class="onebox" target="_blank" rel="noopener nofollow ugc">https://js2.jetstream-cloud.org:8001/swift/v1/SampleData/Rendering/molar.png</a></p>

---

## Post #47 by @SDV (2025-06-16 14:44 UTC)

<p>Has this ever been implemented? I would need to export an image series at 4x the resolution of my display.</p>

---

## Post #48 by @pieper (2025-06-16 14:47 UTC)

<p>Yes, it’s in the SlicerMorph extension linked above.</p>

---

## Post #49 by @SDV (2025-06-16 15:00 UTC)

<p>Sorry, with SlicerMorph, I see only the option to export a 3D viewer screenshot at high resolution. I would need the entire image sequence of the 2D views. Is that possible with SlicerMorph?</p>

---

## Post #50 by @pieper (2025-06-16 15:13 UTC)

<p>Did you try the ScreenCapture module?  It should be able to that if you make the slice view big.</p>

---

## Post #51 by @SDV (2025-06-17 08:23 UTC)

<p>Yes I did, and the problem seems that it is limited to the resolution of my monitor, and I would need it to be at 2 or 4x that resolution. In the Screen Capture module I can’t find a Resolution Scaling factor as is present in SlicerMorph.</p>

---

## Post #52 by @pieper (2025-06-17 12:17 UTC)

<p>Okay, I see.  If you need that you’ll need to do a bit of python scripting based on the features of the various modules.</p>

---

## Post #53 by @SDV (2025-06-17 12:26 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> for your reply! Unfortunately that would take a long time with my current programming skills…</p>

---

## Post #54 by @muratmaga (2025-06-17 17:14 UTC)

<p>I am curious why do you need to export your slice views at such high resolution? What’s the use case?</p>

---

## Post #55 by @SDV (2025-06-18 07:07 UTC)

<p>A science-art installation</p>

---

## Post #56 by @muratmaga (2025-06-18 14:49 UTC)

<p>Nice application.</p>
<p>In that case, you will probably better of outputting what layout you want from the screen capture module, and upsampling it in Photoshop to the desired resolution.</p>

---
