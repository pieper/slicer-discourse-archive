# Setting up the qMRML Segment editor Widget in ui

**Topic ID**: 24486
**Date**: 2022-07-25
**URL**: https://discourse.slicer.org/t/setting-up-the-qmrml-segment-editor-widget-in-ui/24486

---

## Post #1 by @HanadElmi (2022-07-25 17:31 UTC)

<p>Slicer version: 5.0.2</p>
<p>Hello everyone,</p>
<p>I have been trying to add the segment editor widget within my own module for user convenience. So far, I have been able to create the widget and have it appear in a popup window. Here is a picture of what was done so far:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01219cb9c74487349f6f02cb27eb19bbd5cac4e7.png" data-download-href="/uploads/short-url/a0usy0cFTBS2tLlP5C3wHJAL1t.png?dl=1" title="picture 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01219cb9c74487349f6f02cb27eb19bbd5cac4e7_2_690x311.png" alt="picture 1" data-base62-sha1="a0usy0cFTBS2tLlP5C3wHJAL1t" width="690" height="311" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01219cb9c74487349f6f02cb27eb19bbd5cac4e7_2_690x311.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01219cb9c74487349f6f02cb27eb19bbd5cac4e7_2_1035x466.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01219cb9c74487349f6f02cb27eb19bbd5cac4e7_2_1380x622.png 2x" data-dominant-color="B8B8B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">picture 1</span><span class="informations">2902×1311 94.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, I wanted to use the Segment Editor Widget I added to my UI. But I am unable to initiate and setup it up. Here is another screenshot showing the widget I want to use:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3ddab802bd5d933f1aacd90a23abc2d1e35e5d25.png" data-download-href="/uploads/short-url/8PbJaxj1tIEJcceFpIp4q8y0AVD.png?dl=1" title="pic 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3ddab802bd5d933f1aacd90a23abc2d1e35e5d25_2_596x499.png" alt="pic 2" data-base62-sha1="8PbJaxj1tIEJcceFpIp4q8y0AVD" width="596" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3ddab802bd5d933f1aacd90a23abc2d1e35e5d25_2_596x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3ddab802bd5d933f1aacd90a23abc2d1e35e5d25_2_894x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3ddab802bd5d933f1aacd90a23abc2d1e35e5d25.png 2x" data-dominant-color="ECECEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic 2</span><span class="informations">1042×873 32.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If anyone could help me it would be greatly appreciated. Thanks!</p>

---

## Post #2 by @Sunderlandkyl (2022-07-25 18:08 UTC)

<p>You need to make sure from your module that the segment editor widget has:</p>
<ul>
<li>The MRMLScene set (editor.setMRMLScene())</li>
<li>A segment editor parameter node (editor.setMRMLSegmentEditorNode())</li>
</ul>
<p>If you are using the Qt designer you can use that to set up a connection to the setMRMLScene slot from the parent widget. The latter will have to be done in Python. You can see an example of this in the SegmentEditor module: <a href="https://github.com/Slicer/Slicer/blob/6931e0d9820a86be8c97f77225bdd3a479980820/Modules/Scripted/SegmentEditor/SegmentEditor.py#L77-L90" class="inline-onebox" rel="noopener nofollow ugc">Slicer/SegmentEditor.py at 6931e0d9820a86be8c97f77225bdd3a479980820 · Slicer/Slicer · GitHub</a></p>

---

## Post #3 by @HanadElmi (2022-07-25 18:11 UTC)

<p>Hey Kyle, thank you very much for the quick answer!!! I’ll try this and get back to you to see if I can get it to work.</p>

---

## Post #4 by @HanadElmi (2022-07-25 19:52 UTC)

<p>Hello again,</p>
<p>So I implemented the code and set the MRMLscene and parameter node for the Segment Editor Widget as well as adding the connection on qt designer.</p>
<p>However, none of the methods seem to work. I linked the code I added as well as the connection I made:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70524caf0817ab3c83fe701febb42b791bf0e35b.png" data-download-href="/uploads/short-url/g1DNLoTIWqQVuBpVcZHD1auPXvB.png?dl=1" title="pic 3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70524caf0817ab3c83fe701febb42b791bf0e35b_2_690x424.png" alt="pic 3" data-base62-sha1="g1DNLoTIWqQVuBpVcZHD1auPXvB" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70524caf0817ab3c83fe701febb42b791bf0e35b_2_690x424.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70524caf0817ab3c83fe701febb42b791bf0e35b_2_1035x636.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/70524caf0817ab3c83fe701febb42b791bf0e35b_2_1380x848.png 2x" data-dominant-color="262C2F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic 3</span><span class="informations">2127×1309 297 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>P.S - I made sure to add the selectParameterNode(self) function as well.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e36f7cdb374fbeacd54d16018a2af455e1c999d.png" data-download-href="/uploads/short-url/6APJnO6cDeIFXXGLux4d8w75xCt.png?dl=1" title="pic 4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e36f7cdb374fbeacd54d16018a2af455e1c999d_2_690x435.png" alt="pic 4" data-base62-sha1="6APJnO6cDeIFXXGLux4d8w75xCt" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e36f7cdb374fbeacd54d16018a2af455e1c999d_2_690x435.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e36f7cdb374fbeacd54d16018a2af455e1c999d_2_1035x652.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e36f7cdb374fbeacd54d16018a2af455e1c999d_2_1380x870.png 2x" data-dominant-color="CACBCC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic 4</span><span class="informations">1854×1171 68.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am not sure where the error comes from. If there is anything else you need please let me know. Thank you again!</p>

---

## Post #5 by @Sunderlandkyl (2022-07-25 20:12 UTC)

<p>If you set slicer.mrmlScene in Python then it doesn’t need to be done in the Qt designer as well.<br>
Can you confirm that selectParameterNode() is run and self.parameterSetNode is not None?</p>
<p>If you still have issues then you can post or email me a link to the code and I can take a look at it.</p>

---

## Post #6 by @HanadElmi (2022-07-26 20:25 UTC)

<p>Hello Kyle,</p>
<p>I apologize for the late response. I tested the function and can assure you that the selectParameterNode() function runs and self.paramaterSetNode is not None type.</p>
<p>I did however realize that the code does create a segment editor widget and if I type self.editor.show(), it appears in another popup window. However, it fails to instead make the connection with the segment editor widget implemented in my UI. I believe the problem comes from the following lines :</p>
<p>import qSlicerSegmentationsModuleWidgetsPythonQt<br>
self.editor = qSlicerSegmentationsModuleWidgetsPythonQt.qMRMLSegmentEditorWidget()</p>
<p>Instead of creating a new widget, I would have to connect the Segment Editor functionality to the widget in my UI. Is there a way to access the widget from the UI file in python?</p>
<p>If that’s alright, I’ll also email you my code. Thank you again for everything.</p>

---

## Post #7 by @laurentletg (2023-03-16 21:17 UTC)

<p>Hello,</p>
<p>I am looking at this discussion, by any chance, were you able to resolve this issue ?<br>
I am not able to connect the segment editor in a customized GUI.<br>
If you have a working code snippet (python), this would be very useful.</p>
<p>Thanks!</p>

---

## Post #8 by @Sunderlandkyl (2023-03-16 21:25 UTC)

<p>If I recall, the issue was that there was an editor widget in the UI file and another that was created in Python that was not added to the module widget.</p>
<p>You need to make sure that your widget is connected to the mrmlScene, and has a segment editor node. The SegmentEditor module is probably the best resource for seeing how to use the widget. <a href="https://github.com/Slicer/Slicer/blob/6931e0d9820a86be8c97f77225bdd3a479980820/Modules/Scripted/SegmentEditor/SegmentEditor.py#L77-L90" class="inline-onebox" rel="noopener nofollow ugc">Slicer/SegmentEditor.py at 6931e0d9820a86be8c97f77225bdd3a479980820 · Slicer/Slicer · GitHub</a>.</p>
<p>Can you be more specific about the problem that you are having?</p>

---
