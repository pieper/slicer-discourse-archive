# How to properly open a saved Landmark registration

**Topic ID**: 5838
**Date**: 2019-02-20
**URL**: https://discourse.slicer.org/t/how-to-properly-open-a-saved-landmark-registration/5838

---

## Post #1 by @mbrammerloh (2019-02-20 04:42 UTC)

<p>Hello,<br>
I am really enjoying 3D slicer for 3D to 2D landmark registration, thanks for the great work.<br>
There is one problem I am facing often: I want to continue working on a saved registration, but when I reopen the scene, all the landmarks are put to the origin. When I open the images first and load the landmarks separately, the same thing happens when opening the landmark registration module. When I just open one set of landmarks, at least they will be displayed correctly in the landmark registration module, but I have to redo the landmarks for the other image (volume). Is there a way to avoid this?<br>
Thanks for any advice!<br>
Cheers,<br>
Malte</p>

---

## Post #2 by @pieper (2019-02-20 14:58 UTC)

<p>Hi <a class="mention" href="/u/mbrammerloh">@mbrammerloh</a> -</p>
<p>It should be working to save/restore the state of the LandmarkRegistration module.  I just tried it with some of the sample data and going to mrb file and back worked as expected.  The module uses a simple naming scheme to recognize the correspondence between volumes and fiducial lists, so maybe if your volumes have unusual names or if you renamed anything it could break.  It will automatically create lists if it doesn’t find an appropriate one, so you want to have your volumes and data loaded before entering the module.</p>
<p>Also note that <a href="https://issues.slicer.org/view.php?id=4634" rel="nofollow noopener">this issue about not being able to select the landmarks</a> is still outstanding but will hopefully be fixed either in VTK itself or in Slicer with the new <a href="https://www.slicer.org/wiki/Documentation/Labs/Improving_Markups" rel="nofollow noopener">markups infrastructure.</a>.</p>

---

## Post #3 by @mbrammerloh (2019-02-21 17:32 UTC)

<p>Hi,<br>
thank you for your advice, I think my “funny” file names were the problem. The landmarks were not recognized and new ones popped up, that makes sense.<br>
Cheers,<br>
Malte<br>
PS: I am mainly working with Slicer 4.8.1 to avoid the landmark selection issue and am looking forward to the fix <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #4 by @mbrammerloh (2019-02-22 16:19 UTC)

<p>Hi again, now I am again facing the same problem. I have not renamed anything and use just numbers and letters in my filenames. But when I open first volume one, then landmarks of volume 1, then volume 2 and landmarks of volume two, then open the landmark registration modlule, the following is the result: I end up with 8 instead of 4 landmarks, number 0 and 4, 1 and 5 and so forth on the same spot. The location is correct in volume 1, but in volume 2 they are placed incorrectly, that is, at the location in absolute space where the landmarks of volume 1 are, which in volume 2 of course is nonsense.</p>
<p>Another strange thing is that when I open the transformed volume in Slicer, it is not displayed as before, but somewhere else. This is really strange, because the original landmark registration in Slicer succeeded and was displayed correctly. Then I saved it, and when loading just the transformed volume, I get something different than before. On top of that: If I use ants to apply the transformation generated with slicer on the volume I want to transform, and use the first image as a reference image, it works fine and the volumes are registered as first seen in Slicer.</p>
<p>Maybe there is some problem with the nifti files I use? Is it possible that somewhere some header information is not used?</p>

---

## Post #5 by @pieper (2019-02-22 20:06 UTC)

<p>Hmm, I’m not seeing this behavior.</p>
<p>I did the following:</p>
<ul>
<li>load two volumes (I used the two brain tumor examples in SampleData)</li>
<li>enter LandmarkRegistration and set them as fixed and moving</li>
<li>turn on affine registration</li>
<li>add/edit some landmarks</li>
<li>save the scene</li>
<li>close the scene</li>
<li>reload the scene</li>
<li>go back to LandmarkRegistration and re-select the volumes</li>
</ul>
<p>After this everything seems to be as expected.  Nifti files shouldn’t make any difference.</p>
<p>Note that the volume named -transformed is underneath the transform node when registering and saving, but if you reload it outside of the scene it won’t have been transformed.</p>

---

## Post #6 by @mbrammerloh (2019-03-05 13:55 UTC)

<p>Ok, I think it was again a problem with naming, after choosing very simple names it got better.<br>
Thank you for the hint on the transform, that really helped me understanding the way Slicer is structured a little more <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=6" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Now I can reopen the scene and in Landmark registration all landmarks are placed correctly. But somehow the _transformed volume is not rendered any more, the display seems to be frozen. Any idea why this is happening?</p>
<p>Thank you for any further advice.</p>
<p>(PS: I think having file names with dashes or underscores are very often used nowadays, so maybe the file name decoder could be adjusted in a way accounting for that. But this is rather an optional idea, not the real problem here.)</p>

---

## Post #7 by @mbrammerloh (2019-03-05 18:56 UTC)

<p>Alright, now it works, opening the same file, nothing changed. Really wondering what causes this behaviour.<br>
Sorry for bothering you with not reproducible bugs…<br>
Cheers,<br>
Malte</p>

---

## Post #8 by @pieper (2019-03-05 22:11 UTC)

<p>Thanks for sticking with it <a class="mention" href="/u/mbrammerloh">@mbrammerloh</a> - I agree with you on the fragile naming convention issue.  I heard from <a class="mention" href="/u/lassoan">@lassoan</a> that he’s reworking the logic to work with the latest changes to fiducials, and maybe when that’s done we can revisit the way the lists are managed.</p>

---

## Post #9 by @wfurquim (2020-03-23 12:07 UTC)

<p>Was the selection of landmarks problem resolved? I still cant do it in version 4.10.2.<br>
It is impacting on performing a ROI registration as I am not able to change radius without selecting the landmark.<br>
Thank you for all the help you can give.</p>

---
