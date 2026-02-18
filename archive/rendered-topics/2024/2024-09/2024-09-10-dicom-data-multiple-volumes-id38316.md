# Dicom data multiple volumes 

**Topic ID**: 38316
**Date**: 2024-09-10
**URL**: https://discourse.slicer.org/t/dicom-data-multiple-volumes/38316

---

## Post #1 by @windrunner (2024-09-10 14:18 UTC)

<p>I like many others am trying to 3D print my brain using the MRI data that I received. I have found many tutorials and helpful information but still am struggling to figure out how to make the best model for printing.<br>
The issue arises with the data itself. Looking through the Dicom there are multiple entries (volumes?) for the scans and when you look at them some have better resolution in one axis vs the other. I am able to use the extension Swiss skull stripper and get to the point of segment editor and when I create a 3d model, it looks great on one axis but when you rotate it, it has less resolution on the other axis. I can use the extension to go through each data file and then select each of those new segments to be in individual window, but when i go to create a 3d model of it, it will only allow me to choose one volume which makes sense. Is there a way edit the data to include the data from the 3 different data sets into one volume so i end up with the best 3d rendering.</p>
<p>I hope this makes sense. I attached some screen shots to try and show what I am seeing. Any help that you can provide would be appreciated.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce49934310feab0230713c52bad99c020519b811.jpeg" data-download-href="/uploads/short-url/tqTZzDtyr5F4dBwX57rdInhRiQF.jpeg?dl=1" title="3d model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce49934310feab0230713c52bad99c020519b811_2_690x299.jpeg" alt="3d model" data-base62-sha1="tqTZzDtyr5F4dBwX57rdInhRiQF" width="690" height="299" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce49934310feab0230713c52bad99c020519b811_2_690x299.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce49934310feab0230713c52bad99c020519b811_2_1035x448.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce49934310feab0230713c52bad99c020519b811_2_1380x598.jpeg 2x" data-dominant-color="44484E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3d model</span><span class="informations">1920×834 66.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/1680110c6266b6ac943c0330da1cb65e0fdc33f1.jpeg" data-download-href="/uploads/short-url/3d2SUSwUtN11eq3vrdhZGzClghX.jpeg?dl=1" title="1 volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/1680110c6266b6ac943c0330da1cb65e0fdc33f1_2_689x311.jpeg" alt="1 volume" data-base62-sha1="3d2SUSwUtN11eq3vrdhZGzClghX" width="689" height="311" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/1680110c6266b6ac943c0330da1cb65e0fdc33f1_2_689x311.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/1680110c6266b6ac943c0330da1cb65e0fdc33f1_2_1033x466.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/1680110c6266b6ac943c0330da1cb65e0fdc33f1_2_1378x622.jpeg 2x" data-dominant-color="464650"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1 volume</span><span class="informations">2721×1228 246 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e8b15679ee82228c0117ed05fa584638b007c42.jpeg" data-download-href="/uploads/short-url/6DJWPAQ7EdXQ4upqpCym3RPurmy.jpeg?dl=1" title="swiss skull removal" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e8b15679ee82228c0117ed05fa584638b007c42_2_690x297.jpeg" alt="swiss skull removal" data-base62-sha1="6DJWPAQ7EdXQ4upqpCym3RPurmy" width="690" height="297" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e8b15679ee82228c0117ed05fa584638b007c42_2_690x297.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e8b15679ee82228c0117ed05fa584638b007c42_2_1035x445.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e8b15679ee82228c0117ed05fa584638b007c42_2_1380x594.jpeg 2x" data-dominant-color="454850"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">swiss skull removal</span><span class="informations">2783×1200 257 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e199dbecc28e26c842f174cda35230d91be40176.png" alt="3 different volumes" data-base62-sha1="wbL4ulYeLc1cZ56P16gJr31eNhk" width="624" height="274"></p>

---

## Post #2 by @pieper (2024-09-10 16:04 UTC)

<p>This thread should help explain what’s going on:</p>
<aside class="quote" data-post="1" data-topic="27089">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/audrina_fernandez/48/17933_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/merge-3-mri-volumes-with-different-orientations-into-one/27089">Merge 3 MRI volumes with different orientations into one</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
I’m working on MRI to segment cheek fat volume and often I have one serie of few images for axial axe, one serie for coronal axe, one serie for sagittal axe (for one patient, one IRM). To get a better volume segmentation I would like to stitch these series. Stitch volume module can help me to match differents axes or it is for differents series of the same axe? 
Sorry for my English <img width="20" height="20" src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title="slight_smile" alt="slight_smile" class="emoji">
  </blockquote>
</aside>

<p>For 3D printing you may also want to look at using <a href="https://github.com/BBillot/SynthSeg">SynthSeg</a> for segmentation.</p>

---
