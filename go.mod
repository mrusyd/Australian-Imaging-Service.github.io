module docs/docs_root

go 1.12

// We always want to pull in the latest docs from each repository,
// which we do by directing hugo at a local path for each module.
//
// This is also handy for local editing of the documentation,
// however, it also requires all the child repositories to be
// checked out locally.

replace github.com/Australian-Imaging-Service/charts/docs => ../charts/docs
require github.com/Australian-Imaging-Service/charts/docs v0.0.0

replace github.com/Australian-Imaging-Service/pipelines/docs => ../pipelines/docs
require github.com/Australian-Imaging-Service/pipelines/docs v0.0.0

replace github.com/Australian-Imaging-Service/xnatutils/docs => ../xnatutils/docs

require (
	github.com/Australian-Imaging-Service/xnatutils/docs v0.0.0
	github.com/FortAwesome/Font-Awesome v4.7.0+incompatible // indirect
	github.com/twbs/bootstrap v5.1.3+incompatible // indirect
)
