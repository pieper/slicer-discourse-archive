# LongitudinalPETCT

**Topic ID**: 14709
**Date**: 2020-11-20
**URL**: https://discourse.slicer.org/t/longitudinalpetct/14709

---

## Post #1 by @Jakub_Mitura (2020-11-20 14:15 UTC)

<p>System : Windows 10<br>
Version of 3dSlicer 4.11.20200930<br>
When I try to load PET/CT data I got information that I should install LongitudinalPETCT extension Hovewer when I query  the Extension manager nothing shows up, what can be done?<br>
In Nuclear Medicine Category I have only this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc6f62cc1eab01f4ec7fec0b0e2bd4d39492bf56.png" data-download-href="/uploads/short-url/vs3GzR2YcCzz3xZVwb8viClXwh0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc6f62cc1eab01f4ec7fec0b0e2bd4d39492bf56_2_690x398.png" alt="image" data-base62-sha1="vs3GzR2YcCzz3xZVwb8viClXwh0" width="690" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc6f62cc1eab01f4ec7fec0b0e2bd4d39492bf56_2_690x398.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc6f62cc1eab01f4ec7fec0b0e2bd4d39492bf56.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc6f62cc1eab01f4ec7fec0b0e2bd4d39492bf56.png 2x" data-dominant-color="EDEFF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">742×429 24.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>query also do not help<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aaa4de52b1cd96d3d066a32790cc805687daadc8.png" data-download-href="/uploads/short-url/olAoJKR1c4P5igQVQiimRVLEUWc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aaa4de52b1cd96d3d066a32790cc805687daadc8_2_690x186.png" alt="image" data-base62-sha1="olAoJKR1c4P5igQVQiimRVLEUWc" width="690" height="186" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aaa4de52b1cd96d3d066a32790cc805687daadc8_2_690x186.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aaa4de52b1cd96d3d066a32790cc805687daadc8_2_1035x279.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aaa4de52b1cd96d3d066a32790cc805687daadc8.png 2x" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1078×292 12.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @wintermute (2021-04-28 05:34 UTC)

<p>I wish to know the same. My Mac reported the same issue but I couldn’t find such an extension in the Extension Manager…</p>

---

## Post #3 by @pieper (2021-04-28 19:13 UTC)

<p>That’s a somewhat old extension and the original developer is not around as far as I know.  It would be great if someone wanted to adopt it and bring it up to the current codebase.  It may happen eventually if someone needs this, but volunteers could help move this forward more quickly.</p>

---

## Post #4 by @Jakub_Mitura (2021-05-08 10:14 UTC)

<p>Eventually I would like to help it, I need to first complete some other projects, Yet I have some problems with joining PET and CT data - I am able to visualize them separately but do not see how to display one over the other (clicking the eye icon next to the images do not work); link to the data below</p>
<p><a href="https://wwsi365-my.sharepoint.com/:f:/g/personal/s9956jm_ms_wwsi_edu_pl/Eq4W77ZBPhhPjwLM8SPxXOUB_c9z2vPTJp3TCoILFJqFNQ?e=YgzzPl" class="onebox" target="_blank" rel="noopener nofollow ugc">https://wwsi365-my.sharepoint.com/:f:/g/personal/s9956jm_ms_wwsi_edu_pl/Eq4W77ZBPhhPjwLM8SPxXOUB_c9z2vPTJp3TCoILFJqFNQ?e=YgzzPl</a></p>

---

## Post #5 by @pieper (2021-05-08 15:59 UTC)

<p>That’s a huge download.  If you still need help can you post just pet and ct data?</p>
<p>In any case, you can use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">slice view controller</a> to set the ct in the background and pet in the foreground and then use the Foreground volume opacity slider to adjust the fusion.</p>
<p>HTH</p>

---

## Post #6 by @Jakub_Mitura (2021-05-11 10:12 UTC)

<p>Thank You it works !</p>

---
