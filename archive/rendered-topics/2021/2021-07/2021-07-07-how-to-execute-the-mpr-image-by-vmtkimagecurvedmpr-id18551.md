---
topic_id: 18551
title: "How To Execute The Mpr Image By Vmtkimagecurvedmpr"
date: 2021-07-07
url: https://discourse.slicer.org/t/18551
---

# How to execute the MPR image by vmtkimagecurvedmpr？

**Topic ID**: 18551
**Date**: 2021-07-07
**URL**: https://discourse.slicer.org/t/how-to-execute-the-mpr-image-by-vmtkimagecurvedmpr/18551

---

## Post #1 by @su2p (2021-07-07 01:58 UTC)

<p>I use this scripts to execute the MPR image, the input file format is vti, the output file format is vtp, the centerlines file is executed by other scrips of vmtk, but the output image size is 1k? Why output is so small?</p>

---

## Post #2 by @su2p (2021-07-07 09:14 UTC)

<p>My scrip’s code  is after follows：</p>
<pre><code class="lang-python">def ReadVTKImageFile(infile):
    if (infile == ''):
        print('Error: no InputFileName.')
    print('Reading VTK image file.')
    # reader = vtk.vtkXMLPolyDataReader()
    # reader = vtk.vtkPolyDataReader()
    reader = vtk.vtkXMLImageDataReader()
    reader.SetFileName(infile)
    reader.Update()
    # image = vtk.vtkImageData()
    # image.DeepCopy(reader.GetOutput())
    # caster = vtk.vtkImageCast()
    # caster.SetInputData(reader.GetOutput())
    # caster.SetOutputScalarTypeToFloat()
    # caster.Update()
    # image = reader.GetOutput()
    # return caster.GetOutput()
    return reader.GetOutput()


def ReadDicomFile(infile):
    dicom_reader = vtk.vtkDICOMImageReader()
    dicom_reader.SetDirectoryName(infile)
    dicom_reader.FileLowerLeftOn()
    dicom_reader.Update()
    img_data = dicom_reader.GetOutput()
    return img_data


def ReadNiiImageFile(ifile):
    DesiredOrientation = 'native'
    if ifile == '':
        print('Error: no InputFileName.')
    print('Reading ITKIO.')
    reader = vtkvmtk.vtkvmtkITKArchetypeImageSeriesScalarReader()
    reader.SetArchetype(ifile)
    reader.SetDefaultDataSpacing([1.0, 1.0, 1.0])
    reader.SetDefaultDataOrigin([0.0, 0.0, 0.0])
    reader.SetOutputScalarTypeToNative()
    if DesiredOrientation == 'native':
        reader.SetDesiredCoordinateOrientationToNative()
    elif DesiredOrientation == 'axial':
        reader.SetDesiredCoordinateOrientationToAxial()
    elif DesiredOrientation == 'coronal':
        reader.SetDesiredCoordinateOrientationToCoronal()
    elif DesiredOrientation == 'sagittal':
        reader.SetDesiredCoordinateOrientationToSagittal()
    reader.SetSingleFile(0)
    reader.Update()
    image = vtk.vtkImageData()
    image.DeepCopy(reader.GetOutput())
    return image


def ReadCeterLineFile(infile):
    if (infile == ''):
        print('Error: no InputFileName.')
    print('Reading VTK image file.')
    # reader = vtk.vtkPolyDataReader()
    reader = vtk.vtkXMLPolyDataReader()
    reader.SetFileName(infile)
    reader.Update()

    att_reader = vtkvmtk.vtkvmtkCenterlineAttributesFilter()
    att_reader.SetInputData(reader.GetOutput())
    att_reader.SetAbscissasArrayName("Abscissas")
    att_reader.SetParallelTransportNormalsArrayName("ParallelTransportNormals")  # ParallelTransportNormals
    att_reader.Update()
    # # image = att_reader.GetOutput()
    # ctr = vtk.vtkPolyData()
    # ctr.DeepCopy(att_reader.GetOutput())
    #
    geo_reader = vtkvmtk.vtkvmtkCenterlineGeometry()
    geo_reader.SetInputData(reader.GetOutput())
    geo_reader.SetLengthArrayName("Length")
    geo_reader.SetCurvatureArrayName("Curvature")  # cur
    geo_reader.SetTorsionArrayName("Torsion")  # tor
    geo_reader.SetTortuosityArrayName("Tortuosity")  # tort
    geo_reader.SetFrenetTangentArrayName("FrenetTangent")
    geo_reader.SetFrenetNormalArrayName("FrenetNormal")  # FSNormals
    # geo_reader.SetFrenetTangentArrayName("FSTangents")  # FSTangents
    geo_reader.SetFrenetBinormalArrayName("FrenetBinormal")  # FSBinormals
    geo_reader.SetLineSmoothing(0)  # 1
    geo_reader.SetOutputSmoothedLines(0)
    # geo_reader.LineSmoothingOff()
    geo_reader.SetNumberOfSmoothingIterations(100)
    geo_reader.SetSmoothingFactor(0.1)
    geo_reader.Update()
    # image = geo_reader.GetOutput()
    # image = reader.GetOutput()
    # att_reader = vtkvmtk.vtkvmtkCenterlineAttributesFilter()
    # att_reader.SetInputData(geo_reader.GetOutput())
    # att_reader.SetAbscissasArrayName("Abscissas")
    # att_reader.SetParallelTransportNormalsArrayName("ParallelTransportNormals")  # ParallelTransportNormals
    # att_reader.Update()

    # transform = vtk.vtkTransform()
    # transform.Scale(1, 1, -1)
    #
    # transformFilter = vtk.vtkTransformPolyDataFilter()
    # transformFilter.SetInputData(att_reader.GetOutput())
    # transformFilter.SetTransform(transform)
    # transformFilter.Update()

    return geo_reader.GetOutput()
    # return reader.GetOutput()


def ReadCeterLineFile2(infile):
    if (infile == ''):
        print('Error: no InputFileName.')
    print('Reading VTK image file.')
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(infile)
    reader.Update()

    transform = vtk.vtkTransform()
    transform.Scale(1, 1, -1)

    transformFilter = vtk.vtkTransformPolyDataFilter()
    transformFilter.SetInputData(reader.GetOutput())
    transformFilter.SetTransform(transform)
    transformFilter.Update()

    return transformFilter.GetOutput()


def WriteVTKSurfaceFile(vtk_data, out_name):
    if (out_name == ''):
        print('Error: no OutputFileName.')
    print('Writing VTK XML image file.')
    # writer = vtk.vtkImageWriter()
    # writer = vtk.vtkStructuredPointsWriter()
    writer = vtk.vtkXMLImageDataWriter()
    writer.SetInputData(vtk_data)
    # print("MPR image", vtk_data)
    writer.SetFileName(out_name)
    # writer.Update()
    writer.Write()


class vmtkImageCurvedMPR(pypes.pypeScript):

    def __init__(self, image_path=None, ctr_path=None, out_file=""):

        pypes.pypeScript.__init__(self)

        self.Image = ReadVTKImageFile(image_path)
        # ReadVTKImageFile(image_path) or ReadNiiImageFile(image_path) or ReadDicomFile(image_path)
        # self.Image = ReadDicomFile(image_path)
        print("Input image\n", self.Image)
        self.Centerlines = ReadCeterLineFile(ctr_path)  # ReadCeterLineFile(ctr_path)
        print("CenterLines\n", self.Centerlines)
        self.NormalsArrayName = 'ParallelTransportNormals'  # ParallelTransportNormals
        self.FrenetTangentArrayName = 'FrenetTangent'  # FrenetTangent, FSTangents
        self.InplaneOutputSize = 100  # 100
        self.InplaneOutputSpacing = 1  # 输出图像的spacing
        self.ReslicingBackgroundLevel = 0.0  # 背景的颜色
        self.OutputFile = out_file

        self.SetScriptName('vmtkimagecurvedmpr')
        self.SetScriptDoc('Make an MPR image from a centerline and an input image')

        self.SetInputMembers([
            ['Image','i','vtkImageData',1,'','the input image','vmtkimagereader'],
            ['Centerlines','centerlines','vtkPolyData',1,'','the input centerlines','vmtksurfacereader'],
            ['NormalsArrayName','normalsarray','str',1,'','name of the array where parallel transport normals to the centerlines are stored'],
            ['InplaneOutputSize','size','int',1,'(1,)','size of the square in pixels that each resulting MPR image should have'],
            ['ReslicingBackgroundLevel','background','float',1,'','value of the pixels in the mpr image that are outside of the inputimage'],
            ['InplaneOutputSpacing','spacing','float',1,'(0.001,)','spacing between the pixels in the output MPR images'],
            ['FrenetTangentArrayName','frenettangentarray','str',1,'','name of the array where tangent vectors of the Frenet reference system are stored']
            ])
        self.SetOutputMembers([
            ['Image','o','vtkImageData',1,'','the output image','vmtkimagewriter']])

    def Execute(self):

        if self.Image == None:
            self.PrintError('Error: No input image.')

        if self.Centerlines == None:
            self.PrintError('Error: No input centerlines.')
   
        curvedMPRImageFilter = vtkvmtk.vtkvmtkCurvedMPRImageFilter()
        curvedMPRImageFilter.SetInputData(self.Image)
        curvedMPRImageFilter.SetCenterline(self.Centerlines)
        curvedMPRImageFilter.SetParallelTransportNormalsArrayName(self.NormalsArrayName)
        curvedMPRImageFilter.SetFrenetTangentArrayName(self.FrenetTangentArrayName)
        curvedMPRImageFilter.SetInplaneOutputSpacing(self.InplaneOutputSpacing, self.InplaneOutputSpacing)
        curvedMPRImageFilter.SetInplaneOutputSize(self.InplaneOutputSize, self.InplaneOutputSize)
        curvedMPRImageFilter.SetReslicingBackgroundLevel(self.ReslicingBackgroundLevel)
        curvedMPRImageFilter.Update()

        self.Image = curvedMPRImageFilter.GetOutput()
        # information = curvedMPRImageFilter.GetOutputInformation(0).Set(
        #     vtk.vtkStreamingDemandDrivenPipeline.UPDATE_EXTENT(),
        #     curvedMPRImageFilter.GetOutputInformation(0).Get(
        #         vtk.vtkStreamingDemandDrivenPipeline.WHOLE_EXTENT()
        #     ), 6
        # )
        # outInfo = curvedMPRImageFilter.Get(vtk.vtkStreamingDemandDrivenPipeline.WHOLE_EXTENT())
        print("MPR image\n", self.Image)
        # WriteVTKSurfaceFile(self.Image, self.OutputFile)
        # print("information\n", information)

        
if __name__=='__main__':

    # main = pypes.pypeMain()
    # main.Arguments = sys.argv
    # main.Execute()
    in_file = "D:/ZhongYang/vmtk_data/temp/334141.vti"
    # in_file = "D:/ZhongYang/vmtk_data/data/334141_1.2.840.113619.6.80.114374081799669.83084.1604475500705.1.nii.gz"
    # in_file = "D:/ZhongYang/vmtk_data/centerlines/334141"
    ctr_file = "D:/ZhongYang/vmtk_data/temp/334141_smooth_ctr.vtp"
    out_file = "D:/ZhongYang/vmtk_data/temp/334141_smooth_mpr.vti"
    curved_mpr = vmtkImageCurvedMPR(image_path=in_file, ctr_path=ctr_file, out_file=out_file)
    curved_mpr.Execute()
</code></pre>

---

## Post #3 by @ljhao303 (2023-05-29 07:12 UTC)

<p>hi,bro,Have you solved the above problems?  I had the same problem.</p>

---

## Post #4 by @lassoan (2023-05-30 01:12 UTC)

<p>You can use Curved Planar Reformat module in 3D Slicer’s Sandbox extension. It comes with convenient GUI and - very importantly - it provides and invertible straightening transform, which can be used for transforming any objects (images, points, curves, etc) between the original and straightened space. It is implemented in Python, so you can also port it to work outside Slicer, too.</p>

---

## Post #5 by @ljhao303 (2023-06-01 02:34 UTC)

<p>Could you please give me a demo Python script? That would be helpful.</p>

---

## Post #6 by @ljhao303 (2023-06-08 07:55 UTC)

<p>The issue has been resolved，recompile vmtk.</p>

---
