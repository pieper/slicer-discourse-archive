# Relative transform between linked 3D views

**Topic ID**: 30597
**Date**: 2023-07-14
**URL**: https://discourse.slicer.org/t/relative-transform-between-linked-3d-views/30597

---

## Post #1 by @mohammed_alshakhas (2023-07-14 08:54 UTC)

<p>i wish for the following to be possible<br>
in dual 3d screen synchronization work through moving in the same direction but not be a duplicate.</p>
<p>right now, if I click on sync, the other 3d view will replicate the original view which is not helpful in my opinion.  rather, both views stay in the same position but if I move one to the right, the other moves to the right relative to the origin.</p>
<p>a practical example, I would like to see how the skull looks like in frontal view when I airplane it to the left or right.</p>
<p>this would be extremely helpful for my workflow</p>
<p>thanks</p>

---

## Post #2 by @lassoan (2023-07-14 14:06 UTC)

<p>Do you load one model or two? Would you like the 3D viewers to show the skull in the same orientation? Maybe you could provide a few screenshots/sketches to explain.</p>
<p>If you want to have a better look of a single model then I would recommend to get a virtual reality headset. The immersive stereoscopic views and ability to hold the model in your hand and rotate it around is far better than multiple views on a regular 2D display.</p>

---

## Post #3 by @mohammed_alshakhas (2023-07-14 14:42 UTC)

<p>i only load one dicom.   I want two views to have different orientations like one basal view and another frontal view.  and I want to tweak the orientation of one and sync to the other.<br>
if sync just copies the other view  , this would serve no purpose.</p>
<p>I thought about VR but  I use Mac so it is out of the question.  but the feature I requested is much simpler and allows assessment and visualization much better.</p>
<p>in this picture, i want to rotate in coronal direction ( roll or airplane ) and want ot see how it looks in basal basal simultaneously</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8ca9854ff51e97d5813cfbad73ea85203b4f468e.jpeg" data-download-href="/uploads/short-url/k4m2CYvBnR0ffllFx58z4Ttwj7w.jpeg?dl=1" title="Screenshot 2023-07-14 at 17.39.47" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8ca9854ff51e97d5813cfbad73ea85203b4f468e_2_690x448.jpeg" alt="Screenshot 2023-07-14 at 17.39.47" data-base62-sha1="k4m2CYvBnR0ffllFx58z4Ttwj7w" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8ca9854ff51e97d5813cfbad73ea85203b4f468e_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8ca9854ff51e97d5813cfbad73ea85203b4f468e_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8ca9854ff51e97d5813cfbad73ea85203b4f468e_2_1380x896.jpeg 2x" data-dominant-color="5F6079"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-07-14 at 17.39.47</span><span class="informations">1920×1247 94.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2023-07-14 14:47 UTC)

<p>One way to do it is to load the image twice, drag-and-drop each into a separate view, and rotate one by 90 degrees using Transforms module.</p>
<p>If many people would vote on this feature request, i.e., want to make it easier to set up relative transform between linked cameras, then its development will be prioritized.</p>

---

## Post #5 by @mohammed_alshakhas (2023-07-14 14:49 UTC)

<p>I believe it’s a great yet very simple feature .<br>
I’d use for all my workflow</p>

---

## Post #6 by @muratmaga (2023-07-14 15:06 UTC)

<p>This is already available for volumes as <strong>QuickAlign</strong> module of SlicerMorph (just got merged after the last PW).</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/RenderingSupportForMultipleViews/">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/RenderingSupportForMultipleViews/" target="_blank" rel="noopener">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/RenderingSupportForMultipleViews/" target="_blank" rel="noopener">Project Description</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2023-07-14 16:03 UTC)

<p>The project week project is for aligning multiple volumes. This request is for viewing one volume from different orientations (linking views with relative transform between them).</p>

---

## Post #8 by @muratmaga (2023-07-14 16:49 UTC)

<p>I know, as a simple solution they can clone the volume (until there is abetter solution).</p>

---
