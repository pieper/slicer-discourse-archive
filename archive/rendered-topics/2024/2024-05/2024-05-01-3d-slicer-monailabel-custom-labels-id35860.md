---
topic_id: 35860
title: "3D Slicer Monailabel Custom Labels"
date: 2024-05-01
url: https://discourse.slicer.org/t/35860
---

# 3d Slicer - MonaiLabel - custom labels

**Topic ID**: 35860
**Date**: 2024-05-01
**URL**: https://discourse.slicer.org/t/3d-slicer-monailabel-custom-labels/35860

---

## Post #1 by @Andras_Gomori (2024-05-01 21:39 UTC)

<p>Hi!</p>
<p>Windows 10, Slicer 3D 5.6.2, MonaiLabel 0.8.1.<br>
I have a functioning Nvidia card with cuda support.<br>
I ran the ‘hello world’ spleen segmentation.</p>
<p>I converted my dicom files to nifti, it works until I use custom labels in the monailabel config. If I use only 1 of my custom labels everything seems fine. After adding at least 1 more custom label, things are getting messy.<br>
I’m unsure what I’m doing wrong.</p>
<p>Somewhere I read try to change the application (radiology) name. May it be the solution?</p>
<p>(I tried to use the --conf use_pretrained_model false, or changing it in the conf, the error is consistent)</p>
<p>Log:<br>
Traceback (most recent call last):<br>
File “G:/prog_app/Slicer 5.6.2/slicer.org/Extensions-32448/MONAILabel/lib/Slicer-5.6/qt-scripted-modules/MONAILabel.py”, line 1545, in onClickSegmentation<br>
result_file, params = self.logic.infer(model, image_file, params, session_id=self.getSessionId())<br>
File “G:/prog_app/Slicer 5.6.2/slicer.org/Extensions-32448/MONAILabel/lib/Slicer-5.6/qt-scripted-modules/MONAILabel.py”, line 2321, in infer<br>
result_file, params = client.infer(model, image_in, params, label_in, file, session_id)<br>
File “G:\prog_app\Slicer 5.6.2\slicer.org\Extensions-32448\MONAILabel\lib\Slicer-5.6\qt-scripted-modules\MONAILabelLib\client.py”, line 344, in infer<br>
raise MONAILabelClientException(<br>
MONAILabelLib.client.MONAILabelClientException: (1, ‘Status: 500; Response: Internal Server Error’)</p>

---

## Post #2 by @Andras_Gomori (2024-05-02 18:37 UTC)

<p>The name change did not solve the problem. I’ve tried to manipulate the pip installs but had no success.</p>

---

## Post #3 by @Andras_Gomori (2024-05-06 19:57 UTC)

<p>The error was on my side.<br>
I found in another forum:<br>
" remove all files in the <code>model</code> folder"</p>
<p>this solved the problem. It has to be done if the training is from absolute zero (“scratch”)</p>

---
