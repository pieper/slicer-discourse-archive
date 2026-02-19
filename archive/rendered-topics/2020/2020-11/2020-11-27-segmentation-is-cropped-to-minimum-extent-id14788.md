---
topic_id: 14788
title: "Segmentation Is Cropped To Minimum Extent"
date: 2020-11-27
url: https://discourse.slicer.org/t/14788
---

# Segmentation is cropped to minimum extent

**Topic ID**: 14788
**Date**: 2020-11-27
**URL**: https://discourse.slicer.org/t/segmentation-is-cropped-to-minimum-extent/14788

---

## Post #1 by @ButuiHu (2020-11-27 02:25 UTC)

<p>step to reproduce:</p>
<ol>
<li>create segmentation in segmen editor using the MRHead from sample data.</li>
<li>export segmentation to labelmap</li>
<li>save MRHead, Segmentation, and the labelmap (as <code>Segmentation-label.nrrd</code>) to file.</li>
<li>load MRHead again</li>
<li>load labelmap file <code>Segmentation-label.nrrd</code>, and select Descriptions as Segmentation.</li>
<li>modify the labelmap in segment editor</li>
<li>save the result again as <code>Segmentation-label-new.nrrd</code> without export segmentation to labelmap, and make sure crop to minimum extent is not checked.</li>
<li>now read MRHead, <code>Segmentation-label.nrrd</code>, and <code>Segmentation-label-1.nrrd</code>, and convert to numpy array with simpleitk, check their shape.<br>
The shape is expected to be the same, but it’s not.</li>
</ol>

---

## Post #2 by @lassoan (2020-11-27 02:57 UTC)

<p>In current Slicer versions, segmentation is not cropped to the minimum extent anymore by default. You can enable this option (to reduce memory usage) or disable it (to make it easier to use the segmentation in software that operates in voxel space instead of physical space) in the Save data dialog.</p>

---

## Post #3 by @ButuiHu (2020-11-27 03:23 UTC)

<p>Yes, I’m using the nightly build (20201124). I do not enable the option, but <code>Segmentation-label-1.nrrd</code> is cropped to the minimum extent.</p>

---

## Post #4 by @lassoan (2020-11-27 03:54 UTC)

<aside class="quote no-group" data-username="ButuiHu" data-post="1" data-topic="14788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/butuihu/48/2386_2.png" class="avatar"> ButuiHu:</div>
<blockquote>
<ol>
<li>create segmentation in segmen editor using the MRHead from sample data.</li>
<li>export segmentation to labelmap</li>
<li>save MRHead, Segmentation, and the labelmap (as <code>Segmentation-label.nrrd</code> ) to file.</li>
</ol>
</blockquote>
</aside>
<p>Have a look at the files - MRHead, Segmentation, and the labelmap all have the same extent. They are all correct.</p>
<aside class="quote no-group" data-username="ButuiHu" data-post="1" data-topic="14788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/butuihu/48/2386_2.png" class="avatar"> ButuiHu:</div>
<blockquote>
<ol start="5">
<li>load labelmap file <code>Segmentation-label.nrrd</code> , and select Descriptions as Segmentation.</li>
</ol>
</blockquote>
</aside>
<p>The segmentation that is imported from a labelmap is not associated with any reference volume, so there is no reference geometry to stick to when the segmentation is saved. We need to consider other use cases, too, but probably we can change the behavior so that reference geometry will be set when importing a plain nrrd or nifti file. I’ve added a ticket to track this request:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/5323">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/5323" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5323" target="_blank" rel="noopener">Segmentation imported from plain nrrd file is saved with smaller extent than the original</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-11-27" data-time="03:53:54" data-timezone="UTC">03:53AM - 27 Nov 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2021-08-13" data-time="14:53:57" data-timezone="UTC">02:53PM - 13 Aug 21 UTC</span>
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
    <p class="github-body-container">When a plain nrrd file is loaded as segmentation then the reference geometry is <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">not set and so when the segmentation is saved, the extent is reduced to the minimum necessary. We should preserve the original extent.

See details here:
https://discourse.slicer.org/t/segmentation-is-cropped-to-minimum-extent/14788</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I would recommend to use .seg.nrrd file format for storing segmentations. You can use it the same way in SimpleITK, but it stores extra information, such as segment names, colors, etc. You can access this metadata from Python, without Slicer as shown <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_information_from_segmentation_nrrd_file_header">here</a>.</p>

---

## Post #5 by @ButuiHu (2020-11-27 04:46 UTC)

<p>thanks, if I would like to pad the segmentation to the reference geometry, what meta data should I consider in the <code>.seg.nrrd</code> file?</p>

---

## Post #6 by @lassoan (2020-11-27 04:54 UTC)

<p>If you store segmentation in .seg.nrrd files (with <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationStorageNode.html#details">these custom metadata fields</a>) then the reference geometry will be preserved.</p>
<p>Reference image geometry is stored in <em>Segmentation_ConversionParameters</em> field:</p>
<p><strong>Segmentation_ConversionParameters:=</strong>…sampling is calculated.&amp;<strong>Reference image geometry|0;0;1.2999954223632812;-86.64489746093749;-1;0;0;133.92860412597656;0;-1;0;116.78569793701172;0;0;0;1;0;255;0;255;0;129</strong>;|Image geometry description string determining the geometry of the labelmap that is created in course of conversion. Can be copied from a volume, using the button.&amp;Smoothing factor|0.5|Smoo…</p>

---
