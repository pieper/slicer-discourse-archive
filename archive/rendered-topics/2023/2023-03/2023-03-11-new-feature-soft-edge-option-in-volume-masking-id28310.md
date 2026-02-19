---
topic_id: 28310
title: "New Feature Soft Edge Option In Volume Masking"
date: 2023-03-11
url: https://discourse.slicer.org/t/28310
---

# New feature: Soft edge option in volume masking

**Topic ID**: 28310
**Date**: 2023-03-11
**URL**: https://discourse.slicer.org/t/new-feature-soft-edge-option-in-volume-masking/28310

---

## Post #1 by @lassoan (2023-03-11 15:19 UTC)

<p>“Mask Volume” is a Segment Editor effect that can paint a a segment’s shape inside an image volume. It can be used for removing anything from the image (e.g., remove the patient table from a CT by blanking out the area) or it can be used for painting in structures (e.g., to simulate presence of objects or to fix problems during imaging). A limitation of the tool was that the edited images often had noticeable artifacts at the boundary of the painted region.</p>
<p>A new <strong>“Soft edge” option has been added to “Mask Volume” effect that removes the boundary artifacts of the in-painting</strong> by gradually blending the solid painted region with the original image. The effect has a single parameter, which specifies the size of the transition zone for this blending.</p>
<h3><a name="p-91827-example-1-painting-in-a-structure-1" class="anchor" href="#p-91827-example-1-painting-in-a-structure-1" aria-label="Heading link"></a>Example 1: Painting in a structure</h3>
<p>Without soft edge (notice the blocky edges and color artifacts due to very high gradient):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec79d108db16fd61467612082f076f37fd7c0bb2.jpeg" data-download-href="/uploads/short-url/xJXFLWoIMiJfCYMTqBpPF6rm1I6.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec79d108db16fd61467612082f076f37fd7c0bb2_2_497x500.jpeg" alt="image" data-base62-sha1="xJXFLWoIMiJfCYMTqBpPF6rm1I6" width="497" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec79d108db16fd61467612082f076f37fd7c0bb2_2_497x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec79d108db16fd61467612082f076f37fd7c0bb2_2_745x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec79d108db16fd61467612082f076f37fd7c0bb2_2_994x1000.jpeg 2x" data-dominant-color="867470"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1204×1209 238 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Using soft edge option with 0.5mm thickness:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e83e5666488dbd27b828966330f8bf4a3cd34044.jpeg" data-download-href="/uploads/short-url/x8wkuTyZI0KqPEtQxdJiFEub1Lm.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e83e5666488dbd27b828966330f8bf4a3cd34044_2_690x394.jpeg" alt="image" data-base62-sha1="x8wkuTyZI0KqPEtQxdJiFEub1Lm" width="690" height="394" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e83e5666488dbd27b828966330f8bf4a3cd34044_2_690x394.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e83e5666488dbd27b828966330f8bf4a3cd34044_2_1035x591.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e83e5666488dbd27b828966330f8bf4a3cd34044_2_1380x788.jpeg 2x" data-dominant-color="605958"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2382×1362 467 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-91827-example-2-remove-a-structure-from-the-image-2" class="anchor" href="#p-91827-example-2-remove-a-structure-from-the-image-2" aria-label="Heading link"></a>Example 2: Remove a structure from the image</h3>
<p>Without soft edge (notice the artifacts where the table touched the patient skin):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/786a0d693f56a0db70effcb2dcde4d47623679f7.jpeg" data-download-href="/uploads/short-url/hbevMBMS8jqSMf3jDxn1ydfxwKb.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/786a0d693f56a0db70effcb2dcde4d47623679f7_2_690x308.jpeg" alt="image" data-base62-sha1="hbevMBMS8jqSMf3jDxn1ydfxwKb" width="690" height="308" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/786a0d693f56a0db70effcb2dcde4d47623679f7_2_690x308.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/786a0d693f56a0db70effcb2dcde4d47623679f7_2_1035x462.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/786a0d693f56a0db70effcb2dcde4d47623679f7.jpeg 2x" data-dominant-color="705741"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1265×565 58.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Soft edge (less edge artifacts):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcdc29242a15a79121d00aab7d2dd4a8108c70d7.jpeg" data-download-href="/uploads/short-url/A4U0UubamLSdDXQQNOH2xWzTCnR.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcdc29242a15a79121d00aab7d2dd4a8108c70d7_2_690x308.jpeg" alt="image" data-base62-sha1="A4U0UubamLSdDXQQNOH2xWzTCnR" width="690" height="308" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcdc29242a15a79121d00aab7d2dd4a8108c70d7_2_690x308.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcdc29242a15a79121d00aab7d2dd4a8108c70d7_2_1035x462.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcdc29242a15a79121d00aab7d2dd4a8108c70d7.jpeg 2x" data-dominant-color="745943"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1267×567 53.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Soft edge (very wide edge, even less edge artifacts but the transition zone somewhat eats into the image):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/4229fb771aa838c2a2a961edf2604224f6c3aefd.jpeg" data-download-href="/uploads/short-url/9rjsv1igSTpbenMYvwvdJpK8BxH.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/4229fb771aa838c2a2a961edf2604224f6c3aefd_2_690x309.jpeg" alt="image" data-base62-sha1="9rjsv1igSTpbenMYvwvdJpK8BxH" width="690" height="309" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/4229fb771aa838c2a2a961edf2604224f6c3aefd_2_690x309.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/4229fb771aa838c2a2a961edf2604224f6c3aefd_2_1035x463.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/4229fb771aa838c2a2a961edf2604224f6c3aefd.jpeg 2x" data-dominant-color="755A44"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1267×569 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The feature is available in recent Slicer Preview Releases (Slicer-5.3.0-2023-03-03 and later). Development was funded by SlicerHeart project.</p>

---

## Post #2 by @lassoan (2023-03-13 14:12 UTC)

<p>5 posts were split to a new topic: <a href="/t/volume-masking-soft-edge-option-requires-non-empty-output-volume/28349">Volume masking “soft edge” option requires non-empty output volume</a></p>

---

## Post #3 by @Spiros_Karkavitsas (2023-03-14 08:30 UTC)

<p>Hello Prof.Lasso</p>
<p>That is a great and very useful addition in Slicer. May I ask in how much time can this addition be added in a stable version instead of a preview?</p>
<p>Best<br>
Spiros</p>

---

## Post #4 by @lassoan (2023-03-14 11:38 UTC)

<p>We have released a stable version very recently and the next one is scheduled in 3 months. Until then you can overwrite the <code>...\lib\Slicer-5.3\qt-scripted-modules\SegmentEditorEffects\SegmentEditorMaskVolumeEffect.py</code> file in the latest stable release by the one that comes from the latest preview release.</p>

---

## Post #5 by @Spiros_Karkavitsas (2023-03-16 08:51 UTC)

<p>Hello again and thank you a lot for your answer <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>It might sound obvious and maybe I understood something wrong here but:<br>
The last stable version of Slicer I can see in the website is 5.2.2 ando not 5.3 where this module is available.</p>
<p>Thank you again for your help,<br>
Spiros.</p>

---

## Post #6 by @lassoan (2023-03-16 13:28 UTC)

<p>The new feature is available in Slicer-5.3. You can copy the feature from Slicer-5.3 to Slicer-5.2 by copying the file I mentioned above.</p>

---
