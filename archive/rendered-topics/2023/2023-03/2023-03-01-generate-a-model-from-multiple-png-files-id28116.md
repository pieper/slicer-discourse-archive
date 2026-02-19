---
topic_id: 28116
title: "Generate A Model From Multiple Png Files"
date: 2023-03-01
url: https://discourse.slicer.org/t/28116
---

# Generate a model from multiple PNG files

**Topic ID**: 28116
**Date**: 2023-03-01
**URL**: https://discourse.slicer.org/t/generate-a-model-from-multiple-png-files/28116

---

## Post #1 by @ConstanzaMor (2023-03-01 15:13 UTC)

<p>Hello,</p>
<p>I’m new to 3D Slicer and I’m working with series of 2D images in PNG or JPEG files. I am trying to arrange them in 3D space since I want to virtually observe the IVD in 360º. So far, I have been able to place the images where I want, but not able to observe them all at the same time.</p>
<p>I wanted to know if there’s an easy way to insert the volume with an specific separation between each image, and if there’s a way to add the transformed images to a new volume with the given positions.</p>
<p>Thank you so much in advance.</p>

---

## Post #2 by @pieper (2023-03-01 18:54 UTC)

<p>You can try this module:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks" target="_blank" rel="noopener">SlicerMorph/Docs/ImageStacks at master · SlicerMorph/SlicerMorph</a></h3>

  <p><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks" target="_blank" rel="noopener">master/Docs/ImageStacks</a></p>

  <p><span class="label1">Extensions to conduct 3D morphometrics in Slicer. Contribute to SlicerMorph/SlicerMorph development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @ConstanzaMor (2023-03-02 12:35 UTC)

<p>Thank you and just an additional question, is there a module that allows me to arrange my PNG images with an arbitrary transform. Lets say, one degree of rotation in the x,y plane?</p>

---

## Post #4 by @pieper (2023-03-02 13:31 UTC)

<p>Yes, look into the Transforms module.</p>

---
