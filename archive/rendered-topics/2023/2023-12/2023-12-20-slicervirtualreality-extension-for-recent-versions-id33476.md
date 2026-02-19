---
topic_id: 33476
title: "Slicervirtualreality Extension For Recent Versions"
date: 2023-12-20
url: https://discourse.slicer.org/t/33476
---

# SlicerVirtualReality extension for recent versions

**Topic ID**: 33476
**Date**: 2023-12-20
**URL**: https://discourse.slicer.org/t/slicervirtualreality-extension-for-recent-versions/33476

---

## Post #1 by @Billuc (2023-12-20 20:36 UTC)

<p>Hi !<br>
I am new to Slicer, but I am interested in the SlicerVirtualReality extension. I wanted to try it with the latest versions of Slicer (5.6 or 5.7), but I couldn’t find it in the extension manager, while I could find it with Slicer 5.2.2.<br>
Has this extension not been compiled for the most recent versions ? Do I have to compile it myself if I want to try it out ?</p>
<p>Thanks in advance.<br>
Luc</p>

---

## Post #2 by @muratmaga (2023-12-21 05:00 UTC)

<p>I believe it is broken for current stable and preview. Use it with 5.4.</p>

---

## Post #3 by @jcfr (2023-12-21 07:58 UTC)

<p>The extension is actively being worked on and you should expect a working OpenVR, OpenXR as well as experimental OpenXRRemoting integration within 1 or 2 weeks. Thanks for your patience <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @Billuc (2024-01-10 16:00 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> I tried to use the extension today, as I saw you made updates and the extension was available for Slicer5.6.1. I could install it, but I got some problems…<br>
I have a Meta Quest 2, so that is maybe part of the reason why I got these problems, but I thought that since I could use SteamVR, it should work.<br>
The thing is that whatever I do, whatever option I change, whatever data I try to open, I always get the same result : a blank scene, with the controllers at the top of my FOV (moving alongside my head, but also moving when I move the controller) and no model appearing (or not in my FOV).</p>
<p>Are you aware of this ? Or maybe the new version isn’t stable yet ?<br>
Thanks in advance.<br>
Luc</p>

---

## Post #5 by @pieper (2024-01-10 19:19 UTC)

<p>I don’t know if it’s still an issue, but at one point I know that you needed to have some data loaded in the Slicer scene for the VR to initialize correctly.</p>

---

## Post #6 by @Billuc (2024-01-11 08:11 UTC)

<p>Unfortunately, I did have some data loaded. I haven’t tried initializing the VR before loading data, might try later…</p>

---

## Post #7 by @petr.raunigr (2024-12-11 14:40 UTC)

<p>Sorry for re-opening a long dead post… did you (or anyone else) ever figured it out? I’m dealing with the exact same issue… blank space and controllers hanging at top of my FOV (rotating correctly).</p>
<p>Thanks.</p>

---

## Post #8 by @cpinter (2024-12-11 15:23 UTC)

<p>Are you using the latest Slicer? Which backend do you use OpenXR or OpenVR (via SteamVR)?</p>

---

## Post #9 by @petr.raunigr (2024-12-12 08:55 UTC)

<p>Hello, so…</p>
<p><strong>3D Slicer</strong>: 5.7.0-2024-11-26 r33130 / c5e8d83<br>
<strong>SlicerVirtualReality</strong>: cloned 3. 12. 2024 (can’t find version info)<br>
<strong>SteamVR</strong>: 2.8.8<br>
<strong>Varjo Base</strong>: 4.3.0.14 (available update to 4.5.1.18)</p>
<p>My setup consists of HTC Vive controllers (1st edition) and Varjo Aero headset + SteamVR.</p>
<p>I tried to use SteamVR OpenXR, I also tried to set Varjo (in their software Varjo Base) as an OpenXR provider + OpenVR provider.</p>
<p>In SlicerVirtualReality settings I tried to set OpenXR and also OpenVR but I have the same problem for both of them but there are few differencies.</p>
<p><em>(Examples below were captured with no data loaded. It doesn’t matter because even if I load any kind of data the result would be the same)</em></p>
<p><strong>Set OpenXR</strong></p>
<details>
<summary>
Console output</summary>
<p>Switch to module:  “Welcome”<br>
Switch to module:  “VirtualReality”<br>
Initializing “OpenXR” XR backend (1/1)<br>
void __cdecl qMRMLVirtualRealityView::updateViewFromReferenceViewCamera(void)  failed: no reference view node is set<br>
Optional extensions HandTracking is supported<br>
Runtime Name: SteamVR/OpenXRRuntime Version: 2.8.8<br>
Debug: In vtkOpenXRManager.cxx, line 879<br>
(nullptr): Successfully got XrSystem with id 1153015959527621024 for HMD form factor.</p>
<p>System Properties for system id:1153015959527621024, with name “SteamVR/OpenXR : lighthouse”, vendorID=10462<br>
Max Layers          : 16<br>
Max Swapchain Height: 2692<br>
Max Swapchain Width : 3140<br>
Orientation Tracking: True<br>
Position Tracking   : True<br>
Hand Tracking       : 1<br>
Runtime supports 1 view configurations<br>
Type XR_VIEW_CONFIGURATION_TYPE_PRIMARY_STEREO: FOV mutable: True<br>
Runtime supports 3 reference spaces:<br>
XR_REFERENCE_SPACE_TYPE_VIEW<br>
XR_REFERENCE_SPACE_TYPE_LOCAL<br>
XR_REFERENCE_SPACE_TYPE_STAGE<br>
Debug: In vtkOpenXRManager.cxx, line 1030<br>
(nullptr): Runtime supports 8 swapchain formats</p>
<p>View Configuration View 0<br>
Resolution       : Recommended: 3140x2692, Max: 8192x8192<br>
Swapchain Samples: Recommended: 1, Max: 1<br>
View Configuration View 1<br>
Resolution       : Recommended: 3140x2692, Max: 8192x8192<br>
Swapchain Samples: Recommended: 1, Max: 1<br>
XR backend " OpenXR " initialized<br>
ActionManifestPath: “D:/Slicer_plugins/SlicerVirtualReality/build_debug/vtkRenderingOpenXR-build/vtkRenderingOpenXR/”<br>
Number of registered displayable manager: 8<br>
Registered displayable managers:<br>
vtkMRMLModelDisplayableManager<br>
vtkMRMLThreeDReformatDisplayableManager<br>
vtkMRMLCrosshairDisplayableManager3D<br>
vtkMRMLMarkupsDisplayableManager<br>
vtkMRMLSegmentationsDisplayableManager3D<br>
vtkMRMLTransformsDisplayableManager3D<br>
vtkMRMLLinearTransformsDisplayableManager<br>
vtkMRMLVolumeRenderingDisplayableManager<br>
Debug: In vtkOpenXRManager.cxx, line 264<br>
(nullptr): Session started.</p>
<p>Debug: In vtkOpenXRManager.cxx, line 1197<br>
(nullptr): Create action set vtk-actions: VTK actions</p>
<p>Debug: In vtkOpenXRManager.cxx, line 1349<br>
(nullptr): SuggestActions for profile : /interaction_profiles/khr/simple_controller</p>
<p>Debug: In vtkOpenXRManager.cxx, line 1349<br>
(nullptr): SuggestActions for profile : /interaction_profiles/htc/vive_controller</p>
<p>Debug: In vtkOpenXRManager.cxx, line 1349<br>
(nullptr): SuggestActions for profile : /interaction_profiles/oculus/touch_controller</p>
<p>Debug: In vtkOpenXRManager.cxx, line 1349<br>
(nullptr): SuggestActions for profile : /interaction_profiles/hp/mixed_reality_controller</p>
<p>Debug: In vtkOpenXRManager.cxx, line 1349<br>
(nullptr): SuggestActions for profile : /interaction_profiles/valve/index_controller</p>
<p>Debug: In vtkOpenXRManager.cxx, line 1349<br>
(nullptr): SuggestActions for profile : /interaction_profiles/microsoft/hand_interaction</p>
<p>Debug: In vtkOpenXRManager.cxx, line 552<br>
(nullptr): Could not suggest actions [XR_ERROR_PATH_UNSUPPORTED].</p>
<p>failed at glDeleteFramebuffers 16 OpenGL errors detected<br>
0 : (1282) Invalid operation<br>
1 : (1282) Invalid operation<br>
2 : (1282) Invalid operation<br>
3 : (1282) Invalid operation<br>
4 : (1282) Invalid operation<br>
5 : (1282) Invalid operation<br>
6 : (1282) Invalid operation<br>
7 : (1282) Invalid operation<br>
8 : (1282) Invalid operation<br>
9 : (1282) Invalid operation<br>
10 : (1282) Invalid operation<br>
11 : (1282) Invalid operation<br>
12 : (1282) Invalid operation<br>
13 : (1282) Invalid operation<br>
14 : (1282) Invalid operation<br>
15 : (1282) Invalid operation</p>
<p>failed at glDeleteFramebuffers 16 OpenGL errors detected<br>
0 : (1282) Invalid operation<br>
1 : (1282) Invalid operation<br>
2 : (1282) Invalid operation<br>
3 : (1282) Invalid operation<br>
4 : (1282) Invalid operation<br>
5 : (1282) Invalid operation<br>
6 : (1282) Invalid operation<br>
7 : (1282) Invalid operation<br>
8 : (1282) Invalid operation<br>
9 : (1282) Invalid operation<br>
10 : (1282) Invalid operation<br>
11 : (1282) Invalid operation<br>
12 : (1282) Invalid operation<br>
13 : (1282) Invalid operation<br>
14 : (1282) Invalid operation<br>
15 : (1282) Invalid operation</p>
<p>failed at glDeleteFramebuffers 16 OpenGL errors detected<br>
0 : (1282) Invalid operation<br>
1 : (1282) Invalid operation<br>
2 : (1282) Invalid operation<br>
3 : (1282) Invalid operation<br>
4 : (1282) Invalid operation<br>
5 : (1282) Invalid operation<br>
6 : (1282) Invalid operation<br>
7 : (1282) Invalid operation<br>
8 : (1282) Invalid operation<br>
9 : (1282) Invalid operation<br>
10 : (1282) Invalid operation<br>
11 : (1282) Invalid operation<br>
12 : (1282) Invalid operation<br>
13 : (1282) Invalid operation<br>
14 : (1282) Invalid operation<br>
15 : (1282) Invalid operation</p>
<p>failed at glDeleteFramebuffers 16 OpenGL errors detected<br>
0 : (1282) Invalid operation<br>
1 : (1282) Invalid operation<br>
2 : (1282) Invalid operation<br>
3 : (1282) Invalid operation<br>
4 : (1282) Invalid operation<br>
5 : (1282) Invalid operation<br>
6 : (1282) Invalid operation<br>
7 : (1282) Invalid operation<br>
8 : (1282) Invalid operation<br>
9 : (1282) Invalid operation<br>
10 : (1282) Invalid operation<br>
11 : (1282) Invalid operation<br>
12 : (1282) Invalid operation<br>
13 : (1282) Invalid operation<br>
14 : (1282) Invalid operation<br>
15 : (1282) Invalid operation</p>
</details>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71b28e35f989ab3a852d45946ad87a56c944e5f6.png" data-download-href="/uploads/short-url/gdOvt8gSRrDjbCc3NVP3VzPGwOq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71b28e35f989ab3a852d45946ad87a56c944e5f6.png" alt="image" data-base62-sha1="gdOvt8gSRrDjbCc3NVP3VzPGwOq" width="407" height="255"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">407×255 11.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Instead of a green headset icon + two green controllers icons I get this orange warning (sometimes there are all 3 of them).<br>
<strong>Also I don’t see controller models in VR but only green triangles.</strong></p>
<p><strong>Set OpenVR</strong></p>
<details>
<summary>
Console output</summary>
<p>Switch to module:  “Welcome”<br>
Switch to module:  “VirtualReality”<br>
Initializing “OpenVR” XR backend (1/1)<br>
void __cdecl qMRMLVirtualRealityView::updateViewFromReferenceViewCamera(void)  failed: no reference view node is set<br>
XR backend " OpenVR " initialized<br>
ActionManifestPath: “D:/Slicer_plugins/SlicerVirtualReality/build_debug/vtkRenderingOpenVR-build/vtkRenderingOpenVR/”<br>
Number of registered displayable manager: 8<br>
Registered displayable managers:<br>
vtkMRMLModelDisplayableManager<br>
vtkMRMLThreeDReformatDisplayableManager<br>
vtkMRMLCrosshairDisplayableManager3D<br>
vtkMRMLMarkupsDisplayableManager<br>
vtkMRMLSegmentationsDisplayableManager3D<br>
vtkMRMLTransformsDisplayableManager3D<br>
vtkMRMLLinearTransformsDisplayableManager<br>
vtkMRMLVolumeRenderingDisplayableManager</p>
</details>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a95e77f024940c45771987b8619d6915b43ce8fb.png" data-download-href="/uploads/short-url/oaj5Bj9uvHzsE1TLMUoj9Y7pkAb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a95e77f024940c45771987b8619d6915b43ce8fb.png" alt="image" data-base62-sha1="oaj5Bj9uvHzsE1TLMUoj9Y7pkAb" width="414" height="238"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">414×238 10.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This time there is a correct icon for a headset and sometimes also for controllers (don’t know what causes controller icons to show up though).</p>
<p>This time I can see controller models in VR but they have the same problem… sitting at top of my FOV. Moreover, I can see a strange cube/square:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb728f1b615b44782a12cdfeeee931d9f44fcd59.png" data-download-href="/uploads/short-url/xARE7tqybRaao1FxSAzBgT1GQFX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb728f1b615b44782a12cdfeeee931d9f44fcd59_2_665x500.png" alt="image" data-base62-sha1="xARE7tqybRaao1FxSAzBgT1GQFX" width="665" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb728f1b615b44782a12cdfeeee931d9f44fcd59_2_665x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb728f1b615b44782a12cdfeeee931d9f44fcd59_2_997x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb728f1b615b44782a12cdfeeee931d9f44fcd59.png 2x" data-dominant-color="9497CF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1004×754 3.45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>A possible clue</strong><br>
I see controllers and the cube (in case of OpenVR) twice… like if it’s rendered for both eyes separately or no depth perception is happening.</p>
<p><strong>Summary</strong>:<br>
I tried to use OpenVR, OpenXR, switch between OpenXR/VR provider from SteamVR to Varjo Base and back. I tried loading MHD data and tried VR without loading any data. The only difference I can see are different icons representing VR headset and controllers in 3D Slicer and different controller models in VR (green triangles for OpenXR, correct models for OpenVR) + in case of OpenVR I also see a cube/square. I also can see controller models/triangles + cube for each eye separately.</p>
<p>EDIT:<br>
If I select OpenVR and in SlicerVirtualReality settings check the “Controller Transform” option this errors spam my console:</p>
<details>
<summary>
Console output</summary>
<p>void __cdecl qMRMLVirtualRealityViewPrivate::updateTransformNodeAttributesFromDevice(class vtkMRMLTransformNode *,enum vtkEventDataDevice,unsigned int) : Unable to retrieve LeftController pose<br>
void __cdecl qMRMLVirtualRealityViewPrivate::updateTransformNodeAttributesFromDevice(class vtkMRMLTransformNode *,enum vtkEventDataDevice,unsigned int) : Unable to retrieve RightController pose</p>
</details>

---

## Post #10 by @petr.raunigr (2024-12-18 12:25 UTC)

<p>Ok, so the problem was more about me not knowing how to work with 3D Slicer rather than a bug in the extension.</p>
<p>As I mentioned, I loaded data, drag and dropped a volume model into the 3D scene and I thought that’s it.</p>
<p>What I needed to do was to check VirtualRealityVIew in the Volume Rendering module (see the screenshot below). Other thing that properly initialized a VR scene was to add one of the 3 CT slices into the 3D scene.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/2896d91d738e3e576b2522ff58fd008b881a715d.jpeg" data-download-href="/uploads/short-url/5N4hWqDt1BxEz1MHnhNzeyYm1iJ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/2896d91d738e3e576b2522ff58fd008b881a715d_2_690x259.jpeg" alt="image" data-base62-sha1="5N4hWqDt1BxEz1MHnhNzeyYm1iJ" width="690" height="259" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/2896d91d738e3e576b2522ff58fd008b881a715d_2_690x259.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/2896d91d738e3e576b2522ff58fd008b881a715d_2_1035x388.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/2896d91d738e3e576b2522ff58fd008b881a715d.jpeg 2x" data-dominant-color="676073"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1049×394 84.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bbe7f46a64bed6363a8dc96a4a7ea456e76e829.jpeg" data-download-href="/uploads/short-url/mdM946br0dr2WQr2aNbzrJ2DtOh.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bbe7f46a64bed6363a8dc96a4a7ea456e76e829_2_690x383.jpeg" alt="image" data-base62-sha1="mdM946br0dr2WQr2aNbzrJ2DtOh" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bbe7f46a64bed6363a8dc96a4a7ea456e76e829_2_690x383.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bbe7f46a64bed6363a8dc96a4a7ea456e76e829_2_1035x574.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bbe7f46a64bed6363a8dc96a4a7ea456e76e829_2_1380x766.jpeg 2x" data-dominant-color="7E7C80"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1493×829 89.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>UX proposition</strong><br>
I find it still a bit weird that not doing that I don’t have a properly running VR scene (problems described in the previous post). I would expect that if I don’t properly prepare a model/data that I would at least end up with an empty VR space with controllers properly synced etc.</p>

---

## Post #11 by @cpinter (2024-12-18 15:26 UTC)

<p>The VR view is not added to the views where the volume rendering appears, because by the time you show it, there is no VR view yet. So it needs to be manually added if you do things in this order. Great that you figured this out yourself! (I think that there have been topics here in the forum where we describe this though)</p>
<aside class="quote no-group" data-username="petr.raunigr" data-post="10" data-topic="33476">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/2acd7d/48.png" class="avatar"> petr.raunigr:</div>
<blockquote>
<p>empty VR space with controllers properly synced etc.</p>
</blockquote>
</aside>
<p>I agree. I’m not sure why not even the controllers appear. Maybe it’s the result of the undefined view parameters.</p>

---
