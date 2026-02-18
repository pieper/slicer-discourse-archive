# ALPACA not working

**Topic ID**: 28488
**Date**: 2023-03-21
**URL**: https://discourse.slicer.org/t/alpaca-not-working/28488

---

## Post #1 by @Gening_Dong (2023-03-21 03:53 UTC)

<p>Hi all,</p>
<p>I’m using the ALPACA in SlicerMorph to register two cardiac models. However, when I clicked “Run ALPACA”, no results were shown. (see the screenshot below)</p>
<p>Here’s my steps:</p>
<ol>
<li>load two .stl files as the target and the source model</li>
<li>use the “PseudoLMGenerator” to generate landmarks for the source model</li>
<li>run ALPACA</li>
</ol>
<p>And here is the output:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1abb4f69287fc030793b05abcfd2cb78f3ca3024.jpeg" data-download-href="/uploads/short-url/3OtIUU3ySTnJGmSoBRCPluOK6GM.jpeg?dl=1" title="Screenshot 2023-03-20 235111" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1abb4f69287fc030793b05abcfd2cb78f3ca3024_2_690x471.jpeg" alt="Screenshot 2023-03-20 235111" data-base62-sha1="3OtIUU3ySTnJGmSoBRCPluOK6GM" width="690" height="471" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1abb4f69287fc030793b05abcfd2cb78f3ca3024_2_690x471.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1abb4f69287fc030793b05abcfd2cb78f3ca3024_2_1035x706.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1abb4f69287fc030793b05abcfd2cb78f3ca3024_2_1380x942.jpeg 2x" data-dominant-color="DADAEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-03-20 235111</span><span class="informations">1980×1352 263 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>There’s an error jumped out:</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “F:/Slicer 5.2.1/NA-MIC/Extensions-31317/SlicerMorph/lib/Slicer-5.2/qt-scripted-modules/ALPACA.py”, line 448, in onRunALPACAButton<br>
self.transformMatrix = logic.estimateTransform(self.sourcePoints, self.targetPoints, self.sourceFeatures, self.targetFeatures, self.voxelSize, self.ui.skipScalingCheckBox.checked, self.parameterDictionary)<br>
File “F:/Slicer 5.2.1/NA-MIC/Extensions-31317/SlicerMorph/lib/Slicer-5.2/qt-scripted-modules/ALPACA.py”, line 1325, in estimateTransform<br>
ransac = self.execute_global_registration(sourcePoints, targetPoints, sourceFeatures, targetFeatures, voxelSize,<br>
File “F:/Slicer 5.2.1/NA-MIC/Extensions-31317/SlicerMorph/lib/Slicer-5.2/qt-scripted-modules/ALPACA.py”, line 1445, in execute_global_registration<br>
evaluation = registration.evaluate_registration(target_down, source_down, distance_threshold, np.linalg.inv(result.transformation))<br>
File “&lt;<strong>array_function</strong> internals&gt;”, line 180, in inv<br>
File “F:\Slicer 5.2.1\lib\Python\Lib\site-packages\numpy\linalg\linalg.py”, line 552, in inv<br>
ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)<br>
File “F:\Slicer 5.2.1\lib\Python\Lib\site-packages\numpy\linalg\linalg.py”, line 89, in _raise_linalgerror_singular<br>
raise LinAlgError(“Singular matrix”)<br>
numpy.linalg.LinAlgError: Singular matrix</p>
</blockquote>
<p>Does anyone have any ideas why the ALPACA is not working? Thanks in advance!</p>
<p>Best,<br>
Gening</p>

---

## Post #2 by @muratmaga (2023-03-21 04:26 UTC)

<aside class="quote no-group" data-username="Gening_Dong" data-post="1" data-topic="28488">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gening_dong/48/14706_2.png" class="avatar"> Gening_Dong:</div>
<blockquote>
<p>Does anyone have any ideas why the ALPACA is not working?</p>
</blockquote>
</aside>
<p>The error indicates RANSAC step failed to do Singular Matrix. If you can share your models it will be easier for us to troubleshoot or tell you why it failed.</p>

---

## Post #3 by @Gening_Dong (2023-03-21 04:40 UTC)

<p>Thanks for the reply! Please see below for the target and source models.</p>
<p><a href="https://drive.google.com/drive/folders/1v9oAierGHOx5GLYkLU0L3OvafjoTSpYv?usp=share_link" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1v9oAierGHOx5GLYkLU0L3OvafjoTSpYv?usp=share_link</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e4f006e600be0e52228c99518845515fe779e3e.png" data-download-href="/uploads/short-url/i1nq8E7oPUedin2E86ya7qmEz4q.png?dl=1" title="9E1A02C3411640208933B75A6458BB97.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e4f006e600be0e52228c99518845515fe779e3e.png" alt="9E1A02C3411640208933B75A6458BB97.png" data-base62-sha1="i1nq8E7oPUedin2E86ya7qmEz4q" width="690" height="0" data-dominant-color="BFCDDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">9E1A02C3411640208933B75A6458BB97.png</span><span class="informations">708×1 83 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @muratmaga (2023-03-21 05:13 UTC)

<aside class="quote no-group" data-username="Gening_Dong" data-post="3" data-topic="28488">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gening_dong/48/14706_2.png" class="avatar"> Gening_Dong:</div>
<blockquote>
<p>Thanks for the reply! Please see below for the target and source models.</p>
</blockquote>
</aside>
<p>if you skip the scaling and the projection (check mark them), ALPACA will run. However, result is not going to be usable. Models are quite different from each other and has unmatched parts (like a bifurcating structure that doesn’t exist in the other one).</p>
<p>ALPACA wasn’t never intended to work with such geometries.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2ed8e14ee0dd1f575d01c68d2edaf61b17c6ee71.jpeg" data-download-href="/uploads/short-url/6GqCSHlDj8ml1OJYW6W62ioskhz.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ed8e14ee0dd1f575d01c68d2edaf61b17c6ee71_2_601x500.jpeg" alt="image" data-base62-sha1="6GqCSHlDj8ml1OJYW6W62ioskhz" width="601" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ed8e14ee0dd1f575d01c68d2edaf61b17c6ee71_2_601x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ed8e14ee0dd1f575d01c68d2edaf61b17c6ee71_2_901x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2ed8e14ee0dd1f575d01c68d2edaf61b17c6ee71_2_1202x1000.jpeg 2x" data-dominant-color="978CA8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1390×1156 224 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Gening_Dong (2023-03-21 05:36 UTC)

<p>Thanks for the clarification! I was hoping it can register between models with different geometries by increasing the landmark density. But now I guess it won’t work. Could you please suggest any other approaches/algorithms might be able to register such geometries? Thanks much!</p>

---
