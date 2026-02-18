# Cut 3d surface from the whole with accuracy

**Topic ID**: 8432
**Date**: 2019-09-14
**URL**: https://discourse.slicer.org/t/cut-3d-surface-from-the-whole-with-accuracy/8432

---

## Post #1 by @Mizo (2019-09-14 23:45 UTC)

<p>hello slicer addicts<br>
i wanna cut the 1st lumbar vertebra out of sacrum with accuracy.<br>
with Scissors i don’t think can do it right since i will cut out by mistake some other parts during the process, is there a way to isolate that vertebra inside segment editor,<br>
what i have in mind using paint &amp; grow from seeds on that vertebra but i don’t know how i approach it right ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1703c27a2d4e6cc4600f0f117fd964fcbbcee79c.jpeg" data-download-href="/uploads/short-url/3hB2hO4QGaI5XqDCm00hQEGXlco.jpeg?dl=1" title="Screen-2019-09-15_01-38-14" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1703c27a2d4e6cc4600f0f117fd964fcbbcee79c_2_522x500.jpeg" alt="Screen-2019-09-15_01-38-14" data-base62-sha1="3hB2hO4QGaI5XqDCm00hQEGXlco" width="522" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1703c27a2d4e6cc4600f0f117fd964fcbbcee79c_2_522x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1703c27a2d4e6cc4600f0f117fd964fcbbcee79c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1703c27a2d4e6cc4600f0f117fd964fcbbcee79c.jpeg 2x" data-dominant-color="89939D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen-2019-09-15_01-38-14</span><span class="informations">774×741 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Amine (2019-09-15 01:30 UTC)

<p>I don’t think you will have good results working directly on the segment, rather use it as a mask to execute grow from seeds as in the method explained here <a href="https://discourse.slicer.org/t/suggestion-quicker-scissor-tool-and-seed-growing-to-split-a-segment-in-two-parts/6006/2" class="inline-onebox">Suggestion: Quicker scissor tool and Seed growing to split a segment in two parts</a><br>
You basically need to</p>
<ol>
<li>draw boundaries outside that segment ( to increase growfromseeds range (let’s call it GFS) )</li>
<li>use masking options editable = inside that segment then draw the seeds in two separate new segments,</li>
<li>then hide the original segment (so GFS does not see it as a seed) and execute GFS with editable = inside the hidden segment (GFS will then use it as a frame).</li>
</ol>

---

## Post #3 by @Mizo (2019-09-15 05:28 UTC)

<p>thx for reply .<br>
but why when i grow from seeds it does not include the whole vertebra that i already painted its seeds on the new layer with editable = inside the the hidden layer segment which has the full threshold pre-defined of the whole bones<br>
why do i need an extra layer editable = everywhere ?</p>
<p>first layer include include the whole bones threshold<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b746a293ba9f3f8723d52054fa4476f722c66b26.jpeg" data-download-href="/uploads/short-url/q9kI91o76yrcoph6n4148vGsRPo.jpeg?dl=1" title="11jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b746a293ba9f3f8723d52054fa4476f722c66b26_2_690x359.jpeg" alt="11jpg" data-base62-sha1="q9kI91o76yrcoph6n4148vGsRPo" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b746a293ba9f3f8723d52054fa4476f722c66b26_2_690x359.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b746a293ba9f3f8723d52054fa4476f722c66b26_2_1035x538.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b746a293ba9f3f8723d52054fa4476f722c66b26_2_1380x718.jpeg 2x" data-dominant-color="818386"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">11jpg</span><span class="informations">1919×1001 380 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> ![12|690x329]</p>
<p>5th vertebra layer that i used to paint the seed over the 5th vertebra, and when i grow its seeds it dones not include the vertebra at all it just gives me what i already painted in the 3d view</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e32302b5254617ab42c69b3ef5290dab2b79693.jpeg" data-download-href="/uploads/short-url/8Sd86OXoKSmtJKbBqZeGak1lh7R.jpeg?dl=1" title="12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e32302b5254617ab42c69b3ef5290dab2b79693_2_690x329.jpeg" alt="12" data-base62-sha1="8Sd86OXoKSmtJKbBqZeGak1lh7R" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e32302b5254617ab42c69b3ef5290dab2b79693_2_690x329.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e32302b5254617ab42c69b3ef5290dab2b79693_2_1035x493.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e32302b5254617ab42c69b3ef5290dab2b79693_2_1380x658.jpeg 2x" data-dominant-color="83848B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">12</span><span class="informations">1920×918 328 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Amine (2019-09-15 09:22 UTC)

<p>Hi, grow from seeds will not have an extent over the whole segment by default, that is why you either paint the limits you want it to have on a dummy segment (outside the segment you want to split, it will not be taken as a seed since its outside the editable area but will still define the boundaries of GFS)<br>
I see you only have one seeding segment, so it is normal for GFS to not work, you need to place seeds in the vertebra AND make another segment with seeds in the sacrum AND a segment outside the main one for limits.<br>
In total these are your 4 segments:</p>
<p>a) original segment (The only hidden one)<br>
b) seeds in the sacrum (painted with editable =  inside original segment) (Visible)<br>
c) seeds in the vertebra (painted with editable = inside original segment) (Visible)<br>
d) seeds at the boundaries (top bottom left right front back) in a segment FULLY  outside the original (you can use editable=everywhere or outside other segments) (Visible)</p>
<p>–&gt; Then launch GFS with editable=inside original segment</p>
<p>Nb: you can bypass making d) by placing the seeds in b) and c) such as they cover the boundaries of the segment if that’s more convenient for you</p>

---

## Post #5 by @Mizo (2019-09-16 01:42 UTC)

<p><a class="mention" href="/u/amine">@Amine</a><br>
thx Amine<br>
successfully i managed to separate parts,<br>
there is one issue<br>
femur is blue paint layer, i keep paint over the femur where some parts of the femur ball overlap with pelvis (green paint), so i keep paint over the femur on its own layer with blue and it does not respond and color stays the same no matter what kind of brush i use i tried them all and in 3d view as well (  the green that belongs to the pelvis does not change over the femur) any idea what causes this issue<br>
note: i use shift to move the cross hair over the part that i want to repaint and i paint  editable area = the hidden layer which is the original segment that has the threshold of the bones<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5201cc5b1dedf26ad1ef3728e35846b467a2f0bf.jpeg" data-download-href="/uploads/short-url/bHt0kxh29Cx65MwNsNYdwqeUtVt.jpeg?dl=1" title="Screen-2019-09-15_01-38-14" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5201cc5b1dedf26ad1ef3728e35846b467a2f0bf_2_690x465.jpeg" alt="Screen-2019-09-15_01-38-14" data-base62-sha1="bHt0kxh29Cx65MwNsNYdwqeUtVt" width="690" height="465" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5201cc5b1dedf26ad1ef3728e35846b467a2f0bf_2_690x465.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/5201cc5b1dedf26ad1ef3728e35846b467a2f0bf_2_1035x697.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/5201cc5b1dedf26ad1ef3728e35846b467a2f0bf.jpeg 2x" data-dominant-color="49545A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen-2019-09-15_01-38-14</span><span class="informations">1350×910 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Amine (2019-09-16 02:11 UTC)

<p>Hi, check your masking options to be editable= inside the original segment and overwrite= visible segments (so that the painted parts get substracted from the excessive segment). Also use a spheric brush instead of a flat one</p>

---

## Post #7 by @Mizo (2019-09-20 06:46 UTC)

<p><a class="mention" href="/u/amine">@Amine</a><br>
was wondering if ct slices thickness 1.mm, compared to 2mm, 3 etc would improve the precision of the images for more accurate &amp; easier segmentation ?<br>
where can i find inside 3dslicer the thickness of the ct slices i’m working with ? i find that the low res ct images very hard to define the gabes between bones like between the vertebras , between femur and pelvis etc<br>
<strong>from cancerimagingarchive</strong><br>
if there is other open ct database could you link me the address , i need the whole body CT scan or complete parts with high res like chest , pelvis to foot , skull etc<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/477bf4d3ca729213dbf1dc3c286cc03749a1f7a8.jpeg" data-download-href="/uploads/short-url/acntutLVYWwbhV4GQ7TIGN30Ry8.jpeg?dl=1" title="Screen-2019-09-20_08-39-03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/477bf4d3ca729213dbf1dc3c286cc03749a1f7a8_2_690x104.jpeg" alt="Screen-2019-09-20_08-39-03" data-base62-sha1="acntutLVYWwbhV4GQ7TIGN30Ry8" width="690" height="104" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/477bf4d3ca729213dbf1dc3c286cc03749a1f7a8_2_690x104.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/477bf4d3ca729213dbf1dc3c286cc03749a1f7a8_2_1035x156.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/477bf4d3ca729213dbf1dc3c286cc03749a1f7a8.jpeg 2x" data-dominant-color="EEEFEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen-2019-09-20_08-39-03</span><span class="informations">1084×164 76.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @Juicy (2019-09-20 08:04 UTC)

<p>Yes smaller slice thickness are better for making 3D volumes from the images as you end up with a higher resolution volume. Most scan protocols for 3D bio-modelling state a slice thickness of around 0.5mm-1.5mm. It starts getting quite difficult to make good models when the slice thickness gets up around 3mm.</p>
<p>When you load a CT DICOM dataset into slicer you can press the ‘metadata’ button next to the ‘Load’ button in the DICOM module window. This will show you the DICOM header information. One of the entries will show you the slice thickness and slice spacing of the CT dataset.</p>
<p>After you load the CT image set it automatically creates a volume from the images. You can go into the volumes module and expand ‘Volume information’. The image spacing entries tell you the dimensions of the voxels which make up your volume. If you have loaded axial images then the first two entries will be the size of the image pixels and the third entry will be the spacing between the images (just don’t change these values or it will distort your volume).</p>
<p><a href="https://discourse.slicer.org/t/fetal-lung-volume-calculation/578/5">Here</a> are some good instructions to get the most out of low resolution (thick slice) scans.</p>

---

## Post #10 by @Mizo (2019-09-20 09:31 UTC)

<p><a class="mention" href="/u/amine">@Amine</a><br>
followd your solution to paint outside the boundary<br>
i get error msg because of the painted area outside the boundary of the area of interest</p>
<p>i want to make a 3d volume out of the pelvic area sacrum not included,<br>
1-1st layer bone with full bone threshold to include bones only _ made it hidden<br>
2- sec layer (pelvis ) Visible, so i painted over the pelvis bone inside its layer , editable inside= bone<br>
3- 3rd layer(outside boundary) visible, i painted outside the pelvis area as a boundary outside the pelvis for the area of bones that i want to include to a separate layer<br>
what i was expecting is to get each layer separated as a 3d volume<br>
do i need to create a layer and paint on the air or over soft tissue which outside the all bones ?<br>
execute initialize grow from seeds i get error msg<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd575e13fb67224728ebfd267d8ec0dee07c5a9b.jpeg" data-download-href="/uploads/short-url/tix43w62g4uHFtZnaZWNoF5V56H.jpeg?dl=1" title="Screen-2019-09-20_08-39-03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd575e13fb67224728ebfd267d8ec0dee07c5a9b_2_690x330.jpeg" alt="Screen-2019-09-20_08-39-03" data-base62-sha1="tix43w62g4uHFtZnaZWNoF5V56H" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd575e13fb67224728ebfd267d8ec0dee07c5a9b_2_690x330.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd575e13fb67224728ebfd267d8ec0dee07c5a9b_2_1035x495.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd575e13fb67224728ebfd267d8ec0dee07c5a9b_2_1380x660.jpeg 2x" data-dominant-color="4E4F54"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen-2019-09-20_08-39-03</span><span class="informations">1917×918 465 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>4th layer soft tissue  editable =everywhere _ visable<br>
painting outside the bones over the soft tissue as a boundary for the whole volume still giving me the same error<br>
i get different result if i press initialize grow from seeds if i have the editable area inside a different layer than bone in masking  which i see is irrelevant to get a different result<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/897d9c701f5f30f328de7554bb946e6e7c842743.jpeg" data-download-href="/uploads/short-url/jCix6y2RcKecJp26irRmF3FGfRh.jpeg?dl=1" title="Screen-2019-09-20_08-39-03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/897d9c701f5f30f328de7554bb946e6e7c842743_2_690x328.jpeg" alt="Screen-2019-09-20_08-39-03" data-base62-sha1="jCix6y2RcKecJp26irRmF3FGfRh" width="690" height="328" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/897d9c701f5f30f328de7554bb946e6e7c842743_2_690x328.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/897d9c701f5f30f328de7554bb946e6e7c842743_2_1035x492.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/897d9c701f5f30f328de7554bb946e6e7c842743_2_1380x656.jpeg 2x" data-dominant-color="535557"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen-2019-09-20_08-39-03</span><span class="informations">1918×913 476 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @Amine (2019-09-20 13:14 UTC)

<p>Your segments are correct, just a note for the 4th with boundaries it doesent have to be soft tissue, just a point in each direction is enough as long as its completely outside the original segment.</p>
<p>The error that is raised however, has nothing to do with your segmentation technique as far as i can guess, someone else could provide a proper explanation.</p>

---

## Post #12 by @Mizo (2019-09-20 14:33 UTC)

<p><a class="mention" href="/u/amine">@Amine</a><br>
let me explain what im trying to do, first method worked ok<br>
now i have skeleton and i only want segmentation of its spine<br>
the steps i follow<br>
0- made a layer with the whole bones threshold<br>
1- i painted seeds over the whole spine on a new layer editable = the original<br>
2- i painted 4 dot’s up right down left outside the original threshold  editable = everywhere<br>
so what i expect when i use grow from seeds it will show me a 3d volume of the spine only over which i painted the seeds. because it is impossible to paint the whole spine with accuracy if no growing from seeds is available<br>
Note :  before i press initialize of growing seeds editable=all segments - overwrite = all segments<br>
is it necessary to paint seeds on everything else except the spine in a different layer beside the step 2?</p>
<p>i find the segmentation options (layers - editable area - overwrite ) are so confusing , and sometimes i find it not follow the logic: would be better if overwrite go beside the layer name or above the layers menu since it has nothing to do with masking</p>

---

## Post #13 by @Amine (2019-09-20 14:43 UTC)

<p>The method i described is for separing a segment into two with help of grow from seeds, so yes you need to define both seeds for it to work (and before initialize you have to chose edit=inside the original not everywhere)</p>

---

## Post #14 by @Mizo (2019-09-20 14:59 UTC)

<p>yes the problem was from edit=all segments , it should be editable =inside the original<br>
i find it strange why the selected layer in editable area which involves the masking has anything to do with  initialize to growing from seeds <img src="https://emoji.discourse-cdn.com/twitter/cold_sweat.png?v=9" title=":cold_sweat:" class="emoji" alt=":cold_sweat:"></p>

---

## Post #15 by @Amine (2019-09-20 15:17 UTC)

<p>It does exactly that, masking, prevents the effect from running outside that segment you defined, while not being considered a seed since it’s hidden</p>

---

## Post #16 by @pieper (2019-09-21 17:09 UTC)

<p>Hi - the error message in dialog in the screen shot above says “bad allocation” which means your computer doesn’t have enough memory to perform these operations.  So you could either crop the volume first, but maybe the most generally useful thing would be to get more memory or use a bigger computer.  Otherwise it sounds like you are on the right track.</p>
<p>Hope that helps,<br>
Steve</p>

---

## Post #17 by @Mizo (2019-09-24 11:19 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a><br>
yep it was a low memory problem thx<br>
solution was to close all other opened programs to free some memory<br>
and restart slicer without changing anything inside the scene<br>
and re initializing the grow from seeds and it works this time</p>

---

## Post #18 by @lassoan (2019-09-24 12:51 UTC)

<p>Note that instead of closing other applications, you can increase the virtual memory size in your computer (on Windows, edit virtual memory size in system settings; on Mac, ensure you have many gigabytes of free disk space).</p>

---
