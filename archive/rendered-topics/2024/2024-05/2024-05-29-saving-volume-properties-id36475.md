---
topic_id: 36475
title: "Saving Volume Properties"
date: 2024-05-29
url: https://discourse.slicer.org/t/36475
---

# Saving volume properties

**Topic ID**: 36475
**Date**: 2024-05-29
**URL**: https://discourse.slicer.org/t/saving-volume-properties/36475

---

## Post #1 by @Stuart (2024-05-29 18:50 UTC)

<p>I’m having what I’m sure is a newbie problem. I’m working with a 3D view of a dcm file. In Volume Rendering I optimize the Display and Advanced parameters to achieve my desired result. I then save the project as a mrb file. After closing the scene and reopening the file the Volume Rendering settings that I had adjusted are not preserved. What do I need to do to retain these settings?</p>
<p>Thanks,</p>
<p>Stuart</p>

---

## Post #3 by @pieper (2024-05-29 19:16 UTC)

<p>Volume rendering settings should be saved in the .mrb file and restored when you load the scene.  Please report what version of slicer you are using and exactly what steps you take.  See if you can reproduce the issue using data from the SampleData module.  Maybe there are some advanced parameters that aren’t be saved correctly and it would help if you identified which ones.</p>

---

## Post #4 by @Stuart (2024-05-29 21:32 UTC)

<p>Thank you both for causing me to look into this issue a little more deeply.</p>
<p>I’m using Slicer 5.6.2. My project involves working with a CT file that has been segmented. When I open this project with the segmentation display turned off and I go to Volume Rendering the 3D CT display has a red highlight. Both the Scalar Opacity and Scalar Color Mapping includes a red band. This is my core problem. I wish to delete this red band permanently. When I select “Synchronized with Volumes” module my 3D rendering is reverts to gray scale only. However, after saving this revised version as a mrb file and then reload this revised project, both the Scalar Opacity and Scalar Color Mapping still include a red band. Otherwise, all numerical values for Threshold, Opacity and in Advanced are identical in both versions.</p>
<p>I don’t know where this red zone I’m my project comes from given that I’m working with CT images but I would like to remove it permanently. Thanks for your help.</p>

---

## Post #5 by @muratmaga (2024-05-29 23:51 UTC)

<p>I think we have to see the mrb file to understand what’s going on. Can you share that? Or maybe provide a screenshot of the red band.</p>

---

## Post #6 by @Stuart (2024-05-30 03:02 UTC)

<p>Here’s a screenshot showing the red band:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/5392ec6d479ec93d8b63c8f93abaf3bd71156473.jpeg" data-download-href="/uploads/short-url/bVkpyP7EdFhThdTcEwsJXo17UTF.jpeg?dl=1" title="Screenshot 2024-05-29 at 8.21.29 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5392ec6d479ec93d8b63c8f93abaf3bd71156473_2_479x499.jpeg" alt="Screenshot 2024-05-29 at 8.21.29 PM" data-base62-sha1="bVkpyP7EdFhThdTcEwsJXo17UTF" width="479" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5392ec6d479ec93d8b63c8f93abaf3bd71156473_2_479x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5392ec6d479ec93d8b63c8f93abaf3bd71156473_2_718x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5392ec6d479ec93d8b63c8f93abaf3bd71156473_2_958x998.jpeg 2x" data-dominant-color="BDBCCA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-29 at 8.21.29 PM</span><span class="informations">1712×1784 225 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The history is this:</p>
<ol>
<li>Open the segmented mrb file</li>
<li>Open Data and turn off segmentation</li>
<li>Open Volume Rendering and see the attached image</li>
<li>Check and uncheck Synchronize with Volumes module to convert to gray scale image</li>
<li>Adjust Threshold, Opacity and Advanced to suit taste</li>
<li>Save modified project as mrb file</li>
<li>Open the newly saved file and see the attached with red band</li>
</ol>
<p>Where does the red band come from? How to remove it permanently?</p>
<p>I tried to attach mrb file but was unsuccessful  - wrong authorized file extension. How do I upload a mrb file?</p>
<p>Thanks</p>

---

## Post #7 by @muratmaga (2024-05-30 15:01 UTC)

<aside class="quote no-group" data-username="Stuart" data-post="6" data-topic="36475">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/cab0a1/48.png" class="avatar"> Stuart:</div>
<blockquote>
<p>How do I upload a mrb file?</p>
</blockquote>
</aside>
<p>You can post it somewhere on the cloud (e.g., dropbox) and then share the public link. Discourse only supports attaching images and video.</p>
<p>Try this:<br>
Go to inputs, and choose to create a new volume property. Then click on (and then off) Synchronize with Volumes module. This should give a basic grayscale ramp, which i think is what you are looking for.</p>

---

## Post #8 by @lassoan (2024-05-30 15:09 UTC)

<p>If you share the scene file then we can tell where the red control point in the scalar color mapping function comes from and suggest how to fix it permanently.</p>

---

## Post #9 by @Stuart (2024-05-30 15:10 UTC)

<p>I’ve learned that if I delete the volume property and add a new one the red cast disappears. However, when I save the project as a mrb file and then reopen it the recast has returned. I hope this observation is useful in understanding what is amiss. Thanks.</p>

---

## Post #10 by @Stuart (2024-05-30 15:24 UTC)

<p>Here’s the Dropbox link: <a href="https://www.dropbox.com/scl/fi/wsu02odzgauws40ihhcso/02-90Cu-32-LR-Reversed.mrb?rlkey=x7aj40khq3iczs0q8tje40xeu&amp;st=foq0yaqn&amp;dl=0" class="inline-onebox" rel="noopener nofollow ugc">Dropbox</a></p>

---

## Post #11 by @muratmaga (2024-05-30 16:40 UTC)

<p>You have a very unusual dataset. The intensities are between 0 and 0.148 and saved as double precision.<br>
I don’t think the volume rendering widgets are designed to handle such low range. The typical intensity values for CT data have 12 bit range (e.g., 0-4096).</p>
<p>I did those changes (Simple Filter-&gt;Rescale Intensity Filter to scale the image 0-4905. Then run the Cast Image Module and choose the option to set unsigned short). everything works fine, with a regular grayscale ramp that persists.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d9146b02ecb33132a43ec77d3c427bb52b89d9e.jpeg" data-download-href="/uploads/short-url/1W1svorakHPvnJSis3QYqk7c0TY.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d9146b02ecb33132a43ec77d3c427bb52b89d9e_2_690x330.jpeg" alt="image" data-base62-sha1="1W1svorakHPvnJSis3QYqk7c0TY" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d9146b02ecb33132a43ec77d3c427bb52b89d9e_2_690x330.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d9146b02ecb33132a43ec77d3c427bb52b89d9e_2_1035x495.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d9146b02ecb33132a43ec77d3c427bb52b89d9e_2_1380x660.jpeg 2x" data-dominant-color="5A5B5E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×921 93.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @lassoan (2024-05-30 18:36 UTC)

<p>I’ve found the root cause of the unexpected red color appearing. The line length in the .vp file reader had an arbitrary maximum line length (1024 characters), therefore when many control points were in the color transfer function then the list of points got truncated. Since truncation occurred in the middle of an entry, the red component was successfully read out, but the green and blue were missing and set to 0.</p>
<p>I’ll push a fix today or tomorrow.</p>

---

## Post #13 by @Stuart (2024-05-30 19:48 UTC)

<p>I followed the steps you outlined and got exactly the same result as in your image including the two control points and nice ramp and same appearance of the 3D image. I then saved the file with a new name, closed the scene, and loaded the new file. This is the result I obtained:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c74f653c97be164ca9f6e37f445893ac6480cf0d.jpeg" data-download-href="/uploads/short-url/srb7tA6AvI8j4mftgJL3gtE3WR7.jpeg?dl=1" title="Screenshot 2024-05-30 at 1.35.08 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c74f653c97be164ca9f6e37f445893ac6480cf0d_2_690x466.jpeg" alt="Screenshot 2024-05-30 at 1.35.08 PM" data-base62-sha1="srb7tA6AvI8j4mftgJL3gtE3WR7" width="690" height="466" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c74f653c97be164ca9f6e37f445893ac6480cf0d_2_690x466.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c74f653c97be164ca9f6e37f445893ac6480cf0d_2_1035x699.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c74f653c97be164ca9f6e37f445893ac6480cf0d_2_1380x932.jpeg 2x" data-dominant-color="67686B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-30 at 1.35.08 PM</span><span class="informations">1920×1298 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Why isn’t the scalar mapping information retained and why is the 3D image different?</p>
<p>I can readjust the mapping and reconstruct the result but why isn’t this information retained in volume properties?</p>
<p>Thanks</p>

---

## Post #14 by @muratmaga (2024-05-30 21:44 UTC)

<aside class="quote no-group" data-username="Stuart" data-post="13" data-topic="36475">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/cab0a1/48.png" class="avatar"> Stuart:</div>
<blockquote>
<p>Why isn’t the scalar mapping information retained and why is the 3D image different?</p>
</blockquote>
</aside>
<p>perhaps it is related to the issue <a class="mention" href="/u/lassoan">@lassoan</a> posted above. When the push is fixed, please try with the latest preview version and see if the issue persists.</p>

---

## Post #15 by @lassoan (2024-05-31 13:11 UTC)

<p>The fix for the truncated color transfer function is submitted and currently under review:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7772">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7772" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7772" target="_blank" rel="noopener">BUG: Fix reading of volume property (.vp) file</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:fix-vp-file-reading</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2024-05-31" data-time="13:10:11" data-timezone="UTC">01:10PM - 31 May 24 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 7 files with 46 additions and 54 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7772/files" target="_blank" rel="noopener">
            <span class="added">+46</span>
            <span class="removed">-54</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Color transfer function line in .vp files can be several thousands character lon<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7772" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">g when there are many control points but the reader had a hardcoded limit at 1024 bytes. Fixed by switching to use an API that does not limit line length.

As a preventive action, all other line parsing where a hardcoded line length limit was set is replaced.

Fixes the issue reported at https://discourse.slicer.org/t/saving-volume-properties/36475/12</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #16 by @Stuart (2024-05-31 17:03 UTC)

<p>Now I’m working with Slicer 5.7.0-2024-05-30, revision 32881.</p>
<p>I’ve opened my project and the red band issue is complete absent. Hurray.</p>
<p>I then created a new volume property, clicked the Synchronize with Volume module on and off, and then adjusted the Threshold and Opacity. This revised project was saved with a new number and then reopened. Unfortunately the adjusted volume properties were not retained. They could easily be reset but were still not retained when repeating this process.</p>

---

## Post #17 by @muratmaga (2024-05-31 20:31 UTC)

<p>I don’t think today’s preview build has those fixed. Changes are merged less than an hour ago. So the earliest it will be incorporated will be tomorrow’s preview build (make sure the revision number has increased before downloading, if build doesn’t complete tonight due to any reason, it will still the same version as today.).</p>

---

## Post #18 by @Stuart (2024-05-31 21:35 UTC)

<p>Well that’s interesting isn’t it?</p>

---

## Post #19 by @lassoan (2024-06-01 12:26 UTC)

<p>I’m not sure what you mean. We fully understand what happened any why: only the first 1024 bytes of the color transfer function was read from the .vp file, which caused incomplete loading and potentially color corruption of the last read color point.</p>
<p>The fix was integrated yesterday and is now available in the Slicer Preview Release today (2024-06-01). Yesterday’s release did not contain the fix.</p>

---

## Post #20 by @Stuart (2024-06-02 17:17 UTC)

<p>Thanks Andras,</p>
<p>This morning I downloaded the new release (5.7.0-2024-06-01 r32886 / eceb683) and all my difficulties disappeared.</p>
<p>You deserve a raise!</p>

---
