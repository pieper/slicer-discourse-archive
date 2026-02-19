---
topic_id: 16160
title: "Dose Accumulation From Rt Slicer To Eclipce Tps"
date: 2021-02-23
url: https://discourse.slicer.org/t/16160
---

# Dose accumulation from RT Slicer to Eclipce TPS

**Topic ID**: 16160
**Date**: 2021-02-23
**URL**: https://discourse.slicer.org/t/dose-accumulation-from-rt-slicer-to-eclipce-tps/16160

---

## Post #1 by @kuba_grepl (2021-02-23 13:32 UTC)

<p>Hello Slicer community,<br>
thank you for awesome software and fast support.</p>
<p>My problem:</p>
<ol>
<li>I exported several RT plans from one patient with doses, structure sets and CTs from Eclipse Varian TPS to 3DSlicer</li>
<li>I accumulated these doses using RT Slicer and deformable registration tool Elastix successfully<br>
(thanks for the tutorial: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DoseAccumulation" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Modules/DoseAccumulation - Slicer Wiki</a>)</li>
<li>But I am not able to export the accumulated dose back to the Eclipse Varian TPS.<br>
Eclipse error message: data cannot be imported.</li>
</ol>
<p>Does anyone know how to export the RT dose from 3DSlicer to Eclipse TPS correctly??? Must be attached to the plan or CT?<br>
Thank you in advance.<br>
Jakub.</p>

---

## Post #2 by @cpinter (2021-02-23 13:46 UTC)

<p>You need to have a study in the Data module, where you have the reference CT and the accumulated dose. Make sure the dose is actually RT Dose type (i.e. it has a colored volume icon - same as of the CT but with colors in the cube). Then right-click the study and choose Export to DICOM, in which window you need to make sure RT type is selected on the bottom left.</p>
<p>If something does not work please post a screenshot of your Data module at the moment of the export and the export window as well.</p>

---

## Post #3 by @kuba_grepl (2021-02-26 10:25 UTC)

<p>Thank you for your answer Csaba Pinter!!!<br>
Here you can see screenshots from 3DSlicer, a folder with exported files and error message from Eclipse TPS.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d7546c8a486af1314363fb2af3e3802af7df201.jpeg" data-download-href="/uploads/short-url/6u8KuEHxpSwS2MrCF2Xdvx2wMoN.jpeg?dl=1" title="01 data module" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2d7546c8a486af1314363fb2af3e3802af7df201_2_690x388.jpeg" alt="01 data module" data-base62-sha1="6u8KuEHxpSwS2MrCF2Xdvx2wMoN" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2d7546c8a486af1314363fb2af3e3802af7df201_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2d7546c8a486af1314363fb2af3e3802af7df201_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2d7546c8a486af1314363fb2af3e3802af7df201_2_1380x776.jpeg 2x" data-dominant-color="7C7F73"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">01 data module</span><span class="informations">1920×1080 448 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82e65ab9760c31476cc0f51e8efa23cc5eb13291.png" data-download-href="/uploads/short-url/iFZBozOERqNyKCCwbyQQTKR1Pix.png?dl=1" title="02 export" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/82e65ab9760c31476cc0f51e8efa23cc5eb13291_2_690x388.png" alt="02 export" data-base62-sha1="iFZBozOERqNyKCCwbyQQTKR1Pix" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/82e65ab9760c31476cc0f51e8efa23cc5eb13291_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/82e65ab9760c31476cc0f51e8efa23cc5eb13291_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/82e65ab9760c31476cc0f51e8efa23cc5eb13291_2_1380x776.png 2x" data-dominant-color="E0E4E1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">02 export</span><span class="informations">1920×1080 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58bdad3d14dfa68b02241fa043812f6032a181a8.png" data-download-href="/uploads/short-url/cF2oFsMtA5Q0rF8dvEYkaqFO7OM.png?dl=1" title="03 export result" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58bdad3d14dfa68b02241fa043812f6032a181a8_2_690x388.png" alt="03 export result" data-base62-sha1="cF2oFsMtA5Q0rF8dvEYkaqFO7OM" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58bdad3d14dfa68b02241fa043812f6032a181a8_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58bdad3d14dfa68b02241fa043812f6032a181a8_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/58bdad3d14dfa68b02241fa043812f6032a181a8_2_1380x776.png 2x" data-dominant-color="F1F2F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">03 export result</span><span class="informations">1920×1080 261 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9e389b1c356379f36bf7418421fe93efb6461ac.png" data-download-href="/uploads/short-url/zECo2C9ZDcQGZ2bcvjvZl9vEGMk.png?dl=1" title="04 import TPS" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9e389b1c356379f36bf7418421fe93efb6461ac_2_690x388.png" alt="04 import TPS" data-base62-sha1="zECo2C9ZDcQGZ2bcvjvZl9vEGMk" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9e389b1c356379f36bf7418421fe93efb6461ac_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9e389b1c356379f36bf7418421fe93efb6461ac_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9e389b1c356379f36bf7418421fe93efb6461ac_2_1380x776.png 2x" data-dominant-color="7F8488"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">04 import TPS</span><span class="informations">1920×1080 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e7dd9873fa821df55dc6a775fea192acc371925.png" data-download-href="/uploads/short-url/4lJXgsxJdEvQdEnO0JeYsEup0kR.png?dl=1" title="05 import TPS 3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e7dd9873fa821df55dc6a775fea192acc371925_2_690x388.png" alt="05 import TPS 3" data-base62-sha1="4lJXgsxJdEvQdEnO0JeYsEup0kR" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e7dd9873fa821df55dc6a775fea192acc371925_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e7dd9873fa821df55dc6a775fea192acc371925_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1e7dd9873fa821df55dc6a775fea192acc371925_2_1380x776.png 2x" data-dominant-color="7F8488"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">05 import TPS 3</span><span class="informations">1920×1080 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/294ab5d4c59fe0a21e2bb4e3da26c6898d6ba6c7.png" data-download-href="/uploads/short-url/5ThDP4YHxqudz2ocnobzVbQg4DB.png?dl=1" title="06 import TPS 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/294ab5d4c59fe0a21e2bb4e3da26c6898d6ba6c7_2_690x388.png" alt="06 import TPS 2" data-base62-sha1="5ThDP4YHxqudz2ocnobzVbQg4DB" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/294ab5d4c59fe0a21e2bb4e3da26c6898d6ba6c7_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/294ab5d4c59fe0a21e2bb4e3da26c6898d6ba6c7_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/294ab5d4c59fe0a21e2bb4e3da26c6898d6ba6c7_2_1380x776.png 2x" data-dominant-color="7F8488"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">06 import TPS 2</span><span class="informations">1920×1080 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Do you have any idea???<br>
Thank you for your time. Jakub…</p>

---

## Post #4 by @cpinter (2021-02-26 11:57 UTC)

<p>You’re using a Slicer that is more than two years old. Please use either the latest stable or a recent preview version and try again. Thanks!</p>

---

## Post #5 by @kuba_grepl (2021-02-26 12:02 UTC)

<p>Ok. I will try it and I will let you know.</p>

---

## Post #6 by @kuba_grepl (2021-03-01 08:42 UTC)

<p>Hello cpinter. I tried the latest stable version, but the problem remains the same. Do you have any other idea?</p>

---

## Post #7 by @cpinter (2021-03-02 09:05 UTC)

<p>I’m not familiar with how Eclipse expects and treats the data. The only thing that occurs me based on the log that can be seen in your screenshots is to try to export it under a new patient, as the error seems related to the imported patient.</p>
<p>Any ideas <a class="mention" href="/u/gregsharp.geo">@gregsharp.geo</a> ?</p>

---

## Post #8 by @gcsharp (2021-03-02 21:39 UTC)

<p>Yes, I think so.  I found a bug in plastimatch where certain required, but zero-length, DICOM attributes were not being written.  This is now patched in plastimatch HEAD.  Still need to update hash in SlicerRT and test.</p>

---

## Post #9 by @cpinter (2021-03-04 10:46 UTC)

<p>This is great <a class="mention" href="/u/gcsharp">@gcsharp</a>, thanks for the quick fix! (not sure how I didn’t find this user of yours before, sorry)</p>
<p>I’ll update Plastimatch in SlicerRT and give an update here when everything works so that <a class="mention" href="/u/kuba_grepl">@kuba_grepl</a> can try it.</p>

---

## Post #10 by @kuba_grepl (2021-03-05 06:23 UTC)

<p>Hello Csaba Pinter and Greg Sharp. Thank you for your cooperation. I believe that Fix a bug and SlicerRT update would be very useful for more Slicer3D users.<br>
I am surprised that no one before me has a similar problem…as the Eclipse software is very widespread.</p>

---

## Post #11 by @cpinter (2021-03-05 10:34 UTC)

<p>I made the necessary changes, see <a href="https://github.com/SlicerRt/SlicerRT/commit/3026110f0a85296c1e28b510bdc1d577dc4a752f">here</a>.</p>
<p>Please try again with tomorrow’s preview release.</p>

---

## Post #12 by @kuba_grepl (2021-03-05 10:51 UTC)

<p>Ok, I will let you know on Monday. Nice weekend.</p>

---

## Post #13 by @kuba_grepl (2021-03-10 16:56 UTC)

<p>Unfortunately I am not able to install RTSlicer 3026110 extension module into 3DSlicer 4.13.0 2021 03 05 r29479 / 121ffbd. I tried it manully. In extension manager it seems that it is installed, but I cannot find it in modul finder. Sorry.</p>

---

## Post #14 by @cpinter (2021-03-10 17:05 UTC)

<p>Today’s dashboard shows that SlicerRT was built successfully on all platforms. Can you please try with the latest preview version? Also give the installer a bit more time, unfortunately sometimes not all operations have finished by the time the Restart button appears (although not sure if it is true also when you install only one extension).</p>

---

## Post #15 by @kuba_grepl (2021-03-11 10:36 UTC)

<p>I tried the latest preview version today. RTSlicer worked, but unfortunately, I received the same error message from Eclipse TPS.</p>

---

## Post #16 by @cpinter (2021-03-11 11:01 UTC)

<p>Is it the exact same error?</p>
<p>Also have you tried my idea above about the different patients?</p>

---

## Post #17 by @kuba_grepl (2021-03-11 13:10 UTC)

<p>Yes, it seems like the same error. Value cannot be null. Parameter name: key.<br>
I tried it with a different patient.</p>

---
