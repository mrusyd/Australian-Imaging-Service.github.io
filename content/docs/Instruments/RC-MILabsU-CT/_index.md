---
title: "RC MILabsU-CT"
linkTitle: "MILabs U-CT"
weight: 10
---

The microCT data needed to be transferred to the RDS before uploading from RDS to XNAT. Both XNAT and RDS will keep a copy of microCT
data at the current stage. If RDS storage researches its maximum capacity or budget in the future, the microCT data on RDS will be removed
periodically to save the space.

The microCT data can be categorized into three types: raw data, temporary data and reconstructed data.

The raw data is saved on the acquisition computer, and in the D drive of the reconstruction computer.

The temporary data is generated in the reconstruction process including the "corr" and "prev" folder of each scan and saved in the "ct-data"
folder. "corr" folder contains all the projection correction files, while "prev" folder contains the single slice preview image of reconstruction. "corr"
and "prev" folder will not be uploaded to the RDS and XNAT.

The reconstructed data contains the final images for CT reconstruction, and it is saved in the "Results" folder of each scan.
Data is uploaded from microCT to RDS daily at 7 p.m.


{{< imgproc acquisition_control_screen Fit "606x488" >}}
Acquisition control screen
{{< /imgproc >}}

The screenshot above is the acquisition control screen. The User field should always leave blank. The Study field should be filled with the XNAT
Project ID and Subject Name in XNAT, e.g. `123_SubjectName`.

Project name can’t contain `_`, this symbol is used to separate the Project ID and Subject Name. Subject Name can contain any numbers of `_`.

The Scan name will become the Session name on XNAT.

Instrument data hierarchy is:

```
Z: (Aquisiton) D: (Reconstruction)

D:\Data\[Study]\[Scan]\*
```

`[Study]` is `[XNAT Project ID]_[Subject]`
`[Scan]` is `[Date]_[Other]`

## Metadata

| Instrument Source | Logic                                              | Config Source  | XNAT Destination |
|-------------------|----------------------------------------------------|----------------|------------------|
| `[Study]`         | `[XNAT Project ID]_*`                              | -              | Subject          |
| `[Study]`         | `*_[Subject]`                                      |                | Subject          |
| `[Scan]`          | -                                                  | -              | Session          |
| -                 | -                                                  | TBD            | `[IID]`          |
| -                 | -                                                  | TBD            | `[QCPID]`        |
| `[Scan]`          | `[Date]_*`                                         | -              | Date             |
| -                 | -                                                  | -              | Time             |
| `[Scan].log`      | `…User: [Operator]…` (Not collecting this for now) | -              | Operator         |
| -                 | -                                                  | TBD            | Scanner Name     |
| -                 | -                                                  | TBD            | Scanner Type     |
| -                 | -                                                  | Sydney Imaging | Acquisition Site |

## Data

| Original structure                       | Note                             | XNAT structure       | XNAT File Type |       |
|------------------------------------------|----------------------------------|----------------------|----------------|-------|
| `[Scan].ct-sequence`                     |                                  | `[Scan].zip`         | uct            | RAW   |
| `[Scan].zipuct`                          |                                  | `[Scan].zip`         | uct            | RAW   |
| `[Scan].mCT`                             |                                  | `[Scan].zip`         | uct            | RAW   |
| `[Scan].parameters`                      |                                  | `[Scan].zip`         | uct            | RAW   |
| `[Scan].log`                             |                                  | `[Scan].zip`         | uct            | RAW   |
| `[Scan].comments`                        |                                  | `[Scan].zip`         | uct            | RAW   |
| `[Scan]_left.png`                        |                                  | `[Scan].zip`         | uct            | RAW   |
| `[Scan]_right.png`                       |                                  | `[Scan].zip`         | uct            | RAW   |
| `[Scan]_top.png`                         |                                  | `[Scan].zip`         | uct            | RAW   |
| `[Scan]_x-ray-left.png`                  |                                  | `[Scan].zip`         | uct            | RAW   |
| `[Scan]_x-ray-right.png`                 |                                  | `[Scan].zip`         | uct            | RAW   |
| `[Scan]_x-ray-top.png`                   |                                  | `[Scan].zip`         | uct            | RAW   |
| `ct-data/calibration/[Stuff].smv`        |                                  |                      | calibration    |       |
| `ct-data/calibration/[stuff2]_dark.tif`  |                                  |                      | calibration    |       |
| `ct-data/calibration/[stuff2]_white.tif` |                                  |                      | calibration    |       |
| `ct-data/calibration/geopar.cfg`         |                                  |                      | calibration    |       |
| `ct-data/proj_000_0_log.csv`             |                                  |                      | proj           |       |
| `ct-data/proj_000_0_00_[NNN].tif`        | where NNN is the index           |                      | proj           |       |
| `Results/CT_[Scan]_80um.log`             | Not maintaining folder structure | `CT_[Scan]_80um.log` | log            | RECON |
| `Results/CT_[Scan]_80um.nii`             | Not maintaining folder structure | `CT_[Scan]_80um.nii` | NIFTI          | RECON |
