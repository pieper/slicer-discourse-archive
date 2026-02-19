---
topic_id: 30448
title: "Cant Edit A Custom Module"
date: 2023-07-07
url: https://discourse.slicer.org/t/30448
---

# Can't edit a custom module

**Topic ID**: 30448
**Date**: 2023-07-07
**URL**: https://discourse.slicer.org/t/cant-edit-a-custom-module/30448

---

## Post #1 by @Poppy (2023-07-07 11:25 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 5.2.2</p>
<p>Expected behavior:<br>
Hello, I am trying to make a custom scripted module. After creating it if I press reload and test on the default template code it says test passed however I am not able to edit the code using the edit button or using the Python debugger.</p>
<p>Actual behavior:<br>
If I press edit on the module then the command line opens and displays "No module named ‘logic’ " before closing and then nothing else happens as you can see in the picture below:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e0eb1e901e855950fea44f032a7d431e0f90484.png" alt="image" data-base62-sha1="20marjArUkfbSgZMmEDoWUu6b4M" width="663" height="203"></p>
<p>I also tried to edit the code using the Python Debugger. The python end appears to be working correctly, however the Slicer end asks me to select a debugger in the settings panel although I believe I have done this already.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/787c5ff7a39ec50bab102d5e5037d7b3a3cebe54.png" data-download-href="/uploads/short-url/hbRLDGDuz0JKdwGPyDo2MdU8zWs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/787c5ff7a39ec50bab102d5e5037d7b3a3cebe54.png" alt="image" data-base62-sha1="hbRLDGDuz0JKdwGPyDo2MdU8zWs" width="575" height="500" data-dominant-color="404445"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">756×657 17.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70719f72aaf2478f02108f583f1a55920228b2fc.png" data-download-href="/uploads/short-url/g2IUzGBeiDbNXrGFNRKkjIpWG5u.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70719f72aaf2478f02108f583f1a55920228b2fc.png" alt="image" data-base62-sha1="g2IUzGBeiDbNXrGFNRKkjIpWG5u" width="690" height="99" data-dominant-color="313232"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">874×126 12.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/158bef71a901c405d13aaf5777d6a10a9e01e99b.png" alt="image" data-base62-sha1="34BPTbxRhZPYj40bk7L3O3vTyWL" width="625" height="386"></p>
<p>Does anyone one know what could be causing these issues?</p>
<p>Thank you for your help</p>

---

## Post #2 by @lassoan (2023-07-08 14:26 UTC)

<p>The “Edit” button opens the module .py file using the default application that you have configured for such files. It seems that you have not confgured an editor but instead you have associated it with a Python launcher (<code>C:\windows\py.exe</code>).</p>
<p>You have a couple of options:</p>
<ul>
<li>change your operating system settings to associate .py files open with a text editor (so that they are opened in a text editor instead of launched on double-click)</li>
<li>do not use the <code>Edit</code> button and instead open the file manually</li>
<li>wait for this <a href="https://github.com/Slicer/Slicer/pull/7074">pull request</a> to be merged (expected within a couple of days) that allows configuration of a custom editor for .py files</li>
</ul>

---

## Post #3 by @lassoan (2024-07-30 21:20 UTC)

<p>A post was split to a new topic: <a href="/t/how-to-add-and-edit-module/37626">How to add and edit module</a></p>

---
