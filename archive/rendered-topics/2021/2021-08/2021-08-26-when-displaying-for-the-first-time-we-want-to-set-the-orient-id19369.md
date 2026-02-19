---
topic_id: 19369
title: "When Displaying For The First Time We Want To Set The Orient"
date: 2021-08-26
url: https://discourse.slicer.org/t/19369
---

# When displaying for the first time, we want to set the orientation of the Anatomical plane

**Topic ID**: 19369
**Date**: 2021-08-26
**URL**: https://discourse.slicer.org/t/when-displaying-for-the-first-time-we-want-to-set-the-orientation-of-the-anatomical-plane/19369

---

## Post #1 by @11136 (2021-08-26 15:21 UTC)

<p>Hello, thank you for reading my topic.</p>
<p>In the sample project I made, I want the screen to be displayed when DICOM is first loaded like the 3D Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6766eb8aa4a54843b43a9bf7498c331da4a7a774.jpeg" data-download-href="/uploads/short-url/eKJGs3UEoNR2ydn6JfghwTsGYD2.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6766eb8aa4a54843b43a9bf7498c331da4a7a774_2_660x500.jpeg" alt="image" data-base62-sha1="eKJGs3UEoNR2ydn6JfghwTsGYD2" width="660" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6766eb8aa4a54843b43a9bf7498c331da4a7a774_2_660x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6766eb8aa4a54843b43a9bf7498c331da4a7a774.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6766eb8aa4a54843b43a9bf7498c331da4a7a774.jpeg 2x" data-dominant-color="5A5A5F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">850×643 96.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>3D Slicer</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6766eb8aa4a54843b43a9bf7498c331da4a7a774.jpeg" data-download-href="/uploads/short-url/eKJGs3UEoNR2ydn6JfghwTsGYD2.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6766eb8aa4a54843b43a9bf7498c331da4a7a774_2_660x500.jpeg" alt="image" data-base62-sha1="eKJGs3UEoNR2ydn6JfghwTsGYD2" width="660" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6766eb8aa4a54843b43a9bf7498c331da4a7a774_2_660x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6766eb8aa4a54843b43a9bf7498c331da4a7a774.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/6766eb8aa4a54843b43a9bf7498c331da4a7a774.jpeg 2x" data-dominant-color="5A5A5F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">850×643 96.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>My sample project</li>
</ul>
<p>DICOM Laterality and Patient Position were handled correctly, but what am I missing?</p>
<p>Below is the sample code.</p>
<blockquote>
<p>Blockquote<br>
vtkSmartPointer importer = vtkSmartPointer::New();<br>
importer-&gt;SetDataSpacing(reader-&gt;m_dPixelSpacing[0], reader-&gt;m_dPixelSpacing[1], reader-&gt;m_dPixelSpacing[2]);<br>
importer-&gt;SetDataOrigin(0, 0, 0);<br>
importer-&gt;SetWholeExtent(0, reader-&gt;m_DicomImageInfo.nWidth - 1, 0, reader-&gt;m_DicomImageInfo.nHeight - 1, 0, reader-&gt;m_nImgCnt - 1);<br>
importer-&gt;SetDataExtentToWholeExtent();<br>
importer-&gt;SetDataScalarType(reader-&gt;m_nScalarType);<br>
importer-&gt;SetNumberOfScalarComponents(reader-&gt;m_DicomImageInfo.nSamplesPerPixel);<br>
importer-&gt;SetImportVoidPointer(reader-&gt;GetOutputBuffer());<br>
importer-&gt;Update();</p>
</blockquote>
<pre><code>vtkSmartPointer&lt;vtkMatrix4x4&gt; pm = vtkSmartPointer&lt;vtkMatrix4x4&gt;::New();
pm-&gt;DeepCopy(reader-&gt;pm);
pm-&gt;Invert();

reslice = vtkSmartPointer&lt;vtkImageReslice&gt;::New();
reslice-&gt;SetInputData(importer-&gt;GetOutput());
reslice-&gt;SetResliceAxes(pm);
reslice-&gt;SetInterpolationModeToLinear();
reslice-&gt;AutoCropOutputOn();
reslice-&gt;Update();

int imageDims[3] = { 0, };
reslice-&gt;GetOutput()-&gt;GetDimensions(imageDims);

for (int i = 0; i &lt; 3; i++)
{
	vtkMFCWindow[i] = make_shared&lt;vtkMFCWindowEx&gt;(GetDlgItem(nWndResourceID[i]));

	riv[i] = vtkSmartPointer&lt;vtkResliceImageViewer&gt;::New();

	riv[i]-&gt;SetRenderWindow(vtkMFCWindow[i]-&gt;GetRenderWindow());
	vtkMFCWindow[i]-&gt;GetRenderWindow()-&gt;AddRenderer(riv[i]-&gt;GetRenderer());
	riv[i]-&gt;SetupInteractor(vtkMFCWindow[i]-&gt;GetInteractor());

	vtkResliceCursorLineRepresentation *rep = vtkResliceCursorLineRepresentation::SafeDownCast(riv[i]-&gt;GetResliceCursorWidget()-&gt;GetRepresentation());
	riv[i]-&gt;SetResliceCursor(riv[0]-&gt;GetResliceCursor());

	rep-&gt;GetResliceCursorActor()-&gt;GetCursorAlgorithm()-&gt;SetReslicePlaneNormal(i);

	riv[i]-&gt;SetInputData(reslice-&gt;GetOutput());

	riv[i]-&gt;SetSlice(imageDims[i] / 2);

	riv[i]-&gt;SetSliceOrientation(i);
	riv[i]-&gt;SetResliceModeToOblique();

	riv[i]-&gt;Reset();
}

vtkSmartPointer&lt;vtkCellPicker&gt; picker = vtkSmartPointer&lt;vtkCellPicker&gt;::New();
picker-&gt;SetTolerance(0.005);

vtkSmartPointer&lt;vtkProperty&gt; ipwProp = vtkSmartPointer&lt;vtkProperty&gt;::New();
ipwProp-&gt;LightingOff();

vtkMFCWindow[3] = make_shared&lt;vtkMFCWindowEx&gt;(GetDlgItem(nWndResourceID[3]));
vtkSmartPointer&lt;vtkRenderer&gt; ren = vtkSmartPointer&lt;vtkRenderer&gt;::New();
vtkWin32OpenGLRenderWindow *renWin = vtkMFCWindow[3]-&gt;GetRenderWindow();
renWin-&gt;AddRenderer(ren);

vtkRenderWindowInteractor *iren = vtkMFCWindow[3]-&gt;GetInteractor();

for (int i = 0; i &lt; 3; i++)
{
	planeWidget[i] = vtkSmartPointer&lt;vtkImagePlaneWidget&gt;::New();
	planeWidget[i]-&gt;SetInteractor(iren);
	planeWidget[i]-&gt;SetPicker(picker);
	planeWidget[i]-&gt;RestrictPlaneToVolumeOn();
	double color[3] = { 0, 0, 0 };
	//color[i] = 1 / 4.0;
	planeWidget[i]-&gt;GetPlaneProperty()-&gt;SetColor(color);

	riv[i]-&gt;GetRenderer()-&gt;SetBackground(color);

	planeWidget[i]-&gt;SetTexturePlaneProperty(ipwProp);
	planeWidget[i]-&gt;TextureInterpolateOff();
	planeWidget[i]-&gt;SetResliceInterpolateToLinear();

	planeWidget[i]-&gt;SetInputConnection(reslice-&gt;GetOutputPort());

	planeWidget[i]-&gt;SetPlaneOrientation(i);
	planeWidget[i]-&gt;SetSliceIndex(imageDims[i] / 2);
	planeWidget[i]-&gt;DisplayTextOn();
	planeWidget[i]-&gt;SetDefaultRenderer(ren);
	planeWidget[i]-&gt;On();
	planeWidget[i]-&gt;InteractionOff();
}

auto resliceCbk = vtkSmartPointer&lt;vtkResliceCursorCallback&gt;::New();

for (int i = 0; i &lt; 3; i++)
{
	resliceCbk-&gt;IPW[i] = planeWidget[i];
	resliceCbk-&gt;RCW[i] = riv[i]-&gt;GetResliceCursorWidget();

	riv[i]-&gt;GetResliceCursorWidget()-&gt;AddObserver(vtkResliceCursorWidget::ResliceAxesChangedEvent, resliceCbk);
	riv[i]-&gt;GetResliceCursorWidget()-&gt;AddObserver(vtkResliceCursorWidget::WindowLevelEvent, resliceCbk);
	riv[i]-&gt;GetResliceCursorWidget()-&gt;AddObserver(vtkResliceCursorWidget::ResliceThicknessChangedEvent, resliceCbk);
	riv[i]-&gt;GetResliceCursorWidget()-&gt;AddObserver(vtkResliceCursorWidget::ResetCursorEvent, resliceCbk);
	riv[i]-&gt;GetInteractorStyle()-&gt;AddObserver(vtkCommand::WindowLevelEvent, resliceCbk);

	riv[i]-&gt;AddObserver(vtkResliceImageViewer::SliceChangedEvent, resliceCbk);

//	// Make them all share the same color map.
	riv[i]-&gt;SetLookupTable(riv[0]-&gt;GetLookupTable());
	planeWidget[i]-&gt;GetColorMap()-&gt;SetLookupTable(riv[0]-&gt;GetLookupTable());
	planeWidget[i]-&gt;SetColorMap(riv[i]-&gt;GetResliceCursorWidget()-&gt;GetResliceCursorRepresentation()-&gt;GetColorMap());
}

ren-&gt;SetBackground(0, 0, 255);
ren-&gt;SetBackground(100, 100, 255);
ren-&gt;SetGradientBackground(true);

ren-&gt;GetActiveCamera()-&gt;SetViewUp(0, 0, 1);
ren-&gt;GetActiveCamera()-&gt;SetPosition(0, 1, 0);
ren-&gt;GetActiveCamera()-&gt;SetFocalPoint(0, 0, 0);
ren-&gt;GetActiveCamera()-&gt;ComputeViewPlaneNormal();

ren-&gt;ResetCamera();
ren-&gt;ResetCameraClippingRange();

delete reader;
reader = nullptr;
</code></pre>
<blockquote>
<p>Blockquote</p>
</blockquote>
<p>thank you.</p>

---

## Post #2 by @lassoan (2021-08-26 15:31 UTC)

<p>You’ll realize that you need more features of Slicer than just setting the orientation of slice views. Instead of copying features from Slicer one by one, I would recommend to create a <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/">custom Slicer application</a>.</p>

---
