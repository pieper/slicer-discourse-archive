# Tutorials for SlicerRT, DICOM import, Plastimatch

**Topic ID**: 11917
**Date**: 2020-06-08
**URL**: https://discourse.slicer.org/t/tutorials-for-slicerrt-dicom-import-plastimatch/11917

---

## Post #1 by @annigilus (2020-06-08 04:21 UTC)

<p>Greetings, everyone!<br>
Can’t find tutorials from this topic, it said “no such host”. <a href="https://www.slicer.org/wiki/Documentation/4.2/Modules/PlmDICOMRTImport" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.2/Modules/PlmDICOMRTImport</a><br>
Please, show where I can find these tutorials or send it ti me <a href="mailto:annigilus@mail.ru">annigilus@mail.ru</a></p>

---

## Post #2 by @cpinter (2020-06-08 08:46 UTC)

<p>This module does not exist any more. As you can see, the page you refer to is for Slicer 4.2, which is about 8 years old. Please use the latest preview version (we are very close to 5.0 now so it is better than 4.10.2), install SlicerRT, and load the DICOM-RT files through the DICOM browser.</p>

---

## Post #3 by @annigilus (2020-06-08 14:55 UTC)

<p>Thank you so much!</p>
<p>Could you tell me, please, how can I convert RTplans from XiO and Monaco, for example, in Slicer 3D to nrrd or DICOM-RT so I can compute it in SlicerRT module?</p>
<p>Thank you for your work! Slicer crew is the best!</p>

---

## Post #4 by @cpinter (2020-06-08 15:34 UTC)

<p>Thanks for the nice words, we need those sometimes <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>SlicerRT mostly manages only standard, non-proprietary data, such as DICOM-RT. If you can export your plan to DICOM-RT from the treatment planning system, then you can also load it in Slicer (check out the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#Data_import_and_loading">DICOM importing/loading section</a> in the wiki).</p>
<p>Please note that RT plan support is not complete. It can now import MLCs (thanks to a recent contributor <a class="mention" href="/u/mik">@Mik</a>), but it does not support some state of the art techniques such as arcs. We are preparing a grant (due tomorrow) in course of which we plan to improve this feature a lot, but it won’t be done in the near future.</p>

---

## Post #5 by @annigilus (2020-06-09 10:20 UTC)

<p>Thank you a lot!<br>
Excuse me, but I have one more question.<br>
Follow to tutorioal of OrthovoltageDoseEngine I can’t edit my beams, although I instanned EGSnrc on my PC. It shoul look like this<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dca55cea7efec50541d77f92ca4a7297a62050f2.png" alt="image.png" data-base62-sha1="vtVkAaXUEYNRmWLnW8NlqR1hrrk" width="567" height="432">.<br>
But it look like this<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/922a9846561a7a39d4b0cef1901064989382821a.png" alt="image.png" data-base62-sha1="kR2Y7qlg46r7ZCyHCbJSSJPA8NI" width="496" height="484"><br>
I don’t have tabs «Generate ctcreate phantom» and «Orthovoltage dose» and onle «Mock dose» that almost empty.<br>
Maybe you could help me what’s wrong with that? Maybe I shold show a folder way for EGSnrc, but where?<br>
Thank you already!</p>

---

## Post #6 by @cpinter (2020-06-09 10:34 UTC)

<p>I believe you skipped the step in the tutorial in which you need to change the Dose engine to Orthovoltage instead of the default selection Mock. Go back to the External Beam Planning module and select that.</p>
<p>Also in the future, please create a new topic if you have a question that does not fit in the title of your original question.</p>

---

## Post #7 by @annigilus (2020-06-09 16:09 UTC)

<p>Thank you a lot!</p>
<p>Created a new topic about my problem (Mock, Orthovoltage, SlicerRT,…)</p>

---
