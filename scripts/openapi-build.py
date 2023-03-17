"""
Usage:

    python openapi-to-html.py --input-file /path/to/api.yaml \
      --output-dir some/path \
      --output-name api

This will generate two files

* `some/path/api.html`
* `some/path/api.json`

"""

import argparse
import json
import pathlib
import sys
import yaml

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Vic.AI OpenAPI Documentation</title>
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.18.1/swagger-ui.css" >
  <style>
    html {
        box-sizing: border-box;
        overflow: -moz-scrollbars-vertical;
        overflow-y: scroll;
    }

    *,
    *:before,
    *:after {
        box-sizing: inherit;
    }

    body {
        margin: 0;
        background: #fafafa;
    }
  </style>
</head>
<body>

<div id="swagger-ui"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.18.1/swagger-ui-bundle.js"> </script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.18.1/swagger-ui-standalone-preset.js"> </script>
<script>
window.onload = function() {

  var spec = %s;

  // Build a system
  const ui = SwaggerUIBundle({
    spec: spec,
    dom_id: '#swagger-ui',
    deepLinking: true,
    presets: [
      SwaggerUIBundle.presets.apis,
      SwaggerUIStandalonePreset
    ],
    plugins: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
    layout: "StandaloneLayout"
  })

  window.ui = ui
}
</script>
</body>

</html>
"""


parser = argparse.ArgumentParser(description="Generates a static OpenAPI page.")
parser.add_argument("--input-file", help="The path to the yaml file")
parser.add_argument("--output-dir", help="The path to the output dir")
parser.add_argument("--output-name", help="The name of the output file without extension")
args = parser.parse_args()

# Make the output directory if it doesn exist `mkdir -p`
pathlib.Path(f"{args.output_dir}").mkdir(parents=True, exist_ok=True)

# Read the yaml and render the output files
with open(args.input_file) as input_file:
  spec = yaml.load(input_file, Loader=yaml.FullLoader)

  output_html = f"{args.output_dir}/{args.output_name}.html"
  output_json = f"{args.output_dir}/{args.output_name}.json"

  with open(output_html, "w") as fd:
    fd.write(TEMPLATE % json.dumps(spec))

  with open(output_json, "w") as fd:
    fd.write(json.dumps(spec))
