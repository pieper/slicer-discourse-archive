---
topic_id: 25004
title: "Slicer Extension Installation"
date: 2022-08-30
url: https://discourse.slicer.org/t/25004
---

# Slicer extension installation

**Topic ID**: 25004
**Date**: 2022-08-30
**URL**: https://discourse.slicer.org/t/slicer-extension-installation/25004

---

## Post #1 by @Mohammad (2022-08-30 16:10 UTC)

<p>Dear support,</p>
<p>Currently I’ve tried to install a extension from GitHub for  3D slicer (<a href="https://github.com/PerkLab/SlicerSkinMouldGenerator" class="inline-onebox" rel="noopener nofollow ugc">GitHub - PerkLab/SlicerSkinMouldGenerator: 3D Slicer extension for generating 3D-printable skin moulds for radiation therapy</a>). I have added the library path into module settings but I can’t find the extension app. It seems it doesn’t installed. Could you please guide me how to install it?<br>
I’m using slicer version 11</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2022-08-30 18:33 UTC)

<p>The extension was developed in 2015, therefore you need to use Slicer-4.5 or Slicer-4.6. Since then, Python, VTK, and Slicer API have changed considerably, but it should not be too hard to update the code to be compatible with latest Slicer release. It would be great if you could work on it and we can help if you have any specific question.</p>

---

## Post #3 by @Mohammad (2022-08-31 05:42 UTC)

<p>Dear lassoan</p>
<p>Right now I installed the 3D slicer 4.5. I could install the mentioned extension ( brachytherapy module) but I don’t have any idea how to use this. Have you tried to install and use this module?</p>
<p>Best regards</p>

---

## Post #4 by @Mohamed_Hamdy (2024-05-12 09:51 UTC)

<p>I have added this extension to slicer 5.7 but unable to use it, could you let me know how to launch it after installation</p>

---

## Post #5 by @Allison_Nicole_Monta (2025-10-27 20:44 UTC)

<p>Hi Mohammad, in 2022 you had difficulties using the skin module. I’d like to know how to use it because I’m in the same situation now and it’s getting complicated. Do you have any instructions? Thank you very much.</p>

---

## Post #6 by @lassoan (2025-10-28 03:53 UTC)

<p>You have to place an ROI box and start/end points for each catheter path. Can you describe what you did, what you expected to happen, and what happened instead?</p>

---
