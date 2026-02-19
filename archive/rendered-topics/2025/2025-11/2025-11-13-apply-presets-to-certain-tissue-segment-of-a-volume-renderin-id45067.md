---
topic_id: 45067
title: "Apply Presets To Certain Tissue Segment Of A Volume Renderin"
date: 2025-11-13
url: https://discourse.slicer.org/t/45067
---

# Apply presets to certain tissue segment of a volume rendering

**Topic ID**: 45067
**Date**: 2025-11-13
**URL**: https://discourse.slicer.org/t/apply-presets-to-certain-tissue-segment-of-a-volume-rendering/45067

---

## Post #1 by @sogo (2025-11-13 15:40 UTC)

<p>Hi, I am working on writing a visualization function that applies a different color to a 3D rendering of a volume to only an area masked with tissue segment.</p>
<p>I am using split volume function to split segments into scalar volume nodes. The idea I am using so far is to use one of the split volume, apply a different preset to that split volume and use the color and component from split volume to set color on original volume scan. In example of screenshot below, I have the original volume and bone tissue split volume from the original scan with a different preset and I want to apply this preset to only bone covered areas of original volume.</p>
<p>Below is the code I have written so far and it is crashing as it calls the “setColor” to set different color transfer function to bone segment of original volume components. I wanted to ask if this is right way to do it or if there is any other efficient method to do something like this.</p>
<pre><code class="lang-auto">// -----------------------------------------------------------------------------------
void qSegmenterAppModuleWidget::testFunction() {
    Q_D(qTestApp);

    //volume nodes
    vtkMRMLScalarVolumeNode* vnodeOriginal = vtkMRMLScalarVolumeNode::SafeDownCast(qSlicerApplication::application()-&gt;mrmlScene()-&gt;GetNodeByID("vtkMRMLScalarVolumeNode1"));
    vtkMRMLScalarVolumeNode* vnodeSplit = vtkMRMLScalarVolumeNode::SafeDownCast(qSlicerApplication::application()-&gt;mrmlScene()-&gt;GetNodeByID("vtkMRMLScalarVolumeNode2"));

    vtkSlicerVolumeRenderingLogic* rlo = vtkSlicerVolumeRenderingLogic::SafeDownCast(qSlicerApplication::application()-&gt;moduleLogic("VolumeRendering"));
    
    //volume rendering display nodes
    vtkMRMLVolumeRenderingDisplayNode* displayNode3DSplit = rlo-&gt;GetFirstVolumeRenderingDisplayNode(vnodeSplit);
    vtkMRMLVolumeRenderingDisplayNode* displayNode3DOriginal = rlo-&gt;GetFirstVolumeRenderingDisplayNode(vnodeOriginal);

    //volume property nodes
    vtkMRMLVolumePropertyNode* volPropertyNodeSplit = displayNode3DSplit-&gt;GetVolumePropertyNode();
    vtkMRMLVolumePropertyNode* volPropertyNodeOriginal = displayNode3DOriginal-&gt;GetVolumePropertyNode();

    vtkDataArray* volArraySplit = vnodeSplit-&gt;GetImageData()-&gt;GetPointData()-&gt;GetScalars();

    for (int i = 0; i &lt; volArraySplit-&gt;GetNumberOfTuples(); i++)
    {
        if (volArraySplit-&gt;GetComponent(i, 0) &gt; 0)
        {
            vtkColorTransferFunction* function = volPropertyNodeSplit-&gt;GetColor(volArraySplit-&gt;GetComponent(i, 0));
            volPropertyNodeOriginal-&gt;SetColor(function, i);
        }
    }
}
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4481e9cee1fc2a8ff8cb601074c922772d98a650.jpeg" data-download-href="/uploads/short-url/9M2NYbBC4ZP4W5i3CpNgJU0arwQ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/4481e9cee1fc2a8ff8cb601074c922772d98a650_2_327x500.jpeg" alt="image" data-base62-sha1="9M2NYbBC4ZP4W5i3CpNgJU0arwQ" width="327" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/4481e9cee1fc2a8ff8cb601074c922772d98a650_2_327x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4481e9cee1fc2a8ff8cb601074c922772d98a650.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/4481e9cee1fc2a8ff8cb601074c922772d98a650.jpeg 2x" data-dominant-color="8E807C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">449×685 69.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-11-13 16:01 UTC)

<p>You can have a look at the ColorizeVolume module in the Sandbox extension.  You can completely control the volume rendering using segments.</p>
<aside class="quote quote-modified" data-post="1" data-topic="32254">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jaimigray/48/67886_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/new-colorize-volume-module/32254">New Colorize Volume module</a> <a class="badge-category__wrapper " href="/c/community/success-stories/29"><span data-category-id="29" style="--category-badge-color: #92278F; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #F7941D;" data-parent-category-id="12" data-drop-close="true" class="badge-category --style-square --has-parent" title="This is the place where you can share how Slicer helped your work. Describe your project and how Slicer was useful in achieving your goal. Include reference to any publication(s) and if possible also add a few nice images or links to videos."><span class="badge-category__name">Success stories</span></span></a>
    </div>
  </div>
  <blockquote>
    Just added to 3D Slicer 5.5 is the new Colorize Volume module! I tried it on a fully segmented rattlesnake skull with really nice results comparable to the expensive proprietary software VGStudio Max. I played around with the Volume Rendering settings, as well as Lights module (from the SandBox extension), and cropping to an ROI in the Volume Rendering module to bisect and view the inside of the skull. I am still exploring the various functions of this module but I am excited to see what else I …
  </blockquote>
</aside>


---

## Post #3 by @sogo (2025-11-13 17:01 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> for the quick response, I will take a look at Colorize Volume module.</p>

---
