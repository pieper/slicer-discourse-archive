# Always display annotation or model on top in 3D view

**Topic ID**: 9121
**Date**: 2019-11-13
**URL**: https://discourse.slicer.org/t/always-display-annotation-or-model-on-top-in-3d-view/9121

---

## Post #1 by @Prashant_Pandey (2019-11-13 03:59 UTC)

<p>I’m using volume rendering to show a CT volume being cut with a tracked tool. The scene also contains a sugical target, which is represented by a cylinder model and an annotation ruler. Is it possible to show the model and ruler so that they are always visible, even when ‘occluded’ by the rendering?</p>
<p>I’ve attached two images to show what I mean. In the first one the model and annotation ruler are visible because the rendering is clipped ‘behind’ the target. In the second it’s not possible to see the model/ruler becayse the volume is clipped ‘in front’ of the target. I’ve played around with rendering opacity but this does not provide a good visual of the model unless the opacity is very low.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c7e4bccbf9cdaa732b4585f24081e2ce68bf560.jpeg" data-download-href="/uploads/short-url/aUGSiU0rh065ZUL91sIGtG0L8Qw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c7e4bccbf9cdaa732b4585f24081e2ce68bf560_2_689x372.jpeg" alt="image" data-base62-sha1="aUGSiU0rh065ZUL91sIGtG0L8Qw" width="689" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c7e4bccbf9cdaa732b4585f24081e2ce68bf560_2_689x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c7e4bccbf9cdaa732b4585f24081e2ce68bf560_2_1033x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c7e4bccbf9cdaa732b4585f24081e2ce68bf560.jpeg 2x" data-dominant-color="9A92B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1299×701 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b05d1c403e593db58486e88d82887ffe67eaee7c.jpeg" data-download-href="/uploads/short-url/pabwpHuTTBkWcNYl1bDheKX4HsU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b05d1c403e593db58486e88d82887ffe67eaee7c_2_690x353.jpeg" alt="image" data-base62-sha1="pabwpHuTTBkWcNYl1bDheKX4HsU" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b05d1c403e593db58486e88d82887ffe67eaee7c_2_690x353.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b05d1c403e593db58486e88d82887ffe67eaee7c_2_1035x529.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b05d1c403e593db58486e88d82887ffe67eaee7c.jpeg 2x" data-dominant-color="9E93AF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1271×652 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Prashant_Pandey (2019-11-18 20:45 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Any ideas on how to get started on this?</p>

---

## Post #3 by @lassoan (2019-11-18 21:49 UTC)

<p>You can get access to the VTK actor and change its rendering layer. Of course, the application does not expect such low-level manipulation, so there might be problems with picking, placing points, etc.</p>
<p>In general, I would avoid such 2.5D view modes and use proper 3D and 2D views instead (you can tune cropping and transparency settings to make sure everything important is visible).</p>
<p>For aligning tool with a trajectory you can show simplified axial and side views of just the tool and the trajectory (bullseye and progress views).</p>

---

## Post #4 by @Prashant_Pandey (2019-11-19 00:13 UTC)

<p>Okay thanks. I know it’s not ideal to do this kind of visualization, but the purpose is actually to compare it to more ‘conventional’ views such as 2D bullseye and progress views which we have already implemented.</p>
<p>From my understanding, 3D views are not very useful for precise navigation but rather rough global navigation (unless you have suggestions for what works well in 3D), so I am trying to make these views more ‘useful’ by augmenting with 2D details such as bullseye or the trajectory projection mentioned in the top post.</p>
<p>Is there a brief description or explanation of how to get access to the vtk actor?</p>

---

## Post #5 by @lassoan (2019-11-19 01:03 UTC)

<aside class="quote no-group" data-username="Prashant_Pandey" data-post="4" data-topic="9121">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/c0e974/48.png" class="avatar"> Prashant_Pandey:</div>
<blockquote>
<p>Is there a brief description or explanation of how to get access to the vtk actor?</p>
</blockquote>
</aside>
<p>You can get the model displayable manager as described in this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_displayable_manager_of_a_certain_type_for_a_certain_view">example in the script repository</a>, then get vtkActor corresponding to a model display node.</p>

---

## Post #6 by @pieper (2019-11-19 02:08 UTC)

<p><a class="mention" href="/u/prashant_pandey">@Prashant_Pandey</a> another approach might be to provide a custom shader that cuts away the part of the volume that is obscuring the annotation.  Something like this example: <a href="https://www.youtube.com/watch?v=yiEI_yBMu8k">https://www.youtube.com/watch?v=yiEI_yBMu8k</a> (from <a href="https://github.com/pieper/VTKCustomShaders">these experiments</a>)</p>

---

## Post #7 by @Prashant_Pandey (2019-12-04 20:54 UTC)

<p>I got round to trying your suggestions. After getting the vtkActor for the target model display node, I can’t seem to find a way to change the rendering layer.</p>
<p>I also tried modelDisplayManager.GetRenderer().SetLayer(int), but this didn’t effect the 3D view in the expected way.<br>
Any tips?</p>

---

## Post #8 by @lassoan (2019-12-05 00:31 UTC)

<p>You need to add a new renderer, set its layer, and move the actor to that new renderer. You may need to update the camera of the new renderer based on the camera of the default layer’s renderer. This is all very fragile but may allow you to confirm that this kind of 2.5-dimensional visualization is clinically useful and worthy of spending time with implementing properly.</p>

---

## Post #9 by @Prashant_Pandey (2019-12-06 00:55 UTC)

<p>I added a new renderer with the modelDisplayNode as an actor, and then played around with the new and old renderer’s layers, but with no luck. I did get some interesting views but not what I was looking for:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a6b20c9b42d003d655b22b9eb498fe910cf79f6.jpeg" data-download-href="/uploads/short-url/8kNdh89nVjwztDmsx4HgmAAudLg.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a6b20c9b42d003d655b22b9eb498fe910cf79f6_2_448x500.jpeg" alt="image" data-base62-sha1="8kNdh89nVjwztDmsx4HgmAAudLg" width="448" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a6b20c9b42d003d655b22b9eb498fe910cf79f6_2_448x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a6b20c9b42d003d655b22b9eb498fe910cf79f6_2_672x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a6b20c9b42d003d655b22b9eb498fe910cf79f6.jpeg 2x" data-dominant-color="39251B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">701×781 202 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @lassoan (2019-12-06 01:31 UTC)

<p>You can also display line as 2D actor, which may make it easier to ensure it is above the 3D geometry, without introducing extra renderers or layers.</p>

---

## Post #11 by @Prashant_Pandey (2019-12-10 03:15 UTC)

<p>That sounds like a promising approach.</p>
<p>I could use something like</p>
<pre><code>actor2D = vtk.vtkAxisActor2D()
actor2D.SetPoint1(x1,y1)
actor2D.SetPoint2(x2, y2)
renderer = slicer.app.layoutManager().threeDWidget(0).threeDView().renderWindow().GetRenderers().GetFirstRenderer()
renderer.AddActor2D(actor2D)
</code></pre>
<p>But is there an easy way to calculate the world to display coordinates for the 3D annotation ruler (x1,y1, x2,y2 for the X,Y,Z ruler coordinates)?</p>

---

## Post #12 by @lassoan (2019-12-10 03:35 UTC)

<p>You can convert from world to display like this:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/63e781dafd5a353cb37ca3f32358bdaa46bd4163/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidgetRepresentation3D.cxx#L300-L302" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/63e781dafd5a353cb37ca3f32358bdaa46bd4163/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidgetRepresentation3D.cxx#L300-L302" target="_blank">Slicer/Slicer/blob/63e781dafd5a353cb37ca3f32358bdaa46bd4163/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidgetRepresentation3D.cxx#L300-L302</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="300" style="counter-reset: li-counter 299 ;">
<li>this-&gt;Renderer-&gt;SetWorldPoint(centerPosWorld);</li>
<li>this-&gt;Renderer-&gt;WorldToDisplay();</li>
<li>this-&gt;Renderer-&gt;GetDisplayPoint(centerPosDisplay);</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #13 by @Prashant_Pandey (2019-12-10 20:18 UTC)

<p>Thanks, got it to work! What’s the correct way of adding an oberver to the renderer node? I’d like the 2D line overlay to change if the camera moves or if the viewport size changes for whatever reason.</p>

---

## Post #14 by @lassoan (2019-12-10 20:47 UTC)

<p>Probably you just need to add an observer to the camera.</p>

---

## Post #15 by @Prashant_Pandey (2019-12-10 21:29 UTC)

<p>I ended up adding an observer to the 3D view interactor. Here is the full code for reference:</p>
<pre><code>import numpy as np
layoutManager = slicer.app.layoutManager()
view = layoutManager.threeDWidget(0).threeDView()
renderWindow = view.renderWindow()
renderers = renderWindow.GetRenderers()
renderer = renderers.GetItemAsObject(0)
interactor = slicer.app.layoutManager().threeDWidget(0).threeDView().interactor()

try:
  interactor.RemoveObserver(rendObs)
  renderer.RemoveActor(slicer.lineActor)
  print("Removed Observer")
except:
  pass

slicer.lineActor = vtk.vtkAxisActor2D()
slicer.lineActor.TickVisibilityOff()
slicer.lineActor.SetLabelVisibility(0)
slicer.lineActor.GetProperty().SetLineWidth(2.0)
renderer.AddActor2D(slicer.lineActor)

def onRenderChange(caller, event):
  renderer.SetWorldPoint(56.685, -57.574, -6.521, 1)
  renderer.WorldToDisplay()
  dispPoint1 = renderer.GetDisplayPoint()
  renderer.SetWorldPoint(24.075, -54.898, -8.065, 1)
  renderer.WorldToDisplay()
  dispPoint2 = renderer.GetDisplayPoint()
  viewSize = renderer.GetSize()
  dispPoint1 = list(np.asarray(dispPoint1[:2])/np.asarray(viewSize))
  dispPoint2 = list(np.asarray(dispPoint2[:2])/np.asarray(viewSize))
  slicer.lineActor.SetPoint1(dispPoint1[0], dispPoint1[1])
  slicer.lineActor.SetPoint2(dispPoint2[0], dispPoint2[1])
  print("Render Modified")

rendObs = interactor.AddObserver(vtk.vtkCommand.ModifiedEvent, onRenderChange, 1.0)</code></pre>

---

## Post #16 by @lassoan (2019-12-10 21:30 UTC)

<p>Great! Can you attach a screenshot of the final result?</p>

---

## Post #17 by @Prashant_Pandey (2019-12-10 21:42 UTC)

<p>Here are two screenshots and a video <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47e59b6bfb8cae827d50be1cc984bd7bea28f9c4.jpeg" data-download-href="/uploads/short-url/ag1PxP9qedfRZap7mpT1bzlxHF2.jpeg?dl=1" title="vlcsnap-2019-12-10-13h37m38s145_cr" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47e59b6bfb8cae827d50be1cc984bd7bea28f9c4_2_690x415.jpeg" alt="vlcsnap-2019-12-10-13h37m38s145_cr" data-base62-sha1="ag1PxP9qedfRZap7mpT1bzlxHF2" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47e59b6bfb8cae827d50be1cc984bd7bea28f9c4_2_690x415.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47e59b6bfb8cae827d50be1cc984bd7bea28f9c4_2_1035x622.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47e59b6bfb8cae827d50be1cc984bd7bea28f9c4_2_1380x830.jpeg 2x" data-dominant-color="84738E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vlcsnap-2019-12-10-13h37m38s145_cr</span><span class="informations">1478×890 277 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21dc97a409f2ca44dc547944e468c0d254b836f1.jpeg" data-download-href="/uploads/short-url/4Pyn9x8SkiYncdrxcGTCrkttgHv.jpeg?dl=1" title="vlcsnap-2019-12-10-13h37m23s170" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21dc97a409f2ca44dc547944e468c0d254b836f1_2_690x415.jpeg" alt="vlcsnap-2019-12-10-13h37m23s170" data-base62-sha1="4Pyn9x8SkiYncdrxcGTCrkttgHv" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21dc97a409f2ca44dc547944e468c0d254b836f1_2_690x415.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21dc97a409f2ca44dc547944e468c0d254b836f1_2_1035x622.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/21dc97a409f2ca44dc547944e468c0d254b836f1_2_1380x830.jpeg 2x" data-dominant-color="8A7388"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vlcsnap-2019-12-10-13h37m23s170</span><span class="informations">1480×892 346 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><a href="https://drive.google.com/file/d/1CX13XfZ5j3uCAJVVcUEMdfMtW6TuvFYe/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">2DLineOverlay.mp4 - Google Drive</a></p>

---

## Post #18 by @lassoan (2019-12-11 03:41 UTC)

<p>Thank you, these pictures and video look nice and visibility of the current and planned trajectory are good. I guess the main question if the floating lines still offer enough 3D cues. Maybe you can show the trajectories as true 3D lines (tubes) and make the 2D floating lines semi-transparent. This way you would still have strong 3D cues and keep the trajectories always visible. Keep us updated how well it works!</p>

---

## Post #19 by @Prashant_Pandey (2020-10-22 12:16 UTC)

<p>Here’s an update for you - we published a preliminary study looking at the differences between these views: <a href="https://link.springer.com/chapter/10.1007/978-3-030-60946-7_1" rel="noopener nofollow ugc">https://link.springer.com/chapter/10.1007/978-3-030-60946-7_1</a></p>
<p>Unfortunately the 3D view was still not as promising as some 2D approaches. However when we combined the 3D view with a 2D central bullseye the performance improved. We’re hoping to have a more extensive study completed soon.</p>

---
