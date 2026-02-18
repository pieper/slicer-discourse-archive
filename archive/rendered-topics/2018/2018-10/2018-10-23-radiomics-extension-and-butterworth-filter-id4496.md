# Radiomics Extension and Butterworth Filter

**Topic ID**: 4496
**Date**: 2018-10-23
**URL**: https://discourse.slicer.org/t/radiomics-extension-and-butterworth-filter/4496

---

## Post #1 by @TingtingYu (2018-10-23 09:02 UTC)

<p>Hi,</p>
<p>I just download the latest-nightly-built 3D slicer, it turns out that Radiomics seems to be removed from the Extension Manager. May I know why?</p>
<p>Another question is I tried to use Butterworth filter with an order of 2 and cutoff of 125 to smooth images before feature calculation. However, I  did not find it. Is there a similar one that can replace Butterworth filter?</p>
<p>Regards,<br>
Tingting</p>

---

## Post #2 by @pieper (2018-10-23 19:37 UTC)

<aside class="quote no-group" data-username="TingtingYu" data-post="1" data-topic="4496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/b38774/48.png" class="avatar"> TingtingYu:</div>
<blockquote>
<p>I just download the latest-nightly-built 3D slicer, it turns out that Radiomics seems to be removed from the Extension Manager. May I know why?</p>
</blockquote>
</aside>
<p>We are in the middle of finalizing the Slicer 4.10 release - check again in a day or two and extensions should be back.</p>
<aside class="quote no-group" data-username="TingtingYu" data-post="1" data-topic="4496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/b38774/48.png" class="avatar"> TingtingYu:</div>
<blockquote>
<p>Another question is I tried to use Butterworth filter with an order of 2 and cutoff of 125 to smooth images before feature calculation. However, I did not find it. Is there a similar one that can replace Butterworth filter?</p>
</blockquote>
</aside>
<p>What module do you use for that?</p>

---

## Post #3 by @TingtingYu (2018-10-24 06:42 UTC)

<p>Hi Steve,</p>
<p>Thank you for your quick reply. Actually, I want to investigate the impact of image pre-processing on radiomics features. And the module I tried named “simple filter”.</p>
<p>Regards,<br>
Tingting</p>

---

## Post #4 by @pieper (2018-10-25 02:09 UTC)

<p>Looks like Radiomics is available for the 4.10 stable release now, at least on windows and linux, but not mac until the application signature issue is sorted out.</p>
<p>Regarding Butterworth in Simple Filters I’m not seeing that - probably <a class="mention" href="/u/blowekamp">@blowekamp</a> knows?</p>

---

## Post #5 by @TingtingYu (2018-10-25 04:19 UTC)

<p>Hi Steve,</p>
<p>Thank you. I tried both stable-release and nightly-build version. None of them have “Radiomics” extension.</p>
<p>I did not see Butterworth filter in other modules, either. But when I searched for the Radiomics extension, I happened to see there is an extension named MatlabBridge. Maybe I could use this extension so that I could use the butter(Butterworth filter design) function from matlab.</p>
<p>Regards,<br>
Tingting</p>

---

## Post #6 by @blowekamp (2018-10-25 14:48 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="4496">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Regarding Butterworth in Simple Filters I’m not seeing that - probably <a class="mention" href="/u/blowekamp">@blowekamp</a> knows?</p>
</blockquote>
</aside>
<p>I am not aware of any ready to go ITK filters which do a classic FFT band pass filtering. ITK certainly have the components to do these operations, but  not a single parameterized filter. There is probably a remote module or other community code to do these operations, but I’m not aware of a specific implementation. If such a filter is found it could easily be wrapped for SimpleITK by writing a json file for it.</p>

---

## Post #7 by @fedorov (2018-11-01 18:22 UTC)

<p>3 posts were split to a new topic: <a href="/t/radiomics-extension-build-errors-on-windows/4616">Radiomics extension build errors on Windows</a></p>

---
