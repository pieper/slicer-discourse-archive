# When Install via conda,Why the radiomics pyradiomics packages are not available from current channels?

**Topic ID**: 10392
**Date**: 2020-02-22
**URL**: https://discourse.slicer.org/t/when-install-via-conda-why-the-radiomics-pyradiomics-packages-are-not-available-from-current-channels/10392

---

## Post #1 by @382831265 (2020-02-22 03:06 UTC)

<p>Operating system:win 10 professional<br>
Slicer version:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ea8322db34a70d80ee838172ea6b5e75e134bf1.jpeg" data-download-href="/uploads/short-url/8WhXBQ6YbASGKaxJtj3heVQUidz.jpeg?dl=1" title="43" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ea8322db34a70d80ee838172ea6b5e75e134bf1_2_690x393.jpeg" alt="43" data-base62-sha1="8WhXBQ6YbASGKaxJtj3heVQUidz" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ea8322db34a70d80ee838172ea6b5e75e134bf1_2_690x393.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ea8322db34a70d80ee838172ea6b5e75e134bf1.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ea8322db34a70d80ee838172ea6b5e75e134bf1.jpeg 2x" data-dominant-color="121212"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">43</span><span class="informations">875×499 93.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @timeanddoctor (2020-02-22 03:21 UTC)

<p>the environment is fail… and you need same more .py files …<br>
please read the feedback: PackagesNot FoundError:’’’’’’</p>

---

## Post #3 by @lassoan (2020-02-22 03:29 UTC)

<p>You can install pyradiomics package in Slicer’s Python environment by installing SlicerRadiomics extension from the extension manager. If you need additional packages then you can run <code>pip_install("packagename")</code> command from Slicer’s Python console.</p>

---
