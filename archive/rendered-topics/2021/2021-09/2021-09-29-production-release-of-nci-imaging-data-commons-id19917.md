# Production release of NCI Imaging Data Commons

**Topic ID**: 19917
**Date**: 2021-09-29
**URL**: https://discourse.slicer.org/t/production-release-of-nci-imaging-data-commons/19917

---

## Post #1 by @fedorov (2021-09-29 18:31 UTC)

<p><a href="https://imaging.datacommons.cancer.gov/">NCI Imaging Data Commons</a> team is happy to announce the production release of the platform!</p>
<p><strong>The main highlights of the production release</strong>:</p>
<ul>
<li>the amount of data available increased from ~1TB in the initial pilot release to &gt;16TB</li>
<li>support for digital pathology added</li>
<li>introduction of versioning to support reproducible science</li>
<li>examples of use cases released to the community</li>
<li>API for programmatic access to cohorts</li>
</ul>
<p><strong>Details on the major milestones and improvements that were accomplished by <span class="mention">@IDC_team</span> in less than 12 months since the initial introduction of the IDC pilot</strong>:</p>
<ul>
<li>the number of <a href="https://imaging.datacommons.cancer.gov/collections/">collections available in IDC</a> increased from 27 (~1TB) to 113 (&gt;16TB of data)
<ul>
<li>
<a href="https://doi.org/10.7937/TCIA.hmq8-j677">National Lung Screening Trial (NLST) collection</a> ( &gt;26K patients, &gt;73K studies, &gt;11TB in size) is now <a href="https://imaging.datacommons.cancer.gov/explore/?filters_for_load=%5B%7B%22filters%22:%5B%7B%22id%22:%22120%22,%22values%22:%5B%22nlst%22%5D%7D%5D%7D%5D">available in IDC</a>!</li>
</ul>
</li>
<li>we added support for DICOM digital pathology
<ul>
<li>digital pathology component of the two of the CPTAC collections, <a href="https://imaging.datacommons.cancer.gov/explore/?filters_for_load=%5B%7B%22filters%22:%5B%7B%22id%22:%22120%22,%22values%22:%5B%22cptac_lscc%22%5D%7D%5D%7D%5D">CPTAC-LSCC</a> and <a href="https://imaging.datacommons.cancer.gov/explore/?filters_for_load=%5B%7B%22filters%22:%5B%7B%22id%22:%22120%22,%22values%22:%5B%22cptac_luad%22%5D%7D%5D%7D%5D">CPTAC-LUAD</a> were converted into the <a href="https://learn.canceridc.dev/dicom/dicom-tiff-dual-personality-files">DICOM/TIFF dual personality format</a> and are included in the release</li>
<li>open source <a href="https://github.com/MGHComputationalPathology/slim">SliM viewer</a> is now integrated with IDC to support <a href="https://viewer.imaging.datacommons.cancer.gov/slim/studies/1.3.6.1.4.1.5962.99.1.2463087261.2121647220.1625960757917.3.0/series/1.3.6.1.4.1.5962.99.1.2463087261.2121647220.1625960757917.2.0">visualization of DICOM Slide Microscopy modality</a>
</li>
</ul>
</li>
<li>we added support for <a href="https://learn.canceridc.dev/data/data-versioning">IDC data versioning</a>, which means you will always be able to access the precise set of files you used in your analysis as defined by DICOM <code>SOPInstanceUID</code>s that are unique and resolvable within IDC, or <a href="https://learn.canceridc.dev/data/organization-of-data/guids-and-uuids">CRDC Globally Unique Identifiers (GUIDs)</a>, even if the collection(s) containing those files has been updated</li>
<li>a number of analysis use cases have been developed, and are now <a href="https://github.com/ImagingDataCommons/IDC-Examples/tree/master/notebooks">available as Colab Notebooks</a> demonstrating examples of how IDC data can be analyzed on the cloud
<ul>
<li>
<a href="https://github.com/ImagingDataCommons/IDC-Examples/blob/master/notebooks/nsclc-radiomics/nsclc_radiomics_demo_release.ipynb">DeepPrognosis use case</a> - replication study, 2 year survival score of NSCLC patients</li>
<li>
<a href="https://github.com/ImagingDataCommons/IDC-Examples/blob/master/notebooks/lung_nodules_demo.ipynb">Lung Nodules segmentation and prognosis use case</a> - NSCLC patients nodules segmentation (nnU-Net) and prognosis (DeepPrognosis)</li>
<li>
<a href="https://github.com/ImagingDataCommons/IDC-Examples/blob/master/notebooks/thoracic_oar_demo.ipynb">Thoracic Organs at Risk segmentation use case</a> - NSCLC patients thoracic OAR segmentation (nnU-Net)</li>
<li>
<a href="https://github.com/ImagingDataCommons/idc-pathomics-use-case-1/blob/master/cptac_use_case.ipynb">Tissue classification in slide microscopy images</a> - this tutorial builds on the publication “Classification and mutation prediction from non–small cell lung cancer histopathology images using deep learning” (<a href="https://doi.org/10.1038/s41591-018-0177-5">Coudray et al., 2018</a>), one of the most cited pathomics publications in recent years</li>
</ul>
</li>
<li>
<a href="https://learn.canceridc.dev/api/getting-started">IDC API</a> is now live, enabling programmatic access to the functionality available through the IDC portal, including authenticated operations with IDC cohorts. IDC API complements Google BigQuery and Cloud Storage APIs that are available to query IDC metadata tables and retrieve files hosted in IDC</li>
<li>numerous features and bug fixes were implemented in IDC Portal; most prominently, <a href="https://learn.canceridc.dev/portal/data-exploration-and-cohorts/understanding-cohorts#viewing-the-cohorts-list">cohorts support was enhanced by integrating with IDC data versioning</a> - no matter what version of IDC data you used to form your cohort, you will always be able to export the manifest, or apply the cohort filter to the current IDC data version</li>
<li>we added various examples demonstrating how Google Cloud tools can be used to enable exploration and analysis of IDC data, and reproducibility in AI reserch. You can learn how to
<ul>
<li><a href="https://learn.canceridc.dev/cookbook/virtual-machines/idc-desktop">set up a GCP Compute Engine VM with the desktop interface to 3D Slicer</a></li>
<li>
<a href="https://learn.canceridc.dev/cookbook/data-studio/cohort-dashboard">use Google DataStudio to build a highly customizable dashboard</a> to explore metadata related to your cohort beyond what can be done with IDC portal, see live dashboard <a href="https://datastudio.google.com/reporting/ab96379c-e134-414f-8996-188e678f1b70/page/KHtxB/preview">here</a>
</li>
<li>
<a href="https://learn.canceridc.dev/cookbook/bigquery">use BigQuery and SQL</a> to get quick access to all of the DICOM metadata extracted from the 36+ <em>million</em> (and counting) DICOM instances available in IDC</li>
</ul>
</li>
<li>IDC implemented security controls and gained Authority to Operate at the Federal Information Security Modernization Act (FISMA) Low level</li>
<li>our launch of the <a href="https://learn.canceridc.dev/introduction/requesting-gcp-cloud-credits">IDC pilot cloud credit program</a> was successful, with a growing number of community members onboarded and using IDC credit allocation for their research (you can see some highlights of this work presented by IDC users in the <a href="https://youtu.be/9Ei1c0PNyDk">recording of the “Infrastructure and Standards” session</a> at SIIM Conference on Machine Intelligence in Medical Imaging 2021,<br>
session)</li>
<li>we had numerous presentations and tutorials at such venues as <a href="https://data4miccai.github.io/">MICCAI</a>, <a href="https://youtube.com/playlist?list=PLhawVWNiPvwaK6iSWvmkk4mKxTVsj_5Uq">RSNA</a>, ASTRO, AAPM, <a href="https://youtu.be/9Ei1c0PNyDk">SIIM CMIMI</a>, <a href="https://www.youtube.com/watch?v=RUBKZoWNTfc">NCI Imaging Community webinar</a>
</li>
<li>we published an <a href="http://dx.doi.org/10.1158/0008-5472.CAN-21-0950">open access manuscript</a> with the overview and vision for IDC role in the community, accompanied by <a href="https://www.youtube.com/playlist?list=PLhawVWNiPvwb2H0D9UTOIL23bc5DuDJRu">demonstration videos</a> highlighting some of the key functions of the system</li>
</ul>
<p><strong>We need input from YOU to guide our development!</strong></p>
<p>Please give IDC a try: we have <a href="https://learn.canceridc.dev/introduction/requesting-gcp-cloud-credits">free cloud credits</a> to help you get started. We welcome you to join our community and help us build this resource to benefit cancer research.</p>

---
