# Draw tool stops working in segmentation editor

**Topic ID**: 14106
**Date**: 2020-10-18
**URL**: https://discourse.slicer.org/t/draw-tool-stops-working-in-segmentation-editor/14106

---

## Post #1 by @Kamyar_Zarkoub (2020-10-18 06:06 UTC)

<p>Operating system:Mac</p>
<p>When I’m trying to draw an aortic segment, the draw and paint tool are what I mainly use. But for some reason, along the way down the scans the draw tool stops working. I can draw the outline just fine, but right clicking to accept the outline doesn’t work. The paint tool is still functional, but sometimes this won’t be working either.</p>
<p>Is there some steps to ensure proper functionality that I’m not aware of? I’m an undergraduate research assistant so I realize this may be a very basic problem but I would appreciate some clarity since this is a consistent issue for me.  <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14657487f14f1fdde36f938936939cf346ae8335.jpeg" data-download-href="/uploads/short-url/2UqUNLd6gXh8tApGbzwNguYxwtT.jpeg?dl=1" title="Screen Shot 2020-10-17 at 9.47.29 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14657487f14f1fdde36f938936939cf346ae8335_2_690x328.jpeg" alt="Screen Shot 2020-10-17 at 9.47.29 PM" data-base62-sha1="2UqUNLd6gXh8tApGbzwNguYxwtT" width="690" height="328" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14657487f14f1fdde36f938936939cf346ae8335_2_690x328.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14657487f14f1fdde36f938936939cf346ae8335_2_1035x492.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14657487f14f1fdde36f938936939cf346ae8335_2_1380x656.jpeg 2x" data-dominant-color="6E6E76"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-10-17 at 9.47.29 PM</span><span class="informations">1920×915 244 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Andinet_Enquobahrie (2020-10-18 16:19 UTC)

<p>Hi <a class="mention" href="/u/kamyar_zarkoub">@Kamyar_Zarkoub</a></p>
<p>Can you please let us know what Slicer version you are using?</p>
<p>Andinet</p>

---

## Post #3 by @Kamyar_Zarkoub (2020-10-18 17:09 UTC)

<p>Hello Andinet ,</p>
<p>My version of slicer is</p>
<p>4.10.2 r28257</p>

---

## Post #4 by @muratmaga (2020-10-18 17:17 UTC)

<p>Please switch to the latest stable and let us know if the issue still persists.</p>

---

## Post #5 by @Kamyar_Zarkoub (2020-10-19 17:04 UTC)

<p>Hello,</p>
<p>The issue is still persisting. I installed the latest version, and the draw tool works fine for a while but around 10 minutes in has stopped working. Right clicking does not fill in the region I have drawn, but the paint feature still works.</p>

---

## Post #6 by @Andinet_Enquobahrie (2020-10-19 17:47 UTC)

<p>Do you get any error messages?</p>
<p>The  <strong>error log</strong>  dialog is accessible from View -&gt;  <strong>Error Log</strong>  or via the Ctrl+0 shortcut.</p>

---

## Post #7 by @Kamyar_Zarkoub (2020-10-19 18:50 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/168a423c6c481da8f9ea799361f13ea49494a47b.png" data-download-href="/uploads/short-url/3doIMBDW2FyQzx1UifRsrV81rsL.png?dl=1" title="Screen Shot 2020-10-19 at 11.49.35 AM.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/168a423c6c481da8f9ea799361f13ea49494a47b_2_473x143.png" alt="Screen Shot 2020-10-19 at 11.49.35 AM.png" data-base62-sha1="3doIMBDW2FyQzx1UifRsrV81rsL" width="473" height="143" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/168a423c6c481da8f9ea799361f13ea49494a47b_2_473x143.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/168a423c6c481da8f9ea799361f13ea49494a47b_2_709x214.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/168a423c6c481da8f9ea799361f13ea49494a47b_2_946x286.png 2x" data-dominant-color="3B3B3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-10-19 at 11.49.35 AM.png</span><span class="informations">2518×760 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/baf1c61ca2be0152705f6bcf7fcc76c969e73f76.png" data-download-href="/uploads/short-url/qFMO4zm26y2hw5PqEqBBJ4T9nrE.png?dl=1" title="Screen Shot 2020-10-19 at 11.50.21 AM.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/baf1c61ca2be0152705f6bcf7fcc76c969e73f76_2_473x146.png" alt="Screen Shot 2020-10-19 at 11.50.21 AM.png" data-base62-sha1="qFMO4zm26y2hw5PqEqBBJ4T9nrE" width="473" height="146" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/baf1c61ca2be0152705f6bcf7fcc76c969e73f76_2_473x146.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/baf1c61ca2be0152705f6bcf7fcc76c969e73f76_2_709x219.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/baf1c61ca2be0152705f6bcf7fcc76c969e73f76_2_946x292.png 2x" data-dominant-color="363636"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-10-19 at 11.50.21 AM.png</span><span class="informations">2520×776 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce441ff99ecf1b6de105d920f586c860fd4e1551.png" data-download-href="/uploads/short-url/tqIjA6iEIyZnqSq1rqPcsRv6eoF.png?dl=1" title="Screen Shot 2020-10-19 at 11.50.03 AM.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce441ff99ecf1b6de105d920f586c860fd4e1551_2_473x140.png" alt="Screen Shot 2020-10-19 at 11.50.03 AM.png" data-base62-sha1="tqIjA6iEIyZnqSq1rqPcsRv6eoF" width="473" height="140" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce441ff99ecf1b6de105d920f586c860fd4e1551_2_473x140.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce441ff99ecf1b6de105d920f586c860fd4e1551_2_709x210.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce441ff99ecf1b6de105d920f586c860fd4e1551_2_946x280.png 2x" data-dominant-color="3A3A3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-10-19 at 11.50.03 AM.png</span><span class="informations">2498×742 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here are some of my most recent errors</p>

---

## Post #8 by @muratmaga (2020-10-19 20:29 UTC)

<p>Can you paste them as text, only a portion is visible in screenshot. There are no errors in these ones, only some info.</p>

---

## Post #9 by @lassoan (2020-10-20 00:23 UTC)

<p><a class="mention" href="/u/kamyar_zarkoub">@Kamyar_Zarkoub</a> Does it fix the issue if you adjust the slice position a bit by moving the mouse in any of the slice viewers while holding down Shift key?</p>

---

## Post #10 by @Kamyar_Zarkoub (2020-10-20 02:16 UTC)

<p><span class="mention">@Andras</span> It has been working for now with the new update - when I did run into the issue a couple times I just closed and re-opened slicer which made things work again. I will try this next time I run into the issue and let you know, thank you!</p>

---
