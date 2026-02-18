# Transforming a 2D image into a tactile, 3D representation

**Topic ID**: 40879
**Date**: 2024-12-28
**URL**: https://discourse.slicer.org/t/transforming-a-2d-image-into-a-tactile-3d-representation/40879

---

## Post #1 by @Muhammed_BASTI (2024-12-28 05:37 UTC)

<p><strong>Project Overview:</strong></p>
<p>I’m working on a project aimed at creating a unique experience for visually impaired individuals. The concept involves transforming a 2D image into a tactile, 3D representation. The goal is to make the project interactive and personal while helping the individuals feel more connected to the subject of the image. I’m currently exploring the best ways to bring this idea to life and would greatly appreciate any advice or insights that could help me improve the project and make it more impactful.</p>
<p><strong>Objective:</strong> To provide a meaningful and innovative solution that can be both emotionally and practically beneficial for the individuals involved.</p>

---

## Post #2 by @lassoan (2024-12-28 05:57 UTC)

<p>We have too many ideas, so you need to be a bit more specific.</p>
<p>Whaf kind kind of images do you work with? Medical images? Cross-sectional images? What imaging modality?</p>
<p>What are your constraints on the representation? 3D printing would be an obvious choice - would that be an option? There are also many haptic devices for a more dynamic experience. Which ones have you considered?</p>

---

## Post #3 by @Muhammed_BASTI (2024-12-28 09:28 UTC)

<p>First of all, thank you very much for your response. I am not a healthcare professional, and I am not familiar with the terms you mentioned. However, I am an entrepreneur who works with 3D printing, and I aim to make a difference in the lives of visually impaired mothers. The main idea of my project is to convert black-and-white ultrasound baby images into 3D-printable formats and produce tactile models as gifts.</p>
<p>For this purpose, I have downloaded the necessary software from <a href="http://3DSlicer.org" rel="noopener nofollow ugc">3DSlicer.org</a>. However, I need guidance on which data I should request from hospitals or how I can obtain this data to bring my project to life.</p>
<p>I would greatly appreciate your assistance.</p>

---

## Post #4 by @nadayoda59 (2025-01-13 05:01 UTC)

<p>Hello Muhammad_BASTI I show my respect for your wonderful idea.<br>
I’ve worked on a similar project. I’d like to help you with your ideas in a few steps.</p>
<ol>
<li>The hospital acquires ultrasound medical images through Pacs, USB, or CD.</li>
<li>Segment the child by searching the medical images. (There may be an ultrasound imaging method that allows the child to segment well.)</li>
<li>Create a 3D model by extracting the mesh of Slicer or Python</li>
<li>Extract with STL and you’re done!</li>
</ol>
<p>I think it would be good to print it in 3D in that way. Thank you</p>
<p>If you are additionally interested, please contact <a href="mailto:nadayoda59@gmail.com">nadayoda59@gmail.com</a></p>

---
