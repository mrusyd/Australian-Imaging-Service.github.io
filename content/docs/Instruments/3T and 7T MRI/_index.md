---
title: "MR Solutions 3T & 7T MRI"
linkTitle: "MR Solutions 3T & 7T MRI"
weight: 10
---

`[Series ID]` should be used for matching files.

The Project field should filled with the XNAT shortcode (EZBooking Project ID) and the Subject field will be filled with the project name.

{{% alert title="Note" %}}
For the new project created through DashR, the XNAT shortcode should be at least 3 digits/characters and less than 20 digits/characters. 

If less than 3 digits, zeros should be added at the beginning. For example, XNAT shortcode 044 for EZBooking Project ID 44
{{% /alert %}}


## Metadata

| Instrument Source                                       | Logic                      | Config Source                                            | XNAT Destination |
|---------------------------------------------------------|----------------------------|----------------------------------------------------------|------------------|
| (0010,0010)                                             | `[Project]:*`              | -                                                        | `[Project]`      |
| (0010,0010)                                             | `*:[Subject]`              | -                                                        | `[Subject]`      |
| (0008,0020)                                             | `[YYYYMMDD]`               |                                                          | `[Session]`      |
| (0008,0050)                                             | [Subject Accession Number] | -                                                        |                  |
| -                                                       | -                          | 3T: 10.25910/5cf9e65ffa8c4<br>7T: 10.25910/5cf9f821b4c94 | [IID] TBD        |
| -                                                       | -                          | TBD                                                      | [QCPID] TBD      |
| TBC                                                     | -                          | -                                                        | Date             |
| Timestamp (0008,0032) TBC                               | -                          | -                                                        | Time             |
| Acquisition Duration (0018,9073)                        | -                          | -                                                        | TBD              |
| Protocol Name (0018,1030)<br>/Sequence Name (0018,0024) | -                          | -                                                        | TBD              |
| -                                                       | -                          | -                                                        | Operator         |
| (0008,1010) Station Name                                | -                          | -                                                        | Scanner Name     |
| (0008,1090) Manufacturer’s Model Name                   | -                          | -                                                        | Scanner Type     |
| -                                                       | -                          | Sydney Imaging                                           | Acquisition Site |

## Data

| Original structure                                                               | Note                | XNAT structure       | XNAT File Type |
|----------------------------------------------------------------------------------|---------------------|----------------------|----------------|
| `D:\smis\dev\Data\[Subject ID]\DICOM\[Series]\[1]\[Series]_[ScanX]`            | DICOM               | `\Session\[Series]\` | DICOM          |
| `D:\smis\dev\Data\[Subject ID]\Image\[Series]\[1]\[Series]_[ScanX]`            | SUR                 | `\Session\[Series]\` | SUR            |
| `D:\smis\dev\Data\[Subject ID]\Image\[Series]\patient[SubjectID]_scan[Series]` | PET (log)           |                      |                |
| `D:\smis\dev\Data\[Subject ID]\Image\[Series]\[Reconstruction]\[Series]_stuff` | PET (Reconstructed) |                      |                |
| `D:\smis\dev\Data\[Subject ID]\Spectroscopy\[Series]\[Series]_0`               | Spectroscopy        | `\Session\[Series]\` | MRD, SPR       |
| `D:\smis\dev\MRD\[Subject ID]\Image\[Series]\[Series]_0`                       | MRD, RPR, rtv       | `\Session\[Series]\` | MRD, RPR       |
| `D:\smis\dev\MRD\[Subject ID]\Image\[Series]\[Series]_0_o`                     | MRD, RPR, rtv       | `\Session\[Series]\` | MRD, RPR       |
| `D:\smis\dev\MRD\[Subject ID]\Image\[Series]\btable.txt`                       | MRD, RPR, rtv       | `\Session\[Series]\` | btable         |
| `D:\smis\dev\MRD\[Subject ID]\Image\[Series]\rtable.txt`                       | MRD, RPR, rtv       | `\Session\[Series]\` | rtable         |
| `D:\smis\dev\PetRaw\[Subject ID]\[Series]\pet_[Series]`                        | PET (RAW)           |                      |                |
