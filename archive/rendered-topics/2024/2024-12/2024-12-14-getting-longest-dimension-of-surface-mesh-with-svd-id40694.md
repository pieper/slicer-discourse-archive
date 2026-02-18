# Getting longest dimension of surface mesh with SVD

**Topic ID**: 40694
**Date**: 2024-12-14
**URL**: https://discourse.slicer.org/t/getting-longest-dimension-of-surface-mesh-with-svd/40694

---

## Post #1 by @evaherbst (2024-12-14 11:00 UTC)

<p>Hello,</p>
<p>I am working with vtk and np.linalg.svd to get the main axes of a surface mesh.<br>
I want to use the SVD singular values to find the longest dimensions of the model (as far as I understand, the singular values represent this).</p>
<p>The axes calculated from the SVD function look good (thanks <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> for the initial code to use the SVD for the axes)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4660e1db8db0f58b5bdcde36c48434d788eebe2.png" data-download-href="/uploads/short-url/s1qeEug4A8wpaSXMXRV200CVpZw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4660e1db8db0f58b5bdcde36c48434d788eebe2.png" alt="image" data-base62-sha1="s1qeEug4A8wpaSXMXRV200CVpZw" width="435" height="500" data-dominant-color="CE9790"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">474×544 12.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>but the singular values are way off. I am getting singular values = [191.01749 137.47546  26.27877] but based on a quick measurement I would expect the first singular value (longest dimension) to be something like 30:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/8325fed62c585a23c6dbac43680a686e2b08d669.png" data-download-href="/uploads/short-url/iIbX7jLmVRHp5ohzz3Cd0B1o74B.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/8325fed62c585a23c6dbac43680a686e2b08d669_2_377x500.png" alt="image" data-base62-sha1="iIbX7jLmVRHp5ohzz3Cd0B1o74B" width="377" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/8325fed62c585a23c6dbac43680a686e2b08d669_2_377x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/8325fed62c585a23c6dbac43680a686e2b08d669_2_565x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/8325fed62c585a23c6dbac43680a686e2b08d669.png 2x" data-dominant-color="D39D89"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">567×751 34.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My mean points look fine scale wise when I print them out.</p>
<blockquote>
<pre><code>modelPoints = vtk_to_numpy(model.GetPolyData().GetPoints().GetData())


# Calculate the mean of the points, i.e. the 'center' of the cloud
modelPointsMean = modelPoints.mean(axis=0)

print("printing model points mean")
print(modelPointsMean)
# print("Model Points:", modelPoints)  # Print the first 5 points
# Do an SVD on the mean-centered data.
uu, singular_values, rightSingularVectors = np.linalg.svd(modelPoints - modelPointsMean)
print("printing singular values")
</code></pre>
</blockquote>

---

## Post #2 by @mau_igna_06 (2024-12-14 12:14 UTC)

<p>Hi</p>
<p>Try creating an ellipsoid with vtk and using its points for the SVD. That way you’ll know if there is something wrong and exactly where</p>
<p>HIH</p>

---

## Post #3 by @lassoan (2024-12-15 22:25 UTC)

<p>You can get the principal-axes-oriented bounding box from Segment Statistics module. That provides you the position and orientation of the principal axis and the diameter along that axis.</p>
<p>The direction of the first principal axis (direction of maximal variance) is not exactly the same as direction along you can find the two farthest data points, but usually they are very similar. Probably you actually want to use the principal axis, as it is a very robust, reproducible metric (not sensitive to noise in the data) and it is also very simple and fast to compute.</p>

---

## Post #4 by @evaherbst (2025-01-26 18:12 UTC)

<p>Thank you!<br>
I resolved the lengths by projecting points into the axes from SVD and then finding the largest and smallest point along that axis.<br>
But your option is also an interesting solution, I will think about which is more optimal for my study</p>

---
