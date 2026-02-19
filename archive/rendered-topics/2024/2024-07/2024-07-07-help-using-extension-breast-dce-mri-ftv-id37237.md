---
topic_id: 37237
title: "Help Using Extension Breast Dce Mri Ftv"
date: 2024-07-07
url: https://discourse.slicer.org/t/37237
---

# Help using extension Breast DCE-MRI FTV

**Topic ID**: 37237
**Date**: 2024-07-07
**URL**: https://discourse.slicer.org/t/help-using-extension-breast-dce-mri-ftv/37237

---

## Post #1 by @do_huy (2024-07-07 15:24 UTC)

<ul>
<li>
<p>Operating system: windows 11<br>
Slicer version: 5.6.2<br>
Expected behavior: selecting sequences from loaded DICOM<br>
Actual behavior:</p>
</li>
<li>
<p>When i chose the “Manual” option, first i get this error:</p>
</li>
</ul>
<pre><code class="lang-auto">FileNotFoundError: [WinError 3] The system cannot find the path specified:
'C:/Users/Lenovo/Downloads/DICOM_24020895_PHẠM THỊ LƯƠNG555171\\0'" because the subfolders in my main folder are named as "0000, 0001, ...
</code></pre>
<ul>
<li>Rename these folders to “0, 1, 2, …” fix the problem and I could chose my sequences, but missing the “Done” button to continue</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/610c39c004421f900c053ae69b095d60f65d6d62.jpeg" data-download-href="/uploads/short-url/dQwvu6o17ZLc3HGhymwZ5vn4ZlE.jpeg?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/610c39c004421f900c053ae69b095d60f65d6d62_2_690x400.jpeg" alt="Untitled" data-base62-sha1="dQwvu6o17ZLc3HGhymwZ5vn4ZlE" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/610c39c004421f900c053ae69b095d60f65d6d62_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/610c39c004421f900c053ae69b095d60f65d6d62_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/610c39c004421f900c053ae69b095d60f65d6d62_2_1380x800.jpeg 2x" data-dominant-color="5F5D5C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1489×865 98.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>Also, if i select the “Automatic” option, nothing would happen and I get this error:</li>
</ul>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:/Users/Lenovo/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/Breast_DCEMRI_FTV/lib/Slicer-5.6/qt-scripted-modules/DCE_IDandPhaseSelect.py", line 705, in onApplyButton
    logic.run(self.exampath,self.dce_folders_manual,self.dce_ind_manual,self.visitstr,self.earlytime.value,self.latetime.value)
  File "C:/Users/Lenovo/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/Breast_DCEMRI_FTV/lib/Slicer-5.6/qt-scripted-modules/DCE_IDandPhaseSelect.py", line 812, in run
    precontrast_node, early_post_node, late_post_node = loadPreEarlyLate(exampath,visitnum,1,dce_folders_manual,dce_ind_manual,earlyadd,lateadd)
UnboundLocalError: local variable 'visitnum' referenced before assignment
</code></pre>
<ul>
<li>Does anyone have the solution for these errors ? This extension seems like the perfect tool I was looking for and I really hope I could make it work.  Thank you.</li>
</ul>

---

## Post #2 by @lassoan (2024-07-07 15:25 UTC)

<p>Can you share an anonymized data set that we can test the module with?</p>

---

## Post #3 by @do_huy (2024-07-07 17:28 UTC)

<ul>
<li>Do you mean the data I’m working on ? This is it.<br>
<a href="https://drive.google.com/file/d/1cqE11vXu4bo3jBjKSLQeCmjQSA6ynk8X/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">DICOM.zip - Google Drive</a></li>
<li>Also, the first time I manually choose the sequences, there would be a “Done” button. But as soon as I click “Done”, nothing would happen and the same error appeared as when I choose the “Automatic” option which is:</li>
</ul>
<p>“Traceback (most recent call last):<br>
File “C:/Users/Lenovo/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/Breast_DCEMRI_FTV/lib/Slicer-5.6/qt-scripted-modules/DCE_IDandPhaseSelect.py”, line 714, in onApplyButton<br>
logic.run(self.exampath,self.dce_folders_manual,self.dce_ind_manual,self.visitstr,self.earlytime.value,self.latetime.value)<br>
File “C:/Users/Lenovo/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/Breast_DCEMRI_FTV/lib/Slicer-5.6/qt-scripted-modules/DCE_IDandPhaseSelect.py”, line 812, in run<br>
precontrast_node, early_post_node, late_post_node = loadPreEarlyLate(exampath,visitnum,1,dce_folders_manual,dce_ind_manual,earlyadd,lateadd)<br>
UnboundLocalError: local variable ‘visitnum’ referenced before assignment”</p>
<ul>
<li>If I chose “Automatic” first then chose “Manual” then the “Done” button would not appear.</li>
</ul>

---

## Post #4 by @jlulloaa (2024-08-21 03:44 UTC)

<p>Hello<br>
I also have had trouble using this extension, mainly because it required the data to be organised in a specific way. I tried to modify it to read other types of DCEMRI DICOM 4D series, but unfortunately, after reviewing the code, I realised it would need major refactoring.</p>
<p>Therefore, I developed an <a href="https://github.com/jlulloaa/SlicerSeQ-DCEMRI" rel="noopener nofollow ugc">alternative extension</a> that leverages the existing 3D Slicer data management infrastructure to deal with Sequence data.</p>
<p>I understand that to keep things simple for users and fellow developers, it is not recommended to have duplicated extensions, so I’ll be very keen to merge mine with the existing one but will need some advice on how would be the best way to proceed.</p>
<p>Meanwhile, if anyone would like to try it, I’ll be happy to get some feedback on this alternative extension. Many thanks!!</p>
<p>Regards<br>
Jose</p>

---

## Post #5 by @do_huy (2024-09-01 03:54 UTC)

<p>Hello Mr Jose,<br>
Sorry for the late reply. It took me some time to understand the instruction because of my limited experience with 3D Slicer, but then when I get familiar with the extension it has been working perfectly.<br>
The only big issue I have encountered so far is when I load the whole patient’s data, the extension would register some unwanted sequences for DCE (like the DWI or MIP sequences) and even if I I click “Register Sequence”, I still can’t find my DCE sequences, as you can see in the image below.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/ded27ae1359f78b58bd9f86f57a6eb0ccae7e77d.png" alt="image" data-base62-sha1="vNaWSRPGSdaSPePAFnByJEh62Xb" width="689" height="72"><br>
But I found a workaround, by only select the DCE sequences when I load the data, so that the DCE sequences would be registered as the only choice.<br>
Thank you so much for your work. I will use it much more in the future and try to give you more feedback.<br>
Best regards,<br>
Huy</p>

---

## Post #6 by @jlulloaa (2024-09-13 23:05 UTC)

<p>Hello Huy<br>
Many thanks for your feedback, I’m glad to hear it has been useful! I’m currently working on a few other bugs, so sooner will be updating the repository. I’ll also include the issue you mentioned that the DCE sequence cannot be found when multiple sequences are in the patient (I haven’t tested that case, so will try to replicate the problem and provide a solution). Thanks again, and please let me know if you detect any other issue, or just add it as an issue in the repository.</p>
<p>Kind regards<br>
Jose</p>

---
