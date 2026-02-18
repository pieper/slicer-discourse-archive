# How to read the value of certain attribute (tag) in DICOM Metadata" from "Python Interactor"

**Topic ID**: 7184
**Date**: 2019-06-16
**URL**: https://discourse.slicer.org/t/how-to-read-the-value-of-certain-attribute-tag-in-dicom-metadata-from-python-interactor/7184

---

## Post #1 by @shahrokh (2019-06-16 09:16 UTC)

<p>Hi Dears 3DSlicer developers</p>
<p>After loading dicom files using DICOM module, how can I access the value of certain attribute (tag) in “DICOM Metadata” from Python Interactor?</p>
<p>For example, I want to access the value of IsocenterPosition with the tag number (300a,012c) from Python Interactor. How can I do that?</p>
<p>Please guide me,<br>
Thanks a lot.<br>
Shahrokh.</p>

---

## Post #2 by @pieper (2019-06-16 19:52 UTC)

<p>Hi -</p>
<p>Here are some examples - let us know if this doesn’t cover your use case.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#DICOM_2" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#DICOM_2</a></p>

---

## Post #3 by @shahrokh (2019-06-17 09:20 UTC)

<p>Hi Steve</p>
<p>Thanks a lot for sending to me the link to ScriptRepository.</p>
<p>I can access to tags such as (0020,0010) to (300a,000c), but unfortunately I can not read tags that are located in <strong>item</strong>, such as (300a,012c), highlighted in the following figure.</p>
<p>The following figure is screenshot of DICOM File Browser and the tag that I want to access its value  (300a,012c).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af7e3228f4a789c677a3aa305dcba7569485423b.png" data-download-href="/uploads/short-url/p2tVIic0nJhsq02qPY1tP464UGL.png?dl=1" title="Screenshot%20from%202019-06-17%2011-58-27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af7e3228f4a789c677a3aa305dcba7569485423b_2_690x418.png" alt="Screenshot%20from%202019-06-17%2011-58-27" data-base62-sha1="p2tVIic0nJhsq02qPY1tP464UGL" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af7e3228f4a789c677a3aa305dcba7569485423b_2_690x418.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af7e3228f4a789c677a3aa305dcba7569485423b_2_1035x627.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af7e3228f4a789c677a3aa305dcba7569485423b_2_1380x836.png 2x" data-dominant-color="F3F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202019-06-17%2011-58-27</span><span class="informations">1440×873 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I enter the following commands:<br>
&gt;&gt;&gt; patientList=db.patients()<br>
&gt;&gt;&gt; studyList=db.studiesForPatient(patientList[0])<br>
&gt;&gt;&gt; seriesList=db.seriesForStudy(studyList[0])<br>
&gt;&gt;&gt; fileList=db.filesForSeries(seriesList[0])<br>
&gt;&gt;&gt; print(db.fileValue(fileList[0],‘300a,000c’))<br>
PATIENT<br>
&gt;&gt;&gt; print(db.fileValue(fileList[0],‘300a,012c’))</p>
<pre><code>&gt;&gt;&gt;
</code></pre>
<p>As you see, the last command dose not give any output.<br>
Please guide me to access tags that are loacted in <strong>Items</strong>.<br>
Thanks a lot.<br>
Shahrokh.</p>

---

## Post #4 by @pieper (2019-06-17 12:50 UTC)

<p>Hi Shahrokh -</p>
<p>Ah, sorry - you are right, the database doesn’t cache nested tags, only top level ones.</p>
<p>I added a new section to the script repository showing how to access nested tags using pydicom.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_access_DICOM_tags_nested_in_a_sequence" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_access_DICOM_tags_nested_in_a_sequence</a></p>
<p>-Steve</p>

---

## Post #5 by @shahrokh (2019-06-17 13:41 UTC)

<p>Hi Dear Steve<br>
Thank you very much for the link you provided. I study it now.<br>
But I accidentally solved my problem according to the description given on the site of <a href="https://pydicom.github.io/pydicom/0.9/pydicom_user_guide.html" rel="nofollow noopener">Pydicom User Guide — pydicom 1.0a documentation</a>.</p>
<p>In JupyterLab, I enter the following commands:</p>
<pre><code>[1]: import pydicom
[2]: ds = dicom.read_file("112325-00000000.dcm")
[3]: ds
...
(300a, 00b0)  Beam Sequence   2 item(s) ---- 
   (300a, 00b2) Treatment Machine Name              SH: 'Compact'
   ...
   (300a, 0111)  Control Point Sequence   2 item(s) ---- 
      (300a, 0112) Control Point Index                 IS: "0"
      ...
      (300a, 012c) Isocenter Position                  DS: ['111.908', '-52.0623', '-1212.2']
      ...
   ...
...
[4]: ds[0x300a,0xb0][0][0x300a,0x111][0][0x300a,0x12c].value
['111.908', '-52.0623', '-1212.2']
</code></pre>
<p>But this method is difficult. <img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=9" title=":thinking:" class="emoji" alt=":thinking:"></p>
<p>Best regards.<br>
Shahrokh</p>

---

## Post #6 by @pieper (2019-06-18 15:59 UTC)

<p>Yes, getting data out of nested dicom sequences is kind of awkward. The example I linked is abit easier to read, since it uses the dicom dictionary name instead of the hex tag. <code>ds.CTExposureSequence[0].ExposureModulationType</code></p>

---
