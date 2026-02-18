# How to make a "mandible template"from many mandibles in slicermorph?

**Topic ID**: 38241
**Date**: 2024-09-05
**URL**: https://discourse.slicer.org/t/how-to-make-a-mandible-template-from-many-mandibles-in-slicermorph/38241

---

## Post #1 by @yijie3091 (2024-09-05 15:43 UTC)

<p>How to make a "mandible template"from many mandibles in slicermorph to match others?</p>

---

## Post #2 by @muratmaga (2024-09-05 19:39 UTC)

<p>The answer to this depends on what modality you have the data in.</p>
<p>If you have 3D models and at least some landmarks, you can use our DeCa extension to generate template. This is an iterative process where a model is used to as a reference to rigidly align all the others, and then use the rigidly aligned ones to generate a population template.</p>
<p>You can find the paper at: <a href="https://www.researchgate.net/publication/375111739_DeCA_A_Dense_Correspondence_Analysis_Toolkit_for_Shape_Analysis" rel="noopener nofollow ugc">https://www.researchgate.net/publication/375111739_DeCA_A_Dense_Correspondence_Analysis_Toolkit_for_Shape_Analysis</a></p>
<p>DeCA is not part of the extension catalogue yet, but you can download the repository and manually install the extension.</p>
<p>If you do not have 3D models and landmarks, but volumetric data (e.g., CT scans), you will need to us an atlas-building framework, such as the one provided by ANTs.</p>
<p><a href="https://github.com/ANTsX/ANTS?tab=readme-ov-file" class="inline-onebox" rel="noopener nofollow ugc">GitHub - ANTsX/ANTs: Advanced Normalization Tools (ANTs)</a> (scroll down to find the tutorial for Brian Template)</p>

---

## Post #3 by @yijie3091 (2024-09-06 11:06 UTC)

<p>I have some mandibles whose foremat is ply.,so as follows as your mean,i can use the the DeCa extension ,right?<br>
And i make some fixed landmarks manually to make the template aligh more precisely, is it necessary?</p>

---

## Post #4 by @muratmaga (2024-09-06 16:37 UTC)

<p>If you have 3D models, yes you can use DeCa. Anatomical (fixed) landmarks makes challenging registration problems a little easier. You don’t have to have a lot of them, anywhere from 6-10 should be sufficient.</p>

---

## Post #5 by @yijie3091 (2024-09-08 07:08 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97506df18ada2fca497ea76418497d4df5fd0f8f.png" data-download-href="/uploads/short-url/lAApSomxgmPVtx6x0qJDeGfKJrh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97506df18ada2fca497ea76418497d4df5fd0f8f_2_690x459.png" alt="image" data-base62-sha1="lAApSomxgmPVtx6x0qJDeGfKJrh" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97506df18ada2fca497ea76418497d4df5fd0f8f_2_690x459.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97506df18ada2fca497ea76418497d4df5fd0f8f_2_1035x688.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97506df18ada2fca497ea76418497d4df5fd0f8f_2_1380x918.png 2x" data-dominant-color="F6F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1713×1141 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb90617d8b8b1af1377585a18474f73e1426856a.png" data-download-href="/uploads/short-url/qLgCwSUxGs3mxpqewS2PdoCI2ng.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb90617d8b8b1af1377585a18474f73e1426856a_2_690x285.png" alt="image" data-base62-sha1="qLgCwSUxGs3mxpqewS2PdoCI2ng" width="690" height="285" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb90617d8b8b1af1377585a18474f73e1426856a_2_690x285.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb90617d8b8b1af1377585a18474f73e1426856a_2_1035x427.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb90617d8b8b1af1377585a18474f73e1426856a.png 2x" data-dominant-color="F8E1E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1099×454 30.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is there a mistake in my steps？I can’t download it in my slicer.</p>

---

## Post #6 by @muratmaga (2024-09-08 17:20 UTC)

<p>The chinese characters in the path might be playing tricks. Instead unzip the file, and drag the DeCa folder inside the zip archive  (not the DeCa-main) to Slicer application window. Then answer OK, to <strong>Add Python scripted modules to the application</strong>. Then, you are set.</p>

---

## Post #7 by @yijie3091 (2024-09-15 07:04 UTC)

<p>Thank you very much.I have mandible datas such as this picture,but this "generate tab"show aligned mesh directory.Do I need make mesh?How can I make mesh?Do you have some video tutorial which can help me,because github can’t show tutorial step by step.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a5e161dc434814a59dd7ce00753a62163a47c3f.png" data-download-href="/uploads/short-url/3LfZAC8j73jAmeb8YKUY6uSyJPx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a5e161dc434814a59dd7ce00753a62163a47c3f_2_437x500.png" alt="image" data-base62-sha1="3LfZAC8j73jAmeb8YKUY6uSyJPx" width="437" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a5e161dc434814a59dd7ce00753a62163a47c3f_2_437x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a5e161dc434814a59dd7ce00753a62163a47c3f_2_655x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a5e161dc434814a59dd7ce00753a62163a47c3f_2_874x1000.png 2x" data-dominant-color="F7F7F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1293×1477 59.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e3e73a3e1bcf3196ad7a5affbb49d5b1526a3ab.png" data-download-href="/uploads/short-url/fJgk5eesyTrNHX0x1l2Ljt3xQJJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e3e73a3e1bcf3196ad7a5affbb49d5b1526a3ab_2_645x500.png" alt="image" data-base62-sha1="fJgk5eesyTrNHX0x1l2Ljt3xQJJ" width="645" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e3e73a3e1bcf3196ad7a5affbb49d5b1526a3ab_2_645x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e3e73a3e1bcf3196ad7a5affbb49d5b1526a3ab.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e3e73a3e1bcf3196ad7a5affbb49d5b1526a3ab.png 2x" data-dominant-color="9A9AB5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">867×672 67.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @muratmaga (2024-09-15 17:04 UTC)

<p>We are going to change and simplify the UI, so there is currently no tutorial.</p>
<p>Before you can generate mean model, you need to align all your samples using a reference model and a set of landmarks. Once you accomplish that those two fields in the Generate Mean (aligned mesh directory, and aligned landmark directory) will be auto-populated.</p>
<p>To run Rigid alignment:</p>
<ol>
<li>Choose one model and its corresponding landmark as reference.</li>
<li>Specify the input model directory</li>
<li>Specify the input landmark directory (note that filename prefixes for models and landmarks needs to be the same. That’s how matching is done)</li>
<li>Specify the output folders for aligned models and landmarks.</li>
</ol>
<p>then run rigid alignment. This should be quick, from then, you can switch to the mean model and generate your template.</p>

---
