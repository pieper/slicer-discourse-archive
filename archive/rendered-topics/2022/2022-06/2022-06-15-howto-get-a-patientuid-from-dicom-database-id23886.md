# Howto get a patientUID from DICOM database?

**Topic ID**: 23886
**Date**: 2022-06-15
**URL**: https://discourse.slicer.org/t/howto-get-a-patientuid-from-dicom-database/23886

---

## Post #1 by @jumbojing (2022-06-15 04:09 UTC)

<p>Well, I’ve got the patient’s name from Dicom database. but howto get a patientUID from DICOM database?</p>
<pre><code class="lang-auto">volumeNode = Helper.getFirstNodeByClass("vtkMRMLScalarVolumeNode")
# Get series instance UID from subject hierarchy
shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
volumeItemId = shNode.GetItemByDataNode(volumeNode)
seriesInstanceUID = shNode.GetItemUID(volumeItemId, 'DICOM')
# Get patient name (0010,0010) from the first file of the series
instUids = slicer.dicomDatabase.instancesForSeries(seriesInstanceUID)
print(slicer.dicomDatabase.instanceValue(instUids[0], '0010,0010')) # patient name
</code></pre>
<p>from <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#dicom:~:text=%E7%9A%84%E8%AE%BF%E9%97%AE%E6%A0%87%E8%AE%B0-,%C2%B6,-%E7%94%B1%E5%90%84%E7%A7%8DDICOM" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>
<p>from <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-table-columns-in-dicom-browser" rel="noopener nofollow ugc">slicer.readthedocs.io</a><br>
I  use this code <code>dicomDatabase.setVisibilityForField("Patients", "UID", True)</code> get the ‘UID’ column.</p>

---

## Post #2 by @mau_igna_06 (2022-06-15 12:55 UTC)

<p>Please don’t share patient data. You can unfocus that text with the names so it is not seen</p>

---

## Post #3 by @jumbojing (2022-06-15 13:18 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/631b1a611dd88f19f35ddf3635b7050353001553.png" data-download-href="/uploads/short-url/e8JkVEAefO1nBLLY5coDLNKeYEz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/631b1a611dd88f19f35ddf3635b7050353001553_2_690x163.png" alt="image" data-base62-sha1="e8JkVEAefO1nBLLY5coDLNKeYEz" width="690" height="163" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/631b1a611dd88f19f35ddf3635b7050353001553_2_690x163.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/631b1a611dd88f19f35ddf3635b7050353001553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/631b1a611dd88f19f35ddf3635b7050353001553.png 2x" data-dominant-color="C0C8D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">948×224 53.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
sorry, but I don’t know how to delete the posted picture…</p>

---

## Post #4 by @rbumm (2022-06-15 13:30 UTC)

<p>[0010,0020]   should hold   PatientID</p>
<p>Good luck !</p>

---

## Post #5 by @jumbojing (2022-06-15 13:34 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56d465986c7cd518ba207548481a65a7423d87b9.png" data-download-href="/uploads/short-url/co87tGAtZInxF5Z3BdvdFrgcr1f.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56d465986c7cd518ba207548481a65a7423d87b9.png" alt="image" data-base62-sha1="co87tGAtZInxF5Z3BdvdFrgcr1f" width="690" height="117" data-dominant-color="BDD7FE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">723×123 22.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
不对呀, 我想要UID而不是patientID</p>
<p>Nope, I want UID not patientID…</p>

---

## Post #6 by @rbumm (2022-06-15 13:50 UTC)

<p>[0020,000d] StudyInstanceUID<br>
[0020,000e] SeriesInstanceUID<br>
[0020,0010] StudyID<br>
[0020,0011] SeriesNumber</p>

---

## Post #7 by @jumbojing (2022-06-15 13:55 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35775285fa92a443bdf34dc5d3f2d3845ab2d801.png" data-download-href="/uploads/short-url/7CYX4XMxq0eFUTl8NFWfWc58AEN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35775285fa92a443bdf34dc5d3f2d3845ab2d801.png" alt="image" data-base62-sha1="7CYX4XMxq0eFUTl8NFWfWc58AEN" width="690" height="131" data-dominant-color="C7E2F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">702×134 26.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://emoji.discourse-cdn.com/twitter/cold_sweat.png?v=12" title=":cold_sweat:" class="emoji only-emoji" alt=":cold_sweat:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @rbumm (2022-06-15 13:56 UTC)

<p>what do you expect ?</p>

---

## Post #9 by @jumbojing (2022-06-15 13:58 UTC)

<aside class="quote no-group" data-username="jumbojing" data-post="3" data-topic="23886" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jumbojing/48/10811_2.png" class="avatar"> jumbojing:</div>
<blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/631b1a611dd88f19f35ddf3635b7050353001553.png" data-download-href="/uploads/short-url/e8JkVEAefO1nBLLY5coDLNKeYEz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/631b1a611dd88f19f35ddf3635b7050353001553_2_690x163.png" alt="image" data-base62-sha1="e8JkVEAefO1nBLLY5coDLNKeYEz" width="690" height="163" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/631b1a611dd88f19f35ddf3635b7050353001553_2_690x163.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/631b1a611dd88f19f35ddf3635b7050353001553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/631b1a611dd88f19f35ddf3635b7050353001553.png 2x" data-dominant-color="C0C8D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">948×224 53.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>sorry, but I don’t know how to delete the posted picture…</p>
</blockquote>
</aside>
<p>I want the UID, ,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/936bc40a378cc45a35d65958cd964d136069cd23.png" data-download-href="/uploads/short-url/l294Fmyvaz73f9FnaddydBUwI5t.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/936bc40a378cc45a35d65958cd964d136069cd23_2_690x46.png" alt="image" data-base62-sha1="l294Fmyvaz73f9FnaddydBUwI5t" width="690" height="46" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/936bc40a378cc45a35d65958cd964d136069cd23_2_690x46.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/936bc40a378cc45a35d65958cd964d136069cd23_2_1035x69.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/936bc40a378cc45a35d65958cd964d136069cd23_2_1380x92.png 2x" data-dominant-color="515152"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1890×128 23.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @cpinter (2022-06-15 14:47 UTC)

<p>I think this is the function you need <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMUtils.py#L83" class="inline-onebox">Slicer/DICOMUtils.py at master · Slicer/Slicer · GitHub</a></p>
<p>So</p>
<pre><code class="lang-auto">from DICOMLib import DICOMUtils
DICOMUtils.getDatabasePatientUIDByPatientName('PatientName')
</code></pre>

---

## Post #11 by @jumbojing (2022-06-15 15:20 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="10" data-topic="23886">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<pre><code class="lang-auto">from DICOMLib import DICOMUtils
DICOMUtils.getDatabasePatientUIDByPatientName('PatientName')
</code></pre>
</blockquote>
</aside>
<p>Thanks! <a class="mention" href="/u/cpinter">@cpinter</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b151b1f1bc2c364a340557d2e699d47f0a5cb5b5.jpeg" data-download-href="/uploads/short-url/piDxG4t13cw9JQKb0YAEDIow181.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b151b1f1bc2c364a340557d2e699d47f0a5cb5b5_2_592x500.jpeg" alt="image" data-base62-sha1="piDxG4t13cw9JQKb0YAEDIow181" width="592" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b151b1f1bc2c364a340557d2e699d47f0a5cb5b5_2_592x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b151b1f1bc2c364a340557d2e699d47f0a5cb5b5_2_888x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b151b1f1bc2c364a340557d2e699d47f0a5cb5b5_2_1184x1000.jpeg 2x" data-dominant-color="CED8E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1526×1288 308 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
