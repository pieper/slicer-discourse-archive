---
topic_id: 15822
title: "Cannot Import Nrrd"
date: 2021-02-03
url: https://discourse.slicer.org/t/15822
---

# Cannot import nrrd

**Topic ID**: 15822
**Date**: 2021-02-03
**URL**: https://discourse.slicer.org/t/cannot-import-nrrd/15822

---

## Post #1 by @jyhong906 (2021-02-03 20:20 UTC)

<p>Hi, this is my first time using a medical image (nrrd format)<br>
Please understand even if there is something lacking.</p>
<p>My nrrd files include ROI of ultrasound image.<br>
Before analyzing with pyradiomics, I want to use a 3D slicer to read the nrrd file. But, error occurs during the process of importing nrrd files.</p>
<pre><code class="lang-nohighlight">Slicer has caught an application error, please save your work and restart.
If you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at http://slicer.org
The message detail is:
Exception thrown in event: D:\D\S\Slicer-0-build\ITK\Modules\IO\NRRD\src\itkNrrdImageIO.cxx:290:
itk::ERROR: NrrdImageIO(0000020554C0CDB0): ReadImageInformation: Error reading C:/Users/jiyun/Desktop/51/51.nrrd:
[nrrd] nrrdLoad: trouble reading "C:/Users/jiyun/Desktop/51/51.nrrd"
[nrrd] nrrdRead: trouble
[nrrd] _nrrdRead: trouble reading NRRD file
[nrrd] _nrrdFormatNRRD_read: trouble parsing space origin info |(-0.0,0.0)|
[nrrd] _nrrdReadNrrdParse_space_origin: couldn't parse origin "(-0.0,0.0)"
[nrrd] _nrrdSpaceVectorParse: parsed 2 values, but space dimension is 3
</code></pre>
<p>The same error occurs even after removing and reinstalling the program. I don’t know what this error means. I couldn’t get the answer I wanted even though I searched.</p>
<p>Please tell me how to solve the error.<br>
Thank you.</p>

---

## Post #2 by @lassoan (2021-02-03 20:22 UTC)

<p>Since the image lives in 3D space, you need to specify all three coordinates of the origin, spacing, and axis directions, and extent. For example, it is not enough to specify <code>(0.0, 0.0)</code> but you need to write <code>(0.0, 0.0, 0.0)</code> instead.</p>

---
