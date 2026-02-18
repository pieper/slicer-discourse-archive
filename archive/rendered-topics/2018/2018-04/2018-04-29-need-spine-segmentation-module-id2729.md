# Need spine segmentation module

**Topic ID**: 2729
**Date**: 2018-04-29
**URL**: https://discourse.slicer.org/t/need-spine-segmentation-module/2729

---

## Post #1 by @FTdiagnose (2018-04-29 02:42 UTC)

<p>have been trying to find spine segmentation module. Windows user but if only avail for linux would gladly install compatible linux. Have some Ubuntu with GUI experience. I have 32 and 64 bit systems and various slicer versions the latest i think is 4.8.1<br>
ref:<br>
<a href="https://www.slicer.org/wiki/Modules:SpineSegmentation-Documentation-3.6" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Modules:SpineSegmentation-Documentation-3.6</a><br>
<a href="https://www.nitrc.org/projects/sylvainproject/" class="onebox" target="_blank" rel="nofollow noopener">https://www.nitrc.org/projects/sylvainproject/</a><br>
<a href="https://na-mic.org/wiki/2010_Winter_Project_Week_Spine_Segmentation_Module_in_Slicer3" class="onebox" target="_blank" rel="nofollow noopener">https://na-mic.org/wiki/2010_Winter_Project_Week_Spine_Segmentation_Module_in_Slicer3</a><br>
member NITRC, nothing there that I can find. I do have windows slicer version 3.6.3.  I think I can get the linux version.  the extension is not available from windows/slicer/extension manager on any windows/slicer version that I know of although wiki say it is there.Linux only?<br>
I’ve found a reference to a spinalcordtoolbox (<a href="https://www.nitrc.org/projects/sct/" rel="nofollow noopener">https://www.nitrc.org/projects/sct/</a>)and there is a linux download on sourceforge but don’t know that its related or grew from of the slicer spine segmentation module, if for Slicer, or how to add it as its not via the extension manager that I know of. tried contact spine segmentation module Author but I have AOL and AOL mail is blocked. Next week will try alt sender email.</p>
<p>Can anyone help with the spine segmentation module or a newer version of it for 3dslicer?</p>
<p>thankyou</p>

---

## Post #2 by @lassoan (2018-04-29 03:29 UTC)

<p>I don’t think a fully automatic method exists for spine segmentation. Choice of semi-automatic methods depend on what part of the spine you would like to segment, for what clinical purpose, on what imaging modality, etc. There are several <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">tutorials about how to segment anatomical structures using 3D Slicer</a>, including spine. If you can share a bit more details about what you would like to do, then we may be able to give more specific advice.</p>

---

## Post #3 by @brhoom (2019-02-20 23:25 UTC)

<p><a href="https://github.com/MedicalImageAnalysisTutorials/SlicerCervicalSpine" rel="nofollow noopener">This extension</a> also could help. You may apply the same idea to get approximate segmentation of different part of the spine.</p>

---
