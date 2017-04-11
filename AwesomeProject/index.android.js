/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import React, { Component } from 'react';
import {
  AppRegistry,
  StyleSheet,
  Text,
  View,
  TouchableHighlight
} from 'react-native'
import FadeInView from './FadeInView'

class MyButton extends Component {
  constructor(props){
    super(props)
    this.state={msg:""}
    this._onPressButton=this._onPressButton.bind(this)
  }
  _onPressButton() {
    //console.log("You tapped the button!");
    this.setState({msg:"you tapped the button"})
  }

  render() {
    return (
      <View>
      <TouchableHighlight onPress={this._onPressButton}>
        <Text>Button</Text>
      </TouchableHighlight>
        <Text>{this.state.msg}</Text>
      </View>
    );
  }
}
export default class AwesomeProject extends Component {
  render() {
    return (
      <FadeInView style={{flex:1, backgroundColor: 'powderblue'}}>
        <Text style={styles.welcome}>
          Welcome to React Native!
        </Text>
        <Text style={styles.instructions}>
          To get started, edit index.android.js
        </Text>
        <Text style={styles.instructions}>
          Hello hjy 123456!
        </Text>
        <Text style={styles.instructions}>
          Double tap R on your keyboard to reload,{'\n'}
          Shake or press menu button for dev menu
        </Text>
        <MyButton />
      </FadeInView>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
});

AppRegistry.registerComponent('AwesomeProject', () => AwesomeProject);
