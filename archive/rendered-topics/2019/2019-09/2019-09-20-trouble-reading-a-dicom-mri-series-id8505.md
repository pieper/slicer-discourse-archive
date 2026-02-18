# Trouble reading a DICOM MRI series

**Topic ID**: 8505
**Date**: 2019-09-20
**URL**: https://discourse.slicer.org/t/trouble-reading-a-dicom-mri-series/8505

---

## Post #1 by @Nathan (2019-09-20 11:53 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.5, 4.8<br>
Expected behavior: Reads in DICOM MRI series as a single volume<br>
Actual behavior: Reads each image into an individual volume</p>
<p>Hi,</p>
<p>This MRI series is not being read in as a volume. Each image is being put into an individual volume. Any ideas on what’s going on and how to fix it?</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="16" height="16">
      <a href="https://www.dropbox.com/s/hol19w2207f7ls8/005.zip?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-zip-large.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://www.dropbox.com/s/hol19w2207f7ls8/005.zip?dl=0" target="_blank" rel="nofollow noopener">005.zip</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #2 by @Chris_Rorden (2019-09-20 13:31 UTC)

<p>These slices are not combined because the DICOM headers report they are from different studies (0020,000d) and from different series (0020,000e). I would check the providence of these images, and see if you can get earlier copies of the images before these tags were manipulated.</p>
<p>Based on 0002,0013, I suspect these images were mangled by a Matlab script (potentially attempting to anonymize data). The DICOM format is extremely complex, and this makes DICOM images fragile to manipulation. Personally, I am a fan of <a href="http://gdcm.sourceforge.net/html/gdcmanon.html" rel="noopener nofollow ugc">gdcmanon</a>.</p>
<blockquote>
<p>(0002,0013) SH [MATLAB IPT 7.1]                         #  14, 1 ImplementationVersionName</p>
</blockquote>
<p>Instance Number 1:</p>
<pre><code>(0020,000d) UI [1.3.6.1.4.1.9590.100.1.2.380037498713055046739759443493873218136] #  64, 1 StudyInstanceUID
(0020,000e) UI [1.3.6.1.4.1.9590.100.1.2.331408360012808881138554615400916651736] #  64, 1 SeriesInstanceUID
</code></pre>
<p>Instance Number 2:</p>
<pre><code>(0020,000d) UI [1.3.6.1.4.1.9590.100.1.2.222023342810310160709387564850599174001] #  64, 1 StudyInstanceUID
(0020,000e) UI [1.3.6.1.4.1.9590.100.1.2.385511264811362958821958401890266751484] #  64, 1 SeriesInstanceUID
</code></pre>

---

## Post #3 by @Nathan (2019-09-20 13:42 UTC)

<p>Hmm - interesting. I get the same behavior with the original non-anonomized images. They are from another site, so I don’t know about how they were obtained.</p>
<p>I can try changing the DICOM fields in Matlab. Would changing (0020,000d) and (0020,000e) be enough for Slicer?</p>
<p>I could also try saving them in another format (nrrd, nifti?). I would need to save the spatial information.</p>
<p>Thanks,<br>
Nathan</p>

---

## Post #4 by @Nathan (2019-09-20 19:07 UTC)

<p>That fixed it.</p>
<p>Thanks again!</p>

---
