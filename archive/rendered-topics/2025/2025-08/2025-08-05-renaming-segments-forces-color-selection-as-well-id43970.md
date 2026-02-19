---
topic_id: 43970
title: "Renaming Segments Forces Color Selection As Well"
date: 2025-08-05
url: https://discourse.slicer.org/t/43970
---

# Renaming Segments forces color selection as well

**Topic ID**: 43970
**Date**: 2025-08-05
**URL**: https://discourse.slicer.org/t/renaming-segments-forces-color-selection-as-well/43970

---

## Post #1 by @tsehrhardt (2025-08-05 12:14 UTC)

<p>I used to be able to double-click a segment name in Segment Editor to change ONLY the name. Now when double-clicking, the box to change color and name both pop up, but requires me to select a color as well or else it will change to whatever color gets auto-selected. This is in 5.8.1 but I believe it was implemented in the previous stable release.</p>
<p>Please change it back to how it was where I could just double-click the name and change only the name!</p>

---

## Post #2 by @muratmaga (2025-08-05 17:11 UTC)

<p>This was introduced to promote use of standard and custom terminologies. If you want the old behavior, you can bring it back by going to Edit→Application Settings→Segmentation</p>
<p>and uncheck “Use standard terminologies for segments”</p>

---

## Post #3 by @tsehrhardt (2025-08-05 17:29 UTC)

<p>Thank you! That works, although the hover message of “invalid terminology information” is annoying but I can live with it.</p>

---

## Post #4 by @muratmaga (2025-08-05 17:57 UTC)

<aside class="quote no-group" data-username="tsehrhardt" data-post="3" data-topic="43970">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>although the hover message of “invalid terminology information” is annoying but I can live with it.</p>
</blockquote>
</aside>
<p>I haven’t seen that before, can you describe or provide a screenshot along with your slicer version/OS?</p>

---

## Post #5 by @tsehrhardt (2025-08-05 18:15 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65997d50d1b631211719f4b018febf5caab8cfbf.jpeg" data-download-href="/uploads/short-url/euN4BxOVSDgF9v8mhsx3jmspoon.jpeg?dl=1" title="2025-08-05_14-13-04" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65997d50d1b631211719f4b018febf5caab8cfbf_2_690x356.jpeg" alt="2025-08-05_14-13-04" data-base62-sha1="euN4BxOVSDgF9v8mhsx3jmspoon" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65997d50d1b631211719f4b018febf5caab8cfbf_2_690x356.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65997d50d1b631211719f4b018febf5caab8cfbf_2_1035x534.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65997d50d1b631211719f4b018febf5caab8cfbf_2_1380x712.jpeg 2x" data-dominant-color="BAB9C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2025-08-05_14-13-04</span><span class="informations">1906×985 228 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>S</p>
<p>Slicer 5.8.1, Windows 11</p>

---

## Post #6 by @muratmaga (2025-08-05 18:23 UTC)

<p>This screenshot from 5.8.1, which doesn’t use the new terminologies feature. Did you create this segmentation in a recent preview and then open it in 5.8.1?</p>

---

## Post #7 by @tsehrhardt (2025-08-05 20:11 UTC)

<p>I started it in an older version and opened it in 5.8.1. I tried another old scene and I’m getting a different hover message.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75a1b10f6a918dcac2a28c4edc4d182abe20a63e.jpeg" data-download-href="/uploads/short-url/gMChMpj8xj9AyrnO684RV6pvSZ8.jpeg?dl=1" title="2025-08-05_16-09-16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75a1b10f6a918dcac2a28c4edc4d182abe20a63e_2_690x366.jpeg" alt="2025-08-05_16-09-16" data-base62-sha1="gMChMpj8xj9AyrnO684RV6pvSZ8" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75a1b10f6a918dcac2a28c4edc4d182abe20a63e_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75a1b10f6a918dcac2a28c4edc4d182abe20a63e_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75a1b10f6a918dcac2a28c4edc4d182abe20a63e_2_1380x732.jpeg 2x" data-dominant-color="ADAFBB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2025-08-05_16-09-16</span><span class="informations">1920×1020 269 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @muratmaga (2025-08-05 20:28 UTC)

<p>This one is correct. It is simply providing more detailed information about the terminology being used.</p>
<p>Having said that, you should really start using your own custom terminology. That way your projects will be consistent (in terms of labels, no typos, colors) and when you extract labelmap (e.g., for machine learning or to export to other software), the conversion will be predictable. You can import a big ontology like Uberon and extract terms from there, or create your custom terminology and color table.</p>
<p>Here is a short tutorial I have written for SlicerMorph.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/Tutorials/blob/main/Segmentation/colors-and-terms/README.md">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/blob/main/Segmentation/colors-and-terms/README.md" target="_blank" rel="noopener">github.com/SlicerMorph/Tutorials</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/Tutorials/blob/main/Segmentation/colors-and-terms/README.md" target="_blank" rel="noopener">Segmentation/colors-and-terms/README.md</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerMorph/Tutorials/blob/main/Segmentation/colors-and-terms/README.md" rel="noopener"><code>main</code></a>
</div>


      <pre><code class="lang-md"># Segment Colors and Terminology

While it is not strictly necessary, we encourage you to determine what structures you will segment and how you will name them and their visual settings **prior** to segmentation. There are couple reasons for them.

While keeping segment names as **Segment_1**, **Segment_2** and so forth is a possibility for small, individual projects, it is better to use proper terms to describe the contents of the segments. The issue with manually typing the segment names is, you can make typos, or use different capitalizations or spellings of the words. You also may not assign the identical colors, so the visual appearance of same structure in different scans might be slightly (or completely) off. Using a standadized terminology and creating a custom color table for your segments can help you deal with this problem.

3D Slicer comes preloaded with two sets of standard terminologies that can be used in segmentation. They are called: **3D Slicer Anatomy List**, and more broad and standardized **DICOM Master List**. Both of these can be found in the `Terminologies` module (CTRL+F, search for terminologies). DICOM Master list contains anatomical structures, tissues and other non-biological things (e.g, feeding tubes) that one can encounter in radiological imaging of human and veterinary patients. However, while terms in those terminologies can probably be sufficient to annotate mammalian anatomy, they are nowhere close to complete for all vertebrate structural diversity. Luckily, terminologies module allows adding new terminologies, which can be obtained from existing ontologies, like [UBERON](https://www.ebi.ac.uk/ols4/ontologies/uberon).

### UBERON 
UBERON is an integrated cross-species anatomy ontology representing a variety of entities classified according to traditional anatomical criteria such as structure, function and developmental lineage. The ontology includes comprehensive relationships to taxon-specific anatomical ontologies, allowing integration of functional, phenotype and expression data. We will refer you to the Uberon website for more information about this ontology. From our perspective UBERON simply serves a dictionary with standardized set of anatomical terms we might need in our segmentation tasks. The benefit is that we can trace the origins of the terms and what they describe. And if they are revised or split we can alter our own color maps accordingly. 

While UBERON distributes its full terminology in JSON format, we need it to be in a specific JSON format to be compatible with Slicer's Terminologies module. Each terms needs to have a color assigned to it and indication of what it represent (e.g., anatomical structure or tissue). Since we cannot assign unique colors to over 17,000 terms UBERON ontology contains, we randomly assigned a small set of colors to each of these terms. The custom color table will allow you to change these colors to whatever you like.

To obtain the full set of UBERON terms (converted mid 2024), [follow this link](https://raw.githubusercontent.com/SlicerMorph/terms-and-colors/refs/heads/main/uberon.full.json) and save the page as `uberon.full.json` somewhere on your computer.

## Importing UBERON to 3D Slicer.
1. Hit CTRL+F, and search for Terminologies.
2. In the Terminologies module click the `+` right of the terminology drop-down selector, and navigate to the `uberon.full.json` file you have downloaded previously. 

&lt;img src="./1.png" width="512"&gt;
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/Tutorials/blob/main/Segmentation/colors-and-terms/README.md" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @tsehrhardt (2025-08-05 20:51 UTC)

<p>I will look into the tutorial. Thank you!</p>

---

## Post #10 by @cpinter (2025-08-06 14:41 UTC)

<aside class="quote no-group" data-username="tsehrhardt" data-post="3" data-topic="43970">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>although the hover message of “invalid terminology information” is annoying but I can live with it</p>
</blockquote>
</aside>
<p>It would not be hard not to show this warning in the tooltip if the user opted for not using terminolgies in the application settings, but it is not something I have time for right now. Feel free to add a new issue on GitHub if you would like us to do it in the next months.</p>

---
