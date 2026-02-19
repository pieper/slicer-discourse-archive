---
topic_id: 11747
title: "Converting Transform H5 To Cmtk Xform"
date: 2020-05-28
url: https://discourse.slicer.org/t/11747
---

# Converting transform.h5 to cmtk .xform

**Topic ID**: 11747
**Date**: 2020-05-28
**URL**: https://discourse.slicer.org/t/converting-transform-h5-to-cmtk-xform/11747

---

## Post #1 by @HugoTrentesaux (2020-05-28 14:00 UTC)

<p>Is there a builtin way for converting the transform.h5 file made by 3DSlicer to a xform file as produced by cmtk?</p>
<p>Here is an example of <em>the same transformation</em> in both formats:</p>
<pre><code class="lang-auto">&gt;&gt; h5read('slicer_transform.h5', '/TransformGroup/0/TranformParameters')

ans =

    1.0430
   -0.0198
   -0.0326
    0.0144
    1.0304
   -0.1652
    0.0353
    0.1646
    1.0300
  -97.7032
 -194.5304
 -243.7022
</code></pre>
<pre><code class="lang-bash">$ cat cmtk_transform.xform/registration 
! TYPEDSTREAM 2.4

registration {
	reference_study "target.nrrd"
	floating_study "source.nrrd"
	affine_xform {
		xlate -101.8 -205.9 -143.7 
		rotate 9.031949273 -1.921484041 -0.7885958359 
		scale 1.04498569 1.044250032 1.040359656 
		shear -8.001045526e-05 -0.0002715663214 -0.001942363876 
		center 282.2 512.7 187.7 
	}
}
</code></pre>
<p>(note the ‘s’ of “transform” is really missing in the hdf5 dataset name)</p>
<p>Here, the cmtk transform was produced by mapping the source image on the target image produced by slicer resampling. The fit is perfect.</p>

---

## Post #2 by @lassoan (2020-05-28 16:41 UTC)

<p>cmtk should be able to read a linear transform from a 4x4 matrix. I have never used cmtk, but found this method by a quick web search, which may work: <a href="https://rdrr.io/cran/nat/man/affmat2cmtkparams.html">https://rdrr.io/cran/nat/man/affmat2cmtkparams.html</a>.</p>

---

## Post #3 by @HugoTrentesaux (2020-05-29 15:31 UTC)

<p>You’re right. This is a bash script using <code>cmtk mat2dof</code> for somebody who would like to do the same thing (thanks <span class="mention">@vbormuth</span>):</p>
<pre><code class="lang-bash">#!/bin/bash
# 1) Perform a landmark registration in 3D slicer.
# 2) Save the transformation as *.txt file.
# 3) Call slicer2cmtk as follows
#    slicer2cmtk Slicer_Transformation.txt Slicer2cmtk.xform

if [ $# -ne 2 ]
then
echo "Usage: slicer2cmtk Slicer_Transformation.txt Slicer2cmtk.xform
Transforms the slicer transformation matrix into a cmtk xform"
else
awk 'NR==4 {print $2 , $5 , -$8 , "0\n" , $3 , $6 , -$9 , "0\n" , -$4 , -$7 , $10, "0\n" , -$11 , -$12 , $13 , "1"}' &lt; $1 | cmtk mat2dof -o ${2}/registration
fi
</code></pre>
<p>(note the minus sign on some values)</p>

---
