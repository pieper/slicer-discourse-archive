# Load OpenInventor (.iv) VRML 1.0 bone files in 3D Slicer

**Topic ID**: 26942
**Date**: 2022-12-27
**URL**: https://discourse.slicer.org/t/load-openinventor-iv-vrml-1-0-bone-files-in-3d-slicer/26942

---

## Post #1 by @roshans17 (2022-12-27 15:08 UTC)

<p>Hi all,</p>
<p>I am very new to Slicer so please excuse me for my ignorance. I am currently trying to understand how I can take an .iv file that represents a bone and output this onto slicer. Would love any help I can get. thank you in advance</p>

---

## Post #2 by @lassoan (2022-12-27 15:10 UTC)

<p>What software did you use to create these .iv file?</p>
<p>Can you share an example?<br>
(upload to dropbox/OneDrive and post the link here; make sure it does not contain patient information)</p>

---

## Post #3 by @roshans17 (2022-12-27 16:38 UTC)

<p>Thank you for your quick response. To be honest, I don’t know what software was used to create these .iv files as I am new to the lab and was just instructed to accomplish this. Attached below is a Google Drive link to an example of one of these files. Essentially just a bunch of 3D coordinate points that represent triangles and then points to distinguish how they are connected.  I am able to run this in Matlab by simply calling on a built-in function after parsing through the data and was wondering if there is some slicer equivalent.</p>
<p>Link: <a href="https://drive.google.com/file/d/17Gl-MOvm8AGz5OAIQu9aOJ9f7RN0ZueN/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">14819_cap_R.iv - Google Drive</a></p>

---

## Post #4 by @roshans17 (2022-12-28 21:03 UTC)

<p>Sorry to be a bother, but any thoughts? I can’t seem to find any prior discussion post about this subject matter nor any documentation. Closest I have gotten is finding scripts that output PLY or STL files.</p>

---

## Post #5 by @pieper (2022-12-28 21:46 UTC)

<p>I haven’t worked with OpenInventor in a long time.  As I recall the format is very free-form so probably no universal reader.  You could start with <a href="https://www.openinventor.com/">OpenInventor</a> code and maybe you can load using a demo program and save the parts you want in another format.  Or you could try <a href="https://www.mevislab.de/">Mevislab</a>, which is based on OpenInventor and has a free trial version with many options.</p>

---

## Post #6 by @lassoan (2022-12-31 03:23 UTC)

<p>I had a look at the file and it is indeed an OpenInventor file, which stores a single triangle mesh in VRML 1.0 file format. I could not find any open-source file reader for it, so <a href="https://github.com/PerkLab/SlicerSandbox/commit/14753dfb8f53e59609a5e0a46a25d02dbab2cff4">I’ve implemented a very simple reader</a> and added to the <code>Sandbox</code> extension.</p>
<p>All you need to do is to install the <code>Sandbox</code> extension tomorrow or later into Slicer-5.2 (or later). You can then load your .iv files as usual: drag-and-drop to the application window or use “Add data” window.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce12d887f3dc26e184ac74b3ee6ed9a54d3cebe7.png" data-download-href="/uploads/short-url/tp0JCOOMdoPwAxIGV4xvk1hUADR.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce12d887f3dc26e184ac74b3ee6ed9a54d3cebe7_2_690x178.png" alt="image" data-base62-sha1="tp0JCOOMdoPwAxIGV4xvk1hUADR" width="690" height="178" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce12d887f3dc26e184ac74b3ee6ed9a54d3cebe7_2_690x178.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce12d887f3dc26e184ac74b3ee6ed9a54d3cebe7_2_1035x267.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce12d887f3dc26e184ac74b3ee6ed9a54d3cebe7_2_1380x356.png 2x" data-dominant-color="5F5F6A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1996×516 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @roshans17 (2023-01-03 02:10 UTC)

<p>Wow, Andras! thank you so much for making this reader for me! I have a follow-up question and was wondering if you could give me some guidance. The main part of my question is how can I access and manipulate the polyData after it is displayed. I want to be able to create a module that has a GUI with sliders that allow the user to transform the bones based on some transformation data we have.</p>
<p>I believe the answer to my question requires an understanding of high-level slicer architecture. I have tried to look into the various tutorials (videos and powerpoints) that discuss slicer architecture; however, I feel lost as I am a fresh novice to slicer. Any thoughts as to how I should approach this specific problem and become more confident creating a slicer module?</p>
<p>Thank you in advance for all your help thus far and continued support.</p>

---

## Post #8 by @lassoan (2023-01-03 03:03 UTC)

<p>I’m glad it all works for you now. Please post a new question about the model transformation. Describe why/how you want to transform (e.g., do you want to align models, align model with an image, …).</p>

---

## Post #9 by @sulli419 (2025-03-04 23:21 UTC)

<p>I’m trying to import a .iv or .wrl file with the sandbox tool but defaults to volume and cannot open.  Is there a newer way to do this? The files were created in Imaris software, so maybe they have some proprietary stamp that prevents it from working.  Thoughts?  Thanks much, Steve</p>

---

## Post #10 by @pieper (2025-03-04 23:27 UTC)

<p>It’s probably because the format is so flexibile that it can store many types of data.  What I suggested above still holds true, about using MevisLab or OpenInventor.</p>

---
