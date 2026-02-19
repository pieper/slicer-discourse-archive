---
topic_id: 31904
title: "Using Qmrmlnodeattributetablewidget With Qmrmlsegmenteditorw"
date: 2023-09-26
url: https://discourse.slicer.org/t/31904
---

# Using qMRMLNodeAttributeTableWidget with qMRMLSegmentEditorWidget

**Topic ID**: 31904
**Date**: 2023-09-26
**URL**: https://discourse.slicer.org/t/using-qmrmlnodeattributetablewidget-with-qmrmlsegmenteditorwidget/31904

---

## Post #1 by @NguyenVuHoaBinh (2023-09-26 04:18 UTC)

<p>Hello everyone! I am new to 3D Slicer.<br>
I am currently creating a sample extension that allow user add additional information about the segmentation when using segment editor, but i got stuck. I dont know how to mapping the qMRMLNodeAttributeTableWidget with qMRMLSegmentEditorWidget. I will really appreaciate any help.</p>
<p>Sorry if my bad English make you confuse to understand. Have a nice day!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f90f9b84d461de05357ace6fa388fd00b511578.png" data-download-href="/uploads/short-url/mLAwD8qKZyNVJI713f8xZx0ZmCQ.png?dl=1" title="Screenshot 2023-09-26 111053" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f90f9b84d461de05357ace6fa388fd00b511578.png" alt="Screenshot 2023-09-26 111053" data-base62-sha1="mLAwD8qKZyNVJI713f8xZx0ZmCQ" width="345" height="124" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-09-26 111053</span><span class="informations">795×288 4.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Operating system: Window 11<br>
Slicer version: 5.2.2<br>
Expected behavior: Can perform add/remove attribute name and value for the selected segmentation node from segment editor widget<br>
Actual behavior: Failed to instantiate module</p>

---

## Post #2 by @cpinter (2023-09-26 11:24 UTC)

<p>What you describe that you want to do seems quite unusual. To my understanding you want to change node attributes visually for the segment editor node. However, that’s kind of halfway between UI and programming, and would be very error-prone and would require continual lookup of attributes in the source code etc.</p>
<p>Can you please describe what you actually want to achieve from the user’s perspective?</p>

---

## Post #3 by @NguyenVuHoaBinh (2023-09-26 13:04 UTC)

<p>Thank you for your support. I will provide detail what i want to achieve.<br>
Assume that i am a radiologist using 3D slicer to annotate multiple segmentations like this.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8830133e9f058a434445cea6e95ea9d36f4fecbb.png" data-download-href="/uploads/short-url/jqLW4a7ta6bdVrICNYjTA3ETEpB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/8830133e9f058a434445cea6e95ea9d36f4fecbb_2_415x375.png" alt="image" data-base62-sha1="jqLW4a7ta6bdVrICNYjTA3ETEpB" width="415" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/8830133e9f058a434445cea6e95ea9d36f4fecbb_2_415x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/8830133e9f058a434445cea6e95ea9d36f4fecbb_2_622x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/8830133e9f058a434445cea6e95ea9d36f4fecbb_2_830x750.png 2x" data-dominant-color="EBEFF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">831×750 29.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, i want to make more comment for each segmentation label i made by using the [qMRMLNodeAttributeTableWidget], giving some fixed attribute and add the value for them so whenever i re-open the file, i can review it or modify the attribute value i created before. Here is the [qMRMLNodeAttributeTableWidget]<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c961546dceba03a9df37f59aed05ec17dffd02f4.png" data-download-href="/uploads/short-url/sJuuYPAyvLg14fcm9nN6Xz1f1kw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c961546dceba03a9df37f59aed05ec17dffd02f4.png" alt="image" data-base62-sha1="sJuuYPAyvLg14fcm9nN6Xz1f1kw" width="517" height="174" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">835×283 3.91 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My desired output is like this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20d2dc0a8892cc9aa0751c001f9dfcfa7d5656a5.png" data-download-href="/uploads/short-url/4Gn2Hjv34FMjNn6qEs5T6X6RGHX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20d2dc0a8892cc9aa0751c001f9dfcfa7d5656a5_2_517x204.png" alt="image" data-base62-sha1="4Gn2Hjv34FMjNn6qEs5T6X6RGHX" width="517" height="204" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20d2dc0a8892cc9aa0751c001f9dfcfa7d5656a5_2_517x204.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20d2dc0a8892cc9aa0751c001f9dfcfa7d5656a5_2_775x306.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20d2dc0a8892cc9aa0751c001f9dfcfa7d5656a5.png 2x" data-dominant-color="EEEEEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">858×339 23.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hope you will understand what i am trying to achieve.<br>
Thank you.</p>

---

## Post #4 by @cpinter (2023-09-26 13:56 UTC)

<p>Segments are not nodes, so this idea won’t work for individual segments. See this part of the documentation:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html</a></p>
<p>The segments do not have attributes, but they have “tags” that can be used for this purpose, see</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/d9485819db2e8e71a4cf0e4d914946f704bbcb39/Libs/vtkSegmentationCore/vtkSegment.h#L94-L110">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/d9485819db2e8e71a4cf0e4d914946f704bbcb39/Libs/vtkSegmentationCore/vtkSegment.h#L94-L110" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/d9485819db2e8e71a4cf0e4d914946f704bbcb39/Libs/vtkSegmentationCore/vtkSegment.h#L94-L110" target="_blank" rel="noopener">Slicer/Slicer/blob/d9485819db2e8e71a4cf0e4d914946f704bbcb39/Libs/vtkSegmentationCore/vtkSegment.h#L94-L110</a></h4>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="94" style="counter-reset: li-counter 93 ;">
          <li>/// Set/add tag</li>
          <li>void SetTag(std::string tag, std::string value);</li>
          <li>/// Set/add integer tag</li>
          <li>void SetTag(std::string tag, int value);</li>
          <li></li>
          <li>/// Remove tag</li>
          <li>void RemoveTag(std::string tag);</li>
          <li></li>
          <li>/// Get tag</li>
          <li>/// \param tag Name of requested tag</li>
          <li>/// \param value Output argument for the value of the tag if found</li>
          <li>/// \return True if tag is found, false otherwise</li>
          <li>bool GetTag(std::string tag, std::string &amp;value);</li>
          <li>/// Determine if a tag is present</li>
          <li>bool HasTag(std::string tag);</li>
          <li>/// Get tags</li>
          <li>void GetTags(std::map&lt;std::string,std::string&gt; &amp;tags);</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>But there is no table for the tags. Maybe you can look at this class as inspiration:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentationConversionParametersWidget.h">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentationConversionParametersWidget.h" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentationConversionParametersWidget.h" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentationConversionParametersWidget.h</a></h4>


      <pre><code class="lang-h">/*==============================================================================

  Program: 3D Slicer

  Copyright (c) Laboratory for Percutaneous Surgery (PerkLab)
  Queen's University, Kingston, ON, Canada. All Rights Reserved.

  See COPYRIGHT.txt
  or http://www.slicer.org/copyright/copyright.txt for details.

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

  This file was originally developed by Csaba Pinter, PerkLab, Queen's University
  and was supported through the Applied Cancer Research Unit program of Cancer Care
  Ontario with funds provided by the Ontario Ministry of Health and Long-Term Care

</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentationConversionParametersWidget.h" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @NguyenVuHoaBinh (2023-09-26 15:08 UTC)

<p>Wonderful! I will check that out. By the way, is it possible to create separate tables like that for each segmentation label map like the sample image below?<br>
P/s: The image is a sample and does not contain any confidential information.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9a64158b4bcf5b32e676b245a355c2656d1a0bd.jpeg" data-download-href="/uploads/short-url/ocMTlL2JikHIl7YiyXosghbg4HP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9a64158b4bcf5b32e676b245a355c2656d1a0bd_2_690x272.jpeg" alt="image" data-base62-sha1="ocMTlL2JikHIl7YiyXosghbg4HP" width="690" height="272" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9a64158b4bcf5b32e676b245a355c2656d1a0bd_2_690x272.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9a64158b4bcf5b32e676b245a355c2656d1a0bd_2_1035x408.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/9/a9a64158b4bcf5b32e676b245a355c2656d1a0bd_2_1380x544.jpeg 2x" data-dominant-color="B2B3BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2542×1004 288 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @cpinter (2023-09-26 20:27 UTC)

<p>I think you should use split islands and separate these into a segment each. In the default terminology you can specify the same type with left/right modifiers, so you can uniquely identify the structures.</p>

---
