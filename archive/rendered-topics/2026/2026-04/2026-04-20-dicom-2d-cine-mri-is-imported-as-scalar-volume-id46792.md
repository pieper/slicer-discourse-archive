---
topic_id: 46792
title: "DICOM 2D cine MRI is imported as Scalar Volume"
date: 2026-04-20
url: https://discourse.slicer.org/t/46792
last_bumped: 2026-04-22T05:45:55.717Z
---

# DICOM 2D cine MRI is imported as Scalar Volume

**Topic ID**: 46792
**Date**: 2026-04-20
**URL**: https://discourse.slicer.org/t/dicom-2d-cine-mri-is-imported-as-scalar-volume/46792

---

## Post #1 by @aabrown100-git (2026-04-20 21:59 UTC)

<p>I have a DICOM file containing a cine MRI on a single slice of the heart (4-chamber slice). I want this to load as a Sequence. Instead, it is loaded as a scalar volume, so that each time frame is treated as a different z-slice.</p>

---

## Post #2 by @mikebind (2026-04-21 20:13 UTC)

<p>There are suggestions for how to load DICOM as a Sequence here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html#load-dicom-file-as-sequence-node">https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html#load-dicom-file-as-sequence-node</a></p>
<p>Give that a try and post back if it doesn’t work for you.</p>

---

## Post #3 by @aabrown100-git (2026-04-21 20:29 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/522295ade09d76350cb36b0abb2956f3177f5a62.png" data-download-href="/uploads/short-url/bIBfuHh5yR2SDRHKUrNcIBIZyj8.png?dl=1" title="Screenshot 2026-04-21 at 1.26.31 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/522295ade09d76350cb36b0abb2956f3177f5a62_2_690x445.png" alt="Screenshot 2026-04-21 at 1.26.31 PM" data-base62-sha1="bIBfuHh5yR2SDRHKUrNcIBIZyj8" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/522295ade09d76350cb36b0abb2956f3177f5a62_2_690x445.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/522295ade09d76350cb36b0abb2956f3177f5a62_2_1035x667.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/522295ade09d76350cb36b0abb2956f3177f5a62_2_1380x890.png 2x" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-04-21 at 1.26.31 PM</span><span class="informations">1401×904 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thanks for sharing those suggestions. When I do that, I get this screen. It looks like the populated table only has one row, with Reader: Scalar Volume. What does this mean exactly?</p>

---

## Post #4 by @mikebind (2026-04-21 20:39 UTC)

<p>In the “DICOM plugins” section on the left, make sure that the “MultiVolumeImporterPlugin” is checked.  You can uncheck the “DICOMScalarVolumePlugin” to force it to ONLY give you Sequence/MultiVolume options, but make sure to check it again before you want to open normal (non-sequence) volumes.  If the MultiVolumeImporterPlugin is already checked, and you still aren’t getting any options for sequence loading, that means that the reader is not recognizing the input image files as part of a sequence.  There may or may not be helpful error messages at that point.</p>
<p>If there are options which appear when you click examine, you are looking for entries where the “Reader” column says MultiVolume, and where the DICOM Data column includes “as a volume Sequence” (you’ll need to expand that column so you can see more of it).  When the plugin finds things it can read, it offers to load them as a Sequence (which is what you want) or a MultiVolume (which is an older legacy version of sequences which is not what you want).  You can only tell which is which by expanding that first column.  If your screen is too small to expand it enough to be able to read it, I think the Sequences version usually comes first, then the MultiVolume version, but you can also figure it out be trial and error.</p>

---

## Post #5 by @aabrown100-git (2026-04-21 20:49 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/175c9cd326959acc36b32e907497fbfa7c90ca83.png" data-download-href="/uploads/short-url/3kFp0E6xGLzcEzW2yewDKdRukef.png?dl=1" title="Screenshot 2026-04-21 at 1.46.48 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/175c9cd326959acc36b32e907497fbfa7c90ca83_2_690x336.png" alt="Screenshot 2026-04-21 at 1.46.48 PM" data-base62-sha1="3kFp0E6xGLzcEzW2yewDKdRukef" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/175c9cd326959acc36b32e907497fbfa7c90ca83_2_690x336.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/175c9cd326959acc36b32e907497fbfa7c90ca83_2_1035x504.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/175c9cd326959acc36b32e907497fbfa7c90ca83_2_1380x672.png 2x" data-dominant-color="ECEDEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-04-21 at 1.46.48 PM</span><span class="informations">1854×904 256 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks for the instructions. I unchecked all plugins except MultiVolumeImporterPlugin and clicked examine. Nothing shows up in that table and I get Debug info that the plugin did not find loadable files. I guess there’s just something wrong with my DICOM data?</p>

---

## Post #6 by @pieper (2026-04-21 20:53 UTC)

<p>From the screenshot above, your data is what is called an “enhanced multiframe” dicom.  This means multiple slices in on file.  This is rare, but increasingly common.  It can encode many different things (dMRI, fMRI, etc) so we don’t have good parsers that sort those all out currently.  Your best bet is ether see if the source of the data can export in legacy single-frame files, or if you really need to work with this data, then roll up your sleeves and write some python code to extract the data (I don’t know how comfortable you are with that idea).</p>

---

## Post #7 by @aabrown100-git (2026-04-21 20:55 UTC)

<p>Ah interesting, thanks for the context. I think this makes sense, the data was from a quite new MRI machine. Just for my own information, how can you tell it is “enhanced multiframe” dicom?</p>

---

## Post #8 by @pieper (2026-04-21 21:51 UTC)

<p>yes, it’s a “new” variant (as in around 10 years old) but only now is being seen in the wild.</p>

---

## Post #9 by @aabrown100-git (2026-04-21 22:21 UTC)

<p>What did you see in my screenshots that told you it was “enhanced multiframe” dicom data?</p>

---

## Post #10 by @lassoan (2026-04-21 23:27 UTC)

<p>By the way, DICOM loading infrastructure is mostly Python-scripted, so if you install Visual Studio Code and open the 3D Slicer folder and ask an AI agent (the built-in Copilot or Claude, etc.) to fix it then it is quite likely that eventually it will succeed. If you can share an anonymized example we can give this a try, too.</p>

---

## Post #11 by @pieper (2026-04-21 23:52 UTC)

<aside class="quote no-group" data-username="aabrown100-git" data-post="9" data-topic="46792" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/aabrown100-git/48/82187_2.png" class="avatar"> aabrown100-git:</div>
<blockquote>
<p>What did you see in my screenshots that told you it was “enhanced multiframe” dicom data?</p>
</blockquote>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/351a44369b6a6698f820b0239ad15d34885373f6.png" data-download-href="/uploads/short-url/7zLA3whfxJ4ugdNpJ0VZOVkuKt8.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/351a44369b6a6698f820b0239ad15d34885373f6_2_690x104.png" alt="image" data-base62-sha1="7zLA3whfxJ4ugdNpJ0VZOVkuKt8" width="690" height="104" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/351a44369b6a6698f820b0239ad15d34885373f6_2_690x104.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/351a44369b6a6698f820b0239ad15d34885373f6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/351a44369b6a6698f820b0239ad15d34885373f6.png 2x" data-dominant-color="F1F1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">706×107 10.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @aabrown100-git (2026-04-22 00:29 UTC)

<p>Thanks! I was able to convert the data into a sequence using a Slicer Python script (with AI help). I guess this is a bit different from directly reading this DICOM data as a sequence? But my solution is good enough for me for now.</p>

---

## Post #13 by @lassoan (2026-04-22 00:35 UTC)

<p>Great! You can ask the AI chatbot to create a DICOM import plugin for it (similar to the <code>DICOMVolumeSequencePlugin.py</code> and <code>DICOMScalarVolumePlugin.py</code>). Then you could load these images directly from the DICOM browser. If it works then you could consider sharing it (we could add it to the Sandbox extension, or maybe even to Slicer core if the implementation is clean and simple).</p>

---

## Post #14 by @aabrown100-git (2026-04-22 05:45 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Great suggestion, I used Claude Code to write a DICOM import plugin that handles this case. Let me know what you think!</p>
<p>Plugin: <a href="https://gist.github.com/aabrown100-git/f032b8eedd5833ca2645bca87422f26e" rel="noopener nofollow ugc">https://gist.github.com/aabrown100-git/f032b8eedd5833ca2645bca87422f26e</a></p>
<p>Anonymized Test Data: <a href="https://drive.google.com/file/d/1v5iC1jJMLXo94wUBbuCdvXhd6w96iAdn/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1v5iC1jJMLXo94wUBbuCdvXhd6w96iAdn/view?usp=sharing</a></p>
<p>Tested on Slicer 5.11.</p>

---
