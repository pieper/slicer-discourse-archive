# How to save and read annotation information for 2D images

**Topic ID**: 19843
**Date**: 2021-09-24
**URL**: https://discourse.slicer.org/t/how-to-save-and-read-annotation-information-for-2d-images/19843

---

## Post #1 by @slicer_user (2021-09-24 18:05 UTC)

<p>I currently want to use 3D slicer to annotate 2D images. I have tried to convert the labeled results to binary labelmap and save them in dicom format. In this saving method, I can use python to read the labels correctly in the order of labels. However, there is a problem of overlapping labels, and the labels covered by subsequent labels are incompletely read. Then I tried to save the annotation result in nrrd format, and then read it with python, but the data format obtained by reading nrrd in this way is inconsistent, sometimes the size is (3<em>w</em>h<em>1), sometimes it is (4</em>w* h*1), and I did not find a definite correspondence between the pixel value and the corresponding label. How can I save the label file so that I can read out the labels of each category in turn, and there is no problem of incomplete labeling caused by overlapping labels.</p>

---

## Post #2 by @pieper (2021-09-26 17:29 UTC)

<p>Hi - to better help you, please try your workflow with the latest preview version and report the version number here along with the exact steps you took using public data so that anyone can reproduce.  This sounds like a very solvable issue.</p>

---

## Post #4 by @slicer_user (2021-10-05 07:40 UTC)

<p>Thank you very much for your reply.<br>
The version of the 3D Slicer I use is 4.11.20210226, and the code used to read the nrrd file is</p>
<p>data, _ = nrrd.read(path)<br>
print(data.shape)</p>
<p>I also uploaded the original image and the annotated result. When I marked all the teeth on the original image, the shape obtained by reading the nrrd file using python was (4, 2440, 1280, 1), and when I only marked two teeth, the shape is (2, 2440, 1280, 1). And I can’t know the correspondence between the value on the read data and the label. When I save the annotation result in dicom format, the area of pixel value 1 on the read data represents the area marked by label 1. This correspondence is very clear, but saving as dicom cannot solve the problem of label overlap.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/6170211815131345bcbca49b8244bf52d5d26e8f.jpeg" data-download-href="/uploads/short-url/dTYy86giU5bGUJRih9DTeQ6eZpt.jpeg?dl=1" title="all_teeth" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6170211815131345bcbca49b8244bf52d5d26e8f_2_690x446.jpeg" alt="all_teeth" data-base62-sha1="dTYy86giU5bGUJRih9DTeQ6eZpt" width="690" height="446" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6170211815131345bcbca49b8244bf52d5d26e8f_2_690x446.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6170211815131345bcbca49b8244bf52d5d26e8f_2_1035x669.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6170211815131345bcbca49b8244bf52d5d26e8f_2_1380x892.jpeg 2x" data-dominant-color="71716F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">all_teeth</span><span class="informations">1920×1243 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7fb5afef98eaa58ca22789b843420791b7be0d93.jpeg" data-download-href="/uploads/short-url/idLTUQhbrHiza6iGZc0cvKP3lWr.jpeg?dl=1" title="fig" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7fb5afef98eaa58ca22789b843420791b7be0d93_2_690x361.jpeg" alt="fig" data-base62-sha1="idLTUQhbrHiza6iGZc0cvKP3lWr" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7fb5afef98eaa58ca22789b843420791b7be0d93_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7fb5afef98eaa58ca22789b843420791b7be0d93_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7fb5afef98eaa58ca22789b843420791b7be0d93_2_1380x722.jpeg 2x" data-dominant-color="5A5A5A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fig</span><span class="informations">1920×1007 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef4bfe4225563ffc8988462f687ef843e29c2662.jpeg" data-download-href="/uploads/short-url/y8UVFloxtkpgEAIYGquuB95vcYO.jpeg?dl=1" title="tow_teeth" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef4bfe4225563ffc8988462f687ef843e29c2662_2_690x443.jpeg" alt="tow_teeth" data-base62-sha1="y8UVFloxtkpgEAIYGquuB95vcYO" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef4bfe4225563ffc8988462f687ef843e29c2662_2_690x443.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef4bfe4225563ffc8988462f687ef843e29c2662_2_1035x664.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef4bfe4225563ffc8988462f687ef843e29c2662_2_1380x886.jpeg 2x" data-dominant-color="6F6F6F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">tow_teeth</span><span class="informations">1920×1233 218 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @mikebind (2021-10-05 14:57 UTC)

<p>Non-overlapping labels can be stored in a single labelmap, but overlapping labels mean than there can be multiple labels at a single location, so a single labelmap is no longer sufficient to describe the relationship between labels and pixels (or voxels in the 3D case). When there is overlap between labels, Slicer creates additional layers of labelmap such that overlapping labels are on different layers of the labelmap.  In your two-teeth example, two layers are required because each tooth must be on a separate layer because they overlap.  More overlapping segments will generally require more layers, although not necessarily one per segment because it will typically be possible to put non-overlapping sets of segments on each layer.  I don’t know what algorithm Slicer uses to sort segments into layers, but the result is 4 layers for your multi-tooth segmentation.</p>
<p>If you open the .nrrd file in a text editor (such as Notepad++) you will see that the top of the file is a human readable header.  There will be a large section with information about each segment. You can see there each segment’s name and which layer of the label map it is stored on.</p>
<p>Unfortunately, I don’t know anything about DICOM segmentations or how Slicer exports to there, so I can’t help you with your problem there, but hopefully this is helpful as background information for understanding what is going on.</p>

---

## Post #6 by @slicer_user (2021-10-06 06:56 UTC)

<p>Thank you very much for your explanation. I will use the text editor to check the nrrd file. Have you used 3D Slicer to label overlapping labels before? Is there another way to solve the label overlap problem?</p>

---

## Post #7 by @lassoan (2021-10-06 14:33 UTC)

<p>We developed the <a href="https://pypi.org/project/slicerio/">slicerio</a> Python package to make it very easy to get pixels and metadata of overlapping segments from a .seg.nrrd file. You can use this Python package anywhere, not just in Slicer’s Python environment, by simply pip-installing <code>slicerio</code>.</p>

---

## Post #8 by @mikebind (2021-10-07 00:00 UTC)

<p>Do you need DICOM segmentations?  If not, and you were just viewing that as a way of exporting segmentations outside of Slicer, then <a class="mention" href="/u/lassoan">@lassoan</a>’s solution should work well for you.  If you need the segmentations in DICOM format, then it would be helpful to have more information about what your goal is and what exactly is going wrong on the way to that goal.</p>

---

## Post #9 by @slicer_user (2021-10-07 07:03 UTC)

<p>I just want to convert 3D Slicer’s annotations to images, not necessarily in DICOM format, <a class="mention" href="/u/lassoan">@lassoan</a>  's solution is very effective and has solved my problem. Thank you all for your help.</p>

---
