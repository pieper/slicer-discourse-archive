---
topic_id: 11859
title: "Mri Requirements For 3D Modeling"
date: 2020-06-04
url: https://discourse.slicer.org/t/11859
---

# MRI requirements for 3D modeling

**Topic ID**: 11859
**Date**: 2020-06-04
**URL**: https://discourse.slicer.org/t/mri-requirements-for-3d-modeling/11859

---

## Post #1 by @Ricardo (2020-06-04 09:45 UTC)

<p>Hello everybody, hope someone can help me with this one:</p>
<p>If I wanted to ask for a MRI similar to a TC scan with the following settings:</p>
<ul>
<li>Matrix: 512 x 512;*</li>
<li>Radiation: 120kV, mAs as given by automatic system;*</li>
<li>Slice Thickness: max 1.0mm;*</li>
<li>Slice Increment: Contiguos slices;*</li>
<li>Step Rotation: max. 1.0mm;*</li>
<li>Step Reconstruction Slice: max. 1.0mm;*</li>
<li>Reconstruction algorithm: High resolution bone or detail algorithm;*</li>
<li>Gantry tilt: 0º.*</li>
</ul>
<p>Which settings do I need to ask for that MRI?</p>
<p>Thanks in advance,</p>
<p>Ricardo</p>

---

## Post #2 by @lassoan (2020-06-04 13:55 UTC)

<p>What would like to visualize in the images and for what purpose?</p>

---

## Post #3 by @Ricardo (2020-06-04 14:49 UTC)

<p>Hi Andras,</p>
<p>it will be mainly for bone modeling (skull and vertebral column).</p>
<p>Those models will be used to build surgical cutting guides, so enough precision is needed.</p>
<p>Thank you,</p>
<p>Ricardo</p>

---

## Post #4 by @pieper (2020-06-04 15:23 UTC)

<p><a class="mention" href="/u/ricardo">@Ricardo</a> - there’s no one-to-one mapping from CT to MR.  They use very different methods and have different pros and cons.  You should probably read up on medical imaging physics before even thinking about creating a surgical cutting guide from any particular modality.</p>

---

## Post #5 by @lassoan (2020-06-04 15:34 UTC)

<p>Bone visualization on MRI is very challenging and you need to use imaging protocol specially tuned for this purpose. This is a hard problem, there are no readily available solutions that could provide bone image quality comparable to CT, but if you work with your MRI technologist then you might come up with solutions that work for certain use cases.</p>
<p>For example, we worked on <a href="https://projectweek.na-mic.org/PW32_2019_London_Canada/Projects/Spinemodels/">MRI-based surgical guide generation based on spine MRI images</a> at the Slicer Robarts Project Week last year with Andrew Kanawati (orthopedic surgeon, from Australia). You may look him and contact him for getting first-hand information about challenges and potential solutions.</p>

---

## Post #6 by @Ricardo (2020-06-04 21:30 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> thank you, much appreciated.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> will try to get in touch with Dr. Kanawati and see if there’s any chance to learn from his experience.</p>
<p>Once again, thank you so much.</p>
<p>Regards,</p>
<p>Ricardo.</p>

---

## Post #7 by @kopachini (2020-06-07 20:22 UTC)

<p>Hi Ricardo,<br>
I am wondering why do you want to scan bones with MR and not using CT scanner? Is it a child or pregnant woman? You will have better contrast of bone and soft tissue using CT scanner.<br>
If MR is your only option, you want to use isovoxel sequences so you can import it and make decent looking model.<br>
T1 and T2 times will show cortical bone and marrow differently, so I propose manual segmentation.</p>
<p>There is one sequence that is used for good bone visualization called <strong>black bone</strong>, but you have to have good radiology technicians and the possibility of tweaking sequences (not all vendors allow that). Two years ago with the help of a radiology technician at my department, we try to come as close as possible to black bone sequence with a really good result and visualization of cranial bone (couldn’t tweak all the parameters as in published articles, but it was sufficient). Here are some papers: <a href="https://pubmed.ncbi.nlm.nih.gov/22391497/" rel="nofollow noopener">https://pubmed.ncbi.nlm.nih.gov/22391497/</a><br>
<a href="https://pubmed.ncbi.nlm.nih.gov/30406272/" rel="nofollow noopener">https://pubmed.ncbi.nlm.nih.gov/30406272/</a></p>
<p>Hope this helps,<br>
Best regards, Vjekoslav.</p>

---

## Post #8 by @Sezen (2022-01-19 17:14 UTC)

<p>Hello, I was wondering if you have managed to find any solution to this? I am doing a project where I want to fine a way to automate segmentation of bone in only MRI so this would be very helpful.<br>
Thanks in advance</p>

---
