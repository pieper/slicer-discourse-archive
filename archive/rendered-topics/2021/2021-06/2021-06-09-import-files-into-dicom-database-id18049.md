# Import files into DICOM database

**Topic ID**: 18049
**Date**: 2021-06-09
**URL**: https://discourse.slicer.org/t/import-files-into-dicom-database/18049

---

## Post #1 by @OpenSource_Contri (2021-06-09 19:56 UTC)

<p>Hello,<br>
I wanted to access “Import DICOM files” modal dialog window to open automatically just after opening of application but not by clicking button “Import DICOM files”.</p>
<p><strong>Includes</strong><br>
“…\Modules\Scripted\DICOM.py”<br>
“…\Modules\Scripted\DICOM\Resources\UI\DICOM.ui”<br>
“…\Applications\SlicerApp\Testing\Python\Utiltest.py”</p>
<p>Could you please help?<br>
Thanks.</p>

---

## Post #2 by @lassoan (2021-06-09 21:06 UTC)

<p>You can open the DICOM import popup like this:</p>
<pre><code class="lang-python">slicer.util.selectModule('DICOM')
slicer.util.getModuleGui('DICOM').importFolder()
</code></pre>
<p>You can find more DICOM module scripting examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#dicom">script repository</a>.</p>

---

## Post #3 by @OpenSource_Contri (2021-06-10 09:34 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08e6fa77f263942b209fbb6a95da0f1785227489.png" data-download-href="/uploads/short-url/1gKGHjzmhIrEPb5h07tVhX7lZqx.png?dl=1" title="Screenshot (174)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/08e6fa77f263942b209fbb6a95da0f1785227489_2_690x388.png" alt="Screenshot (174)" data-base62-sha1="1gKGHjzmhIrEPb5h07tVhX7lZqx" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/08e6fa77f263942b209fbb6a95da0f1785227489_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/08e6fa77f263942b209fbb6a95da0f1785227489_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/08e6fa77f263942b209fbb6a95da0f1785227489_2_1380x776.png 2x" data-dominant-color="36363C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (174)</span><span class="informations">1920×1080 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Thanks for the reply.</p>
<p><strong>I wanted to open DICOM import popup window just after starting of application.</strong><br>
It is currently opening after clicking button Import DICOM files.</p>
<p><strong>Screenshot is attached</strong></p>

---

## Post #4 by @cpinter (2021-06-10 09:48 UTC)

<p>Have you read <a class="mention" href="/u/lassoan">@lassoan</a>’s comment just above? Do you have any questions about that?</p>

---

## Post #5 by @OpenSource_Contri (2021-06-10 09:54 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a><br>
Yes I have read <a class="mention" href="/u/lassoan">@lassoan</a>’s comment and I can open the DICOM import popup by that but not as I want.<br>
I wanted to open DICOM import popup window automatically just after starting of application without clicking on any button.<br>
Please guide.</p>

---

## Post #6 by @cpinter (2021-06-10 10:17 UTC)

<p>If you add those lines in your <code>.slicerrc.py</code> file then it will run at startup and it will open the window for you. You can easily find that file in Application settings / General / Application startup script.</p>

---

## Post #7 by @OpenSource_Contri (2021-06-10 14:43 UTC)

<p>Thank You <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> .<br>
It was very much helpful.</p>

---
