# Temporal Calibration

**Topic ID**: 37324
**Date**: 2024-07-11
**URL**: https://discourse.slicer.org/t/temporal-calibration/37324

---

## Post #1 by @J.vd.Zee (2024-07-11 14:18 UTC)

<p>Hello, I defined the temporal calibration, in ms, via the Fcal module. However, if I add the TemporalTimeOffsetSec for the trackerstream, nothing happens. Does someone can assist on this topic?</p>
<p>I have a delay in the image acquisition, and streaming, and want to create a delay on the trackingstream to math these two together.</p>
<p>Thanks in advance!</p>
<p>The code:<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
</p>

---

## Post #2 by @lassoan (2024-07-14 16:55 UTC)

<p>The attribute name is <code>LocalTimeOffsetSec</code>. See an example how it can be used <a href="https://github.com/PlusToolkit/PlusLibData/blob/master/ConfigFiles/PlusDeviceSet_Server_Ultrasonix_L14-5_Ascension3DG_calibrated.xml#L30">here</a>.</p>

---

## Post #3 by @J.vd.Zee (2024-07-15 08:15 UTC)

<p>Thank you for your response. Unfortunately, no increased latency occurs. Although I added the <code>LocalTimeOffsetSec</code> as you mentioned in the code below and expected a latency of 1 second, nothing happens. Could there be a mistake in the code?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fea0b55bb923ad3500f74f9ca0236226e16fac75.png" data-download-href="/uploads/short-url/AkxAOfTHVNP0O5gIWp2ccgAEZPD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fea0b55bb923ad3500f74f9ca0236226e16fac75_2_690x221.png" alt="image" data-base62-sha1="AkxAOfTHVNP0O5gIWp2ccgAEZPD" width="690" height="221" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fea0b55bb923ad3500f74f9ca0236226e16fac75_2_690x221.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fea0b55bb923ad3500f74f9ca0236226e16fac75_2_1035x331.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fea0b55bb923ad3500f74f9ca0236226e16fac75_2_1380x442.png 2x" data-dominant-color="FAF6FC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1576×507 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2024-07-15 11:42 UTC)

<p>The value is not intended for introducing a latency, but to apply a time offset when synchronizing data streams.</p>

---

## Post #5 by @J.vd.Zee (2024-07-15 12:42 UTC)

<p>Sorry, that’s what I mean. I want to create a time offset to synchronize the data streams. However, I do not see any difference by adding this offset.</p>

---

## Post #6 by @lassoan (2024-07-15 13:22 UTC)

<p>Could you please post here your complete device set configuration file?</p>

---

## Post #7 by @J.vd.Zee (2024-07-15 14:52 UTC)

<p>Ofcourse! Hereby my complete code:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/342e54f08b1c2c238fd3c744497fff04bd413268.png" data-download-href="/uploads/short-url/7rC5ORyU5MB8rBlmVbLw96aKyhi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/342e54f08b1c2c238fd3c744497fff04bd413268.png" alt="image" data-base62-sha1="7rC5ORyU5MB8rBlmVbLw96aKyhi" width="554" height="500" data-dominant-color="FCFAFD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1072×966 24.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2024-07-16 03:05 UTC)

<p>The local time offset is used for finding corresponding timestamped items (images, position tracking, other sensor data) in multiple data streams. If you have multiple data streams in a channel then the slowest one will make all the others delayed.</p>
<p>In your device set configuration there is only one data stream in the channel, so there is no data to be synchronized, nothing to wait for, so the local time offset will not delay anything.</p>

---
