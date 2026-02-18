# Improve markups label visibility

**Topic ID**: 17022
**Date**: 2021-04-10
**URL**: https://discourse.slicer.org/t/improve-markups-label-visibility/17022

---

## Post #1 by @lassoan (2021-04-10 15:22 UTC)

<p>Sometimes markups labels are difficult to read over complex background. Should we enable shadow and bold style by default to improve visibility?</p>
<p>Examples:</p>
<p>Current default (no bold or shadow):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/2338fffd91fd5bce434585bfb45097aaaea80893.jpeg" alt="image" data-base62-sha1="51APFidATNXI8hXEjtoZBwfA3sL" width="508" height="242"></p>
<p>Shadow:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b62126ee6eab6358cccf36b918188db424f76f98.jpeg" alt="image" data-base62-sha1="pZbVvKWiWh7si6iv8LPCsSc3L84" width="517" height="240"></p>
<p>Bold:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2adb28b66a63b19ba761cc246577c13550ea5f2.jpeg" alt="image" data-base62-sha1="yCPGXuG7QLGFpuBwZYxRojzSMzo" width="521" height="248"></p>
<p>Shadow+bold:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d676c87f73d4bd2873ef5a039b110ce22a3e638c.jpeg" alt="image" data-base62-sha1="uBeFzofKyERoTS4c1YkZXHXSO7O" width="520" height="241"></p>
<p>Shadow+bold (with smaller font size):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89d15ba94fd5ba2c5602b00d3f8983c7ad11ad32.jpeg" alt="image" data-base62-sha1="jFbXA7xju2KoWe6r9VPJhIR0YvM" width="520" height="246"></p>

---

## Post #2 by @pieper (2021-04-10 15:48 UTC)

<p>A shadow plus bold, slightly smaller font looks good to me.  A screen-space halo would be even better but I don’t think that’s available in VTK.</p>
<p>OHIF defaults to a yellow which is more readable sometimes but not always.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebb547669346ca58920027f68d9d9a6c96a84567.jpeg" alt="image" data-base62-sha1="xDaAOFwqdbXhd3D9kKyNyBIH4Dt" width="376" height="307"></p>
<p>They use a convention I do like though, which is that the markup is green while it’s being actively defined (e.g. when only one point of a line has been placed) the then it gets it’s final color when completed.</p>

---

## Post #3 by @rbumm (2021-04-10 17:37 UTC)

<p>Shadow and bold look great!</p>

---

## Post #4 by @muratmaga (2021-04-10 18:43 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="17022">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>OHIF defaults to a yellow which is more readable sometimes but not always.</p>
</blockquote>
</aside>
<p>In anatomical drawings/labelling, it is common to pair these lines with a color that is much darker in contrast (e.g., white/black, yellow/blue etc), so that part of the line remains visible regardless both in areas of high/low contrast. On option like this would be great actually!</p>

---

## Post #5 by @pieper (2021-04-10 19:32 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="17022">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>it is common to pair these lines with a color that is much darker in contrast (e.g., white/black, yellow/blue etc)</p>
</blockquote>
</aside>
<p>Yes, that’s what the drop shadow does, but our default markup color is too dark.  I’ve never really cared for that red color actually.  It carries over from the days when you needed to use bland colors so they could be recorded to VHS tape (clearly no longer a requirement).</p>

---

## Post #6 by @hherhold (2021-04-10 19:50 UTC)

<p>+1 on drop shadow on by default. Incidentally, sometimes enabling shadow doesn’t seem to work - any idea why that might happen?</p>

---

## Post #7 by @lassoan (2021-04-10 19:54 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="6" data-topic="17022">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>sometimes enabling shadow doesn’t seem to work - any idea why that might happen</p>
</blockquote>
</aside>
<p>We would need more information to investigate. Preferably step-by-step instructions to reproduce.</p>

---

## Post #8 by @hherhold (2021-04-11 01:03 UTC)

<p>Yeah, sorry, that was a pretty useless observation. I’ll try to get something more concrete… I just have a few scenes where drop shadows don’t seem to show. I’ll work on steps to reproduce.</p>

---

## Post #9 by @muratmaga (2021-04-11 01:30 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="17022">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Yes, that’s what the drop shadow does, but our default markup color is too dark.</p>
</blockquote>
</aside>
<p>I meant the line/curve itself as well, not just the markups label. Even in your example above, part of the the yellow line is hard to see.</p>
<p>Also in the stable version, the two unselected and active color is either identical or too close to differentiate (I really can’t tell). I set them to be different, and then hit Save as Defaults, but this is not retained after Slicer is restarted. Is this a bug or a color defaults are not meant to be saved ? In comparison glyph/text size changes are saved and retained correctly.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb1034a5ecd4b1b768e277fa41cb661ba2291b4b.png" alt="image" data-base62-sha1="sYnE6URxhKsrtUOi6lIqnkDGe71" width="650" height="140"></p>

---

## Post #10 by @lassoan (2021-04-11 13:46 UTC)

<p>Currently, only “basic” display properties can be saved as default. This made sense when there were not too many display properties, but now there are dozens, and it is very hard to select a meaningful subset. So, I’ll change the implementation to save/restore all display properties.</p>
<p>I agree that we would need high-contrast outline for lines and markers as well. One option is to use additional rendering passes, such as Gaussian or glow pass, but that would require some work (adding two additional rendering layers and improve image quality of these rendering passes, because glow pass is optimized for adding bright glow and not dark shadow and the outline is not continuous; Gaussian step is hardcoded to 5 pixels, which is not sufficient as a border).</p>
<p>Example of glow pass:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e37f2168888a3a98b78a82a5e09adca61a2c701.jpeg" data-download-href="/uploads/short-url/4jkbBkahUhSeNK25LEmKuYuNWEh.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e37f2168888a3a98b78a82a5e09adca61a2c701_2_690x388.jpeg" alt="image" data-base62-sha1="4jkbBkahUhSeNK25LEmKuYuNWEh" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e37f2168888a3a98b78a82a5e09adca61a2c701_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e37f2168888a3a98b78a82a5e09adca61a2c701_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e37f2168888a3a98b78a82a5e09adca61a2c701.jpeg 2x" data-dominant-color="636363"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1090×614 62.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<details>
<summary>
Code to test custom rendering passes</summary>
<pre data-code-wrap="python"><code class="lang-python">newRenderer=False
gaussian=False

if newRenderer:
    iren = vtk.vtkRenderWindowInteractor()
    renWin = vtk.vtkRenderWindow()
    renWin.SetMultiSamples(0)
    iren.SetRenderWindow(renWin)
    renderer = vtk.vtkRenderer()
    rendererOutline = vtk.vtkRenderer()
    rendererOutline.SetLayer(1)
    renWin.SetNumberOfLayers(2)
    renWin.AddRenderer(rendererOutline)
    renWin.AddRenderer(renderer)
else:
    layoutManager = slicer.app.layoutManager()
    view = layoutManager.sliceWidget('Red').sliceView()
    renderWindow = view.renderWindow()
    renderers = renderWindow.GetRenderers()
    renderer = renderers.GetItemAsObject(0)
    renderWindow.SetNumberOfLayers(renderWindow.GetNumberOfLayers()+2)
    renderer = vtk.vtkRenderer()
    rendererOutline = vtk.vtkRenderer()
    if gaussian:
        renderer.SetLayer(renderWindow.GetNumberOfLayers()-1)
        rendererOutline.SetLayer(renderWindow.GetNumberOfLayers()-2)
    else:
        renderer.SetLayer(renderWindow.GetNumberOfLayers()-2)
        rendererOutline.SetLayer(renderWindow.GetNumberOfLayers()-1)
    renderWindow.AddRenderer(renderer)
    renderWindow.AddRenderer(rendererOutline)

basicPasses = vtk.vtkRenderStepsPass()
if gaussian:
    glowPass = vtk.vtkGaussianBlurPass()
else:
    glowPass = vtk.vtkOutlineGlowPass()
    glowPass.SetOutlineIntensity(1.0)

glowPass.SetDelegatePass(basicPasses)

# Apply the render pass to the highlight renderer
rendererOutline.SetPass(glowPass)

outlineColor = [1.0, 1.0, 1.0]

# Create mapper and actor for the main renderer
coneSource = vtk.vtkConeSource()
coneMapperMain = vtk.vtkPolyDataMapper()
coneMapperMain.SetInputConnection(coneSource.GetOutputPort())
coneActorMain = vtk.vtkActor()
coneActorMain.SetMapper(coneMapperMain)
renderer.AddActor(coneActorMain)

# Create mapper and actor for the outline
coneMapperOutline = vtk.vtkPolyDataMapper()
coneMapperOutline.SetInputConnection(coneSource.GetOutputPort())
coneActorOutline = vtk.vtkActor()
coneActorOutline.SetMapper(coneMapperOutline)
coneActorOutline.GetProperty().SetColor(outlineColor)
coneActorOutline.GetProperty().LightingOff()
rendererOutline.AddActor(coneActorOutline)

fontSize=20
textActor = vtk.vtkTextActor()
textActor.SetDisplayPosition(100, 100);
textActor.SetVisibility(True)
textActor.GetTextProperty().SetFontSize(fontSize)
textActor.GetTextProperty().SetColor(0,0,0)
textActor.SetInput("This is a test")
renderer.AddActor(textActor)

textActorOutline = vtk.vtkTextActor()
textActorOutline.SetDisplayPosition(100, 100);
textActorOutline.SetVisibility(True)
textActorOutline.GetTextProperty().SetColor(outlineColor)
textActorOutline.GetTextProperty().SetFontSize(fontSize)
textActorOutline.SetInput("This is a test")
rendererOutline.AddActor(textActorOutline)

if newRenderer:
    renWin.SetSize(400, 400)
    renderer.ResetCamera()
    camera = renderer.GetActiveCamera()
    camera.Azimuth(-40.0)
    camera.Elevation(20.0)
    renderer.ResetCamera()
    rendererOutline.SetActiveCamera(camera)
    renWin.Render()
    iren.Start()
</code></pre>
</details>
<p>Another option is to render thicker dark line in the same renderer behind the normal line:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91e27bf7c1de944201e3c14dc234bc29de6df38c.png" alt="image" data-base62-sha1="kOytm3OWPkTv3TDjB3irY6tvgQs" width="398" height="149"></p>
<p>With enabling FXAA anti-aliasing (to make the line edges smoother):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffa1f573da85a762b7a5e43b56f802315bca253e.png" alt="image" data-base62-sha1="AtqKvlIofhlRYDxHqOqzwRNCaCy" width="394" height="147"></p>
<details>
<summary>
Code snippet to enable FXAA anti-aliasing</summary>
<pre data-code-wrap="python"><code class="lang-python">view = slicer.app.layoutManager().sliceWidget('Red').sliceView()
#view = slicer.app.layoutManager().threeDWidget(0).threeDView()
renderWindow = view.renderWindow()
renderers = renderWindow.GetRenderers()
for renderer in renderers:
    renderer.UseFXAAOn()
</code></pre>
</details>
<p>Probably we should expose FXAA anti-aliasing option to users, too. It performs smart smoothing in the rendered image (only smoothing at sharp edges), which may impact anything in the rendering layer, but if we render markups in a separate layer (which is easy to do in slice views) then we can ensure that only markups edges are smoothed.</p>

---

## Post #11 by @lassoan (2021-04-11 20:16 UTC)

<p>I’ve submitted a pull request to enable bold and shadow by default for markup labels, a potential fix for the issue when shadow cannot be enabled, and saving/restoring all markups display properties as default:</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/5580" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5580" target="_blank" rel="noopener">Improve markups label visibility</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>lassoan:improve-markups-label-visibility</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-04-11" data-time="20:04:35" data-timezone="UTC">08:04PM - 11 Apr 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="3 commits changed 4 files with 195 additions and 53 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5580/files" target="_blank" rel="noopener">
          <span class="added">+195</span>
          <span class="removed">-53</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>I’ve added an issue to track the remaining enhancement ideas:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/5579" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5579" target="_blank" rel="noopener">Improve markups rendering quality</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-04-11" data-time="19:25:36" data-timezone="UTC">07:25PM - 11 Apr 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">Markup lines and text are not well visible when their color is similar to background color.
Edges of markup lines and curves...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:enhancement</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #12 by @hherhold (2021-05-12 21:50 UTC)

<p>I think I was able to find out <em>what</em> was happening with shadows not showing up but not <em>why</em>. In a scene where I didn’t see any drop shadows, the scene MRML had the <code>textProperty</code> setting for the <code>MarkupsFiducialDisplay</code> node set with <code>text-shadow:0px 0px 2px rgba(0,0,0,1.0);</code>.  All I had to do was manually change it to <code>text-shadow:2px 2px 2px rgba(0,0,0,1.0);</code> and drop shadows showed up.</p>

---

## Post #13 by @lassoan (2021-05-22 14:37 UTC)

<p>These corrupted values were saved in the scene due to a bug (that I fixed in April).</p>

---
