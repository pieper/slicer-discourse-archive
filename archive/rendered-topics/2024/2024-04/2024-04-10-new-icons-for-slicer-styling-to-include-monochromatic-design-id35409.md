# New icons for Slicer: styling to include monochromatic designs and optional accent colors

**Topic ID**: 35409
**Date**: 2024-04-10
**URL**: https://discourse.slicer.org/t/new-icons-for-slicer-styling-to-include-monochromatic-designs-and-optional-accent-colors/35409

---

## Post #1 by @wenples (2024-04-10 13:22 UTC)

<p>Hello all,<br>
I wanted to confirm next steps for me and also confirm some followup on QSS/other-styling questions.</p>
<p>next steps:</p>
<ol>
<li>
<p>Change Slicer BG color in Dark Theme to be <span class="hashtag-raw">#000000</span> and make sure this works with existing icons. Not a big change, but I’ll verify all new icons are good to go.</p>
</li>
<li>
<p>Curate a refactored version of icons that are each FLAT SVG that works for the default theme. (I assume if we are dropping in a few icons to test that Light theme is the default – please let me know if you’d prefer Dark instead.)</p>
</li>
</ol>
<ul>
<li>For testing, we’ll start with the Load/Save and Application Basics icons, which are simplest and can be used for testing. I’ll let the group know when these refactored icons are checked in and where to find them. Should have them in place early next week.</li>
</ul>
<p>followup:</p>
<p>Regarding the new icons with accent color(s), I have some questions about QSS for icon.svg files. I understood that Sam was looking into this and would guide me about how that translates into icon design requirements. In particular I wonder whether existing icons can be <em>optionally</em> instrumented with selectors that Qt can use to handle accent colors --or whether there is another acceptable strategy. And in the absence of that ability… all monochromatic, like material symbols icons?..</p>
<p>Ideally, we can keep the creation of icons super simple, as Andras emphasized at the end of this week’s developer mtg – but still add the value of accent colors for designers willing to take the extra steps, and in a way that is trusted to work efficiently and reliably. Have our cake and eat it too!</p>
<p>So I’ll stay tuned for more info before touching the existing icons with color, or making new icons for slice controller widgets etc.</p>
<p>Cheers! Also, I will post the latest versions of light and dark theme mockups. Cheers!</p>

---

## Post #2 by @wenples (2024-04-10 13:23 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3deef78f57d2acf0b1c8e113b63d0a2af75a725b.jpeg" data-download-href="/uploads/short-url/8PT6PBKSG9MMFiYTqjDdNoZcIHh.jpeg?dl=1" title="DarkSlicerToolbarMock-04-04-24"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3deef78f57d2acf0b1c8e113b63d0a2af75a725b_2_690x428.jpeg" alt="DarkSlicerToolbarMock-04-04-24" data-base62-sha1="8PT6PBKSG9MMFiYTqjDdNoZcIHh" width="690" height="428" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3deef78f57d2acf0b1c8e113b63d0a2af75a725b_2_690x428.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3deef78f57d2acf0b1c8e113b63d0a2af75a725b_2_1035x642.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3deef78f57d2acf0b1c8e113b63d0a2af75a725b_2_1380x856.jpeg 2x" data-dominant-color="4B4849"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">DarkSlicerToolbarMock-04-04-24</span><span class="informations">1800×1118 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c3d026de2d206312292829bd80ce12a351a74b7.jpeg" data-download-href="/uploads/short-url/aSqZZVHqIEL4P8MKhwWfUxj1t31.jpeg?dl=1" title="LightSlicerToolbarMock-04-04-24"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3d026de2d206312292829bd80ce12a351a74b7_2_690x439.jpeg" alt="LightSlicerToolbarMock-04-04-24" data-base62-sha1="aSqZZVHqIEL4P8MKhwWfUxj1t31" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3d026de2d206312292829bd80ce12a351a74b7_2_690x439.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3d026de2d206312292829bd80ce12a351a74b7_2_1035x658.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/c/4c3d026de2d206312292829bd80ce12a351a74b7_2_1380x878.jpeg 2x" data-dominant-color="ECE9EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">LightSlicerToolbarMock-04-04-24</span><span class="informations">1801×1148 261 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @jamesobutler (2024-04-10 15:45 UTC)

<aside class="quote no-group" data-username="wenples" data-post="1" data-topic="35409">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/wenples/48/6801_2.png" class="avatar"> wenples:</div>
<blockquote>
<p>Change Slicer BG color in Dark Theme to be <span class="hashtag-raw">#000000</span></p>
</blockquote>
</aside>
<p>I’m not sure if pure black is the best option. Material Design appears to suggest <span class="hashtag-raw">#121212</span> for dark themes for accessibility reasons:</p>
<blockquote>
<p>A dark theme uses dark grey, rather than black, as the primary surface color for components. Dark grey surfaces can express a wider range of color, elevation, and depth, because it’s easier to see shadows on grey (instead of black).</p>
<p>Dark grey surfaces also reduce eye strain, as light text on a dark grey surface has less contrast than light text on a black surface.</p>
</blockquote>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://m2.material.io/design/color/dark-theme.html#properties">
  <header class="source">
      <img src="https://m2.material.io/static/assets/favicon.ico" class="site-icon" width="32" height="32">

      <a href="https://m2.material.io/design/color/dark-theme.html#properties" target="_blank" rel="noopener nofollow ugc">Material Design</a>
  </header>

  <article class="onebox-body">
    <img width="500" height="500" src="https://material.io/static/assets/result.png" class="thumbnail onebox-avatar">

<h3><a href="https://m2.material.io/design/color/dark-theme.html#properties" target="_blank" rel="noopener nofollow ugc">Material Design</a></h3>

  <p>Build beautiful, usable products faster. Material Design is an adaptable system—backed by open-source code—that helps teams build high quality digital experiences.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @wenples (2024-04-10 16:37 UTC)

<p>I’m happy to go with that instead – <span class="hashtag-raw">#000000</span> was suggested in the meeting for better contrast than <span class="hashtag-raw">#323232</span> gives, which is shown in the current mockup. Betting <span class="hashtag-raw">#121212</span> would accomplish that just fine! Thanks, James.</p>

---

## Post #5 by @pieper (2024-04-10 17:37 UTC)

<p>Yes, sorry if it sounded like I was suggesting pure black, I meant just something darker than what we had.  Something like <span class="hashtag-raw">#121212</span> sounds like a good option.</p>

---

## Post #6 by @wenples (2024-04-15 21:40 UTC)

<p>Hi all,<br>
Keeping you posted: flat (no layered elements) icon versions of light themed icons are checked into github, accessible here:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/Slicer/slicer-media-assets/tree/main/SlicerIcons/SlicerSVG/QStyled">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Slicer/slicer-media-assets/tree/main/SlicerIcons/SlicerSVG/QStyled" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Slicer/slicer-media-assets/tree/main/SlicerIcons/SlicerSVG/QStyled" target="_blank" rel="noopener">slicer-media-assets/SlicerIcons/SlicerSVG/QStyled at main ·...</a></h3>


  <p><span class="label1">Contribute to Slicer/slicer-media-assets development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Only versions of DataIO (load, save, dicom) and ApplicationBasics icons so far. These are for testing with various approaches to styling for different themes and interaction states. I’ve also updated the palettes to include DarkSlicer background color as <span class="hashtag-raw">#121212</span>.</p>
<p>I looked a bit at Qt Stylesheets and QtStyle, and wasn’t able to see how these can be used on the svgs themselves – so I’m deferring to Sam on this for sure! In the meantime, I’m playing with logic to modify an lxml etree parsed version of an svg – we’ll see if that can be a sufficiently robust and performant option…</p>
<p>Meanwhile, I will work on flattening other layered versions of icons.</p>
<p>Cheers!<br>
wen</p>

---
