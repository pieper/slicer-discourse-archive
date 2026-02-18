# New feature: Basic support for physically based rendering (PBR)

**Topic ID**: 21725
**Date**: 2022-02-01
**URL**: https://discourse.slicer.org/t/new-feature-basic-support-for-physically-based-rendering-pbr/21725

---

## Post #1 by @lassoan (2022-02-01 05:29 UTC)

<p>VTK (Slicer’s rendering library) added support for physically based rendering (PBR) in recent versions. See some examples in these blog posts: <a href="https://www.kitware.com/vtk-pbr/">PBR basics</a>, <a href="https://www.kitware.com/pbrj1/">image-based lighting</a>, <a href="https://www.kitware.com/pbr-journey-part-3-clear-coat-model-with-vtk/">coats</a>. We exposed some of these features in the latest Slicer Preview Release.</p>
<ol>
<li>PBR interpolation mode in Models module</li>
</ol>
<p>A new <em>PBR</em> mode is added to Models module / Display / 3D Display / Advanced / Interpolation listbox. In PBR mode, the material properties are described with a diffuse reflection factor (overall brightness), metallic, and roughness factors.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3bbe21f7cd59394cf9bd00e6bb513ba6fba30e0.jpeg" data-download-href="/uploads/short-url/ud5hD5LHIJtO6T7o2FI4haMDQ9q.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3bbe21f7cd59394cf9bd00e6bb513ba6fba30e0_2_690x419.jpeg" alt="image" data-base62-sha1="ud5hD5LHIJtO6T7o2FI4haMDQ9q" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3bbe21f7cd59394cf9bd00e6bb513ba6fba30e0_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3bbe21f7cd59394cf9bd00e6bb513ba6fba30e0_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d3bbe21f7cd59394cf9bd00e6bb513ba6fba30e0_2_1380x838.jpeg 2x" data-dominant-color="CFCFD9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1167 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>Image-based lighting</li>
</ol>
<p>Experimental image-based lighting setup feature was added to Lights module (in Sandbox extension). This can be used to specify an image that provides lighting to PBR models and this image can be seen reflected from smooth metallic surfaces.</p>
<p></p><div class="video-placeholder-container" data-video-src="/404" data-orig-src="upload://jsdfW5QSofj708nNvA59uTOQWut.mp4">
  </div><p></p>
<p>Currently a single image of a hospital room can be chosen (by clicking the corresponding button), but users can experiment with adding different images by editing the module’s Python script.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9ca0a3b4e9ca6221f07f6ffbb0ccff2c37113621.png" data-download-href="/uploads/short-url/mlAExxBp2ONpGhIbgf09wlUOErD.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ca0a3b4e9ca6221f07f6ffbb0ccff2c37113621_2_670x499.png" alt="image" data-base62-sha1="mlAExxBp2ONpGhIbgf09wlUOErD" width="670" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ca0a3b4e9ca6221f07f6ffbb0ccff2c37113621_2_670x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9ca0a3b4e9ca6221f07f6ffbb0ccff2c37113621.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9ca0a3b4e9ca6221f07f6ffbb0ccff2c37113621.png 2x" data-dominant-color="EBEAED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">886×661 58.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="3">
<li>Ambient shadows (screen-space ambient occlusion - SSAO)</li>
</ol>
<p>This feature was added to the Lights module some time ago, but it is worth mentioning again here, because PBR models often don’t have darkening at the edges and this feature can help making edges more visible.</p>
<p>Example rendering of models with PBR interpolation, non-metallic objects with image-based lighting and ambient shadows:</p>
<p></p><div class="video-placeholder-container" data-video-src="/404" data-orig-src="upload://3fRfEawuiLHi2QEkvJmNKDPM9jy.mp4">
  </div><p></p>

---

## Post #2 by @hherhold (2022-02-01 13:08 UTC)

<p>This looks <em>fantastic</em>!</p>
<p>I tried installing this morning for Windows preview release (2022-02-01) but the Sandbox extension could not be found. I did try the PBR interpolation and it looks great, but I’d like to see the image based lighting with it.</p>
<p>The Mac build doesn’t have this yet - seems to be a couple of days old?</p>
<p>Thanks!</p>

---

## Post #3 by @lassoan (2022-02-01 18:05 UTC)

<p>Thanks for testing. A file was missing from SlicerSandbox that prevented the packaging. I’ve added the file now. If you don’t want to wait for tomorrow’s release, you can download the extension from <a href="https://github.com/PerkLab/SlicerSandbox">here</a> and add the <code>Lights</code> folder to the Modules → Additional module paths in your application settings.</p>
<p>I’m not sure what’s going on with the macOS build. <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> can you have a look?</p>

---

## Post #4 by @muratmaga (2022-02-02 05:10 UTC)

<p>It really looks cool. Couple usability comments:</p>
<ol>
<li>
<p>In the models module, after I change the interpolation to PBR, and then I click on one of the presets, the settings change the way it looks under phong/flat/goraud  shading (i.e., there are ambient/specular sliders etc). But when I try touch one of them, it reverts the way it looks in PBR (three sliders only).</p>
</li>
<li>
<p>I couldn’t try with the Lights module due to lack of Sandbox extension, but have a feeling that for PBR to work better, we might have to have the Lights module in the core perhaps (i.e., graduate out of Sandbox?)</p>
</li>
<li>
<p>Would it be possible to enable this in Segment Editor as well (maybe it is possible, I didn’t look to deep really).</p>
</li>
<li>
<p>Does it work with volume rendering?</p>
</li>
</ol>
<p>But it does look cool, thanks for working on it…</p>

---

## Post #5 by @lassoan (2022-02-03 05:54 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="21725">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>In the models module, after I change the interpolation to PBR, and then I click on one of the presets, the settings change the way it looks under phong/flat/goraud shading (i.e., there are ambient/specular sliders etc). But when I try touch one of them, it reverts the way it looks in PBR (three sliders only).</p>
</blockquote>
</aside>
<p>If you click on it then the interpolation mode will be set to the mode that is specified in the preset. Currently, all 3 presets uses Gouraud interpolation, but unfortunately, there is a display bug: after clicking the preset, the interpolation checkbox still shows “PBR”.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="21725">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I couldn’t try with the Lights module due to lack of Sandbox extension, but have a feeling that for PBR to work better, we might have to have the Lights module in the core perhaps (i.e., graduate out of Sandbox?)</p>
</blockquote>
</aside>
<p>When I added this feature I missed adding a file, so for one day the Sandbox extension was not built.<br>
It would be awesome if someone would help with adding these features to the Slicer core. The Lights module cannot be added to the Slicer core as is, because settings are not preserved in the scene. We would need to decide where to store these settings (store lights in the view node, in a “lightkit” node, or add a separate node for each light), and implement standard GUI (make these view parameters available near existing view parameters), linking of properties (when view link is enabled and you change a view parameter in one view, apply it to all other views), etc. I also feel that without the ability to assign texture to each model, PBR rendering is still too limited and experimental.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="21725">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Would it be possible to enable this in Segment Editor as well (maybe it is possible, I didn’t look to deep really).</p>
</blockquote>
</aside>
<p>PBR is somewhat supported for segmentation nodes: metallic and roughness value can only be specified for the entire segmentation (not for each segment) and we haven’t added GUI for this yet. It would not be hard to resolve these limitations, but for now you need to export to models to edit these properties.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="21725">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Does it work with volume rendering?</p>
</blockquote>
</aside>
<p>Image-based lighting can be used for volume rendering, too, but I don’t think it is implemented in VTK (at least not in the default OpenGL2 rendering backend). <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> showed some nice examples <a href="https://discourse.slicer.org/t/how-to-perform-3d-cinematic-rendering/7313/4">here</a>, which proves that it is possible (I think MatCaps is the same or very similar to what VTK calls image-based lighting).</p>

---

## Post #6 by @hherhold (2022-02-03 11:30 UTC)

<p>This works fine on latest MacOS preview build.</p>
<p>PBR and image-based lighting (especially with ambient shadows) looks to be particularly useful for viewing intricate structures with lots of overhangs and such. I’ll be testing this out quite a bit in the next little while.</p>
<p>Speaking of ambient shadows, the size scale parameter seems somewhat arbitrary - my CT scans are typically of things ~ 1cm in size, and I basically just tweak this parameter until it looks good. I confess I have not looked this up in the VTK docs at all. Are there units associated with it or is it just a non-dimensional adjustment?</p>
<p>Thanks for working on this! Very cool!</p>

---

## Post #7 by @lassoan (2022-02-03 15:02 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="6" data-topic="21725">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>just tweak this parameter until it looks good. I confess I have not looked this up in the VTK docs at all. Are there units associated with it or is it just a non-dimensional adjustment?</p>
</blockquote>
</aside>
<p>This is how it is intended to be used - you look at the image and adjust the slider.</p>
<p>The slider sets a “scene size” using an exponential exponential scale. This size is then used to set a distance threshold value (that is used to decide if shadow should be casted between two objects) and the radius value (that specifies the spread of the shadow).</p>
<p>The distance threshold value (called <code>bias</code> in the SSAO algorithm) is computed as <code>pow(10, self.ssaoSizeScaleLog - 1)</code>. The power of 10 is used to allow covering a large range of size with a single slider. The -1 offset is added so that 0.0 slider value corresponds to 100 length unit size (millimeter by default), which works well as a default.</p>
<p>The spread value (called <code>radius</code> in the SSAO algorithm) is set to 100x the distance threshold value.</p>
<p>It might make sense to display the scene size or distance threshold value to the user to make this slider a bit less mysterious.</p>

---

## Post #8 by @hherhold (2022-02-03 15:06 UTC)

<p>Gotcha, thanks. I might try tweaking this bias calculation a bit, as the default unit size for 0.0 might be a little large for insects. I get a lot of mach banding in shadows and some flicker artifacts, not sure if this is due to an overly large bias setting. That said, I haven’t tried it at all on larger things, so maybe this is just how it works until you get a good value figured out.</p>

---

## Post #9 by @Kawtar_Lakrad (2022-02-05 05:34 UTC)

<p>where can I find the Lights folder?</p>

---

## Post #10 by @manjula (2022-02-05 05:57 UTC)

<p>Lights module is with sandbox extension.</p>
<p>You will find it in the Extension manager → under “Examples” category</p>

---

## Post #11 by @hherhold (2022-02-17 14:38 UTC)

<p>I’ve had a chance to work with PBR, Lights, and Ambient shadows quite a bit in the last week or so and I have a few thoughts on it.</p>
<p>The results I can get from tweaking the lights and various settings is nothing short of fantastic. I can get screen shots that are very similar to the level of shading and lighting I can achieve using Blender.</p>
<p>I would love to be able to use this to create publication quality plates. <em>However</em>, for my use case, it’s not useable for this, primarily because (as far as I know) I’m not able to save camera position and restore a view <em>exactly</em> as it was for a previous screen grab. My workflow is to export screen captures (or renders from Blender) and annotate them with lines and annotations using Illustrator. I’m currently in the midst of a large comparative study on insect morphology, and this will often require updating segmentations and figures, meaning I will have to update and re-export a view with the same camera position and lighting settings as previously, so I can re-import it into Illustrator and have my lines and labels where they were before. It would be great if there was a “scene save” so that I could reload exactly the same scene setup and position.</p>
<p>I know we’ve had discussions previously regarding things like key framing animation of the camera, saving various parameters for lights and other settings, and I fully realize that many of these things are substantial tasks. I just wanted to relay some initial feedback after a couple of weeks using PBR and lights. If others have suggestions on things like saving camera positions, etc I would be very happy to discuss.</p>
<p>In short, I think the output is stunning, in fact I’ve showed a few of my segmentations to others and they’ve universally given a “holy crap” reaction. Thanks very much for your work on it!</p>

---

## Post #12 by @rkikinis (2022-02-17 15:07 UTC)

<p>How about using sceneviews for this? The module might be in need of maintenance as it does not capture volume rendering state and I am not sure about the lighting, but it does capture camera position</p>

---

## Post #13 by @hherhold (2022-02-17 15:09 UTC)

<p>Ah, that’s definitely worth a try - I haven’t tried Scene views in an embarrassingly long time.</p>
<p>Thanks for the tip!</p>

---

## Post #14 by @hherhold (2022-02-17 15:37 UTC)

<p>Ran into an odd issue with Scene Views - I will post in a new thread. (Possible bug?)</p>

---

## Post #15 by @pieper (2022-02-17 17:53 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="11" data-topic="21725">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>I’m not able to save camera position and restore a view <em>exactly</em> as it was for a previous screen grab.</p>
</blockquote>
</aside>
<p>Can’t you just save the mrml scene and reload it?</p>
<p>By the way, <a class="mention" href="/u/hherhold">@hherhold</a> how about posting some example “holy crap” images?</p>

---

## Post #16 by @hherhold (2022-02-17 19:07 UTC)

<p>Yes, I could do that, but as <a class="mention" href="/u/muratmaga">@muratmaga</a> mentioned in another post, I’d wind up with a lot of separate mrml files, one for each figure. It would get cumbersome pretty quickly.</p>
<p>Images - in the works… The “holy crap” was more for the lighting and shading now available than for my images! We have a few VG Studio users here that continue to be very surprised at how capable Slicer is.</p>

---

## Post #17 by @lassoan (2022-02-18 00:37 UTC)

<p>Scene Views feature have had lots of instability issues over the years. Now we have a good <a href="https://github.com/Slicer/Slicer/issues/4841">plan how to fix all that</a>, but we’ll only do this rework after Slicer5 is released.</p>
<p>Until then, I would recommend to use Sequences to store state of selected nodes - such as the camera, maybe volume rendering properties. See a short tutorial here:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="KZfOtqqwCq0" data-video-title="Saving and restoring of node states" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=KZfOtqqwCq0" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/KZfOtqqwCq0/maxresdefault.jpg" title="Saving and restoring of node states" width="" height="">
  </a>
</div>


---
