For instructions on writing documents, see the [documentation][1] of the LaTeX+Markdown template.

 [1]: https://github.com/istqborg/istqb_product_base/releases/download/latest/example-document.pdf


To build locally, make sure you have docker installed, and run:

* `docker pull ghcr.io/istqborg/istqb_product_base`
* `docker run --rm -it --platform linux/amd64  -v "$PWD":/mnt  -w /mnt ghcr.io/istqborg/istqb_product_base compile-tex-to-pdf`
 
