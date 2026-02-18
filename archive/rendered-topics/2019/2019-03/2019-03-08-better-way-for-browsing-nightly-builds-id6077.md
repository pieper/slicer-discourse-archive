# Better way for browsing nightly builds?

**Topic ID**: 6077
**Date**: 2019-03-08
**URL**: https://discourse.slicer.org/t/better-way-for-browsing-nightly-builds/6077

---

## Post #1 by @mcfly3001 (2019-03-08 16:23 UTC)

<p>Hi Slicer-Team,</p>
<p>Your team recently helped me to solve a bug we have found in the OpenIGTLink extension. It was quickly fixed and I was told that there will be an updated available in the next day.<br>
Today I found time to update the extension but I found it quite diffucult to accomplish. So I was just wondering if there would have been a faster way. This is what I did:</p>
<ul>
<li>Went to <a href="https://download.slicer.org/" rel="nofollow noopener">https://download.slicer.org/</a> and clicked on “older releases” to find out that there is a whole “network” folder with lots of releases</li>
<li>From there navigated to “/Public/Slicer/Packages/Extensions/Nightly”</li>
<li>Going into nightly does not even work (guess due to amount of files)</li>
<li>So I sorted the parent folder according to “Modified” and clicked on “show more” hoping to find a new build of SlicerIGT. Finally found one and downloaded the build</li>
</ul>
<p>What I tried before, was to start Slicer and use the extension manager. But when chosing the OpenIGTLink Extension the release data showed 17. January 2019 so I was quite sure that this is not what I need.<br>
Is there some way I could mount this network-drive to my PC? Or any other way how to get nightly builds more easily? In my case I was actually searching for a Slicer 4.10.0 release. So first when trying to install the fixed extension I ended up with Slicer crashing. It took me a while to figure out that my download was for Slicer 4.10.1. So I upgraded to 4.10.1 and it finally runs without problem and the bug-fix included.</p>
<p>Thanks for any tips on how I could upgrade in future with less pain <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #2 by @Sunderlandkyl (2019-03-08 16:28 UTC)

<p>You can update extensions using the drop-down menu in the Extensions Manager:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/780fd023f9912129caa398550547d2b2bfbd2ba0.png" data-download-href="/uploads/short-url/h87aTBkzuQ98AiI0gccGcYRbfgc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/780fd023f9912129caa398550547d2b2bfbd2ba0_2_690x435.png" alt="image" data-base62-sha1="h87aTBkzuQ98AiI0gccGcYRbfgc" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/780fd023f9912129caa398550547d2b2bfbd2ba0_2_690x435.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/780fd023f9912129caa398550547d2b2bfbd2ba0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/780fd023f9912129caa398550547d2b2bfbd2ba0.png 2x" data-dominant-color="D9E2E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">785×495 51.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @mcfly3001 (2019-03-08 16:41 UTC)

<p>Thanks for the hint. I remember that I have also tried this but back then I used Slicer 4.10 and not 4.10.1. But good to know for the future that this is the correct way to upgrade.<br>
I was not sure whether nightly builds are available with the update feature as well.</p>
<p>Thanks! Have a nice weekend!</p>

---
