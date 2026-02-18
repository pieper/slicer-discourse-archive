# Scale model in gltf

**Topic ID**: 31639
**Date**: 2023-09-11
**URL**: https://discourse.slicer.org/t/scale-model-in-gltf/31639

---

## Post #1 by @Caterina (2023-09-11 09:24 UTC)

<p>Good morning,<br>
I performed segmentation and I would like to scale the results of segmentation in gltf format.<br>
Actually I can scale the model in stl using Surface Toolbox or save the unscaled model in gltf.<br>
I need to scale the model and export it in gltf.<br>
Can I hace suggestion about this topic?<br>
Thanks</p>

---

## Post #2 by @muratmaga (2023-09-11 14:58 UTC)

<p>Then why can’t you export the scaled model from Surface toolbox as GLTF?</p>

---

## Post #3 by @Caterina (2023-09-12 08:21 UTC)

<p>Surface Toolbox allows to scale segmentation objects (stl or obj).<br>
OpenAnatomy allows to export gltf model but it doesn’t see segmentation objects previously scaled with Surface Toolbox.</p>

---

## Post #4 by @muratmaga (2023-09-12 16:20 UTC)

<p>That doesn’t sound right.</p>
<p>You should be able to export models from OpenAnatomy, not just segmentation. They need to be under a subject hierarachy, thought i believe. So try making a folder within your data module, move your scaled model under that folder and then try the OA one more time.</p>
<p>This worked for me with 5.4.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/6814f63f6835ab10a7acdf485fce4aee2613517e.png" data-download-href="/uploads/short-url/eQKzbRe8beXFTUd6KkkIvPqjjZ4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/6814f63f6835ab10a7acdf485fce4aee2613517e_2_690x375.png" alt="image" data-base62-sha1="eQKzbRe8beXFTUd6KkkIvPqjjZ4" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/6814f63f6835ab10a7acdf485fce4aee2613517e_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/6814f63f6835ab10a7acdf485fce4aee2613517e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/6814f63f6835ab10a7acdf485fce4aee2613517e.png 2x" data-dominant-color="E6EEF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">987×537 19.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Caterina (2023-09-20 12:47 UTC)

<p>Thanks for suggestions.<br>
Since my segmentation is made up of many segmentations (result from TotalSegmentation), when I export the models, many models are also created. Is there a way to merge them together before scaling them and then export them to gltf?Thanks</p>

---

## Post #6 by @lassoan (2023-09-20 13:51 UTC)

<p>I’ve checked the glTF standard and actually the length unit is specified to be in meters. So, I’ve <a href="https://github.com/PerkLab/SlicerOpenAnatomy/commit/ce61de8995aebdbf0ff0e7293f6d41aef1019568">updated the OpenAnatomy export module to always export in meters</a>. You can get the updated extensions from the Extensions Manager tomorrow or later.</p>

---

## Post #7 by @Caterina (2023-09-21 08:03 UTC)

<p>Thank you very much for support and for information. Hasn’t the unit of measurement for the OpenAnatomy export module been meters so far? Concerning the way to merge the segmentations together and then export them to gltf, can you please suggest me a solution?<br>
Thanks</p>

---

## Post #8 by @lassoan (2023-09-21 15:13 UTC)

<aside class="quote no-group" data-username="Caterina" data-post="7" data-topic="31639">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/439d5e/48.png" class="avatar"> Caterina:</div>
<blockquote>
<p>Hasn’t the unit of measurement for the OpenAnatomy export module been meters so far?</p>
</blockquote>
</aside>
<p>Length unit in Slicer (and in DICOM and in all medical image computing software) is millimeters. OpenAnatomy export module has exported all models in millimeters, too.</p>
<p>In the latest module, I’ve included a millimeter to meter scaling transformation in the root of the glTF file, so we comply to glTF specifications.</p>
<p>You can verify distances in a glTF file using an independent viewer, such as <a href="http://3dviewer.net">3dviewer.net</a> - just drag-and-drop the exported glTF file to the viewer and use the measurement tool.</p>

---

## Post #9 by @Caterina (2023-09-27 15:09 UTC)

<p>Dear Prof Lasso,<br>
thanks a lot for the updates and for modifying the OpenAnatomy Export module.<br>
However, I can’t see a millimeter to meter scaling transformation in the root of the glTF file.<br>
Can you please share with me a screenshot of the modified module?<br>
Thanks</p>

---

## Post #10 by @lassoan (2023-09-27 15:17 UTC)

<p>I’ve already provided the link to the change above, but here it is again:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/PerkLab/SlicerOpenAnatomy/commit/ce61de8995aebdbf0ff0e7293f6d41aef1019568">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerOpenAnatomy/commit/ce61de8995aebdbf0ff0e7293f6d41aef1019568" target="_blank" rel="noopener">github.com/PerkLab/SlicerOpenAnatomy</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/PerkLab/SlicerOpenAnatomy/commit/ce61de8995aebdbf0ff0e7293f6d41aef1019568" target="_blank" rel="noopener">Save glTF files in meters</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2023-09-20" data-time="13:48:51" data-timezone="UTC">01:48PM - 20 Sep 23 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 1 files with 29 additions and 6 deletions">
        <a href="https://github.com/PerkLab/SlicerOpenAnatomy/commit/ce61de8995aebdbf0ff0e7293f6d41aef1019568" target="_blank" rel="noopener">
          <span class="added">+29</span>
          <span class="removed">-6</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">According to glTF specifications (3.4. Coordinate System and Units, https://regi<span class="show-more-container"><a href="https://github.com/PerkLab/SlicerOpenAnatomy/commit/ce61de8995aebdbf0ff0e7293f6d41aef1019568" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">stry.khronos.org/glTF/specs/2.0/glTF-2.0.html#coordinate-system-and-units):

  glTF uses a right-handed coordinate system. glTF defines +Y as up, +Z as forward, and -X as right; the front of a glTF asset faces +Z.
  The units for all linear distances are meters.
  All angles are in radians.
  Positive rotation is counterclockwise.

Therefore, we now scale the whole model to meters (apply a factor of 0.001 if scene length unit is mm) when exporting to glTF.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @lassoan (2023-09-27 15:18 UTC)

<p>Note that you need to use the latest Slicer Stable Release or latest Slicer Preview Release to get extension updates.</p>

---

## Post #12 by @Caterina (2023-09-27 15:27 UTC)

<p>Thanks a lot.<br>
I’m using 5.4.0 version. I also checked the updates of openAnatomy module from extentions manager.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3df9ac2d6934a45de9d1287aa219d81b681c33b.png" data-download-href="/uploads/short-url/nnGTGE4Eww3WVl8wZHJqIrBnf7l.png?dl=1" title="Screenshot 2023-09-27 alle 17.26.45" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3df9ac2d6934a45de9d1287aa219d81b681c33b_2_487x500.png" alt="Screenshot 2023-09-27 alle 17.26.45" data-base62-sha1="nnGTGE4Eww3WVl8wZHJqIrBnf7l" width="487" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3df9ac2d6934a45de9d1287aa219d81b681c33b_2_487x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3df9ac2d6934a45de9d1287aa219d81b681c33b_2_730x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3df9ac2d6934a45de9d1287aa219d81b681c33b_2_974x1000.png 2x" data-dominant-color="DADBDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-09-27 alle 17.26.45</span><span class="informations">1130×1158 96 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @lassoan (2023-09-27 17:56 UTC)

<p>It should be all good then. To confirm, you can click the “Edit” button to load the .py file and see if the changes in the commit that I linked above are there.</p>

---

## Post #14 by @Caterina (2023-09-27 18:26 UTC)

<p>Thanks again. Here the screen of the .py file in which the changes you made<br>
are present.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd7e477000fcb1a0d22f0aff50284e20ffb6dcef.jpeg" data-download-href="/uploads/short-url/r2kNcmfPkwOLwCtv5bfLbkrWfxl.jpeg?dl=1" title="Screenshot 2023-09-27 alle 20.23.16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd7e477000fcb1a0d22f0aff50284e20ffb6dcef_2_552x500.jpeg" alt="Screenshot 2023-09-27 alle 20.23.16" data-base62-sha1="r2kNcmfPkwOLwCtv5bfLbkrWfxl" width="552" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd7e477000fcb1a0d22f0aff50284e20ffb6dcef_2_552x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd7e477000fcb1a0d22f0aff50284e20ffb6dcef_2_828x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd7e477000fcb1a0d22f0aff50284e20ffb6dcef_2_1104x1000.jpeg 2x" data-dominant-color="F5F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-09-27 alle 20.23.16</span><span class="informations">1280×1158 261 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>.<br>
But there is no selection on the user interface related to dimension conversion.</p>

---

## Post #15 by @lassoan (2023-09-28 01:53 UTC)

<p>According to glTF standard, the distance unit in the world coordinate system is meter. Therefore we do not allow the user to select units but always use meter.</p>

---

## Post #16 by @Caterina (2023-09-28 08:34 UTC)

<p>Dear Prof Lasso,<br>
thanks a lot for support and for your patience.<br>
I need to export segmentation results from TotalSegmentation (several volumes) as gltf file with the same dimensions that I see on 3d slicer (for example around 650 mm).<br>
Actually, after exporting using OpenAnatomy, the dimension will be 650 m.<br>
So I need to scale before exporting as gltf. Is there a way to scale all volumes of a segmentation at once?<br>
Thanks</p>

---

## Post #17 by @muratmaga (2023-09-28 15:42 UTC)

<aside class="quote no-group" data-username="Caterina" data-post="16" data-topic="31639">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/439d5e/48.png" class="avatar"> Caterina:</div>
<blockquote>
<p>around</p>
</blockquote>
</aside>
<p>There is something amiss here. You wouldn’t see 650mm being reported as 650m. You should see 650mm being reported as 0.65m in the software you are loading the exported glTF file, because the scaleToMeters function shown above divides the values by 1000, if the units are millimeters (which is default in slicer).</p>
<p>Regardless if you want to try this on your own for further troubleshooting, create a linear transform whose first three diagonals are 0.001, and then put your segmentation under it, and harden the transform (that’s what the code snipped above is doing).</p>
<p>Then you can perhaps figure out where the issue is coming from.</p>

---

## Post #18 by @lassoan (2023-09-28 19:01 UTC)

<p>Please check in the Extensions Manager if you have the latest version of the SlicerOpenAnatomy extension installed:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f54ec83cf12fd9559a7fe4da6ffa22de235b50fe.png" data-download-href="/uploads/short-url/z05LL2xjdYaCoTTAjvXvWdJpRnM.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f54ec83cf12fd9559a7fe4da6ffa22de235b50fe.png" alt="image" data-base62-sha1="z05LL2xjdYaCoTTAjvXvWdJpRnM" width="690" height="122" data-dominant-color="424343"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1096×195 11.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you have this version, then you can do a simple test to confirm it works well:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df81c4c2ad941cece73c8e2213e0bc115f994d33.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df81c4c2ad941cece73c8e2213e0bc115f994d33.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df81c4c2ad941cece73c8e2213e0bc115f994d33.mp4</a>
    </video>
  </div><p></p>
<p>As you can see, the segment length measurement result was the same in Slicer (114mm) and in the glTF viewer (0.111m).</p>
<p>Maybe you haven’t used the current version of SlicerOpenAnatomy extension or you used a glTF viewer that measured distance incorrectly.</p>

---
