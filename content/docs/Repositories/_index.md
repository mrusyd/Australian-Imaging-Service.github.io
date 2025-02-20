---
title: "Top level overview of the AIS repositories"
linkTitle: "Repositories"
weight: 5
---

In each case, we recommend raising issue tickets within the repository in question.

## XNAT-build

This repository builds an XNAT 1.7.6 instance in docker or linux containers (lxd). This is suitable for local deployments.

Code: [xnat-build](https://github.com/australian-imaging-service/xnat-build)

Documentation: [{{< param baseURL >}}/xnat-build]({{< param baseURL >}}/xnat-build)
 
## Charts

This is an alternative deployment process utilising Helm and Kubernetes. This is suitable for cloud deployments.

Code: [charts](https://github.com/australian-imaging-service/charts)

Documentation: [{{< absref "docs" >}}]({{< ref "docs" >}})

## XNATUtils

Xnat-utils is a collection of scripts for conveniently up/downloading and listing data on/from XNAT based on the XnatPy package.

Code: [xnatutils](https://github.com/australian-imaging-service/xnatutils)

Documentation: [{{< param baseURL >}}/xnatutils]({{< param baseURL >}}/xnatutils)

## s3fs-build

A side container to mount Amazon S3 storage in a docker container's filesystem.

Code: [s3fs-build](https://github.com/australian-imaging-service/s3fs-build)

Documentation: [{{< param baseURL >}}/s3fs-build]({{< param baseURL >}}/s3fs-build)

## qc-pipelines

A collection of QA pipelines for assessing quality biomedical images

Code: [qc-pipelines](https://github.com/australian-imaging-service/qc-pipelines)

Documentation: [{{< param baseURL >}}/qc-pipelines]({{< param baseURL >}}/qc-pipelines)

## CTP-build

[Clinical Trials Processor (CTP)](http://mircwiki.rsna.org/index.php?title=MIRC_CTP) is used for processing images from clinical trials. [XNAT utilises CTP](https://wiki.xnat.org/display/XW2/Part+3%3A+Batch+DICOM+Operations+with+CTP+and+XNAT) for anonymisation.

Code: [ctp-build](https://github.com/australian-imaging-service/ctp-build)

Documentation: [{{< param baseURL >}}/CTP-build]({{< param baseURL >}}/CTP-build)

## xnat-openid-auth-plugin

Provides AAF authentication in particular.

Code: [xnat-openid-auth-plugin](https://github.com/australian-imaging-service/xnat-openid-auth-plugin)

Documentation: [{{< param baseURL >}}/xnat-openid-auth-plugin]({{< param baseURL >}}/xnat-openid-auth-plugin)

