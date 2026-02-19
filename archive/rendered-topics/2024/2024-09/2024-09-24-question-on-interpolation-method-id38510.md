---
topic_id: 38510
title: "Question On Interpolation Method"
date: 2024-09-24
url: https://discourse.slicer.org/t/38510
---

# Question on Interpolation method

**Topic ID**: 38510
**Date**: 2024-09-24
**URL**: https://discourse.slicer.org/t/question-on-interpolation-method/38510

---

## Post #1 by @alientex (2024-09-24 10:11 UTC)

<p>Hello,</p>
<p>In the <code>models.md</code> file of the Slicer source code, it is mentioned that the Gouraud interpolation method is enabled by default. I would like to switch to a different interpolation method, such as Phong or Flat, for the 3D model visible in the interactive 3D widget.</p>
<p>Could someone please guide me on which file to modify?</p>

---

## Post #2 by @cpinter (2024-09-24 10:55 UTC)

<p>You can set the interpolation method in the Models module</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a943627458cb2a194c18ff804739ebc765c1818.png" data-download-href="/uploads/short-url/8mdezunwX7rmTveIg8ORgRYUUOY.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a943627458cb2a194c18ff804739ebc765c1818_2_348x500.png" alt="image" data-base62-sha1="8mdezunwX7rmTveIg8ORgRYUUOY" width="348" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a943627458cb2a194c18ff804739ebc765c1818_2_348x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a943627458cb2a194c18ff804739ebc765c1818.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a943627458cb2a194c18ff804739ebc765c1818.png 2x" data-dominant-color="ECEDEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">510×731 28.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @cpinter (2024-09-24 11:11 UTC)

<p>It seems that you found the documentation but it did not give you enough information. Would you have any suggestion to improve it?</p>
<p>By the way the md file you found is rendered here in the documentation: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/models.html" class="inline-onebox">Models — 3D Slicer documentation</a></p>
<p>Thanks for any feedback!</p>

---

## Post #4 by @alientex (2024-09-26 12:24 UTC)

<p>Thank you for asking for my suggestions! I would be happy to offer one: I believe that providing a short demo video for each module’s usage at the top of each module section in the documentation would greatly help users and learners of Slicer.</p>

---

## Post #5 by @cpinter (2024-09-26 14:25 UTC)

<p>Thanks for the suggestion! The problem with videos is that they cannot be changed when something changes in the app, they need to be redone from scratch. At the same time text documentation is very easy to maintain. Since Slicer does not have funding for infrastructure, any development that is not directly related to an ongoing research effort needs to be done in our “free time”.</p>
<p>At the same time there is an ongoing effort to automatically record tutorial videos in different languages following a script. That could be used for the module doc videos as well once done and proven. (I tried to find the project week page but didn’t succeed)</p>

---
