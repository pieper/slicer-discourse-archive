# Can I reconstruct implant for defect zone for a human patient?

**Topic ID**: 32325
**Date**: 2023-10-19
**URL**: https://discourse.slicer.org/t/can-i-reconstruct-implant-for-defect-zone-for-a-human-patient/32325

---

## Post #1 by @Fatih_Hamircu (2023-10-19 12:37 UTC)

<p>Hello,</p>
<p>Because my research and learning are continuing…</p>
<p>The point I’m curious about is related to your software; let me try to<br>
explain it step by step.</p>
<ol>
<li>The person’s CBCT scan is being taken.</li>
<li>Region of interest is modeled via CBCT scan.</li>
<li>The defect area is being reconstructed.</li>
<li>The reconstructed region is extracted in stl format.</li>
<li>The stl model is being given to the printer program to be sliced.</li>
</ol>
<p>Does your program in stage-3 do what I want to say? I put a picture on Attachment, I like it if you look at it.</p>
<p>Thank you very much in advance</p>
<p>Best regards</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3a1cb2fd0845a90ea9b1c65970d1f6accb4a92c.jpeg" alt="Ekran görüntüsü 2023-10-17 182800" data-base62-sha1="nlyt59EY9buD8FKSW5OAhJhzq4Q" width="400" height="427"></p>

---

## Post #2 by @mau_igna_06 (2023-10-19 15:10 UTC)

<p>Please check if this extension can achieve your goals:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner#bonereconstructionplanner">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner#bonereconstructionplanner" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:649/499;"><img src="https://repository-images.githubusercontent.com/316575529/81a13a10-3663-47f0-9fea-152b8ca4d35e" class="thumbnail" width="649" height="499"></div>

<h3><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner#bonereconstructionplanner" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerIGT/SlicerBoneReconstructionPlanner: 3D Slicer module for...</a></h3>

  <p>3D Slicer module for planning mandible reconstruction surgery using fibula flap - GitHub - SlicerIGT/SlicerBoneReconstructionPlanner: 3D Slicer module for planning mandible reconstruction surgery u...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If not please comment about what’s missing <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #3 by @Fatih_Hamircu (2023-10-19 15:19 UTC)

<p>Can I use the software on human patients? Or is it just for software research purposes?</p>

---

## Post #4 by @mau_igna_06 (2023-10-19 15:43 UTC)

<p>This should address your questions:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/main/LICENSE">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/main/LICENSE" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/main/LICENSE" target="_blank" rel="noopener nofollow ugc">SlicerIGT/SlicerBoneReconstructionPlanner/blob/main/LICENSE</a></h4>


      <pre><code class="lang-">BSD 3-Clause License

Copyright (c) 2020, Andras Lasso, Mauro I. Dominguez
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/main/LICENSE" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @pieper (2023-10-19 15:58 UTC)

<p>And for Slicer itself, please be aware of this information about the license:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#license" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/about.html#license</a></p>

---
