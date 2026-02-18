# Save scene with written name

**Topic ID**: 4469
**Date**: 2018-10-19
**URL**: https://discourse.slicer.org/t/save-scene-with-written-name/4469

---

## Post #1 by @Ash_Alarfaj (2018-10-19 16:40 UTC)

<p>Problem report for Slicer 4.9.0-2018-10-16 macosx-amd64: [please describe expected and actual behavior]</p>
<p>expected: usually in version 4.8 I can save my work in mrb format and I can change the file name.<br>
actual : I can not change the name when  I need to save my work in mrb formate.</p>
<p>actually, I can not see any diffrences or improvment in the new 4.9 v over 4.8. and I feel the new one is a bit slower. however I’ve followed 3D slicer team advice of using 4.9 instead of 4.8.</p>
<p>sorry for being annoing but I am really intersted in this programme. Thanks</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a8a912b01d6de2f5cef24a45e4d115450514079.png" data-download-href="/uploads/short-url/64kVNQd6pgCyCVdqasPA1sYl9Db.png?dl=1" title="27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a8a912b01d6de2f5cef24a45e4d115450514079_2_690x375.png" alt="27" data-base62-sha1="64kVNQd6pgCyCVdqasPA1sYl9Db" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a8a912b01d6de2f5cef24a45e4d115450514079_2_690x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a8a912b01d6de2f5cef24a45e4d115450514079_2_1035x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a8a912b01d6de2f5cef24a45e4d115450514079.png 2x" data-dominant-color="BCBDBF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">27</span><span class="informations">1366×743 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2018-10-19 18:27 UTC)

<p>I can use a custom name that I type in the same version you’re referring to.</p>
<p>Also from the screenshot it seems that you successfully selected the name of the scene for renaming you just need to type the name. What is the issue you’re having?</p>

---

## Post #3 by @Ash_Alarfaj (2018-10-19 19:20 UTC)

<p>Hi</p>
<p>When I’ve saved the sence with the new name it is saved with just the origenal name(display the date only)</p>

---

## Post #4 by @jamesobutler (2018-10-19 20:33 UTC)

<p>I’ve tried with 4.9.0-2018-10-16 on Windows and I am able to save an MRB with a custom name successfully.</p>
<p>If you have all the text in the cell selected and then start typing a new name you will have to type the extension as well. If you type something like “test-name” and then click outside the field, it will revert back to the previous acceptable name. You might not have noticed this if you clicked “Save” while the file name field was still in edit mode. You would need to type something like “test-name.mrb”.</p>
<p>To any developers, I think qSlicerDataDialog would be a bit easier to use if you didn’t have to type the extension in the file name which has to match the currently specified File Format combo box item for the new name to pass the validator.  It seems redundant to specify extension in file name and in the file format column.</p>

---
