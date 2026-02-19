---
topic_id: 44456
title: "Extract Center Line From Ct Empty Snail Shell"
date: 2025-09-12
url: https://discourse.slicer.org/t/44456
---

# Extract center line from CT empty snail shell

**Topic ID**: 44456
**Date**: 2025-09-12
**URL**: https://discourse.slicer.org/t/extract-center-line-from-ct-empty-snail-shell/44456

---

## Post #1 by @kuoi (2025-09-12 14:19 UTC)

<p>Hello, I know there is a <a href="https://discourse.slicer.org/t/new-module-extract-centerline-in-slicervmtk-extension/12117">post</a> about extracting a centerline from a solid 3D model. However, my case is more complicated: it is an empty shell with an internal cavity. What I actually want to do is extract a centerline from this cavity, save it as an .obj file, and then obtain contours of several equally spaced cross-sections perpendicular to the centerline for mathematical fitting. Could I get some suggestions on how to approach this?</p>
<p>I can show an example figure to illustrate what I mean. Centerline is shown as B, and the cross-section is shown as C.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/303992cdd64bb1d7694312a725c06b50c2dee9f1.jpeg" data-download-href="/uploads/short-url/6SCgGyK7bhxubYwUc9bLS4ypFuN.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/303992cdd64bb1d7694312a725c06b50c2dee9f1_2_517x135.jpeg" alt="image" data-base62-sha1="6SCgGyK7bhxubYwUc9bLS4ypFuN" width="517" height="135" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/303992cdd64bb1d7694312a725c06b50c2dee9f1_2_517x135.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/303992cdd64bb1d7694312a725c06b50c2dee9f1_2_775x202.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/303992cdd64bb1d7694312a725c06b50c2dee9f1.jpeg 2x" data-dominant-color="707072"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">843×220 37.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chir.set (2025-09-12 14:41 UTC)

<p><code>ExtractCenterline</code> can work with a model also. I’m not familiar with .obj files, but  my understanding is that they get presented as models, which are surface models. The problem with your specimen is that each individual coil is connected with the previous and/or the next. That may be bad for <code>ExtractCenterline</code>. If you get a valid centerline, you may next check the <code>CrossSectionAnalysis</code> module. Again the effect of the connectivity between successive coils is yet to be seen.</p>

---

## Post #3 by @kuoi (2025-09-12 14:44 UTC)

<p>I’m also wondering how I could automatically extract the cavity itself, so that everything else can proceed more easily, not that sure?</p>
<p>I imported the .obj file into 3D slicer, so it’s actually called model in software</p>

---

## Post #4 by @muratmaga (2025-09-12 14:59 UTC)

<aside class="quote no-group" data-username="kuoi" data-post="1" data-topic="44456">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/2acd7d/48.png" class="avatar"> kuoi:</div>
<blockquote>
<p>What I actually want to do is extract a centerline from this cavity,</p>
</blockquote>
</aside>
<p>This part should be easy. Just fill the cavity as a separate segment in Segment Editor using WrapSurfaceSolidify. And then use this segment to create center line.</p>
<aside class="quote no-group" data-username="kuoi" data-post="1" data-topic="44456">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/2acd7d/48.png" class="avatar"> kuoi:</div>
<blockquote>
<p>several equally spaced cross-sections perpendicular to the centerline for mathematical fitting.</p>
</blockquote>
</aside>
<p>This part you will probably have to code yourself.</p>

---

## Post #5 by @kuoi (2025-09-13 12:54 UTC)

<p>Thanks for your solution, I want to convert the model to a segment, however, it takes quite a long time for 3D slicer to convert. Is there any solution for this?</p>

---

## Post #6 by @kuoi (2025-09-13 16:09 UTC)

<p>Just some background: I only have model file .obj, so my first step is to generate segment and generate that cavity file</p>

---

## Post #7 by @lassoan (2025-09-13 21:52 UTC)

<aside class="quote no-group" data-username="kuoi" data-post="5" data-topic="44456" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/2acd7d/48.png" class="avatar"> kuoi:</div>
<blockquote>
<p>Thanks for your solution, I want to convert the model to a segment, however, it takes quite a long time for 3D slicer to convert. Is there any solution for this?</p>
</blockquote>
</aside>
<p>You can choose to make this step as fast or accurate as you need, by choosing the oversampling factor as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-model-surface-mesh-file">here</a>.</p>
<p>However, there is a much simpler and faster way: You can extract the inner surface of the shell using the <code>Dynamic modeler</code> module’s <code>Select by points</code> tool with <code>GeodesicDistance</code> selection algorithm and dropping a point in the inner surface of the shell somewhere deep inside (you can clip the model with a plane to see inside). The result is an open surface of the lumen. I think you can use this as input for the centerline computation as is, without even closing the surface.</p>
<p>Where is this image from? If it is from a micro-CT scanner then there is an even simpler way: You can avoid all the trouble of segmenting the shell then exporting it as an obj file and then importing into Slicer and trying to recover the segmentation. Instead, you can segment the image in Slicer and get the centerline (each takes just 2-3 clicks).</p>
<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="4" data-topic="44456">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<aside class="quote no-group" data-username="kuoi" data-post="1" data-topic="44456">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/2acd7d/48.png" class="avatar"> kuoi:</div>
<blockquote>
<p>several equally spaced cross-sections perpendicular to the centerline for mathematical fitting.</p>
</blockquote>
</aside>
<p>This part you will probably have to code yourself.</p>
</blockquote>
</aside>
<p>This is implemented in Cross-section analysis module, you just need to write a short Python code snippet that does the batch export in the format you prefer. This is probably 5-10 line of Python code that ChatGPT should be able to write for you.</p>

---

## Post #8 by @kuoi (2025-09-14 05:45 UTC)

<p>Hello, I tried using the “select by points” option, but unfortunately the snail shell does not have a clear boundary between the inner and outer surfaces. Below is my model, which was generated from a CT scan.</p>
<p>Additionally, the aperture of the shell is not parallel to the z-axis, so the centerline may curve upward or downward.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d0e09628ad524c2ddb13d0b8693e1e2089b10eb.jpeg" data-download-href="/uploads/short-url/mpn2fp6QLCgOPBsdc20wza7VB0L.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d0e09628ad524c2ddb13d0b8693e1e2089b10eb_2_690x318.jpeg" alt="image" data-base62-sha1="mpn2fp6QLCgOPBsdc20wza7VB0L" width="690" height="318" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d0e09628ad524c2ddb13d0b8693e1e2089b10eb_2_690x318.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d0e09628ad524c2ddb13d0b8693e1e2089b10eb_2_1035x477.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d0e09628ad524c2ddb13d0b8693e1e2089b10eb_2_1380x636.jpeg 2x" data-dominant-color="A5A2BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1781×822 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2025-09-15 04:59 UTC)

<p>Great! Starting from the CT scan should be much easier. You can extract the interior volume of the spiral using Segment Editor module and then get the centerline directly from the segmentation.</p>
<p>If the boundaries are intact then simple thresholding will work well. It takes just a few clicks. If there are small cracks in the surfaces then you can use the margin effect to make sure any connections between adjacent whorls are broken up. Margin effect takes away voxels from the entire surface of an object, so it should not impact the centerline.</p>
<p>If the holes are bigger then you can erase the connections manually or use the Wrap Solidify effect (choosing “Region” → “largest cavity”).</p>

---

## Post #10 by @kuoi (2025-09-15 05:21 UTC)

<p>I tried the segment editor</p>
<p>My approach shown as follows</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74829cbc90efe0da50163e73e049f3903473e4d3.png" data-download-href="/uploads/short-url/gCHdLurYJAqeqM0pSsFYLNm4n6z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74829cbc90efe0da50163e73e049f3903473e4d3_2_383x500.png" alt="image" data-base62-sha1="gCHdLurYJAqeqM0pSsFYLNm4n6z" width="383" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74829cbc90efe0da50163e73e049f3903473e4d3_2_383x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74829cbc90efe0da50163e73e049f3903473e4d3_2_574x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74829cbc90efe0da50163e73e049f3903473e4d3.png 2x" data-dominant-color="E8EAEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">744×969 67.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>then click the cube bottom</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bb3536a8fb4654ec49a1155e21c527f513afd9b.png" data-download-href="/uploads/short-url/mdod82JkO6IF8h3weoyproDTCgH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bb3536a8fb4654ec49a1155e21c527f513afd9b.png" alt="image" data-base62-sha1="mdod82JkO6IF8h3weoyproDTCgH" width="690" height="408" data-dominant-color="DBDBDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">768×455 24.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>select okay, source geometry is the segment from .obj.</p>
<p>I haven’t found wrapsurfacesolidify, some tutorial video shows that’s a exnteion, but I haven’t found via searcing.</p>
<p>Also any bottom at the left I clicked, it always shows</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd550ae9a817f4a8b3d8fe8c8638f71daaacf192.png" data-download-href="/uploads/short-url/r0UrAdeI5kzOTV7hZOjFbDVpLDY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd550ae9a817f4a8b3d8fe8c8638f71daaacf192.png" alt="image" data-base62-sha1="r0UrAdeI5kzOTV7hZOjFbDVpLDY" width="568" height="252"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">568×252 25 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I click yes, it will take quite a long time</p>

---

## Post #11 by @lassoan (2025-09-15 05:31 UTC)

<p>It seems that you have created a surface mesh in some software and trying to import it into Slicer as a segmentation. This is a lot of extra steps that adds time, complexity, and may result in loss of details. It should be much simpler to load the CT image (DICOM files or a TIFF, PNG, or JPG stack - not some surface mesh file, such as an OBJ, PLY, or STL) and segment that image using Segment Editor module.</p>

---

## Post #12 by @kuoi (2025-09-15 05:36 UTC)

<p>So what I actually need is stacks of tiff files and .obj files? But now I am somewhat confused about the whole logic.</p>
<p>The main logic is load stacks of tiff → volume rendering to generate a volume → segment editor? I totally felt lost.</p>

---

## Post #13 by @lassoan (2025-09-15 05:47 UTC)

<p>Surface mesh (OBJ/STL/PLY file) should not be needed in the workflow at this stage. You can follow these steps:</p>
<ul>
<li>Install Slicer</li>
<li>Install SurfaceWrapSolidify extension in Slicer’s Extensions Manager</li>
<li>Load 3D Image (DICOM, TIFF/JPG/PNG stack, etc.) into Slicer</li>
<li>Switch to Segment Editor module</li>
<li>Use Threshold effect to segment the shell</li>
<li>Use Wrap Solidify effect to extract the largest cavity</li>
</ul>
<p>There are many variants of this workflow (instead of Wrap Solidify you can manually close down the opening of the shell and then use Islands effect to segment the internal volume; you can use Margin effect to break up connections between adjacent whorls; etc.) but without having access to the data or seeing your intermediate results (e.g., Thresholding and Wrap Solidify output) it is hard to tell what works best.</p>

---

## Post #14 by @kuoi (2025-09-15 07:52 UTC)

<p>Thanks for your answer, it solves quite a lof of my questions. I had serveral shells in one scan, so what should I do to seperate them? During the segmen editor or any other stage?</p>

---

## Post #15 by @kuoi (2025-09-15 13:35 UTC)

<p>I currently obtained a model using wrap solidify to extract the inner structure while excluding the shell.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/390487b98606d732ca19c117f1ab1586acd568e4.jpeg" data-download-href="/uploads/short-url/88oV8TKMKv6ZFeb5DeRnNIkYLLC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/390487b98606d732ca19c117f1ab1586acd568e4_2_476x500.jpeg" alt="image" data-base62-sha1="88oV8TKMKv6ZFeb5DeRnNIkYLLC" width="476" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/390487b98606d732ca19c117f1ab1586acd568e4_2_476x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/390487b98606d732ca19c117f1ab1586acd568e4.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/390487b98606d732ca19c117f1ab1586acd568e4.jpeg 2x" data-dominant-color="9590AF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">676×709 96.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, whenever I run extract centerline without a point list, I receive the following notification:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38fe8fe88539190dcdcd782cbac3fd3ef17b7008.png" data-download-href="/uploads/short-url/88c8nMlolvfT7jeSHf65ak0LTBK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38fe8fe88539190dcdcd782cbac3fd3ef17b7008.png" alt="image" data-base62-sha1="88c8nMlolvfT7jeSHf65ak0LTBK" width="690" height="138" data-dominant-color="62605C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">955×191 12.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Therefore, I have to add two points to define the start and end. What I am unsure about is whether it matters if my aperture point is placed in the middle of the aperture curve surface.</p>
<p>Another issue is that after using wrap solidify, the inner structure does not perfectly match the shell. Do you think this approach could be a solution?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf7925f0787ee3da898e6c5c5f25bdab456b5622.jpeg" data-download-href="/uploads/short-url/tBoovaxS3EI6CbHtQ8ZYbxls28q.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf7925f0787ee3da898e6c5c5f25bdab456b5622.jpeg" alt="image" data-base62-sha1="tBoovaxS3EI6CbHtQ8ZYbxls28q" width="322" height="326"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">322×326 33.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @chir.set (2025-09-15 14:23 UTC)

<p>Your centerline curve in the first image is impressive <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=14" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> . I don’t think that <code>CrossSectionAnalysis</code> would be able to give you the outline of the cross-sections as you expected because there’s a common wall all along. It can still show you the maximum inscribed sphere.</p>
<p>You may also try the <code>Curve Planar Reformat</code> module if you have an input volume, to see how far it can straighten such an elaborate geometry.</p>

---

## Post #17 by @kuoi (2025-09-16 04:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="44456">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>you can manually close down the opening of the shell and then use Islands effect to segment the internal volume</p>
</blockquote>
</aside>
<p>Hello, could I know if I want to manually close the aperture, what tool I need? Do I need to first manually closed that in blender or 3D slicer can also handle this?</p>

---

## Post #18 by @lassoan (2025-09-16 12:39 UTC)

<p>It seems that you oretty much solved the task! It looks like Wrap Solidify to be doing a perfect job in closing the aperture and the detected centerline is accurate.</p>
<p>If you see a small distance between the cavity segment and the shell and small distances then you can adjust Wrap Solidify effect parameters to work at higher resolution (at the cost of longer computation time) to diminish that. However, probably it is not needed, because it does not impact the centerline location. If you have doubts then you can do a small experiment on a few dozen scans to see if increasing the resolution leads to significant difference in the centerline computation results.</p>
<p>You can implement an algorithm to automatically pick the two endpoints of the curve (one endpoint is the wrapped surface point that has the largest distance from original surface; the other endpoint is the farthest surface point from some automatically determined base plate). Considering that developing and testing this algorithm can take a few days, while manually marking may take less than a minute per case, it would only pay off to develop a fully automatic method if you need to segment thousands of these scans.</p>
<aside class="quote no-group" data-username="kuoi" data-post="14" data-topic="44456">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/2acd7d/48.png" class="avatar"> kuoi:</div>
<blockquote>
<p>I had serveral shells in one scan, so what should I do to seperate them? During the segmen editor or any other stage?</p>
</blockquote>
</aside>
<p>You can use the Split Volume effect (provided by SegmentEditorExtraEffects extension), which is developed for exactly this purpose.</p>

---

## Post #19 by @kuoi (2025-09-16 16:02 UTC)

<p>Hello, yes, I think so. But the problem is that</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2547debac3bfcb33aae9faef0e95d3716935a759.jpeg" data-download-href="/uploads/short-url/5jNE827UFl2YgmMl5UE4CAauhux.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2547debac3bfcb33aae9faef0e95d3716935a759_2_690x497.jpeg" alt="image" data-base62-sha1="5jNE827UFl2YgmMl5UE4CAauhux" width="690" height="497" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2547debac3bfcb33aae9faef0e95d3716935a759_2_690x497.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2547debac3bfcb33aae9faef0e95d3716935a759.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2547debac3bfcb33aae9faef0e95d3716935a759.jpeg 2x" data-dominant-color="C7D6DB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">957×690 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This section, as I pointed out, should be filled using warp solidify. Which parameters should I adjust to achieve that?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4a431a710cf3b2f91292690aa8ebf988b5a7716.png" data-download-href="/uploads/short-url/s3zmP6VnCmewRYCqqkkTJRphriC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4a431a710cf3b2f91292690aa8ebf988b5a7716_2_503x500.png" alt="image" data-base62-sha1="s3zmP6VnCmewRYCqqkkTJRphriC" width="503" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4a431a710cf3b2f91292690aa8ebf988b5a7716_2_503x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4a431a710cf3b2f91292690aa8ebf988b5a7716.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4a431a710cf3b2f91292690aa8ebf988b5a7716.png 2x" data-dominant-color="E5E5E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">646×642 50.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I cannot finish it perfectly, how can I manually close the aperture? I tried drawing, but it is very tricky. Could I use a SlicerMorph grid surface to achieve a similar effect and close the aperture?</p>
<p>Regarding the start and end point for the centerline, may I know whether any point on the aperture surface would cause the same effect or not?</p>
<p>Thanks a lot.</p>

---

## Post #20 by @kuoi (2025-09-16 17:04 UTC)

<p>Additionally, what about the inner structure being broken? How can I fix that?</p>

---

## Post #21 by @lassoan (2025-09-17 01:03 UTC)

<aside class="quote no-group" data-username="kuoi" data-post="19" data-topic="44456">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/2acd7d/48.png" class="avatar"> kuoi:</div>
<blockquote>
<p>Regarding the start and end point for the centerline, may I know whether any point on the aperture surface would cause the same effect or not?</p>
</blockquote>
</aside>
<p>The centerline will end near the marked point, so make sure to mark the endpoint of the centerline near the middle of the opening.</p>
<p>You can increase <code>Oversampling</code> to increase accuracy. See <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">documentation</a>:</p>
<blockquote>
<ul>
<li><strong>Oversampling</strong>: Specifies resolution during internal remeshing. Higher value results in higher accuracy but longer computation time. <strong>Increase this value up to 2-4x if output does not follow the input segmentation accurately enough.</strong></li>
</ul>
</blockquote>
<p>It is very hard to guess how to fine-tune your results and address remaining small issues just by looking at a few screenshots. I would recommend to share a dataset (upload to dropbox, onedrive, etc. and post the link here) or bring your dataset to one of the Slicer meeting:</p>
<ul>
<li><a href="https://discourse.slicer.org/c/community/hangout/20">online weekly meeting</a></li>
<li><a href="https://slicermorph.github.io/#three">online monthly SlicerMorph meeting</a></li>
<li><a href="https://projectweek.na-mic.org/">in-person biannual Slicer meeting</a></li>
</ul>

---

## Post #22 by @kuoi (2025-09-17 01:54 UTC)

<p>I tried increasing oversampling from 1.5x to 2.5x, but it doesn’t help at all. I want to close the aperture, then it will probably be okay, but the editing tool in 3D slicer isn’t as flexible as Blender. So, I want to try editing the model in Blender first, then convert it to a series of TIFF photos (but everything will fail in voxelized processes).</p>
<p>I can share a model link here. <a href="http://tmpfiles.org/dl/912876/slice_0000.nrrd" rel="noopener nofollow ugc">http://tmpfiles.org/dl/912876/slice_0000.nrrd</a></p>
<p>This shell has no broken structures, but you will find the aperture surface, which is not filled<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cbfee82f9af6cc1390144177eb83642cbfe23a6.jpeg" data-download-href="/uploads/short-url/aWXuY3DbAEYcFuW0NUDNaTKnYTs.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4cbfee82f9af6cc1390144177eb83642cbfe23a6_2_613x500.jpeg" alt="image" data-base62-sha1="aWXuY3DbAEYcFuW0NUDNaTKnYTs" width="613" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4cbfee82f9af6cc1390144177eb83642cbfe23a6_2_613x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cbfee82f9af6cc1390144177eb83642cbfe23a6.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4cbfee82f9af6cc1390144177eb83642cbfe23a6.jpeg 2x" data-dominant-color="BC2833"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">768×626 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I also need to think about how to deal with a slightly broken shell</p>
<p>I guess I already missed this week’s meeting, I may join next week, maybe timezone is not that friendly</p>

---

## Post #23 by @lassoan (2025-09-17 05:53 UTC)

<p>Thanks, the data file was very useful. The opening is very large, so it makes sense to close it before you extract the internal volume. You can use “Baffle planner” module (provided by SlicerHeart extension).</p>
<p>Here is a short video that shows the entire workflow:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="m4Kt0QmmYO4" data-video-title="Extract centerline of a shell's internal cavity" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=m4Kt0QmmYO4" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/m4Kt0QmmYO4/maxresdefault.jpg" title="Extract centerline of a shell's internal cavity" width="690" height="388">
  </a>
</div>


---

## Post #24 by @kuoi (2025-09-17 06:06 UTC)

<p>Thanks I just used another way to do similar tthing, actually your method is muchs simplier than what I did. Thanks a lot.</p>

---

## Post #25 by @lassoan (2025-09-17 13:59 UTC)

<p>Note that the curve provided by <code>Extract Centerline</code> module’s “centerline” method finds the shortest path on the medial surface (approximated by the edges of the Voronoi diagram, purple spiky surface in the screenshot), which is not the geometric center of the cross-section for a spiral shape:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c431c0e596cdef52791a4b8a04f99db687280595.jpeg" data-download-href="/uploads/short-url/rZCbcdlCF4bX1roS0Yx3BeZzLBH.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c431c0e596cdef52791a4b8a04f99db687280595_2_690x473.jpeg" alt="image" data-base62-sha1="rZCbcdlCF4bX1roS0Yx3BeZzLBH" width="690" height="473" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c431c0e596cdef52791a4b8a04f99db687280595_2_690x473.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c431c0e596cdef52791a4b8a04f99db687280595_2_1035x709.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c431c0e596cdef52791a4b8a04f99db687280595_2_1380x946.jpeg 2x" data-dominant-color="6F6978"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1318 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can use <code>Curved Planar Reformat</code> module (in Sandbox extension) to straighten the spiral and get an idea about the shape and size of the cross-sections in simple 2D images:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/190467fb3272a00c6c385b67a2db2bda8cc494c5.jpeg" data-download-href="/uploads/short-url/3zjnn030uNGCHrAw1SJpp9sTZFX.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/190467fb3272a00c6c385b67a2db2bda8cc494c5_2_690x476.jpeg" alt="image" data-base62-sha1="3zjnn030uNGCHrAw1SJpp9sTZFX" width="690" height="476" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/190467fb3272a00c6c385b67a2db2bda8cc494c5_2_690x476.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/190467fb3272a00c6c385b67a2db2bda8cc494c5_2_1035x714.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/190467fb3272a00c6c385b67a2db2bda8cc494c5_2_1380x952.jpeg 2x" data-dominant-color="9D9CAC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1327 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can use <code>Endoscopy</code> module to fly through inside the shell to inspect segmentation quality or to get a sense of shapes and sizes inside the shell.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8c19cbb8baca48d0523fab1ebc8ff85085575e8.jpeg" data-download-href="/uploads/short-url/zuBdWNWIbmApmYxq70aFdkl0cpq.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8c19cbb8baca48d0523fab1ebc8ff85085575e8_2_690x310.jpeg" alt="image" data-base62-sha1="zuBdWNWIbmApmYxq70aFdkl0cpq" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8c19cbb8baca48d0523fab1ebc8ff85085575e8_2_690x310.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8c19cbb8baca48d0523fab1ebc8ff85085575e8_2_1035x465.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8c19cbb8baca48d0523fab1ebc8ff85085575e8_2_1380x620.jpeg 2x" data-dominant-color="837A7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×863 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #26 by @kuoi (2025-09-18 02:03 UTC)

<p>Can I know if there is any centerline algorithm that can be perpendicular to the last plane that we sealed the shell?</p>

---

## Post #27 by @lassoan (2025-09-18 02:12 UTC)

<p>Yes, curves have a built-in algorithm for this. More specifically, its <a href="https://apidocs.slicer.org/main/classvtkMRMLMarkupsCurveNode.html#ab23760b90d69d1b2e8392c75ce0a7123"> GetCurvePointToWorldTransformAtPointIndex</a> method provides transforms that can be used to translate an object (such as the end plate) along the curve, with minimal spinning and rotation.</p>

---

## Post #28 by @kuoi (2025-09-18 02:22 UTC)

<p>Could you please tell me how I can use that? Do I need to use the Python console in 3D Slicer, or is there a graphical user interface available?</p>

---

## Post #29 by @lassoan (2025-09-18 02:29 UTC)

<p>No graphical user interface is provided for such specialized needs, but you need to write some Python code snippets to describe what you need exactly. Most of the code can be written by AI chatbots, but you need to be able to provide guidance for them. You can start from the Cross-section analysis module, which gets the cross-section that is orthogonal to the centerline, and modify it to use planes that are parallel to the end plate instead.</p>

---

## Post #30 by @kuoi (2025-09-18 05:29 UTC)

<p>So the main logic should be that… I list all points on that plate then tried to see if it’s perpendicular to the plate using that function?</p>

---

## Post #31 by @lassoan (2025-09-18 12:16 UTC)

<p>You can transform the endplate normal directiom from World coordinate system to Curve coordinate system. The plane normal direction remains the same along the curve in he same direction anywhere along the curve in Curve coordinate system. You can get the plane direction in World coordinate system by using the CurvePointToWorld transformation matrix.</p>

---

## Post #32 by @kuoi (2025-09-19 05:46 UTC)

<p>Thanks, I tried a lot, however, it’s still quite difficult for me. Coding is not that big problem, the main problem is that quite a lot of API I’m not familiar with, many terms, e.g. world etc., I will think about any other solution.</p>

---

## Post #33 by @lassoan (2025-09-19 16:53 UTC)

<p>Learning any new API is always time consuming and spending the time on it is a bit of a gamble when you are not sure yet what tools you will use in the end. Fortunately, chatbots are quite good at knowing APIs of open-source tools, such as Slicer, so you don’t have to dig into documentation or examples, just start vibe coding right away. You can also get help from community members who can help out (online, in virtual meetings, and in-person meetings) or get dedicated support from a Slicer Commercial Partner company. You are probably really close to what you need (reslicing the volume with planes parallel to the endplate is about 10 lines of quite simple Python code), but of course you can look around if you can find any tools that work better for you.</p>

---
