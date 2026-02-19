---
topic_id: 5262
title: "Separate Arterial Phase And Venous Phase Into Two Series"
date: 2019-01-03
url: https://discourse.slicer.org/t/5262
---

# Separate arterial phase and venous phase into two series

**Topic ID**: 5262
**Date**: 2019-01-03
**URL**: https://discourse.slicer.org/t/separate-arterial-phase-and-venous-phase-into-two-series/5262

---

## Post #1 by @Chen_Bangbin (2019-01-03 11:49 UTC)

<p>Operating system: macbook pro<br>
Slicer version: 4.11.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Dear sir:</p>
<p>When I upload abdominal CT images, the arterial phase and venous phase images are mixed up. How can I separate them and upload arterial phase (or venous phase) only?</p>
<p>Thank you for the help!</p>

---

## Post #2 by @lassoan (2019-01-03 15:50 UTC)

<p>What do you mean by mixed up? Do you mean that both arteries and veins are opacified by the contrast agent and you would like to segment them separately? You can do that using Segment Editor’s Grow from seeds effect (paint different segments in artery and vein branches). Probably <a href="https://www.youtube.com/watch?v=8Nbi1Co2rhY" rel="nofollow noopener">masked region growing</a> that has been added to Slicer recently will work well.</p>

---

## Post #3 by @Chen_Bangbin (2019-01-03 22:33 UTC)

<p>Thank you for the quick reply.</p>
<p>When I import theses CT images that contain both arterial and venous phases, the slice order is one image of arteral phase, then one image of venous phase in the same location, then arterial phase, then venous phase…It is impossible to segment a tumor in arterial phase only （or in venous phase only becase the slice order is mixed. How can I separate these two phases？</p>
<p>Thank you for the help again!</p>

---

## Post #4 by @Chen_Bangbin (2019-01-03 22:40 UTC)

<p>By the way, the arterial phase images are images taken 35 seconds after contrast injection, venous phase images are 80 seconds after contrast injection. They are two sets of images on the same location of abdomen with different contrast enhancement.</p>
<p>Thank you!</p>

---

## Post #5 by @pieper (2019-01-03 22:48 UTC)

<p>If you go into <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/DICOM" rel="nofollow noopener">advanced mode in the dicom browser</a> you should be presented with different load options.  These could probably be read as different scalar volumes, or maybe as a multivolume, depending on what tags are in the header.</p>

---

## Post #6 by @lassoan (2019-01-03 23:00 UTC)

<p>You may also try to enable grouping based on content time in application settings / DICOM section. It may make additional loadables show up in Advanced section in DICOM module.</p>

---

## Post #7 by @Emmanuel_Salinas_Mir (2020-05-15 15:57 UTC)

<p>Hi Chen.</p>
<p>Operating system: macbook pro<br>
Slicer version: 4.11.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Dear sir:</p>
<p>Did you come out with any solution for this issue of separate the arterial phase and venous phases ?</p>
<p>Regards</p>

---

## Post #8 by @Chen_Bangbin (2020-05-16 00:19 UTC)

<p>Hello:</p>
<p>No, I have to use other software to separate different phases.<br>
I would be very appreciated if you can come up with solutions.<br>
Thank you!</p>
<p>Best</p>
<p>Bang-Bin</p>

---

## Post #9 by @Emmanuel_Salinas_Mir (2020-05-16 00:41 UTC)

<p>Hi Chen</p>
<p>Could you share the name privately?</p>
<p>Best</p>

---

## Post #10 by @Chen_Bangbin (2020-05-16 01:00 UTC)

<p>Hi:</p>
<p>I used “RadiAnt” software to see the images and manually select the venous phase images.</p>
<p>Bang-Bin</p>

---

## Post #11 by @yf025 (2020-05-16 01:24 UTC)

<p>There is a impressive software called ‘Mango’ which I highly recommend ，you can separate the arterial phase and venous phases rapidly and convert them to compressed（or not as your will）nii format in the same time.The download url followed as：<a href="http://ric.uthscsa.edu/mango/index.html" rel="nofollow noopener">http://ric.uthscsa.edu/mango/index.html</a></p>

---

## Post #12 by @Chen_Bangbin (2020-05-16 01:54 UTC)

<p>Great! I will try it. Thank you for your help!</p>

---

## Post #13 by @Emmanuel_Salinas_Mir (2020-05-16 01:59 UTC)

<p>Thanks</p>
<p>Will try it.</p>
<p>Thanks a lot.</p>

---

## Post #14 by @lassoan (2020-05-16 03:41 UTC)

<p>Recent Slicer Preview releases should be able to load these 3D volume sequences without problems. If you run into issues then let us know.</p>

---

## Post #15 by @Emmanuel_Salinas_Mir (2020-05-16 15:25 UTC)

<p>I can confirm no problem using these 3D volume sequences on slicer.</p>
<p>Thans <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/chen_bangbin">@Chen_Bangbin</a> and <a class="mention" href="/u/yf025">@yf025</a></p>

---
