---
title: Integrating a new repository
weight: 10
---

## Setup

1. Copy the `.github` and `docs` folder to the target repository from [skeleton](https://github.com/Australian-Imaging-Service/Australian-Imaging-Service.github.io/tree/master/skeleton)
2. Edit the [gh-pages.yml](https://github.com/Australian-Imaging-Service/Australian-Imaging-Service.github.io/blob/master/.github/workflows/gh-pages.yml) workflow in the main docs repository
    
    Add a new `checkout` step for the repository, replacing **`REPOSITORY_NAME`** with the name of the repository
    
    ```yaml {linenos=table,linenostart=28}
          - name: Checkout REPOSITORY_NAME repo
            uses: actions/checkout@v2
            with:
              repository: 'Australian-Imaging-Service/REPOSITORY_NAME'
              path: REPOSITORY_NAME
    ```
3. Edit the [config.toml](https://github.com/Australian-Imaging-Service/Australian-Imaging-Service.github.io/blob/master/config.toml#L101) file in the [main docs repository](https://github.com/Australian-Imaging-Service/Australian-Imaging-Service.github.io)
    
    Add a new module import section to the end of the file, replacing **`REPOSITORY_NAME`** with the name of the repository
    
    ```toml {linenos=table,linenostart=101}
     [[module.imports]]
        path = "github.com/Australian-Imaging-Service/REPOSITORY_NAME/docs"
        disable = false
    ```
4. Edit the [go.mod](https://github.com/Australian-Imaging-Service/Australian-Imaging-Service.github.io/blob/master/go.mod) file in the [main docs repository](https://github.com/Australian-Imaging-Service/Australian-Imaging-Service.github.io)
    
    Add a reference to the new repository, replacing **`REPOSITORY_NAME`** with the name of the repository
    
    ```mod
    replace github.com/Australian-Imaging-Service/REPOSITORY_NAME/docs => ../REPOSITORY_NAME/docs
    require github.com/Australian-Imaging-Service/REPOSITORY_NAME/docs v0.0.0
    ```

## Troubleshooting

### Error: Parameter token or opts.auth is required

Usually indicative that either:

* The workflow is running in a fork, actions cannot access organisation secrets in a fork
* The repository doesn't have access to the `GITHUBPAGES_KEY` organisation secret
    * Contact the Australian-Imaging-Service organisation admin to request the repository be added
