# AMASSS Issue: CLI execution failed:

**Topic ID**: 38552
**Date**: 2024-09-26
**URL**: https://discourse.slicer.org/t/amasss-issue-cli-execution-failed/38552

---

## Post #1 by @Arash1 (2024-09-26 07:08 UTC)

<p>Hello</p>
<p>I have a challenge with running the AMASSS and it seems the problem is somewhat common from what I see in other posts.</p><aside class="quote quote-modified" data-post="1" data-topic="33715">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohamed_tolba/48/68823_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/amasss-module-issues/33715">AMASSS module issues</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi slicer community I recently discovered the automated dental tools. Although when I use AMASSS module and enter the input data and choose the output data and click on run prediction the software doesn’t respond and it doesn’t freeze too. I don’t know what is the problem? 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f1ac52aad6d5a0d954eb69f6d7610f1ef6750f5.jpeg" data-download-href="/uploads/short-url/kpXDfJyJpbaaxbu9Q3rvDqJ925L.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a>
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="1" data-topic="35142">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/artur_zhumabekov/48/67145_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/amasss-error-with-cbct-segmentation/35142">AMASSS error with cbct segmentation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello 
I have got a problem with AMASSS extension 
Traceback (most recent call last): 
File “C:\Users\zhuma\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\site-packages\pkg_resources_vendor\packaging\requirements.py”, line 35, in init 
parsed = _parse_requirement(requirement_string) 
File “C:\Users\zhuma\AppData\Local\slicer.org\Slicer 5.6.1\lib\Python\Lib\site-packages\pkg_resources_vendor\packaging_parser.py”, line 64, in parse_requirement 
return _parse_requirement(Tokenizer(source, rul…
  </blockquote>
</aside>

<p>I tried both the nightly build and the stable version on a new system, and it didn’t work. Any suggestions?</p>

---

## Post #2 by @Esteban_Barreiro (2025-01-11 13:34 UTC)

<p>Hi there! AMASS module works fine if you save the 3dslicer scene before you run the module, and use the folder where you save it (it will contain the .nrrd file now) with NRRD Input Modality, selecting that folder you create  as Directory.</p>

---
