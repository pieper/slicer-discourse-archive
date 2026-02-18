# Independent zoom along different axes

**Topic ID**: 19263
**Date**: 2021-08-18
**URL**: https://discourse.slicer.org/t/independent-zoom-along-different-axes/19263

---

## Post #1 by @keri (2021-08-18 22:45 UTC)

<p>Hi,</p>
<p>I’m working on Slicer CAT where I need to display different 3D data (the data represent the geological objects) in XYZ domain where X, Y axes - has the meaning of geographic coordinates (meters) and Z - is the depth (zero is the ocean water level) or time (meters or milliseconds). Right handed coordinate system: X-to the east, Y-to the north, Z-out of the Earth.</p>
<p>I need to provide ability to zoom Z-axis independently from X and Y. That leads that the scales along X,Y will differ from Z-axis.</p>
<p>Maybe Slicer already has such opportunity? If not maybe you have some recommendations/links and especially should I implement it in Slicer core library via Slicer-github pull request or only in my Slicer CAT?</p>

---

## Post #2 by @pieper (2021-08-18 23:03 UTC)

<p>Yes, all of that should be pretty doable.  You could have a look at SlicerAstro, which also adapted a lot of things to deal with different coordinate meanings so I’d think a lot of the hooks that <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> added will be of use to you.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/Punzo/SlicerAstro">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Punzo/SlicerAstro" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/26fd57d9e407c81ab0ce0ae0af90a5660ccd9dd824e2ad8cd324ed41fdc99b0d/Punzo/SlicerAstro" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/Punzo/SlicerAstro" target="_blank" rel="noopener">GitHub - Punzo/SlicerAstro: Astronomy (HI) extension for 3DSlicer...</a></h3>

  <p>Astronomy (HI) extension for 3DSlicer (https://www.slicer.org/) - GitHub - Punzo/SlicerAstro: Astronomy (HI) extension for 3DSlicer (https://www.slicer.org/)</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @keri (2021-08-18 23:07 UTC)

<p>Thank you,</p>
<p>Is there precompiled bindary of Slicer Astro for Windows?</p>

---

## Post #4 by @pieper (2021-08-18 23:12 UTC)

<p>In general, yes, you can just install the extension.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Extensions/SlicerAstro" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/4.10/Extensions/SlicerAstro</a></p>
<p>But it looks like there may be a <a href="https://slicer.cdash.org/viewBuildError.php?buildid=2364700">build issue on windows</a> currently.  Looks like mac and linux are working.</p>

---

## Post #5 by @keri (2021-08-19 00:18 UTC)

<p>I’m trying to build Slicer Astro but there are some things…</p>
<p>My slicer cat (named Colada) is in <code>C:/C</code> and the build folder <code>C:/C/d</code>.<br>
Slicer Astro is in <code>C:/A</code> and the build folder <code>C:/A/d</code>.</p>
<p>Then I do (using IDE though the commands should be similar):</p>
<pre><code class="lang-auto">cd C:/A/d
cmake .. -DSlicer_DIR=C:/C/d/Slicer-build
cmake --build .
</code></pre>
<p>Then I can see that only <code>SlicerAstroWelcome</code> module is built. Can’t understand why…</p>
<p>How to add this extension to my Slicer CAT? Do I need to add all the path to Slicer Astro’s built modules (via `Edit-&gt;Application Settings-&gt;Modules-&gt;add)?</p>
<p>If I try to execute <code>C:\A\d\SlicerWithSlicerAstro.exe</code> in cmd I get:</p>
<pre><code class="lang-auto">PS C:\A\d&gt; ./SlicerWithSlicerAstro.exe
error: File specified using --launcher-additional-settings argument does NOT exist ! [C:/A/d/AdditionalLauncherSettings.ini]
Usage
  Colada [options]

Options
  --launcher-help                                 Display help
  --launcher-version                              Show launcher version information
  --launcher-verbose                              Verbose mode
  --launch                                        Specify the application to launch
  --launcher-detach                               Launcher will NOT wait for the application to finish
  --launcher-no-splash                            Hide launcher splash
  --launcher-timeout                              Specify the time in second before the launcher kills the application. -1 means no timeout (default: -1)
  --launcher-load-environment                     Specify the saved environment to load.
  --launcher-dump-environment                     Launcher will print environment variables to be set, then exit
  --launcher-show-set-environment-commands        Launcher will print commands suitable for setting the parent environment (i.e. using 'eval' in a POSIX shell), then exit
  --launcher-additional-settings                  Additional settings file to consider
  --launcher-additional-settings-exclude-groups   Comma separated list of settings groups that should NOT be overwritten by values in User and Additional settings. For example: General,Application,ExtraApplicationToLaunch
  --launcher-ignore-user-additional-settings      Ignore additional user settings
  --launcher-generate-exec-wrapper-script         Generate executable wrapper script allowing to set the environment
  --launcher-generate-template                    Generate an example of setting file
  --VisualStudioProject                           Open Visual Studio Slicer project with Slicer's DLL paths set up
  --cmd                                           Start cmd
  --designer                                      Start Qt designer using Slicer plugins
  --VisualStudio                                  Open Visual Studio with Slicer's DLL paths set up
PS C:\A\d&gt;
</code></pre>

---

## Post #6 by @keri (2021-08-19 11:53 UTC)

<p>I just saw that slicer astro is unix only</p>

---

## Post #7 by @keri (2021-08-20 14:33 UTC)

<p>I have installed Slicer Astro on Ubuntu, definately there are some useful features.<br>
But I can’t find a way to make independent zooming along chosen axis…<br>
Perhaps I postpone this task for a while and try get a little experience of writing/modifying Slcier’s widgets that are on the scene (on the picture, I think they are called <code>qMRMLwidgets</code>)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef88e3897a5e5ea72f7bb9e6581ab26c48350d01.jpeg" data-download-href="/uploads/short-url/yb1oHlH1kgKRoE9WLxQ3RYORah3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef88e3897a5e5ea72f7bb9e6581ab26c48350d01_2_690x369.jpeg" alt="image" data-base62-sha1="yb1oHlH1kgKRoE9WLxQ3RYORah3" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef88e3897a5e5ea72f7bb9e6581ab26c48350d01_2_690x369.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef88e3897a5e5ea72f7bb9e6581ab26c48350d01.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef88e3897a5e5ea72f7bb9e6581ab26c48350d01.jpeg 2x" data-dominant-color="5F6068"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">822×440 75.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2021-08-20 15:39 UTC)

<p>This question has come up before and I think setting slice field of view manually worked acceptably for that use case. However, it would be a much cleaner solution to simply apply a transform to the volume that scales it down along an axis.</p>

---

## Post #9 by @keri (2021-08-20 15:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="19263">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>However, it would be a much cleaner solution to simply apply a transform to the volume that scales it down along an axis.</p>
</blockquote>
</aside>
<p>I’m afraid that I need to work in XYZ coordinate system and all the data (not only volumes, but everything that is on scene) must be hard linked to axes… But thank you, I’m going to take some time to investigate the problem</p>

---

## Post #10 by @keri (2021-08-20 17:02 UTC)

<p>Could ypu please give a hint how to acieve widgets from the scene and add widgets there (widgets are shown on the picture)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1cc123e855dc8852ba9474c57100760fd92e2e5.png" alt="image" data-base62-sha1="n5k5N5foC1YvdLJ0XRgiPBeNWiF" width="422" height="227"></p>

---

## Post #11 by @lassoan (2021-08-20 17:42 UTC)

<aside class="quote no-group" data-username="keri" data-post="9" data-topic="19263">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>I’m afraid that I need to work in XYZ coordinate system and all the data (not only volumes, but everything that is on scene) must be hard linked to axes…</p>
</blockquote>
</aside>
<p>You can apply linear transforms to all node types, not just volumes. Also, you can unregister default measurements in markups nodes and register your own custom measurements that take into account the changed scale when reporting length/area/volume values.</p>
<aside class="quote no-group" data-username="keri" data-post="10" data-topic="19263">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>Could ypu please give a hint how to acieve widgets from the scene and add widgets there (widgets are shown on the picture)</p>
</blockquote>
</aside>
<p>There should be examples for this in the script repository, but the idea is that you l get widgets via the layout manager and then manipulate child widgets using standard Qt API.</p>

---

## Post #12 by @Davide_Punzo (2021-08-20 23:56 UTC)

<p>Hi,</p>
<p>In SlicerAstro there isn’t s feature to zoom just one axis. However you could easily add in Python some widgets (e.g. sliders) in the slide pop up menu on which you could modify the field of view of the slice (i.e. you modify the attributes of the MRML slice object associated to the slice widget). Modifying the mouse zooming interaction is more complicated.</p>
<p>In general, regarding a full coordinates customization, you may have a look at the custom classes in the AstroVolumes module (the MRMLDM classes and the widgets, something like SlicerAstroController etc…) and few tweaks in Python (SlicerAstroDataProde module). The implementation is mainly in C++ and somewhat tricky if you don’t have a full picture of Slicer infrastructure.</p>
<p>Cheers,<br>
Davide.</p>

---

## Post #13 by @keri (2021-08-21 16:41 UTC)

<p>Thank you, I have found example how to customize 3d view and slice widgets <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-widgets-in-view-controller-bars" rel="noopener nofollow ugc">here</a>.</p>
<p><a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> thank you for explanation. Step by step I’m getting known with Slicer philosophy. Probably a little later I will come back to this task and reread this topic. I guess that should help me</p>

---

## Post #14 by @keri (2021-08-22 15:02 UTC)

<p>It seems that I can set <a href="https://discourse.vtk.org/t/scaling-a-rendering-scene/173/4?u=kerim" rel="noopener nofollow ugc">transform to the vtkCamera</a>. And I tested with VTK 9.0.1 it works.</p>
<pre data-code-wrap="cpp"><code class="lang-cpp">  vtkNew&lt;vtkTransform&gt; transform;
  transform-&gt;Scale(2, 1, 1);

  renderer-&gt;GetActiveCamera()-&gt;SetModelTransformMatrix(transform-&gt;GetMatrix());
</code></pre>
<p>Though there are some problems that is connected with <code>vtkCubeAxesActor</code>.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00b3c26df9bc6275bd4060e7159e5ec15a960198.png" data-download-href="/uploads/short-url/6d8eZvxWFHLXgk9gV3k7D5JUc8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00b3c26df9bc6275bd4060e7159e5ec15a960198_2_626x500.png" alt="image" data-base62-sha1="6d8eZvxWFHLXgk9gV3k7D5JUc8" width="626" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00b3c26df9bc6275bd4060e7159e5ec15a960198_2_626x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00b3c26df9bc6275bd4060e7159e5ec15a960198.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00b3c26df9bc6275bd4060e7159e5ec15a960198.png 2x" data-dominant-color="515B58"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">642×512 94.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>P.S. as I have previously created <a href="https://discourse.slicer.org/t/add-an-actor-vtkcubeaxesactor-to-the-scene-in-c/19294">topic dedicated to adding vtkCubeAxesActor to the Slicer’s scene</a>, I think I should discuss  the mentionned problem there.</p>

---

## Post #15 by @keri (2021-09-01 19:51 UTC)

<p>I’m trying to set transfrom on camera but it seems that this only affect on 3D view:</p>
<pre><code class="lang-python"># Getting camera from 3D view
layoutManager = slicer.app.layoutManager()
view = layoutManager.threeDWidget(0).threeDView()
threeDViewNode = view.mrmlViewNode()
cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode(threeDViewNode)

# Getting camera
renderWindow = view.renderWindow()
renderers = renderWindow.GetRenderers()
renderer = renderers.GetItemAsObject(0)
camera = cameraNode.GetCamera()

# Create `transform` object and set scales for it
transform = vtk.vtkTransform()
transform.Scale(2, 1, 1)

# Apply transform to the camera
camera.SetModelTransformMatrix(transform.GetMatrix())
</code></pre>
<p>With this I get scaled 3D view but none of the Slice view is affected by scale. It seems that there is no camera on Slice view.</p>
<p>I understand that I can apply transform directly on volume but in this case coordinates of my object will be broken. I need to keep the original coordinates of object untouched…</p>
<p>What can I do to apply independently scale axes in slice view? I don’t fully understand yet how what are slice-views represented in sense of VTK objects, but probably I could set fake camera on them?</p>

---

## Post #16 by @lassoan (2021-09-02 23:41 UTC)

<p>You can change the aspect ratio of slice views by simply setting the desired field of view in the slice node.</p>

---

## Post #17 by @keri (2021-09-03 00:45 UTC)

<p>Thank you very much!</p>
<p>With this I see how to solve my issue with zooming. At least I think so <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
