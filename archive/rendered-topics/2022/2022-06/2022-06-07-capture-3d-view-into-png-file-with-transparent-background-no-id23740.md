# Capture 3D view into PNG file with transparent background not working as expected

**Topic ID**: 23740
**Date**: 2022-06-07
**URL**: https://discourse.slicer.org/t/capture-3d-view-into-png-file-with-transparent-background-not-working-as-expected/23740

---

## Post #1 by @aliabidi (2022-06-07 00:18 UTC)

<p>I have a 3D image which I want to take a screenshot of, I do not want to have the background or the axes (I, R, S) or purple lines when I save the image. The current state looks as follows:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c8dd06f606648907770515265df1c29b4db11ec.jpeg" data-download-href="/uploads/short-url/1N3z2uZPxKEEaHGb0RxT9xHBAtK.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c8dd06f606648907770515265df1c29b4db11ec_2_689x413.jpeg" alt="image" data-base62-sha1="1N3z2uZPxKEEaHGb0RxT9xHBAtK" width="689" height="413" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c8dd06f606648907770515265df1c29b4db11ec_2_689x413.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c8dd06f606648907770515265df1c29b4db11ec_2_1033x619.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c8dd06f606648907770515265df1c29b4db11ec_2_1378x826.jpeg 2x" data-dominant-color="D6D6E3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2412×1444 341 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I have run the ‘<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#capture-3d-view-into-png-file-with-transparent-background" rel="noopener nofollow ugc">Capture 3D view into PNG file with transparent background</a>’ script by saving it in a Python file and then running <code>exec(open('./Users/me/Downloads/save.py').read())</code> in the Python console in Slicer (see screenshot).</p>
<p>However, the screenshot which is output does not have the current 3D view, and does not have a 3D background or hidden axes:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5522b8d091e6d813c0b11a61da52066643cb70be.jpeg" data-download-href="/uploads/short-url/c98Yxe0pXMvAPQJEbonHpKBZtwy.jpeg?dl=1" title="screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5522b8d091e6d813c0b11a61da52066643cb70be_2_690x494.jpeg" alt="screenshot" data-base62-sha1="c98Yxe0pXMvAPQJEbonHpKBZtwy" width="690" height="494" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5522b8d091e6d813c0b11a61da52066643cb70be_2_690x494.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5522b8d091e6d813c0b11a61da52066643cb70be_2_1035x741.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5522b8d091e6d813c0b11a61da52066643cb70be.jpeg 2x" data-dominant-color="7E839F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot</span><span class="informations">1158×830 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What can I do about this?</p>

---

## Post #2 by @mau_igna_06 (2022-06-07 09:13 UTC)

<p>You need to ise the orthogonal prpjection</p>

---

## Post #3 by @aliabidi (2022-06-07 12:14 UTC)

<p>Sorry I’m a bit new to this software- what does this mean?</p>

---

## Post #4 by @mau_igna_06 (2022-06-07 12:23 UTC)

<p>Click on the pin icon on the upper left view and click where there is a cubb<br>
Let me know if that helps</p>

---

## Post #5 by @pieper (2022-06-07 12:54 UTC)

<p>You can configure the view with something like this:</p>
<pre><code class="lang-auto">    slicer.app.layoutManager().threeDWidget(0).viewLogic().GetViewNode().SetBackgroundColor((0,0,0))
    slicer.app.layoutManager().threeDWidget(0).viewLogic().GetViewNode().SetBackgroundColor2((0,0,0))
    slicer.app.layoutManager().threeDWidget(0).viewLogic().GetViewNode().SetBoxVisible(False)
    slicer.app.layoutManager().threeDWidget(0).viewLogic().GetViewNode().SetAxisLabelsVisible(False)
</code></pre>

---
