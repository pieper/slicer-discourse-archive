# Is there interest in higher quality rendering for Slicer?

**Topic ID**: 6862
**Date**: 2019-05-20
**URL**: https://discourse.slicer.org/t/is-there-interest-in-higher-quality-rendering-for-slicer/6862

---

## Post #1 by @Dave_DeMarle (2019-05-20 22:50 UTC)

<p>Hello,</p>
<p>If I may, I would like to ask the group if there is significant interest in future extensions to Slicer that would bridge the gap to photorealistic rendering?</p>
<p>In the ParaView world we’ve been doing work with NVidia’s IndeX and OptiX (volume and surface rendering respectively) and Intel’s OSPRay (both volume and surface) that give ParaView the ability to render photorealistic images. I would like to make the case for doing the same thing in Slicer.</p>
<p>So, do you think that photorealism be a useful tool medical visualization? If it was available what would you use it for and what controls and features would you want to see? Also, if Slicer isn’t the right platform, could you suggest others?</p>
<p>thank you for your insights.</p>

---

## Post #2 by @muratmaga (2019-05-21 01:17 UTC)

<p><a class="mention" href="/u/dave_demarle">@Dave_DeMarle</a></p>
<p>I will be interested in the seeing these features in the Slicer, especially if they are compatible with the existing volume rendering interface. I think Slicer is indeed the right platform for it. But I think a good photorealistic renderer also can benefit from some sort of a keyframe rendering to enable complex animations, which we currently seem to lack.</p>

---

## Post #3 by @hherhold (2019-05-21 11:05 UTC)

<p>I would be very interested in this as well, as would colleagues here who use Slicer. I can’t speak for medical imaging, but would be very useful in invertebrate and vertebrate zoology and paleontology. If I have specific lighting or surfacing requirements, I usually wind up exporting models to Blender.</p>
<p>A key-framing animation setup would be a very welcome addition, but I’m also aware that it’s likely a major undertaking. As with photorealistic rendering, any time I need to do any animations, I likewise export models to Blender. Just for my uses, I would actually put some kind of key-framing animation setup for camera movement at a higher priority than photorealistic rendering. I’ve tried to use the endoscopy module before but I just can’t get it to do what I’d like it to do. (Problem between chair and keyboard, probably.)</p>
<p>I have no experience with OSPRay, so I’m not sure what it can do. Things I would like to see in a photorealistic rendering setup would include the ability to position multiple lights, different light types (point, directional, area), light color, enable/disable casting shadows, the ability to set some rudimentary surface shading parameters (a whole node-based shading system would be awesome but total overkill), etc. I do a lot of transparency shading to show internal structures, so rudimentary controls like that would be very useful.</p>
<p>I used to use ParaView for animations but have not checked it out in a while - if these are the directions they’re going in lately, I will definitely have to take a look. Exporting from Slicer to ParaView is super-easy.</p>
<p>-Hollister</p>

---

## Post #4 by @muratmaga (2019-05-21 11:30 UTC)

<p>I agree with <a class="mention" href="/u/hherhold">@hherhold</a>, if one is to be prioritized over one I think keyframe editor is a bigger issue for people who wants to do animations of their organism in Slicer.</p>

---

## Post #5 by @lassoan (2019-05-21 16:45 UTC)

<aside class="quote no-group" data-username="Dave_DeMarle" data-post="1" data-topic="6862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dave_demarle/48/3772_2.png" class="avatar"> Dave_DeMarle:</div>
<blockquote>
<p>do you think that photorealism be a useful tool medical visualization?</p>
</blockquote>
</aside>
<p>In medical imaging, photorealistic volume rendering is advertised as “cinematic rendering”. There are mixed results in using it for diagnostics (complex lighting may improve depth perception and even visibility of some structures in certain circumstances, but it may also make it harder to see some details). However, more realistic rendering would be very welcome in medical education and in communication between patients and physicians. We (and I guess many other) users would be very interested in trying these techniques.</p>
<aside class="quote no-group" data-username="Dave_DeMarle" data-post="1" data-topic="6862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dave_demarle/48/3772_2.png" class="avatar"> Dave_DeMarle:</div>
<blockquote>
<p>If it was available what would you use it for and what controls and features would you want to see?</p>
</blockquote>
</aside>
<p>Same interface as regular volume rendering (presets, transfer function editor, quality/speed controls, etc.), shadows enable/disable, and light editing (probably lightkit presets, maybe tuning of position of key light and intensity of filling lights exposed on the GUI). We would also like to use multi-volume rendering.</p>
<aside class="quote no-group" data-username="Dave_DeMarle" data-post="1" data-topic="6862">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dave_demarle/48/3772_2.png" class="avatar"> Dave_DeMarle:</div>
<blockquote>
<p>if Slicer isn’t the right platform, could you suggest others?</p>
</blockquote>
</aside>
<p>For medical image visualization (human and animal) Slicer is probably the best platform for many reasons. The infrastructure is already in place, only little work is needed to expose new volume rendering features on the GUI. The main reason we have not considered adding OSPray support to Slicer yet is because of the long rendering time for good-quality images (see details below) - but if there is a chance for fast options then we should work together to make it available for users.</p>
<p>Current experience with OSPray:</p>
<p>With default settings in ParaView, speed is borderline tolerable but there are significant rendering artifacts compared to baseline GPU raycasting.</p>
<p>GPU raycasting (baseline, non-photorealistic):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fce4ae202724026112a41260441a9ffafe251b1f.jpeg" data-download-href="/uploads/short-url/A5cgAyEBcft6qksNorTjCCCGi6j.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fce4ae202724026112a41260441a9ffafe251b1f_2_690x449.jpeg" alt="image" data-base62-sha1="A5cgAyEBcft6qksNorTjCCCGi6j" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fce4ae202724026112a41260441a9ffafe251b1f_2_690x449.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fce4ae202724026112a41260441a9ffafe251b1f_2_1035x673.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fce4ae202724026112a41260441a9ffafe251b1f_2_1380x898.jpeg 2x" data-dominant-color="C8C7CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2245×1463 957 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>OSPray (default settings: samples per pixel = 1):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/955cc62b829ab41617435c840e12d510557c947b.jpeg" data-download-href="/uploads/short-url/ljjUsHw3Pq88YxCNePt3x5o6qDN.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/955cc62b829ab41617435c840e12d510557c947b_2_690x449.jpeg" alt="image" data-base62-sha1="ljjUsHw3Pq88YxCNePt3x5o6qDN" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/955cc62b829ab41617435c840e12d510557c947b_2_690x449.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/955cc62b829ab41617435c840e12d510557c947b_2_1035x673.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/955cc62b829ab41617435c840e12d510557c947b_2_1380x898.jpeg 2x" data-dominant-color="B2AFB2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2245×1463 1.21 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Increasing samples per pixel value removes many artifacts but surfaces still look quite messy at high-gradient areas (maybe sampling distance is not small enough? but I did not find how to set that in ParaView) and rendering is not interactive anymore (rendering may take 5-20 seconds).</p>
<p>OSPray (default settings: samples per pixel = 15):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4619a0028570d0d70076ae0d00e530d0e924596.jpeg" data-download-href="/uploads/short-url/wAlYmIf97gD2NJPIejcVHWOlMqi.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4619a0028570d0d70076ae0d00e530d0e924596_2_690x449.jpeg" alt="image" data-base62-sha1="wAlYmIf97gD2NJPIejcVHWOlMqi" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4619a0028570d0d70076ae0d00e530d0e924596_2_690x449.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4619a0028570d0d70076ae0d00e530d0e924596_2_1035x673.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4619a0028570d0d70076ae0d00e530d0e924596_2_1380x898.jpeg 2x" data-dominant-color="B2AFB2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2245×1463 1020 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @jcfr (2019-05-22 14:53 UTC)

<p>2 posts were split to a new topic: <a href="/t/support-for-jkeyframe-based-animation/6885">Support for jkeyframe based animation</a></p>

---

## Post #7 by @the3dslicerdude (2020-04-25 06:07 UTC)

<p>I figure I’d bump this thread with some good looking volume renders. One from syngo-via, the other from Inviwo (I think). You will notice the shadows are not harsh, and over all they look a lot more realistic than those paraview examples. Another nice feature would be real time basic lighting for meshes also like when using segment editor.</p>
<p>                    <a href="https://csdl-images.computer.org/trans/tg/2011/12/figures/ttg20111221251.gif" target="_blank" class="onebox" rel="nofollow noopener">
            <img src="https://csdl-images.computer.org/trans/tg/2011/12/figures/ttg20111221251.gif" width="690" height="161">
          </a>

</p>
<p>                    <a href="https://www.auntminnie.com/user/images/content_images/sup_adv/2019_09_25_20_40_7782_cinematic_rendering_isct_slide1_20190925210137.jpg" target="_blank" class="onebox" rel="nofollow noopener">
            <img src="https://www.auntminnie.com/user/images/content_images/sup_adv/2019_09_25_20_40_7782_cinematic_rendering_isct_slide1_20190925210137.jpg" width="690" height="379">
          </a>

</p>

---

## Post #8 by @muratmaga (2020-04-25 06:30 UTC)

<p>You can actually use lighting with Segment Editor, if you install the <code>Sandbox</code> extension. Here is an example, actual color of the segment is green.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/380e9b2ce585dd457b152befaae3d53f63d6e5a2.png" data-download-href="/uploads/short-url/7ZU1Yzb29Jy79HeQeejdnz7Hemu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/380e9b2ce585dd457b152befaae3d53f63d6e5a2_2_690x473.png" alt="image" data-base62-sha1="7ZU1Yzb29Jy79HeQeejdnz7Hemu" width="690" height="473" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/380e9b2ce585dd457b152befaae3d53f63d6e5a2_2_690x473.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/380e9b2ce585dd457b152befaae3d53f63d6e5a2_2_1035x709.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/380e9b2ce585dd457b152befaae3d53f63d6e5a2.png 2x" data-dominant-color="8D9598"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1127×774 215 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
