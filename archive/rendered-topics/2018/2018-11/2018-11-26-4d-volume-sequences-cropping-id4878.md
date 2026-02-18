# 4D volume sequences cropping

**Topic ID**: 4878
**Date**: 2018-11-26
**URL**: https://discourse.slicer.org/t/4d-volume-sequences-cropping/4878

---

## Post #1 by @M_pavi (2018-11-26 22:14 UTC)

<p>I have been working on 4D volume sequences (.nrrd format) on 3D slicer. I use segmentation editor to crop some parts where after I crop some parts I wanted to save it as another new volume. But after saving this I couldn’t open it as a 4D volume. It shows as a 3D volume without any 4D supports.</p>

---

## Post #2 by @lassoan (2018-11-27 00:00 UTC)

<aside class="quote no-group" data-username="M_pavi" data-post="1" data-topic="4878">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/54ee81/48.png" class="avatar"> M_pavi:</div>
<blockquote>
<p>I use segmentation editor to crop some parts where after I crop some parts</p>
</blockquote>
</aside>
<p>Segment editor can be used to create and edit segments. How did you use it to crop something? Do you mean you masked out certain region of an image volume?</p>
<aside class="quote no-group" data-username="M_pavi" data-post="1" data-topic="4878">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/54ee81/48.png" class="avatar"> M_pavi:</div>
<blockquote>
<p>I wanted to save it as another new volume</p>
</blockquote>
</aside>
<p>Would you like to mask out a certain region in all frames of a volume sequence (4D volume) and save the result as a volume sequence?</p>

---

## Post #3 by @M_pavi (2018-11-27 00:04 UTC)

<p>Yes, I masked out certain region of volume sequence.I might be wrong. What I need to do eliminate some area from my 4D volume and save the results as  4D volume (volume sequence )</p>

---

## Post #4 by @lassoan (2018-11-27 00:30 UTC)

<p>You need to create a new 4D volume sequence and go through your 4D volume and apply cropping to each frame:</p>
<p>Create a new 4D volume:</p>
<ul>
<li>In Segment Editor module, apply masking to the current frame of your volume (it’ll create a volume such as “CTP-cardio masked”)</li>
<li>Go to “Sequence Browser” module, in Synchronized nodes section, click “+” icon =&gt; this creates a new sequence (while “Create new sequence” is selected on the left) and a new row appears in the table below</li>
<li>In that new row, set the “Proxy node” to the masked volume (e.g., “CTP-cardio masked”) to associate the 3D volume with the 4D sequence, and check “Save changes” checkbox to automatically save modifications (when you mask the volume, the result will be saved in the sequence)</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14715ecc148495f66be9fffbd6e8f0bca8c22bb8.png" data-download-href="/uploads/short-url/2UQrxlHR84sV1T2uHRyK2dr2eFi.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14715ecc148495f66be9fffbd6e8f0bca8c22bb8_2_665x500.png" alt="image" data-base62-sha1="2UQrxlHR84sV1T2uHRyK2dr2eFi" width="665" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14715ecc148495f66be9fffbd6e8f0bca8c22bb8_2_665x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14715ecc148495f66be9fffbd6e8f0bca8c22bb8_2_997x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14715ecc148495f66be9fffbd6e8f0bca8c22bb8.png 2x" data-dominant-color="F5F5F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1151×865 52.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Apply masking to each frame:</p>
<ul>
<li>Go to Segment Editor module</li>
<li>Click on Mask volume effect</li>
<li>Click Apply</li>
<li>Go to next frame by hitting Ctrl + Shift + Right-arrow key</li>
<li>Click Apply</li>
<li>… repeat the last 2 steps until you reach the end of your sequence</li>
</ul>
<p>I know that the last two steps may be tedious (especially if you have hundreds of frames), but it can be automated using Python scripting. Let me know if you need this and I can describe how to do that.</p>

---

## Post #5 by @J.vd.Zee (2022-06-17 09:58 UTC)

<p>Hi!<br>
This problem is still relevant and I wonder if any progress on this topic has been carried out.<br>
I have a live US stream to Slicer via the Plus Server and openIGTlink. However, my stream contains the whole US interface including all not useful aspects as visible in the picture below. The machine learning module is now performing the algorithm on this window instead of the US images alone. Is there any possibility to mask or crop the input signal in a live manner before getting a sequence or giving it to the live Unet algorithm?</p>
<p>Thanks!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4e78377a89c7b3eca1c8cfcb3317471c6f806c1.png" data-download-href="/uploads/short-url/wEYStTjOooTZ5A88AKmYMCvMGPf.png?dl=1" title="US_stream" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4e78377a89c7b3eca1c8cfcb3317471c6f806c1.png" alt="US_stream" data-base62-sha1="wEYStTjOooTZ5A88AKmYMCvMGPf" width="649" height="500" data-dominant-color="0D0D0D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">US_stream</span><span class="informations">685×527 48.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2022-06-17 14:28 UTC)

<p>You can crop 4D volume sequences using <code>Crop volume sequence</code> module. Let us know if you have any questions about how to use it.</p>

---

## Post #7 by @J.vd.Zee (2022-06-21 10:54 UTC)

<p>Thanks for your answer!</p>
<p>Is it also possible to crop the input signal in the <em>PuDeviceSet_Server_MmfVideoCapture.xml</em> instead by just adding a few lines of code? That would be perfect as I am only interested in the<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89905660f40b8854220528eb462fa67c96759dc7.jpeg" data-download-href="/uploads/short-url/jCWEBAMhDaFqRiWWib0uw6kclKL.jpeg?dl=1" title="Cropping_input" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89905660f40b8854220528eb462fa67c96759dc7_2_345x168.jpeg" alt="Cropping_input" data-base62-sha1="jCWEBAMhDaFqRiWWib0uw6kclKL" width="345" height="168" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89905660f40b8854220528eb462fa67c96759dc7_2_345x168.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89905660f40b8854220528eb462fa67c96759dc7_2_517x252.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/89905660f40b8854220528eb462fa67c96759dc7_2_690x336.jpeg 2x" data-dominant-color="444445"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Cropping_input</span><span class="informations">2976×1450 241 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2022-06-21 15:31 UTC)

<p>Yes, you can clip the image to the relevant region by setting <code>ClipRectangleOrigin</code> and <code>ClipRectangleSize</code> parameters in the Plus configuration file - see specification <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/DeviceMicrosoftMediaFoundation.html">here</a>.</p>

---

## Post #9 by @J.vd.Zee (2022-06-22 08:34 UTC)

<p>Thanks for your answer. You really helped me out!<br>
It worked with just adding a line of code <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>A little remark for the specification you sent me.<br>
For two-dimensional input data the third component <em>must</em> be ommitted instead of <em>may</em> be ommitted in my case.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49f97c8399fe94d2721a435a509c05a82d2f4646.png" data-download-href="/uploads/short-url/aypnoVHnQ9XFvQQV38IY7DF8Kqi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49f97c8399fe94d2721a435a509c05a82d2f4646.png" alt="image" data-base62-sha1="aypnoVHnQ9XFvQQV38IY7DF8Kqi" width="690" height="209" data-dominant-color="FBF6FD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1462×444 18.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2022-06-22 13:06 UTC)

<p>Thanks for confirming. I’ve updated the language around “may be” (changed to “may need to be”, as I’m not sure if it “must be” omitted for every devices).</p>

---
