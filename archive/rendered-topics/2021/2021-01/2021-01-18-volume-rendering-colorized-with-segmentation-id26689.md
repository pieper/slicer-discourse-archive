---
topic_id: 26689
title: "Volume Rendering Colorized With Segmentation"
date: 2021-01-18
url: https://discourse.slicer.org/t/26689
---

# Volume rendering colorized with segmentation

**Topic ID**: 26689
**Date**: 2021-01-18
**URL**: https://discourse.slicer.org/t/volume-rendering-colorized-with-segmentation/26689

---

## Post #1 by @pieper (2021-01-18 23:12 UTC)

<p>I’d like to have a follow up chat about segmentation rendering.  I found the vtk shader bug we discussed before so now shading can be made to work (no PR yet, but it’s a small set of changes).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7ac7974a69d026024c8d7f9dedcd5fdf209ab97.jpeg" data-download-href="/uploads/short-url/x3tORNYZvwWMcQFoPQuTEVqgHuD.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7ac7974a69d026024c8d7f9dedcd5fdf209ab97_2_690x494.jpeg" alt="image" data-base62-sha1="x3tORNYZvwWMcQFoPQuTEVqgHuD" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7ac7974a69d026024c8d7f9dedcd5fdf209ab97_2_690x494.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7ac7974a69d026024c8d7f9dedcd5fdf209ab97.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7ac7974a69d026024c8d7f9dedcd5fdf209ab97.jpeg 2x" data-dominant-color="13130F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">881×632 60.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-01-18 23:47 UTC)

<p>This rendering looks very nice!</p>
<p>It should not be hard to add this as a new volume rendering option. This is required for photorealistic volume rendering (a.k.a. “cinematic rendering”), too - there the RGB array is filled in quickly and approximately using AI-based segmentation, making vessels appear red, bone off-white, soft-tissues brown, etc.</p>
<p>It would be nice to use this in the segmentation displayable manager, too. For this we should have the option of generating opacity volume from the segmentation’s binary labelmap and compute smooth gradients. Smoothing the binary labelmap would be easy, but slow and it would double the memory usage. It would be better to improve the GPU raycaster’s gradient computation to use a small local neighborhood. Eventually, binary labelmap volume rendering as RGB should be a built-in feature of the GPU volume raycast mapper.</p>
<p>Do you use the GPU volume mapper’s labelmap masking features (<a href="https://vtk.org/doc/nightly/html/classvtkVolumeProperty.html#a9d2b68822d0969c3a527bd97eadb4391">specify a lookup table for input labelmap mask</a> and <a href="https://vtk.org/doc/nightly/html/classvtkGPUVolumeRayCastMapper.html#a296933b0880cd97f8bf16ba0a2aef1ec">mask blend factor controls how much coloring is applied from the mask</a>) or you generate an RGBA volume from scratch?</p>

---

## Post #3 by @pieper (2021-01-18 23:51 UTC)

<p>This one was done by generating the RGBA volume and then rendering withe the GPU ray cast (once the shading was fixed).</p>
<p>Yes, I think the segmentation rendering should all be done in the GPU code.</p>

---

## Post #4 by @lassoan (2021-01-19 00:03 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="26689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>This one was done by generating the RGBA volume and then rendering withe the GPU ray cast (once the shading was fixed).</p>
</blockquote>
</aside>
<p>It would be nice if you could try if setting the segmentation as labelmap mask for the GPU mapper provides the same results. The advantage would be that we would not need to generate an RGBA volume (faster updates, less memory usage).</p>

---

## Post #5 by @jcfr (2021-01-19 00:17 UTC)

<aside class="quote no-group" data-username="pieper" data-post="1" data-topic="26689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I’d like to have a follow up chat about segmentation rendering. I found the vtk shader bug we discussed before so now shading can be made to work (no PR yet, but it’s a small set of changes).</p>
</blockquote>
</aside>
<p>This is great <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>Cc: <a class="mention" href="/u/sankhesh_jhaveri">@Sankhesh_Jhaveri</a></p>

---

## Post #6 by @pieper (2021-01-19 00:26 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="26689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would be nice if you could try if setting the segmentation as labelmap mask for the GPU mapper provides the same results. The advantage would be that we would not need to generate an RGBA volume (faster updates, less memory usage).</p>
</blockquote>
</aside>
<p>Yes, exactly.</p>
<p>This image uses the CT as alpha, so you get nice detail with the coloring, but we should also do the option where the segmentation opacity controls the alpha channel.  We’ll need to do the local smoothing / surface fitting in the GPU using the segmentation and the color from the lookup table.  This should be effectively the same as building a surface model but faster and with some extra options.</p>
<p>I agree we should think about how we should handle volume rendering from a UI perspective.</p>
          <div class="onebox video-onebox">
            <video width="100%" height="100%" controls="">
              <source src="https://dl.dropboxusercontent.com/s/l04gdww0l3ftqs1/RGBA-mouse-segment-render.mp4?dl=0">
              <a href="https://dl.dropboxusercontent.com/s/l04gdww0l3ftqs1/RGBA-mouse-segment-render.mp4?dl=0" rel="noopener">https://dl.dropboxusercontent.com/s/l04gdww0l3ftqs1/RGBA-mouse-segment-render.mp4?dl=0</a>
            </video>
          </div>


---

## Post #7 by @muratmaga (2021-01-19 00:30 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="26689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>ut we should also do the option where the segmentation opacity controls the alpha channel.</p>
</blockquote>
</aside>
<p>I would say this is almost a must for this to be a meaningful replacement of existing segmentation rendering, and creating complex visualization from them.</p>

---

## Post #8 by @lassoan (2022-12-11 03:56 UTC)

<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="26689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>This one was done by generating the RGBA volume and then rendering withe the GPU ray cast (once the shading was fixed).</p>
</blockquote>
</aside>
<p>I’ve tried to colorize volume rendering using TotalSegmentator’s segments (see <a href="https://gist.github.com/lassoan/ecb3edaa42521261f5e552055065b3b5">implementation</a>), but the result looks quite bad:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb906c8585149cca19c264bcc8a5a9826b9644d3.jpeg" data-download-href="/uploads/short-url/t2OlU6MJpG8ypIPOPgoqZ10UWTV.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb906c8585149cca19c264bcc8a5a9826b9644d3_2_651x500.jpeg" alt="image" data-base62-sha1="t2OlU6MJpG8ypIPOPgoqZ10UWTV" width="651" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb906c8585149cca19c264bcc8a5a9826b9644d3_2_651x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb906c8585149cca19c264bcc8a5a9826b9644d3_2_976x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb906c8585149cca19c264bcc8a5a9826b9644d3_2_1302x1000.jpeg 2x" data-dominant-color="7F7086"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1306×1002 67.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The main issue is that I had to boost the opacity inside segments but then the boundary becomes very sharp/blocky. Applying smoothing removes the blockiness but also removes intricate details of the surface. Even if I don’t boost opacity (just show bones and contrasted vessels), the surface is still blocky because the RGB values have an abrupt change at the segment boundary.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> What was the VTK shader bug? Did the fix make it into VTK? In your mouse skull rendering above it seems that you managed to just change the RGB color but kept the original surface details (opacity and surface gradient) - did you have to apply any thresholding, masking, dilation?</p>

---

## Post #9 by @pieper (2022-12-11 17:02 UTC)

<p>The fix is in this post.  No, I don’t think it was ever merged.</p>
<aside class="onebox discoursetopic" data-onebox-src="https://discourse.vtk.org/t/color-volume-rendering-vtkdataarray-indexing/5695/5">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/color-volume-rendering-vtkdataarray-indexing/5695/5" target="_blank" rel="noopener" title="05:38PM - 04 May 2021">VTK – 4 May 21</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/494;"><img src="https://discourse.vtk.org/uploads/default/original/2X/c/c9b40fb52b6165efa0846382938b9b504d6f7fa8.jpeg" class="thumbnail" width="690" height="494"></div>

<div class="title-wrapper">
  <h3><a href="https://discourse.vtk.org/t/color-volume-rendering-vtkdataarray-indexing/5695/5" target="_blank" rel="noopener">Color Volume Rendering: vtkDataArray Indexing</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #E50068;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Web</span>
        </span>
      </span>
  </div>
</div>

  <p>Hi @Alireza and @sankhesh -  Regarding RGBA rendering, Sankesh and I discussed some issues I was running into so I did a dive into the shader code and was able to fix an issue to calculate shading from the alpha channel and get color from the RGB...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a href="https://github.com/Kitware/VTK/blob/master/Rendering/VolumeOpenGL2/vtkVolumeShaderComposer.h">The code</a>  has been rearranged but it looks like the bug is still there but I didn’t get back to it.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="26689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>you have to apply any thresholding, masking, dilation?</p>
</blockquote>
</aside>
<p>Yes, sort of.  What I did was to use the CT volume as the alpha channel directly, and that’s why the bone detail is so crisp.  Then for the RGB I did dilate the segmentation with a Voronoi-like distance function so that each voxel is the color of the nearest segment.  This way the ray samples around the segments get the correct color even when they make small opacity contributions and anything below the threshold is ignored.</p>
<p>I did some of this by hand and didn’t finish the code but there’s some <a href="https://github.com/pieper/SlicerMorph/tree/segmentation-rendering/SegmentationRendering">work in progress here</a>.</p>
<p>I didn’t do this but I thought about also changing the transfer function based on the nearest segment, so that, for example, even if a segment is in an area of low signal intensity it could still be made more opaque.  That is, allowing something closer to an isosurface rendering while retaining the image details.</p>
<p>It would definitely be fun to finish this up and make it available.</p>

---

## Post #10 by @lassoan (2022-12-11 18:36 UTC)

<p>Thank you, this is very useful. Is component 0 correspond to the alpha channel in the shader code? (in CPU memory the component order is RGBA)</p>
<p>With the shader code change, the results look different, a bit better, but I had to dilate the segments and there is still problem with if I don’t boost the opacity of segments that have low intensity:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a202f8712e2ececdcc6a58d5b64be7a986104d7b.jpeg" data-download-href="/uploads/short-url/n7dIigL1QyC1ASrUhaxg8t3fA3p.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a202f8712e2ececdcc6a58d5b64be7a986104d7b_2_690x403.jpeg" alt="image" data-base62-sha1="n7dIigL1QyC1ASrUhaxg8t3fA3p" width="690" height="403" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a202f8712e2ececdcc6a58d5b64be7a986104d7b_2_690x403.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a202f8712e2ececdcc6a58d5b64be7a986104d7b_2_1035x604.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a202f8712e2ececdcc6a58d5b64be7a986104d7b.jpeg 2x" data-dominant-color="777693"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1246×728 66.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @pieper (2022-12-11 19:03 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="26689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is component 0 correspond to the alpha channel in the shader code? (in CPU memory the component order is RGBA)</p>
</blockquote>
</aside>
<p>I’d have to go back and look - I remember the logic was odd.</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="26689">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>boost the opacity of segments that have low intensity</p>
</blockquote>
</aside>
<p>Yes, that’s what I meant by customizing the transfer function or alpha value based on the image values of the underlying volume.</p>
<p>Is your gist code up to date?</p>

---

## Post #12 by @lassoan (2022-12-11 22:40 UTC)

<p>I’ve updated the <a href="https://gist.github.com/lassoan/ecb3edaa42521261f5e552055065b3b5">gist</a> and uploaded the test scene <a href="https://github.com/lassoan/PublicTestingData/releases/download/data/ColoredVolumeRenderingScene.mrb">here</a>. I experimented with applying Margin effect - expanding all segments expand by 3mm (not quite Voronoi but should be OK for a quick test) - but it did not make a big difference. With or without margin growing, there are still those dark artifacts and blurriness in the rendering.</p>

---

## Post #13 by @muratmaga (2022-12-12 04:49 UTC)

<p>I still think this is better than both the surface rendering of segmentation (lower left), and its labelmap (lower right). But the background and intestines are too close and removing the background seems to remove the intestines as well.</p>
<p>For me the real benefit of RGBA is to replace the slow 3D model based rendering of segmentation. So in that specific case, it would be perhaps possible to mask out the background values (i.e values not assigned to a segment?)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/153e69153d31b8572305dbbd8486e551e5133d27.jpeg" data-download-href="/uploads/short-url/31VJVjzcysJpdey6T6QLLB9qouz.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/153e69153d31b8572305dbbd8486e551e5133d27_2_633x500.jpeg" alt="image" data-base62-sha1="31VJVjzcysJpdey6T6QLLB9qouz" width="633" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/153e69153d31b8572305dbbd8486e551e5133d27_2_633x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/153e69153d31b8572305dbbd8486e551e5133d27_2_949x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/153e69153d31b8572305dbbd8486e551e5133d27_2_1266x1000.jpeg 2x" data-dominant-color="8587AD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1342×1059 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #14 by @muratmaga (2022-12-12 05:04 UTC)

<p>Here it is with the background masked out (same ordering):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d474b1897b950ffb6760b876675a6e7393411d8f.jpeg" data-download-href="/uploads/short-url/ujteMsSrJog8iziKJybV2DtGGGr.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d474b1897b950ffb6760b876675a6e7393411d8f_2_588x500.jpeg" alt="image" data-base62-sha1="ujteMsSrJog8iziKJybV2DtGGGr" width="588" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d474b1897b950ffb6760b876675a6e7393411d8f_2_588x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d474b1897b950ffb6760b876675a6e7393411d8f_2_882x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d474b1897b950ffb6760b876675a6e7393411d8f_2_1176x1000.jpeg 2x" data-dominant-color="8388AA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1243×1056 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @lassoan (2022-12-12 05:49 UTC)

<p>I think what we miss for a good-quality volume rendering is smooth surface normal vectors. Surface normals may come from the original image, but it we only get surface normals in regions that have much higher intensity compared to surroundings, which are typically only bones and contrast material filled regions. There can be segment boundaries that do not have any corresponding change in input image intensity, so in these cases no matter how we try, we cannot get surface normals from the original image.</p>
<p>Therefore, at least in some boundaries, we would need to estimate the surface normal from the segmentation. If the direction estimation is done simply on the binary image then we get the blocky appearance as visible in the lower-right image. Masking causes sudden jump in the intensity similarly to a binary image, which causes the blockiness in the top image, too. If we apply smoothing on the binary segment or masked image (so that the change is intensity jump is spread over a few voxels) then the normals are very nice and smooth. Unfortunately, smoothing is computationally expensive, removes some relevant details, and it is not clear how can be performed on a labelmap that contains many labels.</p>
<p>Maybe the solution would be to use some higher-order method for gradient estimation (such as <a href="https://developer.nvidia.com/gpugems/gpugems2/part-iii-high-quality-rendering/chapter-20-fast-third-order-texture-filtering">this</a>) if the input is a labelmap volume. Currently, a very simple <a href="https://github.com/Kitware/VTK/blob/19b788991290cb9a4a5100ac37f1a250caf80158/Rendering/VolumeOpenGL2/vtkVolumeShaderComposer.h#L718-L739">central differences based gradient estimation is used in the volume rendering shader</a>, which only gives acceptable results if the voxel intensity is continuous (results in blocky appearance if voxel values are discrete labels).</p>

---

## Post #16 by @rbumm (2022-12-12 08:39 UTC)

<p>My take on this <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2f7bbfdc5fa5127beed6689229c687ed6cf42e2.jpeg" data-download-href="/uploads/short-url/pxdL0cFPzkpAyQHpjlFyT6vkY6K.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2f7bbfdc5fa5127beed6689229c687ed6cf42e2.jpeg" alt="image" data-base62-sha1="pxdL0cFPzkpAyQHpjlFyT6vkY6K" width="451" height="500" data-dominant-color="6C7277"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">599×664 46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This kind of hybrid display may help speed up the review of individual cases.</p>

---

## Post #17 by @rbumm (2022-12-12 08:47 UTC)

<p>The Shift slider in Volume rendering is too sensitive, and it would be great if it would be a ctkRangeWidget to enable entering range numbers …</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e9a11e48956745fa7056c86a24d7ced2a265cef.png" alt="image" data-base62-sha1="klvTqDVp41fLQmZViLcXynIvEe3" width="528" height="320"></p>

---

## Post #18 by @rkikinis (2022-12-12 12:09 UTC)

<p>Hi,<br>
you can adjust the sensitivity in the advanced tab in the section with the transfer function. P.S. the shift refers to shifting the transfer function.<br>
Best<br>
Ron</p>

---

## Post #19 by @rbumm (2022-12-12 13:00 UTC)

<p>Thanks <a class="mention" href="/u/rkikinis">@rkikinis</a> ,</p>
<p>Still quite difficult to hit the sweet spot</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43306854a1ec0760fbefe9ab0c5a911afbbc283d.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43306854a1ec0760fbefe9ab0c5a911afbbc283d.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43306854a1ec0760fbefe9ab0c5a911afbbc283d.mp4</a>
    </source></video>
  </div><p></p>
<p>unless I oversee something …</p>

---

## Post #20 by @rkikinis (2022-12-12 13:06 UTC)

<p>First set the slider below scalar opacity mapping. Then use the shift slider</p>

---

## Post #21 by @rbumm (2022-12-12 13:11 UTC)

<p>Hurrah.</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6bb5fe0b2820f387e49bb5cf21feb1bb22c4629.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6bb5fe0b2820f387e49bb5cf21feb1bb22c4629.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6bb5fe0b2820f387e49bb5cf21feb1bb22c4629.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #22 by @lassoan (2022-12-12 14:31 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a>, this image looks has very nice and smooth surface. Was it the result of enabling gradient opacity mapping? Were you able to get similarly smooth surfaces without making the segments semi-transparent?</p>

---

## Post #23 by @rbumm (2022-12-12 14:55 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Sorry for not providing that information.<br>
I used the dataset you linked, Median smoothed all segments (3.0 mm) and reduced the overall segment opacity to 0.4. Then combined it with a Muscle CT volume rendering.</p>

---

## Post #24 by @lassoan (2022-12-12 15:02 UTC)

<p>Oh, I see. In this topic we investigate the possibility of displaying the segmentation in 3D <strong>using volume rendering</strong> to preserve subtle details in the original image (that cannot be captured in a binary segmentation), make occlusion more realistic (make thicker structures less transparent), and make 3D display updates faster (without having to spend time with generating a surface mesh).</p>

---

## Post #25 by @ME_Rad (2023-06-23 17:57 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> Nice renderings.  I like the approach.<br>
<a class="mention" href="/u/lassoan">@lassoan</a> I am interested in exactly what you described.  Have you had any additional thoughts or implemented anything to make it easy for the end user to achieve?</p>
<p>Has anyone done a more photo-realistic coloring mapping based on the TotalSegmentator labels?  Ribs and vertebrae are whiteish, intestines are pinky red, etc.</p>

---

## Post #26 by @pieper (2023-10-15 21:49 UTC)

<p><a class="mention" href="/u/me_rad">@ME_Rad</a> - in case you missed it, there’s been some progress in fixing the underlying rendering code and adding a module in the sandbox extension that exposes this technique for end users.</p>
<p>See these links some example images and movies including TotalSegmentator labels.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/VTK/pull/43">
  <header class="source">

      <a href="https://github.com/Slicer/VTK/pull/43" target="_blank" rel="noopener">github.com/Slicer/VTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/VTK/pull/43" target="_blank" rel="noopener">BUG: use alpha to calculate RGBA lighting</a>
      </h4>

    <div class="branches">
      <code>Slicer:slicer-v9.2.20230607-1ff325c54</code> ← <code>pieper:fix-rgba-gpu-vr</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-10-06" data-time="22:33:11" data-timezone="UTC">10:33PM - 06 Oct 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/pieper" target="_blank" rel="noopener">
            <img alt="pieper" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
            pieper
          </a>
        </div>

        <div class="lines" title="3 commits changed 1 files with 34 additions and 19 deletions">
          <a href="https://github.com/Slicer/VTK/pull/43/files" target="_blank" rel="noopener">
            <span class="added">+34</span>
            <span class="removed">-19</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Implements the feature and fixes discussed in this thread:

https://discourse.<span class="show-more-container"><a href="https://github.com/Slicer/VTK/pull/43" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">slicer.org/t/volume-rendering-colorized-with-segmentation/26689/6

Basically allows RGBA volumes to be shaded according to their alpha component so that something like a CT or microCT can define an rgb value at spatial regions, while getting opacity and gradient information from the alpha channel (e.g. the Hounsfield unit).

Also always uses the 0 channel for defining the lighting parameters. This part is WIP since it may be more appropriate to set the alpha channel lighting parameters in this scenario.  Currently, at least in 3D Slicer, only the 0 compnent's lighting parameters are being set, so they are being used here.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="onebox githubfolder" data-onebox-src="https://github.com/PerkLab/SlicerSandbox/tree/master/ColorizeVolume">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerSandbox/tree/master/ColorizeVolume" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/PerkLab/SlicerSandbox/tree/master/ColorizeVolume" target="_blank" rel="noopener"></a></h3>

  <p><a href="https://github.com/PerkLab/SlicerSandbox/tree/master/ColorizeVolume" target="_blank" rel="noopener">//github.com/PerkLab/SlicerSandbox/tree/master/ColorizeVolume</a></p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<aside class="quote quote-modified" data-post="22" data-topic="31981">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/vtk-multivolume-cinematic-volume-rendering/31981/22">VTK multivolume/cinematic volume rendering</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    OMG! This is a game changer for us. 
We just now a way to adjust TF per segment basis somehow… And regular shadows/lights work great, just need the ambient shadows as <a class="mention" href="/u/lassoan">@lassoan</a> mentioned. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c5a532f77905930b10be6ff74d8539992e8f41f.jpeg" data-download-href="/uploads/short-url/fsx5oPUeuKWjMlnEJT2FAT5MqlN.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a>
  </blockquote>
</aside>


---

## Post #27 by @muratmaga (2023-10-16 19:02 UTC)

<p>Adding the new thread from <a class="mention" href="/u/jaimigray">@jaimigray</a> she posted. Check out the visuals.</p><aside class="quote quote-modified" data-post="1" data-topic="32254">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jaimigray/48/67886_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-colorize-volume-module/32254">New Colorize Volume module</a> <a class="badge-category__wrapper " href="/c/community/success-stories/29"><span data-category-id="29" data-parent-category-id="12" data-drop-close="true" class="badge-category --has-parent" title="This is the place where you can share how Slicer helped your work. Describe your project and how Slicer was useful in achieving your goal. Include reference to any publication(s) and if possible also add a few nice images or links to videos."><span class="badge-category__name">Success stories</span></span></a>
  </div>
  <blockquote>
    Just added to 3D Slicer 5.5 is the new Colorize Volume module! I tried it on a fully segmented rattlesnake skull with really nice results comparable to the expensive proprietary software VGStudio Max. I played around with the Volume Rendering settings, as well as Lights module (from the SandBox extension), and cropping to an ROI in the Volume Rendering module to bisect and view the inside of the skull. I am still exploring the various functions of this module but I am excited to see what else I …
  </blockquote>
</aside>


---
