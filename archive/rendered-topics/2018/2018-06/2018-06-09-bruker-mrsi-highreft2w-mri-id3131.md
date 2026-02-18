# Bruker MRSI / HighRefT2w MRI

**Topic ID**: 3131
**Date**: 2018-06-09
**URL**: https://discourse.slicer.org/t/bruker-mrsi-highreft2w-mri/3131

---

## Post #1 by @virginia_fgc (2018-06-09 13:15 UTC)

<p>Hi,</p>
<p>I have always worked with DICOM and nrrd files in 3D Slicer. However, I am currently working on a project in which I need to handle High Resolution T2w MRI images acquired by <strong>Bruker</strong> equipment.<br>
The problem is that the files I have are in format “2dseq”, and Slicer does not handle that format. From all open source programs I have found on the web, I’ve only been able to open the file with ImageJ. However, I haven’t managed to convert the files to any format Slicer can actually read.</p>
<p>Of all formats, I am only familiarized with DICOM; I’ve never worked with Bruker images before, and I am not sure of the information they contain (besides the image itself).</p>
<p>Has anyone ever managed to open images in “2dseq” format with Slicer, or used any intermediate program to make it possible?</p>
<p>Thank you very much.</p>
<p>Virginia</p>

---

## Post #2 by @fedorov (2018-06-09 15:24 UTC)

<p>I don’t have an answer to your question, but if I were you I would try <a href="https://sourceforge.net/p/sivic/sivicwiki/Home/">SIVIC</a> (I hope that URL is up to date location for it), which is a package specifically developed for processing of MRSI. I also think that its developers might be more knowledgeable about the MRSI-specific formats to help you (and I believe it has some tools to process non-DICOM MRSI). But I don’t have any hands-on experience with SIVIC.</p>
<p>I will also forward a link to this topic to the lead developer of SIVIC whom I know, in case he has a more specific answer for you.</p>

---

## Post #3 by @ihnorton (2018-06-11 14:50 UTC)

<ul>
<li>I would first suggest to try Bru2Nii, and if it works then import the resulting NIfTI into Slicer. Bru2Nii will probably handle more varieties and metadata than my second suggestion:</li>
</ul>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/neurolabusc/Bru2Nii/">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/neurolabusc/Bru2Nii/" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/ef65c37e4cb7d2a6e67ef796359d9d52053ee12a98fca089b9bb49651a7b4b6c/neurolabusc/Bru2Nii" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/neurolabusc/Bru2Nii/" target="_blank" rel="noopener">GitHub - neurolabusc/Bru2Nii: Bruker ParaVision to NIfTI conversion</a></h3>

  <p>Bruker ParaVision to NIfTI conversion . Contribute to neurolabusc/Bru2Nii development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>(also see the list of other conversion tools at the bottom of that page)</p>
<ul>
<li>Recent Slicer builds – not 4.8.1 – should open some .2dseq files directly thanks to an upstream ITK contribution:</li>
</ul>
<aside class="onebox discoursetopic" data-onebox-src="https://discourse.itk.org/t/nifti-orientation-issues/431">
  <header class="source">
      <img src="https://discourse.itk.org/uploads/default/optimized/1X/71db04d41479c229accbe8bf0b99195f75f46770_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.itk.org/t/nifti-orientation-issues/431" target="_blank" rel="noopener" title="08:25PM - 17 November 2017">ITK – 17 Nov 17</a>
  </header>

  <article class="onebox-body">
    <img src="https://discourse.itk.org/uploads/default/original/1X/8a8379ed42cbc60fb262a064faca192c7d7111e7.png" class="thumbnail onebox-avatar" width="500" height="500">

<div class="title-wrapper">
  <h3><a href="https://discourse.itk.org/t/nifti-orientation-issues/431" target="_blank" rel="noopener">NIFTI Orientation Issues</a></h3>
  <div class="topic-category">
    <div class="topic-header-extra">
      <div class="list-tags">
        <div class="discourse-tags">
          <svg class="fa d-icon d-icon-tag svg-icon svg-string"><use href="#tag"></use></svg>
            <span class="discourse-tag simple">nifti</span>
        </div>
      </div>
    </div>
  </div>
</div>

  <p>Hello,  I am having trouble with NIFTI orientations (again). I am using the Bruker reader I contributed to read in a 2dseq file and then save to NIFTI. When I then read that file with FSL or nibabel, the orientation comes back as different. This...</p>

  <p>
    <span class="label1">Reading time: 5 mins 🕑</span>
      <span class="label2">Likes: 10 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I just tested <code>File -&gt; Add Data -&gt; [select a .2dseq file]</code> in Slicer nightly build 2018-05-24, and Slicer I/O automatically detected and loaded the file. However, I believe only the first of the volumes in the 4D acquisition was loaded.</p>

---

## Post #4 by @virginia_fgc (2018-06-11 22:30 UTC)

<p>Hello,</p>
<p>Thank you both! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
I will check SIVIC more thoroughly; however, the files I need to open for now are not MRSI. I will be using MRSI data later on, but for now I need to open High Resolution T2w images.<br>
Regarding Isaiah’s reply, I will go for option 1 and see if it works. For now, the 3 versions I have installed of Slicer (including a recent nightly build version), I still have the same problem when adding 2dseq files: nothing happens when I select the “2dseq” file through Add Data. With ImageJ, I’ve seen what it looks like (so the file is not blank); however, I wonder if the problem might be that in ImageJ, I get all slices in the same window, not separated in a stack.</p>
<p>I will update this again as soon as I try all options.<br>
Thank you very much</p>
<p>Virginia</p>

---

## Post #5 by @virginia_fgc (2018-06-17 08:50 UTC)

<p>Hello,</p>
<p>I finally managed to open a perfect stack in ImageJ. I converted it to JPG and then was able to run it in Slicer and get my T2w images.<br>
I also tried using the Bru2Nii option and it worked as well; the problem is that it’s necessary to install Lazarus as well if you don’t have it, and if you only need Lazarus for that it’s sort of using a sledgehammer to crack a nut. However, it worked fine too. In case someone wants to use Lazarus-Bru2Nii, you need to convert the “acpq” file that is also present on the folder with the Bruker images (not ‘2dseq’).<br>
As per my research, SIVIC seems a great tool to handle MRSI data in Slicer, but it does not support Bruker files apparently (only Siemens).</p>
<p>Cheers <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #6 by @ihnorton (2018-06-17 20:22 UTC)

<aside class="quote no-group" data-username="virginia_fgc" data-post="5" data-topic="3131">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/virginia_fgc/48/3309_2.png" class="avatar"> virginia_fgc:</div>
<blockquote>
<p>I also tried using the Bru2Nii option and it worked as well; the problem is that it’s necessary to install Lazarus as well if you don’t have it, and if you only need Lazarus for that it’s sort of using a sledgehammer to crack a nut.</p>
</blockquote>
</aside>
<p>There are pre-compiled binaries on the <a href="https://github.com/neurolabusc/Bru2Nii/releases">releases</a> page.</p>

---

## Post #7 by @ihnorton (2018-06-25 13:47 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="3" data-topic="3131">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>I just tested <code>File -&gt; Add Data -&gt; [select a .2dseq file]</code> in Slicer nightly build 2018-05-24, and Slicer I/O automatically detected and loaded the file. However, I believe only the first of the volumes in the 4D acquisition was loaded.</p>
</blockquote>
</aside>
<p>Just to add a note here, I just tried this again and noticed it doesn’t work immediately after starting Slicer – it only works after running <code>import SimpleITK as sitk</code> in the Python interactor. I believe that doing so registers the Bruker I/O facility in ITK, which is probably not registered by default (we could change that if people find it useful).</p>

---

## Post #8 by @virginia_fgc (2018-06-25 21:29 UTC)

<p>I downloaded the version and tried it. I get a file imported but it’s blurry and zoomed.</p>
<p>I varied the Selection options but the preview did not improve.</p>
<p>The result is very different with the NII file.</p>
<p>Perhaps there’s some additional setting that needs to be done with the “2dseq file”.</p>
<p>When I get the volume shape, it’s the same, but both things look entirely different.</p>

---
