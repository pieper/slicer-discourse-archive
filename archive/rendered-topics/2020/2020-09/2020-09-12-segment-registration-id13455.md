# Segment registration

**Topic ID**: 13455
**Date**: 2020-09-12
**URL**: https://discourse.slicer.org/t/segment-registration/13455

---

## Post #1 by @Pratik (2020-09-12 03:12 UTC)

<p>I am trying to compare the coordinates of a geometry before and after deformation in order to compute displacements in x,y and z direction. I am using segment registration feature from 3D slicer to register the two segments. However, when I press perform registration, it just loads but does not do anything. Just wanted to know if I am doing it wrong or if this usually takes very long time. I have attached a pic of my segments and the setup used.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a145e2f670e35663255ec8c8b39e9c6c24e1020.png" data-download-href="/uploads/short-url/jHvwNmgKs7UraqLfTJtKATTj8oU.png?dl=1" title="segments" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a145e2f670e35663255ec8c8b39e9c6c24e1020_2_612x500.png" alt="segments" data-base62-sha1="jHvwNmgKs7UraqLfTJtKATTj8oU" width="612" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a145e2f670e35663255ec8c8b39e9c6c24e1020_2_612x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a145e2f670e35663255ec8c8b39e9c6c24e1020_2_918x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a145e2f670e35663255ec8c8b39e9c6c24e1020.png 2x" data-dominant-color="9399C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segments</span><span class="informations">1007×822 34.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-09-12 04:29 UTC)

<p>Could you try if registration works if you select a fixed and moving image? You can probably use a labelmap volume exported from the segmentation (by right-clicking on the segmentation in Data module).</p>

---

## Post #3 by @Pratik (2020-09-12 04:52 UTC)

<p>Hi Andras,</p>
<p>Thank you for your prompt reply. I created the segments from stl files. When you refer to labelmap volume from the segmentation, do you mean to say exporting as binary labelmap? (screenshot attached)<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b8eb6bf567d2936177f282dc9bb34857320cfea.jpeg" data-download-href="/uploads/short-url/jUA89bjGItdnC9xHX2Lb3BwDsNQ.jpeg?dl=1" title="export" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b8eb6bf567d2936177f282dc9bb34857320cfea_2_690x332.jpeg" alt="export" data-base62-sha1="jUA89bjGItdnC9xHX2Lb3BwDsNQ" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b8eb6bf567d2936177f282dc9bb34857320cfea_2_690x332.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b8eb6bf567d2936177f282dc9bb34857320cfea_2_1035x498.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b8eb6bf567d2936177f282dc9bb34857320cfea_2_1380x664.jpeg 2x" data-dominant-color="B5B9DC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">export</span><span class="informations">2583×1245 271 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f60f310c6ca516af3225cf6aca7f2e47bce194db.png" data-download-href="/uploads/short-url/z6K0lqxAYiV67LKiqnNTgHW3LPt.png?dl=1" title="export1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f60f310c6ca516af3225cf6aca7f2e47bce194db_2_690x290.png" alt="export1" data-base62-sha1="z6K0lqxAYiV67LKiqnNTgHW3LPt" width="690" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f60f310c6ca516af3225cf6aca7f2e47bce194db_2_690x290.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f60f310c6ca516af3225cf6aca7f2e47bce194db_2_1035x435.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f60f310c6ca516af3225cf6aca7f2e47bce194db_2_1380x580.png 2x" data-dominant-color="E1E7EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">export1</span><span class="informations">1390×586 30.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I do this and retry registration, i still cannot select anything from the image i.e the volume dropdown.</p>
<p>Regards<br>
Pratik</p>

---

## Post #4 by @lassoan (2020-09-12 04:59 UTC)

<p>Probably it expects a scalar volume and not labelmap volume. Go to Volumes module’s Information section to convert the labelmap volumes to scalar volumes.</p>

---

## Post #5 by @Pratik (2020-09-12 05:55 UTC)

<p>Hi Andras,</p>
<p>My overall aim is to determine how the coordinates of test3 changes as it moves to the configuration of test4 (see pic below)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/73fd7348174519784bb9891e2708180b9c255bd7.jpeg" data-download-href="/uploads/short-url/gy5Vhuunlmg4rRhTi3ECxb6xsd9.jpeg?dl=1" title="test.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/73fd7348174519784bb9891e2708180b9c255bd7_2_559x500.jpeg" alt="test.PNG" data-base62-sha1="gy5Vhuunlmg4rRhTi3ECxb6xsd9" width="559" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/73fd7348174519784bb9891e2708180b9c255bd7_2_559x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/73fd7348174519784bb9891e2708180b9c255bd7_2_838x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/73fd7348174519784bb9891e2708180b9c255bd7_2_1118x1000.jpeg 2x" data-dominant-color="9199C1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">test.PNG</span><span class="informations">1279×1143 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The segment registration does seem to complete when i use the scalar volume as input. However, i still do not understand how I can use the end result to fulfil my aim and if indeed the registration has been done correctly (attached the results i can view after registration) .<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b5ef508bcbd1b9377f6ef8697dc5d54d602c4da.png" data-download-href="/uploads/short-url/mats4cC81lqcHBiDPakZJyAbcCe.png?dl=1" title="postregistration" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b5ef508bcbd1b9377f6ef8697dc5d54d602c4da_2_690x361.png" alt="postregistration" data-base62-sha1="mats4cC81lqcHBiDPakZJyAbcCe" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b5ef508bcbd1b9377f6ef8697dc5d54d602c4da_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b5ef508bcbd1b9377f6ef8697dc5d54d602c4da_2_1035x541.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9b5ef508bcbd1b9377f6ef8697dc5d54d602c4da_2_1380x722.png 2x" data-dominant-color="C0C1DE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">postregistration</span><span class="informations">3697×1938 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>From my understanding, in the surface registration module, the initial configuration actually transforms to the desired configuration and this way I could export both the initial and transformed coordinates and find the change in X,Y ,Z. Since this module only works for rigid motions, I am using the segment registration instead but I cant see the transformation happening in this module.</p>

---
