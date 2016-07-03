THEME_DATA_SCHEMA =  """
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "theme_name": {
        "type": "string",
        "enum" : [
            "merlin-master",
            "dark-cloud"
        ]
    },
    "top_image": {
      "type": "string"
    },
    "background_color": {
      "type": "string",
      "format": "color",
      "default" : "#444444",
      "title": "background color"
    },
    "background_color_alt": {
      "type": "string",
      "format": "color",
      "default" : "#444444",
      "title": "alternative background color"
    },
    "text_color": {
      "type": "string",
      "format": "color",
      "title": "text color",
      "default": "#ffffff"
    },
    "text_color_alt": {
      "type": "string",
      "format": "color",
      "title": "alternative text color",
      "default": "#ffffff"
    },
    "font_family" : {
        "type" : "string",
        "default" : "'Source Sans Pro', sans-serif",
        "enum" : [
            "Arial, Helvetica, sans-serif",
            "'Source Sans Pro', sans-serif",
            "Impact, Charcoal, sans-serif",
            "'Lucida Sans Unicode', 'Lucida Grande', sans-serif",
            "Tahoma, Geneva, sans-serif",
            "'Courier New', Courier, monospace",
            "'Lucida Console', Monaco, monospace"
        ]
    }
  },
  "required": [
    "top_image", "font_family", "theme_name", "background_color", "background_color_alt",
     "text_color", "text_color_alt"
  ]
}
"""
