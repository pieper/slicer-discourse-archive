---
topic_id: 39441
title: "Vtkitkarchetypeimageseriesscalarreader Getrastoijkmatrix Sam"
date: 2024-09-30
url: https://discourse.slicer.org/t/39441
---

# vtkITKArchetypeImageSeriesScalarReader:: GetRasToIjkMatrix Same DicomFiles but Different result

**Topic ID**: 39441
**Date**: 2024-09-30
**URL**: https://discourse.slicer.org/t/vtkitkarchetypeimageseriesscalarreader-getrastoijkmatrix-same-dicomfiles-but-different-result/39441

---

## Post #1 by @Hanzhang_DAI (2024-09-30 01:50 UTC)

<p>My   C++ Code<br>
#################<br>
vtkSmartPointer volumeReader = vtkSmartPointer::New();<br>
volumeReader-&gt;SetArchetype(sortedFiles-&gt;GetValue(0).c_str());<br>
for (int i = 0; i &lt; sortedFiles-&gt;GetNumberOfValues(); i++) {<br>
volumeReader-&gt;AddFileName(sortedFiles-&gt;GetValue(i).c_str());<br>
}</p>
<pre><code>volumeReader-&gt;SetSingleFile(0);
volumeReader-&gt;SetOutputScalarTypeToNative();
volumeReader-&gt;SetDesiredCoordinateOrientationToNative();
volumeReader-&gt;SetUseNativeOriginOn();
volumeReader-&gt;Update();
PrintMatrix4X4(volumeReader-&gt;GetRasToIjkMatrix(), "VolumeReader RasIjk");
</code></pre>
<p>######### Output ##################<br>
Begin VolumeReader RasIjk#<br>
-1.600000,      -0.000000,       0.000000,     240.320000<br>
-0.000000,      -1.600000,      -0.000000,     256.000000<br>
0.000000,      -0.000000,       0.800000,     <strong>-34.800000</strong><br>
-0.000000,       0.000000,      -0.000000,       1.000000<br>
<span class="hashtag-raw">#End</span> VolumeReader RasIjk<br>
########################################</p>
<p>3DSlicer  Edit File :   Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py<br>
#############<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e440b13afffb8bf2e920518718aad11d6bfed1f9.png" data-download-href="/uploads/short-url/wzdsSSBfqLfRDSsdaPcxvUTgpCN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e440b13afffb8bf2e920518718aad11d6bfed1f9.png" alt="image" data-base62-sha1="wzdsSSBfqLfRDSsdaPcxvUTgpCN" width="689" height="480" data-dominant-color="B8BAB9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1209×842 60.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What is happening ?</p>

---

## Post #2 by @Hanzhang_DAI (2024-09-30 01:55 UTC)

<pre><code class="lang-auto">
void PrintMatrix4X4(const vtkMatrix4x4 *matrix4X4, const char *flagName);

int main(int argc, char **argv) {
    vtkLogger::Init(argc, argv);
    // Put every log message in "everything.log":
    vtkLogger::LogToFile("everything.log", vtkLogger::APPEND, vtkLogger::VERBOSITY_MAX);
    // needed to ensure appropriate OpenGL context is created for VTK rendering.
    QSurfaceFormat::setDefaultFormat(QVTKRenderWidget::defaultFormat());
    // QT Stuff
    QApplication app(argc, argv);

    vtkNew&lt;vtkDICOMDirectory&gt; dicomdir;
    dicomdir-&gt;SetDirectoryName("/home/dhz/v4486");
    dicomdir-&gt;RequirePixelDataOff();
    dicomdir-&gt;Update();

    int n = dicomdir-&gt;GetNumberOfSeries();
    if (n == 0) {
        std::cerr &lt;&lt; "No DICOM images in directory!" &lt;&lt; std::endl;
        return EXIT_FAILURE;
    }

    int firstStudy = 0;
    // Get information related to the patient study
    vtkDICOMItem patient = dicomdir-&gt;GetPatientRecordForStudy(firstStudy);
    vtkDICOMItem study = dicomdir-&gt;GetStudyRecord(firstStudy);


    // Iterate through all the series in this study.
    int j1 = dicomdir-&gt;GetFirstSeriesForStudy(firstStudy);
    //  int j2 = dicomdir-&gt;GetLastSeriesForStudy(i);
    // get some of the series attributes as a vtkDICOMItem
    vtkDICOMItem series = dicomdir-&gt;GetSeriesRecord(j1);
    // get all the files in the series
    vtkStringArray *sortedFiles = dicomdir-&gt;GetFileNamesForSeries(j1);


    vtkSmartPointer&lt;vtkITKArchetypeImageSeriesScalarReader&gt; volumeReader = vtkSmartPointer&lt;vtkITKArchetypeImageSeriesScalarReader&gt;::New();
    volumeReader-&gt;SetArchetype(sortedFiles-&gt;GetValue(0).c_str());
    for (int i = 0; i &lt; sortedFiles-&gt;GetNumberOfValues(); i++) {
        volumeReader-&gt;AddFileName(sortedFiles-&gt;GetValue(i).c_str());
    }



    volumeReader-&gt;SetSingleFile(0);
    volumeReader-&gt;SetOutputScalarTypeToNative();
    volumeReader-&gt;SetDesiredCoordinateOrientationToNative();
    volumeReader-&gt;SetUseNativeOriginOn();
    volumeReader-&gt;Update();
    PrintMatrix4X4(volumeReader-&gt;GetRasToIjkMatrix(), "VolumeReader RasIjk");

    auto imageChangeInformation = vtkSmartPointer&lt;vtkImageChangeInformation&gt;::New();
    imageChangeInformation-&gt;SetInputConnection(volumeReader-&gt;GetOutputPort());
    imageChangeInformation-&gt;SetOutputSpacing(1, 1, 1);
    imageChangeInformation-&gt;SetOutputOrigin(0, 0, 0);
    imageChangeInformation-&gt;Update();


    auto imageData = imageChangeInformation-&gt;GetOutputDataObject(0);
    if (!imageData-&gt;IsA("vtkImageData")) {
        vtkLogF(INFO, "ImageData is vtkImageData");
        return EXIT_FAILURE;
    }
    auto pImg = (vtkImageData *) imageData;


    int imageDims[3];
    double origin[3] = {0.0};
    double spacing[3] = {1.0};
    int extentInfo[6] = {0};
    pImg-&gt;GetDimensions(imageDims);
    pImg-&gt;GetOrigin(origin);
    pImg-&gt;GetSpacing(spacing);
////        vtkMatrix3x3 *imageDirection = chgData-&gt;GetDirectionMatrix();
//
    pImg-&gt;GetExtent(extentInfo);

    vtkLogF(INFO, "Dimensions: %d,%d,%d", imageDims[0], imageDims[1], imageDims[2]);
    vtkLogF(INFO, "    Origin: %f,%f,%f", origin[0], origin[1], origin[2]);
    vtkLogF(INFO, "   Spacing: %f,%f, %f", spacing[0], spacing[1], spacing[2]);
    vtkLogF(INFO, "    Extent: %d,%d,%d,%d,%d,%d", extentInfo[0], extentInfo[1], extentInfo[2],
            extentInfo[3], extentInfo[4], extentInfo[5]);
    return QApplication::exec();
}


void PrintMatrix4X4(const vtkMatrix4x4 *matrix4X4, const char *flagName = nullptr) {
    vtkLogF(INFO, "Begin %s#", flagName);
    auto data = matrix4X4-&gt;GetData();
    for (int i = 0; i &lt; 4; ++i) {
        vtkLogF(INFO, "%15.6f,%15.6f,%15.6f,%15.6f", data[4 * i], data[4 * i + 1], data[4 * i + 2],
                data[4 * i + 3]);
    }

    vtkLogF(INFO, "#End %s", flagName);
}
</code></pre>

---

## Post #3 by @pieper (2024-10-01 12:55 UTC)

<p>I’m not sure anyone has time to read through and comment your C++ code.  Do you have a specific issue that would narrow down your concern?</p>
<p>If you think there’s a bug in the library could you provide a reproducible example using public data?</p>

---

## Post #4 by @Hanzhang_DAI (2024-10-08 04:04 UTC)

<p>Sorry !   the same serices dicom files. when use vtkITK library vtkITKArchetypeImageSeriesScalarReader →  GetRasToIjkMatrix is not equal PyScripts :  DICOMScalarVolumePlugin   .I’m just wondering about the cause. is there  miss something ?</p>

---

## Post #5 by @pieper (2024-10-08 17:07 UTC)

<p>I don’t know off the top of my head.  You should be able to use debuggers to figure out what the code path is to see why they are not what you expect.</p>

---
