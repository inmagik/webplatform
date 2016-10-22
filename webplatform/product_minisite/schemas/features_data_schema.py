FEATURES_DATA_SCHEMA =  """
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "title" : "SITE FEATURES",
  "type": "object",
  "properties": {
    "services_heading": {
        "type" : "string",
        "default" : "What we love doing."
    },
    "services_message": {
        "type" : "string",
        "default" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Culpa, alias enim placeat earum quos ab."
    },

    "services": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "icon": {
            "type": "string"
          },
          "title": {
            "type": "string"
          },
          "description": {
            "type": "string"
          }
        },
        "required": [
          "icon",
          "title",
          "description"
        ]
      }
    }
  },
  "required": [

  ]
}"""
