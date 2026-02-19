---
topic_id: 18542
title: "Unexpected Behavior Of Color When Using Lut With Color Count"
date: 2021-07-06
url: https://discourse.slicer.org/t/18542
---

# Unexpected behavior of color when using LUT with color count < 255

**Topic ID**: 18542
**Date**: 2021-07-06
**URL**: https://discourse.slicer.org/t/unexpected-behavior-of-color-when-using-lut-with-color-count-255/18542

---

## Post #1 by @squll1 (2021-07-06 19:57 UTC)

<p>Hello:<br>
The issue is first noted when I tried to reproduce a specific LUT in a commercial workstation by creating a custom LUT with 10 colors, and use it in a subtracted CT volume with standardized window and level  ( basically with min 0 HU and max at a certain HU ). Then I noted that the displayed color is not compatible with the window and level settings in Volumes module, most region in the volume shows the color of maximum value. I then toggle color bar in Dataprobe module, and found that while as the data probe in left lower corner shows correct value, the viewport shows the color of 20-25 times of the actual value.<br>
This also applies to builtin color tables with less then 255 colors (e.g. DarkBrightChartColors / 64Color-Nonsemantic) and I then noted that the it shows the color of with [ 255 / color count ]  times the actual value.</p>
<p>CT Volume in “Gery” color table:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e217ee94c8b7908914a0e5b9f4f3cde728a2e1dd.jpeg" alt="image" data-base62-sha1="wg7biMgT8emfxMLteKB1k55vFkF" width="661" height="445"><br>
CT Volume in custom 10-color color table (see below for color txt):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/975c6bf58d29673352a38806559340d024f5d3bf.png" alt="image" data-base62-sha1="lB06Rl2jGzzhCIcJwyQIhQUPU0T" width="662" height="447"><br>
Expected color is shown when adjust color window/level to roughly 25.5X  (255/10)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4ac9b6732c44f2eb7bf9b10e4a87802c2611c487.png" alt="image" data-base62-sha1="aFBv125BEHo7t49oYjtETTyyPEr" width="660" height="444"></p>
<p>This issue is also reproducible with sample dataset.<br>
I’m not sure if I’ve missed something. <img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=12" title=":thinking:" class="emoji" alt=":thinking:" loading="lazy" width="20" height="20"></p>
<p>the custom color table:</p>
<pre><code class="lang-auto"># step 10
0 Navy_blue 0 0 128 255
1 Blue 0 0 255 255
2 Green 0 128 0 255
3 Harlequin 0 255 0 255
4 Maroon 128 0 0 255
5 Red 255 0 0 255
6 Raw_Umber 128 96 0 255
7 Amber 255 192 0 255
8 Gray 128 128 128 255
9 White 255 255 255 255
#EOF
</code></pre>
<p>Platform: Windows 10 20H2, 3D slicer 4.11.20210226, intel i5-9400 + nVidia 1060.</p>

---

## Post #2 by @lassoan (2021-07-09 05:29 UTC)

<p>Thanks for reporting. The current behavior is indeed not intuitive. We already have an issue for improving this, but for now you need to specify 0-255 range in the color table and then map it to the volume by setting the appropriate window/level in the display node. See more information here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5336">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5336" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5336" target="_blank" rel="noopener">RedGreenBlue color node is not usable for volumes</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-12-05" data-time="20:16:11" data-timezone="UTC">08:16PM - 05 Dec 20 UTC</span>
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
    <p class="github-body-container">When choosing a procedural color node as a color node for a scalar volume then t<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">he values are not mapped correctly.

## Steps to reproduce

- Load MRHead
- Choose RedGreenBlue as color node
- Adjust window/level =&gt; ERROR: no matter what you do, red color will not be used
- Create a copy of RedGreenBlue, edit values
- Colors corresponding to X values do not match actual values

It seems that 0-255 range of the color transfer function is mapped to the intensity window specified by volume display node's window width/level.

## Expected behavior

Probably the best behavior would be to use the color transfer function for direct mapping (ignore window/level). This would be expected, especially when the user specifies x-&gt;RGB mapping using a color transfer function.

If that would be too much of a trouble for some reason then at least the behavior should be changed so that the entire scalar range of the colormap would be used by default (e.g., red, green, and blue colors for RedGreenBlue color node).

## Environment
- Slicer version: Slicer-4.11.0-2020-09-30
- Operating system: Windows 10</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @squll1 (2021-07-10 06:38 UTC)

<p>Hello:<br>
Thanks for the quick and precise reply!<br>
The workaround you provided works fine.<br>
(upper panel: original 10 step color LUT, lower panel: 255 step workaround)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/195d2447111be89e9c51a903925b8103140dbe6c.jpeg" data-download-href="/uploads/short-url/3Cnuv4eIQ8p67zgRmFENbfAKgB6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/195d2447111be89e9c51a903925b8103140dbe6c_2_361x500.jpeg" alt="image" data-base62-sha1="3Cnuv4eIQ8p67zgRmFENbfAKgB6" width="361" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/195d2447111be89e9c51a903925b8103140dbe6c_2_361x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/195d2447111be89e9c51a903925b8103140dbe6c_2_541x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/195d2447111be89e9c51a903925b8103140dbe6c.jpeg 2x" data-dominant-color="442D31"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">590×817 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
