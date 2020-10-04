import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:quest_creator/shared_widgets/map_widget/map_widget.dart';

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body:  Padding(
        padding: const EdgeInsets.only(left: 10.0,right: 10.0,top: 70.0),
        child: SizedBox(
          width: 350.0,
          height: 300.0,
          child: MapWidget()
        ),
      ),
      bottomNavigationBar: BottomAppBar(
        color: Theme.of(context).primaryColor,
        child: Row(
            children: [
              Padding(
                padding: EdgeInsets.all(20),
                child: Text('To be localized')
              )
            ],
          ),
      ),
    );
  }

}