# Fiducials Segments alignment in 4.11 using fiducial registration wizard

**Topic ID**: 13816
**Date**: 2020-10-02
**URL**: https://discourse.slicer.org/t/fiducials-segments-alignment-in-4-11-using-fiducial-registration-wizard/13816

---

## Post #1 by @Ada_123 (2020-10-02 12:26 UTC)

<p>Hello,<br>
I am new to 3D slicer so sorry for most likely basic question. I am aligning a head CT with a target created from markups list with a post-procedure CT with the needle. When saving the scene I get the error: fcvs file format only stores control point coordinates and a limited set of display properties. After reopening the scene which was saved the most crucial part of the scene (aligned target with needle) is not displayed. Is it this related to the error? Or is it something else I do wrong? I am enclosing pictures<br>
Thank you very much for your help<br>
Ada<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f41c9b971480d1933e8158911e010dd35c90c214.jpeg" data-download-href="/uploads/short-url/yPvNgGosdSOpgPRRfYWVFkm7pdy.jpeg?dl=1" title="Screenshot (210)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f41c9b971480d1933e8158911e010dd35c90c214_2_690x388.jpeg" alt="Screenshot (210)" data-base62-sha1="yPvNgGosdSOpgPRRfYWVFkm7pdy" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f41c9b971480d1933e8158911e010dd35c90c214_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f41c9b971480d1933e8158911e010dd35c90c214_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f41c9b971480d1933e8158911e010dd35c90c214_2_1380x776.jpeg 2x" data-dominant-color="A8B1C0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (210)</span><span class="informations">1920×1080 567 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6dbdd6f444e6689778876716d0eadb14bfd172e3.png" data-download-href="/uploads/short-url/fEOLYOqI3WjS8G5jDN7ZoJaVNGX.png?dl=1" title="Screenshot (211)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6dbdd6f444e6689778876716d0eadb14bfd172e3_2_690x388.png" alt="Screenshot (211)" data-base62-sha1="fEOLYOqI3WjS8G5jDN7ZoJaVNGX" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6dbdd6f444e6689778876716d0eadb14bfd172e3_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6dbdd6f444e6689778876716d0eadb14bfd172e3_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6dbdd6f444e6689778876716d0eadb14bfd172e3_2_1380x776.png 2x" data-dominant-color="B1B6D3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (211)</span><span class="informations">1920×1080 434 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2020-10-02 13:37 UTC)

<p>Can you describe what procedure you use to do the alignment?  You should use a Transform to one of the datasets to bring them into registration and this would be saved in the scene and reloaded.</p>

---

## Post #3 by @Ada_123 (2020-10-02 13:46 UTC)

<p>Hi Steve, I am using IGT-&gt; fiducial registration wizard-&gt; and then I am creating the new linear segment and then in Data I click on the transform to align models like in this youtube video <a href="https://www.youtube.com/watch?v=TBHr2wizGTM&amp;feature=youtu.be" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=TBHr2wizGTM&amp;feature=youtu.be</a></p>

---

## Post #4 by @pieper (2020-10-02 13:49 UTC)

<p>Hmm, that <em>should</em> create a transform that’s saved with the scene.  I’m not a SlicerIGT user or developer so maybe someone else can comment on how to save the transform.</p>

---

## Post #5 by @muratmaga (2020-10-02 15:15 UTC)

<p>This is a warning, it is not an error. FCSV format is the older format for the Markups and it doesn’t retain all the information (derivative measurements, color settings etc) that the newer JSON format does. The warning is there to remind people about that. But perhaps wording can be a bit better.</p>
<p>I am not entirely sure why you are not getting what you are expecting.</p>

---

## Post #6 by @ungi (2020-10-03 01:36 UTC)

<p>As <a class="mention" href="/u/pieper">@pieper</a> said, the Fiducial Registration Wizard stores the result in the transform node that you specify at “Registration result (From-&gt;To) transform”. That transform node is saved with the scene and should be reloaded. Sometimes what causes an issue is that “Auto update” remains checked. That is the default state of the Update button. In that case the registration is recomputed every time the input fiducial nodes change. If you have an issue saving/loading the fiducial nodes, then the computation may fail. Maybe try to uncheck “Auto update”.</p>

---
