---
topic_id: 20234
title: "Data Module Remember Previous Zoom Pan Slice Selection When"
date: 2021-10-19
url: https://discourse.slicer.org/t/20234
---

# Data module: remember previous zoom & pan & slice selection when making a volume visible

**Topic ID**: 20234
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/data-module-remember-previous-zoom-pan-slice-selection-when-making-a-volume-visible/20234

---

## Post #1 by @DIV (2021-10-19 11:49 UTC)

<p>In the Data module if a different Volume is made visible, the <em>full field of view</em> of that Volume is displayed in each orthogonal slice, for the <em>middle slice</em> in the respective series.</p>
<p>I would prefer either one of the following:</p>
<ul>
<li>remember any previously used display parameters (zoom, pan, slice selection) for <em>that Volume</em>, and re-apply them when displaying the Volume again;  <strong>or</strong>
</li>
<li>remember the ‘incumbent’ display parameters (zoom, pan, slice selection) for <em>the Volume that had most recently been visible</em>, and apply them to the newly visible Volume.</li>
</ul>
<p>—DIV</p>

---

## Post #2 by @jamesobutler (2021-10-19 12:49 UTC)

<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>remember the ‘incumbent’ display parameters (zoom, pan, slice selection) for <em>the Volume that had most recently been visible</em> , and apply them to the newly visible Volume.</p>
</blockquote>
</aside>
<p>This is currently possible when selecting the volume to view by using a slice view controller to set your background(or foreground) volume node.</p>

---

## Post #3 by @lassoan (2021-10-20 04:48 UTC)

<p>You can also right-click the eye icon to customize what it does. You can disable resetting of field of view and orientation by unchecking the corresponding two checkboxes:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30be797e4fc8fe06278f62bbbbb9aec117b7ef51.png" data-download-href="/uploads/short-url/6Xd0wEyPsj9jY2pX7JuDzBtnlCh.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30be797e4fc8fe06278f62bbbbb9aec117b7ef51_2_690x433.png" alt="image" data-base62-sha1="6Xd0wEyPsj9jY2pX7JuDzBtnlCh" width="690" height="433" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30be797e4fc8fe06278f62bbbbb9aec117b7ef51_2_690x433.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/30be797e4fc8fe06278f62bbbbb9aec117b7ef51_2_1035x649.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/30be797e4fc8fe06278f62bbbbb9aec117b7ef51.png 2x" data-dominant-color="BFC3BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1098×690 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @DIV (2021-10-20 07:57 UTC)

<p>Thanks, James.<br>
I had seen the ‘preferred’ behaviour in the Slice Controllers of the <strong>View Controllers</strong> module before — although I’d temporarily forgotten about it, so it’s good to be reminded.<br>
However, it seems that in there the volume would have to be specified three separate times — once for each orthogonal slice.<br>
—DIV</p>

---

## Post #5 by @DIV (2021-10-20 08:13 UTC)

<p>Thanks, Andras.<br>
So it seems that the feature I was talking about is already present!</p>
<p>I notice that it is necessary to right-click on the eye for <em>one of the volumes</em> in the hierarchy (it won’t work when clicking on the eye for a segmentation, for example), and thereafter the setting is automatically applied to all other volumes open in that instance of Slicer.<br>
It appears that the preference is also preserved for new instances of Slicer.</p>
<p>—DIV</p>
<p>P.S.  It never occurred to me to right-click any of the eyes in the hierarchy.</p>

---

## Post #6 by @jamesobutler (2021-10-20 12:53 UTC)

<aside class="quote no-group" data-username="DIV" data-post="4" data-topic="20234">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>However, it seems that in there the volume would have to be specified three separate times — once for each orthogonal slice.</p>
</blockquote>
</aside>
<p>You only have to do it once if you have pressed the link button in the slice controller. This applies the same action to all linked slice views.</p>

---
