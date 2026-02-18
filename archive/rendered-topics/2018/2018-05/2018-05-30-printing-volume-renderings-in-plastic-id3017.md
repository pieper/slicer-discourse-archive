# Printing volume renderings in plastic

**Topic ID**: 3017
**Date**: 2018-05-30
**URL**: https://discourse.slicer.org/t/printing-volume-renderings-in-plastic/3017

---

## Post #1 by @pieper (2018-05-30 12:42 UTC)

<p>A question that comes up on this forum from time to time is why we can’t <a href="https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524">just 3D print the volume rendered view</a>.  We explain that most printers today expect STL surface models and we go into the difference between volume rendering and surface segmentation.</p>
<p>I wanted to point out some just published research about new printing techniques that are much closer to directly printing out a volume rendering.</p>
<p>These are photographs of 3D prints made using this technique:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a496d030927d0e4275076c12a22a39b048e7a5b0.jpeg" data-download-href="/uploads/short-url/nu1q6rRtxvFEDEQE9YPpsTP0S4g.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a496d030927d0e4275076c12a22a39b048e7a5b0_2_382x500.jpg" alt="image" data-base62-sha1="nu1q6rRtxvFEDEQE9YPpsTP0S4g" width="382" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a496d030927d0e4275076c12a22a39b048e7a5b0_2_382x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a496d030927d0e4275076c12a22a39b048e7a5b0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a496d030927d0e4275076c12a22a39b048e7a5b0.jpeg 2x" data-dominant-color="40392E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">564×738 95.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here’s our paper that describes the method:</p>
<p><a href="https://www.liebertpub.com/doi/pdf/10.1089/3dp.2017.0140" class="onebox" target="_blank" rel="noopener">https://www.liebertpub.com/doi/pdf/10.1089/3dp.2017.0140</a></p>
<p>It still requires special printers and materials, but if the technique proves useful we can expect it to become more commonly available.</p>

---

## Post #2 by @lassoan (2018-05-30 13:38 UTC)

<p>These look beautiful and it’s great that you don’t need to segment your data.</p>

---

## Post #3 by @lassoan (2018-10-10 04:11 UTC)

<p>An extension has been added to Slicer that can print such models: <a href="https://github.com/SlicerFab/SlicerFab">SlicerFab</a>. It is available in the extension manager for recent nightly builds.</p>

---

## Post #6 by @Wan (2020-04-10 02:20 UTC)

<p>Hello, I am  a Chinese student and I am going to print a heart model like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/4028e827a6289d977a922bb17574dffae0c9ba22.jpeg" data-download-href="/uploads/short-url/99AcrgsfnwTFuEkKv3XPvdtOrjY.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4028e827a6289d977a922bb17574dffae0c9ba22_2_690x367.jpeg" alt="image" data-base62-sha1="99AcrgsfnwTFuEkKv3XPvdtOrjY" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4028e827a6289d977a922bb17574dffae0c9ba22_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4028e827a6289d977a922bb17574dffae0c9ba22_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4028e827a6289d977a922bb17574dffae0c9ba22_2_1380x734.jpeg 2x" data-dominant-color="9D9FA3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1023 447 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
But I encountered certain difficulties in volume rendering, my heart model is dark, like this picture. It doesn’t has any color,  so I got  numbers of bitmap(png) without colors. How can I save this problem.</p>

---

## Post #7 by @lassoan (2020-04-10 02:52 UTC)

<p>In cardiac CT images, all contrast-filled structures have similar image intensity, so direct volume rendering will not help. You need to segment the image as explained here in detail:</p>
<div class="lazyYT" data-youtube-id="BJoIexIvtGo" data-youtube-title="Whole heart segmentation from cardiac CT in 10 minutes" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #8 by @Wan (2020-04-10 12:16 UTC)

<p>I‘m sorry. My English is poor, I will describe my question more clearly:<br>
I want to 3D print a heart model. In the 3D slicer, I used the “grow from seed” method and got the following picture:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71d4ab9ee27322c37288cd2c626b32d5c7196759.jpeg" data-download-href="/uploads/short-url/geZB69U7k0tqjpG6iQUbhG8rFmV.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71d4ab9ee27322c37288cd2c626b32d5c7196759_2_690x370.jpeg" alt="image" data-base62-sha1="geZB69U7k0tqjpG6iQUbhG8rFmV" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71d4ab9ee27322c37288cd2c626b32d5c7196759_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71d4ab9ee27322c37288cd2c626b32d5c7196759_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71d4ab9ee27322c37288cd2c626b32d5c7196759_2_1380x740.jpeg 2x" data-dominant-color="9EA0A3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1031 429 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I know that only the volume can be rendered, so I want to convert these 8 segmentation into volume. In this step, I used the “split volume” method. This way I got 8 volumes。<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed241e4ad053f6678bc045d69a5fceab5df83f41.png" alt="image" data-base62-sha1="xPQxHPipDbcUOxBmk61fduudbQ5" width="625" height="437"><br>
I want to render these volumes one by one, superimposed in the window, like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5864da9a86224f80ded91bdcf0f47eddaa1f0d9a.jpeg" data-download-href="/uploads/short-url/cBY5WKajeWePIhJguaMiA2E3mNY.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5864da9a86224f80ded91bdcf0f47eddaa1f0d9a_2_690x194.jpeg" alt="image" data-base62-sha1="cBY5WKajeWePIhJguaMiA2E3mNY" width="690" height="194" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5864da9a86224f80ded91bdcf0f47eddaa1f0d9a_2_690x194.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5864da9a86224f80ded91bdcf0f47eddaa1f0d9a_2_1035x291.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5864da9a86224f80ded91bdcf0f47eddaa1f0d9a_2_1380x388.jpeg 2x" data-dominant-color="B0B0BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×542 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @Wan (2020-04-10 12:20 UTC)

<p>Finally I got the picture below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56fc0d30b32429a0040877d832081b7a670411a5.jpeg" data-download-href="/uploads/short-url/cpv4YTNBGScZWmMkAH6zxBVqSwJ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/56fc0d30b32429a0040877d832081b7a670411a5_2_690x361.jpeg" alt="image" data-base62-sha1="cpv4YTNBGScZWmMkAH6zxBVqSwJ" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/56fc0d30b32429a0040877d832081b7a670411a5_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/56fc0d30b32429a0040877d832081b7a670411a5_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/56fc0d30b32429a0040877d832081b7a670411a5_2_1380x722.jpeg 2x" data-dominant-color="A1A2A5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1005 380 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
But I have this very serious problem when using bitmap generator. There is nothing left<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87a5b90b6537b60707a540630ed24d43446210a5.jpeg" data-download-href="/uploads/short-url/jlZw7kDIFgB8xORAUfq0VXg2Yol.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/87a5b90b6537b60707a540630ed24d43446210a5_2_690x370.jpeg" alt="image" data-base62-sha1="jlZw7kDIFgB8xORAUfq0VXg2Yol" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/87a5b90b6537b60707a540630ed24d43446210a5_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/87a5b90b6537b60707a540630ed24d43446210a5_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/87a5b90b6537b60707a540630ed24d43446210a5_2_1380x740.jpeg 2x" data-dominant-color="C1C2C5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1032 255 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I think maybe multiple volumes cause an error, but the same problem still happens when I try render one volume and generate bitmap.<br>
I ’m sure there are no errors in my bitmap, because the picture below is a successful example<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e11cd441ed6c57d2fb2d6be7b058840812a12da1.jpeg" data-download-href="/uploads/short-url/w7rcdbG58nQ1nkZtqbELFjh8fSx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e11cd441ed6c57d2fb2d6be7b058840812a12da1_2_690x331.jpeg" alt="image" data-base62-sha1="w7rcdbG58nQ1nkZtqbELFjh8fSx" width="690" height="331" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e11cd441ed6c57d2fb2d6be7b058840812a12da1_2_690x331.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e11cd441ed6c57d2fb2d6be7b058840812a12da1_2_1035x496.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e11cd441ed6c57d2fb2d6be7b058840812a12da1_2_1380x662.jpeg 2x" data-dominant-color="B7B9BE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×922 234 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Thank you for reading, I look forward to your answer, thank you</p>

---

## Post #10 by @pieper (2020-04-10 13:05 UTC)

<p><a class="mention" href="/u/wan">@Wan</a> - Can you try the latest nightly preview of Slicer and the SlicerFab extension?  If the bitmap generator is not working for you please share a scene that can be used to replicate the issue.</p>

---

## Post #11 by @lassoan (2020-04-10 16:52 UTC)

<p>If you already segmented your volume then you don’t need bitmap printing but you can use a regular plastic color printer. You need to export the segmentation to STL or colored OBJ (using Export to files feature in Segment Editor). You may also export to colored VRML (as described <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_entire_scene_as_VRML">here</a>) or glTF (using <a href="https://github.com/PerkLab/SlicerOpenAnatomy">SlicerOpenAnatomy extension</a>).</p>

---

## Post #12 by @lassoan (2020-12-12 21:32 UTC)

<p>A post was split to a new topic: <a href="/t/i-have-lots-of-questions-can-i-write-you-an-email/15025">I have lots of questions. Can I write you an email?</a></p>

---

## Post #13 by @facfox (2022-06-22 02:43 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> , thanks a lot for the great plugin!<br>
However after exporting the slicing images using Slicerfab with only 6 colors, the Voxel Print Utility still shows error “voxel data contains 4043(too many) colors”… Guess the boundaries are still not clear enough… Any solution to that??<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98990e40f3e7db0d7d1ab719a69e871ff96070f7.png" data-download-href="/uploads/short-url/lLWuJNZO5Ke4gL1Wyl7dhvUAUZh.png?dl=1" title="b863390c6f4cfd62408bde8370fa41c" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98990e40f3e7db0d7d1ab719a69e871ff96070f7.png" alt="b863390c6f4cfd62408bde8370fa41c" data-base62-sha1="lLWuJNZO5Ke4gL1Wyl7dhvUAUZh" width="690" height="393" data-dominant-color="F4F4F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">b863390c6f4cfd62408bde8370fa41c</span><span class="informations">912×520 6.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #14 by @lassoan (2022-06-22 13:38 UTC)

<p>Slicer exports full-color images. You need to apply dithering on the exported images if you want to reduce the total number of colors used. I have never gone further than generating the full-color images, so I cannot recommend any specific software to do that. If you find a good one then please share it here to help future users.</p>

---

## Post #15 by @facfox (2022-06-23 06:18 UTC)

<p>Thanks! I got the same answer from Stratasys team asking me to use the dithering/halftoning tools to process the image, I will find a way to bulk process them then.</p>

---

## Post #16 by @Esteban_Barreiro (2022-06-23 09:02 UTC)

<p>it could be great if SlicerFab have dithering within the algorithm. We were using Gimp with Bimp (the batch mode modification for Gimp, all free and open source software) to change the amount of colours by dithering the images, but still having errors to solve. And I recently post an error, I was using SlicerFab properly until today <a href="https://discourse.slicer.org/t/slicerfab-doesnt-work-properly-in-5-0-2/24001">https://discourse.slicer.org/t/slicerfab-doesnt-work-properly-in-5-0-2/24001</a></p>

---

## Post #17 by @lassoan (2022-06-23 15:07 UTC)

<aside class="quote no-group" data-username="Esteban_Barreiro" data-post="16" data-topic="3017">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/esteban_barreiro/48/5430_2.png" class="avatar"> Esteban_Barreiro:</div>
<blockquote>
<p>it could be great if SlicerFab have dithering within the algorithm</p>
</blockquote>
</aside>
<p>Dithering should be done by the printer manufacturer, because only they know the optimal parameters (which colors are available, what is the resolution, what amount of each color can be deposited, etc.).</p>
<p>However, until they provide this feature it woul be indeed nice if Slicer could do some generic dithering.</p>
<p>Integrating Gimp/Bimp with Slicer could be somewhat complicated, as they are both applications and I’m not sure if they have a command-line interface.</p>
<p>However, using <a href="https://imagemagick.org/">ImageMagick</a> should be quite easy. It has nice <a href="https://legacy.imagemagick.org/Usage/quantize/#intro">quantization features</a> and Slicer could run the command-line tool to quantize each captured image slice.</p>

---

## Post #18 by @Dr3dGeoff (2022-08-19 13:03 UTC)

<p>Hi, I’m a bit confused how to use this extension to convert a .STL file into a stack of images for use in inkjet 3D printing.  I can import the .STL fine, but then when I try to use the extension it returns a traceback error, attached below.</p>
<p>I’ll be honest, I’m a materials development person.  Software always throws me for a loop.  Any help understanding what I’m looking at, what’s going wrong, and how the software understands STLs would be wonderful.</p>
<p>"Traceback (most recent call last):<br>
File “C:/Users/geoff/AppData/Local/NA-MIC/Slicer 5.0.3/NA-MIC/Extensions-30893/SlicerFab/lib/Slicer-5.0/qt-scripted-modules/BitmapGenerator.py”, line 157, in onApplyButton<br>
self.logic.generate(volumeRenderingNode, filePattern)<br>
File “C:/Users/geoff/AppData/Local/NA-MIC/Slicer 5.0.3/NA-MIC/Extensions-30893/SlicerFab/lib/Slicer-5.0/qt-scripted-modules/BitmapGenerator.py”, line 268, in generate<br>
self.create3dView(volumeRenderingNode)<br>
File “C:/Users/geoff/AppData/Local/NA-MIC/Slicer 5.0.3/NA-MIC/Extensions-30893/SlicerFab/lib/Slicer-5.0/qt-scripted-modules/BitmapGenerator.py”, line 251, in create3dView<br>
self.threeDViewNode.SetAndObserveParentLayoutNodeID(viewOwnerNode.GetID())<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetID’</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/geoff/AppData/Local/NA-MIC/Slicer 5.0.3/NA-MIC/Extensions-30893/SlicerFab/lib/Slicer-5.0/qt-scripted-modules/BitmapGenerator.py”, line 160, in onApplyButton<br>
logging.error(“Error: {0}”.format(e.message))<br>
AttributeError: ‘AttributeError’ object has no attribute ‘message’"</p>

---

## Post #19 by @pieper (2022-08-19 13:49 UTC)

<p>It looks like the SlicerFab extension needs to be updated to work with the recent Slicer5 release.  Probably you can have it working with an older release.</p>
<p>But FYI, if you are starting with an STL file than SlicerFab is not what you need.  The BitmapGenerator is for taking volumetric data, like a CT scan and making rendered slices (rgb images).  STL files are already surface models.</p>

---

## Post #20 by @Dr3dGeoff (2022-08-19 15:40 UTC)

<p>Ah, I see, thank you.  This is what came up while hunting around online, I guess the keywords were a bit tricked.  Thanks so much!</p>

---
