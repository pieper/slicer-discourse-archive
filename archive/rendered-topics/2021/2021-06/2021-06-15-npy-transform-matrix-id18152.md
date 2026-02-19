---
topic_id: 18152
title: "Npy Transform Matrix"
date: 2021-06-15
url: https://discourse.slicer.org/t/18152
---

# Npy transform matrix

**Topic ID**: 18152
**Date**: 2021-06-15
**URL**: https://discourse.slicer.org/t/npy-transform-matrix/18152

---

## Post #1 by @sfglio (2021-06-15 21:25 UTC)

<p>When saving a transformation matrix in python as .npy or .txt, I get a different position in slicer when applying the transformation to a model node. I assume that there is a problem due to different coordinate system but I thought that slicer would handle itk and thus convert my transform matrix.</p>
<p>I failed to update a segmentation node in slicer using np.load however I have the same matrix also as txt and it did not work.</p>
<p>Do you have any suggestions?</p>

---

## Post #2 by @lassoan (2021-06-16 17:35 UTC)

<p>Slicer uses all data in LPS coordinate system in files (following conventions set by DICOM, ITK, and most other modern medical image computing software), while uses RAS in the scene (for backward compatibility). You need to apply LPS&lt;-&gt;RAS basis transform if you import an LPS transform as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#convert-between-itk-and-slicer-linear-transforms">here</a>. You also need to be aware of the transform direction (modeling/resampling; from/to parent).</p>

---

## Post #3 by @sfglio (2021-06-16 21:07 UTC)

<p>Thank you for your reply!!!<br>
I tried to find a solution for the index error however when I do exactly like in the respository mentioned I get the following:</p>
<blockquote>
<blockquote>
<blockquote>
<p>m = np.array( tfm_file.splitlines()[3].split()[1:], dtype=np.float64 )</p>
</blockquote>
</blockquote>
</blockquote>
<p>Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>IndexError: list index out of range</p>
<p>Do you know how to fix that?</p>

---

## Post #4 by @lassoan (2021-06-16 22:35 UTC)

<p>The example code works for the example transform file. If your transform has a different format then you need to adjust the script. For example, if the parameters are not in the 4th line of the string then change <code>[3]</code>.</p>
<p>If you already extracted a 4x4 matrix then skip the transform file parsing (the first few lines) and just call the <code>itktfm_to_slicer</code> method.</p>

---

## Post #5 by @sfglio (2021-06-17 20:50 UTC)

<p>The problem was that I linked to the file however did not read the content of tfm file.</p>
<p>But I am still frustrated by the fact that when I copy the 4x4 matrix from cloudcompare (where I aligned two STL models) and import it to slicer, the transformation does not work.</p>
<p>Is a different software using a different coordinate system???</p>

---

## Post #6 by @lassoan (2021-06-18 23:45 UTC)

<p>The two main coordinate system conventions in medical image computing are LPS and RAS. LPS has practically won, but for backward compatibility reasons RAS is still used in software that placed its bet on RAS (such as Slicer).</p>
<p>Conversion of a transformation matrix from LPS to RAS is trivial:</p>
<pre><code class="lang-python">transform_ras = np.diag([-1, -1, 1, 1]) @ transform_lps @ np.diag([-1, -1, 1, 1])
</code></pre>
<p>A complete example to parse CloudCompare output, convert to RAS, and write it into a new transform node:</p>
<pre><code class="lang-python">registrationInfo="""---------------------------
Register info
---------------------------
Final RMS: 5.11411e-5 (computed on 50000 points)
----------------
Transformation matrix
0.632	0.684	-0.365	-28.784
-0.774	0.576	-0.263	17.832
0.030	0.448	0.893	25.578
0.000	0.000	0.000	1.000
----------------
Scale: fixed (1.0)
----------------
Theoretical overlap: 100%
----------------
This report has been output to Console (F8)
---------------------------
OK   
---------------------------
"""

# Get LPS-&gt;LPS registration matrix as numpy array
import numpy as np
transformValues_lps = '\t'.join(registrationInfo.splitlines()[6:10]).split()
transform_lps = np.array(transformValues_lps, dtype=np.float64 ).reshape(4, 4)

# Convert LPS-&gt;LPS registration matrix to RAS-&gt;RAS registration matrix
transform_ras = np.diag([-1, -1, 1, 1]) @ transform_lps @ np.diag([-1, -1, 1, 1])

# Save transform into a new transform node
transformNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLinearTransformNode", "RegistrationResult")
transformNode.SetMatrixTransformToParent(slicer.util.vtkMatrixFromArray(transform_ras))
</code></pre>
<p>Note that Slicer has lots of registration tools, so it should not be necessary to use CloudCompare. Have a look at <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">this page</a> for a quick overview. There are many other, more specialized registration tools, too. Let us know if you were interested in having your complete workflow implemented in Slicer.</p>

---
