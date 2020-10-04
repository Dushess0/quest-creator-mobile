import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:quest_creator/screens/home_screen/home_screen.localizations.dart';
import 'package:quest_creator/shared_widgets/map_widget/map_widget.dart';

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: MapWidget(),
      ),
      bottomNavigationBar: BottomAppBar(
        color: Theme.of(context).primaryColor,
        child: Row(
            children: [
              Padding(
                padding: EdgeInsets.all(20),
                child: Text(HomeScreenLocalizations.of(context).exampleMessage)
              )
            ],
          ),
      ),
    );
  }

}