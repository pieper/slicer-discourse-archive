# Implementing the Demons Algorithm Registration

**Topic ID**: 16054
**Date**: 2021-02-18
**URL**: https://discourse.slicer.org/t/implementing-the-demons-algorithm-registration/16054

---

## Post #1 by @toyama (2021-02-18 08:22 UTC)

<p>I would like to implement DIR using the demon algorithm.<br>
I am including SlicerRT and Elastix to do the DIR.<br>
Is it possible to do DIR using demon algorithm with these two?</p>

---

## Post #2 by @Andinet_Enquobahrie (2021-02-18 12:58 UTC)

<p><a class="mention" href="/u/toyama">@toyama</a></p>
<p>If you are trying to implement this in python, you can look into using SimpleITK which is available via SimpleElastix or independently in as part of Slicer dependencies. Here is a notebook that shows how you can executed demons based non-rigid registration.</p>
<p><a href="http://insightsoftwareconsortium.github.io/SimpleITK-Notebooks/Python_html/66_Registration_Demons.html" class="onebox" target="_blank" rel="noopener nofollow ugc">http://insightsoftwareconsortium.github.io/SimpleITK-Notebooks/Python_html/66_Registration_Demons.html</a></p>
<p>Or use ITK C++ API directly</p>
<p><a href="https://itk.org/Doxygen/html/Examples_2RegistrationITKv4_2DeformableRegistration2_8cxx-example.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://itk.org/Doxygen/html/Examples_2RegistrationITKv4_2DeformableRegistration2_8cxx-example.html</a></p>
<p><a href="https://itk.org/Doxygen/html/Examples_2RegistrationITKv4_2DeformableRegistration16_8cxx-example.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://itk.org/Doxygen/html/Examples_2RegistrationITKv4_2DeformableRegistration16_8cxx-example.html</a></p>
<p>-Andinet</p>

---

## Post #3 by @toyama (2021-02-26 05:39 UTC)

<p>Thank you for your answer.<br>
I will try it as soon as possible.</p>

---

## Post #4 by @Chuan (2024-11-28 08:02 UTC)

<p>Hi Toyama,</p>
<p>Could you tell me if you find the DemonRegistration in python? Now I think I meet the similar question with you.  What I am looking for is the python code of DemonRegistration that used in SLICER3D, not sure if the link from Andinet uses the same code that SLICER3D employed.<br>
Best regards,<br>
Chuan</p>

---
