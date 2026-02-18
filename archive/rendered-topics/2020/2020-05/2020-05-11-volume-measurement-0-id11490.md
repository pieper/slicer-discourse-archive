# Volume measurement = 0

**Topic ID**: 11490
**Date**: 2020-05-11
**URL**: https://discourse.slicer.org/t/volume-measurement-0/11490

---

## Post #1 by @Gaborri (2020-05-11 07:21 UTC)

<p>Hello there,</p>
<p>I am a new user. Windows 10 and Slicer 4.10.1 version.</p>
<p>I have a problem in measuring a volume.<br>
I have the segmentation done and it is displayed correctly in the 3d views.<br>
Unfortunately when I go for Quantification and segment statistics it display to me 0 volume.<br>
With another scene and segmentation I have not such problem…<br>
I cannot really find where I am wrong. Could you please give me a piece of advice?</p>
<p>All the best</p>

---

## Post #2 by @lassoan (2020-05-12 03:33 UTC)

<p>Volume can be computed from binary labelmap and closed surface representations. Do you get 0 value from both?</p>
<p>Can you share the segmentation file (upload somewhere and post the link here) so that we can investigate?</p>

---

## Post #3 by @Gaborri (2020-05-12 07:15 UTC)

<p>Ok I am attaching here the link of the segmentation (data set and the scene) that actually works:</p>
<p><aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/139kwEx4vRhTSCxZevONGrXraKS8kaE8f/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/139kwEx4vRhTSCxZevONGrXraKS8kaE8f/view?usp=sharing" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/139kwEx4vRhTSCxZevONGrXraKS8kaE8f/view?usp=sharing" target="_blank" rel="nofollow noopener">2020-04-27-Scene.mrml</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1rHyA6-KRQSr6cS2CJ-KjE7nB2MJ5_Q_d/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1rHyA6-KRQSr6cS2CJ-KjE7nB2MJ5_Q_d/view?usp=sharing" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1rHyA6-KRQSr6cS2CJ-KjE7nB2MJ5_Q_d/view?usp=sharing" target="_blank" rel="nofollow noopener">Segmentation_1_2.seg.nrrd</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>and here the one that does not:<br>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1wZOrk75gwJjlLUChZFxu2jX27tarrTzo/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1wZOrk75gwJjlLUChZFxu2jX27tarrTzo/view?usp=sharing" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1wZOrk75gwJjlLUChZFxu2jX27tarrTzo/view?usp=sharing" target="_blank" rel="nofollow noopener">Segmentation.seg.nrrd</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1sYcc1mJkUoscclW_Z1Zp0a3JYReJijSM/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1sYcc1mJkUoscclW_Z1Zp0a3JYReJijSM/view?usp=sharing" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1sYcc1mJkUoscclW_Z1Zp0a3JYReJijSM/view?usp=sharing" target="_blank" rel="nofollow noopener">2020-05-02-Scene.mrml</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>Once I open the scene and the data set, export the segments in models… and from there I see the information on the model where you can find volume ecc…</p>
<p>I did the same on the segment statistics tool but it gives me the same.<br>
I am wondering if the dataset that does not work is due to some problems in grow from seed (such as the surface is not closed, but I do not understand then the difference with respect to the other one).</p>
<p>Thank you so much</p>

---

## Post #4 by @manjula (2020-05-12 12:46 UTC)

<p>it gives volume for volume info for all 3 segments out of 4.</p>
<p>Only the segment “major ampullate” doest not give the volume or comes as 0 but that is because there is noting there. that segment is empty so it is 0</p>

---

## Post #5 by @Gaborri (2020-05-12 13:24 UTC)

<p>Thank you manjula,<br>
but how is it possible that I actually see the segment but it is not there? The file looks good (at least equal to the other one).</p>
<p>Thank you very much</p>

---

## Post #6 by @manjula (2020-05-12 18:38 UTC)

<p>I don’t see that segment in 3D View. In your given data. you have two segments with the same name “segmentation”  and the same kind of segments. So actually you must have two<br>
Segmentation.seg.nrrd  files. If you are seen the ampulla in 3d view it must have been rendered from the other segment with the same name. But it is clearly not the one you have shared<br>
So if you are seen the ampulla it must be on the other segment. If you select that segment and to it should work<br>
. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09eb78759341b37d564f123d21f9df2f90c88670.png" data-download-href="/uploads/short-url/1pKN0RIBKTL1ZyqxyjFZuQQqkhi.png?dl=1" title="2020-05-12-203642_1920x1080_scrot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09eb78759341b37d564f123d21f9df2f90c88670_2_690x388.png" alt="2020-05-12-203642_1920x1080_scrot" data-base62-sha1="1pKN0RIBKTL1ZyqxyjFZuQQqkhi" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09eb78759341b37d564f123d21f9df2f90c88670_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09eb78759341b37d564f123d21f9df2f90c88670_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/09eb78759341b37d564f123d21f9df2f90c88670_2_1380x776.png 2x" data-dominant-color="CACBE3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2020-05-12-203642_1920x1080_scrot</span><span class="informations">1920×1080 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2020-05-12 18:40 UTC)

<p>Data module gives a good overview of all data that is loaded into the scene.</p>

---

## Post #8 by @Gaborri (2020-05-13 07:28 UTC)

<p>Hello, I am afraid that is not the problem.<br>
In the first case, I upload the scene and the segmentation data set and I obtain this, where i see both segments and also the relative volume in the segment statistics…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2fe022bfb41279ab872adbd0670130a84fbae50.jpeg" data-download-href="/uploads/short-url/yFBL1JljeQxwUbThvnwoS1Nywa4.jpeg?dl=1" title="Cattura" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2fe022bfb41279ab872adbd0670130a84fbae50_2_690x472.jpeg" alt="Cattura" data-base62-sha1="yFBL1JljeQxwUbThvnwoS1Nywa4" width="690" height="472" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2fe022bfb41279ab872adbd0670130a84fbae50_2_690x472.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2fe022bfb41279ab872adbd0670130a84fbae50_2_1035x708.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2fe022bfb41279ab872adbd0670130a84fbae50_2_1380x944.jpeg 2x" data-dominant-color="D6D1C7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Cattura</span><span class="informations">1511×1034 90.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>for the other, i can upload the file as before (so the scene and the segmentation one) or both of them, but I still obtain the same… so I can visualise the thing that I am studying but I cannot measure the volume<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/668216581ad8d97c6429661429a362dbeac66707.jpeg" data-download-href="/uploads/short-url/eCPpAqoIYGjTnALDXgshyXKEmXB.jpeg?dl=1" title="Cattura1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/668216581ad8d97c6429661429a362dbeac66707_2_668x500.jpeg" alt="Cattura1" data-base62-sha1="eCPpAqoIYGjTnALDXgshyXKEmXB" width="668" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/668216581ad8d97c6429661429a362dbeac66707_2_668x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/668216581ad8d97c6429661429a362dbeac66707_2_1002x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/668216581ad8d97c6429661429a362dbeac66707.jpeg 2x" data-dominant-color="C0B3C1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Cattura1</span><span class="informations">1327×993 58.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7d2d684f54fccbab8019ab2b18b641af7c4d5bc.jpeg" data-download-href="/uploads/short-url/qeb5UwXLSEQ8S7m4KCb2ARzoyCM.jpeg?dl=1" title="Cattura2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7d2d684f54fccbab8019ab2b18b641af7c4d5bc_2_690x336.jpeg" alt="Cattura2" data-base62-sha1="qeb5UwXLSEQ8S7m4KCb2ARzoyCM" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7d2d684f54fccbab8019ab2b18b641af7c4d5bc_2_690x336.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7d2d684f54fccbab8019ab2b18b641af7c4d5bc_2_1035x504.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7d2d684f54fccbab8019ab2b18b641af7c4d5bc_2_1380x672.jpeg 2x" data-dominant-color="B7B9DB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Cattura2</span><span class="informations">1920×936 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aedb160861e4b4c608b09124844e867b6635390c.jpeg" data-download-href="/uploads/short-url/oWQt764V5x5OjHZ4W2CUBHk2jrC.jpeg?dl=1" title="Cattura3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aedb160861e4b4c608b09124844e867b6635390c_2_690x407.jpeg" alt="Cattura3" data-base62-sha1="oWQt764V5x5OjHZ4W2CUBHk2jrC" width="690" height="407" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aedb160861e4b4c608b09124844e867b6635390c_2_690x407.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aedb160861e4b4c608b09124844e867b6635390c_2_1035x610.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aedb160861e4b4c608b09124844e867b6635390c_2_1380x814.jpeg 2x" data-dominant-color="F9F8F9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Cattura3</span><span class="informations">1700×1005 69.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>as you can see here… even though you clearily see the gland, the volume is 0, which is strange and makes me think that I am doing something wrong.</p>
<p>Moreover, I would stress also the attention on a thing… if you notice in the first picture that I have uploaded the volume of the gland is bigger than the one of the space. This is very unlikely since the space contain the gland and it is clearily bigger…<br>
I would be very gratefull if you suggest me something and how to eventually fix this problem.</p>
<p>In the data module, I see all the segments…<br>
I am really appreciating this fruitful discussion and I am sorry if I seem dumb to you.</p>
<p>All the best</p>

---

## Post #9 by @Gaborri (2020-05-15 07:33 UTC)

<p>No comments?</p>
<p>I am really curious about my mistakes<br>
<img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji only-emoji" alt=":slight_smile:"></p>

---

## Post #10 by @lassoan (2020-05-23 05:10 UTC)

<p>Finally I had time to look at your data sets.</p>
<p>I’ve noticed one issue: Both segmentations only contain seeds, not the final segmentation result. It is important that when you are happy with preview results that the “Grow from seed” effect shows you, switch to “Grow from seeds” effect and click “Apply”.</p>
<p>I’ve also noticed that your segmentations are very big and you are probably using “Grow from seeds” effect, which uses lots of memory. So, there is a good chance that you run out of memory. To confirm this, you can crop&amp;downsample your input image by setting scaling factor of 2-3x in “Crop Volume” module and see if it makes a difference. If it does then you can try to increase virtual memory setting in your computer and try with a smaller scaling factor increase.</p>

---
