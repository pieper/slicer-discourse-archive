---
topic_id: 27298
title: "Add A User Warning Prompt When Nifti Imported As A Segment I"
date: 2023-01-17
url: https://discourse.slicer.org/t/27298
---

# Add a user warning prompt when NIfTI imported as a segment is not a binary mask

**Topic ID**: 27298
**Date**: 2023-01-17
**URL**: https://discourse.slicer.org/t/add-a-user-warning-prompt-when-nifti-imported-as-a-segment-is-not-a-binary-mask/27298

---

## Post #1 by @mikbuch (2023-01-17 13:34 UTC)

<p>Hi, I struggled a bit with importing NIfTI images as a segment (“Segmentation”) to the Slicer.</p>
<p>It took ma a while to realize that the image I was trying to import was not a binary mask (0s and 1s), but a probability map (values from 0 to 1).</p>
<p>When I tried to import a non-binary NIfTI image as a segment, I got the following results:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83431281a0dacf98449c243fcb04c813bff5fc85.png" data-download-href="/uploads/short-url/iJcfwl2jcg5LqpiAIQj6QoPounb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83431281a0dacf98449c243fcb04c813bff5fc85_2_663x500.png" alt="image" data-base62-sha1="iJcfwl2jcg5LqpiAIQj6QoPounb" width="663" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83431281a0dacf98449c243fcb04c813bff5fc85_2_663x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83431281a0dacf98449c243fcb04c813bff5fc85_2_994x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83431281a0dacf98449c243fcb04c813bff5fc85.png 2x" data-dominant-color="E9EDF3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1220×920 46.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b43f4c2433bddb5b5229fdea05aa96bae2513c1.png" data-download-href="/uploads/short-url/fiUGryq03HWHcSbDuKZ0gXkeAbn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b43f4c2433bddb5b5229fdea05aa96bae2513c1_2_628x500.png" alt="image" data-base62-sha1="fiUGryq03HWHcSbDuKZ0gXkeAbn" width="628" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b43f4c2433bddb5b5229fdea05aa96bae2513c1_2_628x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b43f4c2433bddb5b5229fdea05aa96bae2513c1_2_942x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b43f4c2433bddb5b5229fdea05aa96bae2513c1.png 2x" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1214×966 74.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(i.e., I couldn’t see the segment), and I got no information whatsoever may be not right with my image.</p>
<p>For the comparison, the Slicer view after uploading binarized NIfTI as a “Segmentation” – everything worked:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65c3c0c427ee426e8a00862fd09123d939e77dc2.png" data-download-href="/uploads/short-url/ewfCEefhJTI2gRQoWgpJzHawlAS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65c3c0c427ee426e8a00862fd09123d939e77dc2_2_690x409.png" alt="image" data-base62-sha1="ewfCEefhJTI2gRQoWgpJzHawlAS" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65c3c0c427ee426e8a00862fd09123d939e77dc2_2_690x409.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65c3c0c427ee426e8a00862fd09123d939e77dc2_2_1035x613.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65c3c0c427ee426e8a00862fd09123d939e77dc2_2_1380x818.png 2x" data-dominant-color="929399"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2574×1526 274 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I think it is a good idea to add a prompt/a warning saying:</p>
<blockquote>
<p>“Warning: The image you are trying to load as a segment has to be a binary map (i.e., it can contain only the values 0 and 1).”</p>
</blockquote>
<p>What is your opinion on this subject?</p>
<p>Similar posts:</p>
<ul>
<li>
<p><a href="/t/how-to-show-the-segmentation-in-segment-editor-which-is-loaded-from-a-nii-gz-file-generated-by-other-program/13096">How to show the segmentation in segment editor which is loaded from a nii.gz file generated by other program?</a></p>
</li>
<li>
<p><a href="/t/importing-segmented-mr-image-in-nifti-format-to-3d/11021">Importing segmented MR image in NIfTI format to 3D</a></p>
</li>
</ul>

---
