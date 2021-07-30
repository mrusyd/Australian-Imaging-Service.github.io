---
title: Documentation
weight: 10
---

## Previewing documentation locally

* Install Hugo (extended version)

    https://gohugo.io/getting-started/installing/#quick-install

* Install PostCSS

    This is a requirement of [Docsy](https://github.com/google/docsy/blob/master/README.md), the Hugo theme we use.

    ```bash
    sudo npm install -D --save autoprefixer
    sudo npm install -D --save postcss-cli
    ```

* Ensure the main docuemtation repository [Australian-Imaging-Service.github.io](https://github.com/Australian-Imaging-Service/Australian-Imaging-Service.github.io) was cloned with submodules:
    
    ```bash
    git clone --recurse-submodules https://github.com/Australian-Imaging-Service/Australian-Imaging-Service.github.io
    ```

    or by initializing them after a normal clone:

    ```bash
    git submodule update --init 
    ```

* Clone the other AIS repositories containing documentation side by side

    Repositories containing documentation can be referenced from the [`go.mod`](https://github.com/Australian-Imaging-Service/Australian-Imaging-Service.github.io/blob/master/go.mod#L12-L100) file in the `Australian-Imaging-Service.github.io` repository.

    ```bash
    $ tree
    .
    ├── Australian-Imaging-Service.github.io
        [snip]
    ├── charts
        [snip]
    ...
    ```

* Start the live preview within the `Australian-Imaging-Service.github.io` directory

    ```bash
    hugo serve
    ```

    This will start serving the documentation locally at [http://localhost:1313/](http://localhost:1313/)

## Adding and updating AIS documentation

NB: This is for Public facing documents.

All MarkDown documents located under the `docs` folder in the root of their respective repo will be published to a public site at [{{< param baseURL >}}]({{< param baseURL >}}).

If you are adding a new document create a file with a .md extension.

Add a YAML front matter block:

```yaml
---
title: "Title of Page"
weight: 10
---

add your markdown here
```

The front matter YAML will tell Hugo that this is a page to publish and the Title to use in links and page headings.

`weight` affects the placement of the page within the navigation sidebar.

Thats it!

NB: Only documentation within the main branch will be published to the official AIS Charts Pages.
