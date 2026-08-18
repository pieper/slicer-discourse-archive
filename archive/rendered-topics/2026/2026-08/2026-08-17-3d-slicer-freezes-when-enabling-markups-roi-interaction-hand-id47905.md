---
topic_id: 47905
title: "3D Slicer Freezes When Enabling Markups ROI Interaction Handles"
date: 2026-08-17
url: https://discourse.slicer.org/t/47905
last_bumped: 2026-08-17T19:34:53.004Z
---

# 3D Slicer Freezes When Enabling Markups ROI Interaction Handles

**Topic ID**: 47905
**Date**: 2026-08-17
**URL**: https://discourse.slicer.org/t/3d-slicer-freezes-when-enabling-markups-roi-interaction-handles/47905

---

## Post #1 by @vedat_ozturk (2026-08-17 14:24 UTC)

<p>Problem report for 3D Slicer 5.12.3 win-amd64: [please describe expected and actual behavior]</p>
<p>Dear 3D Slicer Team,</p>
<p>I would greatly appreciate your help with a persistent and highly reproducible 3D rendering/freezing issue that I have been unable to resolve despite extensive troubleshooting.</p>
<p>I am an orthopedic surgeon and use 3D Slicer extensively for surgical planning and several custom scripted modules. The problem initially appeared around the time I attempted to move from Slicer 5.10 to Slicer 5.12.3. Importantly, the same computer had been running Slicer and my workflow without any problem for approximately one month before this occurred.</p>
<p>After many tests, the issue now appears to be much more specific than a general GPU, OpenGL, Volume Rendering, or extension problem. The most reproducible trigger we have identified is the <strong>3D interaction handles of a Markups ROI</strong>, particularly in a scene in which Volume Rendering is active.</p>
<h3><a name="p-135426-system-1" class="anchor" href="#p-135426-system-1" aria-label="Heading link"></a>System</h3>
<ul>
<li>
<p>Laptop: ASUS ProArt PX13</p>
</li>
<li>
<p>Model: HN7306EAC</p>
</li>
<li>
<p>Operating system: Windows 11</p>
</li>
<li>
<p>GPU: AMD Radeon™ 8060S Graphics</p>
</li>
<li>
<p>Slicer versions tested:</p>
<ul>
<li>
<p>5.10</p>
</li>
<li>
<p>5.12.3</p>
</li>
</ul>
</li>
<li>
<p>The problem occurs even on a completely clean Slicer installation with no custom extensions loaded.</p>
</li>
</ul>
<p>Current OpenGL report from Slicer:</p>
<pre><code class="lang-auto">OpenGL vendor string: ATI Technologies Inc.
OpenGL renderer string: AMD Radeon(TM) 8060S Graphics
OpenGL version string: 3.2.0 Core Profile Context 26.7.1.260716

</code></pre>
<p>Current AMD display driver:</p>
<pre><code class="lang-auto">Driver version: 32.0.31035.1003
AMD Adrenalin: 26.7.1
Driver date: 24 July 2026

</code></pre>
<p>The original ASUS/OEM driver was:</p>
<pre><code class="lang-auto">32.0.22032.6002
15 December 2025

</code></pre>
<p>The problem occurred with <strong>both drivers</strong>.</p>
<h3><a name="p-135426-important-timeline-2" class="anchor" href="#p-135426-important-timeline-2" aria-label="Heading link"></a>Important timeline</h3>
<p>The same laptop initially ran Slicer 5.10 normally for approximately one month.</p>
<p>The problem appeared around the time I attempted to install/use Slicer 5.12.3.</p>
<p>After the problem began:</p>
<ul>
<li>
<p>I returned to Slicer 5.10.</p>
</li>
<li>
<p>The problem remained.</p>
</li>
<li>
<p>I completely removed Slicer.</p>
</li>
<li>
<p>Slicer user configuration folders were removed.</p>
</li>
<li>
<p>Registry remnants related to Slicer were removed.</p>
</li>
<li>
<p>Slicer 5.10 and 5.12.3 were both tested independently.</p>
</li>
<li>
<p>Eventually, Windows itself was completely reset/reinstalled.</p>
</li>
<li>
<p>Slicer 5.12.3 was then installed again as a clean installation with no extensions.</p>
</li>
<li>
<p>The problem still occurred immediately.</p>
</li>
</ul>
<p>Therefore, this no longer appears to be caused by a corrupted Slicer installation, a custom extension, or a persistent Slicer preference.</p>
<p>I also tested the same Slicer 5.12.3 installation and my custom modules on another, less powerful computer, and they work normally there.</p>
<h3><a name="p-135426-main-clinicalworkflow-symptom-3" class="anchor" href="#p-135426-main-clinicalworkflow-symptom-3" aria-label="Heading link"></a>Main clinical/workflow symptom</h3>
<p>A CT can be loaded and Volume Rendering can initially be displayed normally.</p>
<p>However, when certain 3D objects or interaction mechanisms are introduced, Slicer freezes completely and may subsequently terminate.</p>
<p>One particularly reproducible example is:</p>
<p><strong>Volume Rendering → create/display a Markups ROI → Slicer freezes.</strong></p>
<p>Sometimes the ROI outline becomes visible first and then the application freezes.</p>
<p>The same behavior occurs independently of my custom modules.</p>
<h3><a name="p-135426-event-viewer-4" class="anchor" href="#p-135426-event-viewer-4" aria-label="Heading link"></a>Event Viewer</h3>
<p>During one Slicer 5.12.3 crash, Windows Event Viewer reported:</p>
<pre><code class="lang-auto">Faulting application:
SlicerApp-real.exe

Faulting module:
python312.dll

Exception code:
0xc0000005

</code></pre>
<p>There were also Application Hang / Event 1002 entries.</p>
<p>I realize that python312.dll being reported does not necessarily mean that Python itself is responsible, because the crash may occur in native VTK/OpenGL code invoked from Python.</p>
<h3><a name="p-135426-opengl-profile-tests-5" class="anchor" href="#p-135426-opengl-profile-tests-5" aria-label="Heading link"></a>OpenGL profile tests</h3>
<p>The application was launched using:</p>
<pre><code class="lang-auto">set SLICER_OPENGL_PROFILE=core

</code></pre>
<p>and separately:</p>
<pre><code class="lang-auto">set SLICER_OPENGL_PROFILE=no

</code></pre>
<p>The problem remained in both cases.</p>
<p>I also tried:</p>
<pre><code class="lang-auto">set VTK_USE_LEGACY_DEPTH_PEELING=1

</code></pre>
<p>The problem remained.</p>
<h3><a name="p-135426-depth-peeling-investigation-6" class="anchor" href="#p-135426-depth-peeling-investigation-6" aria-label="Heading link"></a>Depth peeling investigation</h3>
<p>Inspection of the renderers initially showed:</p>
<pre><code class="lang-auto">Renderer 0 | Layer: 0 | DepthPeeling: 1 | DepthPeelingForVolumes: True
Renderer 1 | Layer: 2 | DepthPeeling: 0 | DepthPeelingForVolumes: False
Renderer 2 | Layer: 1 | DepthPeeling: 0 | DepthPeelingForVolumes: False
Renderer 3 | Layer: 1 | DepthPeeling: 0 | DepthPeelingForVolumes: False
Renderer 4 | Layer: 1 | DepthPeeling: 1 | DepthPeelingForVolumes: False
Renderer 5 | Layer: 1 | DepthPeeling: 1 | DepthPeelingForVolumes: False

</code></pre>
<p>I then explicitly disabled both modes on <strong>all renderers</strong>:</p>
<pre><code class="lang-auto">rw = slicer.app.layoutManager().threeDWidget(0).threeDView().renderWindow()

renderers = rw.GetRenderers()
renderers.InitTraversal()

for i in range(renderers.GetNumberOfItems()):
    r = renderers.GetNextItem()
    r.SetUseDepthPeeling(False)
    r.SetUseDepthPeelingForVolumes(False)

rw.Render()

</code></pre>
<p>The resulting state was:</p>
<pre><code class="lang-auto">Renderer 0 | DepthPeeling: 0 | DepthPeelingForVolumes: False
Renderer 1 | DepthPeeling: 0 | DepthPeelingForVolumes: False
Renderer 2 | DepthPeeling: 0 | DepthPeelingForVolumes: False
Renderer 3 | DepthPeeling: 0 | DepthPeelingForVolumes: False
Renderer 4 | DepthPeeling: 0 | DepthPeelingForVolumes: False
Renderer 5 | DepthPeeling: 0 | DepthPeelingForVolumes: False

</code></pre>
<p>Even in this state, a normally created ROI could appear briefly and then Slicer would freeze.</p>
<p>Therefore, depth peeling alone does not appear to explain the problem.</p>
<h3><a name="p-135426-mesa-llvmpipe-test-7" class="anchor" href="#p-135426-mesa-llvmpipe-test-7" aria-label="Heading link"></a>Mesa / llvmpipe test</h3>
<p>This was one of the most important tests.</p>
<p>I used Mesa software OpenGL with:</p>
<pre><code class="lang-auto">set GALLIUM_DRIVER=llvmpipe
set MESA_GL_VERSION_OVERRIDE=3.3COMPAT

</code></pre>
<p>Under llvmpipe:</p>
<p><strong>the ROI worked and Slicer did not freeze.</strong></p>
<p>Performance was extremely slow, as expected from CPU software rendering, but the problematic functionality worked.</p>
<p>I also attempted the Mesa D3D12 backend, but Slicer did not start with that configuration.</p>
<p>This suggests that the hardware-accelerated/native graphics path is involved, although the subsequent tests below indicate that native AMD OpenGL itself is capable of rendering the relevant VTK primitives.</p>
<h3><a name="p-135426-basic-vtk-transparency-test-8" class="anchor" href="#p-135426-basic-vtk-transparency-test-8" aria-label="Heading link"></a>Basic VTK transparency test</h3>
<p>A completely independent VTK render window was created from the Slicer Python Interactor.</p>
<p>An opaque sphere rendered successfully.</p>
<p>The same sphere with:</p>
<pre><code class="lang-auto">actor.GetProperty().SetOpacity(0.25)

</code></pre>
<p>also rendered successfully.</p>
<p>The script reached:</p>
<pre><code class="lang-auto">1 - OPAQUE RENDER BASLIYOR
2 - OPAQUE RENDER TAMAM
3 - TRANSPARENT RENDER BASLIYOR
4 - TRANSPARENT RENDER TAMAM

</code></pre>
<p>Therefore:</p>
<p><strong>native AMD OpenGL + VTK translucent polydata works.</strong></p>
<h3><a name="p-135426-independent-vtk-volume-rendering-translucent-actor-test-9" class="anchor" href="#p-135426-independent-vtk-volume-rendering-translucent-actor-test-9" aria-label="Heading link"></a>Independent VTK Volume Rendering + translucent actor test</h3>
<p>I then created a separate <code>vtkRenderWindow</code> containing:</p>
<ul>
<li>
<p><code>vtkGPUVolumeRayCastMapper</code></p>
</li>
<li>
<p>a synthetic volume</p>
</li>
<li>
<p>a translucent <code>vtkSphereSource</code> actor</p>
</li>
</ul>
<p>Both were rendered simultaneously.</p>
<p>The test successfully reached:</p>
<pre><code class="lang-auto">1 - SADECE VOLUME BASLIYOR
2 - SADECE VOLUME TAMAM
3 - VOLUME + TRANSPARENT OBJE BASLIYOR
4 - VOLUME + TRANSPARENT OBJE TAMAM

</code></pre>
<p>Therefore:</p>
<p><strong>native AMD OpenGL + VTK GPU Volume Rendering + translucent polydata in the same renderer also works.</strong></p>
<p>This seems important because it argues against a general AMD OpenGL transparency or VTK GPU volume-rendering failure.</p>
<h3><a name="p-135426-test-inside-slicers-actual-3d-renderer-10" class="anchor" href="#p-135426-test-inside-slicers-actual-3d-renderer-10" aria-label="Heading link"></a>Test inside Slicer’s actual 3D renderer</h3>
<p>With Volume Rendering active, I inserted a simple <code>vtkCubeSource</code> wireframe actor directly into Slicer’s existing 3D renderer:</p>
<pre><code class="lang-auto">import vtk, slicer

view = slicer.app.layoutManager().threeDWidget(0).threeDView()
rw = view.renderWindow()

ren = rw.GetRenderers().GetFirstRenderer()

fp = ren.GetActiveCamera().GetFocalPoint()

cube = vtk.vtkCubeSource()
cube.SetCenter(fp[0], fp[1], fp[2])
cube.SetXLength(100)
cube.SetYLength(100)
cube.SetZLength(100)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cube.GetOutputPort())

testActor = vtk.vtkActor()
testActor.SetMapper(mapper)
testActor.GetProperty().SetRepresentationToWireframe()
testActor.GetProperty().SetLineWidth(3)
testActor.GetProperty().SetOpacity(1.0)

ren.AddActor(testActor)

print("CUBE RENDER START")
rw.Render()
print("CUBE RENDER COMPLETE")

</code></pre>
<p>The result was:</p>
<pre><code class="lang-auto">CUBE RENDER START
CUBE RENDER COMPLETE

</code></pre>
<p>Slicer remained responsive.</p>
<p>Therefore, Slicer’s main 3D renderer can also render additional VTK actors while Volume Rendering is active.</p>
<h3><a name="p-135426-most-important-finding-markups-roi-interaction-handles-11" class="anchor" href="#p-135426-most-important-finding-markups-roi-interaction-handles-11" aria-label="Heading link"></a>Most important finding: Markups ROI interaction handles</h3>
<p>We then created a Markups ROI programmatically while rendering was temporarily paused.</p>
<p>Before allowing its first render, the ROI was configured as follows:</p>
<pre><code class="lang-auto">d.SetFillVisibility(False)
d.SetOutlineVisibility(True)
d.SetOccludedVisibility(False)
d.SetHandlesInteractive(False)
d.SetPropertiesLabelVisibility(False)

</code></pre>
<p>Rendering was resumed.</p>
<p><strong>Result: the ROI appeared and Slicer remained completely responsive.</strong></p>
<p>In other words:</p>
<blockquote>
<p>Volume Rendering + Markups ROI with interaction handles disabled = WORKS.</p>
</blockquote>
<p>We then enabled the interaction handles:</p>
<pre><code class="lang-auto">d = roi.GetDisplayNode()

d.SetFillVisibility(False)
d.SetOccludedVisibility(False)

d.SetHandlesInteractive(True)
d.SetTranslationHandleVisibility(True)
d.SetRotationHandleVisibility(True)
d.SetScaleHandleVisibility(True)

print("HANDLE TEST START")
slicer.app.processEvents()
slicer.app.forceRenderAllViews()
print("HANDLE TEST COMPLETE")

</code></pre>
<p><strong>Slicer froze immediately.</strong></p>
<p>This is currently the most specific and reproducible trigger we have identified.</p>
<p>Therefore:</p>
<blockquote>
<p>Markups ROI without interaction handles → works<br>
Enabling Markups ROI interaction handles → immediate freeze</p>
</blockquote>
<p>This occurred with Volume Rendering active.</p>
<h3><a name="p-135426-cpu-volume-rendering-12" class="anchor" href="#p-135426-cpu-volume-rendering-12" aria-label="Heading link"></a>CPU Volume Rendering</h3>
<p>I also switched from GPU ray casting to CPU Volume Rendering.</p>
<p>The ROI interaction still caused the application to freeze.</p>
<p>Therefore, this does not appear to be specific to <code>vtkGPUVolumeRayCastMapper</code>.</p>
<h3><a name="p-135426-earlier-transparency-observation-13" class="anchor" href="#p-135426-earlier-transparency-observation-13" aria-label="Heading link"></a>Earlier transparency observation</h3>
<p>During earlier testing of one of my custom modules, a simple spherical model could be displayed at 100% opacity, while lowering its opacity initially caused a freeze.</p>
<p>Disabling depth peeling allowed that translucent sphere to work.</p>
<p>However, the later direct VTK tests described above showed that simple VTK transparency itself works correctly, and the ROI interaction-handle freeze remains even with all renderer depth-peeling flags explicitly disabled.</p>
<p>Therefore, I believe the ROI interaction-handle result is currently the more specific finding.</p>
<h3><a name="p-135426-what-appears-to-have-been-ruled-out-14" class="anchor" href="#p-135426-what-appears-to-have-been-ruled-out-14" aria-label="Heading link"></a>What appears to have been ruled out</h3>
<p>Based on these tests, the problem does <strong>not appear to be simply</strong>:</p>
<ul>
<li>
<p>a corrupted custom extension;</p>
</li>
<li>
<p>my scripted modules;</p>
</li>
<li>
<p>a corrupted Slicer installation;</p>
</li>
<li>
<p>Slicer user preferences;</p>
</li>
<li>
<p>a leftover Slicer registry entry;</p>
</li>
<li>
<p>one particular Slicer version;</p>
</li>
<li>
<p>one particular AMD driver version;</p>
</li>
<li>
<p>general inability of the Radeon 8060S to render 3D;</p>
</li>
<li>
<p>general OpenGL failure;</p>
</li>
<li>
<p>general VTK translucent polydata failure;</p>
</li>
<li>
<p>general VTK GPU Volume Rendering failure;</p>
</li>
<li>
<p>general simultaneous rendering of a volume and translucent actor;</p>
</li>
<li>
<p>Slicer’s basic main 3D renderer;</p>
</li>
<li>
<p>or depth peeling alone.</p>
</li>
</ul>
<p>The current evidence seems to point more specifically toward the <strong>Markups 3D interaction-widget / interaction-handle rendering path</strong>, potentially in combination with this particular hardware/OpenGL environment.</p>
<h3><a name="p-135426-what-remains-unexplained-15" class="anchor" href="#p-135426-what-remains-unexplained-15" aria-label="Heading link"></a>What remains unexplained</h3>
<p>The part I find particularly confusing is the chronology.</p>
<p>This exact laptop initially ran Slicer normally for approximately one month, including my normal 3D workflow.</p>
<p>The problem appeared around the time I attempted to migrate from Slicer 5.10 to Slicer 5.12.3.</p>
<p>However, after the problem appeared, returning to 5.10 did not solve it.</p>
<p>Even a complete Windows reset and clean Slicer reinstall did not restore the previous working behavior.</p>
<p>Therefore, I cannot determine whether:</p>
<ol>
<li>
<p>the timing of the 5.12.3 installation was coincidental;</p>
</li>
<li>
<p>an OS/graphics/runtime component changed at approximately the same time;</p>
</li>
<li>
<p>Slicer 5.12 exposed a latent interaction-widget/OpenGL issue;</p>
</li>
<li>
<p>there is a persistent system-level graphics/runtime condition that Windows Reset did not change;</p>
</li>
<li>
<p>or there is another explanation specific to Markups interaction rendering.</p>
</li>
</ol>
<h3><a name="p-135426-request-16" class="anchor" href="#p-135426-request-16" aria-label="Heading link"></a>Request</h3>
<p>Could you please advise whether this resembles any known issue involving:</p>
<ul>
<li>
<p><code>vtkSlicerMarkupsInteractionWidgetRepresentation</code></p>
</li>
<li>
<p>Markups ROI 3D interaction handles</p>
</li>
<li>
<p>interaction renderers/layers</p>
</li>
<li>
<p>Radeon 8060S / recent AMD OpenGL implementations</p>
</li>
<li>
<p>VTK OpenGL state management</p>
</li>
<li>
<p>or Markups interaction widgets combined with Volume Rendering?</p>
</li>
</ul>
<p>If useful, I would be happy to provide:</p>
<ul>
<li>
<p>full Slicer application logs;</p>
</li>
<li>
<p>Windows Event Viewer reports;</p>
</li>
<li>
<p>crash/hang dumps;</p>
</li>
<li>
<p>exact Python reproducer scripts;</p>
</li>
<li>
<p>screenshots/video of the freeze;</p>
</li>
<li>
<p>Slicer system information;</p>
</li>
<li>
<p>complete OpenGL capability output;</p>
</li>
<li>
<p>or test a patched build / Preview build / specific VTK change that you recommend.</p>
</li>
</ul>
<p>At this stage I would particularly appreciate guidance on how to obtain a useful stack trace or hang dump while the Markups interaction handles are causing the freeze, since that may help identify exactly where the rendering thread is blocked.</p>
<p>I have spent considerable time trying to isolate this issue, and the current minimal distinction — <strong>ROI works with interaction handles disabled but freezes immediately when they are enabled</strong> — is the most reproducible finding so far.</p>
<p>Thank you very much for your time and assistance.</p>
<p>Best regards,</p>
<p>Vedat Öztürk, MD<br>
Orthopaedic Surgeon<br>
Istanbul, Türkiye</p>

---

## Post #2 by @lassoan (2026-08-17 14:36 UTC)

<p>You can try removing the settings file (or the entire Slicer settings folder) - <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location" class="inline-onebox">Application settings — 3D Slicer documentation</a></p>
<p>You can also try to downgrade your graphics driver to a few versions that were released half year to 1-2 years ago.</p>
<p>It may also be possible that some software that you installed interferes. Check the list of DLLs that the SlicerApp-real.exe process loaded and see if anything looks out of place (such as a non-system DLL that is loaded outside of the Slicer folder).</p>
<p>It seems that you could use an LLM quite effectively to diagnose the problem, so you may also be able to build Slicer in debug mode, which would allow you to get detailed call stack and even add debug logs and instrumentation. If you have a debug-mode build and a way to reproduce the issue in debug mode but you are not sure how to resolve the problem then you could ask a quick meeting with a Slicer developer to check what’s wrong.</p>

---

## Post #3 by @vedat_ozturk (2026-08-17 19:34 UTC)

<p>Thank you for the suggestions. I followed several of them and performed some additional controlled tests, which helped narrow the problem down considerably.</p>
<p>I completely removed the Slicer settings/profile folders, tested with a new Windows user, performed clean Slicer reinstalls, and also checked the DLLs loaded into <code>SlicerApp-real.exe</code>. Norton DLLs were initially present, so I completely removed Norton and repeated the test, but the freeze remained. I also reset/reinstalled Windows previously, without any change.</p>
<p>I reproduced the problem with both the ASUS/OEM AMD driver and AMD Adrenalin 26.7.1. I have <strong>not yet performed a systematic rollback through 6–24 month old AMD drivers</strong>.</p>
<p>Some controlled tests were interesting: generic VTK transparency and GPU volume rendering work correctly, and a simple VTK actor also renders normally inside Slicer. However, with Volume Rendering active, a Markups ROI works with interaction handles disabled, while enabling the translation/rotation/scale handles reproducibly freezes Slicer. Mesa/llvmpipe software rendering avoids the freeze.</p>
<p>I also captured a hang dump and analyzed it with WinDbg. <code>!analyze -hang</code> reports:</p>
<p><code>APPLICATION_HANG_BusyHang_cfffffff_atio6axx.dll!Unknown</code></p>
<p>The main GUI/render thread is stuck in:</p>
<p><code>vtkDualDepthPeelingPass::EndTranslucentOcclusionQuery</code><br>
<code>→ vtkDualDepthPeelingPass::Peel</code><br>
<code>→ vtkDualDepthPeelingPass::Render</code><br>
<code>→ vtkOpenGLRenderer::DeviceRenderTranslucentPolygonalGeometry</code><br>
<code>→ atio6axx.dll</code></p>
<p>So the hang appears to occur in the VTK dual-depth-peeling/translucency rendering path when it reaches the AMD OpenGL driver. I cannot determine from this alone whether the root cause is the AMD driver, VTK, or Slicer’s rendering configuration.</p>
<p>I can provide the WinDbg thread dump and the minimal Python reproducer if useful.</p>

---
