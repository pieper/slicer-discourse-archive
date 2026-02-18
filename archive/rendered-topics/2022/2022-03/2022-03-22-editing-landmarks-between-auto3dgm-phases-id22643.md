# Editing landmarks between auto3DGM phases

**Topic ID**: 22643
**Date**: 2022-03-22
**URL**: https://discourse.slicer.org/t/editing-landmarks-between-auto3dgm-phases/22643

---

## Post #1 by @Jasmine_Croghan (2022-03-22 20:03 UTC)

<p>Hi, all another newbie question here. I am using auto3DGM to landmark some turtle hemiskulls, and I do not need landmarks on the inside of the cranium. Currently my solution is to run auto3DGM as is and then go through the generated landmarks and generate a list to remove for the GPA, which is quite tedious to do for 1000+ landmarks in the markup module. I am being helped with my issues on this front elsewhere on this forum, but I have thought of another possibility though I don’t think there is a way to implement it.</p>
<p>I have noticed that there are buttons to separate the phases of auto3DGM, which I assume are there to help organize the computing time. Is there a way to run the module through phase 1, remove landmarks that are not relevant, and then feed those trimmed landmarks into phase 2 ? This would save on computing time and give me much more control over the number of landmarks I am using. There is not currently a way to add landmark files in the module, so I’m assuming it will have to be forced via script.  I’m not sure what is possible.</p>
<p>Thanks for any ideas you may provide,</p>
<p>-Jasmine</p>

---

## Post #2 by @muratmaga (2022-03-22 21:14 UTC)

<p>I am not sure if any of the auto3Dgm developers are tracking the forum. You might get faster response if you contact them directly.</p>
<p>Meanwhile, did you try using the <a href="https://github.com/SlicerMorph/Tutorials/tree/main/MarkupsEditor" rel="noopener nofollow ugc">MarkupEditor</a> in the SlicerMorph to choose your landmarks? At least it might help you with the generating the list to remove for GPA a bit?</p>

---

## Post #3 by @Jasmine_Croghan (2022-03-22 21:16 UTC)

<p>Yes, that is what I have been using the generate the list in the other thread, and why I made the switch to Slicer over R, since the markup editor is so easy to use!</p>
<p>I have contacted them, but was hoping other members may have some experience!</p>
<p>Thank you for all your help!</p>

---
