import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:mapbox_gl/mapbox_gl.dart';



class MapWidget extends StatelessWidget {


  static const String ACCESS_TOKEN = "pk.eyJ1IjoiZHVzaGVzcyIsImEiOiJja2VmcWpneHcwc201MnluNzl3ZDRjNDl1In0.sV8IejZBXjXoUbHgRGeN6w";


  @override
  Widget build(BuildContext context) {
    return new Scaffold(
        body: MapboxMap(
          accessToken: ACCESS_TOKEN,
          initialCameraPosition:
          const CameraPosition(target: LatLng(0.0, 0.0)),
        )


       
    );
  }
}