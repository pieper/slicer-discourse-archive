---
topic_id: 24267
title: "Can Multi Volume Rendering With Two Volumes Overlapped Impor"
date: 2022-07-11
url: https://discourse.slicer.org/t/24267
---

# Can Multi-Volume Rendering with two volumes overlapped imporved performance?

**Topic ID**: 24267
**Date**: 2022-07-11
**URL**: https://discourse.slicer.org/t/can-multi-volume-rendering-with-two-volumes-overlapped-imporved-performance/24267

---

## Post #1 by @StephenLeePeng (2022-07-11 07:48 UTC)

<p>Hi everybody,<br>
Recently I researched multi-volume rendering.<br>
The situation is I have to render the lung nodule, the vessel and pleura arround the nodule.<br>
The lung nodule is first volume, and the vessel and pleura is second volume.<br>
As the HU value and location in those two volumes exist overlap, but I want to render two volumes with different opacity, color and gradient transfer functions.<br>
When I load two volume nodes, switch to volume rendering module, set the proper opacity, gradient and color transfer func seprately, and choose “VTK GPU Ray Casting”, two volumes could be rendered  well as expected. But defect of this render method is lack of Spatial location, and render result seems not real.<br>
Because the lung nodule is inside the pleura, but when I rotate the volumes in 3d view, in some angle, the lung nodule would be hided by the pleura, not inside the pleura.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3ad7f0d00a400b6c4381e338ea9aa2b2cf4a35f9.jpeg" data-download-href="/uploads/short-url/8oylkw6CYwRnf5oAcceOi19SOAV.jpeg?dl=1" title="render1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ad7f0d00a400b6c4381e338ea9aa2b2cf4a35f9_2_690x444.jpeg" alt="render1" data-base62-sha1="8oylkw6CYwRnf5oAcceOi19SOAV" width="690" height="444" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ad7f0d00a400b6c4381e338ea9aa2b2cf4a35f9_2_690x444.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3ad7f0d00a400b6c4381e338ea9aa2b2cf4a35f9.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3ad7f0d00a400b6c4381e338ea9aa2b2cf4a35f9.jpeg 2x" data-dominant-color="363423"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">render1</span><span class="informations">1009×650 53.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76c669bdf855362b0b707873c2061b7db441b0a4.jpeg" data-download-href="/uploads/short-url/gWJrfwzjUQ1PbPOknJrTEblzp7S.jpeg?dl=1" title="render2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76c669bdf855362b0b707873c2061b7db441b0a4_2_590x500.jpeg" alt="render2" data-base62-sha1="gWJrfwzjUQ1PbPOknJrTEblzp7S" width="590" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/76c669bdf855362b0b707873c2061b7db441b0a4_2_590x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76c669bdf855362b0b707873c2061b7db441b0a4.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76c669bdf855362b0b707873c2061b7db441b0a4.jpeg 2x" data-dominant-color="7A6B40"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">render2</span><span class="informations">734×622 49.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
When I choose the “VTK Multi-Volume (experimental)” method, the two volumes could be rendered in the same time, and the Spatial location is right even though I rotate the volumes many times.<br>
But the defect of this multi-volume render method is,  the detail of volume disappeared, the vessel and pleura became not continuous and blurred.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f76f1cee5271615c79f3bb586af15f0ae09688f.jpeg" data-download-href="/uploads/short-url/kt97beub9P1UcNVtEN8e8qomp2v.jpeg?dl=1" title="render3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f76f1cee5271615c79f3bb586af15f0ae09688f_2_542x500.jpeg" alt="render3" data-base62-sha1="kt97beub9P1UcNVtEN8e8qomp2v" width="542" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f76f1cee5271615c79f3bb586af15f0ae09688f_2_542x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f76f1cee5271615c79f3bb586af15f0ae09688f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f76f1cee5271615c79f3bb586af15f0ae09688f.jpeg 2x" data-dominant-color="6A6140"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">render3</span><span class="informations">709×654 74.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When I test the vtkMultiVolume outside the Slicer, use the vtkMultiVolume and vtkGPUVolumeRayCastMapper class, set the same parameters for two volumes, the rendering result is as expected.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/119f73bff2da8795cb2a58f9d0ab00f0eb7418c1.jpeg" data-download-href="/uploads/short-url/2vTJYTAlfNPwwAuy2pByha8xEzL.jpeg?dl=1" title="azimuth_260" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/119f73bff2da8795cb2a58f9d0ab00f0eb7418c1_2_500x500.jpeg" alt="azimuth_260" data-base62-sha1="2vTJYTAlfNPwwAuy2pByha8xEzL" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/119f73bff2da8795cb2a58f9d0ab00f0eb7418c1_2_500x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/119f73bff2da8795cb2a58f9d0ab00f0eb7418c1_2_750x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/119f73bff2da8795cb2a58f9d0ab00f0eb7418c1_2_1000x1000.jpeg 2x" data-dominant-color="3C3924"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">azimuth_260</span><span class="informations">1024×1024 50.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So I want to know the differences between the multiVolume rendering in Slicer and use vtk class directly? Why the effect in Slicer 3d view is lower than in VTK render window? And how can I improve the vtkMultiVolume rendering performand in Slicer?<br>
Any suggestion will be appreciate~<br>
And thanks to <a class="mention" href="/u/lassoan">@lassoan</a>  <a class="mention" href="/u/muratmaga">@muratmaga</a>  <a class="mention" href="/u/pieper">@pieper</a>  <a class="mention" href="/u/cpinter">@cpinter</a>  in advance, expect to your<br>
professional answer and advices.</p>

---

## Post #2 by @pieper (2022-07-11 19:13 UTC)

<p>Thanks for testing and reporting <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> I haven’t looked at the details myself but I’m sure there are issues with the multivolume rendering that need to be investigated and fixed.  The feature was added to Slicer a few years ago but VTK has been upgraded since then and I don’t know if we are taking advantage of any recent fixes.  Based on the images you showed it could be <a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Modules/Loadable/VolumeRendering/MRMLDM/vtkMRMLVolumeRenderingDisplayableManager.cxx">some of the logic</a> around updating sample distances or similar.</p>

---

## Post #3 by @StephenLeePeng (2022-07-12 02:08 UTC)

<p>I have forgotten to tell the Slicer version and vtk version.<br>
What I have tested VTK Multi-Volume rendering, is in the <strong>Slicer-4.13.0-2022-01-16-linux-amd64</strong> Nightly build version, and from the python terminal, I got the vtk.vtkVersion().GetVTKSourceVersion() is ‘<strong>vtk version 9.0.0</strong>’.<br>
Certainly, I also download the latest Slicer, version is: <strong>Slicer-5.1.0-2022-06-24-linux-amd64</strong>, and vtk version is also 9.0.0. But the multi-volume rendering effect is also not improved.<br>
<a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #4 by @lassoan (2022-07-12 03:11 UTC)

<p>I’ve checked this and I was able to reproduce the issue. It seems to be a known issue (see <a href="https://github.com/Slicer/Slicer/issues/5238" class="inline-onebox">MultiVolume Rendering quality is very low if volume spacing is small · Issue #5238 · Slicer/Slicer · GitHub</a>). I’ll fix this, but it is not a simple problem (it involves fixing multi-volume rendering in VTK or complex workarounds in Slicer - see details below).</p>
<p>Fortunately, for your use case, multi-volume rendering is not needed. General anatomical environment can be visualized nicely using volume rendering, but lesions, devices, other structures of interest are typically displayed as segmentation. Segmentation has many advantages, including clear visualization in both slice and 3D views, good-quality visualization even if the structure has low contrast or wide intensity range, and the segmentation can be used for quantification (volume, intensity statistics, radiomics features, etc.).</p>
<hr>
<p>Details about the multi-volume rendering issue: Slicer always instructed VTK to use adaptive rendering quality, which ended up choosing somewhat lower quality rendering (larger sampling distance) than the default single-volume volume renderer. When I’ve fixed this logic it turned out that the automatic sampling distance computation in the multi-volume renderer computes the sampling distance based on the very first volume. In Slicer, this volume is an empty volume because VTK has a bug that the first volume’s transform is not taken into account. I’ll have to see if it is easier to fix the issues in VTK or develop more complicated workarounds in Slicer. This will probably take a few weeks to sort out. You can track the status of this issue here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5238">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5238" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5238" target="_blank" rel="noopener">MultiVolume Rendering quality is very low if volume spacing is small</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-10-09" data-time="04:55:13" data-timezone="UTC">04:55AM - 09 Oct 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/SlicerMorph" target="_blank" rel="noopener">
          <img alt="SlicerMorph" src="https://avatars.githubusercontent.com/u/45026482?v=4" class="onebox-avatar-inline" width="20" height="20">
          SlicerMorph
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">[Give a short summary of what the problem is]
Description from https://discours<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">e.slicer.org/t/multi-volume-rendering-bug/13939/5?u=muratmaga

`The problem is that automatic sampling step computation does not work in the multivolume renderer, so the image spacing has to be approximately 1 to get good-quality rendering. `

## Environment
- Slicer version: Slicer-4.11-2020-09-30
- Operating system: Windows</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @StephenLeePeng (2022-07-13 12:58 UTC)

<p>Thank you for your professional advice. <a class="mention" href="/u/lassoan">@lassoan</a>  <a class="mention" href="/u/pieper">@pieper</a><br>
But in my situation, I can’t replace Multi-Volume Rendering with Segmentation show 3D. Becuase density and type of lesion/nodule is different, I will rendering by different opacity, color tranfer funcs.<br>
But if I use segmentation show 3d, the color of the segmentation in 3d view is only one color, not with different color by different diensity.</p>
<p>To my surprise, according to use segmentation show 3d, lack of Spatial location may be solved.<br>
The steps reproduce is as follows:</p>
<ol>
<li>segmentation show 3d;</li>
<li>set the opacity to 0.01;</li>
<li>Switch to View Controller, set the UseDepthPeeling to True;</li>
<li>Swith to Volume Rendering, and VTK GPU ray casting rendering;</li>
<li>Open the nodule and vessel two different volume to rendering;</li>
<li>OK.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c7f78e6d14f3a35142d3d13271025e7a78732a1.jpeg" data-download-href="/uploads/short-url/6lE7eUE8a4vQQEEN61WAyIAfpeh.jpeg?dl=1" title="001" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c7f78e6d14f3a35142d3d13271025e7a78732a1_2_690x377.jpeg" alt="001" data-base62-sha1="6lE7eUE8a4vQQEEN61WAyIAfpeh" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c7f78e6d14f3a35142d3d13271025e7a78732a1_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c7f78e6d14f3a35142d3d13271025e7a78732a1_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2c7f78e6d14f3a35142d3d13271025e7a78732a1_2_1380x754.jpeg 2x" data-dominant-color="282923"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">001</span><span class="informations">1846×1009 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e9f5551422c7ba79dd641bc1db214664df85877.jpeg" data-download-href="/uploads/short-url/bdwBZ2CMObThVzIHau2MWaTokpF.jpeg?dl=1" title="002" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e9f5551422c7ba79dd641bc1db214664df85877_2_690x357.jpeg" alt="002" data-base62-sha1="bdwBZ2CMObThVzIHau2MWaTokpF" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e9f5551422c7ba79dd641bc1db214664df85877_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e9f5551422c7ba79dd641bc1db214664df85877_2_1035x535.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e9f5551422c7ba79dd641bc1db214664df85877_2_1380x714.jpeg 2x" data-dominant-color="3B3E36"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">002</span><span class="informations">1708×884 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I don’t know why, but the VTK GPU Ray Casting to render two different volume, lack of Spatial Location may be solved, seems to be ok.<br>
I want to know why?</p>

---

## Post #6 by @lassoan (2022-07-13 13:21 UTC)

<aside class="quote no-group" data-username="StephenLeePeng" data-post="5" data-topic="24267">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stephenleepeng/48/11892_2.png" class="avatar"> StephenLeePeng:</div>
<blockquote>
<p>Becuase density and type of lesion/nodule is different,</p>
</blockquote>
</aside>
<p>This is exactly why segmentation is even much easier and more appropriate for visualizing the lesions than volume rendering. Volume rendering is essentially simple global thresholding (with a smooth threshold and some coloring and transparency effects). In contrast, you can segment arbitrarily complex shapes with subtle, local, spatially varying contrast, with even incorporating prior information about the expected shape, location, and appearance of the structure.</p>
<p>3D appearance of a single volume rendered image and any number of segments will be correct (each object will only occluding other objects that are behind it). Rendering of segmentations is also much faster than multi-volume rendering.</p>

---

## Post #7 by @StephenLeePeng (2022-07-14 02:46 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Thank you for your explaination, but I think you may not understand me totally.</p>
<p>Althrough I use segmentation rendering in 3D view, but the opacity of segmentation is set  to only 0.01, is totally transparent.<br>
Finally, there are three object to be rendered in 3D view:<br>
(1) nodule volume,<br>
(2) vessel and pleura volume,<br>
(3) nodule segmentation.<br>
As nodule segmentation is nearly to transparent, there are two objects rendered will be seen actually.</p>
<p><strong>What confuses me is that, If I don’t render nodule segmentation before, two volumes rendered by “VTK GPU Ray cast” will lack of spatial location. But, with the help of nodule segmentation rendered and set the UseDepthPeeling to True before (althrough near to transparent), lost relative spatial location will be found.</strong></p>
<p>So actually, I don’t use VTK Multi-Volume rendering to render two volumes, I used VTK GPU Ray casting to render two volume separely, and displayed in the 3D view  at the same time, seems to solve VTK Multi-Volume rendering problem, that is: lost of detail and blurred result.</p>
<p>Next, I will explain why I can’t use segmentation rendering to replace two volumes rendering.<br>
(1) Automatic segment, semi-automatic segment or deep-learning segment  the nodule or vessel volume will cause lost information more or less, but doctor want to see original volume.<br>
(2) The density of single nodule is not average, we will use different opacity and color transfer function to render the single nodule volume.<br>
(3) We will cut the volume to see the inside of nodule volume. If I use the segmentation rendering, inside is empty, and I can’t see the inside of nodule.</p>

---

## Post #8 by @cpinter (2022-07-14 09:03 UTC)

<blockquote>
<p><strong>lost relative spatial location will be found</strong></p>
</blockquote>
<p>It will not, it will be the result of you seeing the segmentation properly instead of the volume rendering. And maybe it creates an optical illusion for you, but in general you should not use more than one volumes in non-multi-volume mode, because as you also noticed, you lose the depth information between the displayed volumes.</p>
<p>I agree very much that we should use multi-volume rendering (actually I’d also prefer in some cases to show segmentation labelmap as volume rendering), but that mapper is broken, unmaintained, and behind in features compared to the single volume mapper, and it requires a huge amount of work, moreover, a type of work that very few people are capable of doing well.</p>
<p>There was talk recently of restructuring the way the shader code is generated, which, currently is an extremely complex string operation in C++ with too many control branches, and this is why it is becoming unmaintainable. I haven’t heard about concrete roadmaps though, or scope of work.</p>

---
