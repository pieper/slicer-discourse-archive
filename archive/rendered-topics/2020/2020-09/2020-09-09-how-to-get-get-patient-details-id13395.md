# How to get Get Patient Details

**Topic ID**: 13395
**Date**: 2020-09-09
**URL**: https://discourse.slicer.org/t/how-to-get-get-patient-details/13395

---

## Post #1 by @Chintha_Siva_Prasad (2020-09-09 04:49 UTC)

<p>How can I get patient details like name, sex etc?<br>
What is the method to access these tags in python through a dicom database?</p>

---

## Post #2 by @jamesobutler (2020-09-09 05:02 UTC)

<p>The <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="noopener nofollow ugc">Slicer script repository</a> includes many python scripting examples of common Slicer actions including manipulating DICOM database details.</p>
<p>This thread details some of that</p><aside class="quote quote-modified" data-post="3" data-topic="7184">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahrokh/48/1499_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-read-the-value-of-certain-attribute-tag-in-dicom-metadata-from-python-interactor/7184/3">How to read the value of certain attribute (tag) in DICOM Metadata" from "Python Interactor"</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi Steve 
Thanks a lot for sending to me the link to ScriptRepository. 
I can access to tags such as (0020,0010) to (300a,000c), but unfortunately I can not read tags that are located in item, such as (300a,012c), highlighted in the following figure. 
The following figure is screenshot of DICOM File Browser and the tag that I want to access its value  (300a,012c). 
[Screenshot%20from%202019-06-17%2011-58-27] 
I enter the following commands: 
&gt;&gt;&gt; patientList=db.patients() 
&gt;&gt;&gt; studyList=db.studie…
  </blockquote>
</aside>


---
