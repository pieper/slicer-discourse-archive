# Wrong value displayed in deformation vector field

**Topic ID**: 29792
**Date**: 2023-06-02
**URL**: https://discourse.slicer.org/t/wrong-value-displayed-in-deformation-vector-field/29792

---

## Post #1 by @bqi (2023-06-02 07:29 UTC)

<p>Hi,</p>
<p>I am coding to extract the deformation vector field stored in a DICOM REG file. This file is generated and exported from ImSim QA.<br>
The size of the grid is 512<em>512</em>141. The DVF value is basically (0,0,9) on each point as I generated it. These values are also shown in ImSim QA perfectly. However, the value on each point shown in Slicer is around (0,0,3). I also tried to extract the DVF in a DIY python script, the result is similar to those shown in Slicer.</p>
<p>Here is the link to the REG file. <a href="https://drive.google.com/file/d/1qWKQu-HQIGWqNV7Q6Ukh42V2nt024VxJ/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">z 9.dcm - Google Drive</a></p>
<p>I really have no idea what is wrong. Any suggestion would be grateful!</p>
<p>Thanks.</p>

---

## Post #2 by @pieper (2023-06-03 14:59 UTC)

<p>Thanks for sharing the example.  It would be great if you could share the script you are using to look at the data.  I tried loading it in pydicom but the vector data couldn’t be loaded as numpy.  If you think the data is valid this could be good to report on the pydicom issue tracker.</p>
<pre data-code-wrap="import"><code class="lang-plaintext">d = pydicom.read_file("/tmp/z 9.dcm")
g = d.DeformableRegistrationSequence[0].DeformableRegistrationGridSequence[0]
v = g.VectorGridData
import numpy
a = numpy.array(v)
print(a.min(), a.max())
Traceback (most recent call last):
  File "&lt;string&gt;", line 7, in &lt;module&gt;
  File "/opt/sr/python-install/lib/python3.9/site-packages/numpy/core/_methods.py", line 45, in _amin
    return umr_minimum(a, axis, None, out, keepdims, initial, where)
numpy.core._exceptions._UFuncNoLoopError: ufunc 'minimum' did not contain a loop with signature matching types (dtype('S443547648'), dtype('S443547648')) -&gt; None
</code></pre>
<p>However if I look with dcmdump, it appears that the vector data is not all 0,0,9 but actually some other vectors.</p>
<pre><code class="lang-auto">0064,0005) SQ (Sequence with explicit length #=1)      # 443547772, 1 DeformableRegistrationGridSequence
      (fffe,e000) na (Item with explicit length #=5)          # 443547764, 1 Item
        (0020,0032) DS [-234.00\-234.00\-208.50]                #  24, 3 ImagePositionPatient
        (0020,0037) DS [1\0\0\0\1\0]                            #  12, 6 ImageOrientationPatient
        (0064,0007) UL 512\512\141                              #  12, 3 GridDimensions
        (0064,0008) FD 0.91404432058334351\0.91404432058334351\3 #  24, 3 GridResolution
        (0064,0009) OF 1.223783e-12\0\-0.053405762\0\0\-0.06942749\0\0\-0.087341309\0\0... # 443547648, 1 VectorGridData
</code></pre>

---

## Post #3 by @lassoan (2023-06-03 18:41 UTC)

<p>A DICOM dump shows that displacement values in the file are approximately all (0, 0, - 3). Therefore, to me it looks like Slicer loaded the transform correctly. We also tested this quite extensively when we developed the importer a number of years ago.</p>
<p>Maybe ImSimQA was confused by somehow wanting to factor in the grid spacing of 3 into the calculations? I would be surprised (and it would be very embarrassing for them), but it is possible. I would recommend to tell Imsim QA developers know about your findings. Report back here if they reply.</p>
<p>Until they get back to you, you can use Slicer to generate displacement fields. You can compute transforms from automatic intensity based image registration (e.g., using Elastix or ANTs) or landmarks (e.g., using Fiducial Registration Wizard module) and then export it to DICOM SRO. You can also do visualization and analysis, apply transforms to structure sets, compute statistics, DVH, DVH metrics, etc. using the Slicer GUI or automate or extend these features using Python scripts.</p>

---

## Post #4 by @pieper (2023-06-03 21:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="29792">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>A DICOM dump shows that displacement values in the file are approximately all (0, 0, - 3).</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> What dicom dump tool did you use?  With dcmdump I see these values:</p>
<pre><code class="lang-auto">        (0064,0009) OF 1.223783e-12\0\-0.053405762\0\0\-0.06942749\0\0\-0.087341309\0\0... # 443547648, 1 VectorGridData
</code></pre>

---

## Post #5 by @lassoan (2023-06-04 00:00 UTC)

<p>At the edge (first/last few ten thousand values) are smaller, but most of the vectors are around (0,0,-3).</p>

---

## Post #6 by @bqi (2023-06-05 07:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="29792">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can also do visualization and analysis, apply transforms to structure sets, compute statistics, DVH, DVH metrics, etc. using the Slicer GUI or automate or extend these features using Python scripts.</p>
</blockquote>
</aside>
<p>Hi,</p>
<p>Thank you so much for the discussion. I think the problem might come from unpacking the data. The data format is little endian.</p>
<pre><code class="lang-auto">#get the displacement field
dvf_vals_raw = ds.DeformableRegistrationSequence[0].DeformableRegistrationGridSequence[0].VectorGridData
#unpack it in little endian format
dvf_vals = struct.unpack(f"&lt;{len(dvf_vals_raw)//4}f", dvf_vals_raw)
</code></pre>
<p>So, the displacement is stored in dvf_vals.<br>
The answer could be a good reference. <a href="https://stackoverflow.com/questions/70170117/dicom-deformable-image-registration" class="inline-onebox" rel="noopener nofollow ugc">python - Dicom deformable image registration - Stack Overflow</a></p>
<p>Bests,<br>
Beiqian</p>

---

## Post #7 by @bqi (2023-06-05 07:31 UTC)

<p>Hi Iassoan,</p>
<p>Thank you so much for the help. I am contacting with them actively. I will get back to you once I get their reply.</p>
<p>Bests,<br>
Beiqian</p>

---

## Post #8 by @bqi (2023-06-05 12:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="29792">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maybe ImSimQA was confused by somehow wanting to factor in the grid spacing of 3 into the calculations?</p>
</blockquote>
</aside>
<p>This is the right explanation. As ImSim QA explained, the DVF stored in VectorGridData is in voxels. ‘‘To convert the DVF values to mm, one must multiply by the voxel size.’’</p>
<p>Thank you so much for the help again.</p>

---

## Post #9 by @lassoan (2023-06-05 13:26 UTC)

<p>To me it seems ImSim QA developers made mistake: they think that the vectors are in voxels, while according to the DICOM standard it is in millimeters.</p>
<p>According to the <a href="https://dicom.nema.org/medical/dicom/current/output/html/part03.html#sect_C.20.3">DICOM standard</a>, the displacement vectors are in the “Registered RCS”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93b42faacfd5da9653038c79195f054de1d86093.png" data-download-href="/uploads/short-url/l4EeAwOdve65posvemhBAa9kiNZ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93b42faacfd5da9653038c79195f054de1d86093_2_690x276.png" alt="image" data-base62-sha1="l4EeAwOdve65posvemhBAa9kiNZ" width="690" height="276" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93b42faacfd5da9653038c79195f054de1d86093_2_690x276.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93b42faacfd5da9653038c79195f054de1d86093_2_1035x414.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93b42faacfd5da9653038c79195f054de1d86093_2_1380x552.png 2x" data-dominant-color="D8D8D8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2592×1038 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>To make it more clear, I just extract one component from the highlighted matrix multiplication and vector addition:</p>
<pre><code>X_Row * X_R * i + X_Column * Y_R * j + X_Depth * Z_R * k + X_Start + DeltaX_IJK
</code></pre>
<p>For i=0, j=0, k=0 the expression simplifies to:</p>
<pre><code>X_Start + DeltaX_IJK
</code></pre>
<p>Since the vectors are added, it means <code>X_Start</code> and <code>DeltaX_IJK</code> are in the same coordinate system. The standard defines <code>X_Start</code> as “The standard coordinate, in the Registered RCS, of the deformation grid as specified in Image Position (Patient) (0020, 0032)”.</p>
<p>ImSim QA is a company working in radiation therapy quality assurance, so making such mistake would be an enormous embarrassment for them (who would ever trust their products if they make such elementary mistake?), so I’m slightly hesitant to make a final verdict.</p>
<p><strong><a class="mention" href="/u/david_clunie">@David_Clunie</a> Could you confirm that <code>Vector Grid Data</code> (0064,0009) vectors are in <code>Registered RCS</code> physical coordinate system (unit is millimeter and not voxel)?</strong></p>

---

## Post #10 by @David_Clunie (2023-06-05 13:53 UTC)

<p>Yes Andras, the encoded displacements should be in mm not voxels, as I understand the standard.</p>
<p>I agree that <a href="https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.20.3.html#equation_C.20.3-1" rel="noopener nofollow ugc">Equation C.20.3-1</a> in the standard that describes how to find the vector and then apply it seems pretty clear that the “deformation specified at index (i,j,k) in the deformation grid” is added to the coordinate without there being any multiplication by the voxel size (as distinct from finding the right entry by using the deformation grid resolution).</p>
<p>As HAL would say, “I don’t think there is any question about it.”</p>
<p>For confirmation, I suggest you ask the DICOM WG 7 (RT) and IHE-RO mailing lists, who may want to add a CP to emphasize this in the standard. You might also want to contact the vendor to see if they need to initiate a safety recall.</p>

---

## Post #11 by @lassoan (2023-06-05 14:02 UTC)

<p><a class="mention" href="/u/david_clunie">@David_Clunie</a> thank you very much for the quick answer. I also saw that you already contacted WG7 members, thanks for this amazing responsiveness!</p>
<p><a class="mention" href="/u/bqi">@bqi</a> Please report this to your ImSim QA contacts. Instead of telling their customers to “multiply by voxel size”, they must fix their software and may want to initiate a safety recall.</p>

---

## Post #12 by @David_Clunie (2023-06-05 14:12 UTC)

<p>Not sure if you still need to be on the WG-07 mailing list register to post since they changed the server, but at the very least you need to be signed up for the NEMA discourse site (<a href="https://forums.nema.org/" rel="noopener nofollow ugc">https://forums.nema.org/</a>).</p>
<p>So I sent a message to them about this just now, since they are meeting F2F in Stockholm this week and can discuss it. I will relay any useful response.</p>

---

## Post #13 by @bqi (2023-06-06 07:10 UTC)

<p>I will contact with them, and to see their following measures.</p>

---
