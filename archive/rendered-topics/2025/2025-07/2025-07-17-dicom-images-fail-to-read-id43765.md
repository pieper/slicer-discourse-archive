---
topic_id: 43765
title: "Dicom Images Fail To Read"
date: 2025-07-17
url: https://discourse.slicer.org/t/43765
---

# Dicom images fail to read

**Topic ID**: 43765
**Date**: 2025-07-17
**URL**: https://discourse.slicer.org/t/dicom-images-fail-to-read/43765

---

## Post #1 by @MLPPD (2025-07-17 21:45 UTC)

<p>Hello all,</p>
<p>I’m a new user of VMTK, trying to read in a set of processed DICOM images with the command “vmtkimagereader -ifile C:\Users\Admin\Documents\s0.5-10\1 -f dicom”. When I do so, it produces the following error:<br>
Traceback (most recent call last):<br>
File “C:\Users\Admin\miniforge3\envs\vmtk\lib\site-packages\vmtk\pypeserver.py”, line 46, in RunPypeProcess<br>
pipe.Execute()<br>
File “C:\Users\Admin\miniforge3\envs\vmtk\lib\site-packages\vmtk\pype.py”, line 324, in Execute<br>
scriptObject.Execute()<br>
File “C:\Users\Admin\miniforge3\envs\vmtk\lib\site-packages\vmtk\vmtkimagereader.py”, line 266, in Execute<br>
self.ReadITKIO()<br>
File “C:\Users\Admin\miniforge3\envs\vmtk\lib\site-packages\vmtk\vmtkimagereader.py”, line 203, in ReadITKIO<br>
matrix.GetElement(0,0), matrix.GetElement(0,1), matrix.GetElement(0,2), matrix.GetElement(0,3),<br>
AttributeError: ‘NoneType’ object has no attribute ‘GetElement’</p>
<p>as well as the following, in the pypepad output:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c304ee6435372b40c13f5a81b021ac0921b6379.png" data-download-href="/uploads/short-url/fr548d0xzFJdHSMtPfgSQT1VFTr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c304ee6435372b40c13f5a81b021ac0921b6379.png" alt="image" data-base62-sha1="fr548d0xzFJdHSMtPfgSQT1VFTr" width="690" height="466" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">962×650 15.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve tried importing multiple different sets of DICOM images, both those I am working with and test datasets, on two different PCs (Windows 10/11), with both binary installation versions as well as through conda forge. Any help in resolving this issue would be greatly appreciated.</p>

---

## Post #2 by @muratmaga (2025-07-18 01:20 UTC)

<p>Is there a reason why you are not using the Slicer’s DICOM module?</p>

---

## Post #4 by @MLPPD (2025-07-21 14:02 UTC)

<p>I’m trying to use VMTK standalone (hence why I posted under the VMTK community).</p>

---

## Post #5 by @chir.set (2025-07-21 15:15 UTC)

<aside class="quote no-group" data-username="MLPPD" data-post="4" data-topic="43765">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c67d28/48.png" class="avatar"> MLPPD:</div>
<blockquote>
<p>I’m trying to use VMTK standalone</p>
</blockquote>
</aside>
<p><em>Just in case</em> you have been tasked by doctors to press the juice from a DICOM series in <em>one click</em>, please consider it is <strong>impossible</strong>.</p>
<p>You may automate a lot of tasks if you use Slicer itself, that’s the way to go and it won’t ever be <code>one-click-get-all</code>.</p>
<p>Admittedly, your purpose may be something else and my comments are unrelated to your intent. Nevertheless, I still point out that it’s not fun playing with VMTK standalone.</p>

---

## Post #6 by @muratmaga (2025-07-21 16:26 UTC)

<aside class="quote no-group" data-username="MLPPD" data-post="4" data-topic="43765" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c67d28/48.png" class="avatar"> MLPPD:</div>
<blockquote>
<p>I’m trying to use VMTK standalone (hence why I posted under the VMTK community).</p>
</blockquote>
</aside>
<p>Sorry don’t know anything about standalone VMTK. All I know, as <a class="mention" href="/u/chir.set">@chir.set</a> is alluded DICOM is a complicated format, and developers of Slicer has put a lot of effort into building a robust DICOM module that handles myriads of exceptions and oddities vendors provide.</p>
<p>Hope someone on the forum can help you with your question.</p>

---

## Post #7 by @MLPPD (2025-07-21 19:23 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bee0007b3773200626ac022ace990119312b7c80.png" data-download-href="/uploads/short-url/reyDKLWEu1y5ggfyEf2Y1flXmCs.png?dl=1" title="thumbnail_image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bee0007b3773200626ac022ace990119312b7c80.png" alt="thumbnail_image" data-base62-sha1="reyDKLWEu1y5ggfyEf2Y1flXmCs" width="690" height="201" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">thumbnail_image</span><span class="informations">933×272 9.59 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I seem to have attached the wrong image, I’ve just noticed. The error is roughly the same but the path is to an actual DICOM image.</p>

---

## Post #8 by @MLPPD (2025-07-21 19:49 UTC)

<p>In noticing this I’ve discovered why I’m getting this error: in all cases either the directory I was working in began with a python escape character, or my images began with a number (causing the same effect). Adding an extra slash has prevented the error (though the image viewer now appears to be showing an entirely black volume).</p>

---
