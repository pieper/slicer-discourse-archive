---
topic_id: 35813
title: "How To Include Markup Annotations In High Resolution Screen"
date: 2024-04-29
url: https://discourse.slicer.org/t/35813
---

# How to include markup annotations in high-resolution screen capture

**Topic ID**: 35813
**Date**: 2024-04-29
**URL**: https://discourse.slicer.org/t/how-to-include-markup-annotations-in-high-resolution-screen-capture/35813

---

## Post #1 by @oothomas (2024-04-29 18:13 UTC)

<p>Hello Slicer Community,</p>
<p>I am currently developing an extension for high-resolution screen captures within Slicer. My goal is to programmatically capture images of a reconstructed scene that include markup annotations such as landmark names, angles, and distance measurements. However, I’ve encountered an issue where these markup labels do not appear in the off-screen rendering used for capturing the scene. My research points to the existence of a <code>vtkMRMLDisplayableManagerGroup</code> object that should be associated with my <code>threeDView</code>. This group should contain the displayable managers responsible for rendering the markup labels. How would I go about accessing this object so I can incorporate these markup annotations into the newly rendered scene?</p>
<p>Below is the core snippet of my screen capture logic:</p>
<pre><code class="lang-auto">    def runScreenCapture(self) -&gt; None:
        if self.resolution and self.outputPath:
            vtk.vtkGraphicsFactory()
            gf = vtk.vtkGraphicsFactory()
            gf.SetOffScreenOnlyMode(1)
            gf.SetUseMesaClasses(1)
            rw = vtk.vtkRenderWindow()
            rw.SetOffScreenRendering(1)
            ren = vtk.vtkRenderer()
            rw.SetSize(self.resolution[0], self.resolution[1])

            lm = slicer.app.layoutManager()

            threeDViewWidget = lm.threeDWidget(self.threeDViewIndex)
            threeDView = threeDViewWidget.threeDView()

            renderers = threeDView.renderWindow().GetRenderers()
            ren3d = renderers.GetFirstRenderer()

            # Set the background color of the off-screen renderer to match the original
            backgroundColor = ren3d.GetBackground()
            ren.SetBackground(backgroundColor)

            camera = ren3d.GetActiveCamera()

            while ren3d:

                actors = ren3d.GetActors()
                for index in range(actors.GetNumberOfItems()):
                    actor = actors.GetItemAsObject(index)

                    actor_class_name = actor.GetClassName()  # Get the class name using VTK's method
                    # Alternatively, use Python's type function: actor_type = type(actor).__name__
                    print("Actor index:", index, "Class name:", actor_class_name)

                    property = actor.GetProperty()
                    # print("Actor Property:", property)
                    representation = property.GetRepresentation()

                    # vtkProperty defines three representation types:
                    # vtkProperty.VTK_POINTS, vtkProperty.VTK_WIREFRAME, vtkProperty.VTK_SURFACE
                    if representation == vtk.VTK_POINTS:
                        print("Actor index:", index, "is represented as points.")
                    elif representation == vtk.VTK_WIREFRAME:
                        print("Actor index:", index, "is represented as wireframe.")
                    elif representation == vtk.VTK_SURFACE:
                        print("Actor index:", index, "is represented as a surface.")
                    else:
                        print("Actor index:", index, "has an unknown representation.")

                    print("Actor index:", index, "Visibility -", actor.GetVisibility(), "|", isActorVisible(camera, actor))
                    if actor.GetVisibility():  # and isActorVisible(camera, actor):
                        ren.AddActor(actor)  # Add only visible actors

                lights = ren3d.GetLights()
                for index in range(lights.GetNumberOfItems()):
                    ren.AddLight(lights.GetItemAsObject(index))

                volumes = ren3d.GetVolumes()
                for index in range(volumes.GetNumberOfItems()):
                    ren.AddVolume(volumes.GetItemAsObject(index))

                ren3d = renderers.GetNextItem()

            ren.SetActiveCamera(camera)

            rw.AddRenderer(ren)
            rw.Render()

            wti = vtk.vtkWindowToImageFilter()
            wti.SetInput(rw)
            wti.Update()
            writer = vtk.vtkPNGWriter()
            writer.SetInputConnection(wti.GetOutputPort())
            writer.SetFileName(self.outputPath)
            writer.Update()
            writer.Write()
            i = wti.GetOutput()
</code></pre>

---

## Post #2 by @oothomas (2024-04-29 18:19 UTC)

<p>Here is the desired output:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab84d66a3980b442708d54e266f6928fac2e3d8a.jpeg" data-download-href="/uploads/short-url/otkfxjI53tro5iA5yV7GKsza1Yu.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab84d66a3980b442708d54e266f6928fac2e3d8a_2_563x499.jpeg" alt="image" data-base62-sha1="otkfxjI53tro5iA5yV7GKsza1Yu" width="563" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab84d66a3980b442708d54e266f6928fac2e3d8a_2_563x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab84d66a3980b442708d54e266f6928fac2e3d8a_2_844x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab84d66a3980b442708d54e266f6928fac2e3d8a_2_1126x998.jpeg 2x" data-dominant-color="836D7B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1338×1187 69.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But my current code only outputs:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3af70640a05b4c4d65e7d47dbc779f36d21f57e0.jpeg" data-download-href="/uploads/short-url/8pCWjWFcnYUC7n49bCgMJSJ9pXG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3af70640a05b4c4d65e7d47dbc779f36d21f57e0_2_487x500.jpeg" alt="image" data-base62-sha1="8pCWjWFcnYUC7n49bCgMJSJ9pXG" width="487" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3af70640a05b4c4d65e7d47dbc779f36d21f57e0_2_487x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3af70640a05b4c4d65e7d47dbc779f36d21f57e0_2_730x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3af70640a05b4c4d65e7d47dbc779f36d21f57e0_2_974x1000.jpeg 2x" data-dominant-color="887173"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1529×1567 81.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @pieper (2024-04-30 22:50 UTC)

<p>Hi <a class="mention" href="/u/oothomas">@oothomas</a> -</p>
<p>Thanks for reporting this - I spent some time looking but didn’t see an obvious solution.  If others want to try the updated code below can be copy-pasted into the python console for easier testing.</p>
<p>I suspect the underlying issue has to do with the way the Markups text is displayed in an overlay so you can see it even when the point itself is hidden.  This overlay mode may need to be copied over into the new temporary renderer or render window.</p>
<p>Perhaps <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> or <a class="mention" href="/u/lassoan">@lassoan</a> has ideas?</p>
<pre><code class="lang-auto">class self:
  resolution = [500,500]
  outputPath = "/tmp/image.png"
  threeDViewIndex = 0

def runScreenCapture(self) -&gt; None:
    if self.resolution and self.outputPath:
        vtk.vtkGraphicsFactory()
        gf = vtk.vtkGraphicsFactory()
        gf.SetOffScreenOnlyMode(1)
        gf.SetUseMesaClasses(1)
        global rw, ren
        rw = vtk.vtkRenderWindow()
        rw.SetOffScreenRendering(1)
        ren = vtk.vtkRenderer()
        rw.SetSize(self.resolution[0], self.resolution[1])

        lm = slicer.app.layoutManager()

        threeDViewWidget = lm.threeDWidget(self.threeDViewIndex)
        threeDView = threeDViewWidget.threeDView()

        renderers = threeDView.renderWindow().GetRenderers()
        rendererCount = renderers.GetNumberOfItems()
        ren3d = renderers.GetFirstRenderer()

        # Set the background color of the off-screen renderer to match the original
        ren.SetBackground(ren3d.GetBackground())
        ren.SetBackground2(ren3d.GetBackground2())
        ren.SetGradientBackground(True)

        camera = ren3d.GetActiveCamera()

        rendererCount = 1 # only use first renderer to get Slicer content
        for rendererIndex in range(rendererCount):
            ren3d = renderers.GetItemAsObject(rendererIndex)
            print(f"\n\nrenderer {rendererIndex}")
            print(f"Layer: {ren3d.GetLayer()}")

            actors = ren3d.GetActors()
            for index in range(actors.GetNumberOfItems()):
                actor = actors.GetItemAsObject(index)

                actor_class_name = actor.GetClassName()  # Get the class name using VTK's method
                # Alternatively, use Python's type function: actor_type = type(actor).__name__
                print("Actor index:", index, "Class name:", actor_class_name)

                property = actor.GetProperty()
                # print("Actor Property:", property)
                representation = property.GetRepresentation()

                # vtkProperty defines three representation types:
                # vtkProperty.VTK_POINTS, vtkProperty.VTK_WIREFRAME, vtkProperty.VTK_SURFACE
                if representation == vtk.VTK_POINTS:
                    print("Actor index:", index, "is represented as points.")
                elif representation == vtk.VTK_WIREFRAME:
                    print("Actor index:", index, "is represented as wireframe.")
                elif representation == vtk.VTK_SURFACE:
                    print("Actor index:", index, "is represented as a surface.")
                else:
                    print("Actor index:", index, "has an unknown representation.")

                #print("Actor index:", index, "Visibility -", actor.GetVisibility(), "|", isActorVisible(camera, actor))
                if actor.GetVisibility():  # and isActorVisible(camera, actor):
                    ren.AddActor(actor)  # Add only visible actors

            lights = ren3d.GetLights()
            for index in range(lights.GetNumberOfItems()):
                ren.AddLight(lights.GetItemAsObject(index))

            volumes = ren3d.GetVolumes()
            for index in range(volumes.GetNumberOfItems()):
                ren.AddVolume(volumes.GetItemAsObject(index))

            ren3d = renderers.GetNextItem()

        ren.SetActiveCamera(camera)

        rw.AddRenderer(ren)
        rw.Render()

        wti = vtk.vtkWindowToImageFilter()
        wti.SetInput(rw)
        wti.Update()
        writer = vtk.vtkPNGWriter()
        writer.SetInputConnection(wti.GetOutputPort())
        writer.SetFileName(self.outputPath)
        writer.Update()
        writer.Write()
        i = wti.GetOutput()

        global label
        label = qt.QLabel()
        label.size = qt.QSize(*self.resolution)
        label.show()
        pixmap = qt.QPixmap()
        pixmap.load(self.outputPath)
        label.setPixmap(pixmap)

slicer.modules.markups.logic().AddControlPoint(0,0,0)
slicer.app.processEvents()
runScreenCapture(self)
</code></pre>
<p>Should show something like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27fae8afc657fa645652afdfdcefb0b57f097e13.png" data-download-href="/uploads/short-url/5HGbRbuM2gQ86if8n2sweSyUGpZ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27fae8afc657fa645652afdfdcefb0b57f097e13_2_690x368.png" alt="image" data-base62-sha1="5HGbRbuM2gQ86if8n2sweSyUGpZ" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27fae8afc657fa645652afdfdcefb0b57f097e13_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27fae8afc657fa645652afdfdcefb0b57f097e13.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27fae8afc657fa645652afdfdcefb0b57f097e13.png 2x" data-dominant-color="8A89B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">984×525 38.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2024-04-30 23:15 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="35813">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Thanks for reporting this - I spent some time looking but didn’t see an obvious solution.</p>
</blockquote>
</aside>
<p>Thanks looking into this <a class="mention" href="/u/pieper">@pieper</a>. High quality, 3D rendering of scenes is a common request we get from SlicerMorph users (e.g., for printed posters or journal covers). It will be great to have this feature fully available (including annotations).</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> your inputs will be much appreciated.</p>

---

## Post #5 by @lassoan (2024-05-01 03:04 UTC)

<p>Computing visibility of a markup control point is a complex operation, which has to be performed very quickly. Therefore we have to use a hardware picker, which captures the z buffer before overlay rendering and caches the result. Then in the overlay rendering step we determine which control points are occluded and only display the label for those points that are not occluded. This complex processing can break many ways.</p>
<p>So, I’m not surprised that the code above has issues. If you take care of initializing the render window the exact same way as it is done in the 3D viewer and copy all relevant renderers then there is a chance that some issues will go away. But the offscreen renderer may work a bit differently or may have different bugs or some features may be missing, so you may need to dig in deeper to fix the label display.</p>
<p>Alternatively, you could keep the render window as is, and also avoid offscreen rendering or switch to a software renderer (Mesa), by rendering the scene in NxN tiles (only the camera parameters are adjusted for each tile). Such logic is implemented in vtkRenderLargeImage, but only for one renderer.</p>

---

## Post #6 by @Davide_Punzo (2024-05-01 07:52 UTC)

<p>I am not sure of your requirements, but another simple option, it could be to instantiate a 3D widget outside the view layout, e.g.: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-3d-view-outside-the-view-layout" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a> . Then you could resize the full widget to get the desired high resolution. It is not an offscreen render (which is a cleaner solution), but you can still hide the widget in some way (e.g. adding it to a layout of another widget and set it to “lower”).</p>

---

## Post #7 by @muratmaga (2024-05-01 15:25 UTC)

<aside class="quote no-group" data-username="Davide_Punzo" data-post="6" data-topic="35813">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>it could be to instantiate a 3D widget outside the view layout, e.g.:</p>
</blockquote>
</aside>
<p>But then rendering would be limited the size of the screen resolution, right? If that’s correct, that’s the issue.</p>

---

## Post #8 by @oothomas (2024-05-01 20:07 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> -</p>
<p>Thank you for adding an easy testing option. I had a feeling the fact that this was an overlay had something to do with the issue. For now, I have updated HiResScreenCapture and added a disclaimer to the tutorial noting that markup labels and annotations won’t be displayed. I’m looking forward to exploring this problem more so I will keep updating this thread with any progress I make.</p>

---

## Post #9 by @oothomas (2024-05-01 20:15 UTC)

<p>Thanks everyone for assisting with this. Your help is well appreciated. I will continue to probe the layout manager and associated objects to see if I can find anything useful. I want to learn more about how these overlays are handled. I’ve found nothing so far in the renderers in  ‘threeDView’ so i’ll keep probing.</p>

---

## Post #10 by @oothomas (2024-05-01 20:22 UTC)

<p>There are many invisible objects in the renderer, this sort of explains why that might be the case. I’ll check vtkRenderlargeImage to see if there’s another possible solution.</p>
<p>Thank you for explaining!</p>

---

## Post #11 by @lassoan (2024-05-01 22:35 UTC)

<aside class="quote no-group" data-username="Davide_Punzo" data-post="6" data-topic="35813">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>I am not sure of your requirements, but another simple option, it could be to instantiate a 3D widget outside the view layout,</p>
</blockquote>
</aside>
<p>That’s a great idea!</p>
<p>You can resize the window to any size - does not matter how large your display is (I’ve tested it on Windows, I don’t see a reason why it would not work on other operating systems or window managers). So, a code snippet to render a 3D view at arbitrarily high resolution:</p>
<p>Set up a 3D view outside the main view layout:</p>
<pre data-code-wrap="python"><code class="lang-python"># Switch to a layout that has a window that is not in the main window
layoutManager = slicer.app.layoutManager()
originalLayout = layoutManager.layout
layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutDualMonitorFourUpView)
# Maximize the 3D view within this layout
viewLogic = slicer.app.applicationLogic().GetViewLogicByLayoutName("1+")
viewNode = viewLogic.GetViewNode()
layoutManager.addMaximizedViewNode(viewNode)
</code></pre>
<p>Now set up visualization in the 3D view (e.g., drag-and-drop an image to show it with volume rendering).</p>
<pre data-code-wrap="python"><code class="lang-python"># Resize the view
viewWidget = layoutManager.viewWidget(viewNode)
# Parent of the view widget is the frame, parent of the frame is the docking widget
layoutDockingWidget = viewWidget.parent().parent()
originalSize = layoutDockingWidget.size
layoutDockingWidget.resize(3000,3000)
# Capture the view
import ScreenCapture
cap = ScreenCapture.ScreenCaptureLogic()
cap.captureImageFromView(viewWidget.threeDView(), "c:/tmp/test.png")
# Restore original size and layout
layoutDockingWidget.resize(originalSize)
layoutManager.setLayout(originalLayout)
</code></pre>
<p>Since this is a regular 3D view, everything will just work - markups will appear the same way as in any other view, you can use it with screen capture module to capture videos, etc.</p>

---

## Post #12 by @muratmaga (2024-05-01 23:05 UTC)

<p>This worked real well, thank you both!</p>
<p><a class="mention" href="/u/oothomas">@oothomas</a> you can revise your module to use this approach.</p>

---

## Post #13 by @evaherbst (2024-05-06 15:38 UTC)

<p>Thank you so much <span class="mention">@Andras</span>, this is very helpful!</p>

---

## Post #14 by @muratmaga (2024-05-09 01:38 UTC)

<p>While this seem to work for the annotation, on closer inspection, it doesn’t seem to do what we want to do, since it doesn’t seem to preserve the zoom in levels, centering etc in the 3D window, and adds a lot of padding to the image.<br>
For example, this is what I have a in my 3D viewer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29ec4ad430946c2b35d99d1a0b9fd2b5d99dba36.jpeg" data-download-href="/uploads/short-url/5YRPtjy4onSOMytLVidrJ5WYSeq.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29ec4ad430946c2b35d99d1a0b9fd2b5d99dba36_2_690x436.jpeg" alt="image" data-base62-sha1="5YRPtjy4onSOMytLVidrJ5WYSeq" width="690" height="436" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29ec4ad430946c2b35d99d1a0b9fd2b5d99dba36_2_690x436.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29ec4ad430946c2b35d99d1a0b9fd2b5d99dba36_2_1035x654.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29ec4ad430946c2b35d99d1a0b9fd2b5d99dba36_2_1380x872.jpeg 2x" data-dominant-color="EDEEDE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2278×1442 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and this is what I get out of the python code above.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2546e01c6ae26228b216b0527b7e50eff79d12d0.png" data-download-href="/uploads/short-url/5jLw0KboBcwQWCSxF8aSKHnLExq.png?dl=1" title="andrastest"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2546e01c6ae26228b216b0527b7e50eff79d12d0_2_690x209.png" alt="andrastest" data-base62-sha1="5jLw0KboBcwQWCSxF8aSKHnLExq" width="690" height="209" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2546e01c6ae26228b216b0527b7e50eff79d12d0_2_690x209.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2546e01c6ae26228b216b0527b7e50eff79d12d0_2_1035x313.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2546e01c6ae26228b216b0527b7e50eff79d12d0_2_1380x418.png 2x" data-dominant-color="9A9DD3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">andrastest</span><span class="informations">5996×1818 46.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @lassoan (2024-05-09 04:54 UTC)

<p>It is an independent 3D view from the one that is in the 4-up layout, so zooming in another view will not affect it. You could set the camera in the detached view using your mouse; or you could copy the camera parameters to the detached view, etc. However, there could be still differences if certain nodes are selected to be shown in certain views. To address all these, you could add a custom layout (just a short xml string set in the layout manager, see examples here: <a href="https://github.com/Slicer/Slicer/blob/bd2c929e54eefd196ffe3105f6b5235c14fa7099/Libs/MRML/Logic/vtkMRMLLayoutLogic.cxx#L1040" class="inline-onebox">Slicer/Libs/MRML/Logic/vtkMRMLLayoutLogic.cxx at bd2c929e54eefd196ffe3105f6b5235c14fa7099 · Slicer/Slicer · GitHub</a>) that displays the selected 3D view in a separate viewport. After the screenshot is taken, you can switch back to the previous layout.</p>

---

## Post #16 by @oothomas (2024-05-10 00:24 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Thanks for your previous help! I’m integrating what you’ve posted into HiResScreenCapture and have encountered a few issues:</p>
<p><strong>1. Volume Rendering Not Displayed</strong> After making volumes visible, they now appear behind the bounding box instead of in front. Here’s what it looks like:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75cbd41847090714f99af406d9bfeaa78885a7e1.jpeg" data-download-href="/uploads/short-url/gO4z0fdBZXnNChAIdJhOkDGFeKd.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75cbd41847090714f99af406d9bfeaa78885a7e1_2_517x233.jpeg" alt="image" data-base62-sha1="gO4z0fdBZXnNChAIdJhOkDGFeKd" width="517" height="233" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75cbd41847090714f99af406d9bfeaa78885a7e1_2_517x233.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75cbd41847090714f99af406d9bfeaa78885a7e1_2_775x349.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75cbd41847090714f99af406d9bfeaa78885a7e1.jpeg 2x" data-dominant-color="797286"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">923×417 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>2. Missing Portions in High-Resolution Screenshots</strong> When taking screenshots at higher resolutions, some parts of the image are cut off. Here’s the expected vs. actual output:<br>
Expected view:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27c27f94fc58480a90d8433f7b09eea27647fe28.jpeg" data-download-href="/uploads/short-url/5FJkAT7hRs4uDBXY77un6AoxB6E.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27c27f94fc58480a90d8433f7b09eea27647fe28_2_517x252.jpeg" alt="image" data-base62-sha1="5FJkAT7hRs4uDBXY77un6AoxB6E" width="517" height="252" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27c27f94fc58480a90d8433f7b09eea27647fe28_2_517x252.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27c27f94fc58480a90d8433f7b09eea27647fe28_2_775x378.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27c27f94fc58480a90d8433f7b09eea27647fe28_2_1034x504.jpeg 2x" data-dominant-color="8C8FA0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1307×639 70.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Actual View:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccfd887c6101df10e0ec9bb4263192285eab734e.jpeg" data-download-href="/uploads/short-url/tfqAXVFJ1ZPp2SBn96C6m5fFeay.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccfd887c6101df10e0ec9bb4263192285eab734e_2_457x500.jpeg" alt="image" data-base62-sha1="tfqAXVFJ1ZPp2SBn96C6m5fFeay" width="457" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccfd887c6101df10e0ec9bb4263192285eab734e_2_457x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/ccfd887c6101df10e0ec9bb4263192285eab734e_2_685x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccfd887c6101df10e0ec9bb4263192285eab734e.jpeg 2x" data-dominant-color="707675"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">832×910 58.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>3. Markup Scaling Issues</strong> Markups and annotations do not scale with resolution increases, making them nearly invisible at higher resolutions. How can we adjust the scaling for points, angles, and lines? Below is the function I’m using to scale annotations:</p>
<pre><code class="lang-auto">    def adjustMarkupSize(viewWidget, scaleFactor):
        # Retrieve the markup display node
        markupsNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLMarkupsDisplayNode")
        if markupsNode:
            # You can access specific properties of viewWidget if needed to further refine scaling
            # For example, you could adjust based on the widget's size or other relevant properties
            widgetSize = viewWidget.size
            scaleAdjustment = max(widgetSize.width(), widgetSize.height()) / 1  # Example scaling factor

            # Adjust size based on a scaling factor combined with widget dimensions
            originalMarkupSize = markupsNode.GetTextScale()
            newScale = originalMarkupSize * scaleFactor * scaleAdjustment
            markupsNode.SetTextScale(newScale)
            print(f"Adjusted markup text scale to: {newScale}")

            return originalMarkupSize

</code></pre>
<p>I haven’t implemented this annotation scaling yet. I plan to calculate a scale factor given the resolution specified by the user. Am I going in the right direction?</p>
<p><strong>Code for Screen Capture</strong> : Here’s the complete function I’m using for screen capturing:</p>
<pre><code class="lang-auto">    def runScreenCapture(resolution, outputPath) -&gt; None:
        if resolution and outputPath:
            layoutManager = slicer.app.layoutManager()
            originalLayout = layoutManager.layout
            originalViewNode = layoutManager.threeDWidget(0).mrmlViewNode()
            originalCamera = slicer.modules.cameras.logic().GetViewActiveCameraNode(originalViewNode)

            # Debugging: Print original camera settings
            print("Original Camera Settings:")
            print("Position:", originalCamera.GetPosition())
            print("Focal Point:", originalCamera.GetFocalPoint())
            print("View Up:", originalCamera.GetViewUp())

            # Set the layout to include the necessary view
            layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutDualMonitorFourUpView)
            viewLogic = slicer.app.applicationLogic().GetViewLogicByLayoutName("1+")
            viewNode = viewLogic.GetViewNode()
            layoutManager.addMaximizedViewNode(viewNode)
            newCamera = slicer.modules.cameras.logic().GetViewActiveCameraNode(viewNode)

            # Set and debug new camera settings
            newCamera.SetPosition(originalCamera.GetPosition())
            newCamera.SetFocalPoint(originalCamera.GetFocalPoint())
            newCamera.SetViewUp(originalCamera.GetViewUp())
            print("New Camera Settings Applied")

            # Ensure volume rendering is visible in the new view
            volumeRenderingLogic = slicer.modules.volumerendering.logic()
            volumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLVolumeNode")
            displayNode = volumeRenderingLogic.GetFirstVolumeRenderingDisplayNode(volumeNode)
            if displayNode:
                displayNode.SetVisibility(True)
                displayNode.SetViewNodeIDs([viewNode.GetID()])

            # Resize and capture the view
            viewWidget = layoutManager.viewWidget(viewNode)
            layoutDockingWidget = viewWidget.parent().parent()
            originalSize = layoutDockingWidget.size
            layoutDockingWidget.resize(resolution[0], resolution[1])

            # Force a redraw
            viewWidget.threeDView().forceRender()

            # Capture the view
            cap = ScreenCapture.ScreenCaptureLogic()
            cap.captureImageFromView(viewWidget.threeDView(), outputPath)

            # Restore original size and layout
            layoutDockingWidget.resize(originalSize.width(), originalSize.height())
            # layoutManager.setLayout(originalLayout)

            # reset volume rendering visibility
            if displayNode:
                displayNode.SetVisibility(True)
                displayNode.SetViewNodeIDs([originalViewNode.GetID()])

            print("Capture Completed")

            # Make all other view nodes except the original one invisible
            allViewNodes = slicer.mrmlScene.GetNodesByClass("vtkMRMLViewNode")
            allViewNodes.InitTraversal()
            viewNode = allViewNodes.GetNextItemAsObject()
            while viewNode:
                if viewNode.GetID() != originalViewNode.GetID():
                    slicer.mrmlScene.RemoveNode(viewNode)
                viewNode = allViewNodes.GetNextItemAsObject()

            # Refresh the layout to reflect changes
            layoutManager.layout = originalLayout

</code></pre>
<p>Could you suggest any improvements or point out what might be going wrong with these features?</p>
<p>Thanks for your continued help!</p>
<p>Best,<br>
Oshane</p>

---

## Post #17 by @lassoan (2024-05-10 13:13 UTC)

<aside class="quote no-group" data-username="oothomas" data-post="16" data-topic="35813">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/oothomas/48/68743_2.png" class="avatar"> oothomas:</div>
<blockquote>
<p><strong>1. Volume Rendering Not Displayed</strong> After making volumes visible, they now appear behind the bounding box instead of in front.</p>
</blockquote>
</aside>
<p>There is indeed something wrong with the z buffer initialization sometimes, which makes the volume rendering not occlude the lines of the box.</p>
<p>As a workaround, you can nudge the view’s camera a bit to force a re-rendering: <code>getNode('Camera_2').GetCamera().Dolly(1.001)</code></p>
<p>If you have a way to reproduce the behavior then please submit an issue to <a href="http://issues.slicer.org">issues.slicer.org</a> and reference it here.</p>
<aside class="quote no-group" data-username="oothomas" data-post="16" data-topic="35813">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/oothomas/48/68743_2.png" class="avatar"> oothomas:</div>
<blockquote>
<ol start="2">
<li>Missing Portions in High-Resolution Screenshots</li>
</ol>
</blockquote>
</aside>
<p>It is because the magnified view has a different shape. You have to record the <code>originalSize</code> before you change layout.</p>
<aside class="quote no-group" data-username="oothomas" data-post="16" data-topic="35813">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/oothomas/48/68743_2.png" class="avatar"> oothomas:</div>
<blockquote>
<ol start="3">
<li>Markup Scaling Issues</li>
</ol>
</blockquote>
</aside>
<p>You can change the screen scale factor to preserve relative size of markup control points and labels. This factor has not been exposed on the public API. I have <a href="https://github.com/Slicer/Slicer/pull/7740">added <code>SetScreenScaleFactor</code> method to the view node</a> that allows you to change it (save the original value, set higher value, take the screenshot, and restore the original value). It will probably take a few days to get the update reviewed and merged into the Slicer Preview Release.</p>

---

## Post #18 by @oothomas (2024-05-15 12:56 UTC)

<p>Hi Everyone,</p>
<p>I want to extend my heartfelt thanks to all of you for your invaluable assistance with this module thus far. Special thanks to Andras, Steve, and everyone else who helped resolve the issues during yesterday’s developer call.</p>
<p>I’m pleased to share the current version of the module:</p>
<p><a href="https://github.com/oothomas/SlicerMorph/tree/master/HiResScreenCapture" rel="noopener nofollow ugc">HiResScreenCapture Module on GitHub</a></p>
<p>The module is functioning very well, and I’ve simplified the UI to enhance ease of use. I would greatly appreciate any additional suggestions or feedback you might have. I’m also eager to discuss how some of these features can be integrated into the screen capture module.</p>
<p>Thank you once again for your support.</p>
<p>Best regards,</p>
<p>Oshane</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa8b28cda1c9d18838826db643983da81a872ebe.jpeg" data-download-href="/uploads/short-url/okHjGOsbiJfsofsecucWIRml6Ds.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa8b28cda1c9d18838826db643983da81a872ebe_2_690x293.jpeg" alt="image" data-base62-sha1="okHjGOsbiJfsofsecucWIRml6Ds" width="690" height="293" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa8b28cda1c9d18838826db643983da81a872ebe_2_690x293.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa8b28cda1c9d18838826db643983da81a872ebe_2_1035x439.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa8b28cda1c9d18838826db643983da81a872ebe_2_1380x586.jpeg 2x" data-dominant-color="BEC0CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1902×810 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5c8aca8958d05ee9431aa408b637b502924eb7b.jpeg" data-download-href="/uploads/short-url/z4iVf5Duz1zZ3ig1QdvxKprZaUr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5c8aca8958d05ee9431aa408b637b502924eb7b_2_690x337.jpeg" alt="image" data-base62-sha1="z4iVf5Duz1zZ3ig1QdvxKprZaUr" width="690" height="337" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5c8aca8958d05ee9431aa408b637b502924eb7b_2_690x337.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5c8aca8958d05ee9431aa408b637b502924eb7b_2_1035x505.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5c8aca8958d05ee9431aa408b637b502924eb7b_2_1380x674.jpeg 2x" data-dominant-color="7F838A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1621×792 94.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #19 by @pieper (2024-05-15 14:50 UTC)

<p>Thanks for joining the call and thanks for working on Slicer!</p>

---

## Post #20 by @evaherbst (2024-05-17 15:48 UTC)

<p>Thanks Oshane for making this available, I will test it out and report back!</p>

---

## Post #21 by @muratmaga (2024-05-17 15:59 UTC)

<p><a class="mention" href="/u/evaherbst">@evaherbst</a> thanks for testing. Make sure you are using the latest preview for this (not the stable).</p>
<p>M</p>

---

## Post #22 by @oothomas (2024-06-07 18:18 UTC)

<p>Hi,</p>
<p>I have encountered an issue with the HiRes Screen Capture feature on both Mac and Windows when display scaling is enabled.</p>
<p><strong>Issue Description:</strong> When using HiRes Screen Capture with display scaling, the resulting screenshot is significantly larger than expected. For example, on a Windows system with 225% scaling, the expected image resolution is 8952x3352, but the saved image resolution is 17904x14448.</p>
<p><strong>Steps to Reproduce:</strong></p>
<ol>
<li>Enable display scaling on your Mac or Windows system.</li>
<li>Set the scaling to 225% (Windows example).</li>
<li>Use the HiRes Screen Capture feature in 3D Slicer.</li>
<li>Observe the discrepancy in the resulting screenshot resolution.</li>
</ol>
<p>Is it possible to account for display scale when setting the desired screen resolution in the module logic?</p>
<p>I’ve also noticed that when the export button is clicked on the mac, 3D Slicer sometimes crashes completely after the image is saved.</p>
<p>Looking forward to any guidance you can provide.</p>
<p>Best,</p>
<p>Oshane</p>

---

## Post #23 by @pieper (2024-06-07 19:58 UTC)

<p>I would think you can detect this and compensate.  You can look to see if Qt provides an API to query the screen scaling factor, but if needed you could look into adding a platform-specific API call somewhere in the C++ code with <code>ifdef</code>s to detect the platform.</p>

---

## Post #24 by @oothomas (2024-06-10 21:37 UTC)

<p>Would this be a worthwhile task for Project Week, in addition to generally improving the module?</p>

---

## Post #25 by @pieper (2024-06-10 21:46 UTC)

<p>Yes, this would be perfect to work on at Project Week <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---
