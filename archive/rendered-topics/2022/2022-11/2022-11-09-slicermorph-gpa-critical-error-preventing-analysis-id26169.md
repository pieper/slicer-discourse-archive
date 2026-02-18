# Slicermorph GPA: Critical Error preventing analysis

**Topic ID**: 26169
**Date**: 2022-11-09
**URL**: https://discourse.slicer.org/t/slicermorph-gpa-critical-error-preventing-analysis/26169

---

## Post #1 by @Madlen_Lang (2022-11-09 16:03 UTC)

<p>Operating system: Windows<br>
Slicer version: 5.0.3<br>
Expected behavior: Run GPA on PseudoLM data<br>
Actual behavior: Does not load, produces error message (below)</p>
<p>Hello,</p>
<p>I am trying to run a GPA on 40 landmarked endocasts. Landmarks represent a dense point cloud (# LM = 1232) which was created with PseudoLMGenerator and applied to a larger dataset using ALPACA.</p>
<p>I can run a GPA on the first 23 species, but when I try to add additional species OR when I try to run it on species at the bottom of the list I get an error (below). As far as I can tell, all my .fcsv files look normal and I haven’t been able to pinpoint a single species from the bottom of the list which might be causing the error. I tried rerunning the GPA on the same data with fewer landmarks (n = 491) and  reinstalling the Slicermorph extension but the same issue occurs.</p>
<p>Is there a way to resolve this?</p>
<p><strong>Error Message:</strong><br>
C:\Users\madle\AppData\Local\NA-MIC\Slicer 5.0.3\NA-MIC\Extensions-30893\SlicerMorph\lib\Slicer-5.0\qt-scripted-modules\Support\gpa_lib.py:94: RuntimeWarning: invalid value encountered in true_divide<br>
shape=shape/np.linalg.norm(shape)<br>
Traceback (most recent call last):<br>
File “C:/Users/madle/AppData/Local/NA-MIC/Slicer 5.0.3/NA-MIC/Extensions-30893/SlicerMorph/lib/Slicer-5.0/qt-scripted-modules/GPA.py”, line 1241, in onLoad<br>
self.LM.doGpa(self.skipScalingOption)<br>
File “C:/Users/madle/AppData/Local/NA-MIC/Slicer 5.0.3/NA-MIC/Extensions-30893/SlicerMorph/lib/Slicer-5.0/qt-scripted-modules/GPA.py”, line 279, in doGpa<br>
self.lm, self.mShape=gpa_lib.runGPA(self.lmOrig)<br>
File “C:\Users\madle\AppData\Local\NA-MIC\Slicer 5.0.3\NA-MIC\Extensions-30893\SlicerMorph\lib\Slicer-5.0\qt-scripted-modules\Support\gpa_lib.py”, line 125, in runGPA<br>
allLandmarkSets = procrustesAlign(allLandmarkSets[:,:,0],allLandmarkSets)<br>
File “C:\Users\madle\AppData\Local\NA-MIC\Slicer 5.0.3\NA-MIC\Extensions-30893\SlicerMorph\lib\Slicer-5.0\qt-scripted-modules\Support\gpa_lib.py”, line 142, in procrustesAlign<br>
allLandmarkSets[:,:,index] = alignShape(mean, allLandmarkSets[:,:,index])<br>
File “C:\Users\madle\AppData\Local\NA-MIC\Slicer 5.0.3\NA-MIC\Extensions-30893\SlicerMorph\lib\Slicer-5.0\qt-scripted-modules\Support\gpa_lib.py”, line 102, in alignShape<br>
u,s,v=sp.svd(np.dot(np.transpose(refShape),shape), full_matrices=True)<br>
File “C:\Users\madle\AppData\Local\NA-MIC\Slicer 5.0.3\lib\Python\Lib\site-packages\scipy\linalg_decomp_svd.py”, line 108, in svd<br>
a1 = _asarray_validated(a, check_finite=check_finite)<br>
File “C:\Users\madle\AppData\Local\NA-MIC\Slicer 5.0.3\lib\Python\Lib\site-packages\scipy_lib_util.py”, line 287, in _asarray_validated<br>
a = toarray(a)<br>
File “C:\Users\madle\AppData\Local\NA-MIC\Slicer 5.0.3\lib\Python\Lib\site-packages\numpy\lib\function_base.py”, line 603, in asarray_chkfinite<br>
raise ValueError(<br>
ValueError: array must not contain infs or NaNs</p>

---

## Post #2 by @muratmaga (2022-11-09 16:10 UTC)

<p><a class="mention" href="/u/madlen_lang">@Madlen_Lang</a> the last line suggests there are NAs or missing values in your dataset. This may come up in different ways. For example alpaca may not successfully transfer lm. As a first step, i suggest loading the models and alpaca transfer and confirm that alpaca set completed successfully for all samples</p>

---

## Post #3 by @Madlen_Lang (2022-11-09 17:38 UTC)

<p>Thank you!</p>
<p>There does appear to have been and error in the transfer of the landmarks using ALPACA. I think the software was having a hard time aligning the surfaces to place the landmarks, as some species have very disparate morphology. When I opened the files in Slicer some of the species only had one landmark visible (though there were the correct number of landmarks in the list). I was able to run the GPA on the species that did not have this issue.</p>
<p>I will be going through my surfaces and translating them into the same plane/orientation as my mean species to help the software align the surfaces.</p>

---

## Post #4 by @muratmaga (2022-11-09 19:25 UTC)

<p>When you have very disparate morphologies, single template usually is not sufficient. You can use a multi-template approach as described in this preprint (which is coincidentally accepted today to appear on Plos One, yay <a class="mention" href="/u/chz31">@chz31</a> ) <a href="https://www.biorxiv.org/content/10.1101/2022.01.04.474967v2" class="inline-onebox" rel="noopener nofollow ugc">Automated Landmarking via Multiple Templates | bioRxiv</a></p>
<p>If you don’t want to do that, as I recall you had some manual landmark on your brain endocast, you might try using the <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ProjectSemiLM#readme" rel="noopener nofollow ugc">ProjectSemiLMs</a> utility of SlicerMorph…</p>

---

## Post #5 by @Madlen_Lang (2022-11-14 19:51 UTC)

<p>After transforming all .ply into the same orientation to help the software align the endocasts I was able to use ALPACA and perform a GPA. Looking at the PCA I think that the landmark placement is still not very accurate as some species plot in unusual spaces. I will try to use MALPACA to place the landmarks and see how that goes (congrats on the newly accepted paper!).</p>
<p>I was able to convert my manual landmarks from an .landmarkascii to a .fcsv using the SlicerMorphR R package. However, the landmarks do not align with my .ply files. They appear to be smaller than the .ply and are shifted ventrolaterally relative to the endocast mesh. As they don’t align, I wont be able to use them with the ProjectSemiLMs module.</p>
<p>Thank you again,</p>

---

## Post #6 by @muratmaga (2022-11-14 22:47 UTC)

<aside class="quote no-group" data-username="Madlen_Lang" data-post="5" data-topic="26169">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/madlen_lang/48/16611_2.png" class="avatar"> Madlen_Lang:</div>
<blockquote>
<p>However, the landmarks do not align with my .ply files. They appear to be smaller than the .ply and are shifted ventrolaterally relative to the endocast mesh.</p>
</blockquote>
</aside>
<p>Sometimes it is a problem of coordinate systems. If you can share one or two of your PLY files and the original LM coordinates, I can see if there is an easy fix.</p>
<p>However, the scaling seems of is a concern. Perhaps units are not the same. What software did you use to do the landmarking?</p>

---

## Post #7 by @Madlen_Lang (2022-11-16 21:02 UTC)

<p>Hello,</p>
<p>I discovered as I was troubleshooting a geomorph surface warping issue that the function I was using to combine multiple landmarks files for a single species (combine.subets: geomorph) applies a transformation to the data (standardizes centroid size). As this is the data I was using to convert my landmarks to a .fscv format it makes sense that it did not align with my .ply file. I have decided to combine these landmarks files by hand rather than using the combine.subsets function which will most likely resolve the issue of the landmarks and the .ply not lining up.</p>
<p>Thank you for all your help,</p>
<p>Maddy</p>

---

## Post #8 by @muratmaga (2022-11-16 21:27 UTC)

<p>Glad to hear that you are figuring out. In general it is best to do the all data collection, clean and data prep in one platform and after making sure everything is correct to proceed with analysis.</p>
<p>Tjere is a utility in SlicerMorph called <code>MergeMarkups</code>(<a href="https://github.com/SlicerMorph/Tutorials/tree/main/MergeMarkups" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/MergeMarkups at main · SlicerMorph/Tutorials · GitHub</a>), that might be helpful.</p>

---
