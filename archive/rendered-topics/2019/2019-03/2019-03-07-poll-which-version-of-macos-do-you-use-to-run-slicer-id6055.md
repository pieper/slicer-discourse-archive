# Poll: Which version of macOS do you use to run Slicer?

**Topic ID**: 6055
**Date**: 2019-03-07
**URL**: https://discourse.slicer.org/t/poll-which-version-of-macos-do-you-use-to-run-slicer/6055

---

## Post #1 by @jcfr (2019-03-07 01:16 UTC)

<p>Hi Slicers,</p>
<p>We are thinking about updating the minimum supported version of macOS (most likely 10.11 “El Capitan”) but before doing so we would like to have a better idea of what you are all using to run Slicer.</p>
<p>Thanks for your input <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=6" title=":smile:" class="emoji" alt=":smile:"></p>
<div class="poll" data-poll-status="open" data-poll-max="6" data-poll-min="1" data-poll-results="always" data-poll-type="multiple" data-poll-name="poll">
<div>
<div class="poll-container">
<ul>
<li data-poll-option-id="cc218b2802f9a6da9993c8bfa76493cf">10.9: “Mavericks” (2013)</li>
<li data-poll-option-id="9c450a2502d3f4e614003ab553a20d68">10.10: “Yosemite” (2014)</li>
<li data-poll-option-id="37c3513a024eef05cd9323c742f1e73c">10.11: “El Capitan” (2015)</li>
<li data-poll-option-id="de794585578151393786ae8f5182bbc6">10.12: “Sierra” (2016)</li>
<li data-poll-option-id="495444796e4cbd5ed808bea2c3dd9e47">10.13: “High Sierra” (2017)</li>
<li data-poll-option-id="4c83c7b2c91685e20f91443c1c069525">10.14: “Mojave” (2018)</li>
</ul>
</div>
<div class="poll-info">
<p>
<span class="info-number">0</span>
<span class="info-label">voters</span>
</p>
</div>
</div>
</div>

---

## Post #2 by @pieper (2019-03-07 13:42 UTC)

<p>Note: I have one machine running 10.13 High Sierra, but it’s got an old GPU so it cannot run either Mojave or Slicer 4.10.x.  This is because Apple isn’t supporting the new OS on the old machines.  To optimize our developer resources I vote that we only support Mojave for Slicer 4.10 and beyond.  People with older machines can use older versions of Slicer.</p>

---

## Post #3 by @Chris_Rorden (2019-03-07 14:07 UTC)

<p>I would vote for targeting 10.13 or later. Our lab also have many Macs that are stranded on 10.13 as 10.14 does not support their Radeon GPUs (even though they are far more powerful than some integrated Intel GPUs that are supported by 10.14). With 10.14 Mojave Apple has deprecated OpenGL. In my experience, an OpenGL application on 10.14 can not set the  “NSRequiresAquaSystemAppearance” to “false”. This means that OpenGL applications can not automatically take advantage of the Mojave Dark Mode. I think this reflects a difference in the Mojave layer manager. A bigger issue is that OpenGL code that works fine on 10.14 when built against the 10.13 SDK fails when built against the 10.14 SDK. This has been well documented, and you can find hacks for this with a web search. Given that OpenGL is deprecated, it is unlikely Apple will fix the OpenGL-specific bugs introduced with the 10.14 SDK. It is unfortunate that one of the worlds most valuable companies does not want to devote the resources for this open standard. Pragmatically, 10.13 appears to be the last version that treats OpenGL as a first class citizen.</p>

---

## Post #4 by @fedorov (2019-03-07 18:58 UTC)

<p>Just as a reference point: here at Partners Healthcare, we have an official policy from IT that only the current macOS and two versions prior are supported.</p>

---

## Post #5 by @jcfr (2019-03-13 04:53 UTC)

<p>Thanks everyone for participating.</p>
<p>Starting with <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28019" rel="nofollow noopener">r28019</a>, setting <code>CMAKE_OSX_DEPLOYMENT_TARGET</code> to at least <code>10.11</code> is mandatory.</p>

---

## Post #6 by @jcfr (2020-05-28 17:32 UTC)

<p>Thanks to <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, following the integration of <a href="https://github.com/Slicer/Slicer/pull/4940">https://github.com/Slicer/Slicer/pull/4940</a>, the minimum deployment target on macOS will be 10.13.</p>
<p>To support this, we will have to update the operating system on our macOS build machine from  Mac OS X 10.11.6 to 10.15.</p>
<h3>What does this mean for Slicer 4.10 extensions on macOS ?</h3>
<p>This means that we will not publish extension update for Slicer 4.10 extension on macOS and only publish extension packages for the Slicer Preview.</p>
<h3>When ?</h3>
<p>We plan on initiating the operating system update tomorrow morning.</p>

---

## Post #7 by @jcfr (2020-05-30 00:52 UTC)

<p>It turns that the operating system can not simply be updated.  In the next few days Kitware sysadmin will proceed to a clean re-installation.</p>
<p>Thanks for your patience</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee9402c343987c6716e1b269c05ac666df9ecaed.jpeg" data-download-href="/uploads/short-url/y2yKtyUQfIdNuDQ0O3kwK1MMUK9.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee9402c343987c6716e1b269c05ac666df9ecaed_2_690x379.jpeg" alt="image" data-base62-sha1="y2yKtyUQfIdNuDQ0O3kwK1MMUK9" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee9402c343987c6716e1b269c05ac666df9ecaed_2_690x379.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee9402c343987c6716e1b269c05ac666df9ecaed.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee9402c343987c6716e1b269c05ac666df9ecaed.jpeg 2x" data-dominant-color="ADABB0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">871×479 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
