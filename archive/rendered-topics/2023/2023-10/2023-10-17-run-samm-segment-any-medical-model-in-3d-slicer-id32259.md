# Run SAMM (Segment Any Medical Model) in 3D Slicer

**Topic ID**: 32259
**Date**: 2023-10-17
**URL**: https://discourse.slicer.org/t/run-samm-segment-any-medical-model-in-3d-slicer/32259

---

## Post #1 by @Vineet_Saravanan (2023-10-17 00:52 UTC)

<p>Hello I am trying to use the SAMM module in 3-D slicer. I was unable to import it using the extensions manager and I saw that I can use this command to use any outside extension:<code> Slicer.exe --additional-module-paths D:\Downloads\samm-main\samm-main\samm</code></p>
<p>When I run that command on cmd I get this:</p>
<pre><code class="lang-auto">'Slicer.exe' is not recognized as an internal or external command,
operable program or batch file.
</code></pre>
<p>What should I do? Is there a different method I should import modules?</p>

---

## Post #2 by @lassoan (2023-10-17 01:12 UTC)

<p>You need to go the folder where <code>Slicer.exe</code> is. For example, using this command:</p>
<pre><code>cd %LOCALAPPDATA%\slicer.org\Slicer 5.4.0
</code></pre>

---

## Post #3 by @Vineet_Saravanan (2023-10-18 00:16 UTC)

<p>Thank you that worked! But now I have a new problem:</p>
<p>After running this command:</p>
<pre><code class="lang-auto">
Slicer.exe --additional-module-paths D:\Downloads\samm-main\samm-main\samm
</code></pre>
<p>Slicer opens, but the module doesn’t show up in 3-d slicer:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/341b0e4507d5070ba25ac50b867790d3f6c2e929.png" data-download-href="/uploads/short-url/7qWNirwZOMOUDqCXlvqHVtaME1b.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/341b0e4507d5070ba25ac50b867790d3f6c2e929_2_690x473.png" alt="image" data-base62-sha1="7qWNirwZOMOUDqCXlvqHVtaME1b" width="690" height="473" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/341b0e4507d5070ba25ac50b867790d3f6c2e929_2_690x473.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/341b0e4507d5070ba25ac50b867790d3f6c2e929.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/341b0e4507d5070ba25ac50b867790d3f6c2e929.png 2x" data-dominant-color="DADADB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">737×506 8.37 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The SAMM folder looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ad3308800761bf3ec7ad13d99a43cc1577c4ab0.png" data-download-href="/uploads/short-url/66Qwzow0fPBSjMndfIi9MrRWK9G.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ad3308800761bf3ec7ad13d99a43cc1577c4ab0.png" alt="image" data-base62-sha1="66Qwzow0fPBSjMndfIi9MrRWK9G" width="690" height="150" data-dominant-color="F1F5F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">692×151 6.46 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Vineet_Saravanan (2023-10-21 01:05 UTC)

<p>Does anyone know what’s wrong? There were no errors in the console.</p>

---

## Post #5 by @muratmaga (2023-10-21 01:11 UTC)

<p>Try the paths with / instead of \</p>

---

## Post #6 by @Vineet_Saravanan (2023-10-21 01:16 UTC)

<p>I used <code>Slicer.exe --additional-module-paths D:/Downloads/samm-main/samm-main</code>. But this still didn’t work.</p>

---

## Post #7 by @Vineet_Saravanan (2023-10-21 01:22 UTC)

<p>What does this mean? :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/9301c05e877da960e03dfe57ad74514e5f3d8a8e.png" alt="image" data-base62-sha1="kYtWjGhv6bhnYrwGogYgR5ECM7I" width="415" height="440"></p>

---

## Post #9 by @muratmaga (2023-10-21 02:31 UTC)

<p>I think you are missing the final /samm folder in your path.<br>
like this:</p>
<aside class="quote no-group" data-username="Vineet_Saravanan" data-post="3" data-topic="32259">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vineet_saravanan/48/67136_2.png" class="avatar"> Vineet_Saravanan:</div>
<blockquote>
<p><code>Slicer.exe --additional-module-paths D:\Downloads\samm-main\samm-main\samm</code></p>
</blockquote>
</aside>
<p>Also instructions says you need to use extension wizard, did you try that? That might generate an error for you to understand why it is failing.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/bingogome/samm#install-the-samm-extension-to-3d-slicer">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/bingogome/samm#install-the-samm-extension-to-3d-slicer" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/5dc59ae2f96cf3f5056f1c0b14375f3176601bd41bcf11c2b4a8ba031f65ad33/bingogome/samm" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/bingogome/samm#install-the-samm-extension-to-3d-slicer" target="_blank" rel="noopener">GitHub - bingogome/samm: A 3D Slicer integration to Meta's SAM.</a></h3>

  <p>A 3D Slicer integration to Meta's SAM. Contribute to bingogome/samm development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @Vineet_Saravanan (2023-10-21 23:16 UTC)

<p>Thank You that worked!</p>

---

## Post #11 by @Vineet_Saravanan (2023-10-22 00:16 UTC)

<p>I made some data of a segmented brain. What’s the best way to use this data and train using SAMM?</p>

---

## Post #12 by @muratmaga (2023-10-23 02:55 UTC)

<p>Not sure if anyone here has any experience using SAMM to train a segmentation model. If you have already created some labeled data, you can give MonaiLabel a try though…</p>
<p><a href="https://docs.monai.io/projects/label/en/latest/quickstart.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://docs.monai.io/projects/label/en/latest/quickstart.html</a></p>

---

## Post #13 by @Vineet_Saravanan (2023-10-23 23:05 UTC)

<p>I am trying to compare MONAILABEL and SAMM.</p>

---

## Post #14 by @muratmaga (2023-10-24 00:07 UTC)

<p>I might be wrong, but I believe SAMM Slicer extension only allows you to use the SAM tool for segmentation. I am not sure if it actually offers any retraining functionality.</p>
<p>You might have better luck contacting the extension developers, I am not sure if they are tracking this forum.</p>

---

## Post #15 by @Vineet_Saravanan (2023-10-24 17:38 UTC)

<p>Ok, thank you. I will ask in the github.</p>

---
