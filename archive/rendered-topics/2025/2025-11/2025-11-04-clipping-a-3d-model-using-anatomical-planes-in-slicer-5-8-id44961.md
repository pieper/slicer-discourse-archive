---
topic_id: 44961
title: "Clipping a 3D model using anatomical planes in Slicer 5.8"
date: 2025-11-04
url: https://discourse.slicer.org/t/44961
last_bumped: 2026-04-13T16:37:22.975Z
---

# Clipping a 3D model using anatomical planes in Slicer 5.8

**Topic ID**: 44961
**Date**: 2025-11-04
**URL**: https://discourse.slicer.org/t/clipping-a-3d-model-using-anatomical-planes-in-slicer-5-8/44961

---

## Post #1 by @Eva_Monclus_Lahoya (2025-11-04 15:05 UTC)

<p>In previous versions of 3D Slicer, the <strong>Models</strong> module allowed clipping a model using the anatomical slice planes (axial, coronal, and sagittal).</p>
<p>In version 5.8, I can’t find the same “Clip model by slice planes” option. What is the new workflow to achieve this behavior?</p>
<p>Specifically, I’d like to clip a surface model using the Red/Yellow/Green slice planes in the 3D view, just as before.</p>
<p>Thanks in advance for any guidance!</p>

---

## Post #2 by @cpinter (2025-11-04 15:15 UTC)

<p>You can still do clipping, please see this screenshot (I used the latest 5.9)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/556f1de3363958e241e1fb5fca7976360543c4e2.jpeg" data-download-href="/uploads/short-url/cbMEosf7nF09FcTfluSxLtaplS2.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/556f1de3363958e241e1fb5fca7976360543c4e2_2_690x385.jpeg" alt="image" data-base62-sha1="cbMEosf7nF09FcTfluSxLtaplS2" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/556f1de3363958e241e1fb5fca7976360543c4e2_2_690x385.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/556f1de3363958e241e1fb5fca7976360543c4e2_2_1035x577.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/556f1de3363958e241e1fb5fca7976360543c4e2_2_1380x770.jpeg 2x" data-dominant-color="797A7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1894×1059 334 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> <a class="mention" href="/u/lassoan">@lassoan</a> Shouldn’t we remove these controls? They don’t seem to do anything (UPDATE: They don’t until you configure it below, then the checkbox seems to be a duplicate of the one in the Clipping section. Even the “Configure…” button did not seem to do anything, I guess it opened the section below but it was not visible. It is at least confusing…)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5eb21b77f76eba8264629581aa55f08911120b7.png" data-download-href="/uploads/short-url/uwpt39E1siCs1D5KnV1r8mZM9Hp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5eb21b77f76eba8264629581aa55f08911120b7.png" alt="image" data-base62-sha1="uwpt39E1siCs1D5KnV1r8mZM9Hp" width="511" height="161"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">511×161 3.22 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Eva_Monclus_Lahoya (2025-11-07 00:13 UTC)

<p>Thanks a lot for your quick reply. However, I’m not sure how to include the “Red,” “Green,” or “Yellow” objects in the clipping list. I can only select from the different 3D meshes available in my scene. I’ve attached a screenshot to help clarify the issue.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f08706c111f64ded0db8a9de290b7dec317623dc.jpeg" data-download-href="/uploads/short-url/yjNSUfkUO0SBEWmzdyk2RucGF9q.jpeg?dl=1" title="Captura de pantalla 2025-11-07 010758" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f08706c111f64ded0db8a9de290b7dec317623dc_2_690x445.jpeg" alt="Captura de pantalla 2025-11-07 010758" data-base62-sha1="yjNSUfkUO0SBEWmzdyk2RucGF9q" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f08706c111f64ded0db8a9de290b7dec317623dc_2_690x445.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/0/f08706c111f64ded0db8a9de290b7dec317623dc_2_1035x667.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f08706c111f64ded0db8a9de290b7dec317623dc.jpeg 2x" data-dominant-color="6B6775"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2025-11-07 010758</span><span class="informations">1361×879 202 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can download the scene I’m using from the link below.</p>
<p><a href="https://www.slicer.org/w/img_auth.php/c/c4/Slicer4minute.zip" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/w/img_auth.php/c/c4/Slicer4minute.zip</a></p>
<p>Thanks in advance for any guidance!</p>

---

## Post #4 by @ffr (2026-04-12 03:07 UTC)

<p>Slicer 5.10 has the same issue. The clipping planes section is no longer available. Instead, there is a clipping section in the Models module, but it does not seem to function well. If I choose “ClipModelsParameter1,” the clipping works for the coronal plane, but that’s it. I cannot figure out how to clip using the axial or sagittal plane.</p>
<p>It also seems like there is no way to edit the “ClipModelsParameter1” clip node. If I delete it and create a new clip node, the clipping function stops working, and I have to restart Slicer to get that node back.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69b9527bfba8e6fc476c3d6a0955779f5dd213a5.png" data-download-href="/uploads/short-url/f5hbuDkt1yS3uX7uGaMNObfVXAV.png?dl=1" title="Screenshot 2026-04-11 195926" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69b9527bfba8e6fc476c3d6a0955779f5dd213a5.png" alt="Screenshot 2026-04-11 195926" data-base62-sha1="f5hbuDkt1yS3uX7uGaMNObfVXAV" width="518" height="303"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-04-11 195926</span><span class="informations">518×303 11.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @pieper (2026-04-12 18:29 UTC)

<p>You need to make sure you have a corresponding volume loaded for the slice planes to work. The color names correspond to the 2D slice views.  The new clipping interface is different and much more powerful now, but I agree it’s a little harder to figure out.</p>

---

## Post #6 by @ffr (2026-04-13 07:39 UTC)

<p>Thank you for your reply. May I ask if there are any tutorials on how to use it? I’ve attached a short video showing how I’ve been using it. So far, I’ve only been able to get coronal clipping to work, but I’m not sure how to edit the clip node. When I edit the clip node, it stops working even if I revert the changes.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c25acd34e5deebce00a047a14355e3709382a9f.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8eedf050543fc60ad9d670f04c6bbb96de4bd90.jpeg" data-video-base62-sha1="8A5mJNXcJE3iquaI5k4MGTUNWtp.mp4">
  </div><p></p>

---

## Post #7 by @pieper (2026-04-13 16:07 UTC)

<p>The menu should look like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14fe1ec786c667b389fdbcb044926ea4409e4284.png" data-download-href="/uploads/short-url/2ZHZY3FV1vWgrGPtRAUVEmtYMte.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14fe1ec786c667b389fdbcb044926ea4409e4284_2_690x280.png" alt="image" data-base62-sha1="2ZHZY3FV1vWgrGPtRAUVEmtYMte" width="690" height="280" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14fe1ec786c667b389fdbcb044926ea4409e4284_2_690x280.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14fe1ec786c667b389fdbcb044926ea4409e4284_2_1035x420.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14fe1ec786c667b389fdbcb044926ea4409e4284_2_1380x560.png 2x" data-dominant-color="ECF0F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1498×608 52 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is 5.10.0 for me.</p>
<p>The problem may be that you are using a very old scene file.  Try loading new data.</p>

---

## Post #8 by @ffr (2026-04-13 16:37 UTC)

<p>Thank you so much! You are right, the scene file causes the issue.</p>

---
