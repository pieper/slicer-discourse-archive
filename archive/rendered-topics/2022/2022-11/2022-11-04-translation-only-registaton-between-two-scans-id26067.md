# Translation only registaton between two scans

**Topic ID**: 26067
**Date**: 2022-11-04
**URL**: https://discourse.slicer.org/t/translation-only-registaton-between-two-scans/26067

---

## Post #1 by @suranga (2022-11-04 12:50 UTC)

<p>I have a 3D-CT and 3D-CBCT scan of the same patient. I just used rigid transformation in SlicerANTs to register 3D-CT (moving image) on 3D-CBCT (fixed image). However, I want to avoid rotation in rigid transforamtion, so I can only allow translation for registration. Is it possible to do so in 3D-slicer?</p>
<p>Is it possible with SlicerANTs or Elastix or BRAINS in 3D slicer ? If so can anyone help me on resolving this issue.</p>
<p>The interpolation also caused grey pixels to appear within the bounds of the registered CT volume, as shown in the attached image. Is it possible to avoid those artefacts?</p>
<p><em>(image removed due to privacy concerns)</em></p>

---

## Post #2 by @ebrahim (2022-11-04 13:56 UTC)

<p>In SlicerANTs you can, instead of choosing one of the “Stages (Presets)”, set up a translation stage only yourself:</p>
<p><em>(image removed due to privacy concerns)</em></p>
<p>Also there is a Settings section below that lets you choose the output interpolation mode; this might help with the gray pixels you are talking about</p>

---

## Post #4 by @ebrahim (2022-11-04 16:44 UTC)

<blockquote>
<p>To avoid the gray values, I just right click on the moving image and apply tranform file to it to deform so that these gray values no longer exists. However, I’m not sure whether that step is correct or not ? Here I attached a screenshot of that.</p>
</blockquote>
<p>Oh, now I see what you meant by gray pixels— at the image boundary. I retract my comment about setting the interpolation mode. IDK where those gray values coming from.</p>
<blockquote>
<p>However, I’m not sure whether that step is correct or not ?</p>
</blockquote>
<p>I guess you are talking about “Harden Transfrom”? That will apply the transform to the volume node “MCR” baking the transform into the volume node. Nothing wrong with that but IDK where the gray pixels are coming from.</p>

---

## Post #5 by @pieper (2022-11-04 17:25 UTC)

<p>The gray pixels are probably the fill value of zero (in a CT zero is in the middle of the expected intensity range).  I believe this is called the Default Value in the Resample Image (BRAINS) module and you could set it to -1024 or similar.</p>

---

## Post #6 by @mikebind (2022-11-04 19:22 UTC)

<p>Yes, it’s fine to apply the transform to the image volume by right-clicking on it as you do, and it will always avoid the creation of the filled gray pixels because you are moving the existing image volume in space rather than resampling it into the image grid defined by the fixed image you are registering to.</p>
<p>It looks like the SlicerAnts graphical interface doesn’t allow you to set what voxel value areas outside your transformed original image should be set to, and the default value is probably zero, as <a class="mention" href="/u/pieper">@pieper</a> suggests, which shows up as gray because it’s a middling value for CT images.</p>

---
