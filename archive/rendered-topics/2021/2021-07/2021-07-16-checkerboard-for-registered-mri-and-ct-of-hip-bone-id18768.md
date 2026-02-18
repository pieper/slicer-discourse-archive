# Checkerboard for registered MRI and CT of hip bone

**Topic ID**: 18768
**Date**: 2021-07-16
**URL**: https://discourse.slicer.org/t/checkerboard-for-registered-mri-and-ct-of-hip-bone/18768

---

## Post #1 by @HodaGH (2021-07-16 17:34 UTC)

<p>Hi everyone,</p>
<p>I would like to make a checkerboard image of my registered CT and MRI. This is what I get when the CT image is input volume 1:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab117fdb64c0e9e160861575000784d72a24846c.png" data-download-href="/uploads/short-url/opl8FuIN25C16wDhfmHmLMsKfJW.png?dl=1" title="CTinputvolume1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab117fdb64c0e9e160861575000784d72a24846c_2_690x243.png" alt="CTinputvolume1" data-base62-sha1="opl8FuIN25C16wDhfmHmLMsKfJW" width="690" height="243" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab117fdb64c0e9e160861575000784d72a24846c_2_690x243.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab117fdb64c0e9e160861575000784d72a24846c_2_1035x364.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab117fdb64c0e9e160861575000784d72a24846c_2_1380x486.png 2x" data-dominant-color="828282"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CTinputvolume1</span><span class="informations">1592×562 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and this is when I have MRI as the input volume 1:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3b0f616f7e16dc5c72506d0fc40301f881bd9ba.png" data-download-href="/uploads/short-url/yLNa74s5vDMb7NwUjYEvxMEetLk.png?dl=1" title="MRIinputvolume1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3b0f616f7e16dc5c72506d0fc40301f881bd9ba_2_690x255.png" alt="MRIinputvolume1" data-base62-sha1="yLNa74s5vDMb7NwUjYEvxMEetLk" width="690" height="255" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3b0f616f7e16dc5c72506d0fc40301f881bd9ba_2_690x255.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3b0f616f7e16dc5c72506d0fc40301f881bd9ba_2_1035x382.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3b0f616f7e16dc5c72506d0fc40301f881bd9ba_2_1380x510.png 2x" data-dominant-color="1B1B1B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">MRIinputvolume1</span><span class="informations">1408×522 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How can I optimize to get a good checkerboard?<br>
Thank you very much.</p>

---

## Post #2 by @pieper (2021-07-16 17:46 UTC)

<p>Yes, there’s a checkerboard filter: <a href="https://slicer.qualitybox.us/wiki/Documentation/4.10/Modules/CheckerBoardFilter" class="inline-onebox">Documentation/4.10/Modules/CheckerBoardFilter - Slicer Wiki</a></p>
<p>Also the CompareVolumes module has a “Layer Reveal Cursor” that is basically an interactive checkerboard.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/CompareVolumes" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/4.10/Modules/CompareVolumes</a></p>

---

## Post #3 by @HodaGH (2021-07-16 17:53 UTC)

<p>Thanks for your reply. I mean from the checkerboard images I attached above I can’t really see the second modality to be able to compare the edges to the input modality to see if I have a good registration. Is there any way to make the second input darker or more visible?</p>

---

## Post #4 by @pieper (2021-07-16 18:24 UTC)

<p>Are you saying you made them with the checkerboard filter?  I don’t think there’s a way to change the individual window/levels using that module.  If you use the layer reveal cursor you can change the window/level of the foreground and background the normal way and also zoom and pan.</p>

---

## Post #5 by @lassoan (2021-07-16 22:02 UTC)

<p>Checkerboard filter is a very, very poor visualization method for comparing images. It is one of those methods that only become somewhat popular because it is very easy to implement. The main problem is that you would need large squares to be able to interpret the image, but you need small squares so that you can compare the image contents (because you only see difference at the boundary of the squares).</p>
<p>For example visualizing misalignment using checkerboard with 4, 8, 16 divisions:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2db5c04a561ba9a6e045bcd87d820ca5891739f.jpeg" data-download-href="/uploads/short-url/u5kf8R8JcvhIWkGjIyTwzk3Ulzx.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d2db5c04a561ba9a6e045bcd87d820ca5891739f_2_690x221.jpeg" alt="image" data-base62-sha1="u5kf8R8JcvhIWkGjIyTwzk3Ulzx" width="690" height="221" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d2db5c04a561ba9a6e045bcd87d820ca5891739f_2_690x221.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d2db5c04a561ba9a6e045bcd87d820ca5891739f_2_1035x331.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d2db5c04a561ba9a6e045bcd87d820ca5891739f_2_1380x442.jpeg 2x" data-dominant-color="8E8E8E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1788×575 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Instead, take one image and overlay edges extracted from the other image. You can use Canny edge detector or similar filters if you want to have a general idea about displacements/distortions. You need to first convert the input image to float type (using Cast Scalar Volume module) and then use Simple Filters module to do the Canny filtering (try with lower threshold = upper threshold = 50) or other filtering. You can change the colormap using Volumes module.</p>
<p>Example:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8ac16eb47875644f16de9954b7d6a0d62144b465.jpeg" data-download-href="/uploads/short-url/jNujIs85K4xzoli2NCHp1yTDspL.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ac16eb47875644f16de9954b7d6a0d62144b465_2_690x273.jpeg" alt="image" data-base62-sha1="jNujIs85K4xzoli2NCHp1yTDspL" width="690" height="273" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ac16eb47875644f16de9954b7d6a0d62144b465_2_690x273.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ac16eb47875644f16de9954b7d6a0d62144b465_2_1035x409.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8ac16eb47875644f16de9954b7d6a0d62144b465_2_1380x546.jpeg 2x" data-dominant-color="5E5E4E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1447×573 390 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But in general, it is even better to segment the structure(s) of interest in one image and display that over the other image. It is also simpler, as segmentations is displayed already overlaid on the image. If you don’t want to segment any specific object then you can use simple thresholding to get a good set of contours.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac287512e1a044ba5e7e0d2fc4ab281ff9d45ee7.jpeg" data-download-href="/uploads/short-url/oyYNROYANVKi5RWIYNU7jlsnqED.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac287512e1a044ba5e7e0d2fc4ab281ff9d45ee7_2_690x334.jpeg" alt="image" data-base62-sha1="oyYNROYANVKi5RWIYNU7jlsnqED" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac287512e1a044ba5e7e0d2fc4ab281ff9d45ee7_2_690x334.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac287512e1a044ba5e7e0d2fc4ab281ff9d45ee7_2_1035x501.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac287512e1a044ba5e7e0d2fc4ab281ff9d45ee7.jpeg 2x" data-dominant-color="8A8B8A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1183×573 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @HodaGH (2021-07-19 07:36 UTC)

<p>Thanks very much for the comprehensive explanation. I have the segmentations but my confusion is from having a good alignment when the three views are centered like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c28b9158bafbdc6dc97c1dfd42295b93b74d90d8.jpeg" data-download-href="/uploads/short-url/rL1EpzzD8Dx488Z2h0ur18nQ5WE.jpeg?dl=1" title="Screen Shot 2021-07-19 at 3.24.46 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c28b9158bafbdc6dc97c1dfd42295b93b74d90d8_2_690x467.jpeg" alt="Screen Shot 2021-07-19 at 3.24.46 AM" data-base62-sha1="rL1EpzzD8Dx488Z2h0ur18nQ5WE" width="690" height="467" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c28b9158bafbdc6dc97c1dfd42295b93b74d90d8_2_690x467.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c28b9158bafbdc6dc97c1dfd42295b93b74d90d8_2_1035x700.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c28b9158bafbdc6dc97c1dfd42295b93b74d90d8.jpeg 2x" data-dominant-color="494A51"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-07-19 at 3.24.46 AM</span><span class="informations">1248×845 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
but when I scroll between the slides the alignment won’t be as good in axial and sagittal views as this picture shows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/717853a47c2b1ae139d27cc1adf11697d6c291ed.jpeg" data-download-href="/uploads/short-url/gbNKGu4GK2Vn3pTGOkCX963dEzb.jpeg?dl=1" title="Screen Shot 2021-07-19 at 3.26.11 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/717853a47c2b1ae139d27cc1adf11697d6c291ed_2_690x492.jpeg" alt="Screen Shot 2021-07-19 at 3.26.11 AM" data-base62-sha1="gbNKGu4GK2Vn3pTGOkCX963dEzb" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/717853a47c2b1ae139d27cc1adf11697d6c291ed_2_690x492.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/717853a47c2b1ae139d27cc1adf11697d6c291ed_2_1035x738.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/717853a47c2b1ae139d27cc1adf11697d6c291ed.jpeg 2x" data-dominant-color="45454D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-07-19 at 3.26.11 AM</span><span class="informations">1217×868 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
So I thought maybe checkerboard could help.</p>

---

## Post #7 by @lassoan (2021-07-19 11:33 UTC)

<p>This visualization using segmentation is very informative. It seems that the femurs are in a different position (slightly more anterior) in the image that was segmented.</p>
<p>If you want perfect alignment of the bones then you will need to do piecewise registration (register each bone separately). You can open a new topic if you want to do that but not sure how.</p>

---

## Post #8 by @Saima (2021-11-10 05:28 UTC)

<p>Hi Andras,<br>
I am trying to use the labelmap check box in the simple filters fro canny edge filter but it is not working.</p>
<p>Any help.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #9 by @lassoan (2021-11-10 06:41 UTC)

<p>The labelmap checkbox is an indicator (grayed out, not to be controlled by the user). You don’t need to convert the float-valued Canny edge detector output to labelmap volume, you can simply select it as foreground volume and then configure its appearance in Volumes module (set a lower threshold &gt; 0 to make the background image visible; you may set a different colormap, adjust the window/level).</p>

---

## Post #10 by @Saima (2021-11-11 03:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="18768">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>re its appearance in Volumes mod</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
I get like this<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81324a80ed0dd524412f897fefc77d319abbb50b.jpeg" alt="image" data-base62-sha1="iqVlbzYL4ArVfdzWI6Ive6xm9u3" width="514" height="361"></p>
<p>if I select the region of interest and create a new volume using the segment editor. I get <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d6b27abea4f53fcee1257ebfc2563231a1a1007.jpeg" alt="image" data-base62-sha1="4cfqm5ssbMsAvxjSZhivPzZ1Mvt" width="514" height="361"></p>
<p>In the volumes I am not understanding how to get the edges.</p>
<p>in simple filters I am using 50 for low and upper threshold. Any help please?</p>
<p>Thankyou</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #11 by @lassoan (2021-11-11 03:57 UTC)

<p>Probably you want to increase “Variance” value to reduce the number of contours. For example try something like 2.0, 2.0, 2.0.</p>
<p>Canny edge detection result with default parameters for MRHead sample data set:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7674377ce2fa6996aa7600f9aef744c2d84ecd1b.jpeg" data-download-href="/uploads/short-url/gTTkKMkVXgoufgobKdEfuwscsCn.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7674377ce2fa6996aa7600f9aef744c2d84ecd1b_2_370x500.jpeg" alt="image" data-base62-sha1="gTTkKMkVXgoufgobKdEfuwscsCn" width="370" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7674377ce2fa6996aa7600f9aef744c2d84ecd1b_2_370x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7674377ce2fa6996aa7600f9aef744c2d84ecd1b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7674377ce2fa6996aa7600f9aef744c2d84ecd1b.jpeg 2x" data-dominant-color="848484"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">414×558 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After setting Variance to 2.0, 2.0, 2.0:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/717ca9d958bc52fbbf126b4858517b9b67b9e0f1.png" data-download-href="/uploads/short-url/gbX2KKkQecxKCJbn4AlRi6kLbA5.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/717ca9d958bc52fbbf126b4858517b9b67b9e0f1.png" alt="image" data-base62-sha1="gbX2KKkQecxKCJbn4AlRi6kLbA5" width="368" height="500" data-dominant-color="3B3B3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">411×557 81.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After setting Upper threshold to 10:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d8541ea6f3474a2307fc98794cf805b70f950b0.png" data-download-href="/uploads/short-url/6uGZjLbNV59bXTamjvTJierUUYo.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d8541ea6f3474a2307fc98794cf805b70f950b0.png" alt="image" data-base62-sha1="6uGZjLbNV59bXTamjvTJierUUYo" width="392" height="500" data-dominant-color="2F2F2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">403×513 54.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After choosing the grayscale volume as background, Canny output as foreground, foreground opacity to 0.5, and in Volumes module setting 0.5 threshold and a color lookup table:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39a6dfd3f49aaf84de5b466865498e5c8a6366f3.jpeg" data-download-href="/uploads/short-url/8e0K1Q78UVQdrIbDP1iGAWGgzXZ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/39a6dfd3f49aaf84de5b466865498e5c8a6366f3_2_690x418.jpeg" alt="image" data-base62-sha1="8e0K1Q78UVQdrIbDP1iGAWGgzXZ" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/39a6dfd3f49aaf84de5b466865498e5c8a6366f3_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/39a6dfd3f49aaf84de5b466865498e5c8a6366f3_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/39a6dfd3f49aaf84de5b466865498e5c8a6366f3_2_1380x836.jpeg 2x" data-dominant-color="ADA8AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1165 202 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @Saima (2021-11-12 06:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="18768">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>0.5, and in Volumes module setting 0.5 threshold and a color looku</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
Is there a way to calculate the Hausdorff distance for the cannyedge outputs.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #13 by @lassoan (2021-11-12 06:25 UTC)

<p>There have been attempts like this in the past to define a similarity metric based on automatically extracted contours. However, most normally you would evaluate misalignment based on landmark points or segmented surfaces.</p>

---
