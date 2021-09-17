---
title: "Siemens ARTIS pheno"
linkTitle: "Siemens ARTIS pheno"
weight: 10
---

## Metadata

| Instrument Source | Logic | Config Source          | XNAT Destination |
|-------------------|-------|------------------------|------------------|
|Additional Info field: Project:HT-003|(0010,4000) Patient’s Comments|(0010,4000) Patient’s Comments|Project: HT-003|
|Lastname:Mukherjee<br>Firstname:Sheep1<br>Title:|(0010,0010) Patient’s Name|(0010,0010) Patient’s Name|Subject: Mukherjee_sheep1|
|Patient ID: Patient01|(0010,0020) Patient ID|(0010,0020) Patient ID +<br>(0032,0012) Study ID Issuer|Session: Patient01_210301-15_47_19-DST-IVS|
|                   | (0020,0010) Study UID      |    (0020,0010) Study UID           |         SCAN ID: 990         |
|                   |       | 10.25910/5cf9f821b4c94 | `[IID]` TBD      |
|                   |       |                        | `[QCPID]` TBD    |

`[Path]` needs to be determined. It can be on instrument, or the export location on RDS.

## Data

| Original structure   | Note                          | XNAT structure |
|----------------------|-------------------------------|----------------|
| `[Path]//[File].jpg` | To be covered with DICOM2JPEG | Resource file  |
| `[Path]//[File].avi` |                               | Resource file  |
| `[Path]//[File].txt` |                               | Resource file  |
| `[Path]//[File].csv` |                               | Resource file  |
