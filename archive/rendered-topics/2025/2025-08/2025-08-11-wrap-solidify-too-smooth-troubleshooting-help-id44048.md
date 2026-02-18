# Wrap Solidify Too Smooth - Troubleshooting help

**Topic ID**: 44048
**Date**: 2025-08-11
**URL**: https://discourse.slicer.org/t/wrap-solidify-too-smooth-troubleshooting-help/44048

---

## Post #1 by @PitaChib (2025-08-11 17:35 UTC)

<p>I work with extracting endocasts from skull ct scans. I have a protocol I follow that basically use wrap solidify with split cavities at 1mm. I pretty much do this every time with slight fluctuation with the split cavity adjustment. See pic 1 for my typical endocast:</p>
<p>you can see the lobes, and even some nerve tracks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6078b1b8cd87d9eb74aab1ffa426a8962298965.jpeg" data-download-href="/uploads/short-url/pYj3NtANV4v4YgqRy3tQaJXBsTX.jpeg?dl=1" title="截圖 2025-08-11 下午12.19.12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6078b1b8cd87d9eb74aab1ffa426a8962298965_2_382x500.jpeg" alt="截圖 2025-08-11 下午12.19.12" data-base62-sha1="pYj3NtANV4v4YgqRy3tQaJXBsTX" width="382" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6078b1b8cd87d9eb74aab1ffa426a8962298965_2_382x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6078b1b8cd87d9eb74aab1ffa426a8962298965_2_573x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6078b1b8cd87d9eb74aab1ffa426a8962298965_2_764x1000.jpeg 2x" data-dominant-color="5D5E5F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截圖 2025-08-11 下午12.19.12</span><span class="informations">1070×1398 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Today when I was working with this skull, and they are from the same batch of scan with the one above (everything remains the same, machine of scan is the same, same species, about same dimensions, etc.)</p>
<p>after 2 separate trials, I get this instead:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88de47c43320e84e6042a181e7bc550e574cb747.png" data-download-href="/uploads/short-url/jwNavcDd5qARyQXyXUFGeQIPAeH.png?dl=1" title="Screenshot 2025-08-11 121855" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88de47c43320e84e6042a181e7bc550e574cb747_2_690x387.png" alt="Screenshot 2025-08-11 121855" data-base62-sha1="jwNavcDd5qARyQXyXUFGeQIPAeH" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88de47c43320e84e6042a181e7bc550e574cb747_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88de47c43320e84e6042a181e7bc550e574cb747_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88de47c43320e84e6042a181e7bc550e574cb747_2_1380x774.png 2x" data-dominant-color="5E5E62"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-08-11 121855</span><span class="informations">1919×1079 391 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Things that I’ve checked:</p>
<ul>
<li>voxel size and dimensions, the measurement is roughly similar with my other scans</li>
<li>surface smoothing is turned off, as I usually do in all my endocasts</li>
<li>I tried a couple times with no split cavities, with splitting it smaller 0.1mm and up to 2mm, all are either overflowing and with little detail or too small.</li>
<li>I also tried to grow the skull by 0.1mm and then try to wrap solidify, then try to grow the endocast back. Still little detail captured.</li>
</ul>
<p>on top of this, the skull looks totally fine in details:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9257ab1261e48855ac0983cfa7897c7a69d19b69.png" data-download-href="/uploads/short-url/kSBxq5743LI4DcrhLhff6kAS15v.png?dl=1" title="Screenshot 2025-08-11 123432" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9257ab1261e48855ac0983cfa7897c7a69d19b69_2_660x500.png" alt="Screenshot 2025-08-11 123432" data-base62-sha1="kSBxq5743LI4DcrhLhff6kAS15v" width="660" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9257ab1261e48855ac0983cfa7897c7a69d19b69_2_660x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9257ab1261e48855ac0983cfa7897c7a69d19b69_2_990x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9257ab1261e48855ac0983cfa7897c7a69d19b69.png 2x" data-dominant-color="3A3C2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-08-11 123432</span><span class="informations">1307×990 238 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m just here to look for some advice and ways I can trouble shoot this.</p>
<p>Appreciate very much!</p>

---

## Post #2 by @muratmaga (2025-08-11 18:05 UTC)

<p>What is the exact voxel size reported in this scan versus the ones that worked well? It looks like there is too much smoothing at some point in the process. So you should try to adjust the kernel sizes based on the voxel resolution (not some preset value)</p>

---

## Post #3 by @PitaChib (2025-08-11 20:24 UTC)

<p>thanks for the suggestion, see below for the specs:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96db173b21fad44afb670a9ae94d2824a50d0c69.jpeg" data-download-href="/uploads/short-url/lwx1g8esa4RQl0WU02IZBmx2Awp.jpeg?dl=1" title="截圖 2025-08-11 下午3.17.17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96db173b21fad44afb670a9ae94d2824a50d0c69_2_690x339.jpeg" alt="截圖 2025-08-11 下午3.17.17" data-base62-sha1="lwx1g8esa4RQl0WU02IZBmx2Awp" width="690" height="339" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96db173b21fad44afb670a9ae94d2824a50d0c69_2_690x339.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96db173b21fad44afb670a9ae94d2824a50d0c69_2_1035x508.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96db173b21fad44afb670a9ae94d2824a50d0c69_2_1380x678.jpeg 2x" data-dominant-color="B8BECE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截圖 2025-08-11 下午3.17.17</span><span class="informations">1920×945 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and here is the one that’s smoothed:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae8cc1d8f0fa67ad7659dd79d5fdaadc6fb8482f.png" data-download-href="/uploads/short-url/oU8ElGJRS8B717vy8l1QSgnWuvl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae8cc1d8f0fa67ad7659dd79d5fdaadc6fb8482f_2_690x290.png" alt="image" data-base62-sha1="oU8ElGJRS8B717vy8l1QSgnWuvl" width="690" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae8cc1d8f0fa67ad7659dd79d5fdaadc6fb8482f_2_690x290.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae8cc1d8f0fa67ad7659dd79d5fdaadc6fb8482f_2_1035x435.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/ae8cc1d8f0fa67ad7659dd79d5fdaadc6fb8482f_2_1380x580.png 2x" data-dominant-color="979591"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1893×796 307 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Although I did realize the better ones are done via version 5.8.0 and the smooth version is done on another computer that has 5.8.1. Is that enough to make any difference?</p>
<p>Thanks so much.</p>

---
