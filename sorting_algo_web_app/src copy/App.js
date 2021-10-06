import './App.css';
import React from 'react';
import Navbar from './components/NavBar'
import BarChart from './components/BarChart';
import Button from  './components/Button';

var c1
function App() {
  c1 = <BarChart number="1" />
  return (
    <div className="App">
      <Navbar />
      {c1}
      

    </div>
  );
}

export const UpdateBarChart = (arrayToSort) => {
  console.log('C1 DATA : ')
  console.log(c1.data);
  c1.data.datasets[0].data= arrayToSort;
  c1.update();
  return c1;
}
export default App;
