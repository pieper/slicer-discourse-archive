---
topic_id: 27447
title: "Cli For Processing Markdown Based Project Pages"
date: 2023-01-24
url: https://discourse.slicer.org/t/27447
---

# CLI for processing markdown-based project pages

**Topic ID**: 27447
**Date**: 2023-01-24
**URL**: https://discourse.slicer.org/t/cli-for-processing-markdown-based-project-pages/27447

---

## Post #1 by @jcfr (2023-01-24 20:42 UTC)

<p>Following this morning discussion, this topic aims to discuss possible way to streamline the update of the project listed on the top-level page associated with each event.</p>

---

## Post #2 by @Sam_Horvath (2023-01-24 20:48 UTC)

<p>Yay!</p>
<p>Metadata of interest for the main page:</p>
<ul>
<li>Project title</li>
<li>Contributor list</li>
<li>Presenter</li>
<li>Main page category</li>
<li>On site vs. remote</li>
</ul>

---

## Post #3 by @jcfr (2023-01-24 21:48 UTC)

<h2><a name="p-89481-projectweek-cli-1" class="anchor" href="#p-89481-projectweek-cli-1" aria-label="Heading link"></a>ProjectWeek CLI</h2>
<p>Here is a python script allowing to parse a collection of <code>README.md</code> files associated with projects and generate the list of links to add to the top-level page.</p>
<p>See <a href="https://github.com/jcfr/ProjectWeekCLI" class="inline-onebox">GitHub - jcfr/ProjectWeekCLI: CLI for processing project week mardown-based documents.</a></p>
<p>It currently extracts:</p>
<ul>
<li>project title</li>
<li>key investigators</li>
</ul>
<p><strong>Running the CLI</strong></p>
<pre><code class="lang-auto">project_week=$HOME/Projects/ProjectWeek/PW38_2023_GranCanaria
project_week_cli=$HOME/Projects/ProjectWeekCLI/project_week_cli.py

(\
  cd ${project_week}/Projects/;  \
  fd README.md -a -i -exec python3 ${project_week_cli} {} \
)
</code></pre>
<details><summary>Example of output</summary><pre>1. [DATSCAN Viewer implementation in OHIF](Projects/OHIF_DATSCAN/README.md) (Salim Kanoun MD, Alireza Sedghi, Celian Abadie, Sofien Sellamo)
1. [Simple DICOM Query/Retrieve Panel](Projects/SimpleDICOMQueryRetrievePanel/README.md) (Davide Punzo, Andras Lasso, Anyone is welcome to join)
1. [Development of Anatomy Atlases and Training Tools with 3D Slicer and Open Source Software](Projects/TTTAtlas/README.md) (Juan Ruiz, Idafen Santana, Mario Monzón)
1. [Cross study sychronizer for OHIF Crosshair](Projects/OHIF_SyncCrosshair/README.md) (Salim Kanoun MD, Alireza Sedghi, Celian Abadie, Sofien Sellamo)
1. [Histology Data and Models Into IDC](Projects/HistologyIntoIDC/README.md) (Curtis Lisle, Andrey Fedorov, others welcome)
1. [Taking Advantage of Open Source Technologies for the Development of Clinical Simulation Centers and Virtual Hospitals for Training and R&amp;D](Projects/OpenSourceSimulationCenter/README.md) (Juan Ruiz, Idafen Santana, Mario Monzón)
1. [MHub Integration](Projects/MHub_Integration/README.md) (Leonard Nürnberg, Dennis Bontempi, Andrey Fedorov)
1. [Transitioning 3D Slicer to QSS Styling](Projects/SlicerQSS/README.md) (Investigator 1, Investigator 2, Investigator 3)
1. [Mesh Comparison](Projects/MeshComparison/README.md) (Paolo Zaffino, Maria Francesca Spadea, Michela Destito, Amerigo Giudice, the clinical mind behind the idea, Anyone who wants to join)
1. [DICOM Segmentation Optimization](Projects/DICOMSEG/README.md) (Steve Pieper, Andrey Fedorov, Andras Lasso, Marco Nolden, Hans Meine, Alireza Sedghi, Erik Ziegler, Markus Hermann, Chris Bridge, David Clunie)
1. [Write full project title here](Projects/IDC DICOM WSI workflow/README.md) (Maximilian Fischer, Andrey Fedorov, Marco Nolden, Philipp Schader, David Clunie, Daniela Schacherer, André Homeyer)
1. [Maxillofacial Surgery Virtual Planning Applications based on Slicer](Projects/Slicer4MaxillofacialSurgery/README.md) (Miguel Ángel Rodriguez-Florido, PhD, Christian Buritica, MD)
1. [Integration of desktop apps](Projects/KaapanaIntegrationOfDesktopApps/README.md) (Hanno Gao, Klaus Kades)
1. [SlicerPipelines](Projects/SlicerPipelines/README.md) (Connor Bowley, Sam Horvath)
1. [New 3D Slicer extension for the YEB Atlas.](Projects/AtlasYEB_Plugin_WEB_API/README.md) (Sara Fern, ez Vidal, Eric Bardinet, Severine Ch, elier)
1. [3D Slicer Internationalization](Projects/3DSlicerInternationalization/README.md) (Sonia Pujol, Steve Pieper, Andras Lasso, Mamadou Camara, Mouhamed DIOP, Adama Wade, Mohamed Alalli Bilal, Adriana H. Vilchis González, Luiz Otavio Murta Junior)
1. [Training system for US-guided lung interventions](Projects/US-guided_TrainingSystem/README.md) (Natalia Arteaga Marrero, David García Mato, Javier González Fernández)
1. [Data and model exchange across different sources](Projects/KaapanaDataAndModelExchangeAcrossDifferentSources/README.md) (Benjamin Hamm, Ünal Akünal, Markus Bujotzek, Klaus Kades)
1. [Multi-stage dental segmentation using MONAI Label](Projects/TeethSegmentation/README.md) (David García Mato, Yucheng Tang, Andres Diaz Pinto, Daniel Palkovics, Csaba Pinter, Attila Nagy)
1. [Slicer + IMSTK for low cost training setups](Projects/SlicerIMSTK/README.md) (Investigator 1, Investigator 2, Investigator 3)
1. [SlicerAstro Update](Projects/SlicerAstroUpdate/README.md) (Davide Punzo, Thijs van der Hulst, Anyone is welcome to join)
1. [Measurement Panel](Projects/MeasurementPanel/README.md) (Davide Punzo, Andras Lasso, Anyone is welcome to join)
1. [How-to setup and run 3D Slicer on an AWS cloud server](Projects/SlicerCloud/README.md) (Rudolf Bumm, Steve Pieper, Gang Fu, Qing Liu)
1. [3DSlicerHub](Projects/SlicerHub/README.md) (Rafael Nebot, Paula Moreno, Juan Ruiz, Idafen Santana)
1. [Automated Standardized Orientation for Cone-Beam Computed Tomography (CBCT)](Projects/ASO_CBCT/README.md) (Luc Anchling, Nathan Hutin, Maxime Gillot, Baptiste Baquero, Jonas Bianchi, Antonio Ruellas, Felicia Mir, a, Selene Barone, Marcela Gurgel, Marilia Yatabe, Najla Al Turkestani, Hina Joshi, Lucia Cevidanes, Juan Prieto)
1. [Conversion of MONAI Label trained network into a MONAI bundle](Projects/MONAILabel2bundle/README.md) (Deepa Krishnaswamy, Cosmin Ciausu, Nazim Haouchine, Andres Diaz-Pinto, Jesse Tetreault, Roya Hajavi, Stephen Aylward, Steve Pieper, Andrey Fedorov)
1. [ Key Investigators](Projects/AutomaticQuantitative3DCephalometrics/README.md) (Nathan Hutin, Luc Anchling, Baptiste Baquero, Maxime Gillot, Lucia Cevidanes, David Allemang, Jean-Christophe Fillion-Robin)
1. [Using VolView with data in Google Storage buckets / IDC buckets](Projects/IDC_with_VolView/README.md) (Andrey Fedorov, Forrest Li, Stephen Aylward)
1. [HOWTO: Detection of prostate cancer in IDC images using MONAI prostate_mri_anatomy model](Projects/MONAI_IDC_PCa_detection/README.md) (Cosmin Ciausu, Deepa Krishnaswamy, Patrick Remerscheid, Tina Kapur, S, y Wells, Andrey Fedorov, Khaled Younis)
1. [Real-time visualization for transcranial magnetic stimulation (TMS)](Projects/SlicerTMS/README.md) (Loraine Franke, Jax Luo, Yogesh Rathi, Lipeng Ning, Steve Pieper, Daniel Haehn)
1. [Automatic Landmark Identification in Cranio-Facial CBCT](Projects/ALI_CBCT/README.md) (Luc Anchling, Nathan Hutin, Maxime Gillot, Baptiste Baquero, Jonas Bianchi, Marcela Gurgel, Najla Al Turkestani, Marilia Yatabe, Lucia Cevidanes, Juan Prieto)
1. [Kaapana related experiments/discussions/collaboratons](Projects/Kaapana_overall/README.md) (Andrey Fedorov, Marco Nolden, Hans Meine, Klaus Kades)
1. [Integration of clinical data into medical imaging pipelines](Projects/KaapanaClinicalData/README.md) (Philipp Schader, anyone is welcome to join)
1. [Systole OS: an operating system for development/deployment of medical devices.](Projects/SystoleOS/README.md) (Rafael Palomar, Steve Pieper)
1. [Automated Landmarking Support](Projects/AutomatedLandmarkingSupport/README.md) (Sara Rolfe, Chi Zhang, Murat Maga, Steve Pieper, Andras Lasso)
1. [Surface Nets 3D Slicer Implementation](Projects/SurfaceNets/README.md) (Andy Huynh, Gerry Gralton, Benjamin Zwick, Open to anyone interested!)
1. [Setting up University Courses on Computer Assisted Medical Imaging, Manufacturing and Interventions using Open Source Technologies and 3D Slicer](Projects/CoursesMedicalImaging/README.md) (Juan Ruiz, Idafen Santana, Mario Monzón)
1. [Automatic multi-anatomical skull structure segmentation of cone-beam computed tomography scans using 3D UNETR](Projects/AMASSS_CBCT/README.md) (Luc Anchling, Nathan Hutin, Maxime Gillot, Baptiste Baquero, Celia Le, Romain Deleat-Besson, Jonas Bianchi, Antonio Ruellas, Marcela Gurgel, Marilia Yatabe, Najla Al Turkestani, Kayvan Najarian, Reza Soroushmehr, Steve Pieper, Ron Kikinis, Beatriz Paniagua, Jonathan Gryak, Marcos Ioshida, Camila Massaro, Liliane Gomes, Heesoo Oh, Karine Evangelista, Cauby Chaves Jr, Daniela Garib, F ́abio Costa, Erika Benavides, Fabiana Soki, Jean-Christophe Fillion-Robin, Hina Joshi, Lucia Cevidanes, Juan Prieto)
1. [Active Viewport](Projects/ActiveViewport/README.md) (Davide Punzo, Andras Lasso, Anyone is welcome to join)
1. [Slicer-Liver](Projects/SlicerLiver/README.md) (Rafael Palomar, Gabriella d'Albenzio, Ruoyan Meng, Ole Vegard Solberg, Geir Arne Tangen)
1. [3D Slicer Lung CT Segmentation](Projects/LungSegmentation/README.md) (Rudolf Bumm, Ron Kikinis, Raúl San José Estépar, Steve Pieper, Eserval Rocha jr, Andras Lasso, Curtis Lisle)
1. [Automatic Standardize Orientation IOS](Projects/AutomaticStandardizeOrientation_IOS/README.md) (Nathan Hutin, Luc Anchling, Marcela Gruge, Felicia Mir, a, Najla Al Turkestani, Selene Barone, Lucia Cevidanes, Juan Prieto)
1. [FAIRification of medical imaging data and analysis tools](Projects/Metadata_IDC_HMC/README.md) (Marco Nolden, Andrey Fedorov)
1. [AR in Slicer](Projects/ARinSlicer/README.md) (Alicia Pose Díez de la Lastra, Javier Pascau, Gabor Fichtinger, Andras Lasso, Adam Rankin, Csaba Pinter, Lucas G, el, Jean-Christophe Fillion-Robin, Simon Drouin)
1. [Real-time ultrasound AI segmentation using Tensorflow and PyTorch models](Projects/RealTimeUltrasoundSegmentationAI/README.md) (María Rosa Rodríguez Luque, Tamas Ungi, David García Mato)
1. [Connecting/Using Kaapana to Google Cloud/Google Health/Google FHIR](Projects/KaapanaConnectingKaapanaToGoogleCloudAndHealthAndFHIR/README.md) (Jonas Scherer)
1. [Electrophysiological biosignals in 3D Slicer: a case of EMG to control 3D models](Projects/Electrophysiological biosignals in 3D Slicer/README.md) (Jordan Ortega Rodríguez)
1. [SlicerVR - Restore Interactions](Projects/SlicerVRInteractions/README.md) (Csaba Pintér, Simon Drouin, Andrey Titov, YOU)
1. [Fetal Ultrasound Simulation for Delivery Training](Projects/FetalUltrasoundSimulation/README.md) (Felix von Haxthausen, David García Mato, Tolga-Can Çallar, José Carlos Mateo Pérez)
1. [Fast viewing and tagging of DICOM Images](Projects/KaapanaFastViewingAndTaggingOfDICOMImages/README.md) (Stefan Denner, Klaus Kades)
1. [Parameter Node Wrapper](Projects/ParameterNodeWrapper/README.md) (Connor Bowley, Sam Horvath, David Allemang)
1. [NCI Imaging Data Commons Tutorial / Workshop](Projects/IDC_Tutorial/README.md) (Andrey Fedorov, Deepa Krishnaswamy, Cosmin Ciausu, Vamsi Thiriveedhi, Dennis Bontempi, Leonard Nuerenberg)
1. [DICOM Segmentation Optimization](Projects/DICOMSEG/README.md) (Steve Pieper, Andrey Fedorov, Andras Lasso, Marco Nolden, Hans Meine, Alireza Sedghi, Erik Ziegler, Markus Hermann, Chris Bridge, David Clunie)
</pre></details>
<p><strong>Prerequisites</strong></p>
<pre><code class="lang-auto">cd $HOME/Projects

# Download project week files
git clone --depth=1 --branch master https://github.com/NA-MIC/ProjectWeek.git

#  Install the CLI
git clone https://github.com/jcfr/ProjectWeekCLI.git
</code></pre>
<h3><a name="p-89481-questions-suggestions-2" class="anchor" href="#p-89481-questions-suggestions-2" aria-label="Heading link"></a>Questions &amp; suggestions</h3>
<p><em>Based on prior work done by <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></em></p>
<h4><a name="p-89481-how-to-associate-category-with-project-page-3" class="anchor" href="#p-89481-how-to-associate-category-with-project-page-3" aria-label="Heading link"></a>How to associate category with project page ?</h4>
<p>I suggest to add a  category section to the project page.</p>
<p>For example:</p>
<pre><code class="lang-auto"># AR in Slicer

## Category

* VR/AR and Rendering

## Key Investigators

- Alicia Pose Díez de la Lastra (Universidad Carlos III de Madrid, Madrid, Spain) - [Presenter]
- Javier Pascau (Universidad Carlos III de Madrid, Madrid, Spain)
- Gabor Fichtinger (PerkLab, Queen's University , Kingston , Canada)
</code></pre>
<h4><a name="p-89481-how-to-label-on-site-vs-remote-in-the-top-level-list-4" class="anchor" href="#p-89481-how-to-label-on-site-vs-remote-in-the-top-level-list-4" aria-label="Heading link"></a>How to label <code>On site</code> vs <code>Remote</code> in the top-level list ?</h4>
<p>If at least one attendee is labelled as <code>In-person &amp; confirmed</code> in the <code>Registrants</code> list, label the project as <code>On site</code></p>
<p>Note that parsing the <code>Registrants</code> list would be straightforward.</p>
<h4><a name="p-89481-how-to-identify-the-presenter-5" class="anchor" href="#p-89481-how-to-identify-the-presenter-5" aria-label="Heading link"></a>How to identify the presenter ?</h4>
<p>The first <code>In-person &amp; confirmed</code> investigator is the presenter</p>
<p>If all investigators are <code>online</code>, the first one of the list is labelled as the presenter.</p>
<h4><a name="p-89481-name-check-6" class="anchor" href="#p-89481-name-check-6" aria-label="Heading link"></a>Name check ?</h4>
<p>The CLI could report warnings if name listed are not found in the <code>Registrants</code> list</p>

---

## Post #4 by @Sam_Horvath (2023-01-24 21:54 UTC)

<p>Re: names not on registration list,  I think it is somewhat common for collaborators who are not attending to still be credited by the project week attendee in the project pages</p>

---
