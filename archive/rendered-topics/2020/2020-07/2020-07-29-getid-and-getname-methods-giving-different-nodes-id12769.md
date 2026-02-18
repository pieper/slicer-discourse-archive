# GetID() and GetName() methods giving different nodes

**Topic ID**: 12769
**Date**: 2020-07-29
**URL**: https://discourse.slicer.org/t/getid-and-getname-methods-giving-different-nodes/12769

---

## Post #1 by @dloopz (2020-07-29 14:03 UTC)

<p>Operating system: Ubuntu Debian 18.04 (KDE neon 5.19)<br>
Slicer version: 4.11.0-2020-06-05<br>
Expected behavior: Getting unic node by its ID<br>
Actual behavior: Getting other node ID by GetID() method</p>
<p>Hi!</p>
<p>I’m devoloping a segmentation module using some of the Sequences Module logic to create or manipulate sequences. When I try to get first and last DataNodes from a sequence, i’m getting a wrong node ID by GetID() method. I think that next image is better to explain my problem:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9c15ec4beacbc6718e873e0f471bbabaa64a5f3.png" data-download-href="/uploads/short-url/qvgCNoAV6hLuIjGRDGqtMvPRWsr.png?dl=1" title="Screenshot_20200729_104722" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9c15ec4beacbc6718e873e0f471bbabaa64a5f3_2_690x185.png" alt="Screenshot_20200729_104722" data-base62-sha1="qvgCNoAV6hLuIjGRDGqtMvPRWsr" width="690" height="185" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9c15ec4beacbc6718e873e0f471bbabaa64a5f3_2_690x185.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9c15ec4beacbc6718e873e0f471bbabaa64a5f3_2_1035x277.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9c15ec4beacbc6718e873e0f471bbabaa64a5f3.png 2x" data-dominant-color="B0B2B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20200729_104722</span><span class="informations">1155×311 49.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The SequenceNode is the one selected (named ‘1proxy_Backg_cardIAc’) and has 2 ScalarVolumeNodes as DataNodes (‘patient045_frame01’ and ‘patient045_frame13’). When i try to get first node of sequence by its ID, I get ‘v4_cSAX_time_1’. Anny suggestion?</p>
<p>Here you can see that sequence is actually formed by ‘patient045_frame01’ and ‘patient045_frame13’ nodes:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2baeaff86ca697e54179e7d4b6335f9b1bf3193f.png" alt="Screenshot_20200729_110248" data-base62-sha1="6eqNqwS9TW2aHvlNX5Co9ls8Ha7" width="500" height="347"></p>
<p>Thanks!<br>
Lucca</p>

---

## Post #2 by @cpinter (2020-07-29 14:21 UTC)

<p>The data nodes in a sequence are not stored in the main Slicer MRML scene, but in a private scene inside the sequence. They become accessible in the main Slicer scene via the proxy node for the selected item. You can either set the item and use the proxy node, or get the internal sequence MRML scene using <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSequenceNode.h#L145">this function</a>.</p>

---
