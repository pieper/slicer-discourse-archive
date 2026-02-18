# I got shape results (such as MajorAxisLength, LeastriAxisLength) through Radiomics analysis. Can I visualize it on model with 3Dslicer?

**Topic ID**: 16817
**Date**: 2021-03-29
**URL**: https://discourse.slicer.org/t/i-got-shape-results-such-as-majoraxislength-leastriaxislength-through-radiomics-analysis-can-i-visualize-it-on-model-with-3dslicer/16817

---

## Post #1 by @jinzhi_lin (2021-03-29 13:13 UTC)

<p>I got shape results (such as MajorAxisLength, LeastriAxisLength) through Radiomics analysis. Can I visualize it on model with 3Dslicer?</p>

---

## Post #2 by @JoostJM (2021-04-12 08:05 UTC)

<p>Currently, no. Maximum diameter features are calculated as scalar values inside the C extension of PyRadiomics, which does not store the mask points that represent that value.</p>
<p>If you want to determine those points (and draw a line), you’d need to implement that algorithm yourself, though due to high number of iteration, it was moved to the C extension for performance in PyRadiomics, so be aware when you implement it in Python, it’ll be quite slow.</p>
<p>In short it works like this:<br>
let <code>mask</code> be an array containing all indices of segmented voxels (i.e. part of the ROI)</p>
<pre><code class="lang-auto">for (int i = 0; i &lt; len(mask); i ++)
{
  for (int j = i + 1; j &lt; len(mask); j++)
  {
    distance = euclidean_distance(mask[i], mask[j])
    if (distance &gt; max_distance)
    {
      max_distance = distance
      max_i = i
      max_j = j
    }
  }
}
</code></pre>
<p>Don’t forget to take pixel spacing into account when calculating the distance.<br>
The above snippet calculates a 3D max distance. If you want the maximum distance in the axial, saggital or coronal plane, add another constraint that forces the x, y or z components of <code>i</code> and <code>j</code> to be equal (equal x yields saggital, y yields coronal and z yields axial max distances).</p>

---

## Post #3 by @JoostJM (2021-04-12 08:08 UTC)

<p>Major and Least axis length are calculated using the eigenvalues (see <a href="https://github.com/AIM-Harvard/pyradiomics/blob/master/radiomics/shape.py#L79-L93">here</a>). You can use the same bit of code to also calculate the associated eigen vectors, which are the axes you are looking for.</p>
<p>So, like maximum diameters, not currently implemented. But it should be easy enough to implement yourself.</p>
<p>See also <a href="https://pyradiomics.readthedocs.io/en/latest/features.html#radiomics.shape.RadiomicsShape.getMajorAxisLengthFeatureValue">the documentation on these features</a>. If you use the eigenvectors and calculated feature values, you can generate the ROI enclosing ellipsoid and visualize it as a slicer model.</p>

---
