---
topic_id: 11143
title: "May I Know How To Call Methods In The Cpp To Get The Name Bi"
date: 2020-04-16
url: https://discourse.slicer.org/t/11143
---

# May I know how to call methods in the cpp to get the name, birthday, gender, and series and series description of the loaded dicom data.Thanks!

**Topic ID**: 11143
**Date**: 2020-04-16
**URL**: https://discourse.slicer.org/t/may-i-know-how-to-call-methods-in-the-cpp-to-get-the-name-birthday-gender-and-series-and-series-description-of-the-loaded-dicom-data-thanks/11143

---

## Post #1 by @Shicong (2020-04-16 07:16 UTC)

<p>Well, I was calling the “qSlicerApplication::application()-&gt;dicomDatabase()” in the c++ code  to get the currently loaded dicom data? i can see stdudy description information in dicom component, but the loading is done, I get study description information in the c, the display is empty.  May I know how to call methods in the c++ code to get the name, birthday, gender, and series and series description of the loaded dicom data? Thank you so much! !!! !!! !<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e69bce08cf3ab5a78a9ba8bcb36205a7a6656fdd.png" data-download-href="/uploads/short-url/wU3CXVTmnzq6JAQvV1Fegxd1t37.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e69bce08cf3ab5a78a9ba8bcb36205a7a6656fdd.png" alt="图片" data-base62-sha1="wU3CXVTmnzq6JAQvV1Fegxd1t37" width="690" height="342" data-dominant-color="EAF1F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">1297×643 7.25 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bc5080d1d2204a87e6949f6f7651b157ea9e3d8.png" data-download-href="/uploads/short-url/aOhWMX3esnljdodxSr7niazhCMU.png?dl=1" title="图片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bc5080d1d2204a87e6949f6f7651b157ea9e3d8_2_690x312.png" alt="图片" data-base62-sha1="aOhWMX3esnljdodxSr7niazhCMU" width="690" height="312" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bc5080d1d2204a87e6949f6f7651b157ea9e3d8_2_690x312.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bc5080d1d2204a87e6949f6f7651b157ea9e3d8_2_1035x468.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bc5080d1d2204a87e6949f6f7651b157ea9e3d8.png 2x" data-dominant-color="292C2B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片</span><span class="informations">1317×596 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Mik (2020-04-16 11:23 UTC)

<p>Dear Zhao,</p>
<p>I think you can use <a href="http://www.commontk.org/docs/html/classctkDICOMDatabase.html#aa2d481e342ac960470bbb03a535e1d38" rel="nofollow noopener">fileValue</a> method if the DICOM data imported into Slicer (you must know a DICOM tag of the info you needed), or you can use DCMTK directly to load all the required information from the DICOM file.</p>

---

## Post #3 by @cpinter (2020-04-16 12:40 UTC)

<aside class="quote no-group" data-username="Shicong" data-post="1" data-topic="11143">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shicong/48/6562_2.png" class="avatar"> Shicong:</div>
<blockquote>
<p>I get study description information in the c, the display is empty</p>
</blockquote>
</aside>
<p>I don’t understand this. What is empty?</p>
<p>You can get the raw DICOM tag values from the files as suggested by <a class="mention" href="/u/mik">@Mik</a>. However, you can also access most of this information from subject hierarchy. From the loaded data (volume node in your case) you can get to the study and patient items, which contain these information as attributes. Here are some pointers about how to use subject hierarchy<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Subject_hierarchy" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Subject_hierarchy</a><br>
And these are the attribute names</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLSubjectHierarchyConstants.h#L74-L124">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLSubjectHierarchyConstants.h#L74-L124" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLSubjectHierarchyConstants.h#L74-L124" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLSubjectHierarchyConstants.h#L74-L124</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="74" style="counter-reset: li-counter 73 ;">
          <li></li>
          <li>// Patient tags</li>
          <li>static const std::string GetDICOMPatientNameTagName()</li>
          <li>  { return "PatientName"; };</li>
          <li>static const std::string GetDICOMPatientNameAttributeName()</li>
          <li>  { return vtkMRMLSubjectHierarchyConstants::GetDICOMAttributePrefix() + vtkMRMLSubjectHierarchyConstants::GetDICOMPatientNameTagName(); };</li>
          <li>static const std::string GetDICOMPatientIDTagName()</li>
          <li>  { return "PatientID"; };</li>
          <li>static const std::string GetDICOMPatientIDAttributeName()</li>
          <li>  { return vtkMRMLSubjectHierarchyConstants::GetDICOMAttributePrefix() + vtkMRMLSubjectHierarchyConstants::GetDICOMPatientIDTagName(); };</li>
          <li>static const std::string GetDICOMPatientSexTagName()</li>
          <li>  { return "PatientSex"; };</li>
          <li>static const std::string GetDICOMPatientSexAttributeName()</li>
          <li>  { return vtkMRMLSubjectHierarchyConstants::GetDICOMAttributePrefix() + vtkMRMLSubjectHierarchyConstants::GetDICOMPatientSexTagName(); };</li>
          <li>static const std::string GetDICOMPatientBirthDateTagName()</li>
          <li>  { return "PatientBirthDate"; };</li>
          <li>static const std::string GetDICOMPatientBirthDateAttributeName()</li>
          <li>  { return vtkMRMLSubjectHierarchyConstants::GetDICOMAttributePrefix() + vtkMRMLSubjectHierarchyConstants::GetDICOMPatientBirthDateTagName(); };</li>
          <li>static const std::string GetDICOMPatientCommentsTagName()</li>
          <li>  { return "PatientComments"; };</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLSubjectHierarchyConstants.h#L74-L124" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
(please note that you need to use the attribute names not the tag names to get the attributes using shNode.GetItemAttribute)</p>

---

## Post #4 by @lassoan (2020-04-16 13:46 UTC)

<p>See complete example in the script repository here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_access_tag_of_an_item_in_the_Subject_Hierachy_tree.3F_For_example.2C_get_the_content_time_tag_of_a_structure_set:">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_access_tag_of_an_item_in_the_Subject_Hierachy_tree.3F_For_example.2C_get_the_content_time_tag_of_a_structure_set:</a></p>

---

## Post #5 by @Shicong (2020-04-17 01:59 UTC)

<p>thank you, your help to me very much!</p>

---

## Post #6 by @Shicong (2020-04-17 02:10 UTC)

<p>thank you and give me the prompt message!</p>

---

## Post #7 by @Shicong (2020-04-17 02:36 UTC)

<p>Thank you for giving me great help!</p>

---

## Post #8 by @Shicong (2020-04-28 09:34 UTC)

<p>Is through the above method, but still can not get the corresponding value ah! Could you help with the sticker code, c++ is the best ，thanks !</p>

---

## Post #9 by @lassoan (2020-04-28 16:18 UTC)

<p>Since most of Slicer core is inplemented in C++, you can find C++ examples there for everything: <a href="https://github.com/Slicer/Slicer">https://github.com/Slicer/Slicer</a></p>

---

## Post #10 by @Shicong (2020-04-29 02:47 UTC)

<p>Thank you very much!</p>

---

## Post #11 by @apparrilla (2023-08-02 07:48 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> .<br>
I can´t access this link:</p>
<blockquote>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_access_tag_of_an_item_in_the_Subject_Hierachy_tree.3F_For_example.2C_get_the_content_time_tag_of_a_structure_set:" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>
</blockquote>
<p>Could you update it?<br>
Thanks in advance!</p>

---

## Post #12 by @lassoan (2023-08-04 19:25 UTC)

<p>The Slicer script repository was moved here a few years ago: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>

---
