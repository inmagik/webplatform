from django import forms
from .models import MiniSite
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from jsoneditor.fields import JSONSchemaFormField
import os
import json


def make_modules_json_schema(cfg):
    modules = cfg.get("modules", [])
    out  = {
        "type" : "array",
        "items" : { "type" : "string", "enum" : modules},
        "uniqueItems": True
    }
    return out


def load_module_config(template_base, schema_path):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    tpl_config = os.path.join(base_dir, "templates_config", schema_path)
    with open(tpl_config) as cfg_file:
        cfg = json.load(cfg_file)
    return cfg


class BaseSiteConfigForm(object):

    def add_helpers(self):
        #super(SiteConfigForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Salva'))
        self.helper.novalidate = True
        self.helper.form_action = ' '

    def get_config(self, instance):
        site_template = self.instance.site_template

        base_dir = os.path.abspath(os.path.dirname(__file__))
        tpl_config = os.path.join(base_dir, "templates_config", site_template+".json")

        with open(tpl_config) as cfg_file:
            cfg = json.load(cfg_file)

        return cfg




class SiteConfigModulesForm(BaseSiteConfigForm, forms.ModelForm) :
    class Meta:
        model = MiniSite
        fields = ['name', 'organization', 'site_template', 'site_config']

    def __init__(self, *args, **kwargs):
        super(SiteConfigModulesForm, self).__init__(*args, **kwargs)
        self.add_helpers()
        cfg = self.get_config(self.instance)
        site_config = self.instance.site_config
        schema = make_modules_json_schema(cfg)
        self.fields["modules"] = JSONSchemaFormField(schema=schema)
        self.initial["modules"] =  site_config.get("modules", [])
        self.fields['site_config'].widget = forms.HiddenInput()

    def clean(self):
        super(SiteConfigModulesForm, self).clean()
        modules = self.cleaned_data.get("modules")
        self.cleaned_data["site_config"]["modules"] = modules



class SiteConfigContentForm(BaseSiteConfigForm, forms.ModelForm) :
    class Meta:
        model = MiniSite
        fields = ['site_content']

    def __init__(self, *args, **kwargs):
        super(SiteConfigContentForm, self).__init__(*args, **kwargs)
        self.add_helpers()
        cfg = self.get_config(self.instance)
        site_config = self.instance.site_config
        site_content = self.instance.site_content
        template_base = self.instance.site_template
        modules =  site_config.get("modules", [])
        self.modules_schemas = {}
        for module in modules:
            modules_config = cfg.get("modules_config", {})
            module_config = modules_config.get(module, {})
            module_schema = module_config.get("schema", None)
            print module_schema
            if module_schema:
                self.modules_schemas[module] = load_module_config(template_base, module_schema)
                self.fields["module_"+module] = JSONSchemaFormField(schema=self.modules_schemas[module])
                self.initial["module_"+module] =  site_content.get(module, {})

        self.fields['site_content'].widget = forms.HiddenInput()


    def clean(self):
        super(SiteConfigContentForm, self).clean()
        print self.cleaned_data
        for module in self.modules_schemas:
            self.cleaned_data["site_content"][module] = self.cleaned_data.get("module_"+module)
        #modules = self.cleaned_data.get("modules")
        #

class SiteConfigStyleForm(BaseSiteConfigForm, forms.ModelForm) :
    class Meta:
        model = MiniSite
        fields = ['site_style']

    def __init__(self, *args, **kwargs):
        super(SiteConfigStyleForm, self).__init__(*args, **kwargs)
        self.add_helpers()
        cfg = self.get_config(self.instance)
        site_config = self.instance.site_config
        site_style = self.instance.site_style
        template_base = self.instance.site_template

        style_config =  cfg.get("styles", {})
        style_schema_path = style_config.get("schema")
        self.style_schema = load_module_config(template_base, style_schema_path)

        self.fields["style"] = JSONSchemaFormField(schema=self.style_schema)
        self.initial["style"] =  site_style

        self.fields['site_style'].widget = forms.HiddenInput()


    def clean(self):
        super(SiteConfigStyleForm, self).clean()
        self.cleaned_data["site_style"] = self.cleaned_data.get("style")
