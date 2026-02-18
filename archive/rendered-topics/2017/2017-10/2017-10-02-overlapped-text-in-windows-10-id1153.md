# Overlapped text in Windows 10

**Topic ID**: 1153
**Date**: 2017-10-02
**URL**: https://discourse.slicer.org/t/overlapped-text-in-windows-10/1153

---

## Post #1 by @TudorSlicer (2017-10-02 13:22 UTC)

<p>I have a new Windows Surface Pro 4 running Windows 10.   I have loaded the latest version of slicer 4.7.0.   When I import dicom and want to choose the series, the list of patients and the list of series is overlapped and difficult to read.</p>
<p>          <a href="http://i246.photobucket.com/albums/gg102/tudordoc/th_Slicer%20screenshot_zpshzudmiig.jpg" target="_blank" rel="nofollow noopener" class="onebox">
            <img src="http://i246.photobucket.com/albums/gg102/tudordoc/th_Slicer%20screenshot_zpshzudmiig.jpg" width="160" height="71">
          </a>
</p>
<p>The Surface Pro is an i7 with 16Gbram ,   In spite of this Slicer seems to run slower when doing tasks such as crop selection of ROI</p>

---

## Post #2 by @ihnorton (2017-10-02 14:08 UTC)

<p>Do you have display scaling enabled? If so, this will hopefully be resolved in a few weeks when we move to Qt5.</p>
<p>If you want to make sure the problem is tracked for resolution, please comment on the issue below or open a new issue:</p>
<p><a href="https://issues.slicer.org/view.php?id=4418" class="onebox" target="_blank">https://issues.slicer.org/view.php?id=4418</a></p>

---

## Post #3 by @lassoan (2017-10-02 14:22 UTC)

<p>You can also try adjusting row spacing in the widget by clicking on <code>&gt;&gt; </code> button in the menu bar of the wiget and setting <code>Density</code> to <code>Comfortable</code>:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/5742e8f7f4a8515f8771d01f59e0b6904beaac45.png" data-download-href="/uploads/short-url/crWTqAJHwezMTxwtLYw6gZpYTT7.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/5742e8f7f4a8515f8771d01f59e0b6904beaac45.png" alt="image" data-base62-sha1="crWTqAJHwezMTxwtLYw6gZpYTT7" width="690" height="113" data-dominant-color="F3F0EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">792×130 11.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @TudorSlicer (2017-10-02 15:18 UTC)

<p>Bingo! (An english expression - maybe lost on others)   Changing the row spacing makes it easier to see.</p>
<p>Thanks</p>
<p>Boyd</p>

---
