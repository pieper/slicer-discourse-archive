# Limit computation only to current slices

**Topic ID**: 24335
**Date**: 2022-07-15
**URL**: https://discourse.slicer.org/t/limit-computation-only-to-current-slices/24335

---

## Post #1 by @brandus1 (2022-07-15 23:37 UTC)

<p>Hello,</p>
<p>I have a 200x200x200 vtk array of 20 components (representing 10 complex numbers).</p>
<p>I need to do a fairly heavy matrix multiplication on each set of 20 components. This needs to happen in real time as the user changes some input parameters with a slider, or moves through the 3 standard slices.</p>
<p>I want to limit the computation only to the visible slices, in order to avoid repeating the computation on the whole volume(which takes too much for real time).</p>
<p>I have an old piece of code that implements this in a custom interface by connecting a custom vtk filter to 3 vtkImageReslices.</p>
<p>I have been searching for the appropriate solution to this for the past week, but I keep struggling to find a suitable one. Any idea would be much appreciated.</p>
<p>Thank you very much</p>

---

## Post #2 by @pieper (2022-07-16 04:27 UTC)

<p>In Slicer’s architecture we call this kind of code a “Displayable Manager” (or MRML Displayable Manager, abbreviated MRMLDM in folder names to keep it short).  Probably the transforms is a good place to look for examples.  There’s a MRMLDM instance for each view and the MRMLDM code is responsible for mapping what’s in the scene to that particular view given the various view parameters such as slice and pan/zoom.  These can be in C++ or Python but typically they are in C++.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/Slicer/tree/main/Modules/Loadable/Transforms/MRMLDM">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/Slicer/tree/main/Modules/Loadable/Transforms/MRMLDM" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/Slicer/tree/main/Modules/Loadable/Transforms/MRMLDM" target="_blank" rel="noopener">Slicer/Modules/Loadable/Transforms/MRMLDM at main · Slicer/Slicer</a></h3>

  <p><a href="https://github.com/Slicer/Slicer/tree/main/Modules/Loadable/Transforms/MRMLDM" target="_blank" rel="noopener">main/Modules/Loadable/Transforms/MRMLDM</a></p>

  <p><span class="label1">Multi-platform, free open source software for visualization and image computing.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @brandus1 (2022-08-26 18:51 UTC)

<p>Thank you, I read what I found about MRMLDM and tried at first to parse through the Transforms code, but honestly, it was too difficult for me to reverse engineer how MRMLDM code is applied in practice.</p>
<p>I ended up rethinking this problem in a different way and made it work.</p>
<p>For future works, is there anywhere else where I could look into a simpler applications of MRMLDM?</p>
<p>Thank you very much</p>

---

## Post #4 by @pieper (2022-08-26 19:34 UTC)

<aside class="quote no-group" data-username="brandus1" data-post="3" data-topic="24335">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brandus1/48/13776_2.png" class="avatar"> brandus1:</div>
<blockquote>
<p>For future works, is there anywhere else where I could look into a simpler applications of MRMLDM?</p>
</blockquote>
</aside>
<p>There are 6 MRMLDM directories in the Slicer core code, and many more in extensions.  I’m not sure what is the best to look at.  Maybe someone who’s developed one recently can make a suggestion?</p>

---

## Post #5 by @lassoan (2022-08-26 20:45 UTC)

<p>I agree that displayable managers can be quite complex, so I think your method of updating only the visible parts of a volume for quick preview is a good approach.</p>

---
