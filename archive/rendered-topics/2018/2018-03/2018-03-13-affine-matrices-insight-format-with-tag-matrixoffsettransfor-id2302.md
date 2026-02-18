# Affine matrices (Insight format) with tag MatrixOffsetTransformBase_double_3_3 cannot be loaded into Slicer anymore

**Topic ID**: 2302
**Date**: 2018-03-13
**URL**: https://discourse.slicer.org/t/affine-matrices-insight-format-with-tag-matrixoffsettransformbase-double-3-3-cannot-be-loaded-into-slicer-anymore/2302

---

## Post #1 by @mangotee (2018-03-13 11:20 UTC)

<p>After running ANTs buildtemplateparallel.sh script to create a template from several of our MRI scans, we receive multiple pairs of linear-affine matrices (<em>.txt) and deformation fields (</em>.nii.gz) that I want to load into Slicer for visualization&amp;sanity checking.<br>
Expected behaviour: drag&amp;drop the .txt affine matrix file into Slicer, and the transform gets loaded.<br>
Actual behaviour: the matrix transformation tag is not recognized by Slicer, as described in the error log:<br>
“Could not create an instance of “MatrixOffsetTransformBase_double_3_3”<br>
The usual cause of this error is not registering the transform with TransformFactory”.<br>
I have to manually change the tag “MatrixOffsetTransformBase_double_3_3” to “AffineTransform_double_3_3”, then it gets loaded correctly.</p>
<p>The full .txt content prior to the manual change is the following:<br>
<span class="hashtag">#Insight</span> Transform File V1.0<br>
<span class="hashtag">#Transform</span> 0<br>
Transform: MatrixOffsetTransformBase_double_3_3<br>
Parameters: 1.128638506675143 -0.018901975572667252 0.003732574598088019 0.05839336218683332 0.9249441890918595 0.012912029188555302 -0.0007861952948720328 -0.09741033293018547 1.2857967364097567 3.45194891887621 -1.6884605061223075 8.428466991955123<br>
FixedParameters: -2.1885326956456645 -15.230008711557268 -15.255627879066756</p>
<p>Previously (Slicer versions &lt;4.8), I was able to load these files without error, now it doesn’t work anymore. Could you please advise?</p>

---

## Post #2 by @lassoan (2018-03-13 12:08 UTC)

<p>There were 1-2 days recently when this was broken in the nightly version. It should work well in the current nightly version.</p>

---

## Post #3 by @jcfr (2018-03-13 13:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2302" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There were 1-2 days recently when this was broken in the nightly version. It should work well in the current nightly version.</p>
</blockquote>
</aside>
<p>Indeed, commit <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27035">r27035</a> fixed the regression</p>

---
