# How to Fuse image SPECT and CTA

**Topic ID**: 16814
**Date**: 2021-03-29
**URL**: https://discourse.slicer.org/t/how-to-fuse-image-spect-and-cta/16814

---

## Post #1 by @akmal871026 (2021-03-29 03:06 UTC)

<p>Operating system: windows<br>
Slicer version: 4.13<br>
Expected behavior:<br>
Actual behavior: anyone can help me with how to fuse image SPECT with CT Abdomen?</p>
<p>That is because my spect image inn 4D(one image), while my CTA has (3D images) have 673 frames.</p>
<p>how could I do?</p>

---

## Post #2 by @pieper (2021-03-29 18:21 UTC)

<p>Can you clarify what you mean by “4D (one image)” ?   I’m not too familiar with SPECT but I thought it would be one volume.</p>

---

## Post #3 by @akmal871026 (2021-03-29 18:31 UTC)

<p>Yes correct, one volume</p>

---

## Post #4 by @pieper (2021-03-29 19:11 UTC)

<p>In that case the regular overlay methods should work.  The documentation is here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view</a></p>
<p>Put the CT in the background and the SPECT in the foreground and then use the slider to adjust the opacity of the overlay.  Someone probably has a video example somewhere but I’m not sure where.</p>

---

## Post #5 by @Kazim_Radfar (2023-12-30 12:29 UTC)

<p>Hell, brother, hope you are doing well.<br>
Did you get your answer? Or did you find the software to fuse SPECT and CT images? I have the same problem. My CT images are around 160 and SPECT image are in one volume. If you solved your problem, Please help me.</p>
<p>Thanks in advance</p>

---

## Post #6 by @akmal871026 (2023-12-30 12:49 UTC)

<p>Yah… I have settle for fusing SPECT and CT. you can use registration module. There is many method you can use.</p>

---

## Post #7 by @Kazim_Radfar (2023-12-30 12:52 UTC)

<p>Thanks for your reply.</p>
<p>Kazim Radfar<br>
Medical Physicist in KUMS<br>
Add: Jamal mina, Karte Sakhi, Kabul, Afghanistan.<br>
Tel: +93-776-200-263</p>

---

## Post #8 by @Kazim_Radfar (2023-12-30 12:56 UTC)

<p>Could describe a bit more, please. <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @akmal871026 (2023-12-30 13:04 UTC)

<p>I think better I remote your computer instead explain by email.</p>

---

## Post #10 by @Kazim_Radfar (2023-12-30 13:07 UTC)

<p>this is my and desk address: 1 791 924 124</p>

---

## Post #11 by @akmal871026 (2023-12-30 13:27 UTC)

<p>Okay I will let you know when I want to remote. Give me some time</p>

---

## Post #12 by @Kazim_Radfar (2023-12-30 13:29 UTC)

<p>Thanks brother <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>Kazim Radfar<br>
Medical Physicist in KUMS<br>
Add: Jamal mina, Karte Sakhi, Kabul, Afghanistan.<br>
Tel: +93-776-200-263</p>

---

## Post #13 by @akmal871026 (2024-01-01 07:42 UTC)

<p>I tried remote, but failed</p>

---

## Post #14 by @Kazim_Radfar (2024-01-01 07:43 UTC)

<p>Hello brother. Sorry my laptop was off. Now it’s on.</p>
<p>Kazim Radfar<br>
Medical Physicist in KUMS<br>
Add: Jamal mina, Karte Sakhi, Kabul, Afghanistan.<br>
Tel: +93-776-200-263</p>

---

## Post #15 by @Kazim_Radfar (2024-01-01 07:59 UTC)

<p>Can you try now?</p>
<p>Kazim Radfar<br>
Medical Physicist in KUMS<br>
Add: Jamal mina, Karte Sakhi, Kabul, Afghanistan.<br>
Tel: +93-776-200-263</p>

---

## Post #16 by @Kazim_Radfar (2024-01-01 09:29 UTC)

<p>Brother, I found your video on YouTube. It was very good. But in my case, the orientation of SPECT and CT Images are not the same. For example, when I import the images, the axial view of CT and SPECT are not the same.</p>
<p>Kazim Radfar<br>
Medical Physicist in KUMS<br>
Add: Jamal mina, Karte Sakhi, Kabul, Afghanistan.<br>
Tel: +93-776-200-263</p>

---

## Post #17 by @akmal871026 (2024-01-01 12:15 UTC)

<p>Actually, I tried to remote you computer. But lagging.</p>
<p>Maybe can try again this evening.</p>

---

## Post #18 by @Kazim_Radfar (2024-01-01 13:11 UTC)

<p>It’s look like this <img src="https://emoji.discourse-cdn.com/twitter/point_down.png?v=12" title=":point_down:" class="emoji" alt=":point_down:" loading="lazy" width="20" height="20"></p>
<p>Kazim Radfar<br>
Medical Physicist in KUMS<br>
Add: Jamal mina, Karte Sakhi, Kabul, Afghanistan.<br>
Tel: +93-776-200-263</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/668eda478e5c252ab549cad6330cf4c2b569a3f7.jpeg" data-download-href="/uploads/short-url/eDgLgBZ8A3MiMiy0H3KDBUi7MHB.jpeg?dl=1" title="IMG_20240101_163948_152.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/668eda478e5c252ab549cad6330cf4c2b569a3f7_2_690x321.jpeg" alt="IMG_20240101_163948_152.jpg" data-base62-sha1="eDgLgBZ8A3MiMiy0H3KDBUi7MHB" width="690" height="321" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/668eda478e5c252ab549cad6330cf4c2b569a3f7_2_690x321.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/668eda478e5c252ab549cad6330cf4c2b569a3f7_2_1035x481.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/668eda478e5c252ab549cad6330cf4c2b569a3f7.jpeg 2x" data-dominant-color="595857"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20240101_163948_152.jpg</span><span class="informations">1280×597 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #19 by @akmal871026 (2024-01-01 13:32 UTC)

<p>Your SPECT images is projection, not reconstructed.</p>
<p>You need to have SPECT reconstruction, not projection.</p>

---

## Post #20 by @Kazim_Radfar (2024-01-01 13:45 UTC)

<p>Thanks brother.</p>
<p>Kazim Radfar<br>
Medical Physicist in KUMS<br>
Add: Jamal mina, Karte Sakhi, Kabul, Afghanistan.<br>
Tel: +93-776-200-263</p>

---
