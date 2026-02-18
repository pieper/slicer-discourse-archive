# How to incorporate the old extension (e.g. FuzzySegmentation) into 3D slicer?

**Topic ID**: 8398
**Date**: 2019-09-12
**URL**: https://discourse.slicer.org/t/how-to-incorporate-the-old-extension-e-g-fuzzysegmentation-into-3d-slicer/8398

---

## Post #1 by @TingtingYu (2019-09-12 09:21 UTC)

<p>Hi,</p>
<p>I tried to use Fuzzy C-mean (FCM)  to do the segmentation but I did not found this module in the nightly-built version. However, I found an old one in version 3.6 but I do not how to incorporate it back to 3D slicer. Could you help me with that?</p>
<p>Best,<br>
Tingting</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb5721b85078245350c313a40f52031176d54eff.png" data-download-href="/uploads/short-url/t0PBwXfbeEGTIIjTirueNMydP55.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb5721b85078245350c313a40f52031176d54eff_2_492x500.png" alt="image" data-base62-sha1="t0PBwXfbeEGTIIjTirueNMydP55" width="492" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb5721b85078245350c313a40f52031176d54eff_2_492x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb5721b85078245350c313a40f52031176d54eff_2_738x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb5721b85078245350c313a40f52031176d54eff.png 2x" data-dominant-color="E2E2E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">743×754 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2019-09-12 14:20 UTC)

<p>Looks like that prototype never made it into slicer proper - the source code is still available and it should still work as a command line module (but it probably needs to ported to the latest ITK).</p>
<p><a href="http://viewvc.slicer.org/viewvc.cgi/NAMICSandBox/trunk/BrainTissueClassification/?pathrev=6314" class="onebox" target="_blank" rel="nofollow noopener">http://viewvc.slicer.org/viewvc.cgi/NAMICSandBox/trunk/BrainTissueClassification/?pathrev=6314</a></p>

---

## Post #3 by @TingtingYu (2019-09-13 08:19 UTC)

<p>Hi Steve,</p>
<p>Thank you for your quick reply. What do you mean by “command line module”? Does that mean the python interactor?  Could you give me some specific guidance on implementing “BrainTissueClassification”?</p>
<p>Best,<br>
Tingting</p>

---

## Post #4 by @pieper (2019-09-14 14:33 UTC)

<p>Hi Tingting -</p>
<p>I mean it’s a C++ executable as described in the link below.  These are simple non-interactive programs, typically for image processing using ITK.  Since the fuzzy segmentation code is a bit old, it may need to be ported to accommodate possible changes to the ITK and CMake infrastructure.  But probably the basic structure of the program is still good and can be made to work with current Slicer.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules#Command_Line_Interface_.28CLI.29" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Modules#Command_Line_Interface_.28CLI.29</a></p>
<p>Hope that helps,<br>
Steve</p>

---

## Post #5 by @TingtingYu (2019-09-16 11:29 UTC)

<p>Hi Steve,</p>
<p>Thank you for your help.I used Extension Wizard to build a new extension and then copy the source code files from the link in the folder where I put the extension (Figure 1). I also check the source code, the code includes the lines below (Figure 2). When I tried to put the extension into the path in application setting, it failed. I am wondering how to do the compiling since Figure 2 shows that “After successfully compiling the Slicer module”? How to compile the new extension? Can I use git bash?I am also confused about Figure 3, should I install visual studio?</p>
<p>Best,<br>
Tingting</p>
<p>Figure 1<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07227a0d46cbfdc7ba23a5574703717b56e14918.png" data-download-href="/uploads/short-url/117cVaIBWvnrpw26foYtNtCG0g8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07227a0d46cbfdc7ba23a5574703717b56e14918.png" alt="image" data-base62-sha1="117cVaIBWvnrpw26foYtNtCG0g8" width="690" height="290" data-dominant-color="F4F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">764×322 16.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3873382be2689a8a801b4202184600c69c2d969.png" data-download-href="/uploads/short-url/nkDuGzT7JBtJyqDb1vi9xPr3j0B.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3873382be2689a8a801b4202184600c69c2d969_2_690x249.png" alt="image" data-base62-sha1="nkDuGzT7JBtJyqDb1vi9xPr3j0B" width="690" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3873382be2689a8a801b4202184600c69c2d969_2_690x249.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3873382be2689a8a801b4202184600c69c2d969_2_1035x373.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3873382be2689a8a801b4202184600c69c2d969.png 2x" data-dominant-color="F4F3F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1304×471 27.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Figure 2 <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Module" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/Build Module - Slicer Wiki</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4399a15756ba194dba3b2c5f6de9f70965be7aa.png" data-download-href="/uploads/short-url/wyYh26NZLdAMugGfcaqzcd3ZTYu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4399a15756ba194dba3b2c5f6de9f70965be7aa.png" alt="image" data-base62-sha1="wyYh26NZLdAMugGfcaqzcd3ZTYu" width="690" height="374" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1690×918 35.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Figure 3 <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_build_an_extension_.3F" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/FAQ - Slicer Wiki</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/841fd4b2eacdac53ef57f32a10f9b5fcf04c2477.png" data-download-href="/uploads/short-url/iQPdQIv5mHHnv6kKImQ3TC1lLjV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/841fd4b2eacdac53ef57f32a10f9b5fcf04c2477.png" alt="image" data-base62-sha1="iQPdQIv5mHHnv6kKImQ3TC1lLjV" width="690" height="211" data-dominant-color="F4F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1443×442 33.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @pieper (2019-09-16 14:22 UTC)

<p>Hi Tingting -</p>
<p>It looks like you are on the right track - but yes, you definitely need a compiler and other prerequisites.  Basically the same ones you need to build Slicer itself.  Fair warning, compiling C++ code can be tricky and there is a learning curve.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Windows" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Windows</a></p>
<p>To run your own compiled CLI module it is usually best to also compile your own slicer too (don’t try to run it against a binary install).  Search the discourse archives and you’ll find advice for building Slicer.  Once that’s done compiling the CLI is easier.</p>
<p>Also, I notice you are running a non-English version of windows - this is probably okay, but avoid non-ASCII characters in file paths.</p>
<p>One final note: because all the steps are required to use custom C++ code, we typically encourage people to work with python if they can.  Stepping back even further, I’d encourage you to confirm that the fuzzy c-means approach is really critical before embarking on a potentially frustrating compilation task.</p>

---

## Post #7 by @TingtingYu (2019-09-17 11:15 UTC)

<p>Hi Steve,</p>
<p>Thank you for your help. I gave a try today. It was frustrating because I am not familiar with the compilation in windows. The reason to use fuzzy c-means is to partition the ROI into several regions based on the enhanced signal (contrast enhanced MRI - pre-contrast MRI). Is there any alternative for segmentation that I can easily used in 3D slicer?</p>
<p>Best,<br>
Tingting</p>

---

## Post #8 by @pieper (2019-09-18 15:50 UTC)

<aside class="quote no-group" data-username="TingtingYu" data-post="7" data-topic="8398">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/b38774/48.png" class="avatar"> TingtingYu:</div>
<blockquote>
<p>Is there any alternative for segmentation that I can easily used in 3D slicer?</p>
</blockquote>
</aside>
<p>With the Slicer Preview (Nightly) builds you can install python packages easily with <code>pip_install</code> (search for it in the discourse history) and this package might help:</p>
<p><a href="https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_cmeans.html" class="onebox" target="_blank" rel="noopener">https://pythonhosted.org/scikit-fuzzy/auto_examples/plot_cmeans.html</a></p>
<p>but otherwise, getting a good MR segmentation is a research topic in general.  You’ll find bookshelves full of options, some of which may or may not work with your specific data.</p>
<p>Hope that helps,<br>
Steve</p>

---

## Post #9 by @TingtingYu (2019-09-19 11:32 UTC)

<p>Hi Steve,</p>
<p>Thank you so much.Thank you for your patience. They are helpful. I think I need to learn python.</p>
<p>Best,<br>
Tingting</p>

---
