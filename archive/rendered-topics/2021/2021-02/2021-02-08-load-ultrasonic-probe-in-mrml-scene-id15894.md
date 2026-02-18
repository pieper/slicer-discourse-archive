# Load ultrasonic probe in MRML scene

**Topic ID**: 15894
**Date**: 2021-02-08
**URL**: https://discourse.slicer.org/t/load-ultrasonic-probe-in-mrml-scene/15894

---

## Post #1 by @Carl098 (2021-02-08 05:42 UTC)

<p>I am referring to the PediclesCrewSimulator program and want to display an ultrasonic probe of STL data in the scene.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad6904635473b5f47dc736751999c37fae03bef1.png" data-download-href="/uploads/short-url/oK3BeBz5ZIXrb3AWvs99eDWkMNP.png?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad6904635473b5f47dc736751999c37fae03bef1_2_690x468.png" alt="捕获" data-base62-sha1="oK3BeBz5ZIXrb3AWvs99eDWkMNP" width="690" height="468" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad6904635473b5f47dc736751999c37fae03bef1_2_690x468.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad6904635473b5f47dc736751999c37fae03bef1_2_1035x702.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad6904635473b5f47dc736751999c37fae03bef1.png 2x" data-dominant-color="9A99C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">1094×743 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I don’t know how to do this as a beginner, thank you.</p>

---

## Post #2 by @lassoan (2021-02-08 05:50 UTC)

<p>To display the probe model in the scene all you need to do is to drag-and-drop the STL file to the application main window and click OK.</p>
<p>You can position the probe manually as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#apply-transform-to-a-node">here</a>. If you want to display position of a tracked ultrasound probe in real-time or reconstruct 3D volume from a tracked ultrasound stream then you can use <a href="http://slicerigt.org/">SlicerIGT</a> extension. There have been lots of work on using SlicerIGT for spine imaging using tracked ultrasound for scoliosis assessment and pedicle screw insertion guidance. If you tell us what you would like to achieve then we may be able to help you getting started.</p>

---
