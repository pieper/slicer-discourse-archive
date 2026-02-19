---
topic_id: 24564
title: "Link Views In Three Over Three Configuration"
date: 2022-07-29
url: https://discourse.slicer.org/t/24564
---

# Link views in three over three configuration

**Topic ID**: 24564
**Date**: 2022-07-29
**URL**: https://discourse.slicer.org/t/link-views-in-three-over-three-configuration/24564

---

## Post #1 by @JoeNajm (2022-07-29 13:07 UTC)

<p>Hello,<br>
I am working on an extension using MRI images, in which I need to display the flair and phase of the same patient next to each other (the flair are the bottom row images and the phase are the top row images in the pictures provided below). To do so I decided to load the flair as the foreground image and phase as the background and just change the opacity to go from one to another.<br>
I would like to simultaneously scroll through both views of the same slice (flair and phase). I noticed that the tool to link views (the small chain on the toolbar) works when I use the “three by three slice” configuration (The views are named Red, Yellow, Green, Slice 4,5,6,7,8,9) :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5eb51eebf5434358da3248f1e52b3be53b326b74.jpeg" data-download-href="/uploads/short-url/dvOVLx82UWxkvWQuLYf1XC6Zlpq.jpeg?dl=1" title="Screenshot from 2022-07-29 14-47-49" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5eb51eebf5434358da3248f1e52b3be53b326b74_2_690x410.jpeg" alt="Screenshot from 2022-07-29 14-47-49" data-base62-sha1="dvOVLx82UWxkvWQuLYf1XC6Zlpq" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5eb51eebf5434358da3248f1e52b3be53b326b74_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5eb51eebf5434358da3248f1e52b3be53b326b74_2_1035x615.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5eb51eebf5434358da3248f1e52b3be53b326b74_2_1380x820.jpeg 2x" data-dominant-color="2A2A29"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-07-29 14-47-49</span><span class="informations">1412×840 91.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, it does not work when I use the “three over three” configuration (The views are now named Red, Yellow, Green and Red+, Yellow+, Green+):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44e2eed955977364da1bf742ff6c25f907d5e933.jpeg" data-download-href="/uploads/short-url/9PoFwmlwqR3rX6H6Anl6lSALh6P.jpeg?dl=1" title="Screenshot from 2022-07-29 14-42-10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44e2eed955977364da1bf742ff6c25f907d5e933_2_690x453.jpeg" alt="Screenshot from 2022-07-29 14-42-10" data-base62-sha1="9PoFwmlwqR3rX6H6Anl6lSALh6P" width="690" height="453" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44e2eed955977364da1bf742ff6c25f907d5e933_2_690x453.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44e2eed955977364da1bf742ff6c25f907d5e933_2_1035x679.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44e2eed955977364da1bf742ff6c25f907d5e933_2_1380x906.jpeg 2x" data-dominant-color="4E4D4C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-07-29 14-42-10</span><span class="informations">1408×925 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As I only need 6 views and not 9, is there a way to link the views in the “three over three” configuration ?</p>
<p>Thanks in advance,<br>
Joe</p>

---

## Post #2 by @lassoan (2022-07-29 13:19 UTC)

<p>Views that are in the same <code>View group</code> are synchronized. See more information in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">user manual</a>.</p>
<p><code>R</code>, <code>G</code>, <code>Y</code> views are in view group <code>0</code>. You can synchronize <code>R+</code>, <code>G+</code>, <code>Y+</code> views with them by changing the view group to <code>0</code> in <code>View Controllers</code> module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9da8212437bb0b10c9d4a7859f05d3dac5096faf.png" data-download-href="/uploads/short-url/muHb4p0y9bbfCpFchfzqfOSjpJt.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9da8212437bb0b10c9d4a7859f05d3dac5096faf_2_417x500.png" alt="image" data-base62-sha1="muHb4p0y9bbfCpFchfzqfOSjpJt" width="417" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9da8212437bb0b10c9d4a7859f05d3dac5096faf_2_417x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9da8212437bb0b10c9d4a7859f05d3dac5096faf_2_625x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9da8212437bb0b10c9d4a7859f05d3dac5096faf_2_834x1000.png 2x" data-dominant-color="4B4A48"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1039×1245 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @JoeNajm (2022-07-29 14:11 UTC)

<p>Thank you for your fast response, is there a way to automatically do that via python code (I couldn’t find any class similar to slicer.app.layoutManager().sliceWidget(“Red”).sliceController() for the “advanced” settings) ?</p>
<p>Moreover, I noticed that the plane intersect does not work anymore once the slices are linked<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f62d999cb5bda1fa45c23f2fa3fcf69630373694.jpeg" data-download-href="/uploads/short-url/z7N9DhM8pPo0C0BHBtXIqmODarW.jpeg?dl=1" title="Screenshot from 2022-07-29 16-03-49" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f62d999cb5bda1fa45c23f2fa3fcf69630373694_2_690x467.jpeg" alt="Screenshot from 2022-07-29 16-03-49" data-base62-sha1="z7N9DhM8pPo0C0BHBtXIqmODarW" width="690" height="467" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f62d999cb5bda1fa45c23f2fa3fcf69630373694_2_690x467.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f62d999cb5bda1fa45c23f2fa3fcf69630373694_2_1035x700.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f62d999cb5bda1fa45c23f2fa3fcf69630373694_2_1380x934.jpeg 2x" data-dominant-color="51504F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-07-29 16-03-49</span><span class="informations">1419×962 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Is there a way to have both plane intersect and linked views work together ?</p>
<p>Thanks in advance!<br>
Joe</p>

---

## Post #4 by @pieper (2022-07-29 14:17 UTC)

<p>You can also try the Compare Volumes module, which manages the layout and linking for you and gives other options.  It was meant for comparing registration results but is also good for looking at multiple MR contrasts.  Unfortunately we don’t have up to date documentation for that module (my bad) but here’s an overview that can be migrated to readthedocs as some point.</p>
<p>The <strong>Volumes</strong> section lists all the volumes in the scene.  You can select the ones you want to see and can drag them to set the layout order.</p>
<p>The <strong>Orientation</strong> radio buttons lets you pick between one view or a row of three per volume.</p>
<p>The <strong>Common Background</strong> option lets you overlay all selected volumes in the foreground compared to a reference volume in the background (used with the Visualization Fade/Rock/Flicker modes).  If you have just two volumes you can select one here and uncheck it in the Volumes section and you will get a layout with one set of views with the volumes in foreground and background.</p>
<p><strong>Common Label</strong> isn’t useful as much now because Segmentations are shown over all views, but if you have a labelmap you can choose to display it.</p>
<p><strong>Hot Link</strong> sets up linking mode so that pan/zoom/scroll happens as you drag vs on mouse release.</p>
<p><strong>Visualization</strong> mode allows you to crossfade between foreground and background when you have common background enabled.  The Rock and Flicker modes animate this action so you can look for subtle changes without needing to use the mouse.  You can also pan/zoom/scroll while the animation modes are active to explore the volumes.</p>
<p>The <strong>+ - Fit</strong> buttons control the field of view of the slice views.</p>
<p><strong>Compare Checked Volumes</strong> is the button to apply the Volumes, Orientation, and Common Background/Label options in a custom layout.  Note that in current Slicer it seems you sometimes need to <em>click the Fit button</em> after applying a new layout.</p>
<p>The <strong>Layer Reveal Cursor</strong> show a real-time checkerboard of the foreground and background as you move the mouse over the slice views.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab9476a328f5be9b73b4d95652bc816f5a34dc47.jpeg" data-download-href="/uploads/short-url/otRJbMHRiNtGWgFD7ZAw3BryFwz.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab9476a328f5be9b73b4d95652bc816f5a34dc47_2_690x434.jpeg" alt="image" data-base62-sha1="otRJbMHRiNtGWgFD7ZAw3BryFwz" width="690" height="434" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab9476a328f5be9b73b4d95652bc816f5a34dc47_2_690x434.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab9476a328f5be9b73b4d95652bc816f5a34dc47_2_1035x651.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab9476a328f5be9b73b4d95652bc816f5a34dc47_2_1380x868.jpeg 2x" data-dominant-color="6C6B6B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1208 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfdb7db54447545ffed5a7ffd65d72ac50aa15e6.jpeg" data-download-href="/uploads/short-url/tEN5Ov2yO0TFhIfyTNJPbQmsKkm.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfdb7db54447545ffed5a7ffd65d72ac50aa15e6_2_690x431.jpeg" alt="image" data-base62-sha1="tEN5Ov2yO0TFhIfyTNJPbQmsKkm" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfdb7db54447545ffed5a7ffd65d72ac50aa15e6_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfdb7db54447545ffed5a7ffd65d72ac50aa15e6_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfdb7db54447545ffed5a7ffd65d72ac50aa15e6_2_1380x862.jpeg 2x" data-dominant-color="656565"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1202 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/832ae33a5fda826eb113647ffb7344f494c62f5d.jpeg" data-download-href="/uploads/short-url/iImqXMPRCNvdUvGrY3fjRY6eCU5.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/832ae33a5fda826eb113647ffb7344f494c62f5d_2_690x227.jpeg" alt="image" data-base62-sha1="iImqXMPRCNvdUvGrY3fjRY6eCU5" width="690" height="227" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/832ae33a5fda826eb113647ffb7344f494c62f5d_2_690x227.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/832ae33a5fda826eb113647ffb7344f494c62f5d_2_1035x340.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/832ae33a5fda826eb113647ffb7344f494c62f5d_2_1380x454.jpeg 2x" data-dominant-color="AAAAA9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1538×508 87.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2022-07-29 22:26 UTC)

<aside class="quote no-group" data-username="JoeNajm" data-post="3" data-topic="24564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/joenajm/48/16145_2.png" class="avatar"> JoeNajm:</div>
<blockquote>
<p>Moreover, I noticed that the plane intersect does not work anymore once the slices are linked</p>
</blockquote>
</aside>
<p>Unfortunately, interactive slice intersections is still an experimental features. This behavior is a bug that will be fixed at some point, but currently not a priority. You can monitor the status of the fix here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6487">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6487" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6487" target="_blank" rel="noopener">Interactive slice intersection displays random lines if more than 3 views</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-07-29" data-time="22:25:34" data-timezone="UTC">10:25PM - 29 Jul 22 UTC</span>
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
          Type: Bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## Summary

Interactive slice intersections appear as quite random parallel li<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">nes when there are more than 3 slices in the view group.

![image](https://user-images.githubusercontent.com/307929/181852988-2bf5d912-6896-4d04-88f3-08071ceae995.png)

## Steps to reproduce

- Load an image
- Switch to `Three over three` view layout
- In View controllers module, set Advanced -&gt; View group to 0 for Red+, Yellow+, Green+ views 
- Enable slice intersection display, enable interaction
- Move the mouse while holding down the shift. The slice intersections appear incorrectly, as parallel lines.

## Expected behavior

Intersection lines should look similar to how the look in non-interactive mode.

## Environment
- Slicer version: Slicer-5.0.3
- Operating system: Windows</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
