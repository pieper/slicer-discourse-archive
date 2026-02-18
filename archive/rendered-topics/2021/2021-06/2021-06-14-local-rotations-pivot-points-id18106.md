# Local Rotations, Pivot Points

**Topic ID**: 18106
**Date**: 2021-06-14
**URL**: https://discourse.slicer.org/t/local-rotations-pivot-points/18106

---

## Post #1 by @Fluvio_Lobo (2021-06-14 03:40 UTC)

<p>Hello,</p>
<p><strong>What is the best way of performing rotations about a fiducial marker, landmark, or pivot point?</strong><br>
I would typically use registration, but I do not have a target segment (final position/rotation) for these structures. In general, I am trying to <strong>roll</strong> the mandible about its condyle. I am also interested in defining an axis of rotation (defined by two landmarks).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07e0db7ff32cb2901b6049a5ef26905d7eaa29f5.png" data-download-href="/uploads/short-url/17H61eHLdUZ3Ni3e9pNYo6K2qz3.png?dl=1" title="local_rotations" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07e0db7ff32cb2901b6049a5ef26905d7eaa29f5_2_477x375.png" alt="local_rotations" data-base62-sha1="17H61eHLdUZ3Ni3e9pNYo6K2qz3" width="477" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07e0db7ff32cb2901b6049a5ef26905d7eaa29f5_2_477x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07e0db7ff32cb2901b6049a5ef26905d7eaa29f5_2_715x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07e0db7ff32cb2901b6049a5ef26905d7eaa29f5.png 2x" data-dominant-color="242A18"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">local_rotations</span><span class="informations">747×586 266 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Ideally I could make manual rotations and then calculate distances between other landmarks using a CMF module like <a href="https://cmf.slicer.org/" rel="noopener nofollow ugc">Q3DC</a></p>
<p>Note that this is not a typical orthognathic planning, and that is the reason why I am interested in more manual/exploratory options. These cases are missing a condyle and zygomatic arch.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82a29ac5e6cea8e6a0dc7ce3e9768406e0badef0.png" data-download-href="/uploads/short-url/iDErTipeT5fSjHPW1ntA81DUBMI.png?dl=1" title="side_view_missing_condyle" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82a29ac5e6cea8e6a0dc7ce3e9768406e0badef0_2_444x375.png" alt="side_view_missing_condyle" data-base62-sha1="iDErTipeT5fSjHPW1ntA81DUBMI" width="444" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82a29ac5e6cea8e6a0dc7ce3e9768406e0badef0_2_444x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82a29ac5e6cea8e6a0dc7ce3e9768406e0badef0_2_666x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82a29ac5e6cea8e6a0dc7ce3e9768406e0badef0.png 2x" data-dominant-color="130E22"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">side_view_missing_condyle</span><span class="informations">801×676 389 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
