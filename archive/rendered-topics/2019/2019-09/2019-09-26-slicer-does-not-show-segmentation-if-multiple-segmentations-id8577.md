---
topic_id: 8577
title: "Slicer Does Not Show Segmentation If Multiple Segmentations"
date: 2019-09-26
url: https://discourse.slicer.org/t/8577
---

# Slicer does not show segmentation if multiple segmentations exists

**Topic ID**: 8577
**Date**: 2019-09-26
**URL**: https://discourse.slicer.org/t/slicer-does-not-show-segmentation-if-multiple-segmentations-exists/8577

---

## Post #1 by @Alex_Vergara (2019-09-26 08:13 UTC)

<p>I have several volumes in a scene, each one with an own segmentation. When I try to visualize the corresponding segmentation it is not shown at all, see this picture</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/802c37867ba26497f7535a8a73899feab33e4d94.jpeg" data-download-href="/uploads/short-url/ihRQJf9uuBmjCyrCjgCzvxA3NHu.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/802c37867ba26497f7535a8a73899feab33e4d94_2_690x431.jpeg" alt="image" data-base62-sha1="ihRQJf9uuBmjCyrCjgCzvxA3NHu" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/802c37867ba26497f7535a8a73899feab33e4d94_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/802c37867ba26497f7535a8a73899feab33e4d94_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/802c37867ba26497f7535a8a73899feab33e4d94_2_1380x862.jpeg 2x" data-dominant-color="68686D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2239×1400 423 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For reference, I created the different segmentations programmatically and use <code>shNode.SetDisplayVisibilityForBranch(segnodeID, 0)</code> to hide them temporarily. But when I want to show a single one, I open all the eyes (see picturre) and nothing happened, I know the segmentation is there (see the 3D view).</p>
<p>What is happening here?</p>

---

## Post #2 by @Alex_Vergara (2019-09-26 09:53 UTC)

<p>Hmm, it turns out there is a problem in hiding the branch visibility inside the shNode. The only way that is currently working is by using <code>segmentationNode.GetDisplayNode().SetVisibility(0)</code><br>
For those using the old wikis that still use the <code>SetDisplayVisibilityForBranch</code>, please note it does not work.<br>
Using the new DisplayNodes for segmentations:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/977de2ab5c3693b6aaa6958a6f518af46bd4ceed.jpeg" data-download-href="/uploads/short-url/lC9NZv3WNF0LJrCPRiUJY8mOQjP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/977de2ab5c3693b6aaa6958a6f518af46bd4ceed_2_690x434.jpeg" alt="image" data-base62-sha1="lC9NZv3WNF0LJrCPRiUJY8mOQjP" width="690" height="434" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/977de2ab5c3693b6aaa6958a6f518af46bd4ceed_2_690x434.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/977de2ab5c3693b6aaa6958a6f518af46bd4ceed_2_1035x651.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/977de2ab5c3693b6aaa6958a6f518af46bd4ceed_2_1380x868.jpeg 2x" data-dominant-color="6C6C70"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2232×1404 478 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @cpinter (2019-09-26 11:51 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="2" data-topic="8577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>old wikis that still use the <code>SetDisplayVisibilityForBranch</code></p>
</blockquote>
</aside>
<p>If you know of a page for the latest version that contains this, please let me know. I just made this change a week or so ago (see <a href="https://discourse.slicer.org/t/improvements-in-atlas-management-model-hierarchy-refactoring/8512">here</a> and specifically for folder visibility, <a href="https://github.com/Slicer/Slicer/commit/1144f81c58bd7c0a4e90d417601d3e4bd803088d">here</a>), and probably some of the documentation is still not updated.</p>

---

## Post #4 by @Alex_Vergara (2019-10-01 12:46 UTC)

<p>You can start by <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulate_subject_hierarchy_item" rel="nofollow noopener">this script repository</a></p>

---

## Post #5 by @Alex_Vergara (2019-10-01 13:47 UTC)

<p>There is also a “bug”? The tables, charts and plot nodes does not have DisplayNodes</p>
<pre><code class="lang-auto">AttributeError: 'MRMLCorePython.vtkMRMLPlotChartNode' object has no attribute 'GetDisplayNode'
</code></pre>
<p>and doing <code>shNode.SetDisplayVisibilityForBranch(itemID, 1)</code> for them does not display them in the sh view. They are now hidden in the view, only visible in the all nodes view. Is this behaviour intentional?</p>

---

## Post #6 by @cpinter (2019-10-01 14:02 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="5" data-topic="8577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>and doing <code>shNode.SetDisplayVisibilityForBranch(itemID, 1)</code></p>
</blockquote>
</aside>
<p>Please refer to the links in my comment above. The SetDisplayVisibilityForBranch function should not be used anymore.<br>
Or if you have this issue with a nightly that is older than two weeks then please update to the latest one, and use the new way of show/hiding branches.</p>

---

## Post #7 by @cpinter (2019-10-01 14:03 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="4" data-topic="8577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>You can start by <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulate_subject_hierarchy_item">this script repository</a></p>
</blockquote>
</aside>
<p>I didn’t find mentions of SetDisplayVisibilityForBranch in the script repository so not sure what you refer to. Please be more specific in terms of what is outdated and I’ll fix it. Thanks!</p>
<p>Update: Sorry, wrong, I did find one. I updated the show/hide examples. Let me know if there is anything else.</p>

---
