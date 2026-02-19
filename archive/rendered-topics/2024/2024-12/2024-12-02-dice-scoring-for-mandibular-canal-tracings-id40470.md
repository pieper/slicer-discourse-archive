---
topic_id: 40470
title: "Dice Scoring For Mandibular Canal Tracings"
date: 2024-12-02
url: https://discourse.slicer.org/t/40470
---

# Dice scoring for mandibular canal tracings

**Topic ID**: 40470
**Date**: 2024-12-02
**URL**: https://discourse.slicer.org/t/dice-scoring-for-mandibular-canal-tracings/40470

---

## Post #1 by @Swarna_Yerebairapura (2024-12-02 04:26 UTC)

<p>I would like to perform Dice scoring for mandibular canal tracings created using the InVivo CBCT software. However, these tracings are only visible in the 2D panoramic reconstruction view and are not displayed in the MPR planes. Is there a way to conduct Dice scoring for these images? Please advise.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a8702af2f8fe9a51c68987b4b71e8d7e7e46a85.png" data-download-href="/uploads/short-url/3MFFIu6Tx5TSmUGXcbLvOFs5Fml.png?dl=1" title="{72FC0973-DCDA-4A56-8376-75417FF9CD12}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a8702af2f8fe9a51c68987b4b71e8d7e7e46a85_2_690x353.png" alt="{72FC0973-DCDA-4A56-8376-75417FF9CD12}" data-base62-sha1="3MFFIu6Tx5TSmUGXcbLvOFs5Fml" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a8702af2f8fe9a51c68987b4b71e8d7e7e46a85_2_690x353.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a8702af2f8fe9a51c68987b4b71e8d7e7e46a85_2_1035x529.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a8702af2f8fe9a51c68987b4b71e8d7e7e46a85_2_1380x706.png 2x" data-dominant-color="C4C2CD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{72FC0973-DCDA-4A56-8376-75417FF9CD12}</span><span class="informations">1912×980 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Swarna_Yerebairapura (2024-11-28 00:23 UTC)

<p>Could I upload JPEG pictures of 2d reconstruction panoramic view with traced mandibular canals into 3D Slicer to do the DICE scores and verify that the mandibular canals overlap?</p>

---

## Post #3 by @cpinter (2024-12-02 09:42 UTC)

<p>Your screenshot shows that you probably created the panoramic image from the CT and a curve. Can you please describe exactly what kind of data you have available?</p>

---

## Post #4 by @Swarna_Yerebairapura (2024-12-02 17:07 UTC)

<p>I have DICOM files, and when I upload them into 3D Slicer, the mandibular canal tracings appear only in the 2D panoramic reconstruction view. Similarly, in the InVivo CBCT software, the tracings are not visible in the MPR planes but are shown in the 2D panoramic reconstruction view and the 3D model.</p>

---

## Post #5 by @cpinter (2024-12-03 11:31 UTC)

<p>Thanks but this has not answered the question. Can you make a screenshot of the DICOM browser with the study selected before you load that data? Is there any other data than the DICOM? Can you also make a screenshot of the Data module after loading?</p>

---

## Post #6 by @Swarna_Yerebairapura (2024-12-03 21:51 UTC)

<p>Hi,<br>
I was unable to export as STL model. Here are the screenshots of the DICOM CASEDATA and data module after loading.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09c75de62b041c486b38781322aea551ebe0d034.png" data-download-href="/uploads/short-url/1ovrc38SuNX96uCKProXICbMyMs.png?dl=1" title="{C9491157-33A9-4ED3-9CDF-4C576CBC21BB}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09c75de62b041c486b38781322aea551ebe0d034_2_690x305.png" alt="{C9491157-33A9-4ED3-9CDF-4C576CBC21BB}" data-base62-sha1="1ovrc38SuNX96uCKProXICbMyMs" width="690" height="305" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09c75de62b041c486b38781322aea551ebe0d034_2_690x305.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09c75de62b041c486b38781322aea551ebe0d034_2_1035x457.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09c75de62b041c486b38781322aea551ebe0d034_2_1380x610.png 2x" data-dominant-color="E3E5EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{C9491157-33A9-4ED3-9CDF-4C576CBC21BB}</span><span class="informations">1862×825 65.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7b3cc5977c746b82ae1495c53aeacc4cff92b1c.png" data-download-href="/uploads/short-url/suEeq0uVm3ksIQgug89qXbS6i9m.png?dl=1" title="{330BA7FB-738A-4B1C-BE08-BFD13D0F43E3}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7b3cc5977c746b82ae1495c53aeacc4cff92b1c_2_690x362.png" alt="{330BA7FB-738A-4B1C-BE08-BFD13D0F43E3}" data-base62-sha1="suEeq0uVm3ksIQgug89qXbS6i9m" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7b3cc5977c746b82ae1495c53aeacc4cff92b1c_2_690x362.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7b3cc5977c746b82ae1495c53aeacc4cff92b1c_2_1035x543.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7b3cc5977c746b82ae1495c53aeacc4cff92b1c_2_1380x724.png 2x" data-dominant-color="BDBBC7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{330BA7FB-738A-4B1C-BE08-BFD13D0F43E3}</span><span class="informations">1920×1009 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Kindly advise,</p>

---

## Post #7 by @cpinter (2024-12-04 15:08 UTC)

<p>Unfortunately I cannot see anything relevant in the screenshots.</p>
<ol>
<li>Please show the DICOM Browser (not the import dialog but the browser with the patient/study/series)</li>
<li>The screen is so small that only two rows can be seen, so the interesting part is all cut off. Maybe hide the Data probe and the markups toolbar to make space</li>
</ol>

---
