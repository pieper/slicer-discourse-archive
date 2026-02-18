# Export DICOM-SEG data

**Topic ID**: 21636
**Date**: 2022-01-26
**URL**: https://discourse.slicer.org/t/export-dicom-seg-data/21636

---

## Post #1 by @Johannes (2022-01-26 16:20 UTC)

<p>Hi everyone,</p>
<p>I cannot export DICOM SEG files from anonymized DICOM files.<br>
It works without any problems with DICOM objects that have not been anonymized.</p>
<p>As an example, this dataset from the internet can be used to reproduce the problem.</p>
<ul>
<li><a href="https://github.com/datalad/example-dicom-structural" class="inline-onebox" rel="noopener nofollow ugc">GitHub - datalad/example-dicom-structural: Example DICOM dataset for a T1w image acquisition</a></li>
</ul>
<p>I get the error message:</p>
<blockquote>
<p>Segmentation object export failed.<br>
Completed with errors:<br>
Convert ITK image(s) into DICOM Segmentation Image standard error<br>
Condition failed: Maximum VR length violated in /work Stable/S-1E-b/DCMQI/libsrc/ImageSEGConverter.cpp:112<br>
Fatal error encountered.</p>
</blockquote>
<p>Which Dicom field causes problems here?</p>

---

## Post #2 by @issakomi (2022-01-26 22:42 UTC)

<p>In particular case maybe <em>DS</em> fields cause the problem, not 100% sure. S. <a href="https://www.dclunie.com/dicom3tools/dciodvfy.html" rel="noopener nofollow ugc">dciodvfy</a>. Completely clean files are seldom, there are very often warnings, BTW.</p>
<p><code>dciodvfy /home/r/Downloads/example-dicom-structural-master/dicoms/N2D_0001.dcm</code></p>
<pre><code class="lang-auto">Warning - Value dubious for this VR - (0x0010,0x0010) PN Patient's Name  PN [1] = &lt;Jane_Doe&gt; - Retired Person Name form
Error - Value invalid for this VR - (0x0010,0x1010) AS Patient's Age  AS [1] = &lt;42&gt; - Length invalid for this VR = 2, expected == 4
Error - Value invalid for this VR - (0x0018,0x0050) DS Slice Thickness  DS [1] = &lt;0.666666686534882&gt; - Length invalid for this VR = 17, expected &lt;= 16
Error - Value invalid for this VR - (0x0018,0x0088) DS Spacing Between Slices  DS [1] = &lt;0.666666686534882&gt; - Length invalid for this VR = 17, expected &lt;= 16
Error - Value invalid for this VR - (0x0020,0x0032) DS Image Position (Patient)  DS [1] = &lt;-91.4495864331908&gt; - Length invalid for this VR = 17, expected &lt;= 16
Error - Value invalid for this VR - (0x0020,0x0032) DS Image Position (Patient)  DS [3] = &lt;-142.505487236053&gt; - Length invalid for this VR = 17, expected &lt;= 16
Error - Value invalid for this VR - (0x0020,0x0037) DS Image Orientation (Patient)  DS [1] = &lt;0.999032176441525&gt; - Length invalid for this VR = 17, expected &lt;= 16
Error - Value invalid for this VR - (0x0020,0x0037) DS Image Orientation (Patient)  DS [2] = &lt;-0.0217883751691557&gt; - Length invalid for this VR = 19, expected &lt;= 16
Error - Value invalid for this VR - (0x0020,0x0037) DS Image Orientation (Patient)  DS [3] = &lt;0.0382096472372976&gt; - Length invalid for this VR = 18, expected &lt;= 16
Error - Value invalid for this VR - (0x0020,0x0037) DS Image Orientation (Patient)  DS [4] = &lt;0.026519476938784&gt; - Length invalid for this VR = 17, expected &lt;= 16
Error - Value invalid for this VR - (0x0020,0x0037) DS Image Orientation (Patient)  DS [5] = &lt;0.991413870277297&gt; - Length invalid for this VR = 17, expected &lt;= 16
Error - Value invalid for this VR - (0x0028,0x0030) DS Pixel Spacing  DS [1] = &lt;0.666666686534882&gt; - Length invalid for this VR = 17, expected &lt;= 16
Error - Value invalid for this VR - (0x0028,0x0030) DS Pixel Spacing  DS [2] = &lt;0.699987828731537&gt; - Length invalid for this VR = 17, expected &lt;= 16
Error - Dicom dataset contains invalid data values for Value Representations
Warning - Retired attribute - (0x0010,0x1000) LO Other Patient IDs 
Warning - Dicom dataset contains retired attributes
MRImage
Error - Missing attribute Type 2C Conditional Element=&lt;Laterality&gt; Module=&lt;GeneralSeries&gt;
Error - Missing attribute Type 2C Conditional Element=&lt;PatientPosition&gt; Module=&lt;GeneralSeries&gt;
Error - Missing attribute Type 2 Required Element=&lt;PositionReferenceIndicator&gt; Module=&lt;FrameOfReference&gt;
Error - A value is required for value 3 in MR Images - attribute &lt;ImageType&gt;
Error - Missing attribute Type 1 Required Element=&lt;ScanningSequence&gt; Module=&lt;MRImage&gt;
Error - Missing attribute Type 1 Required Element=&lt;SequenceVariant&gt; Module=&lt;MRImage&gt;
Error - Missing attribute Type 2 Required Element=&lt;ScanOptions&gt; Module=&lt;MRImage&gt;
Error - Missing attribute Type 2 Required Element=&lt;MRAcquisitionType&gt; Module=&lt;MRImage&gt;
Error - Missing attribute Type 2C Conditional Element=&lt;RepetitionTime&gt; Module=&lt;MRImage&gt;
Error - Missing attribute Type 2 Required Element=&lt;EchoTime&gt; Module=&lt;MRImage&gt;
Error - Missing attribute Type 2 Required Element=&lt;EchoTrainLength&gt; Module=&lt;MRImage&gt;
Warning - Attribute is not present in standard DICOM IOD - (0x0010,0x1000) LO Other Patient IDs 
Warning - Attribute is not present in standard DICOM IOD - (0x0028,0x1052) DS Rescale Intercept 
Warning - Attribute is not present in standard DICOM IOD - (0x0028,0x1053) DS Rescale Slope 
Warning - Attribute is not present in standard DICOM IOD - (0x0028,0x1054) LO Rescale Type 
Warning - Dicom dataset contains attributes not present in standard DICOM IOD - this is a Standard Extended SOP Class
</code></pre>

---

## Post #3 by @lassoan (2022-01-27 05:06 UTC)

<p>Many errors are tolerated, but the geometry (origin, spacing, axis directions) are stored in invalid decimal string (DS) values that the DICOM writer cannot reproduce. So, it is not possible to use this messed up DICOM image as a reference image for a DICOM segmentation object.</p>
<p>I would recommend to contact the maintainers of the <a href="https://github.com/datalad/example-dicom-structural">https://github.com/datalad/example-dicom-structural</a> repository about the issue and see if they are willing to fix up the data set. At least they should describe these issues in the repository. Probably the culprit is the <code>nifti2dicom</code> utility that they used. The problem should be reported to the maintainers of <code>nifti2dicom</code>, too.</p>
<p>In the meantime, you can create a valid DICOM volume by loading the invalid DICOM into Slicer (it will tolerate it), then export it into DICOM within Slicer. Then load that DICOM volume and use that as master volume for the segmentation.</p>

---

## Post #4 by @Johannes (2022-01-27 12:06 UTC)

<p><strong>Thank you so much!!!.</strong> I will create a corresponding report.</p>
<p>The problem seems to occur with many data sets from the Internet. I couldn’t find one that would allow me to generate DICOM SEG files. Maybe because most of them created by nifti2dcm.</p>
<p><strong>Regardless, the workaround you suggested works fine!</strong></p>

---

## Post #5 by @lennart81 (2025-01-23 11:33 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> - this fix helped me a lot in getting DICOM seg files exported</p>

---
