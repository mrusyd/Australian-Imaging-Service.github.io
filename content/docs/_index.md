
---
title: "Documentation"
linkTitle: "Documentation"
weight: 20
menu:
  main:
    weight: 20
---

## Background

Due to the number of systems and audiences involved, the current documentation 
plan is for the canonical documentation to be within the Github repository, 
using GitHub pages.

This provides a number of easy to use tools and systems to help keep 
standardised, versions and readable documentation.

## Strategy

 - main AIS documentation to be at the top level [https://australian-imaging-service.github.io/](https://australian-imaging-service.github.io/)
 - each repository will self document  
 - using [submodules](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/using-submodules-with-github-pages) the documentation for each repository will be integrated into the main documentation, which link out to the repositories as necessary - see the [repository list](repositories) for examples.


## Documentation

- should be written in Markdown
- should be in a directory called docs in the top level of the repository. We have chosen this methodology as it allows for versioned documentation that matches the code base.
- each repository will need to visit settings, scroll down to the Github Pages section, and make the necessary changes.
- either add themselves to the main site or ask an administrator to add them.

## Local Builds

If you would like to build your documentation locally to test before pushing upstream, the process is documented on the [github site](https://docs.github.com/en/free-pro-team@latest/github/working-with-github-pages/testing-your-github-pages-site-locally-with-jekyll).

I found that the docs weren't sufficient for pre-existing repos. For Ubuntu 20.10 my working process was:

```bash
# Install dependencies
$ apt install ruby-full build-essential zlib1g-dev ruby-all-dev

# set environment variables for non root gem installation
$ echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
$ echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
$ echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
$ source ~/.bashrc

# Install the necessary gems
$ gem install github-pages
$ gem install bundler

# from within the cloned repository, create a Gemfile
$ cd /path/src/ais/Australian-Imaging-Service.github.io/
$ echo "gem 'github-pages', group: :jekyll_plugins" > Gemfile

# build, then start the test server
$ bundle exec jekyll build
$ bundle exec jekyll serve
```


