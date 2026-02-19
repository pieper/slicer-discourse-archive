---
topic_id: 8973
title: "Automatic Center Volume When Clicking On The Eye To Show Vol"
date: 2019-10-31
url: https://discourse.slicer.org/t/8973
---

# Automatic center volume when clicking on the eye to show volume

**Topic ID**: 8973
**Date**: 2019-10-31
**URL**: https://discourse.slicer.org/t/automatic-center-volume-when-clicking-on-the-eye-to-show-volume/8973

---

## Post #1 by @giovform (2019-10-31 14:56 UTC)

<p>Hi, I have multiple volumes and would like to call</p>
<pre><code>slicer.util.resetSliceViews()
</code></pre>
<p>when the ‘eye’ button is clicked to show the volume.</p>
<p>Is there a way to script this behavior?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2019-10-31 15:00 UTC)

<p>It is already available as an option in Data module in recent Slicer Prevew Releases. Right-click on a volume’s eye icon and check “Reset field of view on show”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e269c55e69892c76526214cf679b657388eca3f.png" data-download-href="/uploads/short-url/fIrfaREM9Xm34IZJ9ce4xN2mOg7.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e269c55e69892c76526214cf679b657388eca3f.png" alt="image" data-base62-sha1="fIrfaREM9Xm34IZJ9ce4xN2mOg7" width="690" height="121" data-dominant-color="DADFE1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">730×129 15.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @giovform (2019-10-31 15:07 UTC)

<p>Nice! Is there a way set as default behavior when Slicer starts?</p>

---

## Post #4 by @lassoan (2019-10-31 16:03 UTC)

<p>Yes. The choice is stored persistently in application settings.</p>

---

## Post #5 by @giovform (2019-10-31 16:05 UTC)

<p>Yes. Just found it on the Slicer.ini file. Thanks!</p>
<pre><code>[SubjectHierarchy]
ResetFieldOfViewOnShowVolume=true</code></pre>

---
