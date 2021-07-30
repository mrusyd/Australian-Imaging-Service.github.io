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

## Hugo shortcodes

Also see:

* [Hugo documentation on shortcodes](https://gohugo.io/content-management/shortcodes/)
* [Docsy documentation on shortcodes](https://www.docsy.dev/docs/adding-content/shortcodes/)

## Custom shortcodes

### `absref`

An extension of the Hugo shortcode `ref` to instead return an absolute URL based on the `baseURL` in `config.toml`.

{{% alert color="primary" %}}
The path is relative to the virtual `content` directory mounted from all repositories.
{{% /alert %}}

```go-html-template
{{</* absref "docs/charts" */>}}
```

renders to:

```html
{{< absref "docs/charts" >}}
```

### `absrelref`

An extension of the Hugo shortcode `relref` to instead return an absolute URL based on the `baseURL` in `config.toml`.

{{% alert color="primary" %}}
The path is relative to the **current file** in virtual `content` tree mounted from all repositories.
{{% /alert %}}

```go-html-template
{{</* absrelref "../charts" */>}}
```

renders to:

```html
{{< absrelref "../charts" >}}
```

### `code`

Renders a code block with syntax highlighting and a header containing a file name.

```go-html-template
{{</* code yaml "filename.yaml" */>}}
key1: value1
foo: bar
metadata:
  name: lipsum
{{</*/ code */>}}
```

{{< code yaml "filename.yaml" >}}
key1: value1
foo: bar
metadata:
  name: lipsum
{{</ code >}}

### `md`

Renders the markdown in the referenced filepath.

{{% alert color="primary" %}}
The path is relative to the virtual `content` directory mounted from all repositories.
{{% /alert %}}

```go-html-template
{{</* md "docs/_index.md" */>}}
```

### `render`

Renders the contents in the referenced filepath with one of Hugo's [supported content formats](https://gohugo.io/content-management/formats/#list-of-content-formats).

{{% alert color="primary" %}}
The path is relative to the virtual `content` directory mounted from all repositories.
{{% /alert %}}

```go-html-template
{{</* render "path/to/file.rst" "rst" */>}}
```

### `rst`

Renders the Restructured Text in the referenced filepath.

{{% alert color="primary" %}}
The path is relative to the virtual `content` directory mounted from all repositories.
{{% /alert %}}

```go-html-template
{{</* rst "path/to/file.rst" */>}}
```

## Docsy shortcodes

This is only a subset of the shortcodes available from Docsy, see the Docsy documentation for more details.

### `alert`

{{% alert title="Alert title" color="warning" %}}
Alert contents
{{% /alert %}}

```go-html-template
{{%/* alert title="Alert title" color="warning" */%}}
Alert contents
{{%/* /alert */%}}
```

### `pageinfo`

{{% pageinfo color="primary" %}}
Page info content
{{% /pageinfo %}}

```go-html-template
{{%/* pageinfo color="primary" */%}}
Page info content
{{%/* /pageinfo */%}}
```


