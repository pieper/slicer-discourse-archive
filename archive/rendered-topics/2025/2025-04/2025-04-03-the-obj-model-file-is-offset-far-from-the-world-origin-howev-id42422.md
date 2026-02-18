# The .obj model file is offset far from the world origin,However, it is still possible to achieve position-based interaction between the image and the model 

**Topic ID**: 42422
**Date**: 2025-04-03
**URL**: https://discourse.slicer.org/t/the-obj-model-file-is-offset-far-from-the-world-origin-however-it-is-still-possible-to-achieve-position-based-interaction-between-the-image-and-the-model/42422

---

## Post #1 by @jiajiadelequ (2025-04-03 12:56 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/1649ee8c363ea0efd1cdea8b275adc5fc0b9200c.png" data-download-href="/uploads/short-url/3baTXqZuqBOCxQgG36nLRFfbm20.png?dl=1" title="图片1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/1649ee8c363ea0efd1cdea8b275adc5fc0b9200c.png" alt="图片1" data-base62-sha1="3baTXqZuqBOCxQgG36nLRFfbm20" width="554" height="358"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片1</span><span class="informations">554×358 93 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I have a set of matching .nii image files and .obj model files. After importing them into 3D Slicer, I found that the .obj model file is offset far from the world origin, basically out of the image’s range in the world coordinate system. However, it is still possible to achieve position-based interaction between the image and the model. How is this accomplished?</p>

---

## Post #2 by @lassoan (2025-04-03 12:59 UTC)

<p>Could you take a screenshot with the slice views visible in 3D so that we can see where the image is? (click the pushpin and then the eye icon above each slice view).</p>

---

## Post #3 by @jiajiadelequ (2025-04-07 02:07 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c59d2f925e753f75459f7a459cf4a4174911a5fd.jpeg" data-download-href="/uploads/short-url/scaPvrmSaiIvWmIv8CxRjl6GowJ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c59d2f925e753f75459f7a459cf4a4174911a5fd_2_690x445.jpeg" alt="image" data-base62-sha1="scaPvrmSaiIvWmIv8CxRjl6GowJ" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c59d2f925e753f75459f7a459cf4a4174911a5fd_2_690x445.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c59d2f925e753f75459f7a459cf4a4174911a5fd_2_1035x667.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c59d2f925e753f75459f7a459cf4a4174911a5fd_2_1380x890.jpeg 2x" data-dominant-color="535259"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1423×918 66.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
However, when I load these .obj models into my self-written VTK software, the displayed positions are significantly offset from the origin, and there is a large discrepancy between the positions selected on the image and the model.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/001292a3541ff9e0ecc57d3752d8be8e3f10bf3e.jpeg" data-download-href="/uploads/short-url/DN6DOXZPbBa6KLYOnwn1xeMpM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/001292a3541ff9e0ecc57d3752d8be8e3f10bf3e_2_690x420.jpeg" alt="image" data-base62-sha1="DN6DOXZPbBa6KLYOnwn1xeMpM" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/001292a3541ff9e0ecc57d3752d8be8e3f10bf3e_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/001292a3541ff9e0ecc57d3752d8be8e3f10bf3e_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/001292a3541ff9e0ecc57d3752d8be8e3f10bf3e_2_1380x840.jpeg 2x" data-dominant-color="515559"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1647×1004 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @jiajiadelequ (2025-04-07 02:09 UTC)

<p>This is the relevant code I wrote</p>
<pre><code class="lang-auto">void vtkSliceLoader::Load(std::string fileName)
{
    reader-&gt;SetFileName(fileName.c_str());
    reader-&gt;Update();

    //计算center
    double spacing[3];
    double origin[3];
    int extent[6];
    reader-&gt;GetOutputInformation(0)-&gt;Get(
        vtkStreamingDemandDrivenPipeline::WHOLE_EXTENT(), extent);
    reader-&gt;GetOutput()-&gt;GetSpacing(spacing);
    reader-&gt;GetOutput()-&gt;GetOrigin(origin);
    this-&gt;center[0] = origin[0] + spacing[0] * 0.5 * (extent[0] + extent[1]);
    this-&gt;center[1] = origin[1] + spacing[1] * 0.5 * (extent[2] + extent[3]);
    this-&gt;center[2] = origin[2] + spacing[2] * 0.5 * (extent[4] + extent[5]);
}</code></pre>

---

## Post #5 by @jiajiadelequ (2025-04-07 02:10 UTC)

<pre><code class="lang-auto">void asclepios::gui::vtkResliceCallback::moveCursor(double* t_position) const
{
	vtkMatrix4x4* matrix = nullptr;
	vtkMatrix4x4* matrix2 = nullptr;
	vtkMatrix4x4* sourceMatrix =
		m_resliceWidget-&gt;getImageReslicers()[m_handleNumber]-&gt;GetResliceAxes();
	switch (m_handleNumber)
	{
	case 0:
		matrix = m_resliceWidget-&gt;getImageReslicers()[1]-&gt;GetResliceAxes();
		matrix2 = m_resliceWidget-&gt;getImageReslicers()[2]-&gt;GetResliceAxes();
		break;
	case 1:
		matrix = m_resliceWidget-&gt;getImageReslicers()[0]-&gt;GetResliceAxes();
		matrix2 = m_resliceWidget-&gt;getImageReslicers()[2]-&gt;GetResliceAxes();
		break;
	case 2:
		matrix = m_resliceWidget-&gt;getImageReslicers()[0]-&gt;GetResliceAxes();
		matrix2 = m_resliceWidget-&gt;getImageReslicers()[1]-&gt;GetResliceAxes();
		break;
	default:
		break;
	}
	if (m_window)
	{
		vtkNew&lt;vtkTransform&gt; transform;
		transform-&gt;SetMatrix(sourceMatrix);
		transform-&gt;Translate(t_position[0], t_position[1], 0);
		double center[3] =
		{
			transform-&gt;GetMatrix()-&gt;GetElement(0, 3),
			transform-&gt;GetMatrix()-&gt;GetElement(1, 3),
			transform-&gt;GetMatrix()-&gt;GetElement(2, 3)
		};
		matrix-&gt;SetElement(0, 3, center[0]);
		matrix-&gt;SetElement(1, 3, center[1]);
		matrix-&gt;SetElement(2, 3, center[2]);
		matrix2-&gt;SetElement(0, 3, center[0]);
		matrix2-&gt;SetElement(1, 3, center[1]);
		matrix2-&gt;SetElement(2, 3, center[2]);

		
		emit EventManager::instance()-&gt;moveCursor(m_handleNumber,center);
	}
}</code></pre>

---

## Post #6 by @jiajiadelequ (2025-04-07 02:10 UTC)

<pre><code class="lang-auto">void vtkThreeDViewerLogic::onSliceMoveCursor(int handleIdx, double* slicePos) {

    double worldPoint[3];
    double* center = vtkSliceLoader::instance().GetCenter();
 
    worldPoint[0] = slicePos[0] - center[0];
    worldPoint[1] = slicePos[1] - center[1];
    worldPoint[2] = slicePos[2] - center[2];

    if (!mRenderer-&gt;HasViewProp(mPickMark)) {
        mRenderer-&gt;AddActor(mPickMark);
    }

    mPickMark-&gt;SetPosition(worldPoint);
    mInteractor-&gt;Render();
}</code></pre>

---

## Post #7 by @lassoan (2025-04-07 04:00 UTC)

<p>The code snippets are incomplete, it is not possible to even guess what they might be doing.<br>
Slicer is open-source, you can inspect the code and figure out what it does and reimplement in your own software. However, you will experience that there is just way too much to copy from Slicer - you are probably better off customizing and extending Slicer - see <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/">https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a></p>

---
