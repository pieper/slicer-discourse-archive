# Unable to run PlaceSemiLMPatches due to missing function?

**Topic ID**: 29048
**Date**: 2023-04-21
**URL**: https://discourse.slicer.org/t/unable-to-run-placesemilmpatches-due-to-missing-function/29048

---

## Post #1 by @Maria_Feiler (2023-04-21 14:20 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> There seems to be an issue concerning the PlaceSemiLMPatches module in SlicerMorph. I have organized my files as described in the help files, but I receive the following errors when trying to place my patches on the rest of the specimens.</p>
<blockquote>
<p>Traceback (most recent call last):</p>
<p>File “C:/Users/maria/AppData/Local/NA-MIC/Slicer 5.0.3/NA-MIC/Extensions-30893/SlicerMorph/lib/Slicer-5.0/qt-scripted-modules/PlaceSemiLMPatches.py”, line 176, in onApplyButton</p>
<pre><code>logic.run(self.meshDirectory.currentPath, self.landmarkDirectory.currentPath, self.gridFile.currentPath,
</code></pre>
<p>File “C:/Users/maria/AppData/Local/NA-MIC/Slicer 5.0.3/NA-MIC/Extensions-30893/SlicerMorph/lib/Slicer-5.0/qt-scripted-modules/PlaceSemiLMPatches.py”, line 216, in run</p>
<pre><code>landmarkNumber=landmarkNode.GetNumberOfControlPoints()
</code></pre>
<p>AttributeError: ‘list’ object has no attribute ‘GetNumberOfControlPoints’</p>
</blockquote>
<p>Here is a <a href="https://drive.google.com/drive/folders/1je5I-RH2fXHzEYzQaK6m_iSQgmPq5j7y?usp=share_link" rel="noopener nofollow ugc">google drive folder</a> of a few representative specimens and landmarks organized as I have on my computer. The patch template was created on specimen W037. Any help would be appreciated!</p>

---

## Post #2 by @muratmaga (2023-04-21 15:00 UTC)

<p>Thank you for reporting. I can repllicate the issue. Will post an update when we fix it.<br>
<a class="mention" href="/u/smrolfe">@smrolfe</a></p>

---

## Post #3 by @smrolfe (2023-04-21 19:15 UTC)

<p><a class="mention" href="/u/maria_feiler">@Maria_Feiler</a> Thanks, we have fixed this issue on our <a href="https://github.com/SlicerMorph/SlicerMorph" rel="noopener nofollow ugc">repo</a>. You can update from there, or from the extension manager after the next nightly build.</p>

---

## Post #4 by @muratmaga (2023-04-21 19:26 UTC)

<p><a class="mention" href="/u/maria_feiler">@Maria_Feiler</a></p>
<p>I noticed that you are using an old stable (5.0.3). Please switch to the newest stable (5.2.2) and then download the slicermorph extension tomorrow. With the stable versions, you can easily update the SlicerMorph to its latest version, but this is only available for the most recent stable build (which is 5.2.2).</p>

---

## Post #5 by @Maria_Feiler (2023-04-24 23:50 UTC)

<p>Thank you <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/smrolfe">@smrolfe</a> for giving this a look! Unfortunately, there seem to be more problems with the program even with the most updated Slicer and SlicerMorph. When I run the program using the files in the folder shared previously, it runs but places the patches in seemingly random places. I even tried making a new grid connectivity file using patches near the incisors, but it placed the patches on the top of the head (even for the reference specimen). Any ideas?</p>

---

## Post #6 by @muratmaga (2023-04-25 02:20 UTC)

<p>This is what I got from your samples (W037). It seems correct to me. This is slicer 5.2.2 on windows, after updating the SlicerMorph extension.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9de7d5326c382ec08d014a3051e67038fdb1020.jpeg" data-download-href="/uploads/short-url/v5mi9kvXKJs7rv418wvkn58OQy4.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9de7d5326c382ec08d014a3051e67038fdb1020_2_458x500.jpeg" alt="image" data-base62-sha1="v5mi9kvXKJs7rv418wvkn58OQy4" width="458" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9de7d5326c382ec08d014a3051e67038fdb1020_2_458x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9de7d5326c382ec08d014a3051e67038fdb1020_2_687x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9de7d5326c382ec08d014a3051e67038fdb1020_2_916x1000.jpeg 2x" data-dominant-color="A8A884"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1066×1163 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @muratmaga (2023-04-25 02:21 UTC)

<p>Also if you are going to use this many semiLMs, perhaps consider using PseudoLMgenerator, which will allow you more uniformly sample. Then you can use the ProjectSemiLMPatches (insted of placepatches you are using) to transfer them.</p>

---

## Post #8 by @muratmaga (2023-04-25 02:30 UTC)

<p>We have an SlicerMorph online office hour tomorrow at 11 (PT), where we can take a look if it works for you. DM me or email for link if you want to attend.</p>

---

## Post #9 by @muratmaga (2023-04-25 04:13 UTC)

<p>Here is an example. Takes about 3 minutes or so… You can sample more or less densely, and remove the unnecessary/unwanted points (such as on teeth) with markupsEditor plugin.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcdd13c8b49c1b567f5e2081f0bd08cd0e7003e8.jpeg" data-download-href="/uploads/short-url/A4VYF8yvHc6Ad8pIxg0qg2YMgYw.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcdd13c8b49c1b567f5e2081f0bd08cd0e7003e8_2_538x500.jpeg" alt="image" data-base62-sha1="A4VYF8yvHc6Ad8pIxg0qg2YMgYw" width="538" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcdd13c8b49c1b567f5e2081f0bd08cd0e7003e8_2_538x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcdd13c8b49c1b567f5e2081f0bd08cd0e7003e8_2_807x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcdd13c8b49c1b567f5e2081f0bd08cd0e7003e8_2_1076x1000.jpeg 2x" data-dominant-color="A6A785"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1302×1208 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
