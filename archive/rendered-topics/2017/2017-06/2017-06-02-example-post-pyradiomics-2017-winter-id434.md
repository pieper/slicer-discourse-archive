# Example post: PyRadiomics (2017 Winter)

**Topic ID**: 434
**Date**: 2017-06-02
**URL**: https://discourse.slicer.org/t/example-post-pyradiomics-2017-winter/434

---

## Post #1 by @ihnorton (2017-06-02 19:58 UTC)

<p><em>(Based on <a href="http://wiki.na-mic.org/wiki/2017_Winter_Project_Week/PyRadiomics" class="inline-onebox">2017 Winter Project Week/PyRadiomics - NAMIC Wiki</a>)</em></p>
<div align="center">
<b>Objective</b>: Introduce PyRadiomics to the community</div>
<hr>
<p><strong>Investigators</strong>:</p>
<ul>
<li>Joost van Griethuysen</li>
<li>Hugo Aerts, Steve Pieper (<a class="mention" href="/u/pieper">@pieper</a>)</li>
<li>Jean-Christophe Fillion-Robin (<a class="mention" href="/u/jcfr">@jcfr</a>)</li>
<li>Andrey Fedorov (<a class="mention" href="/u/fedorov">@fedorov</a>)</li>
</ul>
<hr>
<p><strong>Approach</strong>:</p>
<ul>
<li>Present, meet collaborators…</li>
<li>Discuss issues related to integration with Slicer: external packages, numpy version, Slicer module UI</li>
<li>Discuss issues related to enhancing performance using C code</li>
</ul>
<hr>
<p><strong>Screenshots</strong>:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/5133e1b312d4c2f243efe27b7887f183fb6e8fa9.jpg" data-download-href="/uploads/short-url/bAlPwnFG3mybpzBbrAOWlnVXWYx.jpg?dl=1" title="RadiomicsWorkflow.jpg"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5133e1b312d4c2f243efe27b7887f183fb6e8fa9_2_250x122.jpg" width="250" height="122" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5133e1b312d4c2f243efe27b7887f183fb6e8fa9_2_250x122.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5133e1b312d4c2f243efe27b7887f183fb6e8fa9_2_375x183.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5133e1b312d4c2f243efe27b7887f183fb6e8fa9_2_500x244.jpg 2x" data-dominant-color="E4E4E4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">RadiomicsWorkflow.jpg</span><span class="informations">1550×760 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The radiomics concept of going from segmented images to heatmaps of features that can be correlated with other data such as genomics, demographics, or outcomes.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/30cfea399c66d1fc1bfea5a7bfa878f0c73ca7df.jpg" data-download-href="/uploads/short-url/6XOncLEKSCWWoisskr2CYC3NTBB.jpg?dl=1" title="PyRadiomics_structure.jpg"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/30cfea399c66d1fc1bfea5a7bfa878f0c73ca7df_2_250x105.jpg" width="250" height="105" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/30cfea399c66d1fc1bfea5a7bfa878f0c73ca7df_2_250x105.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/30cfea399c66d1fc1bfea5a7bfa878f0c73ca7df_2_375x157.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/30cfea399c66d1fc1bfea5a7bfa878f0c73ca7df_2_500x210.jpg 2x" data-dominant-color="F1F2F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PyRadiomics_structure.jpg</span><span class="informations">1770×746 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
PyRadiomics allows processing of image data and an extensible set of image feature calculators.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/8d3c540481799f4bf120ecdb12af81af31ce9816.png" data-download-href="/uploads/short-url/k9qzHJgunbZ2WEQS6CeVDFUcqii.png?dl=1" title="SlicerRadiomics.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/8d3c540481799f4bf120ecdb12af81af31ce9816_2_250x142.png" width="250" height="142" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/8d3c540481799f4bf120ecdb12af81af31ce9816_2_250x142.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/8d3c540481799f4bf120ecdb12af81af31ce9816_2_375x213.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/8d3c540481799f4bf120ecdb12af81af31ce9816_2_500x284.png 2x" data-dominant-color="B5B4B7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerRadiomics.png</span><span class="informations">2880×1636 407 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
The SlicerRadiomics extension makes it easy to test and apply PyRadiomics to medical imaging data.</p>
<hr>
<p><strong>Progress</strong>:</p>
<ul>
<li>Introduced PyRadiomics to the community</li>
<li>There are still some issues with the packaging of the extension, SlicerRadiomics. Numpy issue is resolved, PyRadiomics works with numpy 1.9.2, adjusted minimum requirements. Once these issues are resolved, it will be made publicly available in the Github Radiomics Organisation.</li>
<li>C code performance enhancement is written, but is still causing some issues during compilation. Switch setup to use skbuild and cmake. Latest (offline) tests work with <code>setup.py</code> develop and setup.py test.</li>
<li>Issues related to building SlicerRadiomics have been fixed, extension can now be built and used in the built version in the basic form</li>
<li>Issues related to packaging SlicerRadiomics have been identified (limitations of Slicer infrastructure packaging external python packages); JC identified the solution approach, and the issue will be resolved soon, we expect the extension to be available publicly within a month</li>
</ul>
<hr>
<p><strong>References</strong>:</p>
<p><a href="https://github.com/Radiomics/pyradiomics">GitHub Repository</a><br>
<a href="http://pyradiomics.readthedocs.io/">Documentation</a></p>
<p><strong>Project page</strong>:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/AIM-Harvard/SlicerRadiomics">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/AIM-Harvard/SlicerRadiomics" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/6e4a9be0dfdb949c7acd55ff6e2255af584c820022e8f71c1c5b86547d9f7e0f/AIM-Harvard/SlicerRadiomics" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/AIM-Harvard/SlicerRadiomics" target="_blank" rel="noopener">GitHub - AIM-Harvard/SlicerRadiomics: A Slicer extension to provide a GUI...</a></h3>

  <p>A Slicer extension to provide a GUI around pyradiomics - GitHub - AIM-Harvard/SlicerRadiomics: A Slicer extension to provide a GUI around pyradiomics</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @jcfr (2017-06-02 20:46 UTC)

<p>Not sure what is best to list screenshot. Here is an approach:</p>
<p>What do you think <a class="mention" href="/u/ihnorton">@ihnorton</a> ? We could also enable table html tag …</p>
<h3><a name="p-1453-option-1-1" class="anchor" href="#p-1453-option-1-1" aria-label="Heading link"></a>Option 1</h3>
<details>
<summary>
Screenshots</summary>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5133e1b312d4c2f243efe27b7887f183fb6e8fa9.jpeg" data-download-href="/uploads/short-url/bAlPwnFG3mybpzBbrAOWlnVXWYx.jpg?dl=1" title=""><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5133e1b312d4c2f243efe27b7887f183fb6e8fa9_2_690x338.jpg" alt="" data-base62-sha1="bAlPwnFG3mybpzBbrAOWlnVXWYx" role="presentation" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5133e1b312d4c2f243efe27b7887f183fb6e8fa9_2_690x338.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5133e1b312d4c2f243efe27b7887f183fb6e8fa9_2_1035x507.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5133e1b312d4c2f243efe27b7887f183fb6e8fa9_2_1380x676.jpg 2x" data-dominant-color="E4E4E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">1550×760 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30cfea399c66d1fc1bfea5a7bfa878f0c73ca7df.jpeg" data-download-href="/uploads/short-url/6XOncLEKSCWWoisskr2CYC3NTBB.jpg?dl=1" title=""><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/30cfea399c66d1fc1bfea5a7bfa878f0c73ca7df_2_690x290.jpg" alt="" data-base62-sha1="6XOncLEKSCWWoisskr2CYC3NTBB" role="presentation" width="690" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/30cfea399c66d1fc1bfea5a7bfa878f0c73ca7df_2_690x290.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/30cfea399c66d1fc1bfea5a7bfa878f0c73ca7df_2_1035x435.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/30cfea399c66d1fc1bfea5a7bfa878f0c73ca7df_2_1380x580.jpg 2x" data-dominant-color="F1F2F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">1770×746 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d3c540481799f4bf120ecdb12af81af31ce9816.png" data-download-href="/uploads/short-url/k9qzHJgunbZ2WEQS6CeVDFUcqii.png?dl=1" title=""><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/8d3c540481799f4bf120ecdb12af81af31ce9816_2_690x391.png" alt="" data-base62-sha1="k9qzHJgunbZ2WEQS6CeVDFUcqii" role="presentation" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/8d3c540481799f4bf120ecdb12af81af31ce9816_2_690x391.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/8d3c540481799f4bf120ecdb12af81af31ce9816_2_1035x586.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/8d3c540481799f4bf120ecdb12af81af31ce9816_2_1380x782.png 2x" data-dominant-color="B5B4B7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">2880×1636 407 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</details>
<h3><a name="p-1453-option-2-2" class="anchor" href="#p-1453-option-2-2" aria-label="Heading link"></a>Option 2</h3>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/5133e1b312d4c2f243efe27b7887f183fb6e8fa9.jpg" data-download-href="/uploads/short-url/bAlPwnFG3mybpzBbrAOWlnVXWYx.jpg?dl=1" title="RadiomicsWorkflow.jpg"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5133e1b312d4c2f243efe27b7887f183fb6e8fa9_2_250x100.jpg" width="250" height="100" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5133e1b312d4c2f243efe27b7887f183fb6e8fa9_2_250x100.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5133e1b312d4c2f243efe27b7887f183fb6e8fa9_2_375x150.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/5133e1b312d4c2f243efe27b7887f183fb6e8fa9_2_500x200.jpg 2x" data-dominant-color="E4E4E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">RadiomicsWorkflow.jpg</span><span class="informations">1550×760 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/30cfea399c66d1fc1bfea5a7bfa878f0c73ca7df.jpg" data-download-href="/uploads/short-url/6XOncLEKSCWWoisskr2CYC3NTBB.jpg?dl=1" title="PyRadiomics_structure.jpg"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/30cfea399c66d1fc1bfea5a7bfa878f0c73ca7df_2_250x100.jpg" width="250" height="100" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/30cfea399c66d1fc1bfea5a7bfa878f0c73ca7df_2_250x100.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/30cfea399c66d1fc1bfea5a7bfa878f0c73ca7df_2_375x150.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/30cfea399c66d1fc1bfea5a7bfa878f0c73ca7df_2_500x200.jpg 2x" data-dominant-color="F1F2F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PyRadiomics_structure.jpg</span><span class="informations">1770×746 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/8d3c540481799f4bf120ecdb12af81af31ce9816.png" data-download-href="/uploads/short-url/k9qzHJgunbZ2WEQS6CeVDFUcqii.png?dl=1" title="SlicerRadiomics.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/8d3c540481799f4bf120ecdb12af81af31ce9816_2_250x100.png" width="250" height="100" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/8d3c540481799f4bf120ecdb12af81af31ce9816_2_250x100.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/8d3c540481799f4bf120ecdb12af81af31ce9816_2_375x150.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/8d3c540481799f4bf120ecdb12af81af31ce9816_2_500x200.png 2x" data-dominant-color="B5B4B7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerRadiomics.png</span><span class="informations">2880×1636 407 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>While visible right away … there are two smalls and its hard to get the correct ratio</p>
<h3><a name="p-1453-option-3-3" class="anchor" href="#p-1453-option-3-3" aria-label="Heading link"></a>Option 3</h3>
<p>Look like this plugin would be useful <a href="https://discourse.pro/t/topic/34" class="inline-onebox">«Gallery» plugin (version 3.1, 2016-12-11) - Discourse Plugins</a></p>

---

## Post #3 by @pieper (2017-06-02 21:05 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="434">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Option 3</p>
<p>Look like this plugin would be useful <a href="https://discourse.pro/t/topic/34" class="inline-onebox">«Gallery» plugin (version 3.1, 2016-12-11) - Discourse Plugins</a></p>
</blockquote>
</aside>
<p>Looks nice but it didn’t seem to work for me.</p>

---

## Post #4 by @ihnorton (2017-06-02 21:09 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> yeah, not sure what to do here. Detail expand works OK, but not ideal. I have no objection to allowing </p><p></p><aside class="quote no-group" data-username="jcfr" data-post="2" data-topic="434">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Look like this plugin would be useful</p>
</blockquote>
</aside><p>We can’t install plugins in the hosted instance.</p><table>

</table>

---

## Post #5 by @jcfr (2017-06-02 21:27 UTC)

<p>Option 2 works great in fact. After few seconds after editing the page, it is possible to show the large size version and also use the right left arrow to see the images.</p>
<ul>
<li>preview “widget”</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/86ad7b2e7ece9c2d0ed972e16ff802ae4d39a82d.png" data-download-href="/uploads/short-url/jdpF5BXlOw32f7jJRcpO8FrE9Mp.png?dl=1" title="1-preview.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/86ad7b2e7ece9c2d0ed972e16ff802ae4d39a82d_2_690x437.png" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/86ad7b2e7ece9c2d0ed972e16ff802ae4d39a82d_2_690x437.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/86ad7b2e7ece9c2d0ed972e16ff802ae4d39a82d_2_1035x655.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/86ad7b2e7ece9c2d0ed972e16ff802ae4d39a82d_2_1380x874.png 2x" data-dominant-color="F4F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1-preview.png</span><span class="informations">1855×1176 261 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ul>
<li>previous / next</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/e0bebedf507b80a614a4ac5f5d9fc9645b88db61.jpg" data-download-href="/uploads/short-url/w4bCGoJsbC23Oe8NKZeHPDnpjxf.jpg?dl=1" title="2-image-large.jpg"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e0bebedf507b80a614a4ac5f5d9fc9645b88db61_2_690x431.jpg" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e0bebedf507b80a614a4ac5f5d9fc9645b88db61_2_690x431.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e0bebedf507b80a614a4ac5f5d9fc9645b88db61_2_1035x646.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e0bebedf507b80a614a4ac5f5d9fc9645b88db61_2_1380x862.jpg 2x" data-dominant-color="B6B7B9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2-image-large.jpg</span><span class="informations">1920×1200 340 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @jcfr (2017-06-07 15:36 UTC)



---
