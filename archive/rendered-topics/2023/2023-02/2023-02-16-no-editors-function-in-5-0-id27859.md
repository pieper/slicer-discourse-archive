# No 'editor's function in 5.0

**Topic ID**: 27859
**Date**: 2023-02-16
**URL**: https://discourse.slicer.org/t/no-editors-function-in-5-0/27859

---

## Post #1 by @Fumi (2023-02-16 11:55 UTC)

<p>Operating system:Diffusion MRI<br>
Slicer version:5.0.3<br>
Expected behavior:Editor module was in Slicer 4.0<br>
Actual behavior:No botton corresponding ‘editor’ in modules.</p>

---

## Post #2 by @pieper (2023-02-16 13:31 UTC)

<p>The Editor was removed so we could focus on the newer <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html">Segment Editor</a> with more powerful functions.</p>

---

## Post #3 by @Fumi (2023-02-18 08:38 UTC)

<p>Hi Steve,</p>
<p>Thank you for a quick reply. Would you tell me if I can use the Segment Editor for ROI seeding, tensor scalar measurement while DTI tractography? I couldn’t find any manuals for ver. 5.0 as to tractography. Any advices would be appreciated about this topic.<br>
Thank you for your kindness.</p>
<p>Sincerely,<br>
Fumi</p>

---

## Post #4 by @pieper (2023-02-18 16:42 UTC)

<p>Yes, all of those functions should be working in the current release version 5.2.1 and the corresponding SlicerDMRI extension.  Let us know if something’s not working as expected for you.</p>

---

## Post #5 by @Fumi (2023-02-19 08:08 UTC)

<p>OK, I’ll try using Segmentation editor tool. I appreciate your kind support.</p>

---

## Post #6 by @Fumi (2023-02-20 06:28 UTC)

<p>Hi Steve,</p>
<p>Now I am trying to do DTI tractography with DMRI, and struggling with tractography seeding because I cannot make FA-label map during segmentation editing. Then cannot select FA-label at “Input Fiducials. model or Label Map” in Seeding. There is only a “Select a Point List” option at that window. Would you tell me how to deal with this problem?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f325a3cec33203b595646fba3161591dd84cfe43.png" data-download-href="/uploads/short-url/yGYFreR43zjYErwRDyHIuh9Bn0v.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f325a3cec33203b595646fba3161591dd84cfe43_2_690x491.png" alt="image" data-base62-sha1="yGYFreR43zjYErwRDyHIuh9Bn0v" width="690" height="491" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f325a3cec33203b595646fba3161591dd84cfe43_2_690x491.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f325a3cec33203b595646fba3161591dd84cfe43_2_1035x736.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f325a3cec33203b595646fba3161591dd84cfe43_2_1380x982.png 2x" data-dominant-color="757575"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1520×1082 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What I want to do is to draw manual ROI tractography, and whole brain tractography with UKF tractography.</p>
<p>Thank you,</p>

---

## Post #7 by @pieper (2023-02-20 16:09 UTC)

<p>Ah, you’re right, the seeding hasn’t been updated to work with Segmentations so you’ll need to export the segmentation to a label map.  What you can do is go to the Data module and right click on the segmentation and pick “Export visible segments to binary labelmap” and you can use the resulting labelmap for seeding.</p>

---

## Post #8 by @Fumi (2023-02-21 00:16 UTC)

<p>Thank you for your advice. I’ll try the Data module function. I appreciate your kind supports.</p>

---

## Post #9 by @Fumi (2023-02-22 02:17 UTC)

<p>Hi Steve,</p>
<p>I tryed Data module, and successed to create a label map file. Then I go to the next step4 “Undesirable track removal”, as in the DMRI manuals, Slicer fell off when I choose the ROI node button.<br>
Is this a bug? I experienced the same phenomenon in the Slicer 4.11 for Windows/ Linux as well during the same process. Do you have any idea to avoid this error?</p>
<p>Thank you,</p>

---

## Post #10 by @pieper (2023-02-23 15:45 UTC)

<p>I guess you mean step 4 from this tutorial?</p>
<aside class="onebox pdf" data-onebox-src="https://dmri.slicer.org/tutorials/Slicer-4.8/DiffusionMRIAnalysis.pdf">
  <header class="source">

      <a href="https://dmri.slicer.org/tutorials/Slicer-4.8/DiffusionMRIAnalysis.pdf" target="_blank" rel="noopener">dmri.slicer.org</a>
  </header>

  <article class="onebox-body">
    <a href="https://dmri.slicer.org/tutorials/Slicer-4.8/DiffusionMRIAnalysis.pdf" target="_blank" rel="noopener"><span class="pdf-onebox-logo"></span></a>

<h3><a href="https://dmri.slicer.org/tutorials/Slicer-4.8/DiffusionMRIAnalysis.pdf" target="_blank" rel="noopener">DiffusionMRIAnalysis.pdf</a></h3>

  <p class="filesize">46.88 MB</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Which exact feature is not working for you?  For me the features seem to be working as expected on linux with 5.2.1 with sample dti data.</p>

---

## Post #11 by @Fumi (2023-02-27 01:58 UTC)

<p>I am sorry for late reply. Yes, I used that DiffusionMRI manual and was doing Undesireble tract removal. Because I could not use the sample data set, I am using my own MRI data set.<br>
When I put the button of ‘ROI node’ and chose the 'Create New annotationROI as… ’ , then Slicer 5.0 for windows fell off. This phenomenon is repeatable.</p>

---

## Post #12 by @lassoan (2023-02-27 15:01 UTC)

<p>Please use the latest Slicer Stable Release (currently Slicer-5.2.2) and let us know if you still find problems.</p>

---

## Post #13 by @pieper (2023-02-27 17:24 UTC)

<p><a class="mention" href="/u/fumi">@Fumi</a> I tried the 5.2.2 release with the latest SlicerDMRI extension (available today for Windows).  I was able to extract fibers using an ROI.  Also, just to be sure we understand, when you say Slicer “fell off” you mean crashed?</p>

---

## Post #14 by @Fumi (2023-02-28 02:14 UTC)

<p>Hi Andras,<br>
Thank you for your advice. I will try ver. 5.2.2.</p>

---

## Post #15 by @Fumi (2023-02-28 02:18 UTC)

<p>Hi Steve,</p>
<p>Thank you for your advice again. I wiall try Slicer 5.2.2 and latest Slicer DMRI. I meant that PC was  ‘crashed’ soon after I pushed the button. Sorry for my bad English.</p>

---

## Post #16 by @pieper (2023-02-28 13:09 UTC)

<p>Thanks for the clarification and definitely let us know if it’s still happening so we can look into this.</p>

---

## Post #17 by @Fumi (2023-03-01 07:59 UTC)

<p>I succeeded in removing track in 5.2.2 ! Thank you so much for your support!</p>
<p>I would  like to ask about the next step ‘Fiducial seeding’. In slicer 5.2.2 the Markups module has toolbar, I didn’t understand which function should I use for fuducial seeding. Any advice would be appreciated.</p>

---

## Post #18 by @pieper (2023-03-01 19:07 UTC)

<p>That’s now available in the Tractography Seeding module, and Fiducials are now Markups point lists.  Unfortunately there’s hasn’t been anyone working on updating the SlicerDMRI tutorials with these changes.  If you would be willing, it would be great it you would provide and updated tutorial or some note for future users who might run into these same issues.</p>

---

## Post #19 by @Fumi (2023-03-06 10:12 UTC)

<p>Thank you Steve, now I am using Markup point list for Fiducials.<br>
Yes,  it is really disappointing we have no new tutrials for SlicerDMRI, but it must be too big deal for<br>
a begginer user to create new manuals… I appreciate to your sapport for my problems many times.</p>

---
