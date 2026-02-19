---
topic_id: 43566
title: "Edit The Rotation Tags In Dicom Ct Slices Without Modify The"
date: 2025-07-01
url: https://discourse.slicer.org/t/43566
---

# Edit the rotation tags in DICOM CT slices without modify the image

**Topic ID**: 43566
**Date**: 2025-07-01
**URL**: https://discourse.slicer.org/t/edit-the-rotation-tags-in-dicom-ct-slices-without-modify-the-image/43566

---

## Post #1 by @JFC (2025-07-01 20:29 UTC)

<p>Dear all:<br>
I would like to know the option in 3D Slicer to edic the DICOM tags regarding to the patient rotation, without modify the CT images. Please, anyone has experinec with this issue?.<br>
Thanks so mch.<br>
JFC<br>
Barcelona. Spain.</p>

---

## Post #2 by @pieper (2025-07-01 22:39 UTC)

<p>If you apply linear transform, harden it, and then export as dicom this should work.</p>

---

## Post #3 by @JFC (2025-07-02 01:21 UTC)

<p>Dear Steve:<br>
Thank you very much for your reply. Please, I have not experience with 3D Slicer. Please, may ask you about the steps to perform in 3D Slicer to do what you told me ?.<br>
Thanks so much for your support and kindness.<br>
Juan Francisco</p>
<p>Ps: please, maybe can arrange a Teams session of 10 min with you?. Thanks so much.</p>
<p><a href="https://mail.onelink.me/107872968?pid=nativeplacement&amp;c=US_Acquisition_YMktg_315_SearchOrgConquer_EmailSignature&amp;af_sub1=Acquisition&amp;af_sub2=US_YMktg&amp;af_sub3=&amp;af_sub4=100002039&amp;af_sub5=C01_Email_Static_&amp;af_ios_store_cpp=0c38e4b0-a27e-40f9-a211-f4e2de32ab91&amp;af_android_url=https://play.google.com/store/apps/details?id=com.yahoo.mobile.client.android.mail&amp;listing=search_organize_conquer" rel="noopener nofollow ugc">Yahoo Mail: Busca, organiza, conquista</a></p>

---

## Post #4 by @pieper (2025-07-02 12:48 UTC)

<p>Hi <a class="mention" href="/u/jfc">@JFC</a>  - Regarding the suggestion of a teams call: a goal of this forum is to jointly discover, document, and disseminate ways to use Slicer to accomplish important tasks in medical imaging, so we like to keep everything public for mutual benefit rather than having one-on-one discussions that are not available to others.</p>
<p>It’s good that you ask questions so we can understand what’s not clear in the existing documentation or in previously answered questions, or what’s hard to figure out in the interface.</p>
<p>Although it’s not required, we hope that people who use this forum to get answers will also help others, either here on the forum or in their community, to learn, document, and share these techniques.</p>
<p>Back to your question, the steps are as follows:</p>
<ul>
<li>load the data using the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#dicom-import">DICOM module</a></li>
<li>create a linear transform using the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#create-a-transform">Transforms module</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#apply-transform-to-a-node">apply the transform</a> to the loaded volume</li>
<li>use the sliders or the interactive tools to <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#modify-transform">set the desired rotation</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#harden-transform-on-a-node">harden the transform</a> on the data</li>
<li><a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#export-data">export</a> the rotated data <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database">as DICOM</a></li>
</ul>

---

## Post #5 by @Xiaojie_Guo (2025-07-04 02:25 UTC)

<p>Do you want to change the DICOM tag (like PatientPosition)?</p>

---
