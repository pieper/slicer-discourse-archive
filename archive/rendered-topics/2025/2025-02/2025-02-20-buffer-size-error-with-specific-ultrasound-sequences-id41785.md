# Buffer size error with specific ultrasound sequences

**Topic ID**: 41785
**Date**: 2025-02-20
**URL**: https://discourse.slicer.org/t/buffer-size-error-with-specific-ultrasound-sequences/41785

---

## Post #1 by @Bernard_Victor (2025-02-20 10:19 UTC)

<p>Hello</p>
<p>I have the following buffer size error with specific ultrasouns sequences:</p>
<blockquote>
<p>Exception thrown in event: /Users/svc-dashboard/ D/S/A/ITK/Modules/IO/GDCM/src/<br>
itkGDCMImagelO.cxx:426:<br>
ITK ERROR: GDCMimagelO(0x7f9293058e40):<br>
Buffer size 678084944 is not valid</p>
</blockquote>
<p>This is specific to 4 DICOM files out of 20. All the files were exported in the same way from a Logic e10s (GE) ultrasound machine. The same error occurs both on macOs and Ubuntu Linux (Slicer version = 5.8.0).</p>
<p>I tried reexporting the files. Same error. The sequences can be read in Horos DICOM reader. Is there something I could do please?</p>
<p>Thak you,</p>
<p>Bernard</p>

---

## Post #2 by @Bernard_Victor (2025-02-21 07:27 UTC)

<p>Hello again,</p>
<p>I further noticed that every sequence I have a problem with is &gt; 800MB. And every sequence I can open is &lt; 405 MB</p>
<p>Thank you</p>
<p>Bernard</p>

---

## Post #3 by @pieper (2025-02-21 16:47 UTC)

<p>You can start with the suggestions here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting</a></p>

---

## Post #4 by @Bernard_Victor (2025-02-25 11:38 UTC)

<p>Thank you.<br>
I cannot find a solution.<br>
I actually succeeded for 2 of 5 of my problematic filers (I diminished frame number but pyhton script then I decompressed the file (with jdcmconv -J --raw). 2 files can now be loaded while 3 are not.<br>
FIle surfer won’t install on my macbook. I have an error trying to run dicom2nifti<br>
I also tried the DICOM patcher module in 3dslicer, without success</p>
<p>This is very strange. Those files can be read normally in Horos. 20 other DICOM ultrasound files were extracted in the exact same way and can be loaded in 3dSlicer.</p>
<p>Any help would be greatly apreciated. Here is a <a href="https://drive.google.com/file/d/1NXuamGjYxJVMMryndQPKZ2k1Gi0tKygg/view?usp=sharing" rel="noopener nofollow ugc">link for one of the 3 problematic files.</a>.<br>
Thank you so much.</p>
<p>Bernard</p>

---

## Post #5 by @pieper (2025-02-26 19:04 UTC)

<p>The error you are seeing if from ITK, so you could report the issue at the ITK forum or issue tracker.  <a href="https://itk.org/">https://itk.org/</a></p>
<pre><code class="lang-auto">&gt;&gt;&gt; i = SimpleITK.ReadImage("/tmp/OCCALBOE")
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/opt/sr/python-install/lib/python3.9/site-packages/SimpleITK/extra.py", line 384, in ReadImage
    return reader.Execute()
  File "/opt/sr/python-install/lib/python3.9/site-packages/SimpleITK/SimpleITK.py", line 6218, in Execute
    return _SimpleITK.ImageFileReader_Execute(self)
RuntimeError: Exception thrown in SimpleITK ImageFileReader_Execute: /opt/sr/ITK/Modules/IO/GDCM/src/itkGDCMImageIO.cxx:426:
ITK ERROR: GDCMImageIO(0x7fb2d2fc5580): Buffer size 2785256438 is not valid
</code></pre>
<p>On the other hand, I could read the file with pydicom and could probably and you could probably extract the data that way with a script.</p>

---

## Post #6 by @Bernard_Victor (2025-02-27 17:08 UTC)

<p>I’ll do it. Thank you very much for your kind help.</p>
<p>Bernard</p>

---
