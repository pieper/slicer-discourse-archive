# A question about interaction mode of scatterplot

**Topic ID**: 19420
**Date**: 2021-08-30
**URL**: https://discourse.slicer.org/t/a-question-about-interaction-mode-of-scatterplot/19420

---

## Post #1 by @chz31 (2021-08-30 23:47 UTC)

<p>Hi all,</p>
<p>I am thinking about including a module for offering better interaction about visualizing shape.deformation in a Principal Component (PC) scatterplot. Currently, the SlicerMorph module has functions to visualize shape deformation along each individual PC.</p>
<p>What I am thinking about is that I could draw a line in a PC scatterplot (as the picture below shows). Shape difference along this direction can then be visualized as mean shape deformation. I believe it is doable as long as I combine the visualization of individual PC</p>
<p>In order to do this, I may need to be able to draw a line in a scatterplot and get the coordinates of the two end points as well as the slope of this line. In this way, I can show the shape deformation by combining the deformation along two individual PCs.</p>
<p>Does Slicer include such functions that allow me to interact with the scatterplot?</p>
<p>Thank you very much!</p>
<p>Best,<br>
Chi</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abc5c8a128db96ad98309e0aa4f6e95383ce9d5c.jpeg" data-download-href="/uploads/short-url/ovzoCptMzEa2zerByQrNz3yAOba.jpeg?dl=1" title="InkedPC1_PC2_plot_LI" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abc5c8a128db96ad98309e0aa4f6e95383ce9d5c.jpeg" alt="InkedPC1_PC2_plot_LI" data-base62-sha1="ovzoCptMzEa2zerByQrNz3yAOba" width="690" height="429" data-dominant-color="F7F9F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">InkedPC1_PC2_plot_LI</span><span class="informations">950×592 27.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-08-31 02:43 UTC)

<p>The easiest way to draw a line is to add a scatter plot series with two points and set <em>Interation mode</em> → <em>move points</em>.</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1b65dddce4d9287efe57e4d8db5d03b001b69e3.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1b65dddce4d9287efe57e4d8db5d03b001b69e3.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1b65dddce4d9287efe57e4d8db5d03b001b69e3.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #3 by @chz31 (2021-08-31 18:24 UTC)

<p>Thank you! This is very helpful!</p>

---
