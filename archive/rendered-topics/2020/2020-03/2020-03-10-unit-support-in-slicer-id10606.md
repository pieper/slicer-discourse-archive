# Unit support in Slicer

**Topic ID**: 10606
**Date**: 2020-03-10
**URL**: https://discourse.slicer.org/t/unit-support-in-slicer/10606

---

## Post #1 by @muratmaga (2020-03-10 02:32 UTC)

<p>Since almost all our users work with sub-millimeter resolution, I am testing how (well) the Units preference work.<br>
I switched to micrometer in settings, and first issue is the mu sign is not displayed correctly on my platform (shows like this �m) Windows build r28798</p>
<p>I downloaded the MRHead and worked on the Segment Editor and look at the margin effect. Margin size is reported in microns, but values are clearly wrong. Anyways, I want to test this more extensively. What would should I report back? What would be most useful thing?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52357364a30f2b136a1481f1b4ce94f58437c649.png" alt="image" data-base62-sha1="bJfFyAQelFR2Q6VeL3wedpUTwN3" width="567" height="449"></p>

---

## Post #2 by @lassoan (2020-03-10 04:45 UTC)

<p>I’ve fixed the mu character encoding, it should show upwell in r28814 and later.</p>
<p>Making units in Slicer fully configurable requires a number of fixes:</p>
<ul>
<li>Use unit-aware widgets (or unit-aware formatting) whenever displaying numerical values with units. There are a number of places where “mm” unit is hardcoded and should be display should be replaced with unit-aware widgets. I remember I had crashes with these widgets in Transform module’s display section and could not easily find the root cause, so just hardcoded mm, but we should give this another go. Examples include: view rulers (horizontal line at the bottom of views) and markups measurements (length of line and curves, surface area of closed curves).</li>
<li>Importers should convert distance units. For example, when loading a DICOM file and the length unit is not mm, the voxel size must be scaled accordingly.</li>
<li>Exporters should write distance units into files.</li>
<li>CLI module interface should be made unit-aware.</li>
<li>All transformable data in the scene must be rescaled when length unit is changed.</li>
<li>All transformable data in the scene must be rescaled when a scene with a different unit is imported.</li>
</ul>
<p>Since these are relatively large and independent tasks, probably separate issues should be added to the issue tracker to make sure they are all addressed (all tagged with Category = “Core: Units”). I can help with advice and reviewing code, but don’t expect to have significant amount of development time.</p>

---

## Post #3 by @lassoan (2020-07-11 18:45 UTC)

<p>For reference, I have entered an issue to track these tasks:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/5040" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5040" target="_blank">Fix custom unit management</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-07-11" data-time="18:44:38" data-timezone="UTC">06:44PM - 11 Jul 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank">
          <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">For numerical stability of various processing methods, it is important to avoid very small and very large numbers.
By default, Slicer uses...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
