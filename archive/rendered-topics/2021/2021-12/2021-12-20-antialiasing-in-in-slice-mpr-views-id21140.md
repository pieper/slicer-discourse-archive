# Antialiasing in in slice (MPR) views

**Topic ID**: 21140
**Date**: 2021-12-20
**URL**: https://discourse.slicer.org/t/antialiasing-in-in-slice-mpr-views/21140

---

## Post #1 by @riep (2021-12-20 11:04 UTC)

<p>Hi everyone,<br>
I was wondering if there was an easy way to reduce aliasing effects in MPR view of the orientation interactor and models.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68ba9c1bd0441a5aa400ab1f23b852f1ab234054.png" alt="Screenshot from 2021-12-20 10-52-56" data-base62-sha1="eWtsVwBwPPOqv2eFqLJaPj926uo" width="282" height="147"></p>
<p>We are developing on slicer 4.11.20210226 but this is also visible on master branch</p>
<p>Thanks for any tips,<br>
Pierre</p>

---

## Post #2 by @pieper (2021-12-20 15:13 UTC)

<p>You can try the antialiasing settings in the View panel.  It doesn’t work on all platforms in my experience - it would be good if people could experiment and maybe we can track down when it does and doesn’t help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8aabb9fbead2204f55edcfb03a2f3b42b3172153.jpeg" data-download-href="/uploads/short-url/jMJOq8G320vHu95lO0eED03RX8L.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8aabb9fbead2204f55edcfb03a2f3b42b3172153_2_690x496.jpeg" alt="image" data-base62-sha1="jMJOq8G320vHu95lO0eED03RX8L" width="690" height="496" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8aabb9fbead2204f55edcfb03a2f3b42b3172153_2_690x496.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8aabb9fbead2204f55edcfb03a2f3b42b3172153_2_1035x744.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8aabb9fbead2204f55edcfb03a2f3b42b3172153.jpeg 2x" data-dominant-color="F6F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1300×935 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @riep (2021-12-21 06:30 UTC)

<p>Thank you very much Steve it is exactly what I was looking for.<br>
Cheers,<br>
Pierre</p>

---

## Post #4 by @lassoan (2021-12-21 07:07 UTC)

<p>Multi-sampling is the true antialiasing method, but that would mess with the Z buffer, and therefore with hardware-accelerated picking that is used for markup nodes label display and control point manipulation, compositing volume rendering and surface rendering, etc. Also as <a class="mention" href="/u/pieper">@pieper</a> mentioned there seem to be some some issues with it in recent VTK and Qt versions (for example, I don’t think the MSAA setting has any effect right now on Windows).</p>
<p>Alternatively, you can do screen-space antialiasing using FXAA. It is very fast and simple, but it can alter any displayed content in the renderer (may makes boundary of line-like structures blurry), so it can be applied safely to renderers such as 2D overlays (markup interactors, labels, etc.), but need to be careful with applying to renderers that display images.</p>
<p>You can enable FXAA to all renderers of a slice or 3D views using this code snippet:</p>
<pre><code class="lang-python">def enableFXAA(view, enable):
    renderWindow = view.renderWindow()
    renderers = renderWindow.GetRenderers()
    for renderer in renderers:
        renderer.SetUseFXAA(enable)
    slicer.util.forceRenderAllViews()

# For slice view:
enableFXAA(slicer.app.layoutManager().sliceWidget('Red').sliceView(), True)

# For 3D view:
# enableFXAA(slicer.app.layoutManager().threeDWidget(0).threeDView(), True)
</code></pre>
<p>FXAA has <a href="https://discourse.vtk.org/t/advice-for-high-quality-anti-aliased-lines-volume-rendering/2141/2?u=lassoan">trouble with smoothing thin lines</a> and may <a href="https://discourse.vtk.org/t/how-to-anti-alias-in-vtkrenderwindow/4556/10">cause various artifacts</a>. So, while it is extremely fast and simple, it would need some more experimentation to see how it could be utilized in Slicer.</p>
<p>Finally, there is also a computationally expensive but high-quality option: using an SSAAPass (render into higher-resolution image and sample down). You can try it with this code snippet:</p>
<pre><code class="lang-python">def setupSSAA(view, enable):
    renderWindow = view.renderWindow()
    renderer = renderWindow.GetRenderers().GetFirstRenderer()
    # create the basic VTK render steps
    basicPasses = vtk.vtkRenderStepsPass()
    # finally blur the resulting image
    # The blur delegates rendering the unblured image
    # to the basicPasses
    ssaa = vtk.vtkSSAAPass()
    ssaa.SetDelegatePass(basicPasses)
    # tell the renderer to use our render pass pipeline
    if enable:
        renderer.SetPass(ssaa)
    else:
        renderer.SetPass(basicPasses)
    slicer.util.forceRenderAllViews()

#setupSSAA(slicer.app.layoutManager().sliceWidget('Red').sliceView(), True)
setupSSAA(slicer.app.layoutManager().threeDWidget(0).threeDView(), True)
</code></pre>
<p>This works quite nicely, but it tends to make thin lines much thinner, and it messes up Z buffer similarly to MSAA (volume rendering is not composited correctly with surfaces, depth peeling does not work, etc.). I haven’t experimented with it much, maybe these issues can be addressed.</p>
<p>I would also mention that I have a hi-dpi laptop and I can barely see aliasing artifacts. So, in some cases upgrading the hardware might be an option, too.</p>

---

## Post #5 by @riep (2021-12-21 07:24 UTC)

<p>Thank you, Andras, for this complete explanation. I am on Linux and the MSAA is working. I will test other solutions too.</p>

---

## Post #6 by @riep (2021-12-21 16:09 UTC)

<p>Would it make sense to you to combine MSAA and FXAA?</p>

---

## Post #7 by @lassoan (2021-12-21 20:14 UTC)

<p>I’m not sure if combining MSAA and FXAA (applying both of them at the same time) would be useful, because the benefit would be marginal, if any, but all the drawbacks and limitations would be combined.</p>
<p>Even though all 3 current anti-aliasing methods have very serious limitations, it could make sense to expose them on the GUI to allow users experiment with it.</p>

---
