import './App.css';
import React from 'react';
import { Component } from 'react';
import Navbar from './components/NavBar'
import Chart from './components/BarChart';
import GoogleChart from './components/GoogleChart';


class App extends Component {
  constructor(){
    super();
    this.state = {
      arrayToSort : [],
      chartData : {}  
    };
  };
 
  render(){
    return (
      <div className="App">
        <Navbar />
        <GoogleChart id = "myChart" chartData = {this.state.chartData}/>
      </div>
    );
    }
  }
  export default App;


