# Volume/Volume Rendering

**Topic ID**: 7209
**Date**: 2019-06-17
**URL**: https://discourse.slicer.org/t/volume-volume-rendering/7209

---

## Post #1 by @steve01 (2019-06-17 21:28 UTC)

<p>This is my first post so please forgive me if this is out of place. I have worked through several tutorials now and found that I can mimic what was presented in the tutorials.   Unfortunately, this does not mean that I understand what is happening.  Why do I have to select the Active Volume in “Modules: Volumes” and then re-select it again in VR?<br>
Why does the sequence of selection make a difference? Why do I have to turn the “eye” off in Volume Rendering and on in Volumes?<br>
I have more or less the same questions for the other tutorials as well.</p>
<p>Thank you for your help.</p>

---

## Post #2 by @muratmaga (2019-06-18 00:35 UTC)

<p>This essentially boils down to the fact that volumes module and volume rendering module, and the slice or volume rendering window are not linked in anyways. If you want to have some control over this, I would suggest using the Data  browser module. Slice views and 3D volume rendering is still not linked (you have to right click and choose enable volume rendering), but still it is a single place to manipulate these settings.</p>

---

## Post #3 by @steve01 (2019-06-18 15:43 UTC)

<p>Thank you Mr. Muratmaga,</p>
<p>I am still a little puzzled. If the Volumes Module and the Volumes Rendering Module are not linked, why is it that after I change the color in the Volumes module and then switch to Volumes Rendering Module, the color of the  Volume selected is the same.  Further (still in Volumes Rendering Module), if I go to Advanced and set an ROI and then switch back to Volumes Module, the ROI shows up in the Active Volume.  I also noticed that if I set an ROI in the Volumes Rendering Module and then go to the Volumes Module I can not set the color in the ROI displayed.  It seems to me that there must be some connection, but as far as i can tell it is never mentioned in any of the tutorials.  Do you have any insight into this?</p>
<p>Thank you for you input.</p>

---

## Post #4 by @cpinter (2019-06-18 16:08 UTC)

<aside class="quote no-group" data-username="steve01" data-post="3" data-topic="7209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e68b1a/48.png" class="avatar"> steve01:</div>
<blockquote>
<p>If the Volumes Module and the Volumes Rendering Module are not linked</p>
</blockquote>
</aside>
<p>Everything is 3D Slicer are linked via the MRML scene containin the MRML nodes. In addition to the data nodes, there are display nodes driving visualization. What <a class="mention" href="/u/muratmaga">@muratmaga</a> meant is that for volumes, 2D (slice) and 3D (vol. rendering) are different mechanisms. They have different display node types etc. So if you show a volume in slice views, it won’t show up in 3D and vice versa.<br>
Color is managed differently for the same reason: the two visualization methods are very different. 2D slice visualization uses lookup tables, while volume rendering uses transfer functions. You can synchronize the two in the Volume rendering module by clicking the button “Synchronize with Volumes module” on the top of the Volume properties tab in the Advanced section.</p>
<p>The combobox in the volume rendering module selects which volume node the module panel will handle. So if you select one and turn on visualization for that, and select another, then the eye icon will reflect the visibility state of the new volume, so if you want to switch between visualizing two volumes in 3D, then you need to hide the first and show the second. This behavir may be confusing, and has historic reasons (we could only show one volume in the past but now there is an experimental multi-volume option, for which the UI has not been fully adapted). See discussion here</p><aside class="quote" data-post="13" data-topic="4018">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/volume-rendering-not-working/4018/13">Volume Rendering not working</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    <a class="mention" href="/u/lassoan">@lassoan</a>,  the problem I’m referring to is that the changed behavior of visibility management happens for all rendering modes, not just the multi-volume rendering.  Previously (e.g. 4.8.1), the volume selector acted like a radiobutton, where selecting a volume made it visible and the others invisible, which makes sense for renderers that don’t support multiple volume rendering.  Now, visibility is sticky with the volume, which makes sense for the multi-volume mode but not for the other modes.
  </blockquote>
</aside>


---

## Post #5 by @steve01 (2019-06-18 19:34 UTC)

<p>Thank you Mr. Pinter,</p>
<p>I think you touched on everything I was asking about.  I will have to go back to 3D Slicer and play around with it some more to make sure I understand it.  I will also revisit the tutorials I think they will make a little bit more sense now.</p>

---
