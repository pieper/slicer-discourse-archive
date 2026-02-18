# How to add existing module and do further development

**Topic ID**: 13260
**Date**: 2020-08-31
**URL**: https://discourse.slicer.org/t/how-to-add-existing-module-and-do-further-development/13260

---

## Post #1 by @Yusuke (2020-08-31 18:12 UTC)

<p>Hi,</p>
<p>I would like to try to load NVIDIA AIAA module from my local repo so that I can try it out and make further changes.</p>
<p>I follow the following instruction on this README, <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/blob/master/slicer-plugin/README.md" class="inline-onebox" rel="noopener nofollow ugc">ai-assisted-annotation-client/slicer-plugin/README.md at master · NVIDIA/ai-assisted-annotation-client · GitHub</a></p>
<ul>
<li>git clone <a href="https://github.com/NVIDIA/ai-assisted-annotation-client.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - NVIDIA/ai-assisted-annotation-client: Client side integration example source code and libraries for AI-Assisted Annotation SDK</a></li>
<li>Open 3D Slicer: Go to Edit → Application Settings → Modules → Additional Module Paths
<ol>
<li>Add New Module Path: &lt;FULL_PATH&gt;/slicer-plugin/NvidiaAIAA</li>
<li>Restart</li>
</ol>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bd4d209e87ba37a19ab9f506ce27ab02de992db.png" data-download-href="/uploads/short-url/8xi8sH4hfEOXXlfq8wS4KjulJnZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bd4d209e87ba37a19ab9f506ce27ab02de992db_2_690x475.png" alt="image" data-base62-sha1="8xi8sH4hfEOXXlfq8wS4KjulJnZ" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bd4d209e87ba37a19ab9f506ce27ab02de992db_2_690x475.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bd4d209e87ba37a19ab9f506ce27ab02de992db.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bd4d209e87ba37a19ab9f506ce27ab02de992db.png 2x" data-dominant-color="353434"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">856×590 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I’m not sure what to do next but I thought I was able to see the module under ‘Example’ on the Module list but I cannot see it.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75677da7b20c72a1b7563c5cf2b21dd958d22811.png" alt="image" data-base62-sha1="gKBAIcGHKgQszKidrnAz3pZ3jNf" width="450" height="98"></p>
<p>Could you tell me how I can see the module under Example? or is there anything I’m missing?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-08-31 18:26 UTC)

<p>Segment Editor effects do not show up in the module list. They show up in Segment Editor module instead.</p>

---

## Post #3 by @Yusuke (2020-08-31 19:28 UTC)

<p>Thank you so much! I was able to see the icon in Segment Editor module.</p>

---
