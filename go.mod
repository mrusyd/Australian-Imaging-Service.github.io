module docs/docs_root

go 1.12

// We always want to pull in the latest docs from each repository,
// which we do by directing hugo at a local path for each module.
//
// This is also handy for local editing of the documentation,
// however, it also requires all the child repositories to be
// checked out locally.
replace github.com/Australian-Imaging-Service/charts/docs => ../charts/docs

require github.com/Australian-Imaging-Service/charts/docs v0.0.0-20210702062413-df2c10ddbcc1
