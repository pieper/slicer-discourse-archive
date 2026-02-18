# Total Segmentator error

**Topic ID**: 33547
**Date**: 2023-12-28
**URL**: https://discourse.slicer.org/t/total-segmentator-error/33547

---

## Post #1 by @mohamed_tolba (2023-12-28 17:00 UTC)

<p>Hello slicer community. I trying to segment the maxilla and the mandible using total segmentator I get this message " Failed to compute results. Command '[‘C:/Users/PC/AppData/Local/slicer.org/Slicer 5.4.0/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, '<a href="https://github.com/wasserth/TotalSegmentator/archive/951f07b9721404f5a4306236358d1d7cab1e3610.zip'%5D'" rel="noopener nofollow ugc">https://github.com/wasserth/TotalSegmentator/archive/951f07b9721404f5a4306236358d1d7cab1e3610.zip’]’</a> returned non-zero exit status 1.", where is the problem and how I solve it?</p>

---

## Post #2 by @jamesobutler (2023-12-28 17:33 UTC)

<p>It appears you are using Slicer 5.4.0 which is an older version. Generally if you come across an error it is good practice to try the latest version.  Therefore I would suggest that you download and install Slicer 5.6.1 (latest stable) from <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a>.</p>
<p>This will also get you access to Total Segmentator v2.</p>
<aside class="quote quote-modified" data-post="1" data-topic="32470">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/totalsegmentator-v2/32470">TotalSegmentator v2</a> <a class="badge-category__wrapper " href="/c/announcements/7"><span data-category-id="7" style="--category-badge-color: #ED207B; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="Low-traffic category for 3D Slicer, extension, and community news and announcements."><span class="badge-category__name">Announcements</span></span></a>
  </div>
  <blockquote>
    We are excited to announce that the 3D Slicer TotalSegmentator extension is now compatible with TotalSegmentator v2! 
TotalSegmentator stands out as a powerful tool, proficient in segmenting up to 117 classes in CT images. It is robust, fast, comprehensive, and can even be run without a GPU. Given its training on a vast variety of CT images - spanning different scanners, institutions, and protocols - it works consistently well across a broad spectrum of images. 
These new structures are availabl…
  </blockquote>
</aside>


---
