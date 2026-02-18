# Error when loading MRB

**Topic ID**: 21890
**Date**: 2022-02-10
**URL**: https://discourse.slicer.org/t/error-when-loading-mrb/21890

---

## Post #1 by @bcolbert (2022-02-10 12:40 UTC)

<p>I repeatedly receive the following error when loading an MRB I saved yesterday evening. Amy support would be helpful:</p>
<blockquote>
<p>Slicer has caught an application error, please save your work and restart.</p>
<p>If you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="http://slicer.org" rel="noopener nofollow ugc">http://slicer.org</a></p>
<p>The message detail is:</p>
<p>Exception thrown in event: D:\D\S\Slicer-1-build\ITK\Modules\IO\NRRD\src\itkNrrdImageIO.cxx:767:</p>
<p>itk::ERROR: itk::ERROR: NrrdImageIO(000001F4CA489030): Read: Error reading C:/Users/Benjamin Colbert/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/__BundleLoadTemp-2022-02-10_073712_461/2022-02-09-Scene/Data/Segmentation.seg.nrrd:</p>
<p>[nrrd] nrrdLoad: trouble reading “C:/Users/Benjamin Colbert/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/__BundleLoadTemp-2022-02-10_073712_461/2022-02-09-Scene/Data/Segmentation.seg.nrrd”</p>
<p>[nrrd] nrrdRead: trouble</p>
<p>[nrrd] _nrrdRead: trouble reading NRRD file</p>
<p>[nrrd] _nrrdFormatNRRD_read:</p>
<p>[nrrd] _nrrdEncodingRaw_read: fread got only 3228075008 1-sized things, not 7523042304 (42.9092% of expected)</p>
</blockquote>

---

## Post #2 by @lassoan (2022-02-10 13:21 UTC)

<p>The segmentation file is expected to be an extremely large file, about 7.5GB, but the actual file size is just 3.2GB.</p>
<p>Make sure there is enough free space on your hard disk (10x more than the mrb file size) and try again.</p>
<p>Saving such large files can be challenging, because you may run out of memory or disk space during saving and if you use a virtual file system (network drive, Virtual cloud drive - such as box or Google) then network connectivity and synchronization issues may affect the saving as well.</p>
<p>What Slicer version did you use? Did you use the same computer for saving and loading the scene? How big is the mrb file? How much free disk space you had when you saved the scene? How much physical RAM do you have in your computer and how much virtual memory have your configured in your Windows system settings?</p>

---

## Post #3 by @bcolbert (2022-02-10 16:08 UTC)

<blockquote>
<p>What Slicer version did you use?</p>
</blockquote>
<p>v4.11.20210226</p>
<blockquote>
<p>Did you use the same computer for saving and loading the scene?</p>
</blockquote>
<p>Yes.</p>
<blockquote>
<p>How big is the mrb file?</p>
</blockquote>
<p>6.01 GB</p>
<blockquote>
<p>How much free disk space you had when you saved the scene?</p>
</blockquote>
<p>Saving on a 4tb portable drive. The drive has &gt;2.5TB left</p>
<blockquote>
<p>How much physical RAM do you have in your computer and how much virtual memory have your configured in your Windows system settings?</p>
</blockquote>
<p>I have 64gb ram installed and virtual memory is 9728mb</p>

---

## Post #4 by @lassoan (2022-02-10 20:00 UTC)

<aside class="quote no-group quote-modified" data-username="bcolbert" data-post="3" data-topic="21890">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bcolbert/48/11162_2.png" class="avatar"> bcolbert:</div>
<blockquote>
<blockquote>
<p>What Slicer version did you use?</p>
</blockquote>
<p>v4.11.20210226</p>
</blockquote>
</aside>
<p>We have added extensive checking and error reporting during scene saving in recent Slicer Preview Releases. Unfortunately, these are not available in v4.11.20210226, so if there were errors during scene saving then it is possible that they were not reported.</p>
<aside class="quote no-group quote-modified" data-username="bcolbert" data-post="3" data-topic="21890">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bcolbert/48/11162_2.png" class="avatar"> bcolbert:</div>
<blockquote>
<blockquote>
<p>How much free disk space you had when you saved the scene?</p>
</blockquote>
<p>Saving on a 4tb portable drive. The drive has &gt;2.5TB left</p>
</blockquote>
</aside>
<p>Saving a 6GB file as MRB may require 10-20 GB temporary space in the temporary folder. This is usually set to a built-in drive, so having lots of space on an external drive may not matter.</p>
<p>Risk of file corruption is significantly increased for huge files and external drives. Since error reporting was limited in the Slicer version that you used and there were some risk factors, there is a chance that there was a failure during saving and it was not reported.</p>
<p>If you work with such huge files, I would recommend to save to the local disk first (and use the external disk for archival), save to mrml (not single-file mrb, to avoid huge files), and use latest Slicer Preview Release for improved error detection and reporting.</p>

---

## Post #5 by @bcolbert (2022-02-11 12:16 UTC)

<p>It’s a good thing this only had a couple of hours of work associated with it. Makes it a cheap lesson.</p>
<p>So question, if I am using a the imagestack tool within the SlicerMorph toolkit and only loading a ROI at full resolution (e.g., load the whole stack as preview resolution, then slect area around structure of interest) is that captured in mrml. Apologize for the basic question but I am the only one in my lab doing this work so don’t really know the best practices.</p>

---

## Post #6 by @pieper (2022-02-11 14:53 UTC)

<p>When you use ImageStacks it will by default use the same target volume in the MRML scene as you change import parameters so you tests won’t be saved, only the last one you import.</p>

---

## Post #7 by @muratmaga (2022-02-11 15:58 UTC)

<aside class="quote no-group" data-username="bcolbert" data-post="5" data-topic="21890">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bcolbert/48/11162_2.png" class="avatar"> bcolbert:</div>
<blockquote>
<p>Apologize for the basic question but I am the only one in my lab doing this work so don’t really know the best practices.</p>
</blockquote>
</aside>
<p>We have quite a bit of training material around SLicerMorph tools. You may want to review them quickly:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerMorph/Tutorials">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/d1d0a376fcb796cfae47a76feef6298b06bcd0267e38024e21e3c5c12142e10c/SlicerMorph/Tutorials" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerMorph/Tutorials" target="_blank" rel="noopener">GitHub - SlicerMorph/Tutorials: SlicerMorph module tutorials</a></h3>

  <p>SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I will second <a class="mention" href="/u/lassoan">@lassoan</a> suggestion not to use the MRB format when working locally, but use it when you need to send data to share data. I also suggest not bothering to compress the data, since it adds a quite a bit of time to your saving process (for large datasets) and nowadays usually storage is so cheap.</p>
<p>If you do NOT have a complex scene (with lots of different things like segmentations, markups, tables, rendering etc), you can also use the <strong>export As</strong> function (right click on the object in the Data module, and choose Export As) to manually save your objects one by one. This works fine for simple workflows, but gets tedious quickly when you a lot of things and you export them one by one.</p>

---

## Post #8 by @lassoan (2022-02-11 18:08 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="21890">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>If you do NOT have a complex scene (with lots of different things like segmentations, markups, tables, rendering etc), you can also use the <strong>export As</strong> function (right click on the object in the Data module, and choose Export As)</p>
</blockquote>
</aside>
<p>In Slicer Preview Release we have a built-in <code>Export to file...</code> menu action. It has several advantages over the prototype <code>Export as...</code> action, including the ability to export all the nodes in a folder at once, so if you export many markups.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> could you disable <code>Export as...</code> for Slicer-4.13 to avoid confusing users with the duplicate export option?</p>

---

## Post #9 by @muratmaga (2022-02-11 19:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="21890">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> could you disable <code>Export as...</code> for Slicer-4.13 to avoid confusing users with the duplicate export option?</p>
</blockquote>
</aside>
<p>Not yet. We will. Thanks for the remainder<br>
<a class="mention" href="/u/smrolfe">@smrolfe</a></p>

---

## Post #10 by @smrolfe (2022-02-11 19:40 UTC)

<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/lassoan">@lassoan</a>, I have updated our extension to remove “ExportAs”.</p>

---
