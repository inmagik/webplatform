import angular from "angular";
import AppController from "./AppController";
import 'jquery/jquery';
window.$ = $;

import "bootstrap-material-design/dist/js/material.js";

angular.module('webplatformUi', [])
.controller('AppController', AppController);
