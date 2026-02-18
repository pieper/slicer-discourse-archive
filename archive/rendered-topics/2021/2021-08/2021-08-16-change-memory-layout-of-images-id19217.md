# Change memory layout of images

**Topic ID**: 19217
**Date**: 2021-08-16
**URL**: https://discourse.slicer.org/t/change-memory-layout-of-images/19217

---

## Post #1 by @keri (2021-08-16 22:07 UTC)

<p>I’m working now with 3D <code>vtkImageData</code> with scalar set. I fill <code>vtkFloatArray</code> from pointer of <code>Eigen::Matrix</code>:</p>
<pre><code class="lang-cpp">    vtkNew&lt;vtkFloatArray&gt; array;
    array-&gt;SetArray(TRACE-&gt;data(), TRACE-&gt;size(), 1);
</code></pre>
<p>The problem is that <code>vtkImageData</code> expects that the scalar array is filled in the order: <code>X-axis</code> then <code>Y-axis</code> and only then <code>Z-axis</code>.<br>
My eigen matrix is filled differently: at first <code>Z-axis</code> then <code>Y-axis</code> and then <code>X-axis</code> (or maybe after Z goes X and only then Y).</p>
<p>As I work with quite big data (few gigabytes or at minimum few hundreds of megabytes) I wanted to avoid copying data and somehow tell to my mrmlnode (or vtkimagedata) that the scalar data has some non-standard memory order.</p>
<p>Rotations will not help me there…<br>
Maybe you have some ideas?</p>

---

## Post #2 by @lassoan (2021-08-16 22:40 UTC)

<p>VTK core supports arbitrary memory layouts but I think only a fraction of filters support it, so you can only use special memory layouts for very specific operations.</p>
<p>This C vs Fortran memory order is typically just an annoyance, something that you need to keep in mind when you cross boundaries between libraries that use different conventions. For example, this issue comes up very often with ITK/VTK vs numpy, but I don’t recall any situation that required somebody to reallocate arrays.</p>
<p>If you just want to display the volume then you can apply a transform that reorders coordinate system axes. For example, the transformation matrix to convert from KJI to IJK is:</p>
<pre><code class="lang-auto">0,0,1,0
0,1,0,0
1,0,0,0
0,0,0,1
</code></pre>
<p>By the way, resampling of a volume with reordered axes is usually a very quick operation, so it should not be perceivable for users, unless you need to keep both representations in memory and synchronize them very frequently.</p>

---
