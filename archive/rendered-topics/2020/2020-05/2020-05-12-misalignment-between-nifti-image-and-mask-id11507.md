---
topic_id: 11507
title: "Misalignment Between Nifti Image And Mask"
date: 2020-05-12
url: https://discourse.slicer.org/t/11507
---

# Misalignment between Nifti image and mask

**Topic ID**: 11507
**Date**: 2020-05-12
**URL**: https://discourse.slicer.org/t/misalignment-between-nifti-image-and-mask/11507

---

## Post #1 by @Bassam (2020-05-12 08:13 UTC)

<p>Hi, Thanks for your kind reply.<br>
The problem has been sorted out and I successfully uploaded the mask file, but another problem popped up, which misalignment between the structure in the original image (in my case it is the pancreas) and the mask file (segmented pancreas). I pressed apply button for extracting the features, but unfortunately no output features, i think because of that misalignment. I matched the spatial resolution between the image and the mask files, but it did not work.</p>
<p>Please any idea on who to sort this out ? and thanks</p>

---

## Post #2 by @lassoan (2020-05-12 18:54 UTC)

<p>Do you load a grayscale image and segmentation from nifti files and they are not aligned?<br>
Could you please share at least a sample image, but preferably a sample data set? (upload it somewhere and post the link)</p>

---

## Post #3 by @Bassam (2020-05-12 23:11 UTC)

<p>The images in DICOM format, while the segmentation in nifti format.</p>
<p>Kindly, the link for the images is:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/bassamabunahel/Test/blob/master/image.zip" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/bassamabunahel/Test/blob/master/image.zip" target="_blank" rel="nofollow noopener">bassamabunahel/Test/blob/master/image.zip</a></h4>
<pre><code class="lang-zip">version https://git-lfs.github.com/spec/v1
oid sha256:62068d20f54057d1135c63b2eff687efce8dd190ea238071cfab3a5c45e81893
size 106061894
</code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>and for the mask nifti file is:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/bassamabunahel/Test/blob/master/mask.nii" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/bassamabunahel/Test/blob/master/mask.nii" target="_blank" rel="nofollow noopener">bassamabunahel/Test/blob/master/mask.nii</a></h4>
<pre><code class="lang-nii">version https://git-lfs.github.com/spec/v1
oid sha256:bcbff313c61e8f40690d2b35267163e609b0139acc5ab492a4d4ee4c7dc67015
size 5964128
</code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Kindly, since the files are big in size, you may need to either click ‘View raw’ or ‘Download’ button to see the attached files.</p>
<p>Kindly, from the attached image file, I used (t1_vibe_obl_d_Panc_5mm_512_opp) image sequence to create the mask file (segmentation)(nifti file) using ITK snap.</p>
<p>I am using image J to show the mask file, while for the image, MicroDicom is used.</p>
<p>Appreciated</p>

---
