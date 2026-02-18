# Working with RGBA in Volume Rendering

**Topic ID**: 44814
**Date**: 2025-10-20
**URL**: https://discourse.slicer.org/t/working-with-rgba-in-volume-rendering/44814

---

## Post #1 by @muratmaga (2025-10-20 04:35 UTC)

<p>I am trying to import some multichannel microscopy data into Slicer. I can get the RGBA volume loaded and shown correctly in the slice views.  But when I volume render it (by dragging and dropping into the 3D view), all I get is a blackbox. Using the slider, seems have no effect (or rather the only effect I get is box disappears). Switching to individual components doesn’t seem to help either. I remember being able to render RGBA images before. Is this a regression, or this about the data? Here is the link to the data: <a href="https://app.box.com/s/1gfscb42fnshsbatfar9u7z0c8wnktl6" class="inline-onebox" rel="noopener nofollow ugc">Box</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a464c6a507700c5115417bbce255306c0f1eb19d.jpeg" data-download-href="/uploads/short-url/nsidqM3mwEsQV21LGAsWHFPRYex.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a464c6a507700c5115417bbce255306c0f1eb19d_2_690x410.jpeg" alt="image" data-base62-sha1="nsidqM3mwEsQV21LGAsWHFPRYex" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a464c6a507700c5115417bbce255306c0f1eb19d_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a464c6a507700c5115417bbce255306c0f1eb19d_2_1035x615.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a464c6a507700c5115417bbce255306c0f1eb19d_2_1380x820.jpeg 2x" data-dominant-color="7F6F76"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1775×1056 265 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-10-20 14:52 UTC)

<p>The issue is that your alpha is 255 everywhere, so the block is the correct rendering.</p>
<p>If you make the alpha into something meaningful then you can look at different structures.  E.g. here I’ve made alpha be the red channel:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; a = arrayFromVolume(getNode("IMS*"))
&gt;&gt;&gt; a[...,3] = a[...,0]
&gt;&gt;&gt; arrayFromVolumeModified(getNode("IMS*"))
&gt;&gt;&gt; 
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec90d2fb9fe1958761cd677154094e6fb0cb3ee8.jpeg" data-download-href="/uploads/short-url/xKKXYslAcgq5KdK5XBiAVVLznU4.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec90d2fb9fe1958761cd677154094e6fb0cb3ee8_2_690x497.jpeg" alt="image" data-base62-sha1="xKKXYslAcgq5KdK5XBiAVVLznU4" width="690" height="497" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec90d2fb9fe1958761cd677154094e6fb0cb3ee8_2_690x497.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec90d2fb9fe1958761cd677154094e6fb0cb3ee8_2_1035x745.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec90d2fb9fe1958761cd677154094e6fb0cb3ee8.jpeg 2x" data-dominant-color="8B83B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1322×954 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And here the blue:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9862acd5dac29bc9278bb55db422a56e06f5939.jpeg" data-download-href="/uploads/short-url/obG8X43OSn8f5KWhFTL8155mzmp.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9862acd5dac29bc9278bb55db422a56e06f5939_2_690x485.jpeg" alt="image" data-base62-sha1="obG8X43OSn8f5KWhFTL8155mzmp" width="690" height="485" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9862acd5dac29bc9278bb55db422a56e06f5939_2_690x485.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9862acd5dac29bc9278bb55db422a56e06f5939_2_1035x727.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9862acd5dac29bc9278bb55db422a56e06f5939.jpeg 2x" data-dominant-color="9B9BD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1330×936 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @muratmaga (2025-10-20 16:10 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>. What is a meaningful alpha in this case, 0.5? I want to see it as RGB as opposed to individual ones.</p>

---

## Post #4 by @pieper (2025-10-20 16:38 UTC)

<p>I’m not sure, you may need to experiment.  If alpha is constant it will be like the block you had before.  Ideally you would make an alpha channel that identifies a structure or region of interest and then the color would be some other information, something simple like 0.2<em>r + 0.7</em>g + 0.1*b (brightness) would be good for visible light, but I’m not sure that’s what you want here.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; a = arrayFromVolume(getNode("IMS*"))
&gt;&gt;&gt; a[...,3] = .2 * a[...,0] + .7 * a[...,1] + .1 * a[...,2]
&gt;&gt;&gt; arrayFromVolumeModified(getNode("IMS*"))
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8be52d781392684b853b195bf7c5edd3d2036872.jpeg" data-download-href="/uploads/short-url/jXznvvzWg6J1npV7QuCtM4OEdP4.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8be52d781392684b853b195bf7c5edd3d2036872_2_690x440.jpeg" alt="image" data-base62-sha1="jXznvvzWg6J1npV7QuCtM4OEdP4" width="690" height="440" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8be52d781392684b853b195bf7c5edd3d2036872_2_690x440.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8be52d781392684b853b195bf7c5edd3d2036872_2_1035x660.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8be52d781392684b853b195bf7c5edd3d2036872_2_1380x880.jpeg 2x" data-dominant-color="B2A6A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1606×1026 246 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>An average of all three might be good.  This basically makes the black background transparent and renders only where there’s “signal” in the images.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; arrayFromVolumeModified(getNode("IMS*"))
&gt;&gt;&gt; a = arrayFromVolume(getNode("IMS*"))
&gt;&gt;&gt; a[...,3] = .33 * a[...,0] + .33 * a[...,1] + .33 * a[...,2]
&gt;&gt;&gt; arrayFromVolumeModified(getNode("IMS*"))
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90c2ab8d992cefe9e37790c7579e52baeaad1534.jpeg" data-download-href="/uploads/short-url/kEBPK6blVK657RGdBiKBF1bHyQs.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90c2ab8d992cefe9e37790c7579e52baeaad1534_2_690x456.jpeg" alt="image" data-base62-sha1="kEBPK6blVK657RGdBiKBF1bHyQs" width="690" height="456" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90c2ab8d992cefe9e37790c7579e52baeaad1534_2_690x456.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90c2ab8d992cefe9e37790c7579e52baeaad1534_2_1035x684.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90c2ab8d992cefe9e37790c7579e52baeaad1534_2_1380x912.jpeg 2x" data-dominant-color="D9D1D4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1578×1044 248 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @muratmaga (2025-10-20 17:36 UTC)

<p>Himm, does that mean this needs to be some kind of user input during the rendering that is adjusted real-time (how much emphasis on R, G, B)?</p>

---

## Post #6 by @pieper (2025-10-20 17:48 UTC)

<p>We could imagine adding something like that, yes.  It’s probably application specific.  In something like CT is it customary to use x-ray density as an implicit or explicit alpha channel.  But you may also want something like a gradient opacity expressed in your alpha.  Or if this is some kind of tagged staining microscopy it could be that one channel makes more sense to use as alpha.</p>
<p>What actually is your data and what are you trying to see in it?</p>

---

## Post #7 by @muratmaga (2025-10-20 17:53 UTC)

<p>It is not specific to anything. I am trying to convince the microscopy group here to use Slicer more for their basic visualization needs. For that I created a simple module that reads their Imaris format and seem to work adequately. When it comes to visualizing RGB, there are couple issues:</p>
<ol>
<li>Can split the channels individually and assign manual Luts (R, G, B). that works well but it breaks when I want to simultaneously render them. Multivolume renderer doesn’t seem to support more than two (and is missing features anyways), and if I use the GPU raycasting, the depth is not preserved correctly.</li>
<li>It is not clear to me whether 16bt per channel RGBA images are supported. It looks like original data is 16 bit per channel (at least raw value are in excess of 256). I am having to do 8 bit conversion to get it displyed in slice views (otherwise slice views are also black).</li>
</ol>

---

## Post #8 by @pieper (2025-10-20 18:04 UTC)

<p>Yes, I’m sure there are limitations to rgba mode.  Remember it was not working at all at the VTK shader level until I fixed it for the ColorizeVolume module.  There could be other limitations that assume RGB will always be 8 bit, but I think in principle the mode should be supported so probably any fixes would be merged.</p>
<p>But my point is that alpha doesn’t have a fixed meaning for all purposes, so some amount of interface and flexibility would be required.</p>

---

## Post #9 by @lassoan (2025-10-20 18:04 UTC)

<p>With <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> we recently added multi-component volume rendering for SlicerHeart (to show B-mode + Doppler images). This is very well applicable to any multichannel images.</p>
<p>The image that you provided had 3 useful channels, the first one seem to be anatomy, while the other second and third have signals in some smaller regions.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85552d2a987016da76c95a94594df79d99e4f0ac.jpeg" data-download-href="/uploads/short-url/j1vZzYYZ8sx0QPhlaXyRZi9qoNK.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85552d2a987016da76c95a94594df79d99e4f0ac_2_690x447.jpeg" alt="image" data-base62-sha1="j1vZzYYZ8sx0QPhlaXyRZi9qoNK" width="690" height="447" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85552d2a987016da76c95a94594df79d99e4f0ac_2_690x447.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85552d2a987016da76c95a94594df79d99e4f0ac_2_1035x670.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85552d2a987016da76c95a94594df79d99e4f0ac_2_1380x894.jpeg 2x" data-dominant-color="7A7D7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1246 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I used a gray color transfer function for component 0, some colored ones for 1 and 2, and all transparent for 3 (because it was just a solid block):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2d9d796a7a743386133df78a2c1878961d4be62.png" data-download-href="/uploads/short-url/neE4DJ0HbSpRlQhAQMuGavajVEC.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2d9d796a7a743386133df78a2c1878961d4be62_2_690x203.png" alt="image" data-base62-sha1="neE4DJ0HbSpRlQhAQMuGavajVEC" width="690" height="203" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2d9d796a7a743386133df78a2c1878961d4be62_2_690x203.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2d9d796a7a743386133df78a2c1878961d4be62_2_1035x304.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2d9d796a7a743386133df78a2c1878961d4be62_2_1380x406.png 2x" data-dominant-color="DDEAE3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2884×852 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There was no need for any data manipulation in Python, it was all done in the GUI.</p>
<p>Up to 4 channels can be rendered like this independently - you can specify opacity and color transfer function for each channel. If you have more channels then you would need to preprocess the data - either select certain channels or combine multiple channels into up to 4 channels that you render independently or as an RGBA color volume.</p>

---

## Post #10 by @pieper (2025-10-20 18:08 UTC)

<p>That’s cool <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=14" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20">   I hadn’t seen that mode before.  That’s the point I was making that these channels are really RGB in this interpretation, more like [alpha, stain1, stain2].  If that’s really the way they did the acquisition this is the sort of interface they probably want.</p>

---

## Post #11 by @muratmaga (2025-10-20 19:00 UTC)

<p>This is great. It is working for me too!</p>
<p>If this the case, do we still need RGBA images, or can I just import them as RGB? Also do you know whether 16 bit per channel is supported?</p>

---

## Post #12 by @lassoan (2025-10-21 04:45 UTC)

<p>No need for manual generation of an alpha channel.</p>
<ul>
<li>If you load an RGB volume then you can render it as a color volume (alpha channel is generated automatically as the average of the RGB channels).</li>
<li>If you load a multichannel image then you can render each channel independently.</li>
</ul>
<p>16-bit per channel is supported. You can render images consisting of 8 to 64 bit integer or floating-point voxels, up to 4 components.</p>

---

## Post #13 by @muratmaga (2025-10-21 17:03 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="44814">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>16-bit per channel is supported.</p>
</blockquote>
</aside>
<p>I think there is an issue with the independent component’s (specifically index 1 and 2), as the Scalar Opacity Mapping range does not go beyond 1024, it appears hardcoded limits (I can’t enter a higher value manually either). It doesn’t happen for component 0, that one automatically gets the full range of intensities in the data. As a result by rendering is blocky, since I need values around 1300 range to remove the noise.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e5dff3d2e7bb8b7f2337e3333373b1109ead0bb.jpeg" data-download-href="/uploads/short-url/mAYPkXugoLYJ5O7DagSnm78tShd.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e5dff3d2e7bb8b7f2337e3333373b1109ead0bb_2_555x500.jpeg" alt="image" data-base62-sha1="mAYPkXugoLYJ5O7DagSnm78tShd" width="555" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e5dff3d2e7bb8b7f2337e3333373b1109ead0bb_2_555x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e5dff3d2e7bb8b7f2337e3333373b1109ead0bb_2_832x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e5dff3d2e7bb8b7f2337e3333373b1109ead0bb_2_1110x1000.jpeg 2x" data-dominant-color="9C808A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1282×1153 275 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c78a460b79906af63876c31aa5b7b0da11fa968e.png" data-download-href="/uploads/short-url/stdgwiNsq0rMsSiPLEp14tUYf7w.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c78a460b79906af63876c31aa5b7b0da11fa968e.png" alt="image" data-base62-sha1="stdgwiNsq0rMsSiPLEp14tUYf7w" width="544" height="257"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">544×257 14.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @muratmaga (2025-10-21 17:08 UTC)

<p>In fact I flatlined scalar opacity mapping of all three components (they are all zero opacities), but I am still seeing this block. First channel has intensities 154-3734 range, second 46-7158, and third 75-7689</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b06a72087952f9ce1268c1861f0934d2a8ef236.jpeg" data-download-href="/uploads/short-url/aHI3XJNSCpWo2LSdhe4tr5b2CCG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b06a72087952f9ce1268c1861f0934d2a8ef236_2_574x500.jpeg" alt="image" data-base62-sha1="aHI3XJNSCpWo2LSdhe4tr5b2CCG" width="574" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b06a72087952f9ce1268c1861f0934d2a8ef236_2_574x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b06a72087952f9ce1268c1861f0934d2a8ef236_2_861x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b06a72087952f9ce1268c1861f0934d2a8ef236_2_1148x1000.jpeg 2x" data-dominant-color="999AA7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1232×1072 368 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @muratmaga (2025-10-22 22:15 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="13" data-topic="44814">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>(specifically index 1 and 2), as the Scalar Opacity Mapping range does not go beyond 1024,</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> <a class="mention" href="/u/lassoan">@lassoan</a> any thoughts on this?</p>

---
