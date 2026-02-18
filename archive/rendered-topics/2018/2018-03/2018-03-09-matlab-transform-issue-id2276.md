# Matlab transform issue

**Topic ID**: 2276
**Date**: 2018-03-09
**URL**: https://discourse.slicer.org/t/matlab-transform-issue/2276

---

## Post #1 by @muratmaga (2018-03-09 19:09 UTC)

<p>I am quite confused. I have a .mat that I want to apply bunch of points. Slicer does it correctly. This is the transform that it displays in the Information tab:</p>
<p>Transform to parent:</p>
<pre><code class="lang-auto">0.999281 0.0298646 -0.0233499 -9.08338 
-0.026954 0.992844 0.116332 15.7514 
0.026657 -0.115619 0.992936 27.7003 
0 0 0 1 
</code></pre>
<p>When I read the same transform into readMat function of R.matlab package, this is what I get:</p>
<pre><code class="lang-auto">&gt; X
$AffineTransform.float.3.3
             [,1]
 [1,]  0.99928123
 [2,] -0.02695397
 [3,] -0.02665700
 [4,]  0.02986464
 [5,]  0.99284458
 [6,]  0.11561931
 [7,]  0.02334986
 [8,] -0.11633231
 [9,]  0.99293584
**[10,]  1.79939485**
**[11,] -2.39244556**
**[12,]  0.75802612**

$fixed
          [,1]
[1,] -108.9425
[2,] -275.4168
[3,] -114.8110

attr(,"header")
attr(,"header")$version
[1] "4"
attr(,"header")$endian
[1] "little"
</code></pre>
<p>I can correct the sign issues due to LPS/RAS difference, but why is the translation so different? How do I rearrange the matlab transform to match the 4x4 transform I see in Slicer? This is the link to the transform if it helps.<br>
<a href="https://app.box.com/s/j0zpgwwjhok99i0eu1nxwf0gp1tb31fi" class="onebox" target="_blank" rel="nofollow noopener">https://app.box.com/s/j0zpgwwjhok99i0eu1nxwf0gp1tb31fi</a></p>

---

## Post #2 by @lassoan (2018-03-09 21:14 UTC)

<p>It is not just LPS/RAS conversion but also modeling/resampling transform difference. See explanation and conversion code here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Transform_files" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Transform_files</a></p>

---

## Post #3 by @ihnorton (2018-09-25 19:59 UTC)

<p>I just had to explain this to someone (and re-explain to myself), so I added a Python example I used, below the C++ snippet at your link.</p>
<p>I also edited the following (similar) FAQ entry to try to make the wording clearer, and added a link to the discussion in the Transforms documentation:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/Registration#The_registration_transform_file_saved_by_Slicer_does_not_seem_to_match_what_is_shown" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/Registration#The_registration_transform_file_saved_by_Slicer_does_not_seem_to_match_what_is_shown</a></p>

---
