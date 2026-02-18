# Read GE .vol files

**Topic ID**: 44539
**Date**: 2025-09-18
**URL**: https://discourse.slicer.org/t/read-ge-vol-files/44539

---

## Post #1 by @Sharmeen_Khan (2025-09-18 07:25 UTC)

<p>I have ge .vol files which i need to read in python for which i tried third-party software which would be able to convert it into a suitable format like dicom, like 3d slicer, dicomatic etc. but 3d slicer with extension of slicer heart is not working and even able to load .vol file. please help me with this task</p>

---

## Post #2 by @lassoan (2025-09-20 22:20 UTC)

<p>SlicerHeart’s importers can read some of GE’s .vol files. See capabilities and limitations here: <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md#ge" class="inline-onebox">SlicerHeart/Docs/ImageImportExport.md at master · SlicerHeart/SlicerHeart · GitHub</a></p>
<p>If you provide more details then we may be able to give more specific information.</p>

---

## Post #3 by @muratmaga (2025-09-20 22:43 UTC)

<aside class="quote no-group" data-username="Sharmeen_Khan" data-post="1" data-topic="44539">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sharmeen_khan/48/80622_2.png" class="avatar"> Sharmeen_Khan:</div>
<blockquote>
<p>ge .vol files which i</p>
</blockquote>
</aside>
<p>Is this a GE microCT or an ultrasound? If it is a microCT (and you have the .pcr file that gets created after reconstruction), you can give GEVolImport in SlicerMorph a try:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/tree/master/GEVolImport#gevolimport">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/GEVolImport#gevolimport" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/GEVolImport#gevolimport" target="_blank" rel="noopener">SlicerMorph/GEVolImport at master · SlicerMorph/SlicerMorph</a></h3>


  <p><span class="label1">Extension to import microCT data and conduct 3D morphometrics in Slicer - SlicerMorph/SlicerMorph</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
