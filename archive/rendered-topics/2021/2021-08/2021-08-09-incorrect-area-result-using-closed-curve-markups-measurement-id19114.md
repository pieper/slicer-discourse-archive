# Incorrect area result using closed curve markups measurement

**Topic ID**: 19114
**Date**: 2021-08-09
**URL**: https://discourse.slicer.org/t/incorrect-area-result-using-closed-curve-markups-measurement/19114

---

## Post #1 by @VincentYu (2021-08-09 09:31 UTC)

<h2><a name="p-64383-os-windows10-x64-slicer-version-4130-2021-08-08-image-used-built-in-sample-data-chest-ct-1" class="anchor" href="#p-64383-os-windows10-x64-slicer-version-4130-2021-08-08-image-used-built-in-sample-data-chest-ct-1" aria-label="Heading link"></a>OS: Windows10 x64<br>
Slicer version: 4.13.0-2021-08-08<br>
Image used: built-in sample data (Chest CT)</h2>
<p><a href="https://drive.google.com/drive/folders/1wt1j-VD2_dDSvTBLEhFp5nt51M_EKrKm?usp=sharing" rel="noopener nofollow ugc">video link</a><br>
I found the results of measured area using the closed curve markup with linear curve were inconsistent when I toggled the Enable checkbox in Slicer ver4.11.20210226, see the video “4.11.mp4”.<br>
I tried to reproduce this problem in Slicer 4.13.0-2021-08-08, but I got 0 cm^2 instead, see the video “4.13.0.mp4”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d3859198e1f85b1fbd325a691ea98fd070daeb6.jpeg" data-download-href="/uploads/short-url/1SWVNyO1OrcvQf3pgO1jGnEiMsu.jpeg?dl=1" title="4.13.0.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d3859198e1f85b1fbd325a691ea98fd070daeb6_2_690x437.jpeg" alt="4.13.0.PNG" data-base62-sha1="1SWVNyO1OrcvQf3pgO1jGnEiMsu" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d3859198e1f85b1fbd325a691ea98fd070daeb6_2_690x437.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d3859198e1f85b1fbd325a691ea98fd070daeb6_2_1035x655.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d3859198e1f85b1fbd325a691ea98fd070daeb6.jpeg 2x" data-dominant-color="A1A0A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4.13.0.PNG</span><span class="informations">1369×868 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The results looked fine if I chose spline curve instead of linear curve, and I haven’t tried any other curve type yet.</p>

---

## Post #2 by @lassoan (2021-08-09 16:32 UTC)

<p>Thanks for reporting. I’ve submitted an issue to track this problem:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5780">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5780" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5780" target="_blank" rel="noopener">Markups closed curve area measurement sometimes fails</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-08-09" data-time="16:30:04" data-timezone="UTC">04:30PM - 09 Aug 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Markups closed curve area measurement sometimes returns 0.0 as a result because <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">Delaunay triangulation fails.

See user reports:
- https://discourse.slicer.org/t/incorrect-area-result-using-closed-curve-markups-measurement/19114
- https://discourse.slicer.org/t/why-closed-curve-cannot-generate-baffle-model-in-baffle-planner-module/19076

## Environment
- Slicer version: Slicer-4.13.0-2021-08-02
- Operating system: Windows 10 (probably OS independent)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>As a quick workaround, you can increase the resolution of the curve by typing this into the Python console (replace <code>CC</code> by the actual name of your curve node):</p>
<pre><code class="lang-python">getNode('CC').SetNumberOfPointsPerInterpolatingSegment(30)
</code></pre>

---

## Post #3 by @VincentYu (2021-08-11 02:11 UTC)

<p>Thank you for the workaround, Prof Lasso.</p>

---
