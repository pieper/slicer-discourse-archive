# BUG when reading mha file with AnatomicalOrientation

**Topic ID**: 7038
**Date**: 2019-06-05
**URL**: https://discourse.slicer.org/t/bug-when-reading-mha-file-with-anatomicalorientation/7038

---

## Post #1 by @agirault (2019-06-05 16:15 UTC)

<p>I’m working on adding support for orientation in VTK image data and what depends on it (filters, mappers, IO… more details <a href="https://gitlab.kitware.com/vtk/vtk/issues/17480" rel="noopener nofollow ugc">here</a>).</p>
<p>I was working on the <a href="https://itk.org/Wiki/ITK/MetaIO/Documentation" rel="noopener nofollow ugc">MetaIO</a> (.mha, .mhd) reader and tested using a sample dataset with the following header:</p>
<pre><code class="lang-auto">ObjectType = Image
NDims = 3
BinaryData = True
BinaryDataByteOrderMSB = False
CompressedData = True
CompressedDataSize = 1486837
TransformMatrix = 1 7.5286998857393448e-16 4.3888503942213362e-16 7.4766581814600425e-16 -1 -3.8487811825327185e-47 0 0 -1
Offset = -9.360019529721862e-29 360.00000000000006 332.5
CenterOfRotation = 0 0 0
AnatomicalOrientation = RPS
ElementSpacing = 1.4062499999999947 1.4062500000000002 2.4999999999999813
DimSize = 256 256 133
ElementType = MET_UCHAR
ElementDataFile = LOCAL
</code></pre>
<p>Note that the anatomical orientation for this file is <code>RPS</code>, spacing is ~ [1.4, 1.4, 2.5] and the orientation matrix is, after rounding:<br>
1  0  0<br>
0 -1  0<br>
0  0 -1</p>
<p>In VTK the system is XYZ=LPS, so after flipping the first axis, the orientation matrix becomes, in LPS:<br>
-1  0  0<br>
0 -1  0<br>
0  0 -1</p>
<p>Now… I use 3DSlicer as the ground truth in term of orientation when I test things for VTK, and the data read in my VTK example with the MHA reader was flipped along the Sagittal axis (L/R) compared to 3D Slicer…</p>
<p>I then proceed to export the dataset to NRRD from Slicer, and this is the resulting header:</p>
<pre><code class="lang-auto">NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: unsigned char
dimension: 3
space: left-posterior-superior
sizes: 256 256 133
space directions: (1.4062499999999947,1.0587234214320913e-15,6.171820866873731e-16) (1.0514050567678187e-15,-1.4062500000000002,-5.4123485379366359e-47) (0,0,-2.4999999999999813)
kinds: domain domain domain
encoding: gzip
space origin: (-9.360019529721862e-29,360.00000000000006,332.5)
</code></pre>
<p>With rounding, the direction matrix here is:<br>
1.4   0    0<br>
0  -1.4   0<br>
0     0  -2.5</p>
<p>If we extract the spacing (1.4, 1.4, 2.5) we get:<br>
1  0  0<br>
0 -1  0<br>
0  0 -1</p>
<p>That’s the same as in the MHA header… however, the <code>space</code> is now <code>left-posterior-superior</code> instead of <code>RPS</code> in MHA: here we find the flip along the X-axis again.</p>
<p>So two possible reasons:</p>
<ol>
<li>MHA reader is incorrect</li>
<li>NRRD writer is incorrect</li>
</ol>
<p>Given that my VTK implementation gives me a flip from the one loaded by Slicer, my guess is on number 1. I followed up by looking at <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/0b1f2da/Modules/IO/Meta/src/itkMetaImageIO.cxx" rel="noopener nofollow ugc">itkMetaImageIO</a> and there are numerous mentions of <code>AnatomicalOrientation</code> in <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/0b1f2da/Modules/IO/Meta/src/itkMetaImageIO.cxx#L820-L1062" rel="noopener nofollow ugc"><code>MetaImageIO::Write</code></a>, but none in <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/0b1f2da/Modules/IO/Meta/src/itkMetaImageIO.cxx#L390-L402" rel="noopener nofollow ugc"><code>MetaImageIO::Read</code></a>.</p>
<p>Based on all this, would you all agree we are indeed ignoring the anatomical orientation when reading MHA/MHD files?</p>
<p>cc: <a class="mention" href="/u/dzenanz">@dzenanz</a> <a class="mention" href="/u/thewtex">@thewtex</a></p>

---

## Post #2 by @pieper (2019-06-05 18:05 UTC)

<p>Hi <a class="mention" href="/u/agirault">@agirault</a> - yes, this has come up a couple of times.  I believe the post from Andras sums up the current understanding.</p>
<aside class="quote quote-modified" data-post="2" data-topic="3389">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/import-mhd-data/3389/2">Import mhd data</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Slicer uses ITK image reader to load metaimage files. This reader intentionally ignores AnatomicalOrientation (I’ve raised this question before to ITK developers and Kitware and they confirmed that this is not a bug and they will not change the behavior) and considers the image to be in LPS coordinate system. Slicer converts the image to RAS when it is loaded into the scene, and Slicer converts it back to LPS when it is saved to file. 
If you want to specify coordinate system using anatomical ax…
  </blockquote>
</aside>


---

## Post #3 by @agirault (2019-06-05 18:44 UTC)

<p>Right on, thank you Steve.</p>
<aside class="quote no-group quote-modified" data-username="pieper" data-post="2" data-topic="7038">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>This reader intentionally ignores AnatomicalOrientation (I’ve raised this question before to ITK developers and Kitware and they confirmed that this is not a bug and they will not change the behavior)</p>
</blockquote>
</aside>
<p>Well… we probably won’t have that in VTK, and I’m afraid that is going to confuse more than one. I don’t understand why it has to be like this in ITK: any of its maintainers would like to explain the argument (<a class="mention" href="/u/dzenanz">@dzenanz</a>, <a class="mention" href="/u/thewtex">@thewtex</a>)?</p>
<p>Thanks!</p>

---

## Post #4 by @lassoan (2019-06-05 19:08 UTC)

<p>I agree, I don’t like having this standard field for “informational purposes” only (that readers should ignore), especially because similar field in nrrd is actually used by the readers.</p>
<p>However, I understand the reluctance in investing more time into improving the file format, as there are already too many file formats (metaio, nrrd, nifti, mgz, …) for storing biomedical images in research applications. It would be probably better if we would focus on maintenance and improvement of a single file format.</p>

---

## Post #6 by @agirault (2019-06-06 18:58 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="3389">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/import-mhd-data/3389/2">Import mhd data</a></div>
<blockquote>
<blockquote>
<p>Does the <strong>TransformationMatrix</strong> specify rotation between (i,j,k) and the RAS coordinate?</p>
</blockquote>
<p>Yes.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> in the other thread linked above, you mention that the TransforMatrix (is that different from the Orientation field?) is a rotation from ijk to RAS. However, when saved as a NRRD, the transformation matrix is the same, but in LPS, as shown above. So either:</p>
<ol>
<li>the actual transform is IJKtoRAS but IJKtoLPS</li>
<li>is is IJKtoRAS but we read it as IJKtoLPS</li>
</ol>
<p>Would you agree?</p>
<p>Also, I’m currently updating those readers &amp; writers in VTK. What do you suggest I do for MetaIO?</p>
<ol>
<li>Same as NRRD (use the AnatomicalOrientation as the target coordinate system)</li>
<li>enforce as LPS (do nothing)</li>
<li>enforce as RAS (flip I and J)</li>
</ol>

---

## Post #7 by @agirault (2019-06-06 19:57 UTC)

<p>After discussion with <a class="mention" href="/u/thewtex">@thewtex</a> and <a class="mention" href="/u/aylward">@aylward</a>, we agreed that the current integration of MetaIO inside ITK is incorrect, namely:</p>
<ol>
<li>The reader ignores the anatomical orientation and assumes the data is always in LPS. It should instead adjust the orientation matrix described in the file to go from IJK to LPS if the anatomical orientation differs from LPS</li>
<li>The writer uses the direction matrix to infer an anatomical orientation (somehow?). It should instead write LPS and the associated direction matrix in that space.</li>
</ol>
<p>As a result:</p>
<ul>
<li>We’ve agreed that this will need to be fixed in ITK.</li>
<li>VTK will properly use those fields when adding orientation support.</li>
</ul>

---

## Post #8 by @agirault (2019-06-12 22:24 UTC)

<p>FYI: an attempt at updating the MetaIO reader and writer in VTK can be found here: <a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/5656" rel="nofollow noopener">https://gitlab.kitware.com/vtk/vtk/merge_requests/5656</a></p>

---

## Post #9 by @agirault (2020-08-12 13:33 UTC)

<p>For the sake of cross-referencing/documenting, the change was NOT implemented as suggested in the last two comments, following a discussion that occurred in the ITK issue tracker: <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/1017" rel="nofollow noopener">https://github.com/InsightSoftwareConsortium/ITK/issues/1017</a></p>

---
