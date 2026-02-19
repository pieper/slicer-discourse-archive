---
topic_id: 23933
title: "Groups Instructions Pdf Is Not Inconsistent With The Slicers"
date: 2022-06-19
url: https://discourse.slicer.org/t/23933
---

# Groups’instructions PDF is not inconsistent with the slicersalt’s option bar

**Topic ID**: 23933
**Date**: 2022-06-19
**URL**: https://discourse.slicer.org/t/groups-instructions-pdf-is-not-inconsistent-with-the-slicersalt-s-option-bar/23933

---

## Post #1 by @lili-yu22 (2022-06-19 02:38 UTC)

<p>according the Groups instruction，first run rigid alignment，but on the Slicer salt"input model directory”shows as picture 1，requiring time-regressed shapes.however the instruction（ picture2）show "input model directory”choose the SPHARM.vtk model，which  one is correct? thanks<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f78e4e137f1456d7e5c0759f591ac8426e0c4f7.png" data-download-href="/uploads/short-url/fU80Q5Rz8Kt0VfaqrNvzYBHWRP9.png?dl=1" title="mmexport1655605716724" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f78e4e137f1456d7e5c0759f591ac8426e0c4f7.png" alt="mmexport1655605716724" data-base62-sha1="fU80Q5Rz8Kt0VfaqrNvzYBHWRP9" width="586" height="500" data-dominant-color="BACDDC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mmexport1655605716724</span><span class="informations">605×516 42.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17275207f87712fb49c4a72fddcb838fafaccac9.png" alt="mmexport1655606225653" data-base62-sha1="3iPdYFSRSOybJzLvIHjlH48AjTb" width="547" height="413"></p>

---

## Post #2 by @lili-yu22 (2022-06-20 04:02 UTC)

<p>can anyone help me?thank you very much</p>

---

## Post #3 by @mau_igna_06 (2022-06-20 05:44 UTC)

<p>I think the first is for non-linear regisrration and the second one for rigif registration</p>
<p>Others wirh more experience in Salt would be able to help more</p>

---

## Post #4 by @lili-yu22 (2022-06-20 06:39 UTC)

<p>thank you for your prompt reply，the instruction can’t help me. if i use the SPHARM.vtk model in the“input model Directory”when i run rigid alignment it failed <img src="https://emoji.discourse-cdn.com/twitter/cry.png?v=12" title=":cry:" class="emoji" alt=":cry:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @mau_igna_06 (2022-06-20 07:13 UTC)

<p>Maybe <a class="mention" href="/u/connor-bowley">@Connor-Bowley</a> can help?</p>

---

## Post #6 by @Connor-Bowley (2022-06-21 12:34 UTC)

<p><a class="mention" href="/u/jared_vicory">@Jared_Vicory</a> do you have any insight on this?</p>

---

## Post #7 by @Jared_Vicory (2022-06-21 15:08 UTC)

<p><a class="mention" href="/u/lili-yu22">@lili-yu22</a>: The information in the tutorial slides is correct: the Input Models Directory should be a directory with SPHARM vtk files.</p>
<p>It looks like the tooltips in the module are wrong and should be fixed. We should also add some sample data for this module so users can see what the folder structure should be.</p>

---

## Post #8 by @lili-yu22 (2022-06-21 23:28 UTC)

<p>thank you for your reply. I have other questions to consult you.</p>
<ol>
<li>When i use the orther module "Rigidalignment "（picture1)，the first option bar shows the tip"template sphere model”,but I don’t know how to import the data,because there is not any button.<br>
2.the module "Rigidalignment "is not the same function with “SPHARM PDM Correspondence Improvement ”?<br>
thank you very much.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9fcfce5d220decbbdf2e4ee286d7e82b0d7322f.png" data-download-href="/uploads/short-url/v6pDnpVkdv2tyt3YxJpexzBs2IL.png?dl=1" title="mmexport1655854017081" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9fcfce5d220decbbdf2e4ee286d7e82b0d7322f_2_455x500.png" alt="mmexport1655854017081" data-base62-sha1="v6pDnpVkdv2tyt3YxJpexzBs2IL" width="455" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9fcfce5d220decbbdf2e4ee286d7e82b0d7322f_2_455x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9fcfce5d220decbbdf2e4ee286d7e82b0d7322f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9fcfce5d220decbbdf2e4ee286d7e82b0d7322f.png 2x" data-dominant-color="B9D0DE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mmexport1655854017081</span><span class="informations">501×550 36.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>

---

## Post #9 by @lili-yu22 (2022-06-24 23:56 UTC)

<p>I’m very confused <img src="https://emoji.discourse-cdn.com/twitter/face_exhaling.png?v=12" title=":face_exhaling:" class="emoji" alt=":face_exhaling:" loading="lazy" width="20" height="20"><br>
I tried many times on the Rigidalignment module，the python interactor always show can’t find rigidalignmentmeta data，i tried unstall the extension “SPHARM”，used another way to install（first download the package，install from the file）but the “module finder” still show RigidalignmentModule module is not loaded<br>
please help me</p>

---

## Post #10 by @lili-yu22 (2022-06-26 09:55 UTC)

<p>can the module contributors <span class="mention">@Ilwoo</span> Lyu give me help？sincere thanks</p>

---

## Post #11 by @bpaniagua (2022-06-26 10:59 UTC)

<p>Hi! Sorry for the delay in replying.</p>
<p>The tool tips are wrong, and they are being updated. We will push a change very soon cc. <a class="mention" href="/u/jared_vicory">@Jared_Vicory</a></p>
<p>Thanks for reporting the problem.</p>

---

## Post #12 by @lili-yu22 (2022-06-26 11:06 UTC)

<p>thank you very much for your reply，I’m looking forward to it</p>

---
