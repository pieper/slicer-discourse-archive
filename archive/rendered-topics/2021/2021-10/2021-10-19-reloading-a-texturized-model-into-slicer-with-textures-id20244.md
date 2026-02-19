---
topic_id: 20244
title: "Reloading A Texturized Model Into Slicer With Textures"
date: 2021-10-19
url: https://discourse.slicer.org/t/20244
---

# Reloading a texturized model into Slicer with textures

**Topic ID**: 20244
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/reloading-a-texturized-model-into-slicer-with-textures/20244

---

## Post #1 by @muratmaga (2021-10-19 16:31 UTC)

<p>I use the TextureModel module from IGT to texturize the surface scans. I tried saving them as OBJ hoping that the textures were remembered next time, but it didn’t. What is the proper way of saving these models with texture, so that I don’t have to use TextureModel each time?</p>

---

## Post #2 by @pieper (2021-10-19 16:58 UTC)

<p>I don’t think there’s a good way to do that currently.  Texture was added to models for the slice display in the 3D view, but wasn’t exposed in the UI.  Full texture support is a complex topic, but probably some basic reloading capability could be added to the reader/writer code.</p>

---

## Post #3 by @lassoan (2021-10-19 18:42 UTC)

<p>PLY, VTK, and VTP formats all preserve colored texture of meshes (in point scalars).</p>
<p>You can copy the color information from textured OBJ to point scalars by using Texture Model module by setting “Save color information as point data” → “single vector”.</p>

---

## Post #4 by @muratmaga (2021-10-19 18:51 UTC)

<p>I did that, and then I saved the textured model as PLY. When I reload that into Slicer, it still didn’t display the textures. Am I msising a step?</p>

---

## Post #5 by @lassoan (2021-10-19 18:53 UTC)

<p>If you use the stable release then you need manually select the color scalar in Models module. This happens all automatically in Slicer Preview Releases.</p>

---

## Post #6 by @muratmaga (2021-10-19 19:02 UTC)

<p>Same for me with the preview. Under the scalar, there is something called Tcoords. But colormaps are weird. Nothing close to the original texture:</p>
<p>Textured:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c42487c9b39d4a042883e9db0e7691e2fd70d727.jpeg" data-download-href="/uploads/short-url/rZ9QIslYzF46aEM9eLyumoKl21F.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c42487c9b39d4a042883e9db0e7691e2fd70d727_2_345x146.jpeg" alt="image" data-base62-sha1="rZ9QIslYzF46aEM9eLyumoKl21F" width="345" height="146" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c42487c9b39d4a042883e9db0e7691e2fd70d727_2_345x146.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c42487c9b39d4a042883e9db0e7691e2fd70d727_2_517x219.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c42487c9b39d4a042883e9db0e7691e2fd70d727_2_690x292.jpeg 2x" data-dominant-color="D0CCD4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1359×577 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Saved and Reloded:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59c3394b9d6b8bd83c7b9c4897bebba16ec3e8b3.png" data-download-href="/uploads/short-url/cO4L7gj6rww0WZeZuCQfqH2dOn1.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59c3394b9d6b8bd83c7b9c4897bebba16ec3e8b3_2_345x191.png" alt="image" data-base62-sha1="cO4L7gj6rww0WZeZuCQfqH2dOn1" width="345" height="191" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59c3394b9d6b8bd83c7b9c4897bebba16ec3e8b3_2_345x191.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59c3394b9d6b8bd83c7b9c4897bebba16ec3e8b3_2_517x286.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59c3394b9d6b8bd83c7b9c4897bebba16ec3e8b3_2_690x382.png 2x" data-dominant-color="DFDEDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1349×748 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2021-10-19 19:04 UTC)

<p>After “Texture model” module saved the color information into the model, do the color scalars show up in Models module?</p>

---

## Post #8 by @muratmaga (2021-10-19 19:07 UTC)

<p>Immediately after texturizing, there is an additional scalar called Color:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7eeb8bb7f9a0c633066bc79215bf20ab93347ddc.jpeg" data-download-href="/uploads/short-url/i6MOzPPyR9BbkDvpSkhOz4cAMC8.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7eeb8bb7f9a0c633066bc79215bf20ab93347ddc_2_652x500.jpeg" alt="image" data-base62-sha1="i6MOzPPyR9BbkDvpSkhOz4cAMC8" width="652" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7eeb8bb7f9a0c633066bc79215bf20ab93347ddc_2_652x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7eeb8bb7f9a0c633066bc79215bf20ab93347ddc_2_978x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7eeb8bb7f9a0c633066bc79215bf20ab93347ddc_2_1304x1000.jpeg 2x" data-dominant-color="C9C3C3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1567×1200 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But by default it is not enabled, and when I enable it, colors look weird again:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a781d6d5b594d3be5a1a8b077a9f44a3abfdd02e.jpeg" data-download-href="/uploads/short-url/nTPUQ2HpMjjr4f1yJkKBMMaBmEK.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a781d6d5b594d3be5a1a8b077a9f44a3abfdd02e_2_690x450.jpeg" alt="image" data-base62-sha1="nTPUQ2HpMjjr4f1yJkKBMMaBmEK" width="690" height="450" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a781d6d5b594d3be5a1a8b077a9f44a3abfdd02e_2_690x450.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a781d6d5b594d3be5a1a8b077a9f44a3abfdd02e_2_1035x675.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a781d6d5b594d3be5a1a8b077a9f44a3abfdd02e_2_1380x900.jpeg 2x" data-dominant-color="B9BEBD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1528×997 95.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @lassoan (2021-10-19 19:19 UTC)

<p>It looks perfect, you just need to choose “direct color mapping” as scalar range mode if you don’t want to map the colors through a color table.</p>
<p>Slicer Stable Release cannot save point scalars into PLY, you either need to use VTK/VTP format or switch to the latest Slicer Preview Release.</p>

---

## Post #10 by @muratmaga (2021-10-19 19:22 UTC)

<p>It is still quite not the same color as the texturized model, but at least acceptable.<br>
By the way I am doing all of this in preview. So not saving the PLY or not showing the Color scalar is all happening with the preview from 10/14 (on windows).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02e55e42d8cb4853b177fd901c729102f0f549ea.jpeg" data-download-href="/uploads/short-url/pCnbSKvBBVFgDh9zL2cIXC8WtY.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02e55e42d8cb4853b177fd901c729102f0f549ea_2_690x375.jpeg" alt="image" data-base62-sha1="pCnbSKvBBVFgDh9zL2cIXC8WtY" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02e55e42d8cb4853b177fd901c729102f0f549ea_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02e55e42d8cb4853b177fd901c729102f0f549ea_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02e55e42d8cb4853b177fd901c729102f0f549ea_2_1380x750.jpeg 2x" data-dominant-color="B9B4BE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1897×1031 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @muratmaga (2021-10-19 19:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="20244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer Stable Release cannot save point scalars into PLY, you either need to use VTK/VTP format or switch to the latest Slicer Preview Release.</p>
</blockquote>
</aside>
<p>I can confirm that saving to PLY does not work as intended in the preview. VTK works fine, I can render the texture from the loaded model. Alhtough I still have to manually activate the scalar (i.e., it is not automatic).</p>

---

## Post #12 by @lassoan (2021-10-19 20:22 UTC)

<p>The model appearance should look very similar, but you may adjust material properties (Models module / Display / 3D Display / Advanced) to get the same brightness.</p>
<p>I’ve checked the Texture Model module and it saves the colors as a vtkDoubleArray (with values between 0-1), which is the VTK convention. However, colors are most commonly stored in vtkUnsignedCharArray, and that’s what Slicer recognizes automatically as colored mesh when a model is loaded.</p>
<p>I’ve added an option to Texture Model module to save as vtkUnsignedCharArray: “Save color information point data” → “RGB vector”. Such models will be loaded automatically in full color.</p>

---

## Post #13 by @ezgimercan (2021-10-19 21:20 UTC)

<p>A couple things about my experience with textures. Pardon my very technical language.</p>
<p>When texture is “applied” to the model, it does not color vertices/polygons with the colors - it maps the 2D picture to the model based on tex coords, so you get a very high quality looking mesh. This is what most mesh programs do and my lab likes to use in annotations.</p>
<p>When you transfer the texture as scalars to the mesh, then you lose the high resolution looking texture, now there is no 2D pic to “stretch” over the model, you see vertices/edges/polygons painted with the colors calculated from the original texture imaged and interpolated. I tried to go this route but my people complained about this saying that it is not the same quality as the camera software (3dMD or Canfield).</p>
<p>Another tricky thing - which happened to your mesh- is the stitching effect. This is the result of cleaning the mesh. Often, there are floating vertices edges etc that contributes to the mapping of the texture to the mesh. When you clean, you remove those vertices/edges and get that white region. I couldn’t find a good solution to this, so we keep using uncleaned original meshes with original textures. That gives the best visualization.</p>

---

## Post #14 by @lassoan (2021-10-19 22:14 UTC)

<aside class="quote no-group" data-username="ezgimercan" data-post="13" data-topic="20244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ezgimercan/48/4584_2.png" class="avatar"> ezgimercan:</div>
<blockquote>
<p>When you transfer the texture as scalars to the mesh, then you lose the high resolution looking texture, now there is no 2D pic to “stretch” over the model, you see vertices/edges/polygons painted with the colors calculated from the original texture imaged and interpolated. I tried to go this route but my people complained about this saying that it is not the same quality as the camera software (3dMD or Canfield).</p>
</blockquote>
</aside>
<p>Yes, very often the mesh resolution is higher than the resolution of the mesh, so you lose details when you just sample at mesh points, which may become visible when you zoom in:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/910e05388ac5717177cdf2eb5026db1a2c6ec28e.jpeg" data-download-href="/uploads/short-url/kHdgQGzVhuUpV5TDwPBzrdTKRgW.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/910e05388ac5717177cdf2eb5026db1a2c6ec28e_2_690x300.jpeg" alt="image" data-base62-sha1="kHdgQGzVhuUpV5TDwPBzrdTKRgW" width="690" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/910e05388ac5717177cdf2eb5026db1a2c6ec28e_2_690x300.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/910e05388ac5717177cdf2eb5026db1a2c6ec28e_2_1035x450.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/910e05388ac5717177cdf2eb5026db1a2c6ec28e_2_1380x600.jpeg 2x" data-dominant-color="807994"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1393×607 61.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73024905031f97597484192acf0bc282e7505969.jpeg" data-download-href="/uploads/short-url/gppNV9mIklXfmo2bXuQJZJiLiKR.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/73024905031f97597484192acf0bc282e7505969_2_690x302.jpeg" alt="image" data-base62-sha1="gppNV9mIklXfmo2bXuQJZJiLiKR" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/73024905031f97597484192acf0bc282e7505969_2_690x302.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/73024905031f97597484192acf0bc282e7505969_2_1035x453.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/73024905031f97597484192acf0bc282e7505969_2_1380x604.jpeg 2x" data-dominant-color="775E40"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1393×611 57.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/563a968ffc33961e5dc19e2c8570980ea59a8f2e.jpeg" data-download-href="/uploads/short-url/ciOAogvYx1yYTKNVaMfIxH9HXBQ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/563a968ffc33961e5dc19e2c8570980ea59a8f2e_2_690x301.jpeg" alt="image" data-base62-sha1="ciOAogvYx1yYTKNVaMfIxH9HXBQ" width="690" height="301" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/563a968ffc33961e5dc19e2c8570980ea59a8f2e_2_690x301.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/563a968ffc33961e5dc19e2c8570980ea59a8f2e_2_1035x451.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/563a968ffc33961e5dc19e2c8570980ea59a8f2e_2_1380x602.jpeg 2x" data-dominant-color="5A4833"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1393×608 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Storing the information that which image should be applied to which node would be quite straightforward and we already have a ticket to track this request:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/2671">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/2671" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/2671" target="_blank" rel="noopener">Persistent texture mapping for models</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="23:49:30" data-timezone="UTC">11:49PM - 12 Mar 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Enhancement
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Priority: Medium
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=2671). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote no-group" data-username="ezgimercan" data-post="13" data-topic="20244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ezgimercan/48/4584_2.png" class="avatar"> ezgimercan:</div>
<blockquote>
<p>Another tricky thing - which happened to your mesh- is the stitching effect. This is the result of cleaning the mesh. Often, there are floating vertices edges etc that contributes to the mapping of the texture to the mesh. When you clean, you remove those vertices/edges and get that white region. I couldn’t find a good solution to this, so we keep using uncleaned original meshes with original textures. That gives the best visualization.</p>
</blockquote>
</aside>
<p>Merging/blending textures is indeed tricky, especially if you have overlapping texture images acquired with slightly varying light conditions. Your 3D scanning software should have options for merging multiple textures either during scanning or as a post-processing step (the software that came with our Artec scanners had them) and then you don’t need to deal with the issue during rendering. I’m sure that other software, such as Blender has many tools for blending textures, too.</p>
<p>Questions about seams in multi-texture OBJs have come up a couple of times on VTK discourse and there are solutions (adjusting rendering settings, maybe some small processing with Python scripting). With a very quick search these two hits have came up (but there are at least a few more):</p>
<ul>
<li><a href="https://discourse.vtk.org/t/multi-texture-obj/3775" class="inline-onebox">Multi-texture OBJ - Support - VTK</a></li>
<li><a href="https://stackoverflow.com/questions/39137374/vtk-inserts-incorrect-color-between-nodes-when-mapping-texture-to-mesh/39237979#39237979" class="inline-onebox">python - Vtk inserts incorrect color between nodes when mapping texture to mesh - Stack Overflow</a></li>
</ul>

---

## Post #15 by @ezgimercan (2021-10-19 22:46 UTC)

<p>I’ve seen these posts and tried everything recommended. Setting interpolation, edge trimming etc. The only thing that worked was to use original mesh and original textures without any preprocesing.<br>
I’ve made some changes to the TextureModel module for it to work with multiple images - I believe I had a pull request open for that.</p>

---

## Post #16 by @muratmaga (2021-10-19 23:24 UTC)

<aside class="quote no-group" data-username="ezgimercan" data-post="13" data-topic="20244">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ezgimercan/48/4584_2.png" class="avatar"> ezgimercan:</div>
<blockquote>
<p>Another tricky thing - which happened to your mesh- is the stitching effect. This is the result of cleaning the mesh. Often, there are floating vertices edges etc that contributes to the mapping of the texture to the mesh.</p>
</blockquote>
</aside>
<p>I am not sure if this mesh was cleaned or not. It was a very old dataset (almost 10 years ago) from the 4 pod 3DMD system. It is possible that 3DMD does not export data sufficiently well. But it it will good to have the stretching available in slicer, but on closer inspection (long time ago), I recall there being some discrepancies between how the pictures is stretched versus underling mesh (as I recall edges of the eyelid - <strong>palpebral fissure</strong>- were not exactly a 1-1 match between mesh and photo).</p>

---
