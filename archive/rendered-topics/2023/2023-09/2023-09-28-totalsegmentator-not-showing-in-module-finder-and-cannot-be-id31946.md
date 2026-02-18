# TotalSegmentator not showing in module finder, and cannot be uninstall from extension module

**Topic ID**: 31946
**Date**: 2023-09-28
**URL**: https://discourse.slicer.org/t/totalsegmentator-not-showing-in-module-finder-and-cannot-be-uninstall-from-extension-module/31946

---

## Post #1 by @zariliusra (2023-09-28 13:54 UTC)

<p>Hi, I’ve installed TotalSegmentator but it cannot be found in the module finder. When I open the extension module and try to uninstall TotalSegmentator, a prompt appears: “Failed to open extension setting…”</p>
<p>please give advice how to overcome this problem. Thank you</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7d72cd1c245c96f3dfa25ba40181812fe53b262.png" alt="image" data-base62-sha1="nWMKnsvtp7ckVt767kWL0YQf9Ps" width="556" height="139"></p>

---

## Post #2 by @rbumm (2023-09-28 14:22 UTC)

<p>How did you install the TotalSegmentator extension? Via the extension manager?</p>

---

## Post #3 by @zariliusra (2023-09-28 14:42 UTC)

<p>Yes, I installed it via extension manager.</p>

---

## Post #4 by @rbumm (2023-09-28 16:16 UTC)

<p>I would uninstall everything and delete the Slicer folder.<br>
Then Install Slicer, install Pytorch extension, and install TotalSegmentator extension. It should be found under “Segmentations”.</p>

---

## Post #5 by @lassoan (2023-09-28 17:43 UTC)

<p>Have you changed the default Slicer installation location? The screenshot indicates that it is installed into some shared location instead of your user folder. Does your user have write access to that folder?</p>

---

## Post #6 by @zariliusra (2023-09-28 22:43 UTC)

<p>Thank you; I’m trying this.</p>

---

## Post #7 by @zariliusra (2023-09-28 22:45 UTC)

<p>No, i use the default Slicer installation location. But the default is in “ProgramData”. (i’m trying to reinstall it). Should i install it in different location?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/581abef184f0e6810a729b31ed51f6c7547d565e.png" alt="image" data-base62-sha1="czpjQIVsa9WbV1wx6qiPRwPNnaK" width="513" height="408"></p>

---

## Post #8 by @zariliusra (2023-09-28 23:32 UTC)

<p>Hi Professor. I’ve re installed it, and it works. Thank you very much! <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=12" title=":blush:" class="emoji" alt=":blush:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @zariliusra (2023-09-28 23:37 UTC)

<p>Hi, Mr. Lassoan, I’ve installed the totalsegmentator and it works when I’m trying to use the total option. But when i use bone extremities option (i’ve already got the bone extremities license for student), it gets this error. Please enlighten me</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f0807efc0c62aadb56ada42bb21374384638775.png" data-download-href="/uploads/short-url/6I3E8OlRut3SsnSwdtVscktQ6fb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f0807efc0c62aadb56ada42bb21374384638775_2_556x500.png" alt="image" data-base62-sha1="6I3E8OlRut3SsnSwdtVscktQ6fb" width="556" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f0807efc0c62aadb56ada42bb21374384638775_2_556x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f0807efc0c62aadb56ada42bb21374384638775_2_834x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f0807efc0c62aadb56ada42bb21374384638775.png 2x" data-dominant-color="9B9B9B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1037×931 193 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @rbumm (2023-09-29 06:58 UTC)

<p>did you import the weights for “bones-extremities”?</p>

---

## Post #11 by @zariliusra (2023-09-29 08:18 UTC)

<p>yes, i did Prof. Or does the “bone extremities” weight different from “Task278_TotalSegmentator_part6_bones_1259subj”?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b255c193ab9adcca28123b735ec7e0a875cec868.png" data-download-href="/uploads/short-url/prCIJj9x8kjoxw9klwSZ99BD9aw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b255c193ab9adcca28123b735ec7e0a875cec868_2_690x326.png" alt="image" data-base62-sha1="prCIJj9x8kjoxw9klwSZ99BD9aw" width="690" height="326" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b255c193ab9adcca28123b735ec7e0a875cec868_2_690x326.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b255c193ab9adcca28123b735ec7e0a875cec868_2_1035x489.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b255c193ab9adcca28123b735ec7e0a875cec868.png 2x" data-dominant-color="F1F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1119×529 82.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2ade2004c570efd71054d9ed02e9aad34bb2d98.png" alt="image" data-base62-sha1="puFwYQk1ItUZzGifDIZRhNIHD3W" width="486" height="487"></p>

---

## Post #12 by @rbumm (2023-09-29 09:08 UTC)

<p>Jakob <a class="mention" href="/u/wasserth">@wasserth</a> could you comment, please?</p>

---

## Post #13 by @zariliusra (2023-09-29 09:59 UTC)

<p>Sorry Prof, I just realized that I failed to activate the student license. Where should I run the student license that I’ve got? the “totalseg_set_license -l aca_xxxxxxxxxxx”</p>

---

## Post #14 by @rbumm (2023-09-29 10:06 UTC)

<p>Which version of TotalSegmentator do you use? Please do the version check in the extension</p>

---

## Post #15 by @zariliusra (2023-09-29 10:11 UTC)

<p>I use the 399cde2 version of TotalSegmentator. What should i do?</p>

---

## Post #16 by @rbumm (2023-09-29 10:33 UTC)

<p>Just import the zip file that you have received via the import button of the extension. Putting in a license number will be implemented in the next version of the 3D Slicer extension, using TotalSegmentator v2, which is currently promoted on the TotalSegmentator GitHub page.</p>
<p>If you have just received a license number please contact the developers and explain that you need the weights as a ZIP file as long as we have not yet updated the 3D Slicer extension.</p>

---

## Post #17 by @zariliusra (2023-09-29 10:56 UTC)

<p>I’ve imported the zip file like in the screenshot above, but it still error. <img src="https://emoji.discourse-cdn.com/twitter/pensive.png?v=12" title=":pensive:" class="emoji" alt=":pensive:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/smiling_face_with_tear.png?v=12" title=":smiling_face_with_tear:" class="emoji" alt=":smiling_face_with_tear:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f0807efc0c62aadb56ada42bb21374384638775.png" data-download-href="/uploads/short-url/6I3E8OlRut3SsnSwdtVscktQ6fb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f0807efc0c62aadb56ada42bb21374384638775_2_556x500.png" alt="image" data-base62-sha1="6I3E8OlRut3SsnSwdtVscktQ6fb" width="556" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f0807efc0c62aadb56ada42bb21374384638775_2_556x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f0807efc0c62aadb56ada42bb21374384638775_2_834x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f0807efc0c62aadb56ada42bb21374384638775.png 2x" data-dominant-color="9B9B9B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1037×931 193 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #18 by @rbumm (2023-09-29 11:04 UTC)

<p>Two alternatives:</p>
<p>Locally install Totalsegmentator v2 as described on their GitHub page and run the tool manually without 3D Slicer or wait for the Totalsegmentator extension getting finish so it accepts a license number.</p>

---

## Post #19 by @zariliusra (2023-09-29 11:48 UTC)

<p>Thank you very much Professor. <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=12" title=":blush:" class="emoji" alt=":blush:" loading="lazy" width="20" height="20"></p>

---

## Post #20 by @zariliusra (2023-10-01 16:09 UTC)

<p>Hi Professor. I’ve been able to use TotalSegmentator v2. But how can i use the output in 3D slicer?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bd5bf00b737a6d3f675d71116b754173d0589cc.png" data-download-href="/uploads/short-url/aORL4mPyK13ShsstAPHKsRXbCz2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bd5bf00b737a6d3f675d71116b754173d0589cc.png" alt="image" data-base62-sha1="aORL4mPyK13ShsstAPHKsRXbCz2" width="690" height="443" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">785×505 20.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve try to import it, but then i see nothing on 3D slicer</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28dd4eee8279596f2af63e064277dc3ef78b908b.png" data-download-href="/uploads/short-url/5PvftVD3eaL0ZVRKO3PUSVEp7uj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28dd4eee8279596f2af63e064277dc3ef78b908b_2_690x332.png" alt="image" data-base62-sha1="5PvftVD3eaL0ZVRKO3PUSVEp7uj" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28dd4eee8279596f2af63e064277dc3ef78b908b_2_690x332.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28dd4eee8279596f2af63e064277dc3ef78b908b_2_1035x498.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28dd4eee8279596f2af63e064277dc3ef78b908b_2_1380x664.png 2x" data-dominant-color="C1C1CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1540×741 68.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c7f2e2ea65f8c7726f56a8e4e07f974a74d9f87.png" data-download-href="/uploads/short-url/445QOMJsVgAwoUalTdpgzsfAgKj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c7f2e2ea65f8c7726f56a8e4e07f974a74d9f87_2_690x281.png" alt="image" data-base62-sha1="445QOMJsVgAwoUalTdpgzsfAgKj" width="690" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c7f2e2ea65f8c7726f56a8e4e07f974a74d9f87_2_690x281.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c7f2e2ea65f8c7726f56a8e4e07f974a74d9f87_2_1035x421.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c7f2e2ea65f8c7726f56a8e4e07f974a74d9f87_2_1380x562.png 2x" data-dominant-color="6A6A75"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1868×761 60.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #21 by @rbumm (2023-10-01 16:15 UTC)

<p>You need to load the NIFTI file (shift it over the 3D Slicer windows) and then shift the segmentations over the Slicer window, but  <strong>load them as segmentations</strong></p>

---

## Post #22 by @zariliusra (2023-10-01 16:31 UTC)

<p>but still nothing happen <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/615854be4af8340188b690083e3daf577e9e173a.png" data-download-href="/uploads/short-url/dT9yU8bFAZze19jB8jh3z1coEz0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/615854be4af8340188b690083e3daf577e9e173a_2_690x271.png" alt="image" data-base62-sha1="dT9yU8bFAZze19jB8jh3z1coEz0" width="690" height="271" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/615854be4af8340188b690083e3daf577e9e173a_2_690x271.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/615854be4af8340188b690083e3daf577e9e173a_2_1035x406.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/615854be4af8340188b690083e3daf577e9e173a_2_1380x542.png 2x" data-dominant-color="DADAE3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1736×684 73.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42567c4787a24a5d98ac4e8174ad83680799ae0b.png" data-download-href="/uploads/short-url/9sQO3hQQzKJLv3oCTGRFIWa0F6j.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42567c4787a24a5d98ac4e8174ad83680799ae0b_2_690x284.png" alt="image" data-base62-sha1="9sQO3hQQzKJLv3oCTGRFIWa0F6j" width="690" height="284" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42567c4787a24a5d98ac4e8174ad83680799ae0b_2_690x284.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42567c4787a24a5d98ac4e8174ad83680799ae0b_2_1035x426.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42567c4787a24a5d98ac4e8174ad83680799ae0b_2_1380x568.png 2x" data-dominant-color="6F6F7A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1895×781 57.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fac6d0e3b8e9b49ef499878bd10bd3c41c8b913f.png" data-download-href="/uploads/short-url/zMtkobO7T7seprVID7WJ5KFKSWX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fac6d0e3b8e9b49ef499878bd10bd3c41c8b913f_2_690x253.png" alt="image" data-base62-sha1="zMtkobO7T7seprVID7WJ5KFKSWX" width="690" height="253" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fac6d0e3b8e9b49ef499878bd10bd3c41c8b913f_2_690x253.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fac6d0e3b8e9b49ef499878bd10bd3c41c8b913f_2_1035x379.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fac6d0e3b8e9b49ef499878bd10bd3c41c8b913f_2_1380x506.png 2x" data-dominant-color="70717E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1885×692 56.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please, what should i do?</p>

---

## Post #23 by @rbumm (2023-10-02 12:04 UTC)

<p>Unload all.<br>
Load the ct.nii.gz first as a volume.<br>
Then rename all organ segmentatons to xxx.seg.gz and reload them.<br>
Then create a Folder “Segmentation” in your scene.<br>
Push all segments into that folder.<br>
Open the Segment editor.<br>
Give every segment a different color.</p>

---
