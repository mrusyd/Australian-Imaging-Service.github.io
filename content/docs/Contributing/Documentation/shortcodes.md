---
title: Shortcodes
weight: 10
---

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
{{</* absref "docs/Repositories" */>}}
```

renders to:

```html
{{< absref "docs/Repositories" >}}
```

### `absrelref`

An extension of the Hugo shortcode `relref` to instead return an absolute URL based on the `baseURL` in `config.toml`.

{{% alert color="primary" %}}
The path is relative to the **current file** in the virtual `content` tree mounted from all repositories.
{{% /alert %}}

```go-html-template
{{</* absrelref "../../Repositories" */>}}
```

renders to:

```html
{{< absrelref "../../Repositories" >}}
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

This is only a subset of the shortcodes available from Docsy, see the [Docsy documentation](https://www.docsy.dev/docs/adding-content/shortcodes/) for more details.

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
