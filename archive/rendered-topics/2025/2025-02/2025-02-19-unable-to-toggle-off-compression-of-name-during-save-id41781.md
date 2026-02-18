# Unable to toggle off compression of name during save

**Topic ID**: 41781
**Date**: 2025-02-19
**URL**: https://discourse.slicer.org/t/unable-to-toggle-off-compression-of-name-during-save/41781

---

## Post #1 by @Nastia_Kfir (2025-02-19 21:20 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/387da082a994ccf3103da7c1265c0e1838251e8d.png" data-download-href="/uploads/short-url/83JTms6SckfPocgcnR7ZGPHAXyR.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387da082a994ccf3103da7c1265c0e1838251e8d_2_690x106.png" alt="image" data-base62-sha1="83JTms6SckfPocgcnR7ZGPHAXyR" width="690" height="106" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387da082a994ccf3103da7c1265c0e1838251e8d_2_690x106.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387da082a994ccf3103da7c1265c0e1838251e8d_2_1035x159.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387da082a994ccf3103da7c1265c0e1838251e8d_2_1380x212.png 2x" data-dominant-color="2B2B2B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1779×274 49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi, I’m working in version 5.8.0<br>
working with .nrrd files and creating segments.<br>
when saving the data, the nrrd name appears compressed, but i need it to present the full name of the file.<br>
toggling off the compress option changes nothing, not for current save and not for future saves, and i couldn’t find anything relevant to saving data in the settings.</p>
<p>in older version i didn’t encounter the compression issue, it just presented the full name of the nrrd file.</p>
<p>how can i revert the compression of the nrrd file name?</p>

---

## Post #2 by @muratmaga (2025-02-19 21:41 UTC)

<p><a class="mention" href="/u/nastia_kfir">@Nastia_Kfir</a> compression in this context compressing the context of the volume to save disk space. That option has no bearing on your issue, which is truncation of long filenames.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I am also not happy about this filename truncation for long file names. We do not use scenes to manage our data, but filenames as stored in the filesystem (since we have many workflows outside of the Slicer as well).</p>
<p>I am not sure how long the filename is to be for truncation to be triggered, but there are few times I have encountered with our datasets.</p>
<p>Can this be turned off?</p>

---
