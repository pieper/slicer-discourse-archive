# How to determine the temporal resolution using DICOM Header Information in perfusion MRI ?

**Topic ID**: 6613
**Date**: 2019-04-26
**URL**: https://discourse.slicer.org/t/how-to-determine-the-temporal-resolution-using-dicom-header-information-in-perfusion-mri/6613

---

## Post #1 by @inesben (2019-04-26 02:27 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2019-04-26 12:56 UTC)

<p>There is no general solution. Scanner manufacturers (especially of pre-clinical devices) misinterpret/misuse the DICOM standard in various ways, so you need to figure out a way that works for your particular system.</p>
<p>We <a href="https://na-mic.github.io/ProjectWeek/PW28_2018_GranCanaria/Projects/PreclinicalDataImport/" rel="nofollow noopener">worked a bit on this at a project week last year</a> but we did not create a module that could solve this.</p>
<p>Probably your best bet is to give more information about your scanner, preferable also a sample data set, and hopefully one of the experts can give you more specific advice.</p>
<p><a class="mention" href="/u/speled">@speled</a></p>

---

## Post #3 by @inesben (2019-04-26 14:29 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="6613">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There is no general solution. Scanner manufacturers (especially of pre-clinical devices) misinterpret/misuse the DICOM standard in various ways, so you need to figure out a way that works for your particular system.</p>
<p>We <a href="https://na-mic.github.io/ProjectWeek/PW28_2018_GranCanaria/Projects/PreclinicalDataImport/" rel="noopener nofollow ugc">worked a bit on this at a project week last year</a> but we did not create a module that could solve this.</p>
<p>Probably your best bet is to give more information about your scanner, preferable also a sample data set, and hopefully one of the experts can give you more specific advice.</p>
</blockquote>
</aside>
<p>Thank you very much for your response.<br>
please find attached the DICOM header information.<br>
FileModDate: ‘22-nov.-2017 19:23:24’<br>
FileSize: 113934<br>
Format: ‘DICOM’<br>
FormatVersion: 3<br>
Width: 128<br>
Height: 128<br>
BitDepth: 12<br>
ColorType: ‘grayscale’<br>
FileMetaInformationGroupLength: 208<br>
FileMetaInformationVersion: [2×1 uint8]<br>
MediaStorageSOPClassUID: ‘1.2.840.10008.5.1.4.1.1.4’<br>
MediaStorageSOPInstanceUID: ‘1.3.12.2.1107.5.2.36.40551.2016121411251097746349710’<br>
TransferSyntaxUID: ‘1.2.840.10008.1.2.1’<br>
ImplementationClassUID: ‘1.2.276.0.7230010.3.0.3.5.4’<br>
ImplementationVersionName: ‘OFFIS_DCMTK_354’<br>
SourceApplicationEntityTitle: ‘DCF’<br>
SpecificCharacterSet: ‘ISO_IR 100’<br>
ImageType: ‘ORIGINAL\PRIMARY\PERFUSION\NONE\ND’<br>
InstanceCreationDate: ‘20161214’<br>
InstanceCreationTime: ‘112534.031000’<br>
SOPClassUID: ‘1.2.840.10008.5.1.4.1.1.4’<br>
SOPInstanceUID: ‘1.3.12.2.1107.5.2.36.40551.2016121411251097746349710’<br>
StudyDate: ‘20161214’<br>
SeriesDate: ‘20161214’<br>
AcquisitionDate: ‘20161214’<br>
ContentDate: ‘20161214’<br>
StudyTime: ‘105858.875000’<br>
SeriesTime: ‘112534.031000’<br>
AcquisitionTime: ‘112510.545000’<br>
ContentTime: ‘112534.031000’<br>
AccessionNumber: ‘’<br>
Modality: ‘MR’<br>
Manufacturer: ‘SIEMENS’<br>
ReferringPhysicianName: [1×1 struct]<br>
StationName: ‘MRC’<br>
StudyDescription: ‘I-N-Neuro^CEREBRALE’<br>
SeriesDescription: ‘ep2d_perf+++’<br>
InstitutionalDepartmentName: ‘Department’<br>
PerformingPhysicianName: [1×1 struct]<br>
ManufacturerModelName: ‘Verio’<br>
ReferencedImageSequence: [1×1 struct]<br>
DerivationDescription: ‘LossLess compression with JPEG 2K, compression ratio 2.7103’<br>
DerivationCodeSequence: [1×1 struct]<br>
PatientID: ‘5859’<br>
ContrastBolusAgent: ‘+ INJECTION’<br>
ScanningSequence: ‘EP’<br>
SequenceVariant: ‘SK’<br>
ScanOptions: ‘PFP\FS’<br>
MRAcquisitionType: ‘2D’<br>
SequenceName: ‘<em>epfid2d1_128’<br>
AngioFlag: ‘N’<br>
SliceThickness: 4<br>
RepetitionTime: 2.8919e+03<br>
EchoTime: 45<br>
NumberOfAverages: 1<br>
ImagingFrequency: 123.2449<br>
ImagedNucleus: ‘1H’<br>
EchoNumber: 1<br>
MagneticFieldStrength: 3<br>
SpacingBetweenSlices: 5.2000<br>
NumberOfPhaseEncodingSteps: 112<br>
EchoTrainLength: 1<br>
PercentSampling: 100<br>
PercentPhaseFieldOfView: 100<br>
PixelBandwidth: 1502<br>
DeviceSerialNumber: ‘40551’<br>
SoftwareVersion: ‘syngo MR B17’<br>
ProtocolName: ‘ep2d_perf+++’<br>
ContrastBolusVolume: 0<br>
ContrastBolusTotalDose: 0<br>
ContrastBolusIngredient: ‘’<br>
ContrastBolusIngredientConcentration: 0<br>
TransmitCoilName: ‘Body’<br>
AcquisitionMatrix: [4×1 uint16]<br>
InPlanePhaseEncodingDirection: ‘COL’<br>
FlipAngle: 90<br>
VariableFlipAngleFlag: ‘N’<br>
SAR: 0.0367<br>
dBdt: 0<br>
PatientPosition: ‘HFS’<br>
Private_0019_10xx_Creator: ‘SIEMENS MR HEADER’<br>
Private_0019_1008: ‘IMAGE NUM 4’<br>
Private_0019_1009: ‘1.0’<br>
Private_0019_100b: 82.5000<br>
Private_0019_100f: 'Fast</em>’<br>
Private_0019_1011: ‘No’<br>
Private_0019_1012: [3×1 int32]<br>
Private_0019_1013: [3×1 int32]<br>
Private_0019_1014: [3×1 double]<br>
Private_0019_1015: [3×1 double]<br>
Private_0019_1016: 0<br>
Private_0019_1017: 1<br>
Private_0019_1018: 2600<br>
Private_0019_1028: 10.4170<br>
StudyInstanceUID: ‘1.3.12.2.1107.5.2.36.40551.30000016121406161846800000022’<br>
SeriesInstanceUID: ‘1.3.12.2.1107.5.2.36.40551.2016121411250039285449704.0.0.0’<br>
StudyID: ‘1’<br>
SeriesNumber: 18<br>
AcquisitionNumber: 1<br>
InstanceNumber: 1<br>
ImagePositionPatient: [3×1 double]<br>
ImageOrientationPatient: [6×1 double]<br>
FrameOfReferenceUID: ‘1.3.12.2.1107.5.2.36.40551.1.20161214110419734.0.0.0’<br>
PositionReferenceIndicator: ‘’<br>
SliceLocation: -56.9148<br>
SamplesPerPixel: 1<br>
PhotometricInterpretation: ‘MONOCHROME2’<br>
Rows: 128<br>
Columns: 128<br>
PixelSpacing: [2×1 double]<br>
BitsAllocated: 16<br>
BitsStored: 12<br>
HighBit: 11<br>
PixelRepresentation: 0<br>
SmallestImagePixelValue: 0<br>
LargestImagePixelValue: 1612<br>
WindowCenter: 317<br>
WindowWidth: 706<br>
RescaleIntercept: 0<br>
RescaleSlope: 1<br>
RescaleType: ‘US’<br>
WindowCenterWidthExplanation: ‘Algo1’<br>
Private_0029_10xx_Creator: ‘SIEMENS CSA HEADER’<br>
Private_0029_11xx_Creator: ‘SIEMENS MEDCOM HEADER2’<br>
Private_0029_1008: ‘IMAGE NUM 4’<br>
Private_0029_1009: ‘20161214’<br>
Private_0029_1010: [9472×1 uint8]<br>
Private_0029_1018: ‘MR’<br>
Private_0029_1019: ‘20161214’<br>
Private_0029_1020: [68276×1 uint8]<br>
Private_0029_1160: ‘com’<br>
RequestedProcedureDescription: ‘I-N-Neuro CEREBRALE’<br>
StudyComments: ‘AVC i OLEA’<br>
PerformedProcedureStepStartDate: ‘20161214’<br>
PerformedProcedureStepStartTime: ‘105858.906000’<br>
PerformedProcedureStepID: ‘MR20161214105858’<br>
PerformedProcedureStepDescription: ‘I-N-Neuro^CEREBRALE’<br>
Private_0051_10xx_Creator: ‘SIEMENS MR HEADER’<br>
Private_0051_1008: ‘IMAGE NUM 4’<br>
Private_0051_1009: ‘1.0’<br>
Private_0051_100a: ‘TA 00.08’<br>
Private_0051_100b: ‘128p<em>128’<br>
Private_0051_100c: 'FoV 230</em>230’<br>
Private_0051_100d: ‘SP F56.9’<br>
Private_0051_100e: ‘Tra&gt;Sag(-6.0)&gt;Cor(-4.9)’<br>
Private_0051_100f: ‘C:HEA;HEP;NE1,2’<br>
Private_0051_1012: ‘TP 0’<br>
Private_0051_1013: ‘+LPH’<br>
Private_0051_1015: ‘R’<br>
Private_0051_1016: ‘PERFUSION/NONE/ND’<br>
Private_0051_1017: ‘SL 4.0’<br>
Private_0051_1019: ‘A1/PFP/FS’</p>
<p>Best regards.</p>

---
