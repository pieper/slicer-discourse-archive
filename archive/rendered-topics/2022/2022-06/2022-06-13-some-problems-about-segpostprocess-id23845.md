---
topic_id: 23845
title: "Some Problems About Segpostprocess"
date: 2022-06-13
url: https://discourse.slicer.org/t/23845
---

# Some problems about SegPostProcess

**Topic ID**: 23845
**Date**: 2022-06-13
**URL**: https://discourse.slicer.org/t/some-problems-about-segpostprocess/23845

---

## Post #1 by @yuanzhen_cui (2022-06-13 04:31 UTC)

<p>Operating system:MacOs<br>
Slicer version:4.1120210226<br>
Expected behavior:I try to execute the SegPostProcess with the example names “InputImage.nrrd” which download from the slicerssalt workshop.<br>
Actual behavior:The Log messages shows "SegPostProcess terminated with a fault.<br>
". Actually I also tried several *.nrrd and *.nii files, all of them didn’t execute SegPostProcess sucessfully. And If I use that files to execute “GenParaMesh” directly, Log messages will show Euler number is not satisfied. I really need some help.<br>
Thanks a lot!<br>
Cui</p>

---

## Post #2 by @lassoan (2022-06-13 13:48 UTC)

<p>Could you describe what you would like to achieve? There may be other modules that work better.</p>

---

## Post #3 by @yuanzhen_cui (2022-06-13 15:12 UTC)

<p>Hi Mr.Lasso,<br>
Thanks for your reply, I will describe my question more specifically.</p>
<p>I want to generate mean shape from some medical nrrd files. And according to the tutorial, I should implement SPHARM first. But none of my examples complete “SegPostProcess” with default parameters. Error: <strong>SegPostProcess terminated with a fault.</strong> Even I try the example names “cillinder_seg.nrrd” which download from the <a href="https://data.kitware.com/#collection/586fbb7b8d777f05f44a5c7b/folder/5e8cbd312660cbefba9c19b0" rel="noopener nofollow ugc">slicersalt workshops</a>. The “SegPostProcess” also failed to execute successfully.</p>
<p>And if I skip the “SegPostProcess” and implement “GenParaMesh” directly, I encounter <strong>Euler equation not satisfied. Euler Number : 106516 - 106508 = 8</strong>.</p>
<p>I think SPHARM is an essential step to generate mean shape because RigidAlignment require Surface meshes and parametrization sphere which are the output of the SPHARM. So I’m stuck.</p>
<p>Thanks again for your attention!<br>
Cui</p>

---

## Post #4 by @yuanzhen_cui (2022-06-13 15:36 UTC)

<p>Mr.Lasso,</p>
<p>According to the tutorial, <strong>SegPostProcess</strong> “<em>ensure spherical topology of the segmentations by filling any interior holes and by applying two smoothing operations</em>”, So I deduce SegPostProcess can solve the problem of <strong>Euler equation</strong>. Is my guess correct?</p>
<p>Then, I find the function <strong>Label Map Smoothing</strong>, which seems to have the same function as <strong>SegPostProcess</strong>. So I apply this function to my nrrd files. Surprisingly, some of them can implement <strong>GenParaMesh</strong> without Euler equation error. But others still have  Euler equation error.</p>
<p>This is my whole process. Looking forward to your reply. Thanks!<br>
Cui</p>

---

## Post #5 by @styner (2022-06-13 17:53 UTC)

<p>Hi Cui<br>
Are you trying to run SegPostProcess on a label/segmentation image with a single label? If not, then you need to provide which label (number) you would like to extract before you run SegPostProcess. This might be your problem with SegPostProcess.</p>
<p>And yes, essentially SegPostProcess smooths the label/segmentation (it performs a closing operation, a surface smoothing and a small hole filing operation). Using the Label Map Smoothing module will partially accomplish a similar thing (though the smoothing operator is different and there is no specific hole filing).</p>
<p>Martin</p>

---

## Post #6 by @yuanzhen_cui (2022-06-14 09:19 UTC)

<p>Hi Mr.Styner,</p>
<p>Thank you very much for your help! Indeed, I forgot to set the label number that I want to extract.<br>
I have successfully run the <strong>SegPostProcess</strong>, and thanks for explaning the relation between <strong>SegPostProcess</strong> and <strong>Label Map Smoothing</strong>.</p>
<p>Have a nice day.<br>
Cui</p>

---
